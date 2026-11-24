---
title: https://developer.android.com/agents/skills/profilers/android-profiler/references/perfetto/setup
url: https://developer.android.com/agents/skills/profilers/android-profiler/references/perfetto/setup
source: md.txt
---

> **Prerequisite:** Ensure `$SKILL_ROOT` is initialized per
> `$SKILL_ROOT/references/env_setup.md`.

## Put the bundled `trace_processor` on the `PATH`

**`trace_processor`** is bundled at
`$SKILL_ROOT/references/perfetto/bin/trace_processor`:

```bash
# some installs lose the exec bit
chmod +x "$SKILL_ROOT/references/perfetto/bin/trace_processor"
export PATH="$SKILL_ROOT/references/perfetto/bin:$PATH"
trace_processor --version                     # smoke test
```

- If each command runs in a fresh shell, repeat the `export` lines in that command.
- The first invocation downloads the prebuilt binary for the host platform into `~/.local/share/perfetto/prebuilts/` and caches it.
- Do not download `trace_processor` separately: the wrapper is pinned to the release the skill was built for.
- On Windows skip the `PATH` step and run `python "$SKILL_ROOT/references/perfetto/bin/trace_processor" ...`.
- If the environment **explicitly** mandates its own `trace_processor` (Google internal, OEM build environments, CI images), prefer that setup.
- The querying guidelines in `$SKILL_ROOT/references/perfetto/sql.md` target the `trace_processor` wrapper shipped with this skill. Only if subcommands, tables, or modules that `sql.md` documents are rejected as unknown in the preferred setup, check `--help` for supported options and find tables using `LIMIT 0` and the stdlib docs. Do **not** export the trace to SQLite or query using `sqlite3`: it is slower and loses the Perfetto standard library.