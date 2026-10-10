#!/system/bin/sh
# FixHUA M0 read-only device evidence probe.
# Writes only to OUTPUT_DIR supplied by the user. It never writes Android settings,
# procfs/sysfs/cgroups, kernel parameters, package state, or boot configuration.
set -u
OUT="${1:-./fixhua-snapshot}"
mkdir -p "$OUT" || exit 2
STATUS="$OUT/command_status.tsv"
: > "$STATUS"
record_cmd() { name="$1"; shift; target="$OUT/$name.txt"; if "$@" >"$target" 2>"$target.err"; then printf '%s\tOK\n' "$name" >> "$STATUS"; else rc=$?; [ -s "$target" ] || : > "$target"; printf '%s\tERROR:%s\n' "$name" "$rc" >> "$STATUS"; fi; }
record_file() { name="$1"; src="$2"; target="$OUT/$name.txt"; if [ -r "$src" ]; then if cat "$src" > "$target" 2>"$target.err"; then printf '%s\tOK\n' "$name" >> "$STATUS"; else printf '%s\tERROR\n' "$name" >> "$STATUS"; fi; else : > "$target"; printf '%s\tMISSING_OR_DENIED\n' "$name" >> "$STATUS"; fi; }
record_cmd props getprop
record_cmd uname uname -a
record_file proc_meminfo /proc/meminfo
record_file pressure_memory /proc/pressure/memory
record_file pressure_cpu /proc/pressure/cpu
record_file pressure_io /proc/pressure/io
record_file vmstat /proc/vmstat
record_file loadavg /proc/loadavg
if command -v dumpsys >/dev/null 2>&1; then record_cmd thermalservice dumpsys thermalservice; record_cmd meminfo_system dumpsys meminfo system; else : > "$OUT/thermalservice.txt"; printf 'thermalservice\tMISSING\n' >> "$STATUS"; : > "$OUT/meminfo_system.txt"; printf 'meminfo_system\tMISSING\n' >> "$STATUS"; fi
NOW="$(date -u '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || date)"
{ printf '{"schemaVersion":1,"createdUtc":"%s","files":[' "$NOW"; first=1; while IFS='\t' read -r name status; do [ -n "$name" ] || continue; case "$status" in OK) js="OK";; MISSING*) js="MISSING";; *DENIED*) js="DENIED";; *) js="ERROR";; esac; [ "$first" -eq 1 ] || printf ','; first=0; printf '{"name":"%s","status":"%s","source":"%s.txt"}' "$name" "$js" "$name"; done < "$STATUS"; printf ']}\n'; } > "$OUT/manifest.json"
printf 'FixHUA snapshot written to %s\n' "$OUT"
