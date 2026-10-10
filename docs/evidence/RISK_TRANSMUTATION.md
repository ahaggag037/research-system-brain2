# Risk-Transmutation Catalog

## RT-001 — Root kernel/system tuning
- **Raw idea:** continuously tune scheduler/memory/cgroup/sysfs controls for performance.
- **Benefit:** potentially large control reach.
- **Hazard:** device-specific semantics, controller conflict, thermal/battery/stability regressions, persistence risk.
- **Bounded redesign:** root is read-mostly first; any write is a typed actuator qualified per device/firmware with one-at-a-time canary, verification and rollback.
- **Required observations:** actual path/owner/semantics, before/after user-visible metric, controller overwrite behavior, thermal/stability response.
- **Abort:** no rollback, repeated overwrite, unstable effect, safety interaction.
- **Shortest falsification:** E-005 on one reversible candidate after E-001.
- **Disposition:** RESEARCH-ONLY until qualification.

## RT-002 — Keep high-value apps warm
- **Raw idea:** pin/protect user-important apps so they never reload.
- **Benefit:** better resume latency.
- **Hazard:** worsens pressure/thrashing and harms foreground work; platform may legitimately reclaim them.
- **Bounded redesign:** shadow-only continuity value estimates; never “pin everything”; prioritize diagnosis and user intent, and only consider bounded actions if pressure/outcome evidence supports them.
- **Abort:** foreground jank/pressure rises, background semantics break, benefit not attributable.
- **Experiment:** replay/controlled app-switch traces before any destructive behavior.
- **Disposition:** EXPERIMENTAL CMP-010.

## RT-003 — Freeze cached apps
- **Raw idea:** freeze background apps to save resources.
- **Benefit:** reduce CPU/wakeup while keeping processes resident.
- **Hazard:** freezing does **not** free their resident memory and can break expected background behavior if applied arbitrarily.
- **Bounded redesign:** observe platform freezer state where available; do not use manual freezer as a memory-pressure cure. Any future use requires app-role safeguards and E-005.
- **Disposition:** DEFERRED/RESEARCH-ONLY.

## RT-004 — Deep continuous tracing
- **Raw idea:** collect Perfetto/system traces continuously for perfect diagnosis.
- **Benefit:** rich evidence.
- **Hazard:** CPU/wakeup/storage/self-interference and privacy.
- **Bounded redesign:** low-cost ring buffer plus short user/triggered deep capture with explicit overhead measurement.
- **Abort:** E-002 exceeds device-derived observer budget.
- **Disposition:** SELECTED only in bounded two-speed form.

## RT-005 — Automatic Huawei setting repair
- **Raw idea:** root-edit hidden vendor state so apps always stay alive.
- **Benefit:** convenience.
- **Hazard:** undocumented schema/version drift, security/behavior breakage, false attribution.
- **Bounded redesign:** settings assessment + documented intent/deep-link/user guidance first; programmable mutation only through documented stable APIs if discovered.
- **Disposition:** SAFE ASSISTANT selected; hidden-store edit rejected.
