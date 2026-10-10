# Failure and Recovery Matrix

| Failure | Detection | User-visible effect | Automatic response | Rollback / degraded mode | Human action | Recovery verification |
|---|---|---|---|---|---|---|
| Missing privilege | broker/request denied | some diagnostics unavailable | continue APP-only | mark UNOBSERVABLE; no write | optionally enable explicit read session | capability rescan |
| Missing device capability | probe absent/unsupported | feature unavailable | remove dependent probe/action | fallback evidence or UNKNOWN | none unless firmware docs needed | DeviceProfile assertion |
| Stale capability/config | firmware fingerprint mismatch/schema mismatch | temporary limited mode | invalidate affected qualifications; migrate/re-scan | read-only/no-op | none normally | new profile + migration tests |
| Invalid/corrupt local state | checksum/parse/DB transaction failure | history/settings may be unavailable | quarantine bad state | conservative defaults; never preserve inferred qualification | optionally export corruption report | clean reopen + consistency check |
| Failed intervention | postcondition false/command error | action reports failure | abort | typed rollback | none unless recovery unresolved | control read-back + health window |
| Partial intervention | multi-step actuator journal incomplete | critical warning | stop all write actions | rollback completed steps in reverse | user may reboot if contract specifies | known baseline restored |
| Privileged helper crash | heartbeat/session closes | privileged session lost | no blind restart during transaction | timeout/rollback owner handles pending transaction; otherwise read-only | re-enable session explicitly | helper handshake + no pending journal |
| App/UI crash | process death | UI closes | OS restart/user reopen | controller helper must not depend on UI to finish rollback | reopen app | audit journal clean |
| Reboot during work | boot fingerprint/session change | session interrupted | invalidate session | no boot-time reapply; next start rescan | reopen app | no pending write, new profile valid |
| Thermal/stability regression | thermal state/jank/crash worsens beyond canary guard | warning/action stopped | abort actuator | rollback + suspend qualification | inspect report | post-rollback stability window |
| Controller fight | repeated read-back reversal/oscillation | action unavailable | suspend actuator | restore baseline where owned | none | no further oscillation |
| Incompatible firmware change | fingerprint/version change | previously qualified actions disabled | invalidate qualification | observation-only | rerun qualification experiment | E-005 passes on new firmware |
| Failed app update | startup/migration/build incompatibility | cannot enter normal mode | fail closed | restore compatible data backup when available | reinstall known build if necessary | version/state integrity check |
| Sensitive export risk | preview detects identifiers/sensitive fields | export blocked/warned | redact by default | source remains local | explicit opt-in only when appropriate | output schema/redaction test |
