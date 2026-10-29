---
title: https://developer.android.com/agents/skills/profilers/android-profiler/recording/workflows/perfetto-trace-recording/references/example-configs/java_heap_dump.pftxt.rawcontent
url: https://developer.android.com/agents/skills/profilers/android-profiler/recording/workflows/perfetto-trace-recording/references/example-configs/java_heap_dump.pftxt.rawcontent
source: md.txt
---

    # Java heap dump (retention graph) of one app. Prefer the java_heap_dump
    # helper script for a standalone dump; use this config when combining a heap
    # dump with other data sources in one trace.
    # Replace com.example.myapp with the app's package name.
    buffers {
      size_kb: 102400
    }
    duration_ms: 30000

    data_sources {
      config {
        name: "android.java_hprof"
        java_hprof_config {
          process_cmdline: "com.example.myapp"
        }
      }
    }

    # Heap dumps can be large; stream to the output file instead of relying on
    # the in-memory buffer alone.
    write_into_file: true