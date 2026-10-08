---
title: https://developer.android.com/agents/skills/profilers/android-profiler/recording/workflows/perfetto-trace-recording/references/example-configs/native_heap.pftxt.rawcontent
url: https://developer.android.com/agents/skills/profilers/android-profiler/recording/workflows/perfetto-trace-recording/references/example-configs/native_heap.pftxt.rawcontent
source: md.txt
---

    # Native (C/C++) heap profiling via heapprofd: sampled malloc/free callstacks
    # for one app. Prefer the heap_profile helper script for a standalone profile;
    # use this config when combining with other data sources.
    # Replace com.example.myapp with the app's package name.
    buffers {
      size_kb: 65536
    }
    duration_ms: 30000

    data_sources {
      config {
        name: "android.heapprofd"
        heapprofd_config {
          sampling_interval_bytes: 4096
          process_cmdline: "com.example.myapp"
          # To profile ART/JNI and custom allocators too, add: all_heaps: true
        }
      }
    }

    write_into_file: true