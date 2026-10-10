#!/system/bin/sh
# FixHUA M0.2 read-only device evidence probe (Arm B research-expanded).
# Writes only to OUTPUT_DIR supplied by the user. It never writes Android settings,
# procfs/sysfs/cgroups, kernel parameters, package state, MemoryLimiter state, or boot configuration.
set -u
OUT="${1:-./fixhua-snapshot}"
mkdir -p "$OUT" || exit 2
STATUS="$OUT/command_status.tsv"
: > "$STATUS"
record_cmd() { name="$1"; shift; target="$OUT/$name.txt"; if "$@" >"$target" 2>"$target.err"; then printf '%s\tOK\n' "$name" >> "$STATUS"; else rc=$?; [ -s "$target" ] || : > "$target"; printf '%s\tERROR:%s\n' "$name" "$rc" >> "$STATUS"; fi; }
record_file() { name="$1"; src="$2"; target="$OUT/$name.txt"; if [ -r "$src" ]; then if cat "$src" > "$target" 2>"$target.err"; then printf '%s\tOK\n' "$name" >> "$STATUS"; else printf '%s\tERROR\n' "$name" >> "$STATUS"; fi; else : > "$target"; printf '%s\tMISSING_OR_DENIED\n' "$name" >> "$STATUS"; fi; }
record_missing() { name="$1"; : > "$OUT/$name.txt"; printf '%s\tMISSING\n' "$name" >> "$STATUS"; }

record_cmd props getprop
record_cmd uname uname -a
record_file proc_meminfo /proc/meminfo
record_file proc_swaps /proc/swaps
record_file pressure_memory /proc/pressure/memory
record_file pressure_cpu /proc/pressure/cpu
record_file pressure_io /proc/pressure/io
record_file vmstat /proc/vmstat
record_file loadavg /proc/loadavg
record_file cgroup_controllers /sys/fs/cgroup/cgroup.controllers
record_file mglru_enabled /sys/kernel/mm/lru_gen/enabled
if command -v am >/dev/null 2>&1; then record_cmd memory_limiter_status am memory-limiter status; else record_missing memory_limiter_status; fi
if command -v perfetto >/dev/null 2>&1; then record_cmd perfetto_version perfetto --version; else record_missing perfetto_version; fi
if command -v dumpsys >/dev/null 2>&1; then
  record_cmd thermalservice dumpsys thermalservice
  record_cmd meminfo_system dumpsys meminfo system
else
  record_missing thermalservice
  record_missing meminfo_system
fi
NOW="$(date -u '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || date)"
{ printf '{"schemaVersion":1,"probeVersion":"M0.2-ArmB","createdUtc":"%s","files":[' "$NOW"; TAB="$(printf '\t')"; first=1; while IFS="$TAB" read -r name status; do [ -n "$name" ] || continue; case "$status" in OK) js="OK";; MISSING*) js="MISSING";; *DENIED*) js="DENIED";; *) js="ERROR";; esac; [ "$first" -eq 1 ] || printf ','; first=0; printf '{"name":"%s","status":"%s","source":"%s.txt"}' "$name" "$js" "$name"; done < "$STATUS"; printf ']}\n'; } > "$OUT/manifest.json"
printf 'FixHUA snapshot written to %s\n' "$OUT"
