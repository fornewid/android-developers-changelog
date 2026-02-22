---
title: https://developer.android.com/studio/profile/chart-glossary/process-memory
url: https://developer.android.com/studio/profile/chart-glossary/process-memory
source: md.txt
---

# Process Memory (RSS)

For apps deployed to devices running Android 9 or higher, the**Process Memory (RSS)**section shows the amount of physical memory in use by the app.

![](https://developer.android.com/static/studio/images/profile/system-trace-process-memory.png)

**Figure 1.**Viewing physical memory in the profiler.

Here is what the rows in the**Process Memory (RSS)**section mean:

- **Total** : This is the total amount of*physical*memory in use by your process. On Unix-based systems, this is known as the "Resident Set Size", and is the combination of all the memory used by anonymous allocations, file mappings, and shared memory allocations.

  For Windows developers, Resident Set Size is analogous to the Working Set Size.
- **Allocated** : This counter tracks how much physical memory is currently used by the process's normal memory allocations. These are allocations which are anonymous (not backed by a specific file) and private (not shared). In most applications, these are made up of heap allocations (with`malloc`or`new`) and stack memory. When swapped out from physical memory, these allocations are written to the system swap file.

- **File Mappings**: This counter tracks the amount of physical memory the process is using for file mappings---that is, memory mapped from files into a region of memory by the memory manager.

- **Shared**: This counter tracks how much physical memory is being used to share memory between this process and other processes in the system.