---
title: https://developer.android.com/agents/skills/profilers/perfetto-sql/references/perfetto-stdlib-docs
url: https://developer.android.com/agents/skills/profilers/perfetto-sql/references/perfetto-stdlib-docs
source: md.txt
---

*This page documents the PerfettoSQL standard library.*

## Introduction

The PerfettoSQL standard library is a repository of tables, views, functions
and macros, contributed by domain experts, which make querying traces easier.
Its design is heavily inspired by standard libraries in languages like Python,
C++ and Java.

Some of the purposes of the standard library include:

1. Acting as a way of sharing and commonly written queries without needing to copy/paste large amounts of SQL.
2. Raising the abstraction level when exposing data in the trace. Many modules in the standard library convert low-level trace concepts e.g. slices, tracks and into concepts developers may be more familar with e.g. for Android developers: app startups, binder transactions etc.

Standard library modules can be included as follows:

\`-- Include all tables/views/functions from the android.startup.startups
-- module in the standard library.
INCLUDE PERFETTO MODULE android.startup.startups;

-- Use the android_startups table defined in the android.startup.startups
-- module.
SELECT \*
FROM android_startups;\`Prelude is a special module is automatically included. It contains key helper
tables, views and functions which are universally useful.

More information on importing modules is available in the
[syntax documentation](https://perfetto.dev/docs/analysis/perfetto-sql-syntax#including-perfettosql-modules)
for the `INCLUDE PERFETTO MODULE` statement.

## Package: prelude

### prelude

#### Views/Tables

**perf_sample**

VIEW
Samples from the traced_perf profiler.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this perf sample. |
| ts | TIMESTAMP | Timestamp of the sample. |
| utid | JOINID(thread.id) | Sampled thread. |
| cpu | LONG | Core the sampled thread was running on. |
| cpu_mode | STRING | Execution state (userspace/kernelspace) of the sampled thread. |
| callsite_id | JOINID(stack_profile_callsite.id) | If set, unwound callstack of the sampled thread. |
| unwind_error | STRING | If set, indicates that the unwinding for this sample encountered an error. Such samples still reference the best-effort result via the callsite_id, with a synthetic error frame at the point where unwinding stopped. |
| perf_session_id | JOINID(perf_session.id) | Distinguishes samples from different profiling streams (i.e. multiple data sources). |

**counter**

VIEW
Counters are values put into tracks during parsing of the trace.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique id of a counter value |
| ts | TIMESTAMP | Time of fetching the counter value. |
| track_id | JOINID(track.id) | Track this counter value belongs to. |
| value | DOUBLE | Value. |
| arg_set_id | ARGSETID | Additional information about the counter value. |

**slice**

VIEW
Contains slices from userspace which explains what threads were doing
during the trace.

| Column | Type | Description |
|---|---|---|
| id | ID | The id of the slice. |
| ts | TIMESTAMP | The timestamp at the start of the slice in nanoseconds. The actual value depends on the `primary_trace_clock` selected in TraceConfig. This is often the value of a monotonic counter since device boot so is only meaningful in the context of a trace. |
| dur | DURATION | The duration of the slice in nanoseconds. |
| track_id | JOINID(track.id) | The id of the track this slice is located on. |
| category | STRING | The "category" of the slice. If this slice originated with track_event, this column contains the category emitted. Otherwise, it is likely to be null (with limited exceptions). |
| name | STRING | The name of the slice. The name describes what was happening during the slice. |
| depth | LONG | The depth of the slice in the current stack of slices. |
| parent_id | JOINID(slice.id) | The id of the parent (i.e. immediate ancestor) slice for this slice. |
| arg_set_id | ARGSETID | The id of the argument set associated with this slice. |
| thread_ts | TIMESTAMP | The thread timestamp at the start of the slice. This column will only be populated if thread timestamp collection is enabled with track_event. |
| thread_dur | DURATION | The thread time used by this slice. This column will only be populated if thread timestamp collection is enabled with track_event. |
| thread_instruction_count | LONG | The value of the CPU instruction counter at the start of the slice. This column will only be populated if thread instruction collection is enabled with track_event. |
| thread_instruction_delta | LONG | The change in value of the CPU instruction counter between the start and end of the slice. This column will only be populated if thread instruction collection is enabled with track_event. |
| cat | STRING | Alias of `category`. |
| slice_id | JOINID(slice.id) | Alias of `id`. |

**instant**

VIEW
Contains instant events from userspace which indicates what happened at a
single moment in time.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | The timestamp of the instant. |
| track_id | JOINID(track.id) | The id of the track this instant is located on. |
| name | STRING | The name of the instant. The name describes what happened during the instant. |
| arg_set_id | ARGSETID | The id of the argument set associated with this instant. |

**slices**

VIEW
Alternative alias of table `slice`.

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Alias of `slice.id`. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | ARGSETID | Alias of `slice.arg_set_id`. |
| thread_ts | TIMESTAMP | Alias of `slice.thread_ts`. |
| thread_dur | DURATION | Alias of `slice.thread_dur`. |
| thread_instruction_count | LONG | Alias of `slice.thread_instruction_count`. |
| thread_instruction_delta | LONG | Alias of `slice.thread_instruction_delta`. |
| cat | STRING | Alias of `slice.cat`. |
| slice_id | JOINID(slice.id) | Alias of `slice.slice_id`. |

**thread**

VIEW
Contains information of threads seen during the trace.

| Column | Type | Description |
|---|---|---|
| id | ID | The id of the thread. Prefer using `utid` instead. |
| utid | ID | Unique thread id. This is != the OS tid. This is a monotonic number associated to each thread. The OS thread id (tid) cannot be used as primary key because tids and pids are recycled by most kernels. |
| tid | LONG | The OS id for this thread. Note: this is *not* unique over the lifetime of the trace so cannot be used as a primary key. Use |
| name | STRING | The name of the thread. Can be populated from many sources (e.g. ftrace, /proc scraping, track event etc). |
| start_ts | TIMESTAMP | The start timestamp of this thread (if known). Is null in most cases unless a thread creation event is enabled (e.g. task_newtask ftrace event on Linux/Android). |
| end_ts | TIMESTAMP | The end timestamp of this thread (if known). Is null in most cases unless a thread destruction event is enabled (e.g. sched_process_free ftrace event on Linux/Android). |
| upid | JOINID(process.id) | The process hosting this thread. |
| is_main_thread | BOOL | Boolean indicating if this thread is the main thread in the process. |
| is_idle | BOOL | Boolean indicating if this thread is a kernel idle thread. |
| machine_id | LONG | Machine identifier, non-null for threads on a remote machine. |
| arg_set_id | ARGSETID | Extra args for this thread. |

**process**

VIEW
Contains information of processes seen during the trace.

| Column | Type | Description |
|---|---|---|
| id | ID | The id of the process. Prefer using `upid` instead. |
| upid | JOINID(process.id) | Unique process id. This is != the OS pid. This is a monotonic number associated to each process. The OS process id (pid) cannot be used as primary key because tids and pids are recycled by most kernels. |
| pid | LONG | The OS id for this process. Note: this is *not* unique over the lifetime of the trace so cannot be used as a primary key. Use |
| name | STRING | The name of the process. Can be populated from many sources (e.g. ftrace, /proc scraping, track event etc). |
| start_ts | TIMESTAMP | The start timestamp of this process (if known). Is null in most cases unless a process creation event is enabled (e.g. task_newtask ftrace event on Linux/Android). |
| end_ts | TIMESTAMP | The end timestamp of this process (if known). Is null in most cases unless a process destruction event is enabled (e.g. sched_process_free ftrace event on Linux/Android). |
| parent_upid | JOINID(process.id) | The upid of the process which caused this process to be spawned. |
| uid | LONG | The Unix user id of the process. |
| android_appid | LONG | Android appid of this process. |
| android_user_id | LONG | Android user id of this process. |
| cmdline | STRING | /proc/cmdline for this process. |
| arg_set_id | ARGSETID | Extra args for this process. |
| machine_id | LONG | Machine identifier, non-null for processes on a remote machine. |

**args**

VIEW
Arbitrary key-value pairs which allow adding metadata to other, strongly
typed tables.
Note: for a given row, only one of \|int_value\|, \|string_value\|, \|real_value\|
will be non-null.

| Column | Type | Description |
|---|---|---|
| id | ID | The id of the arg. |
| arg_set_id | ARGSETID | The id for a single set of arguments. |
| flat_key | STRING | The "flat key" of the arg: this is the key without any array indexes. |
| key | STRING | The key for the arg. |
| int_value | LONG | The integer value of the arg. |
| string_value | STRING | The string value of the arg. |
| real_value | DOUBLE | The double value of the arg. |
| value_type | STRING | The type of the value of the arg. Will be one of 'int', 'uint', 'string', 'real', 'pointer', 'bool' or 'json'. |
| display_value | STRING | The human-readable formatted value of the arg. |

**perf_session**

VIEW
Contains the Linux perf sessions in the trace.

| Column | Type | Description |
|---|---|---|
| id | LONG | The id of the perf session. Prefer using `perf_session_id` instead. |
| perf_session_id | LONG | The id of the perf session. |
| cmdline | STRING | Command line used to collect the data. |

**android_logs**

VIEW
Log entries from Android logcat.

NOTE: this table is not sorted by timestamp.

| Column | Type | Description |
|---|---|---|
| id | ID | Which row in the table the log corresponds to. |
| ts | TIMESTAMP | Timestamp of log entry. |
| utid | JOINID(thread.id) | Thread writing the log entry. |
| prio | LONG | Priority of the log. 3=DEBUG, 4=INFO, 5=WARN, 6=ERROR. |
| tag | STRING | Tag of the log entry. |
| msg | STRING | Content of the log entry |

**track**

VIEW
Tracks are a fundamental concept in trace processor and represent a
"timeline" for events of the same type and with the same context. See
<https://perfetto.dev/docs/analysis/trace-processor#tracks> for a more
detailed explanation, with examples.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this track. Identical to |
| name | STRING | Name of the track; can be null for some types of tracks (e.g. thread tracks). |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| dimension_arg_set_id | ARGSETID | The dimensions of the track which uniquely identify the track within a given `type`. Join with the `args` table or use the `EXTRACT_ARG` helper function to expand the args. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Generic key-value pairs containing extra information about the track. Join with the `args` table or use the `EXTRACT_ARG` helper function to expand the args. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| track_group_id | LONG | An opaque key indicating that this track belongs to a group of tracks which are "conceptually" the same track. Tracks in trace processor don't allow overlapping events to allow for easy analysis (i.e. SQL window functions, SPAN JOIN and other similar operators). However, in visualization settings (e.g. the UI), the distinction doesn't matter and all tracks with the same `track_group_id` should be merged together into a single logical "UI track". |

**thread_track**

TABLE
Tracks which are associated to a single thread.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this thread track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| utid | JOINID(thread.id) | The utid that the track is associated with. |

**process_track**

TABLE
Tracks which are associated to a single process.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this process track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| upid | JOINID(process.id) | The upid that the track is associated with. |

**cpu_track**

TABLE
Tracks which are associated to a single CPU.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this cpu track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| cpu | LONG | The CPU that the track is associated with. |

**gpu_track**

TABLE
Table containing tracks which are loosely tied to a GPU.

NOTE: this table is deprecated due to inconsistency of it's design with
other track tables (e.g. not having a GPU column, mixing a bunch of different
tracks which are barely related). Please use the track table directly
instead.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this cpu track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| dimension_arg_set_id | ARGSETID | The dimensions of the track which uniquely identify the track within a given type. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| scope | STRING | The source of the track. Deprecated. |
| description | STRING | The description for the track. |
| context_id | LONG | The context id for the GPU this track is associated to. |

**ftrace_event**

VIEW
Contains all the ftrace events in the trace. This table exists only for
debugging purposes and should not be relied on in production usecases (i.e.
metrics, standard library etc). Note also that this table might be empty if
raw ftrace parsing has been disabled.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this ftrace event. |
| ts | TIMESTAMP | The timestamp of this event. |
| name | STRING | The ftrace event name. |
| cpu | LONG | The CPU this event was emitted on (meaningful only in single machine traces). For multi-machine, join with the `cpu` table on `ucpu` to get the CPU identifier of each machine. |
| utid | JOINID(thread.id) | The thread this event was emitted on. |
| arg_set_id | ARGSETID | The set of key/value pairs associated with this event. |
| common_flags | LONG | Ftrace event flags for this event. Currently only emitted for sched_waking events. |
| ucpu | LONG | The unique CPU identifier that this event was emitted on. |

**raw**

VIEW
This table is deprecated. Use `ftrace_event` instead which contains the same
rows; this table is simply a (badly named) alias.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this raw event. |
| ts | TIMESTAMP | The timestamp of this event. |
| name | STRING | The name of the event. For ftrace events, this will be the ftrace event name. |
| cpu | LONG | The CPU this event was emitted on (meaningful only in single machine traces). For multi-machine, join with the `cpu` table on `ucpu` to get the CPU identifier of each machine. |
| utid | JOINID(thread.id) | The thread this event was emitted on. |
| arg_set_id | ARGSETID | The set of key/value pairs associated with this event. |
| common_flags | LONG | Ftrace event flags for this event. Currently only emitted for sched_waking events. |
| ucpu | LONG | The unique CPU identifier that this event was emitted on. |

**frame_slice**

VIEW
Table containing graphics frame events on Android.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Alias of `slice.id`. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(frame_slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | LONG | Alias of `slice.arg_set_id`. |
| layer_name | STRING | Name of the graphics layer this slice happened on. |
| frame_number | LONG | The frame number this slice is associated with. |
| queue_to_acquire_time | LONG | The time between queue and acquire for this buffer and layer. |
| acquire_to_latch_time | LONG | The time between acquire and latch for this buffer and layer. |
| latch_to_present_time | LONG | The time between latch and present for this buffer and layer. |

**gpu_slice**

VIEW
Table containing graphics frame events on Android.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Alias of `slice.id`. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(frame_slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | LONG | Alias of `slice.arg_set_id`. |
| context_id | LONG | Context ID. |
| render_target | LONG | Render target ID. |
| render_target_name | STRING | The name of the render target. |
| render_pass | LONG | Render pass ID. |
| render_pass_name | STRING | The name of the render pass. |
| command_buffer | LONG | The command buffer ID. |
| command_buffer_name | STRING | The name of the command buffer. |
| frame_id | LONG | Frame id. |
| submission_id | LONG | The submission id. |
| hw_queue_id | LONG | The hardware queue id. |
| upid | JOINID(process.id) | The id of the process. |
| render_subpasses | STRING | Render subpasses. |

**expected_frame_timeline_slice**

TABLE
This table contains information on the expected timeline of either a display
frame or a surface frame.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Alias of `slice.id`. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(frame_slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | LONG | Alias of `slice.arg_set_id`. |
| display_frame_token | LONG | Display frame token (vsync id). |
| surface_frame_token | LONG | Surface frame token (vsync id), null if this is a display frame. |
| upid | JOINID(process.id) | Unique process id of the app that generates the surface frame. |
| layer_name | STRING | Layer name if this is a surface frame. |

**actual_frame_timeline_slice**

TABLE
This table contains information on the actual timeline and additional
analysis related to the performance of either a display frame or a surface
frame.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Alias of `slice.id`. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(frame_slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | LONG | Alias of `slice.arg_set_id`. |
| display_frame_token | LONG | Display frame token (vsync id). |
| upid | JOINID(process.id) | Surface frame token (vsync id), null if this is a display frame. |
| surface_frame_token | LONG | Unique process id of the app that generates the surface frame. |
| layer_name | STRING | Layer name if this is a surface frame. |
| present_type | STRING | Frame's present type (eg. on time / early / late). |
| on_time_finish | LONG | Whether the frame finishes on time. |
| gpu_composition | LONG | Whether the frame used gpu composition. |
| jank_type | STRING | Specify the jank types for this frame if there's jank, or none if no jank occurred. |
| jank_severity_type | STRING | Severity of the jank: none if no jank. |
| prediction_type | STRING | Frame's prediction type (eg. valid / expired). |
| jank_tag | STRING | Jank tag based on jank type, used for slice visualization. |
| jank_tag_experimental | STRING | Jank tag (experimental) based on jank type, used for slice visualization. |

**heap_graph_class**

VIEW
Stores class information within ART heap graphs. It represents Java/Kotlin
classes that exist in the heap, including their names, inheritance
relationships, and loading context.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this heap graph class. |
| name | STRING | (potentially obfuscated) name of the class. |
| deobfuscated_name | STRING | If class name was obfuscated and deobfuscation map for it provided, the deobfuscated name. |
| location | STRING | the APK / Dex / JAR file the class is contained in. |
| superclass_id | JOINID(heap_graph_class.id) | The superclass of this class. |
| classloader_id | LONG | The classloader that loaded this class. |
| kind | STRING | The kind of class. |

**heap_graph_object**

VIEW
The objects on the Dalvik heap.

All rows with the same (upid, graph_sample_ts) are one dump.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this heap graph object. |
| upid | JOINID(process.id) | Unique PID of the target. |
| graph_sample_ts | TIMESTAMP | Timestamp this dump was taken at. |
| self_size | LONG | Size this object uses on the Java Heap. |
| native_size | LONG | Approximate amount of native memory used by this object, as reported by libcore.util.NativeAllocationRegistry.size. |
| reference_set_id | JOINID(heap_graph_reference.reference_set_id) | Join key with heap_graph_reference containing all objects referred in this object's fields. |
| reachable | BOOL | Bool whether this object is reachable from a GC root. If false, this object is uncollected garbage. |
| heap_type | STRING | The type of ART heap this object is stored on (app, zygote, boot image) |
| type_id | JOINID(heap_graph_class.id) | Class this object is an instance of. |
| root_type | STRING | If not NULL, this object is a GC root. |
| root_distance | LONG | Distance from the root object. |

**heap_graph_reference**

VIEW
Many-to-many mapping between heap_graph_object.

This associates the object with given reference_set_id with the objects
that are referred to by its fields.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this heap graph reference. |
| reference_set_id | JOINID(heap_graph_object.reference_set_id) | Join key to heap_graph_object reference_set_id. |
| owner_id | JOINID(heap_graph_object.id) | Id of object that has this reference_set_id. |
| owned_id | JOINID(heap_graph_object.id) | Id of object that is referred to. |
| field_name | STRING | The field that refers to the object. E.g. Foo.name. |
| field_type_name | STRING | The static type of the field. E.g. java.lang.String. |
| deobfuscated_field_name | STRING | The deobfuscated name, if field_name was obfuscated and a deobfuscation mapping was provided for it. |

**memory_snapshot**

VIEW
Table with memory snapshots.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this snapshot. |
| timestamp | TIMESTAMP | Time of the snapshot. |
| track_id | JOINID(track.id) | Track of this snapshot. |
| detail_level | STRING | Detail level of this snapshot. |

**process_memory_snapshot**

VIEW
Table with process memory snapshots.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this snapshot. |
| snapshot_id | JOINID(memory_snapshot.id) | Snapshot ID for this snapshot. |
| upid | JOINID(process.id) | Process for this snapshot. |

**memory_snapshot_node**

VIEW
Table with memory snapshot nodes.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this node. |
| process_snapshot_id | JOINID(process_memory_snapshot.id) | Process snapshot ID for to this node. |
| parent_node_id | JOINID(memory_snapshot_node.id) | Parent node for this node, optional. |
| path | STRING | Path for this node. |
| size | LONG | Size of the memory allocated to this node. |
| effective_size | LONG | Effective size used by this node. |
| arg_set_id | ARGSETID | Additional args of the node. |

**memory_snapshot_edge**

VIEW

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this edge. |
| source_node_id | JOINID(memory_snapshot_node.id) | Source node for this edge. |
| target_node_id | JOINID(memory_snapshot_node.id) | Target node for this edge. |
| importance | LONG | Importance for this edge. |

**counter_track**

VIEW
Tracks containing counter-like events.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this cpu counter track. |
| name | STRING | Name of the track. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| dimension_arg_set_id | ARGSETID | The dimensions of the track which uniquely identify the track within a given type. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| unit | STRING | The units of the counter. This column is rarely filled. |
| description | STRING | The description for this track. For debugging purposes only. |

**cpu_counter_track**

TABLE
Tracks containing counter-like events associated to a CPU.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this cpu counter track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| unit | STRING | The units of the counter. This column is rarely filled. |
| description | STRING | The description for this track. For debugging purposes only. |
| cpu | LONG | The CPU that the track is associated with. |

**gpu_counter_track**

TABLE
Tracks containing counter-like events associated to a GPU.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this gpu counter track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| unit | STRING | The units of the counter. This column is rarely filled. |
| description | STRING | The description for this track. For debugging purposes only. |
| gpu_id | LONG | The GPU that the track is associated with. |

**process_counter_track**

TABLE
Tracks containing counter-like events associated to a process.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this process counter track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| unit | STRING | The units of the counter. This column is rarely filled. |
| description | STRING | The description for this track. For debugging purposes only. |
| upid | LONG | The upid of the process that the track is associated with. |

**thread_counter_track**

TABLE
Tracks containing counter-like events associated to a thread.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this thread counter track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | JOINID(track.id) | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| unit | STRING | The units of the counter. This column is rarely filled. |
| description | STRING | The description for this track. For debugging purposes only. |
| utid | LONG | The utid of the thread that the track is associated with. |

**perf_counter_track**

TABLE
Tracks containing counter-like events collected from Linux perf.

| Column | Type | Description |
|---|---|---|
| id | ID(track.id) | Unique identifier for this thread counter track. |
| name | STRING | Name of the track. |
| type | STRING | The type of a track indicates the type of data the track contains. Every track is uniquely identified by the the combination of the type and a set of dimensions: type allow identifying a set of tracks with the same type of data within the whole universe of tracks while dimensions allow distinguishing between different tracks in that set. |
| parent_id | JOINID(track.id) | The track which is the "parent" of this track. Only non-null for tracks created using Perfetto's track_event API. |
| source_arg_set_id | ARGSETID | Args for this track which store information about "source" of this track in the trace. For example: whether this track orginated from atrace, Chrome tracepoints etc. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| unit | STRING | The units of the counter. This column is rarely filled. |
| description | STRING | The description for this track. For debugging purposes only. |
| perf_session_id | LONG | The id of the perf session this counter was captured on. |
| cpu | LONG | The CPU the counter is associated with. Can be null if the counter is not associated with any CPU. |
| is_timebase | BOOL | Whether this counter is the sampling timebase for the session. |

**counters**

VIEW
Alias of the `counter` table.

| Column | Type | Description |
|---|---|---|
| id | ID | Alias of `counter.id`. |
| ts | TIMESTAMP | Alias of `counter.ts`. |
| track_id | JOINID(track.id) | Alias of `counter.track_id`. |
| value | DOUBLE | Alias of `counter.value`. |
| arg_set_id | LONG | Alias of `counter.arg_set_id`. |
| name | STRING | Legacy column, should no longer be used. |
| unit | STRING | Legacy column, should no longer be used. |

**cpu**

VIEW
Contains information about the CPUs on the device this trace was taken on.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this CPU. Identical to |
| ucpu | ID | Unique identifier for this CPU. Isn't equal to |
| cpu | LONG | The 0-based CPU core identifier. |
| cluster_id | LONG | The cluster id is shared by CPUs in the same cluster. |
| processor | STRING | A string describing this core. |
| machine_id | LONG | Machine identifier, non-null for CPUs on a remote machine. |
| capacity | LONG | Capacity of a CPU of a device, a metric which indicates the relative performance of a CPU on a device For details see: <https://www.kernel.org/doc/Documentation/devicetree/bindings/arm/cpu-capacity.txt> |
| arg_set_id | ARGSETID | Extra key/value pairs associated with this cpu. |

**cpu_available_frequencies**

VIEW
Contains the frequency values that the CPUs on the device are capable of
running at.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this cpu frequency. |
| cpu | LONG | The CPU for this frequency, meaningful only in single machine traces. For multi-machine, join with the `cpu` table on `ucpu` to get the CPU identifier of each machine. |
| freq | LONG | CPU frequency in KHz. |
| ucpu | LONG | The CPU that the slice executed on (meaningful only in single machine traces). For multi-machine, join with the `cpu` table on `ucpu` to get the CPU identifier of each machine. |

**sched**

VIEW
Contains scheduling slices with kernel thread scheduling information.
These slices are collected when the Linux "ftrace" data source is used with
the "sched/switch" and "sched/wakeup\*" events enabled.

The rows in this view will always have a matching row in the \|thread_state\|
table with \|thread_state.state\| = 'Running'

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this scheduling slice. |
| ts | TIMESTAMP | The timestamp at the start of the slice. |
| dur | DURATION | The duration of the slice. |
| cpu | LONG | The CPU that the slice executed on (meaningful only in single machine traces). For multi-machine, join with the `cpu` table on `ucpu` to get the CPU identifier of each machine. |
| utid | JOINID(thread.id) | The thread's unique id in the trace. |
| end_state | STRING | A string representing the scheduling state of the kernel thread at the end of the slice. The individual characters in the string mean the following: R (runnable), S (awaiting a wakeup), D (in an uninterruptible sleep), T (suspended), t (being traced), X (exiting), P (parked), W (waking), I (idle), N (not contributing to the load average), K (wakeable on fatal signals) and Z (zombie, awaiting cleanup). |
| priority | LONG | The kernel priority that the thread ran at. |
| ucpu | LONG | The unique CPU identifier that the slice executed on. |
| ts_end | LONG | Legacy column, should no longer be used. |

**sched_slice**

VIEW
Alias of `sched`. Prefer using `sched` instead.

| Column | Type | Description |
|---|---|---|
| id | ID | Alias of `sched.id`. |
| ts | TIMESTAMP | Alias of `sched.ts`. |
| dur | DURATION | Alias of `sched.dur`. |
| cpu | LONG | Alias of `sched.cpu`. |
| utid | JOINID(thread.id) | Alias of `sched.utid`. |
| end_state | STRING | Alias of `sched.end_state`. |
| priority | LONG | Alias of `sched.priority`. |
| ucpu | LONG | Alias of `sched.ucpu`. |

**thread_state**

VIEW
This table contains the scheduling state of every thread on the system during
the trace.

The rows in this table which have \|state\| = 'Running', will have a
corresponding row in the \|sched_slice\| table.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for this thread state. |
| ts | TIMESTAMP | The timestamp at the start of the slice. |
| dur | DURATION | The duration of the slice. |
| cpu | LONG | The CPU that the thread executed on (meaningful only in single machine traces). For multi-machine, join with the `cpu` table on `ucpu` to get the CPU identifier of each machine. |
| utid | JOINID(thread.id) | The thread's unique id in the trace. |
| state | STRING | The scheduling state of the thread. Can be "Running" or any of the states described in |
| io_wait | LONG | Indicates whether this thread was blocked on IO. |
| blocked_function | STRING | The function in the kernel this thread was blocked on. |
| waker_utid | JOINID(thread.id) | The unique thread id of the thread which caused a wakeup of this thread. |
| waker_id | JOINID(thread_state.id) | The unique thread state id which caused a wakeup of this thread. |
| irq_context | LONG | Whether the wakeup was from interrupt context or process context. |
| ucpu | LONG | The unique CPU identifier that the thread executed on. |

**trace_metrics**

VIEW
Lists all metrics built-into trace processor.

| Column | Type | Description |
|---|---|---|
| name | STRING | The name of the metric. |

**trace_bounds**

VIEW
Definition of `trace_bounds` table. The values are being filled by Trace
Processor when parsing the trace.
It is recommended to depend on the `trace_start()` and `trace_end()`
functions rather than directly on `trace_bounds`.

| Column | Type | Description |
|---|---|---|
| start_ts | TIMESTAMP | First ts in the trace. |
| end_ts | TIMESTAMP | End of the trace. |

#### Functions

**trace_start**

Fetch start of the trace.
Returns TIMESTAMP: Start of the trace.

**trace_end**

Fetch end of the trace.
Returns TIMESTAMP: End of the trace.

**trace_dur**

Fetch duration of the trace.
Returns DURATION: Duration of the trace.

**slice_is_ancestor**

Given two slice ids, returns whether the first is an ancestor of the second.
Returns BOOL: Whether `ancestor_id` slice is an ancestor of `descendant_id`.

| Argument | Type | Description |
|---|---|---|
| ancestor_id | LONG | Id of the potential ancestor slice. |
| descendant_id | LONG | Id of the potential descendant slice. |

#### Macros

**cast_int**

Casts \|value\| to INT.
Returns: Expr,

| Argument | Type | Description |
|---|---|---|
| value | Expr | Query or subquery that will be cast. |

**cast_double**

Casts \|value\| to DOUBLE.
Returns: Expr,

| Argument | Type | Description |
|---|---|---|
| value | Expr | Query or subquery that will be cast. |

**cast_string**

Casts \|value\| to STRING.
Returns: Expr,

| Argument | Type | Description |
|---|---|---|
| value | Expr | Query or subquery that will be cast. |

## Package: chrome

### chrome.android_input

#### Views/Tables

**chrome_deliver_android_input_event**

TABLE
DeliverInputEvent is the third step in the input pipeline.
It is responsible for routing the input events within browser process.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Touch move processing duration. |
| utid | LONG | Utid. |
| android_input_id | STRING | Input id (assigned by the system, used by InputReader and InputDispatcher) |

**chrome_android_input**

TABLE
Collects information about input reader, input dispatcher and
DeliverInputEvent steps for the given Android input id.

| Column | Type | Description |
|---|---|---|
| android_input_id | STRING | Input id. |
| input_reader_processing_start_ts | TIMESTAMP | Input reader step start timestamp. |
| input_reader_processing_end_ts | TIMESTAMP | Input reader step end timestamp. |
| input_reader_utid | LONG | Input reader step utid. |
| input_dispatcher_processing_start_ts | TIMESTAMP | Input dispatcher step start timestamp. |
| input_dispatcher_processing_end_ts | TIMESTAMP | Input dispatcher step end timestamp. |
| input_dispatcher_utid | LONG | Input dispatcher step utid. |
| deliver_input_event_start_ts | TIMESTAMP | DeliverInputEvent step start timestamp. |
| deliver_input_event_end_ts | TIMESTAMP | DeliverInputEvent step end timestamp. |
| deliver_input_event_utid | LONG | DeliverInputEvent step utid. |

### chrome.chrome_scrolls

#### Views/Tables

**chrome_scroll_update_refs**

TABLE
Ties together input (`LatencyInfo.Flow`) and frame (`Graphics.Pipeline`)
trace events. Only covers input events of the `GESTURE_SCROLL_UPDATE_EVENT`
type.

| Column | Type | Description |
|---|---|---|
| scroll_update_latency_id | LONG | Id of the Chrome input pipeline (`LatencyInfo.Flow`). |
| touch_move_latency_id | LONG | Id of the touch move input corresponding to this scroll update. |
| presentation_latency_id | LONG | Id of the `EventLatency` of the frame that the input was presented in. |
| surface_frame_id | LONG | Id of the frame pipeline (`Graphics.Pipeline`), pre-surface aggregation. |
| display_trace_id | LONG | Id of the frame pipeline (`Graphics.Pipeline`), post-surface aggregation. |

**chrome_scroll_update_input_pipeline**

TABLE
Timestamps and durations for the input-associated (before coalescing inputs
into a frame) stages of a scroll.

| Column | Type | Description |
|---|---|---|
| id | LONG | Id of the `LatencyInfo.Flow` slices corresponding to this scroll event. |
| scroll_id | LONG | Id of the scroll this scroll update belongs to. |
| presented_in_frame_id | LONG | Id of the frame that this input was presented in. Can be joined with `chrome_scroll_update_frame_pipeline.id`. |
| is_presented | BOOL | Whether this input event was presented. |
| is_janky | BOOL | Whether the corresponding frame is janky based on the Event.ScrollJank.DelayedFramesPercentage.FixedWindow metric. This comes directly from `perfetto.protos.EventLatency.is_janky_scrolled_frame`. |
| is_inertial | BOOL | Whether the corresponding scroll is inertial (fling). If this is `true`, "generation" and "touch_move" related timestamps and durations will be null. |
| is_first_scroll_update_in_scroll | BOOL | Whether this is the first update in a scroll. First scroll update can never be janky. |
| is_first_scroll_update_in_frame | BOOL | Whether this is the first input that was presented in frame `presented_in_frame_id`. |
| generation_ts | TIMESTAMP | Input generation timestamp (from the Android system). |
| input_reader_processing_end_ts | TIMESTAMP | End timestamp for the InputReader step (see android_input.sql). Only populated when atrace 'input' category is enabled. |
| input_dispatcher_processing_end_ts | TIMESTAMP | End timestamp for the InputDispatcher step (see android_input.sql). Only populated when atrace 'input' category is enabled. |
| generation_to_browser_main_dur | DURATION | Duration from input generation to when the browser received the input. |
| browser_utid | LONG | Utid for the browser main thread. |
| touch_move_received_slice_id | LONG | Slice id for the `STEP_SEND_INPUT_EVENT_UI` slice for the touch move. |
| touch_move_received_ts | TIMESTAMP | Timestamp for the `STEP_SEND_INPUT_EVENT_UI` slice for the touch move. |
| touch_move_processing_dur | DURATION | Duration for processing a `TouchMove` event. |
| scroll_update_created_slice_id | LONG | Slice id for the `STEP_SEND_INPUT_EVENT_UI` slice for the gesture scroll. |
| scroll_update_created_ts | TIMESTAMP | Timestamp for the `STEP_SEND_INPUT_EVENT_UI` slice for the gesture scroll. |
| scroll_update_processing_dur | DURATION | Duration for creating a `GestureScrollUpdate` from a `TouchMove` event. |
| scroll_update_created_end_ts | TIMESTAMP | End timestamp for the `STEP_SEND_INPUT_EVENT_UI` slice for the above. |
| browser_to_compositor_delay_dur | DURATION | Duration between the browser and compositor dispatch. |
| compositor_utid | LONG | Utid for the renderer compositor thread. |
| compositor_dispatch_slice_id | LONG | Slice id for the `STEP_HANDLE_INPUT_EVENT_IMPL` slice. |
| compositor_dispatch_ts | TIMESTAMP | Timestamp for the `STEP_HANDLE_INPUT_EVENT_IMPL` slice or the containing task (if available). |
| compositor_dispatch_dur | DURATION | Duration for the compositor dispatch itself. |
| compositor_dispatch_end_ts | TIMESTAMP | End timestamp for the `STEP_HANDLE_INPUT_EVENT_IMPL` slice. |
| compositor_dispatch_to_coalesced_input_handled_dur | DURATION | Duration between compositor dispatch and coalescing input. |
| compositor_coalesced_input_handled_slice_id | LONG | Slice id for the `STEP_DID_HANDLE_INPUT_AND_OVERSCROLL` slice. |
| compositor_coalesced_input_handled_ts | TIMESTAMP | Timestamp for the `STEP_DID_HANDLE_INPUT_AND_OVERSCROLL` slice. |
| compositor_coalesced_input_handled_dur | DURATION | Duration for the `STEP_DID_HANDLE_INPUT_AND_OVERSCROLL` slice. |
| compositor_coalesced_input_handled_end_ts | TIMESTAMP | End timestamp for the `STEP_DID_HANDLE_INPUT_AND_OVERSCROLL` slice. |

**chrome_scroll_update_frame_pipeline**

TABLE
Timestamps and durations for the frame-associated (after coalescing inputs
into a frame) stages of a scroll.

| Column | Type | Description |
|---|---|---|
| id | LONG | Id of the `LatencyInfo.Flow` slices corresponding to this scroll event. |
| display_trace_id | LONG | Id of the aggregated frame this scroll update was presented in. |
| vsync_interval_ms | DOUBLE | Vsync interval (in milliseconds). |
| compositor_resample_slice_id | LONG | Slice id for the `STEP_RESAMPLE_SCROLL_EVENTS` slice. |
| compositor_resample_ts | TIMESTAMP | Timestamp for the `STEP_RESAMPLE_SCROLL_EVENTS` slice. |
| compositor_receive_begin_frame_ts | TIMESTAMP | Timestamp for the `STEP_RECEIVE_BEGIN_FRAME` slice or the containing task (if available). |
| compositor_generate_compositor_frame_slice_id | LONG | Slice id for the `STEP_GENERATE_COMPOSITOR_FRAME` slice. |
| compositor_generate_compositor_frame_ts | TIMESTAMP | Timestamp for the `STEP_GENERATE_COMPOSITOR_FRAME` slice or the containing task (if available). |
| compositor_generate_frame_to_submit_frame_dur | DURATION | Duration between generating and submitting the compositor frame. |
| compositor_submit_compositor_frame_slice_id | LONG | Slice id for the `STEP_SUBMIT_COMPOSITOR_FRAME` slice. |
| compositor_submit_compositor_frame_ts | TIMESTAMP | Timestamp for the `STEP_SUBMIT_COMPOSITOR_FRAME` slice. |
| compositor_submit_frame_dur | DURATION | Duration for submitting the compositor frame (to viz). |
| compositor_submit_compositor_frame_end_ts | TIMESTAMP | End timestamp for the `STEP_SUBMIT_COMPOSITOR_FRAME` slice. |
| compositor_to_viz_delay_dur | DURATION | Delay when a compositor frame is sent from the renderer to viz. |
| viz_compositor_utid | LONG | Utid for the viz compositor thread. |
| viz_receive_compositor_frame_slice_id | LONG | Slice id for the `STEP_RECEIVE_COMPOSITOR_FRAME` slice. |
| viz_receive_compositor_frame_ts | TIMESTAMP | Timestamp for the `STEP_RECEIVE_COMPOSITOR_FRAME` slice or the containing task (if available). |
| viz_receive_compositor_frame_dur | DURATION | Duration of the viz work done on receiving the compositor frame. |
| viz_receive_compositor_frame_end_ts | TIMESTAMP | End timestamp for the `STEP_RECEIVE_COMPOSITOR_FRAME` slice. |
| viz_wait_for_draw_dur | DURATION | Duration between viz receiving the compositor frame to frame draw. |
| viz_draw_and_swap_slice_id | LONG | Slice id for the `STEP_DRAW_AND_SWAP` slice. |
| viz_draw_and_swap_ts | TIMESTAMP | Timestamp for the `STEP_DRAW_AND_SWAP` slice or the containing task (if available). |
| viz_draw_and_swap_dur | DURATION | Duration for the viz drawing/swapping work for this frame. |
| viz_send_buffer_swap_slice_id | LONG | Slice id for the `STEP_SEND_BUFFER_SWAP` slice. |
| viz_send_buffer_swap_end_ts | TIMESTAMP | End timestamp for the `STEP_SEND_BUFFER_SWAP` slice. |
| viz_to_gpu_delay_dur | DURATION | Delay between viz work on compositor thread and `CompositorGpuThread`. |
| viz_gpu_thread_utid | LONG | Utid for the viz `CompositorGpuThread`. |
| viz_swap_buffers_slice_id | LONG | Slice id for the `STEP_BUFFER_SWAP_POST_SUBMIT` slice. |
| viz_swap_buffers_ts | TIMESTAMP | Timestamp for the `STEP_BUFFER_SWAP_POST_SUBMIT` slice or the containing task (if available). |
| viz_swap_buffers_dur | DURATION | Duration of frame buffer swapping work on viz. |
| viz_swap_buffers_end_ts | TIMESTAMP | End timestamp for the `STEP_BUFFER_SWAP_POST_SUBMIT` slice. |
| viz_swap_buffers_to_latch_dur | DURATION | Duration of `EventLatency`'s `BufferReadyToLatch` step. |
| latch_timestamp | TIMESTAMP | Timestamp for `EventLatency`'s `LatchToSwapEnd` step. |
| viz_latch_to_presentation_dur | DURATION | Duration of either `EventLatency`'s `LatchToSwapEnd` + `SwapEndToPresentationCompositorFrame` steps or its `LatchToPresentation` step. |
| presentation_timestamp | TIMESTAMP | Presentation timestamp for the frame. |

**chrome_scrolls**

TABLE
Defines slices for all of the individual scrolls in a trace based on the
LatencyInfo-based scroll definition.

NOTE: this view of top level scrolls is based on the LatencyInfo definition
of a scroll, which differs subtly from the definition based on
EventLatencies.
TODO(b/278684408): add support for tracking scrolls across multiple Chrome/
WebView instances. Currently gesture_scroll_id unique within an instance, but
is not unique across multiple instances. Switching to an EventLatency based
definition of scrolls should resolve this.

| Column | Type | Description |
|---|---|---|
| id | LONG | The unique identifier of the scroll. |
| ts | TIMESTAMP | The start timestamp of the scroll. |
| dur | DURATION | The duration of the scroll. |
| gesture_scroll_begin_ts | TIMESTAMP | The earliest timestamp of the EventLatency slice of the GESTURE_SCROLL_BEGIN type for the corresponding scroll id. |
| gesture_scroll_end_ts | TIMESTAMP | The earliest timestamp of the EventLatency slice of the GESTURE_SCROLL_END type / the latest timestamp of the EventLatency slice of the GESTURE_SCROLL_UPDATE type for the corresponding scroll id. |

**chrome_scroll_update_info**

TABLE
Timestamps and durations for the critical path stages during scrolling.
This table covers both the input-associated (before coalescing inputs into a
frame) and frame-associated (after coalescing inputs into a frame) stages of
a scroll:

`...
|
+---+---+
| |
V V` +---+ +---+
\| *scroll_update_INPUT* \| \| *scroll_update_FRAME* \|
\| timestamps_and_metadata \| \| timestamps_and_metadata \|
+---+---+ +---+---+
\| \|
V V
+---+ +---+
\| chrome_scroll*update* \| \| chrome_scroll*update* \|
\| INPUT_pipeline \| \| FRAME_pipeline \|
+---+---+ +---+---+
\| \|
+---+---+
\|
V
+---+
\| chrome_scroll_update_info \|
+---+

| Column | Type | Description |
|---|---|---|
| id | LONG | Id of the `LatencyInfo.Flow` slices corresponding to this scroll event. |
| scroll_id | LONG | Id of the scroll this scroll update belongs to. |
| previous_input_id | LONG | Id (`LatencyInfo.ID`) of the previous input in this scroll. |
| frame_display_id | LONG | Id (`display_trace_id`) of the aggregated frame which this scroll update was presented in. |
| vsync_interval_ms | DOUBLE | Vsync interval (in milliseconds). |
| is_presented | BOOL | Whether this input event was presented. |
| is_janky | BOOL | Whether the corresponding frame is janky based on the Event.ScrollJank.DelayedFramesPercentage.FixedWindow metric. This comes directly from `perfetto.protos.EventLatency.is_janky_scrolled_frame`. |
| is_inertial | BOOL | Whether the corresponding scroll is inertial (fling). If this is `true`, "generation" and "touch_move" related timestamps and durations will be null. |
| is_first_scroll_update_in_scroll | BOOL | Whether this is the first update in a scroll. First scroll update can never be janky. |
| is_first_scroll_update_in_frame | BOOL | Whether this is the first input that was presented in the frame. |
| browser_uptime_dur | DURATION | Duration from the start of the browser process to the first input generation timestamp. |
| generation_ts | TIMESTAMP | Input generation timestamp (from the Android system). |
| input_reader_dur | DURATION | Duration from the generation timestamp to the end of InputReader's work. Only populated when atrace 'input' category is enabled. |
| input_dispatcher_dur | DURATION | Duration of InputDispatcher's work. Only populated when atrace 'input' category is enabled. |
| since_previous_generation_dur | DURATION | Duration from the generation timestamp for the previous input to this input's generation timestamp. |
| generation_to_browser_main_dur | DURATION | Duration from input generation to when the browser received the input. |
| browser_utid | LONG | Utid for the browser main thread. |
| touch_move_received_slice_id | LONG | Slice id for the `STEP_SEND_INPUT_EVENT_UI` slice for the touch move. |
| touch_move_received_ts | TIMESTAMP | Timestamp for the `STEP_SEND_INPUT_EVENT_UI` slice for the touch move. |
| touch_move_processing_dur | DURATION | Duration for processing a `TouchMove` event. |
| scroll_update_created_slice_id | LONG | Slice id for the `STEP_SEND_INPUT_EVENT_UI` slice for the gesture scroll. |
| scroll_update_created_ts | TIMESTAMP | Timestamp for the `STEP_SEND_INPUT_EVENT_UI` slice for the gesture scroll. |
| scroll_update_processing_dur | DURATION | Duration for creating a `GestureScrollUpdate` from a `TouchMove` event. |
| scroll_update_created_end_ts | TIMESTAMP | End timestamp for the `STEP_SEND_INPUT_EVENT_UI` slice for the above. |
| browser_to_compositor_delay_dur | DURATION | Duration between the browser and compositor dispatch. |
| compositor_utid | LONG | Utid for the renderer compositor thread. |
| compositor_dispatch_slice_id | LONG | Slice id for the `STEP_HANDLE_INPUT_EVENT_IMPL` slice. |
| compositor_dispatch_ts | TIMESTAMP | Timestamp for the `STEP_HANDLE_INPUT_EVENT_IMPL` slice or the containing task (if available). |
| compositor_dispatch_dur | DURATION | Duration for the compositor dispatch itself. |
| compositor_dispatch_end_ts | TIMESTAMP | End timestamp for the `STEP_HANDLE_INPUT_EVENT_IMPL` slice. |
| compositor_dispatch_to_on_begin_frame_delay_dur | DURATION | Duration between compositor dispatch and input resampling work. |
| compositor_resample_slice_id | LONG | Slice id for the `STEP_RESAMPLE_SCROLL_EVENTS` slice. |
| compositor_coalesced_input_handled_slice_id | LONG | Slice id for the `STEP_DID_HANDLE_INPUT_AND_OVERSCROLL` slice. |
| compositor_on_begin_frame_ts | TIMESTAMP | Start timestamp for work done on the input during "OnBeginFrame". |
| compositor_on_begin_frame_dur | DURATION | Duration of the "OnBeginFrame" work for this input. |
| compositor_on_begin_frame_end_ts | TIMESTAMP | End timestamp for work done on the input during "OnBeginFrame". |
| compositor_on_begin_frame_to_generation_delay_dur | DURATION | Delay until the compositor work for generating the frame begins. |
| compositor_generate_compositor_frame_slice_id | LONG | Slice id for the `STEP_GENERATE_COMPOSITOR_FRAME` slice. |
| compositor_generate_compositor_frame_ts | TIMESTAMP | Timestamp for the `STEP_GENERATE_COMPOSITOR_FRAME` slice or the containing task (if available). |
| compositor_generate_frame_to_submit_frame_dur | DURATION | Duration between generating and submitting the compositor frame. |
| compositor_submit_compositor_frame_slice_id | LONG | Slice id for the `STEP_SUBMIT_COMPOSITOR_FRAME` slice. |
| compositor_submit_compositor_frame_ts | TIMESTAMP | Timestamp for the `STEP_SUBMIT_COMPOSITOR_FRAME` slice. |
| compositor_submit_frame_dur | DURATION | Duration for submitting the compositor frame (to viz). |
| compositor_submit_compositor_frame_end_ts | TIMESTAMP | End timestamp for the `STEP_SUBMIT_COMPOSITOR_FRAME` slice. |
| compositor_to_viz_delay_dur | DURATION | Delay when a compositor frame is sent from the renderer to viz. |
| viz_compositor_utid | LONG | Utid for the viz compositor thread. |
| viz_receive_compositor_frame_slice_id | LONG | Slice id for the `STEP_RECEIVE_COMPOSITOR_FRAME` slice. |
| viz_receive_compositor_frame_ts | TIMESTAMP | Timestamp for the `STEP_RECEIVE_COMPOSITOR_FRAME` slice or the containing task (if available). |
| viz_receive_compositor_frame_dur | DURATION | Duration of the viz work done on receiving the compositor frame. |
| viz_receive_compositor_frame_end_ts | TIMESTAMP | End timestamp for the `STEP_RECEIVE_COMPOSITOR_FRAME` slice. |
| viz_wait_for_draw_dur | DURATION | Duration between viz receiving the compositor frame to frame draw. |
| viz_draw_and_swap_slice_id | LONG | Slice id for the `STEP_DRAW_AND_SWAP` slice. |
| viz_draw_and_swap_ts | TIMESTAMP | Timestamp for the `STEP_DRAW_AND_SWAP` slice or the containing task (if available). |
| viz_draw_and_swap_dur | DURATION | Duration for the viz drawing/swapping work for this frame. |
| viz_send_buffer_swap_slice_id | LONG | Slice id for the `STEP_SEND_BUFFER_SWAP` slice. |
| viz_send_buffer_swap_end_ts | TIMESTAMP | End timestamp for the `STEP_SEND_BUFFER_SWAP` slice. |
| viz_to_gpu_delay_dur | DURATION | Delay between viz work on compositor thread and `CompositorGpuThread`. |
| viz_gpu_thread_utid | LONG | Utid for the viz `CompositorGpuThread`. |
| viz_swap_buffers_slice_id | LONG | Slice id for the `STEP_BUFFER_SWAP_POST_SUBMIT` slice. |
| viz_swap_buffers_ts | TIMESTAMP | Timestamp for the `STEP_BUFFER_SWAP_POST_SUBMIT` slice or the containing task (if available). |
| viz_swap_buffers_dur | DURATION | Duration of frame buffer swapping work on viz. |
| viz_swap_buffers_end_ts | TIMESTAMP | End timestamp for the `STEP_BUFFER_SWAP_POST_SUBMIT` slice. |
| viz_swap_buffers_to_latch_dur | DURATION | Duration of `EventLatency`'s `BufferReadyToLatch` step. |
| latch_timestamp | TIMESTAMP | Timestamp for `EventLatency`'s `LatchToSwapEnd` step. |
| viz_latch_to_presentation_dur | DURATION | Duration of either `EventLatency`'s `LatchToSwapEnd` + `SwapEndToPresentationCompositorFrame` steps or its `LatchToPresentation` step. |
| presentation_timestamp | TIMESTAMP | Presentation timestamp for the frame. |

**chrome_scroll_frame_info**

TABLE
A list of all presented Chrome frames which contain scroll updates and associated
metadata.

| Column | Type | Description |
|---|---|---|
| id | LONG | Id (frame's display_trace_id) for the given frame. |
| scroll_id | LONG | Id of the scroll this scroll update belongs to. |
| last_input_before_this_frame_id | LONG | Id (LatencyInfo.ID) of the last input before this frame. |
| vsync_interval_ms | DOUBLE | Vsync interval (in milliseconds). TODO(b/394303662): Remove in favour of `vsync_interval_dur`. |
| vsync_interval_dur | DURATION | Vsync interval (in nanoseconds). |
| is_janky | BOOL | Whether the corresponding frame is janky based on the Event.ScrollJank.DelayedFramesPercentage.FixedWindow metric. This comes directly from `perfetto.protos.EventLatency.is_janky_scrolled_frame`. |
| is_inertial | BOOL | Whether the corresponding scroll is inertial (fling). |
| total_input_delta_y | DOUBLE | Sum of all input deltas for all scroll updates in this frame. These values are based on the delta of the OS input events. |
| presented_scrolled_delta_y | DOUBLE | Presented delta (change in page offset) for the given frame. This delta is computed by Chrome (based on the input events). |
| browser_uptime_dur | DURATION | Duration from the start of the browser process to the first input generation timestamp. |
| first_input_generation_ts | TIMESTAMP | Input generation timestamp (from the Android system) for the first input. |
| input_reader_dur | DURATION | Duration from the generation timestamp to the end of InputReader's work. Only populated when atrace 'input' category is enabled. |
| input_dispatcher_dur | DURATION | Duration of InputDispatcher's work. Only populated when atrace 'input' category is enabled. |
| previous_last_input_to_first_input_generation_dur | DURATION | Duration from the previous input (last input that wasn't part of this frame) to the first input in this frame. |
| presentation_ts | TIMESTAMP | Presentation timestamp for the frame. |
| browser_utid | JOINID(thread.id) | Utid for the browser main thread. |
| first_input_generation_to_browser_main_dur | DURATION | Duration from input generation to when the browser received the first input in this frame. |
| first_input_generation_to_browser_main_delta_dur | DURATION | Difference between `first_input_generation_to_browser_main_dur` for this frame and the previous frame in the same scroll. |
| first_input_touch_move_processing_dur | DURATION | Duration for processing a `TouchMove` event for the first input in this frame. |
| first_input_touch_move_processing_delta_dur | DURATION | Difference between `first_input_touch_move_processing_dur` for this frame and the previous frame in the same scroll. |
| compositor_utid | JOINID(thread.id) | Utid for the renderer compositor thread. |
| first_input_browser_to_compositor_delay_dur | DURATION | Duration between the browser and compositor dispatch for the first input in this frame. |
| first_input_browser_to_compositor_delay_delta_dur | DURATION | Difference between `first_input_browser_to_compositor_delay_dur` for this frame and the previous frame in the same scroll. |
| first_input_compositor_dispatch_dur | DURATION | Duration for the compositor dispatch for the first input in this frame. |
| first_input_compositor_dispatch_delta_dur | DURATION | Difference between `first_input_compositor_dispatch_dur` for this frame and the previous frame in the same scroll. |
| first_input_compositor_dispatch_to_on_begin_frame_delay_dur | DURATION | Duration between the compositor dispatch and the "OnBeginFrame" work for the first input in this frame. |
| first_input_compositor_dispatch_to_on_begin_frame_delay_delta_dur | DURATION | Difference between `first_input_compositor_dispatch_to_on_begin_frame_delay_dur` for this frame and the previous frame in the same scroll. |
| compositor_on_begin_frame_dur | DURATION | Duration of the "OnBeginFrame" work for this frame. |
| compositor_on_begin_frame_delta_dur | DURATION | Difference between `compositor_on_begin_frame_dur` for this frame and the previous frame in the same scroll. |
| compositor_on_begin_frame_to_generation_delay_dur | DURATION | Duration between the "OnBeginFrame" work and the generation of this frame. |
| compositor_on_begin_frame_to_generation_delay_delta_dur | DURATION | Difference between `compositor_on_begin_frame_to_generation_delay_dur` for this frame and the previous frame in the same scroll. |
| compositor_generate_frame_to_submit_frame_dur | DURATION | Duration between the generation and submission of this frame. |
| compositor_generate_frame_to_submit_frame_delta_dur | DURATION | Difference between `compositor_generate_frame_to_submit_frame_dur` for this frame and the previous frame in the same scroll. |
| compositor_submit_frame_dur | DURATION | Duration for submitting this frame. |
| compositor_submit_frame_delta_dur | DURATION | Difference between `compositor_submit_frame_dur` for this frame and the previous frame in the same scroll. |
| viz_compositor_utid | JOINID(thread.id) | Utid for the viz compositor thread. |
| compositor_to_viz_delay_dur | DURATION | Delay when a compositor frame is sent from the renderer to viz. |
| compositor_to_viz_delay_delta_dur | DURATION | Difference between `compositor_to_viz_delay_dur` for this frame and the previous frame in the same scroll. |
| viz_receive_compositor_frame_dur | DURATION | Duration of the viz work done on receiving the compositor frame. |
| viz_receive_compositor_frame_delta_dur | DURATION | Difference between `viz_receive_compositor_frame_dur` for this frame and the previous frame in the same scroll. |
| viz_wait_for_draw_dur | DURATION | Duration between viz receiving the compositor frame to frame draw. |
| viz_wait_for_draw_delta_dur | DURATION | Difference between `viz_wait_for_draw_dur` for this frame and the previous frame in the same scroll. |
| viz_draw_and_swap_dur | DURATION | Duration of the viz drawing/swapping work for this frame. |
| viz_draw_and_swap_delta_dur | DURATION | Difference between `viz_draw_and_swap_dur` for this frame and the previous frame in the same scroll. |
| viz_gpu_thread_utid | JOINID(thread.id) | Utid for the viz `CompositorGpuThread`. |
| viz_to_gpu_delay_dur | DURATION | Delay between viz work on compositor thread and `CompositorGpuThread`. |
| viz_to_gpu_delay_delta_dur | DURATION | Difference between `viz_to_gpu_delay_dur` for this frame and the previous frame in the same scroll. |
| viz_swap_buffers_dur | DURATION | Duration of frame buffer swapping work on viz. |
| viz_swap_buffers_delta_dur | DURATION | Difference between `viz_swap_buffers_dur` for this frame and the previous frame in the same scroll. |
| viz_swap_buffers_to_latch_dur | DURATION | Time between buffers ready until Choreographer's latch. |
| viz_swap_buffers_to_latch_delta_dur | DURATION | Difference between `viz_swap_buffers_to_latch_dur` for this frame and the previous frame in the same scroll. |
| viz_latch_to_presentation_dur | DURATION | Duration between Choreographer's latch and presentation. |
| viz_latch_to_presentation_delta_dur | DURATION | Difference between `viz_latch_to_presentation_dur` for this frame and the previous frame in the same scroll. |

**chrome_scroll_update_info_step_templates**

TABLE
Source of truth for the definition of the stages of a scroll. Mainly intended
for visualization purposes (e.g. in Chrome Scroll Jank plugin).

| Column | Type | Description |
|---|---|---|
| step_name | STRING | The name of a stage of a scroll. |
| ts_column_name | STRING | The name of the column in `chrome_scroll_update_info` which contains the timestamp of the stage. |
| dur_column_name | STRING | The name of the column in `chrome_scroll_update_info` which contains the duration of the stage. NULL if the stage doesn't have a duration. |

### chrome.event_latency

#### Views/Tables

**chrome_event_latencies**

TABLE
All EventLatency slices.

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice Id for the EventLatency scroll event. |
| name | STRING | Slice name. |
| ts | TIMESTAMP | The start timestamp of the scroll. |
| dur | DURATION | The duration of the scroll. |
| scroll_update_id | LONG | The id of the scroll update event (aka LatencyInfo.ID). |
| surface_frame_trace_id | LONG | The id of the first frame (pre-surface aggregation) which included the scroll update and was presented. NULL if: (1) the event is not a scroll update (`event_type` is NOT GESTURE_SCROLL_UPDATE, FIRST_GESTURE_SCROLL_UPDATE, or INERTIAL_GESTURE_SCROLL_UPDATE), (2) the scroll update wasn't presented (e.g. it was an overscroll) or (3) the trace comes from an old Chrome version (<https://crrev.com/c/6185817> was first included in version 134.0.6977.0 and was cherry-picked in version 133.0.6943.33). |
| display_trace_id | LONG | The id of the first frame (post-surface aggregation) which included the scroll update and was presented. NULL if: (1) the event is not a scroll update (`event_type` is NOT GESTURE_SCROLL_UPDATE, FIRST_GESTURE_SCROLL_UPDATE, or INERTIAL_GESTURE_SCROLL_UPDATE), (2) the scroll update wasn't presented (e.g. it was an overscroll) or (3) the trace comes from an old Chrome version (<https://crrev.com/c/6185817> was first included in version 134.0.6977.0 and was cherry-picked in version 133.0.6943.33). |
| is_presented | BOOL | Whether this input event was presented. |
| event_type | STRING | EventLatency event type. |
| track_id | LONG | Perfetto track this slice is found on. |
| vsync_interval_ms | DOUBLE | Vsync interval (in milliseconds). |
| is_janky_scrolled_frame | BOOL | Whether the corresponding frame is janky based on the Event.ScrollJank.DelayedFramesPercentage.FixedWindow metric. |
| buffer_available_timestamp | LONG | Timestamp of the BufferAvailableToBufferReady substage. |
| buffer_ready_timestamp | LONG | Timestamp of the BufferReadyToLatch substage. |
| latch_timestamp | LONG | Timestamp of the LatchToSwapEnd substage (or LatchToPresentation as a fallback). |
| swap_end_timestamp | LONG | Timestamp of the SwapEndToPresentationCompositorFrame substage. |
| presentation_timestamp | LONG | Frame presentation timestamp aka the timestamp of the SwapEndToPresentationCompositorFrame substage. TODO(b/341047059): temporarily use LatchToSwapEnd as a workaround if SwapEndToPresentationCompositorFrame is missing due to b/247542163. |

**chrome_gesture_scroll_updates**

TABLE
All scroll-related events (frames) including gesture scroll updates, begins
and ends with respective scroll ids and start/end timestamps, regardless of
being presented. This includes pinches that were presented. See b/315761896
for context on pinches.

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice Id for the EventLatency scroll event. |
| name | STRING | Slice name. |
| ts | TIMESTAMP | The start timestamp of the scroll. |
| dur | DURATION | The duration of the scroll. |
| scroll_update_id | LONG | The id of the scroll update event. |
| is_presented | BOOL | Whether this input event was presented. |
| event_type | STRING | EventLatency event type. |
| track_id | LONG | Perfetto track this slice is found on. |
| vsync_interval_ms | DOUBLE | Vsync interval (in milliseconds). |
| is_janky | BOOL | Whether the corresponding frame is janky based on the Event.ScrollJank.DelayedFramesPercentage.FixedWindow metric. |
| buffer_available_timestamp | LONG | Timestamp of the BufferAvailableToBufferReady substage. |
| buffer_ready_timestamp | LONG | Timestamp of the BufferReadyToLatch substage. |
| latch_timestamp | LONG | Timestamp of the LatchToSwapEnd substage (or LatchToPresentation as a fallback). |
| swap_end_timestamp | LONG | Timestamp of the SwapEndToPresentationCompositorFrame substage. |
| presentation_timestamp | LONG | Frame presentation timestamp aka the timestamp of the SwapEndToPresentationCompositorFrame substage. TODO(b/341047059): temporarily use LatchToSwapEnd as a workaround if SwapEndToPresentationCompositorFrame is missing due to b/247542163. |
| scroll_id | LONG | The id of the scroll. |

### chrome.event_latency_description

#### Views/Tables

**chrome_event_latency_stage_descriptions**

TABLE
Source of truth of the descriptions of EventLatency stages.

| Column | Type | Description |
|---|---|---|
| name | STRING | The name of the EventLatency stage. |
| description | STRING | A description of the EventLatency stage. |

### chrome.graphics_pipeline

#### Views/Tables

**chrome_graphics_pipeline_surface_frame_steps**

TABLE
`Graphics.Pipeline` steps corresponding to work done by a Viz client to
produce a frame (i.e. before surface aggregation). Covers steps:

- STEP_ISSUE_BEGIN_FRAME
- STEP_RECEIVE_BEGIN_FRAME
- STEP_GENERATE_RENDER_PASS
- STEP_GENERATE_COMPOSITOR_FRAME
- STEP_SUBMIT_COMPOSITOR_FRAME
- STEP_RECEIVE_COMPOSITOR_FRAME
- STEP_RECEIVE_BEGIN_FRAME_DISCARD
- STEP_DID_NOT_PRODUCE_FRAME
- STEP_DID_NOT_PRODUCE_COMPOSITOR_FRAME

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice Id of the `Graphics.Pipeline` slice. |
| ts | TIMESTAMP | The start timestamp of the slice/step. |
| dur | DURATION | The duration of the slice/step. |
| step | STRING | Step name of the `Graphics.Pipeline` slice. |
| surface_frame_trace_id | LONG | Id of the graphics pipeline, pre-surface aggregation. |
| utid | LONG | Utid of the thread where this slice exists. |
| task_start_time_ts | TIMESTAMP | Start time of the parent Chrome scheduler task (if any) of this step. |

**chrome_graphics_pipeline_display_frame_steps**

TABLE
`Graphics.Pipeline` steps corresponding to work done on creating and
presenting one frame during/after surface aggregation. Covers steps:

- STEP_DRAW_AND_SWAP
- STEP_SURFACE_AGGREGATION
- STEP_SEND_BUFFER_SWAP
- STEP_BUFFER_SWAP_POST_SUBMIT
- STEP_FINISH_BUFFER_SWAP
- STEP_SWAP_BUFFERS_ACK

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice Id of the `Graphics.Pipeline` slice. |
| ts | TIMESTAMP | The start timestamp of the slice/step. |
| dur | DURATION | The duration of the slice/step. |
| step | STRING | Step name of the `Graphics.Pipeline` slice. |
| display_trace_id | LONG | Id of the graphics pipeline, post-surface aggregation. |
| utid | LONG | Utid of the thread where this slice exists. |
| task_start_time_ts | TIMESTAMP | Start time of the parent Chrome scheduler task (if any) of this step. |

**chrome_surface_frame_id_to_first_display_id**

TABLE
Links surface frames (`chrome_graphics_pipeline_surface_frame_steps`) to the
the first display frame (`chrome_graphics_pipeline_display_frame_steps`) into
which it was included. As an display frame usually aggregates frames from
multiple surfaces, multiple `surface_frame_trace_id`s will correspond to one
`display_trace_id`.

| Column | Type | Description |
|---|---|---|
| surface_frame_trace_id | LONG | Id of the graphics pipeline, pre-surface aggregation. |
| display_trace_id | LONG | Id of the graphics pipeline, post-surface aggregation. |

**chrome_graphics_pipeline_inputs_to_surface_frames**

TABLE
Links inputs (`chrome_input_pipeline_steps.latency_id`) to the surface frame
(`chrome_graphics_pipeline_surface_frame_steps`) to which they correspond.
In other words, in general, multiple `latency_id`s will correspond to one
`surface_frame_trace_id`.

| Column | Type | Description |
|---|---|---|
| latency_id | LONG | Id corresponding to the input pipeline. |
| surface_frame_trace_id | LONG | Id of the graphics pipeline, post-surface aggregation. |

### chrome.histograms

#### Views/Tables

**chrome_histograms**

TABLE
A helper view on top of the histogram events emitted by Chrome.
Requires "disabled-by-default-histogram_samples" Chrome category or the
"org.chromium.histogram_sample" data source.

| Column | Type | Description |
|---|---|---|
| name | STRING | The name of the histogram. |
| value | LONG | The value of the histogram sample. |
| ts | TIMESTAMP | Alias of |
| thread_name | STRING | Thread name. |
| utid | LONG | Utid of the thread. |
| tid | LONG | Tid of the thread. |
| process_name | STRING | Process name. |
| upid | LONG | Upid of the process. |
| pid | LONG | Pid of the process. |

### chrome.input

#### Views/Tables

**chrome_inputs**

TABLE
Each row represents one input pipeline.

| Column | Type | Description |
|---|---|---|
| latency_id | LONG | Id of this Chrome input pipeline (LatencyInfo). |
| input_type | STRING | Input type. |

**chrome_input_pipeline_steps**

TABLE
Since not all steps have associated input type (but all steps
for a given latency id should have the same input type),
populate input type for steps where it would be NULL.

| Column | Type | Description |
|---|---|---|
| latency_id | LONG | Id of this Chrome input pipeline (LatencyInfo). |
| slice_id | LONG | Slice id |
| ts | TIMESTAMP | The step timestamp. |
| dur | DURATION | Step duration. |
| utid | LONG | Utid of the thread. |
| step | STRING | Step name (ChromeLatencyInfo.step). |
| input_type | STRING | Input type. |
| task_start_time_ts | TIMESTAMP | Start time of the parent Chrome scheduler task (if any) of this step. |

**chrome_coalesced_inputs**

TABLE
For each input, if it was coalesced into another input, get the other input's
latency id.

| Column | Type | Description |
|---|---|---|
| coalesced_latency_id | LONG | The `latency_id` of the coalesced input. |
| presented_latency_id | LONG | The `latency_id` of the other input that the current input was coalesced into. Guaranteed to be different from `coalesced_latency_id`. |

**chrome_touch_move_to_scroll_update**

TABLE
Each scroll update event (except flings) in Chrome starts its life as a touch
move event, which is then eventually converted to a scroll update itself.
Each of these events is represented by its own LatencyInfo. This table
contains a mapping between touch move events and scroll update events they
were converted into.

| Column | Type | Description |
|---|---|---|
| touch_move_latency_id | LONG | Latency id of the touch move input (LatencyInfo). |
| scroll_update_latency_id | LONG | Latency id of the corresponding scroll update input (LatencyInfo). |

**chrome_dispatch_android_input_event_to_touch_move**

TABLE
Matches Android input id to the corresponding touch move event.

| Column | Type | Description |
|---|---|---|
| android_input_id | STRING | Input id (assigned by the system, used by InputReader and InputDispatcher) |
| touch_move_latency_id | LONG | Latency id. |

### chrome.interactions

#### Views/Tables

**chrome_interactions**

TABLE
All critical user interaction events, including type and table with
associated metrics.

| Column | Type | Description |
|---|---|---|
| scoped_id | LONG | Identifier of the interaction; this is not guaranteed to be unique to the table - rather, it is unique within an individual interaction type. Combine with type to get a unique identifier in this table. |
| type | STRING | Type of this interaction, which together with scoped_id uniquely identifies this interaction. Also corresponds to a SQL table name containing more details specific to this type of interaction. |
| name | STRING | Interaction name - e.g. 'PageLoad', 'Tap', etc. Interactions will have unique metrics stored in other tables. |
| ts | TIMESTAMP | Timestamp of the CUI event. |
| dur | DURATION | Duration of the CUI event. |

### chrome.loadline_2

#### Views/Tables

**chrome_loadline2_stages**

TABLE

| Column | Type | Description |
|---|---|---|
| page | STRING | Name of the page |
| story_start | TIMESTAMP | Story start timestamp |
| start_request | TIMESTAMP | Start request timestamp |
| end_request | TIMESTAMP | End request timestamp |
| renderer_ready | TIMESTAMP | Renderer ready timestamp |
| visual_mark | TIMESTAMP | Visual mark timestamp |
| visual_raf | TIMESTAMP | Visual rAF timestamp |
| visual_presentation | TIMESTAMP | Visual presentation timestamp |
| interactive_mark | TIMESTAMP | Interactive mark timestamp |
| interactive_raf | TIMESTAMP | Interactive rAF timestamp |
| interactive_presentation | TIMESTAMP | Interactive presentation timestamp |
| story_finish | TIMESTAMP | Story finish timestamp |

### chrome.metadata

#### Functions

**chrome_hardware_class**

Returns hardware class of the device, often use to find device brand
and model.
Returns STRING: Hardware class name.

### chrome.page_loads

#### Views/Tables

**chrome_page_loads**

TABLE
Chrome page loads, including associated high-level metrics and properties.

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the navigation and Chrome browser process; this combination is unique to every individual navigation. |
| navigation_id | LONG | ID of the navigation associated with the page load (i.e. the cross-document navigation in primary main frame which created this page's main document). Also note that navigation_id is specific to a given Chrome browser process, and not globally unique. |
| navigation_start_ts | TIMESTAMP | Timestamp of the start of navigation. |
| fcp | LONG | Duration between the navigation start and the first contentful paint event (web.dev/fcp). |
| fcp_ts | TIMESTAMP | Timestamp of the first contentful paint. |
| lcp | LONG | Duration between the navigation start and the largest contentful paint event (web.dev/lcp). |
| lcp_ts | TIMESTAMP | Timestamp of the largest contentful paint. |
| dom_content_loaded_event_ts | TIMESTAMP | Timestamp of the DomContentLoaded event: <https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event> |
| load_event_ts | TIMESTAMP | Timestamp of the window load event: <https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event> |
| mark_fully_loaded_ts | TIMESTAMP | Timestamp of the page self-reporting as fully loaded through the performance.mark('mark_fully_loaded') API. |
| mark_fully_visible_ts | TIMESTAMP | Timestamp of the page self-reporting as fully visible through the performance.mark('mark_fully_visible') API. |
| mark_interactive_ts | TIMESTAMP | Timestamp of the page self-reporting as fully interactive through the performance.mark('mark_interactive') API. |
| url | STRING | URL at the page load event. |
| browser_upid | LONG | The unique process id (upid) of the browser process where the page load occurred. |

### chrome.scroll_jank.predictor_error

#### Views/Tables

**chrome_predictor_error**

TABLE
The scrolling offsets and predictor jank values for the actual (applied)
scroll events.

| Column | Type | Description |
|---|---|---|
| scroll_id | LONG | An ID that ties all EventLatencies in a particular scroll. (implementation note: This is the EventLatency TraceId of the GestureScrollbegin). |
| scroll_update_id | LONG | An ID that ties this |
| present_ts | TIMESTAMP | Presentation timestamp. |
| delta_y | DOUBLE | The delta in raw coordinates between this presented EventLatency and the previous presented frame. |
| relative_offset_y | DOUBLE | The pixel offset of this presented EventLatency compared to the initial one. |
| prev_delta | DOUBLE | The delta in raw coordinates of the previous scroll update event. |
| next_delta | DOUBLE | The delta in raw coordinates of the subsequent scroll update event. |
| predictor_jank | DOUBLE | The jank value based on the discrepancy between scroll predictor coordinates and the actual deltas between scroll update events. |
| delta_threshold | DOUBLE | The threshold used to determine if jank occurred. |

### chrome.scroll_jank.scroll_jank_cause_map

#### Views/Tables

**chrome_scroll_jank_cause_descriptions**

TABLE
Source of truth of the descriptions of EventLatency-based scroll jank causes.

| Column | Type | Description |
|---|---|---|
| event_latency_stage | STRING | The name of the EventLatency stage. |
| cause_process | STRING | The process where the cause of scroll jank occurred. |
| cause_thread | STRING | The thread where the cause of scroll jank occurred. |
| cause_description | STRING | A description of the cause of scroll jank. |

**chrome_scroll_jank_causes_with_event_latencies**

VIEW
Combined description of scroll jank cause and associated event latency stage.

| Column | Type | Description |
|---|---|---|
| name | STRING | The name of the EventLatency stage. |
| description | STRING | Description of the EventLatency stage. |
| cause_process | STRING | The process name that may cause scroll jank. |
| cause_thread | STRING | The thread name that may cause scroll jank. The thread will be on the cause_process. |
| cause_description | STRING | Description of the cause of scroll jank on this process and thread. |

### chrome.scroll_jank.scroll_jank_cause_utils

#### Table Functions

**chrome_select_scroll_jank_cause_thread**

Function to retrieve the thread id of the thread on a particular process if
there are any slices during a particular EventLatency slice duration; this
upid/thread combination refers to a cause of Scroll Jank.

| Argument | Type | Description |
|---|---|---|
| event_latency_id | LONG | The slice id of an EventLatency slice. |
| process_type | STRING | The process type that the thread is on: one of 'Browser', 'Renderer' or 'GPU'. |
| thread_name | STRING | The name of the thread. |

| Column | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | The utid associated with |

### chrome.scroll_jank.scroll_jank_intervals

#### Views/Tables

**chrome_janky_event_latencies_v3**

TABLE
Selects EventLatency slices that correspond with janks in a scroll. This is
based on the V3 version of scroll jank metrics.

| Column | Type | Description |
|---|---|---|
| id | LONG | The slice id. |
| ts | TIMESTAMP | The start timestamp of the slice. |
| dur | DURATION | The duration of the slice. |
| track_id | LONG | The track_id for the slice. |
| name | STRING | The name of the slice (EventLatency). |
| cause_of_jank | STRING | The stage of EventLatency that the caused the jank. |
| sub_cause_of_jank | STRING | The stage of cause_of_jank that caused the jank. |
| delayed_frame_count | LONG | How many vsyncs this frame missed its deadline by. |
| frame_jank_ts | TIMESTAMP | The start timestamp where frame presentation was delayed. |
| frame_jank_dur | LONG | The duration in ms of the delay in frame presentation. |

**chrome_janky_frame_presentation_intervals**

VIEW
Frame presentation interval is the delta between when the frame was supposed
to be presented and when it was actually presented.

| Column | Type | Description |
|---|---|---|
| id | LONG | Unique id. |
| ts | TIMESTAMP | The start timestamp of the slice. |
| dur | DURATION | The duration of the slice. |
| delayed_frame_count | LONG | How many vsyncs this frame missed its deadline by. |
| cause_of_jank | STRING | The stage of EventLatency that the caused the jank. |
| sub_cause_of_jank | STRING | The stage of cause_of_jank that caused the jank. |
| event_latency_id | LONG | The id of the associated event latency in the slice table. |

**chrome_scroll_stats**

TABLE
Scroll jank frame presentation stats for individual scrolls.

| Column | Type | Description |
|---|---|---|
| scroll_id | LONG | Id of the individual scroll. |
| frame_count | LONG | The number of frames in the scroll. |
| missed_vsyncs | LONG | The number of missed vsyncs in the scroll. |
| presented_frame_count | LONG | The number presented frames in the scroll. |
| janky_frame_count | LONG | The number of janky frames in the scroll. |
| janky_frame_percent | DOUBLE | The % of frames that janked in the scroll. |

**chrome_scroll_jank_intervals_v3**

TABLE
Defines slices for all of janky scrolling intervals in a trace.

| Column | Type | Description |
|---|---|---|
| id | LONG | The unique identifier of the janky interval. |
| ts | TIMESTAMP | The start timestamp of the janky interval. |
| dur | DURATION | The duration of the janky interval. |

### chrome.scroll_jank.scroll_jank_v3

#### Views/Tables

**chrome_presented_gesture_scrolls**

TABLE
Scroll updates, corresponding to all input events that were converted to a
presented scroll update.

| Column | Type | Description |
|---|---|---|
| id | LONG | Minimum slice id for input presented in this frame, the non-presented input. |
| ts | TIMESTAMP | The start timestamp for producing the frame. |
| dur | DURATION | The duration between producing and presenting the frame. |
| last_presented_input_ts | TIMESTAMP | The timestamp of the last input that arrived and got presented in the frame. |
| scroll_update_id | LONG | The id of the scroll update event, a unique identifier to the gesture. |
| scroll_id | LONG | The id of the ongoing scroll. |
| presentation_timestamp | LONG | Frame presentation timestamp. |
| event_type | STRING | EventLatency event type. |

**chrome_scroll_updates_with_deltas**

TABLE
Associate every trace_id with it's perceived delta_y on the screen after
prediction.

| Column | Type | Description |
|---|---|---|
| scroll_update_id | LONG | The id of the scroll update event. |
| delta_y | DOUBLE | The perceived delta_y on the screen post prediction. |

**chrome_full_frame_view**

TABLE
Obtain the subset of input events that were fully presented.

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the frame. |
| ts | TIMESTAMP | Start timestamp of the frame. |
| last_presented_input_ts | TIMESTAMP | The timestamp of the last presented input. |
| scroll_id | LONG | ID of the associated scroll. |
| scroll_update_id | LONG | ID of the associated scroll update. |
| event_latency_id | LONG | ID of the associated EventLatency. |
| dur | DURATION | Duration of the associated EventLatency. |
| presentation_timestamp | LONG | Frame presentation timestamp. |

**chrome_full_frame_delta_view**

TABLE
Join deltas with EventLatency data.

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the frame. |
| ts | TIMESTAMP | Start timestamp of the frame. |
| scroll_id | LONG | ID of the associated scroll. |
| scroll_update_id | LONG | ID of the associated scroll update. |
| last_presented_input_ts | TIMESTAMP | The timestamp of the last presented input. |
| delta_y | DOUBLE | The perceived delta_y on the screen post prediction. |
| event_latency_id | LONG | ID of the associated EventLatency. |
| dur | DURATION | Duration of the associated EventLatency. |
| presentation_timestamp | LONG | Frame presentation timestamp. |

**chrome_merged_frame_view**

TABLE
Group all gestures presented at the same timestamp together in
a single row.

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the frame. |
| max_start_ts | TIMESTAMP | The timestamp of the last presented input. |
| min_start_ts | TIMESTAMP | The earliest frame start timestamp. |
| scroll_id | LONG | ID of the associated scroll. |
| scroll_update_id | LONG | ID of the associated scroll update. |
| encapsulated_scroll_ids | STRING | All scroll updates associated with the frame presentation timestamp. |
| total_delta | DOUBLE | Sum of all perceived delta_y values at the frame presentation timestamp. |
| segregated_delta_y | STRING | Lists all of the perceived delta_y values at the frame presentation timestamp. |
| event_latency_id | LONG | ID of the associated EventLatency. |
| dur | DURATION | Maximum duration of the associated EventLatency. |
| presentation_timestamp | LONG | Frame presentation timestamp. |

**chrome_frame_info_with_delay**

TABLE
View contains all chrome presented frames during gesture updates
while calculating delay since last presented which usually should
equal to \|VSYNC_INTERVAL\| if no jank is present.

| Column | Type | Description |
|---|---|---|
| id | LONG | gesture scroll slice id. |
| max_start_ts | TIMESTAMP | OS timestamp of the last touch move arrival within a frame. |
| min_start_ts | TIMESTAMP | OS timestamp of the first touch move arrival within a frame. |
| scroll_id | LONG | The scroll which the touch belongs to. |
| scroll_update_id | LONG | ID of the associated scroll update. |
| encapsulated_scroll_ids | STRING | Trace ids of all frames presented in at this vsync. |
| total_delta | DOUBLE | Summation of all delta_y of all gesture scrolls in this frame. |
| segregated_delta_y | STRING | All delta y of all gesture scrolls comma separated, summing those gives |
| event_latency_id | LONG | Event latency id of the presented frame. |
| dur | DURATION | Duration of the EventLatency. |
| presentation_timestamp | LONG | Timestamp at which the frame was shown on the screen. |
| delay_since_last_frame | DOUBLE | Time elapsed since the previous frame was presented, usually equals |
| delay_since_last_input | DOUBLE | Difference in OS timestamps of inputs in the current and the previous frame. |
| prev_event_latency_id | LONG | The event latency id that will be used as a reference to determine the jank cause. |

**chrome_vsyncs**

TABLE
Calculate \|VSYNC_INTERVAL\| as the lowest vsync seen in the trace or the
minimum delay between frames larger than zero.

TODO(\~M130): Remove the lowest vsync since we should always have vsync_interval_ms.

| Column | Type | Description |
|---|---|---|
| vsync_interval | DOUBLE | The lowest delay between frames larger than zero. |

**chrome_janky_frames_no_cause**

TABLE
Filter the frame view only to frames that had missed vsyncs.

| Column | Type | Description |
|---|---|---|
| delay_since_last_frame | DOUBLE | Time elapsed since the previous frame was presented, will be more than |
| event_latency_id | LONG | Event latency id of the presented frame. |
| vsync_interval | DOUBLE | Vsync interval at the time of recording the trace. |
| hardware_class | STRING | Device brand and model. |
| scroll_id | LONG | The scroll corresponding to this frame. |
| prev_event_latency_id | LONG | The event latency id that will be used as a reference to determine the jank cause. |

**chrome_janky_frames_no_subcause**

TABLE
Janky frame information including the jank cause.

| Column | Type | Description |
|---|---|---|
| delay_since_last_frame | DOUBLE | Time elapsed since the previous frame was presented, will be more than |
| event_latency_id | LONG | Event latency id of the presented frame. |
| vsync_interval | DOUBLE | Vsync interval at the time of recording the trace. |
| hardware_class | STRING | Device brand and model. |
| scroll_id | LONG | The scroll corresponding to this frame. |
| prev_event_latency_id | LONG | The event latency id that will be used as a reference to determine the jank cause. |
| cause_id | LONG | Id of the slice corresponding to the offending stage. |

**chrome_janky_frames**

TABLE
Finds all causes of jank for all janky frames, and a cause of sub jank
if the cause of jank was GPU related.

| Column | Type | Description |
|---|---|---|
| cause_of_jank | STRING | The reason the Vsync was missed. |
| sub_cause_of_jank | STRING | Further breakdown if the root cause was GPU related. |
| delay_since_last_frame | DOUBLE | Time elapsed since the previous frame was presented, will be more than |
| event_latency_id | LONG | Event latency id of the presented frame. |
| vsync_interval | DOUBLE | Vsync interval at the time of recording the trace. |
| hardware_class | STRING | Device brand and model. |
| scroll_id | LONG | The scroll corresponding to this frame. |

**chrome_unique_frame_presentation_ts**

TABLE
Counting all unique frame presentation timestamps.

| Column | Type | Description |
|---|---|---|
| presentation_timestamp | LONG | The unique frame presentation timestamp. |

**chrome_janky_frames_percentage**

TABLE
Dividing missed frames over total frames to get janky frame percentage.
This represents the v3 scroll jank metrics.
Reflects Event.Jank.DelayedFramesPercentage UMA metric.

| Column | Type | Description |
|---|---|---|
| delayed_frame_percentage | DOUBLE | The percent of missed frames relative to total frames - aka the percent of janky frames. |

**chrome_frames_per_scroll**

TABLE
Number of frames and janky frames per scroll.

| Column | Type | Description |
|---|---|---|
| scroll_id | LONG | The ID of the scroll. |
| num_frames | LONG | The number of frames in the scroll. |
| num_janky_frames | LONG | The number of delayed/janky frames. |
| scroll_jank_percentage | DOUBLE | The percentage of janky frames relative to total frames. |

### chrome.scroll_jank.scroll_jank_v3_cause

#### Functions

**chrome_get_v3_jank_cause_id**

Given two slice Ids A and B, find the maximum difference
between the durations of it's direct children with matching names
for example if slice A has children named (X, Y, Z) with durations of (10, 10, 5)
and slice B has children named (X, Y) with durations of (9, 9), the function will return
the slice id of the slice named Z that is A's child, as no matching slice named Z was found
under B, making 5 - 0 = 5 the maximum delta between both slice's direct children
Returns LONG: The slice id of the breakdown that has the maximum duration delta.

| Argument | Type | Description |
|---|---|---|
| janky_slice_id | LONG | The slice id of the parent slice that we want to cause among it's children. |
| prev_slice_id | LONG | The slice id of the parent slice that's the reference in comparison to |

### chrome.scroll_jank.scroll_offsets

#### Views/Tables

**chrome_scroll_input_deltas**

TABLE
The raw input deltas for all input events which were part of a scroll.

| Column | Type | Description |
|---|---|---|
| scroll_update_id | LONG | Scroll update id (aka LatencyInfo.ID) for this scroll update input event. |
| delta_x | DOUBLE | The delta in pixels (scaled to the device's screen size) how much this input event moved over the X axis vs previous, as reported by the OS. |
| delta_y | DOUBLE | The delta in pixels (scaled to the device's screen size) how much this input event moved over the Y axis vs previous, as reported by the OS. |

**chrome_scroll_input_offsets**

TABLE
The raw coordinates and pixel offsets for all input events which were part of
a scroll.

| Column | Type | Description |
|---|---|---|
| scroll_update_id | LONG | An ID for this scroll update (aka LatencyInfo.ID). |
| scroll_id | LONG | An ID for the scroll this scroll update belongs to. |
| ts | TIMESTAMP | Timestamp the of the scroll input event. |
| delta_y | DOUBLE | The delta in raw coordinates between this scroll update event and the previous. |
| relative_offset_y | DOUBLE | The total delta of all scroll updates within the same as scroll up to and including this scroll update. |

**chrome_scroll_presented_deltas**

TABLE
The page offset delta (by how much the page was scrolled vs previous frame)
for each frame.
This is the resulting delta that is shown to the user after the input has
been processed. `chrome_scroll_input_deltas` tracks the underlying signal
deltas between consecutive input events.

| Column | Type | Description |
|---|---|---|
| scroll_update_id | LONG | Scroll update id (aka LatencyInfo.ID) for this scroll update input event. |
| delta_x | DOUBLE | The delta in pixels (scaled to the device's screen size) how much this input event moved over the X axis vs previous, as reported by the OS. |
| delta_y | DOUBLE | The delta in pixels (scaled to the device's screen size) how much this input event moved over the Y axis vs previous, as reported by the OS. |
| offset_x | LONG | The page offset in pixels (scaled to the device's screen size) along the X axis. |
| offset_y | LONG | The page offset in pixels (scaled to the device's screen size) along the Y axis. |

**chrome_presented_scroll_offsets**

TABLE
The scrolling offsets for the actual (applied) scroll events. These are not
necessarily inclusive of all user scroll events, rather those scroll events
that are actually processed.

| Column | Type | Description |
|---|---|---|
| scroll_update_id | LONG | An ID for this scroll update (aka LatencyInfo.ID). |
| scroll_id | LONG | An ID for the scroll this scroll update belongs to. |
| ts | TIMESTAMP | Presentation timestamp. |
| delta_y | DOUBLE | The delta in raw coordinates between this scroll update event and the previous. |
| relative_offset_y | DOUBLE | The pixel offset of this scroll update event compared to the initial one. |

### chrome.scroll_jank.utils

#### Table Functions

**chrome_select_long_task_slices**

Extract mojo information for the long-task-tracking scenario for specific
names. For example, LongTaskTracker slices may have associated IPC
metadata, or InterestingTask slices for input may have associated IPC to
determine whether the task is fling/etc.

| Argument | Type | Description |
|---|---|---|
| name | STRING | The name of slice. |

| Column | Type | Description |
|---|---|---|
| interface_name | STRING | Name of the interface of the IPC call. |
| ipc_hash | LONG | Hash of the IPC call. |
| message_type | STRING | Message type (e.g. reply). |
| id | LONG | The slice id. |

### chrome.scroll_jank_tagging

#### Views/Tables

**chrome_scroll_jank_tags**

TABLE
List of scroll jank causes that apply to janky scroll frames.
Each frame can have zero or multiple tags.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame ID. |
| tag | STRING | Tag of the scroll jank cause. |

**chrome_tagged_janky_scroll_frames**

TABLE
Consolidated list of tags for each janky scroll frame.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id. |
| tagged | BOOL | Whether this frame has any tags or not. |
| tags | STRING | Comma-separated list of tags for this frame. |

### chrome.scroll_jank_v4

#### Views/Tables

**chrome_scroll_jank_v4_results**

TABLE
Results of the Scroll Jank V4 metric for frames which contain one or more
scroll updates.

See
<https://docs.google.com/document/d/1AaBvTIf8i-c-WTKkjaL4vyhQMkSdynxo3XEiwpofdeA>
and `EventLatency.ScrollJankV4Result` in
<https://source.chromium.org/chromium/chromium/src/+/main:base/tracing/protos/chrome_track_event.proto>
for more information.

Available since Chrome 145.0.7573.0 and cherry-picked into 144.0.7559.31.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Slice ID of the 'ScrollJankV4' slice. |
| name | STRING | Slice name ('ScrollJankV4'). |
| ts | TIMESTAMP | The timestamp at the start of the slice. |
| dur | DURATION | The duration of the slice. |
| is_janky | BOOL | Whether this frame is janky. True if and only if there's at least one row with `id` in `chrome_scroll_jank_v4_reasons`. If true, then `vsyncs_since_previous_frame` must be greater than one. |
| vsyncs_since_previous_frame | LONG | How many VSyncs were between (A) this frame and (B) the previous frame. If this value is greater than one, then Chrome potentially missed one or more VSyncs (i.e. might have been able to present this scroll update earlier). NULL if this frame is the first frame in a scroll. |
| running_delivery_cutoff | DURATION | The running delivery cut-off based on frames preceding this frame. NULL if ANY of the following holds: \* This frame is the first frame in a scroll. \* All frames since the beginning of the scroll up to and including the previous frame have been non-damaging. \* The most recent janky frame was non-damaging and all frames since then up to and including the previous frame have been non-damaging. |
| adjusted_delivery_cutoff | DURATION | The running delivery cut-off adjusted for this frame. NULL if ANY of the following holds: \* This frame is the first frame in a scroll. \* This frame is non-damaging. \* All frames since the beginning of the scroll up to and including the previous frame have been non-damaging. \* The most recent janky frame was non-damaging and all frames since then up to and including the previous frame have been non-damaging. \* `vsyncs_since_previous_frame` is equal to one. |
| current_delivery_cutoff | DURATION | The delivery cut-off of this frame. NULL if this frame is non-damaging. |
| real_first_event_latency_id | LONG | Trace ID of the first real scroll update included in this frame. Can be joined with `chrome_event_latencies.scroll_update_id`. NULL if this frame contains no real scroll updates. |
| real_first_input_generation_ts | TIMESTAMP | The actual generation timestamp of the first real scroll update included (coalesced) in this frame. NULL if this frame contains no real scroll updates. |
| real_last_input_generation_ts | TIMESTAMP | The actual generation timestamp of the last real scroll update included (coalesced) in this frame. NULL if this frame contains no real scroll updates. |
| real_abs_total_raw_delta_pixels | DOUBLE | The absolute total raw (unpredicted) delta of all real scroll updates included in this frame (in pixels). NULL if this frame contains no real scroll updates. |
| real_max_abs_inertial_raw_delta_pixels | DOUBLE | The maximum absolute raw (unpredicted) delta out of all inertial (fling) scroll updates included in this frame (in pixels). NULL if there were no inertial scroll updates in this frame. |
| synthetic_first_event_latency_id | LONG | Trace ID of the first synthetic scroll update included in this frame. Can be joined with `chrome_event_latencies.scroll_update_id`. NULL if this frame contains no synthetic scroll updates. |
| synthetic_first_extrapolated_input_generation_ts | TIMESTAMP | The generation timestamp of the first synthetic scroll update included (coalesced) in this frame extrapolated based on the input generation → begin frame duration of the most recent real scroll update. NULL if ANY of the following holds: \* This frame contains no synthetic scroll updates. \* This frame is janky (i.e. `is_janky` is true). \* All frames since the beginning of the scroll up to and including the previous frame have contained only synthetic scroll updates. \* The most recent janky frame contained only synthetic scroll updates and all frames since then up to and including the previous frame have contained only synthetic scroll updates. |
| synthetic_first_original_begin_frame_ts | TIMESTAMP | The begin frame timestamp of the first synthetic scroll update included (coalesced) in this frame. NULL if this frame contains no synthetic scroll updates. If not NULL, it's less than or equal to `begin_frame_ts`. |
| first_scroll_update_type | STRING | Type of the first scroll update in this frame. Possible values: \* 'REAL' \* 'SYNTHETIC_WITH_EXTRAPOLATED_INPUT_GENERATION_TIMESTAMP' \* 'SYNTHETIC_WITHOUT_EXTRAPOLATED_INPUT_GENERATION_TIMESTAMP' The first scroll update is decided as follows: \* For real scroll updates, we consider their actual input generation timestamp. \* For synthetic scroll updates, we extrapolate their input generation timestamp based on the input generation → begin frame duration of the most recent real scroll update UNLESS ANY of the following holds (in which case we DON'T extrapolate input generation timestamps for synthetic scroll updates in this frame): \* This frame is janky. \* All frames since the beginning of the scroll up to and including the previous frame have contained only synthetic scroll updates. \* The most recent janky frame contained only synthetic scroll updates and all frames since then up to and including the previous frame have contained only synthetic scroll updates. If, based on the above rules, the scroll update with the earliest input generation timestamp is a real scroll update, then this frame's type is 'REAL'. If the scroll update with the earliest input generation timestamp is a synthetic scroll update, then this frame's type is 'SYNTHETIC_WITH_EXTRAPOLATED_INPUT_GENERATION_TIMESTAMP'. If this frame contains only synthetic scroll updates but it wasn't possible to extrapolate their input generation timestamp (for any of the reasons listed above), then this frame's type is 'SYNTHETIC_WITHOUT_EXTRAPOLATED_INPUT_GENERATION_TIMESTAMP'. |
| first_event_latency_id | LONG | Trace ID of the first scroll update included in this frame. \* If `first_scroll_update_type` is 'REAL', then `first_event_latency_id` is equal to `real_first_event_latency_id`. \* If `first_scroll_update_type` is 'SYNTHETIC_WITH_EXTRAPOLATED_INPUT_GENERATION_TIMESTAMP' or 'SYNTHETIC_WITHOUT_EXTRAPOLATED_INPUT_GENERATION_TIMESTAMP', then `first_event_latency_id` equal to `synthetic_first_event_latency_id`. Can be joined with `chrome_event_latencies.scroll_update_id`. |
| damage_type | STRING | Type of scroll damage in this frame. Possible values: \* 'DAMAGING' \* 'NON_DAMAGING_WITH_EXTRAPOLATED_PRESENTATION_TIMESTAMP' \* 'NON_DAMAGING_WITHOUT_EXTRAPOLATED_PRESENTATION_TIMESTAMP' A frame F is non-damaging if the following conditions are BOTH true: 1. All scroll updates in F are non-damaging. A scroll update is non-damaging if it didn't cause a frame update and/or didn't change the scroll offset. 2. All frames between (both ends exclusive): a. the last frame presented by Chrome before F and b. F are non-damaging. If this frame is damaging, its type is 'DAMAGING'. If this frame is non-damaging and its presentation timestamp could be extrapolated based on the begin frame → presentation duration of the most recent damaging frame, its type is 'NON_DAMAGING_WITH_EXTRAPOLATED_PRESENTATION_TIMESTAMP'. If this frame is non-damaging and its presentation timestamp couldn't be extrapolated for ANY of the reasons below, its type is 'NON_DAMAGING_WITHOUT_EXTRAPOLATED_PRESENTATION_TIMESTAMP': \* This frame is janky and non-damaging. \* All frames since the beginning of the scroll up to and including this frame have been non-damaging. \* The most recent janky frame was non-damaging and all frames since then up to and including the this frame have been non-damaging. Note: The `first_scroll_update_type` and `damage_type` columns are orthogonal. The former depends on whether the frame is synthetic (only contains synthetic scroll updates). The latter depends on whether the frame is damaging. For example: \* If a frame is synthetic and damaging, it will\[1\] have an extrapolated input generation timestamp. \* If a frame is real and non-damaging, it will\[1\] have an extrapolated presentation timestamp. \* If a frame is both synthetic and damaging, it will\[1\] have both timestamps extrapolated. \[1\] As long as there's Chrome past performance to extrapolate based on. |
| vsync_interval | DURATION | The VSync interval that this frame was produced for according to the BeginFrameArgs. |
| begin_frame_ts | TIMESTAMP | The begin frame timestamp, at which this frame started, according to the BeginFrameArgs. |
| presentation_ts | TIMESTAMP | The presentation timestamp of the frame. \* If `damage_type` is 'DAMAGING', then `presentation_ts` is the actual presentation timestamp. \* If `damage_type` is 'NON_DAMAGING_WITH_EXTRAPOLATED_PRESENTATION_TIMESTAMP', then `presentation_ts` is an extrapolated timestamp based on the begin frame → presentation duration of the most recent damaging frame. \* If `damage_type` is 'NON_DAMAGING_WITHOUT_EXTRAPOLATED_PRESENTATION_TIMESTAMP', then `presentation_ts` is NULL. |

**chrome_scroll_jank_v4_reasons**

TABLE
Reasons why the Scroll Jank V4 metric marked frames as janky.

A frame might be janky for multiple reasons, so this table might contain
multiple rows with the same `id` and distinct `jank_reason`s.

Available since Chrome 145.0.7573.0 and cherry-picked into 144.0.7559.31.

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Slice ID of the 'ScrollJankV4' slice. Can be joined with `chrome_scroll_jank_v4_results.id`. |
| jank_reason | STRING | A reason why the frame is janky. Possible values: \* 'MISSED_VSYNC_DUE_TO_DECELERATING_INPUT_FRAME_DELIVERY': Chrome's input→frame delivery slowed down to the point that it missed one or more VSyncs. \* 'MISSED_VSYNC_DURING_FAST_SCROLL': Chrome missed one or more VSyncs in the middle of a fast regular scroll. \* 'MISSED_VSYNC_AT_START_OF_FLING': Chrome missed one or more VSyncs during the transition from a fast regular scroll to a fling. \* 'MISSED_VSYNC_DURING_FLING': Chrome missed one or more VSyncs in the middle of a fling. |
| missed_vsyncs | LONG | Number of VSyncs that that Chrome missed (for `jank_reason`) before presenting the first scroll update in the frame. Greater than zero. |

### chrome.speedometer

#### Views/Tables

**chrome_speedometer_measure**

TABLE
Augmented slices for Speedometer measurements.
These are the intervals of time Speedometer uses to compute the final score.
There are two intervals that are measured for every test: sync and async

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start timestamp of the measure slice |
| dur | DURATION | Duration of the measure slice |
| name | STRING | Full measure name |
| iteration | LONG | Speedometer iteration the slice belongs to. |
| suite_name | STRING | Suite name |
| test_name | STRING | Test name |
| measure_type | STRING | Type of the measure (sync or async) |

**chrome_speedometer_iteration**

TABLE
Slice that covers one Speedometer iteration.
Depending on the Speedometer version these slices might need to be estimated
as older versions of Speedometer to not emit marks for this interval. The
metrics associated are the same ones Speedometer would output, but note we
use ns precision (Speedometer uses \~100us) so the actual values might differ
a bit.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start timestamp of the iteration |
| dur | DURATION | Duration of the iteration |
| name | STRING | Iteration name |
| iteration | LONG | Iteration number |
| geomean | DOUBLE | Geometric mean of the suite durations for this iteration. |
| score | DOUBLE | Speedometer score for this iteration (The total score for a run in the average of all iteration scores). |

#### Functions

**chrome_speedometer_score**

Returns DOUBLE: Speedometer score

**chrome_speedometer_renderer_main_utid**

Returns LONG: Renderer main utid

### chrome.speedometer_2_1

#### Views/Tables

**chrome_speedometer_2_1_measure**

TABLE
Augmented slices for Speedometer measurements.
These are the intervals of time Speedometer uses to compute the final score.
There are two intervals that are measured for every test: sync and async
sync is the time between the start and sync-end marks, async is the time
between the sync-end and async-end marks.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start timestamp of the measure slice |
| dur | DURATION | Duration of the measure slice |
| name | STRING | Full measure name |
| iteration | LONG | Speedometer iteration the slice belongs to. |
| suite_name | STRING | Suite name |
| test_name | STRING | Test name |
| measure_type | STRING | Type of the measure (sync or async) |

**chrome_speedometer_2_1_iteration**

TABLE
Slice that covers one Speedometer iteration.
This slice is actually estimated as a default Speedometer run will not emit
marks to cover this interval. The metrics associated are the same ones
Speedometer would output, but note we use ns precision (Speedometer uses
\~100us) so the actual values might differ a bit. Also note Speedometer
returns the values in ms these here and in ns.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start timestamp of the iteration |
| dur | DURATION | Duration of the iteration |
| name | STRING | Iteration name |
| iteration | LONG | Iteration number |
| geomean | DOUBLE | Geometric mean of the suite durations for this iteration. |
| score | DOUBLE | Speedometer score for this iteration (The total score for a run in the average of all iteration scores). |

#### Functions

**chrome_speedometer_2_1_score**

Returns the Speedometer 2.1 score for all iterations in the trace
Returns DOUBLE: Speedometer 2.1 score

**chrome_speedometer_2_1_renderer_main_utid**

Returns the utid for the main thread that ran Speedometer 2.1
Returns LONG: Renderer main utid

### chrome.speedometer_3

#### Views/Tables

**chrome_speedometer_3_measure**

TABLE
Augmented slices for Speedometer measurements.
These are the intervals of time Speedometer uses to compute the final score.
There are two intervals that are measured for every test: sync and async.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start timestamp of the measure slice |
| dur | DURATION | Duration of the measure slice |
| name | STRING | Full measure name |
| iteration | LONG | Speedometer iteration the slice belongs to. |
| suite_name | STRING | Suite name |
| test_name | STRING | Test name |
| measure_type | STRING | Type of the measure (sync or async) |

**chrome_speedometer_3_iteration**

TABLE
Slice that covers one Speedometer iteration.
The metrics associated are the same ones
Speedometer would output, but note we use ns precision (Speedometer uses
\~100us) so the actual values might differ a bit.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start timestamp of the iteration |
| dur | DURATION | Duration of the iteration |
| name | STRING | Iteration name |
| iteration | LONG | Iteration number |
| geomean | DOUBLE | Geometric mean of the suite durations for this iteration. |
| score | DOUBLE | Speedometer score for this iteration (The total score for a run in the average of all iteration scores). |

#### Functions

**chrome_speedometer_3_score**

Returns DOUBLE: Speedometer 3 score

**chrome_speedometer_3_renderer_main_utid**

Returns LONG: Renderer main utid

### chrome.startups

#### Views/Tables

**chrome_startups**

TABLE
Chrome startups, including launch cause.

| Column | Type | Description |
|---|---|---|
| id | LONG | Unique ID |
| activity_id | LONG | Chrome Activity event id of the launch. |
| name | STRING | Name of the launch start event. |
| startup_begin_ts | TIMESTAMP | Timestamp that the startup occurred. |
| first_visible_content_ts | TIMESTAMP | Timestamp to the first visible content. |
| launch_cause | STRING | Launch cause. See Startup.LaunchCauseType in chrome_track_event.proto. |
| browser_upid | LONG | Process ID of the Browser where the startup occurred. |

### chrome.tasks

#### Views/Tables

**chrome_java_views**

VIEW
A list of slices corresponding to operations on interesting (non-generic)
Chrome Java views. The view is considered interested if it's not a system
(ContentFrameLayout) or generic library (CompositorViewHolder) views.

TODO(altimin): Add "columns_from slice" annotation.
TODO(altimin): convert this to EXTEND_TABLE when it becomes available.

| Column | Type | Description |
|---|---|---|
| filtered_name | STRING | Name of the view. |
| is_software_screenshot | BOOL | Whether this slice is a part of non-accelerated capture toolbar screenshot. |
| is_hardware_screenshot | BOOL | Whether this slice is a part of accelerated capture toolbar screenshot. |
| slice_id | LONG | Slice id. |

**chrome_scheduler_tasks**

VIEW
A list of tasks executed by Chrome scheduler.

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice id. |
| type | STRING | Type. |
| name | STRING | Name of the task. |
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Duration. |
| utid | LONG | Utid of the thread this task run on. |
| thread_name | STRING | Name of the thread this task run on. |
| upid | LONG | Upid of the process of this task. |
| process_name | STRING | Name of the process of this task. |
| track_id | LONG | Same as slice.track_id. |
| category | STRING | Same as slice.category. |
| depth | LONG | Same as slice.depth. |
| parent_id | LONG | Same as slice.parent_id. |
| arg_set_id | LONG | Same as slice.arg_set_id. |
| thread_ts | TIMESTAMP | Same as slice.thread_ts. |
| thread_dur | DURATION | Same as slice.thread_dur. |
| posted_from | STRING | Source location where the PostTask was called. |

**chrome_tasks**

VIEW
A list of "Chrome tasks": top-level execution units (e.g. scheduler tasks /
IPCs / system callbacks) run by Chrome. For a given thread, the slices
corresponding to these tasks will not intersect.

| Column | Type | Description |
|---|---|---|
| id | LONG | Id for the given task, also the id of the slice this task corresponds to. |
| name | STRING | Name for the given task. |
| task_type | STRING | Type of the task (e.g. "scheduler"). |
| thread_name | STRING | Thread name. |
| utid | LONG | Utid. |
| process_name | STRING | Process name. |
| upid | LONG | Upid. |
| ts | TIMESTAMP | Alias of |
| dur | DURATION | Alias of |
| track_id | LONG | Alias of |
| category | STRING | Alias of |
| arg_set_id | LONG | Alias of |
| thread_ts | TIMESTAMP | Alias of |
| thread_dur | DURATION | Alias of |
| full_name | STRING | STRING Legacy alias for |

### chrome.vsync_intervals

#### Views/Tables

**chrome_vsync_intervals**

TABLE
A simple table that checks the time between VSync (this can be used to
determine if we're refreshing at 90 FPS or 60 FPS).

> [!NOTE]
> **Note:** In traces without the "Java" category there will be no VSync TraceEvents and this table will be empty.

| Column | Type | Description |
|---|---|---|
| slice_id | LONG | Slice id of the vsync slice. |
| ts | TIMESTAMP | Timestamp of the vsync slice. |
| dur | DURATION | Duration of the vsync slice. |
| track_id | LONG | Track id of the vsync slice. |
| time_to_next_vsync | LONG | Duration until next vsync arrives. |

#### Functions

**chrome_calculate_avg_vsync_interval**

Function: compute the average Vysnc interval of the
gesture (hopefully this would be either 60 FPS for the whole gesture or 90
FPS but that isnt always the case) on the given time segment.
If the trace doesnt contain the VSync TraceEvent we just fall back on
assuming its 60 FPS (this is the 1.6e+7 in the COALESCE which
corresponds to 16 ms or 60 FPS).
Returns DOUBLE: The average vsync interval on this time segment or 1.6e+7, if trace doesn't contain the VSync TraceEvent.

| Argument | Type | Description |
|---|---|---|
| begin_ts | TIMESTAMP | Interval start time. |
| end_ts | TIMESTAMP | Interval end time. |

### chrome.web_content_interactions

#### Views/Tables

**chrome_web_content_interactions**

TABLE
Chrome web content interactions (InteractionToFirstPaint), including
associated high-level metrics and properties.

Multiple events may occur for the same interaction; each row in this table
represents the primary (longest) event for the interaction.

Web content interactions are discrete, as opposed to sustained (e.g.
scrolling); and only occur with the web content itself, as opposed to other
parts of Chrome (e.g. omnibox). Interaction events include taps, clicks,
keyboard input (typing), and drags.

| Column | Type | Description |
|---|---|---|
| id | LONG | Unique id for this interaction. |
| ts | TIMESTAMP | Start timestamp of the event. Because multiple events may occur for the same interaction, this is the start timestamp of the longest event. |
| dur | DURATION | Duration of the event. Because multiple events may occur for the same interaction, this is the duration of the longest event. |
| interaction_type | STRING | The interaction type. |
| total_duration_ms | LONG | The total duration of all events that occurred for the same interaction. |
| renderer_upid | LONG | The process id this event occurred on. |

## Package: android

### android.anrs

#### Views/Tables

**android_anrs**

TABLE
List of all ANRs that occurred in the trace (one row per ANR).

| Column | Type | Description |
|---|---|---|
| process_name | STRING | Name of the process that triggered the ANR. |
| pid | LONG | PID of the process that triggered the ANR. |
| upid | JOINID(process.id) | UPID of the process that triggered the ANR. |
| error_id | STRING | UUID of the ANR (generated on the platform). |
| ts | TIMESTAMP | Timestamp of the ANR. |
| subject | STRING | Subject line of the ANR. |
| intent | STRING | The intent that caused the ANR (if applicable). |
| component | STRING | The component associated with the ANR (if applicable). |
| timer_delay | LONG | The duration between the timer expiration event and the anr counter event |
| anr_type | STRING | The standard type of ANR. |
| anr_dur_ms | LONG | Duration of the ANR, computed from the timer expiration event. |
| default_anr_dur_ms | LONG | Default duration of the ANR, based on the anr_type (default means in AOSP/Pixel). Note: Other OEMs may have customized these timeout values, so the defaults provided here might not be accurate for all devices. |

### android.app_process_starts

#### Views/Tables

**android_app_process_starts**

TABLE
All app cold starts with information about their cold start reason:
broadcast, service, activity or provider.

| Column | Type | Description |
|---|---|---|
| start_id | LONG | Slice id of the bindApplication slice in the app. Uniquely identifies a process start. |
| id | LONG | Slice id of intent received in the app. |
| track_id | JOINID(track.id) | Track id of the intent received in the app. |
| process_name | STRING | Name of the process receiving the intent. |
| pid | LONG | Pid of the process receiving the intent. |
| upid | JOINID(process.id) | Upid of the process receiving the intent. |
| intent | STRING | Intent action or component responsible for the cold start. |
| reason | STRING | Process start reason: activity, broadcast, service or provider. |
| proc_start_ts | TIMESTAMP | Timestamp the process start was dispatched from system_server. |
| proc_start_dur | DURATION | Duration to dispatch the process start from system_server. |
| bind_app_ts | TIMESTAMP | Timestamp the bindApplication started in the app. |
| bind_app_dur | DURATION | Duration to complete bindApplication in the app. |
| intent_ts | TIMESTAMP | Timestamp the Intent was received in the app. |
| intent_dur | DURATION | Duration to handle intent in the app. |
| total_dur | LONG | Total duration from proc_start dispatched to intent completed. |

### android.auto.multiuser

#### Views/Tables

**android_auto_multiuser_timing**

TABLE
Time elapsed between the latest user start
and the specific end event
like package startup(ex carlauncher) or previous user stop.

| Column | Type | Description |
|---|---|---|
| event_start_user_id | STRING | Id of the started android user |
| event_start_time | LONG | Start event time |
| event_end_time | LONG | End event time |
| event_end_name | STRING | End event name |
| event_start_name | STRING | Start event name |
| duration | LONG | User switch duration from start event to end event |

**android_auto_multiuser_timing_with_previous_user_resource_usage**

VIEW
This table extends `android_auto_multiuser_timing` table with previous user resource usage.

| Column | Type | Description |
|---|---|---|
| event_start_user_id | STRING | Start user id |
| event_start_time | LONG | Start event time |
| event_end_time | LONG | End event time |
| event_end_name | STRING | End event name |
| event_start_name | STRING | Start event name |
| duration | LONG | User switch duration from start event to end event |
| user_id | LONG | User id |
| total_cpu_time | LONG | Total CPU time for a user |
| total_memory_usage_kb | LONG | Total memory user for a user |

### android.battery

#### Views/Tables

**android_battery_charge**

VIEW
Battery charge at timestamp.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp. |
| current_avg_ua | DOUBLE | Current average micro ampers. |
| capacity_percent | DOUBLE | Current capacity percentage. |
| charge_uah | DOUBLE | Current charge in micro ampers. |
| current_ua | DOUBLE | Current micro ampers. |
| voltage_uv | DOUBLE | Current voltage in micro volts. |
| energy_counter_uwh | DOUBLE | Current energy counter in microwatt-hours(µWh). |
| power_mw | DOUBLE | Current power in milliwatts. |

### android.battery.charging_states

#### Views/Tables

**android_charging_states**

TABLE
Device charging states.

| Column | Type | Description |
|---|---|---|
| id | LONG | Alias of counter.id if a slice with charging state exists otherwise there will be a single row where id = 1. |
| ts | TIMESTAMP | Timestamp at which the device charging state began. |
| dur | DURATION | Duration of the device charging state. |
| short_charging_state | STRING | One of: charging, discharging, not_charging, full, unknown. |
| charging_state | STRING | Device charging state, one of: Charging, Discharging, Not charging (when the charger is present but battery is not charging), Full, Unknown |

### android.battery.doze

#### Views/Tables

**android_light_idle_state**

TABLE
Light idle states. This is the state machine that quickly detects the
device is unused and restricts background activity.
See <https://developer.android.com/training/monitoring-device-state/doze-standby>

| Column | Type | Description |
|---|---|---|
| id | LONG | ID |
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Duration. |
| light_idle_state | STRING | Description of the light idle state. |

**android_deep_idle_state**

TABLE
Deep idle states. This is the state machine that more slowly detects deeper
levels of device unuse and restricts background activity further.
See <https://developer.android.com/training/monitoring-device-state/doze-standby>

| Column | Type | Description |
|---|---|---|
| id | LONG | ID |
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Duration. |
| deep_idle_state | STRING | Description of the deep idle state. |

### android.battery_stats

#### Views/Tables

**android_battery_stats_state**

VIEW
View of human readable battery stats counter-based states. These are recorded
by BatteryStats as a bitmap where each 'category' has a unique value at any
given time.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the new barrary state. |
| dur | DURATION | The duration the state was active, -1 for incomplete slices. |
| safe_dur | DURATION | The same as `dur`, but extends to trace end for incomplete slices. |
| track_name | STRING | The name of the counter track. |
| value | LONG | The counter value as a number. |
| value_name | STRING | The counter value as a human-readable string. |

**android_battery_stats_event_slices**

VIEW
View of slices derived from battery_stats events. Battery stats records all
events as instants, however some may indicate whether something started or
stopped with a '+' or '-' prefix. Events such as jobs, top apps, foreground
apps or long wakes include these details and allow drawing slices between
instant events found in a trace.

For example, we may see an event like the following on 'battery_stats.top':

`-top=10215:"com.google.android.apps.nexuslauncher"` This view will find the associated start ('+top') with the matching suffix
(everything after the '=') to construct a slice. It computes the timestamp
and duration from the events and extract the details as follows:

`track_name='battery_stats.top'
str_value='com.google.android.apps.nexuslauncher'
int_value=10215`

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of a new battery state. |
| dur | DURATION | The duration the state was active, -1 for incomplete slices. |
| safe_dur | DURATION | The same as `dur`, but extends to trace end for incomplete slices. |
| track_name | STRING | The name of the counter track. |
| str_value | STRING | String value. |
| int_value | LONG | Int value. |

#### Functions

**android_battery_stats_counter_to_string**

Converts a battery_stats counter value to human readable string.
Returns STRING: The human-readable name for the counter value.

| Argument | Type | Description |
|---|---|---|
| track | STRING | The counter track name (e.g. 'battery_stats.audio'). |
| value | DOUBLE | The counter value. |

### android.binder

#### Views/Tables

**android_binder_metrics_by_process**

VIEW
Count Binder transactions per process.

| Column | Type | Description |
|---|---|---|
| process_name | STRING | Name of the process that started the binder transaction. |
| pid | LONG | PID of the process that started the binder transaction. |
| slice_name | STRING | Name of the slice with binder transaction. |
| event_count | LONG | Number of binder transactions in process in slice. |

**android_sync_binder_thread_state_by_txn**

VIEW
Aggregated thread_states on the client and server side per binder txn
This builds on the data from \|_sync_binder_metrics_by_txn\| and
for each end (client and server) of the transaction, it returns
the aggregated sum of all the thread state durations.
The \|thread_state_type\| column represents whether a given 'aggregated thread_state'
row is on the client or server side. 'binder_txn' is client side and 'binder_reply'
is server side.

| Column | Type | Description |
|---|---|---|
| binder_txn_id | LONG | slice id of the binder txn |
| client_ts | TIMESTAMP | Client timestamp |
| client_tid | LONG | Client tid |
| binder_reply_id | LONG | slice id of the binder reply |
| server_ts | TIMESTAMP | Server timestamp |
| server_tid | LONG | Server tid |
| thread_state_type | STRING | whether thread state is on the txn or reply side |
| thread_state | STRING | a thread_state that occurred in the txn |
| thread_state_dur | DURATION | aggregated dur of the |
| thread_state_count | LONG | aggregated count of the |

**android_sync_binder_blocked_functions_by_txn**

VIEW
Aggregated blocked_functions on the client and server side per binder txn
This builds on the data from \|_sync_binder_metrics_by_txn\| and
for each end (client and server) of the transaction, it returns
the aggregated sum of all the kernel blocked function durations.
The \|thread_state_type\| column represents whether a given 'aggregated blocked_function'
row is on the client or server side. 'binder_txn' is client side and 'binder_reply'
is server side.

| Column | Type | Description |
|---|---|---|
| binder_txn_id | LONG | slice id of the binder txn |
| client_ts | TIMESTAMP | Client ts |
| client_tid | LONG | Client tid |
| binder_reply_id | LONG | slice id of the binder reply |
| server_ts | TIMESTAMP | Server ts |
| server_tid | LONG | Server tid |
| thread_state_type | STRING | whether thread state is on the txn or reply side |
| blocked_function | STRING | blocked kernel function in a thread state |
| blocked_function_dur | DURATION | aggregated dur of the |
| blocked_function_count | LONG | aggregated count of the |

**android_binder_txns**

TABLE
Breakdown binder transactions per txn.
It returns data about the client and server ends of every binder transaction async.

| Column | Type | Description |
|---|---|---|
| aidl_name | STRING | Fully qualified name of the binder endpoint if existing. |
| interface | STRING | Interface of the binder endpoint if existing. |
| method_name | STRING | Method name of the binder endpoint if existing. |
| aidl_ts | TIMESTAMP | Timestamp the binder interface name was emitted. Proxy to 'ts' and 'dur' for async txns. |
| aidl_dur | DURATION | Duration of the binder interface name. Proxy to 'ts' and 'dur' for async txns. |
| binder_txn_id | JOINID(slice.id) | Slice id of the binder txn. |
| client_process | STRING | Name of the client process. |
| client_thread | STRING | Name of the client thread. |
| client_upid | JOINID(process.id) | Upid of the client process. |
| client_utid | JOINID(thread.id) | Utid of the client thread. |
| client_tid | LONG | Tid of the client thread. |
| client_pid | LONG | Pid of the client thread. |
| is_main_thread | BOOL | Whether the txn was initiated from the main thread of the client process. |
| client_ts | TIMESTAMP | Timestamp of the client txn. |
| client_dur | DURATION | Wall clock dur of the client txn. |
| binder_reply_id | JOINID(slice.id) | Slice id of the binder reply. |
| server_process | STRING | Name of the server process. |
| server_thread | STRING | Name of the server thread. |
| server_upid | JOINID(process.id) | Upid of the server process. |
| server_utid | JOINID(thread.id) | Utid of the server thread. |
| server_tid | LONG | Tid of the server thread. |
| server_pid | LONG | Pid of the server thread. |
| server_ts | TIMESTAMP | Timestamp of the server txn. |
| server_dur | DURATION | Wall clock dur of the server txn. |
| client_oom_score | LONG | Oom score of the client process at the start of the txn. |
| server_oom_score | LONG | Oom score of the server process at the start of the reply. |
| is_sync | BOOL | Whether the txn is synchronous or async (oneway). |
| client_monotonic_dur | DURATION | Monotonic clock dur of the client txn. |
| server_monotonic_dur | DURATION | Monotonic clock dur of the server txn. |
| client_package_version_code | LONG | Client package version_code. |
| server_package_version_code | LONG | Server package version_code. |
| is_client_package_debuggable | BOOL | Whether client package is debuggable. |
| is_server_package_debuggable | BOOL | Whether server package is debuggable. |

#### Table Functions

**android_binder_outgoing_graph**

Returns a DAG of all outgoing binder txns from a process.
The roots of the graph are the threads making the txns and the graph flows from:
thread -\> server_process -\> AIDL interface -\> AIDL method.
The weights of each node represent the wall execution time in the server_process.

| Argument | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Upid of process to generate an outgoing graph for. |

| Column | Type | Description |
|---|---|---|
| pprof | BYTES | Pprof of outgoing binder txns. |

**android_binder_incoming_graph**

Returns a DAG of all incoming binder txns from a process.
The roots of the graph are the clients making the txns and the graph flows from:
client_process -\> AIDL interface -\> AIDL method.
The weights of each node represent the wall execution time in the server_process.

| Argument | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Upid of process to generate an incoming graph for. |

| Column | Type | Description |
|---|---|---|
| pprof | BYTES | Pprof of incoming binder txns. |

**android_binder_graph**

Returns a graph of all binder txns in a trace.
The nodes are client_process and server_process.
The weights of each node represent the wall execution time in the server_process.

| Argument | Type | Description |
|---|---|---|
| min_client_oom_score | LONG | Matches txns from client_processes greater than or equal to the OOM score. |
| max_client_oom_score | LONG | Matches txns from client_processes less than or equal to the OOM score. |
| min_server_oom_score | LONG | Matches txns to server_processes greater than or equal to the OOM score. |
| max_server_oom_score | LONG | Matches txns to server_processes less than or equal to the OOM score. |

| Column | Type | Description |
|---|---|---|
| pprof | BYTES | Pprof of binder txns. |

### android.binder_breakdown

#### Views/Tables

**android_binder_server_breakdown**

TABLE
Server side binder breakdowns per transactions per txn.

| Column | Type | Description |
|---|---|---|
| binder_txn_id | JOINID(slice.id) | Client side id of the binder txn. |
| binder_reply_id | JOINID(slice.id) | Server side id of the binder txn. |
| ts | TIMESTAMP | Timestamp of an exclusive interval during the binder reply with a single reason. |
| dur | DURATION | Duration of an exclusive interval during the binder reply with a single reason. |
| reason | STRING | Cause of delay during an exclusive interval of the binder reply. |

**android_binder_client_breakdown**

TABLE
Client side binder breakdowns per transactions per txn.

| Column | Type | Description |
|---|---|---|
| binder_txn_id | JOINID(slice.id) | Client side id of the binder txn. |
| binder_reply_id | JOINID(slice.id) | Server side id of the binder txn. |
| ts | TIMESTAMP | Timestamp of an exclusive interval during the binder txn with a single latency reason. |
| dur | DURATION | Duration of an exclusive interval during the binder txn with a single latency reason. |
| reason | STRING | Cause of delay during an exclusive interval of the binder txn. |

**android_binder_client_server_breakdown**

TABLE
Combined client and server side binder breakdowns per transaction.

| Column | Type | Description |
|---|---|---|
| binder_txn_id | JOINID(slice.id) | Client side id of the binder txn. |
| binder_reply_id | JOINID(slice.id) | Server side id of the binder txn. |
| ts | TIMESTAMP | Timestamp of an exclusive interval during the binder txn with a single latency reason. |
| dur | DURATION | Duration of an exclusive interval during the binder txn with a single latency reason. |
| server_reason | STRING | The server side component of this interval's binder latency reason, if any. |
| client_reason | STRING | The client side component of this interval's binder latency reason. |
| reason | STRING | Combined reason indicating whether latency came from client or server side. |
| reason_type | STRING | Whether the latency is due to the client or server. |

### android.bitmaps

#### Views/Tables

**android_bitmap_memory**

TABLE
Provides a timeseries of "Bitmap Memory" counter for each process, which
is useful for retrieving the total memory used by bitmaps by an application over time.

To populate this table, tracing must be enabled with the "view" atrace
category.

| Column | Type | Description |
|---|---|---|
| id | ID(counter.id) | ID of the row in the underlying counter table. |
| upid | JOINID(process.upid) | Upid of the process. |
| ts | TIMESTAMP | Timestamp of the start of the interval. |
| dur | DURATION | Duration of the interval. |
| track_id | JOINID(counter.track_id) | Duration of the interval. |
| value | LONG | Memory consumed by bitmaps in bytes. |

**android_bitmap_count**

TABLE
Provides a timeseries of "Bitmap Count" counter for each process, which
is useful for retrieving the number of bitmaps used by an application over time.

To populate this table, tracing must be enabled with the "view" atrace
category.

| Column | Type | Description |
|---|---|---|
| id | ID(counter.id) | ID of the row in the underlying counter table. |
| upid | JOINID(process.upid) | Upid of the process. |
| ts | TIMESTAMP | Timestamp of the start of the interval. |
| dur | DURATION | Duration of the interval. |
| track_id | JOINID(counter.track_id) | Duration of the interval. |
| value | LONG | Number of allocated bitmaps. |

**android_bitmap_counters_per_process**

TABLE
Provides a timeseries of bitmap-related counters for each process, which
is useful for understanding an application's bitmap usage over time.

To populate this table, tracing must be enabled with the "view" atrace
category.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.upid) | Upid of the process. |
| process_name | STRING | Name of the process. |
| ts | TIMESTAMP | Timestamp of the start of the interval. |
| dur | DURATION | Duration of the interval. |
| bitmap_memory | LONG | Memory consumed by bitmaps in bytes. |
| bitmap_count | LONG | Number of allocated bitmaps. |
| bitmap_memory_id | JOINID(counter.id) | ID of the row in the underlying counter table. |
| bitmap_count_id | JOINID(counter.id) | ID of the row in the underlying counter table. |

### android.cpu.cluster_type

#### Views/Tables

**android_cpu_cluster_mapping**

TABLE
Stores the mapping of a cpu to its cluster type - e.g. little, medium, big.
This cluster type is determined by initially using cpu_capacity from sysfs
and grouping clusters with identical capacities, ordered by size.
In the case that capacities are not present, max frequency is used instead.
If nothing is avaiable, NULL is returned.

| Column | Type | Description |
|---|---|---|
| ucpu | LONG | Alias of `cpu.ucpu`. |
| cpu | LONG | Alias of `cpu.cpu`. |
| cluster_type | STRING | The cluster type of the CPU. |

### android.cpu.cpu_per_uid

#### Views/Tables

**android_cpu_per_uid_track**

TABLE
Table of tracks for CPU-per-UID data. Each row represents one UID / cluster
combination.

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the track; can be joined with cpu_per_uid_counter. |
| uid | LONG | UID doing the work. |
| cluster | LONG | Cluster ID for the track, starting from 0, typically with larger numbers meaning larger cores. |
| total_cpu_millis | LONG | Total number of cpu millis used by this track. |
| package_name | STRING | A package name for the UID. If there are multiple for a UID, one is chosen arbitrarily. UIDs below 10000 always have null package name. |

**android_cpu_per_uid_counter**

VIEW
View of counters for CPU-per-UID data. Each row represents one instant in
time for one UID / cluster.

| Column | Type | Description |
|---|---|---|
| id | LONG | ID for the row. |
| ts | LONG | Timestamp for the row. |
| dur | LONG | Time to the next measurement for the UID / cluster combination. |
| track_id | LONG | Associated track. |
| diff_ms | LONG | CPU time measurement for this time period (milliseconds). |
| cpu_ratio | DOUBLE | Inferred CPU use value for the period where 1.0 means a single core at 100% utilisation. |

### android.cujs.base

#### Views/Tables

**android_jank_cuj**

TABLE
Table tracking all jank CUJs information.

| Column | Type | Description |
|---|---|---|
| cuj_id | LONG | Unique incremental ID for each CUJ. |
| upid | JOINID(process.id) | process id. |
| process_name | STRING | process name. |
| cuj_slice_name | STRING | Name of the CUJ slice. |
| cuj_name | STRING | Name of the CUJ without the 'J\<' prefix. |
| slice_id | JOINID(slice.id) | Id of the CUJ slice in perfetto. Keeping the slice id column as part of this table as provision to lookup the actual CUJ slice ts and dur. The ts and dur in this table might differ from the slice duration, as they are associated with start and end frame corresponding to the CUJ. |
| ts | TIMESTAMP | Start timestamp of the CUJ. Start of the CUJ as defined by the start of the first overlapping expected frame. |
| ts_end | TIMESTAMP | End timestamp of the CUJ. Calculated as the end timestamp of the last actual frame overlapping with the CUJ. |
| dur | DURATION | Duration of the CUJ calculated based on the ts and ts_end values. |
| state | STRING | State of the CUJ. One of "completed", "cancelled" or NULL. NULL in cases where the FT#cancel or FT#end instant event is not present for the CUJ. |
| ui_thread | JOINID(thread.id) | thread id of the UI thread. |
| layer_id | LONG | layer id associated with the actual frame. |
| begin_vsync | LONG | vysnc id of the first frame that falls within the CUJ boundary. |
| end_vsync | LONG | vysnc id of the last frame that falls within the CUJ boundary. |

### android.cujs.sysui_cujs

#### Views/Tables

**android_sysui_jank_cujs**

TABLE
Table tracking all jank CUJs information.

| Column | Type | Description |
|---|---|---|
| cuj_id | LONG | Unique incremental ID for each CUJ. |
| upid | JOINID(process.id) | process id. |
| process_name | STRING | process name. |
| cuj_slice_name | STRING | Name of the CUJ slice. |
| cuj_name | STRING | Name of the CUJ without the 'J\<' prefix. |
| slice_id | JOINID(slice.id) | Id of the CUJ slice in perfetto. Keeping the slice id column as part of this table as provision to lookup the actual CUJ slice ts and dur. The ts and dur in this table might differ from the slice duration, as they are associated with start and end frame corresponding to the CUJ. |
| ts | TIMESTAMP | Start timestamp of the CUJ. Start of the CUJ as defined by the start of the first overlapping expected frame. |
| ts_end | TIMESTAMP | End timestamp of the CUJ. Calculated as the end timestamp of the last actual frame overlapping with the CUJ. |
| dur | DURATION | Duration of the CUJ calculated based on the ts and ts_end values. |
| state | STRING | State of the CUJ. One of "completed", "cancelled" or NULL. NULL in cases where the FT#cancel or FT#end instant event is not present for the CUJ. |
| ui_thread | JOINID(thread.id) | thread id of the UI thread. |
| layer_id | LONG | layer id associated with the actual frame. |
| begin_vsync | LONG | vysnc id of the first frame that falls within the CUJ boundary. |
| end_vsync | LONG | vysnc id of the last frame that falls within the CUJ boundary. |

**android_sysui_latency_cujs**

TABLE
Table tracking all latency CUJs information.

| Column | Type | Description |
|---|---|---|
| cuj_id | LONG | Unique incremental ID for each CUJ. |
| upid | JOINID(process.id) | process id. |
| process_name | STRING | process name. |
| cuj_slice_name | STRING | Name of the CUJ slice. |
| cuj_name | STRING | Name of the CUJ without the 'L\<' prefix. |
| slice_id | JOINID(slice.id) | Id of the CUJ slice in perfetto. Keeping the slice id column as part of this table as provision to lookup the actual CUJ slice ts and dur. The ts and dur in this table might differ from the slice duration, as they are associated with start and end frame corresponding to the CUJ. |
| ts | TIMESTAMP | Start timestamp of the CUJ calculated as the start of the CUJ slice in trace. |
| ts_end | TIMESTAMP | End timestamp of the CUJ calculated as the end timestamp of the CUJ slice. |
| dur | DURATION | Duration of the CUJ calculated based on the ts and ts_end values. |
| state | STRING | State of the CUJ whether it was completed/cancelled. |

**android_jank_latency_cujs**

TABLE
Table tracking all jank/latency CUJs information.

| Column | Type | Description |
|---|---|---|
| cuj_id | LONG | Unique incremental ID for each CUJ. |
| id | LONG | An alias for cuj_id for compatibility purposes. |
| upid | JOINID(process.id) | process id. |
| process_name | STRING | process name. |
| cuj_slice_name | STRING | Name of the CUJ slice. |
| cuj_name | STRING | Name of the CUJ without the 'J\<' prefix. |
| slice_id | JOINID(slice.id) | Id of the CUJ slice in perfetto. Keeping the slice id column as part of this table as provision to lookup the actual CUJ slice ts and dur. The ts and dur in this table might differ from the slice duration, as they are associated with start and end frame corresponding to the CUJ. |
| ts | TIMESTAMP | Start timestamp of the CUJ. Start of the CUJ as defined by the start of the first overlapping expected frame. |
| ts_end | TIMESTAMP | End timestamp of the CUJ. Calculated as the end timestamp of the last actual frame overlapping with the CUJ. |
| dur | DURATION | Duration of the CUJ calculated based on the ts and ts_end values. |
| state | STRING | State of the CUJ. One of "completed", "cancelled" or NULL. NULL in cases where the FT#cancel or FT#end instant event is not present for the CUJ. |
| ui_thread | JOINID(thread.id) | thread id of the UI thread. In case of latency CUJs, this will always be the main thread of the process. |
| layer_id | LONG | layer id associated with the actual frame. |
| begin_vsync | LONG | vysnc id of the first frame that falls within the CUJ boundary. |
| end_vsync | LONG | vysnc id of the last frame that falls within the CUJ boundary. |
| cuj_type | STRING | Type of CUJ, i.e. jank or latency. |

### android.cujs.threads

#### Views/Tables

**android_jank_cuj_render_thread**

TABLE
Table captures thread information for 'RenderThread' for all CUJs.

| Column | Type | Description |
|---|---|---|
| cuj_id | LONG | Unique incremental ID for each CUJ. |
| upid | JOINID(process.id) | process id. |
| utid | JOINID(thread.id) | thread id of the main/UI thread. |
| name | STRING | thread name. |
| track_id | JOINID(track.id) | track_id for the thread. |

#### Table Functions

**android_jank_cuj_app_thread**

Returns a table with all CUJs and an additional column for the track id of thread_name
passed as parameter, if present in the same process of the cuj.

| Argument | Type | Description |
|---|---|---|
| thread_name | STRING | Name of the thread for which information needs to be extracted. |

| Column | Type | Description |
|---|---|---|
| cuj_id | LONG | Unique incremental ID for each CUJ. |
| upid | JOINID(process.id) | process id. |
| utid | LONG | thread id of the input thread. |
| name | STRING | name of the thread. |
| track_id | LONG | track id associated with the thread. |

### android.desktop_mode

#### Views/Tables

**android_desktop_mode_windows**

TABLE
Desktop Windows with durations they were open.

| Column | Type | Description |
|---|---|---|
| raw_add_ts | TIMESTAMP | Window add timestamp; NULL if no add event in the trace. |
| raw_remove_ts | TIMESTAMP | Window remove timestamp; NULL if no remove event in the trace. |
| ts | TIMESTAMP | Timestamp that the window was added; or trace_start() if no add event in the trace. |
| dur | DURATION | Furation the window was open; or until trace_end() if no remove event in the trace. |
| instance_id | LONG | Desktop Window instance ID - unique per window. |
| uid | LONG | UID of the app running in the window. |

### android.device

#### Views/Tables

**android_device_name**

TABLE
Extract name of the device based on metadata from the trace.

| Column | Type | Description |
|---|---|---|
| name | STRING | Device name. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |

### android.dumpsys.show_map

#### Views/Tables

**android_dumpsys_show_map**

TABLE
This table represents memory mapping information from /proc/\[pid\]/smaps
All memory values are in kilobytes (KB)

| Column | Type | Description |
|---|---|---|
| process_name | STRING | Name of the process. |
| pid | JOINID(process.pid) | Process ID. |
| vss_kb | LONG | Virtual Set Size in kilobytes - total virtual memory mapped by the process. |
| rss_kb | LONG | Resident Set Size in kilobytes - actual physical memory used by the process. |
| pss_kb | LONG | Proportional Set Size in kilobytes - amount of memory shared with other processes. |
| shared_clean_kb | LONG | Clean shared pages in kilobytes - shared pages that haven't been modified. |
| shared_dirty_kb | LONG | Dirty shared pages in kilobytes - shared pages that have been modified. |
| private_clean_kb | LONG | Clean private pages in kilobytes - private pages that haven't been modified. |
| private_dirty_kb | LONG | Dirty private pages in kilobytes - private pages that have been modified. |
| swap_kb | LONG | Swap memory in kilobytes - memory that has been moved to swap space. |
| swap_pss_kb | LONG | Proportional Swap Size in kilobytes - swap shared with other processes. |
| anon_huge_pages_kb | LONG | Anonymous huge pages in kilobytes - large anonymous memory regions. |
| shmem_pmd_mapped_kb | LONG | Shared Memory PMD mapped in kilobytes - page middle directory mapped shared memory. |
| file_pmd_mapped_kb | LONG | File PMD mapped in kilobytes - page middle directory mapped file memory. |
| shared_huge_tlb_kb | LONG | Shared huge TLB in kilobytes - shared huge page table entries. |
| private_hugetlb_kb | LONG | Private huge TLB in kilobytes - private huge page table entries. |
| locked_kb | LONG | Locked memory in kilobytes - memory that can't be swapped out. |
| mapping_count | LONG | Number of mappings of the object. |
| mapped_object | STRING | Path to the mapped object (file, library, etc.). |

### android.dvfs

#### Views/Tables

**android_dvfs_counters**

VIEW
Dvfs counter with duration.

| Column | Type | Description |
|---|---|---|
| name | STRING | Counter name. |
| ts | TIMESTAMP | Timestamp when counter value changed. |
| value | DOUBLE | Counter value. |
| dur | DURATION | Counter duration. |

**android_dvfs_counter_stats**

TABLE
Aggregates dvfs counter slice for statistic.

| Column | Type | Description |
|---|---|---|
| name | STRING | Counter name on which all the other values are aggregated on. |
| max | DOUBLE | Max of all counter values for the counter name. |
| min | DOUBLE | Min of all counter values for the counter name. |
| dur | DURATION | Duration between the first and last counter value for the counter name. |
| wgt_avg | DOUBLE | Weighted avergate of all the counter values for the counter name. |

**android_dvfs_counter_residency**

VIEW

| Column | Type | Description |
|---|---|---|
| name | STRING | Counter name. |
| value | DOUBLE | Counter value. |
| dur | DURATION | Counter duration. |
| pct | DOUBLE | Counter duration as a percentage of total duration. |

### android.entity_state_residency

#### Views/Tables

**android_entity_state_residency**

TABLE
Android entity state residency samples.
For details see: <https://perfetto.dev/docs/reference/trace-config-proto#AndroidPowerConfig>

| Column | Type | Description |
|---|---|---|
| id | ID(counter.id) | `counter.id` |
| ts | TIMESTAMP | Timestamp of the residency sample. |
| dur | DURATION | Time until the next residency sample. |
| entity_name | STRING | Entity or subsytem name. |
| state_name | STRING | State name |
| raw_name | STRING | Raw name (alias of counter.name) |
| state_time_since_boot | DURATION | Time the entity or subsystem spent in the state since boot |
| state_time_since_boot_at_end | DURATION | Time the entity or subsystem spent in the state since boot on the next sample |
| state_time_ratio | DOUBLE | ratio of the time the entity or subsystem spend in the state out of the elapsed time of the sample period. A value of 1 typically means the 100% of time was spent in the state, and a value of 0 means no time was spent. |
| track_id | JOINID(track.id) | entity + state track id. Alias of `counter_track.id`. |

### android.frames.jank_type

#### Functions

**android_is_sf_jank_type**

Returns BOOL: True when the jank type represents sf jank

| Argument | Type | Description |
|---|---|---|
| jank_type | STRING | the jank type from args.display_value with key = "Jank type" |

**android_is_app_jank_type**

Returns BOOL: True when the jank type represents app jank

| Argument | Type | Description |
|---|---|---|
| jank_type | STRING | the jank type from args.display_value with key = "Jank type" |

**android_is_missed_frame_type**

Returns BOOL: True if jank_type represents missed frame jank

| Argument | Type | Description |
|---|---|---|
| jank_type | STRING | the jank type from args.display_value with key = "Jank type" |

### android.frames.per_frame_metrics

#### Views/Tables

**android_frames_overrun**

TABLE
The amount by which each frame missed of hit its deadline. Negative if the
deadline was not missed. Frames are considered janky if `overrun` is
positive.
Calculated as the difference between the end of the
`expected_frame_timeline_slice` and `actual_frame_timeline_slice` for the
frame.
Availability: from S (API 31).
For Googlers: more details in go/android-performance-metrics-glossary.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id. |
| overrun | LONG | Difference between `expected` and `actual` frame ends. Negative if frame didn't miss deadline. |

**android_frames_ui_time**

TABLE
How much time did the frame's Choreographer callbacks take.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id |
| ui_time | LONG | UI time duration |

**android_app_vsync_delay_per_frame**

TABLE
App Vsync delay for a frame. The time between the VSYNC-app signal and the
start of Choreographer work.
Calculated as time difference between the actual frame start (from
`actual_frame_timeline_slice`) and start of the `Choreographer#doFrame`
slice.
For Googlers: more details in go/android-performance-metrics-glossary.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id |
| app_vsync_delay | LONG | App VSYNC delay. |

**android_cpu_time_per_frame**

TABLE
How much time did the frame take across the UI Thread + RenderThread.
Calculated as sum of `app VSYNC delay` `Choreographer#doFrame` slice
duration and summed durations of all `DrawFrame` slices associated with this
frame.
Availability: from N (API 24).
For Googlers: more details in go/android-performance-metrics-glossary.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id |
| app_vsync_delay | LONG | Difference between actual timeline of the frame and `Choreographer#doFrame`. See `android_app_vsync_delay_per_frame` table for more details. |
| do_frame_dur | DURATION | Duration of `Choreographer#doFrame` slice. |
| draw_frame_dur | DURATION | Duration of `DrawFrame` slice. Summed duration of all `DrawFrame` slices, if more than one. See `android_frames_draw_frame` for more details. |
| cpu_time | LONG | CPU time across the UI Thread + RenderThread. |

**android_frame_stats**

TABLE
Aggregated stats of the frame.

For Googlers: more details in go/android-performance-metrics-glossary.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id. |
| overrun | LONG | The amount by which each frame missed of hit its deadline. See `android_frames_overrun` for details. |
| cpu_time | LONG | How much time did the frame take across the UI Thread + RenderThread. |
| ui_time | LONG | How much time did the frame's Choreographer callbacks take. |
| was_jank | BOOL | Was frame janky. |
| was_slow_frame | BOOL | CPU time of the frame took over 20ms. |
| was_big_jank | BOOL | CPU time of the frame took over 50ms. |
| was_huge_jank | BOOL | CPU time of the frame took over 200ms. |

### android.frames.timeline

#### Views/Tables

**android_frames_choreographer_do_frame**

TABLE
All of the `Choreographer#doFrame` slices with their frame id.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Choreographer#doFrame slice. Slice with the name "Choreographer#doFrame {frame id}". |
| frame_id | LONG | Frame id. Taken as the value behind "Choreographer#doFrame" in slice name. |
| ui_thread_utid | JOINID(thread.id) | Utid of the UI thread |
| upid | JOINID(process.id) | Upid of application process |
| ts | TIMESTAMP | Timestamp of the slice. |

**android_frames_draw_frame**

TABLE
All of the `DrawFrame` slices with their frame id and render thread.
There might be multiple DrawFrames slices for a single vsync (frame id).
This happens when we are drawing multiple layers (e.g. status bar and
notifications).

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | DrawFrame slice. Slice with the name "DrawFrame {frame id}". |
| frame_id | LONG | Frame id. Taken as the value behind "DrawFrame" in slice name. |
| render_thread_utid | JOINID(thread.id) | Utid of the render thread |
| upid | JOINID(process.id) | Upid of application process |

**android_frames_layers**

TABLE
TODO(b/384322064) Match actual timeline slice with correct draw frame using layer name.
All slices related to one frame. Aggregates `Choreographer#doFrame`,
`actual_frame_timeline_slice` and `expected_frame_timeline_slice` slices.
This table differs slightly from the android_frames table, as it
captures the layer_id for each actual timeline slice too.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id. |
| ts | TIMESTAMP | Timestamp of the frame. Start of the frame as defined by the start of "Choreographer#doFrame" slice and the same as the start of the frame in \`actual_frame_timeline_slice if present. |
| dur | DURATION | Duration of the frame, as defined by the duration of the corresponding `actual_frame_timeline_slice` or, if not present the time between the `ts` and the end of the final `DrawFrame`. |
| ts_end | TIMESTAMP | End timestamp of the frame. End of the frame as defined by the sum of start timestamp and duration of the frame. |
| do_frame_id | JOINID(slice.id) | `slice.id` of "Choreographer#doFrame" slice. |
| draw_frame_id | JOINID(slice.id) | `slice.id` of "DrawFrame" slice. For now, we only support the first DrawFrame slice (due to b/384322064). |
| actual_frame_timeline_id | JOINID(slice.id) | `slice.id` from `actual_frame_timeline_slice` |
| expected_frame_timeline_id | JOINID(slice.id) | `slice.id` from `expected_frame_timeline_slice` |
| render_thread_utid | JOINID(thread.id) | `utid` of the render thread. |
| ui_thread_utid | JOINID(thread.id) | thread id of the UI thread. |
| layer_id | LONG | layer id associated with the actual frame. |
| layer_name | STRING | layer name associated with the actual frame. |
| upid | JOINID(process.id) | process id. |
| process_name | STRING | process name. |

**android_frames**

TABLE
Table based on the android_frames_layers table. It aggregates time, duration and counts
information across different layers for a given frame_id in a given process.

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id. |
| ts | TIMESTAMP | Timestamp of the frame. Start of the frame as defined by the start of "Choreographer#doFrame" slice and the same as the start of the frame in \`actual_frame_timeline_slice if present. |
| dur | DURATION | Duration of the frame, as defined by the duration of the corresponding `actual_frame_timeline_slice` or, if not present the time between the `ts` and the end of the final `DrawFrame`. |
| do_frame_id | JOINID(slice.id) | `slice.id` of "Choreographer#doFrame" slice. |
| draw_frame_id | JOINID(slice.id) | `slice.id` of "DrawFrame" slice. For now, we only support the first DrawFrame slice (due to b/384322064). |
| actual_frame_timeline_id | JOINID(slice.id) | `slice.id` from `actual_frame_timeline_slice` |
| expected_frame_timeline_id | JOINID(slice.id) | `slice.id` from `expected_frame_timeline_slice` |
| render_thread_utid | JOINID(thread.id) | `utid` of the render thread. |
| ui_thread_utid | JOINID(thread.id) | thread id of the UI thread. |
| actual_frame_timeline_count | LONG | Count of slices in `actual_frame_timeline_slice` related to this frame. |
| expected_frame_timeline_count | LONG | Count of slices in `expected_frame_timeline_slice` related to this frame. |
| draw_frame_count | LONG | Count of draw_frame associated to this frame. |
| upid | JOINID(process.id) | process id. |
| process_name | STRING | process name. |

#### Table Functions

**android_first_frame_after**

Returns first frame after the provided timestamp. The returning table has at
most one row.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp. |

| Column | Type | Description |
|---|---|---|
| frame_id | LONG | Frame id. |
| ts | TIMESTAMP | Start of the frame, the timestamp of the "Choreographer#doFrame" slice. |
| dur | DURATION | Duration of the frame. |
| do_frame_id | JOINID(slice.id) | "Choreographer#doFrame" slice. The slice with name "Choreographer#doFrame" corresponding to this frame. |
| draw_frame_id | JOINID(slice.id) | "DrawFrame" slice. The slice with name "DrawFrame" corresponding to this frame. |
| actual_frame_timeline_id | JOINID(slice.id) | actual_frame_timeline_slice\` slice related to this frame. |
| expected_frame_timeline_id | JOINID(slice.id) | `expected_frame_timeline_slice` slice related to this frame. |
| render_thread_utid | JOINID(thread.id) | `utid` of the render thread. |
| ui_thread_utid | JOINID(thread.id) | `utid` of the UI thread. |

### android.freezer

#### Views/Tables

**android_freezer_events**

TABLE
All frozen processes and their frozen duration.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Upid of frozen process |
| pid | LONG | Pid of frozen process |
| ts | TIMESTAMP | Timestamp process was frozen. |
| dur | DURATION | Duration process was frozen for. |
| unfreeze_reason_int | LONG | Unfreeze reason Integer. |
| unfreeze_reason_str | STRING | Unfreeze reason String. |

### android.garbage_collection

#### Views/Tables

**android_garbage_collection_events**

TABLE
All Garbage collection events with a breakdown of the time spent and heap reclaimed.

| Column | Type | Description |
|---|---|---|
| tid | LONG | Tid of thread running garbage collection. |
| pid | LONG | Pid of process running garbage collection. |
| utid | JOINID(thread.id) | Utid of thread running garbage collection. |
| upid | JOINID(process.id) | Upid of process running garbage collection. |
| thread_name | STRING | Name of thread running garbage collection. |
| process_name | STRING | Name of process running garbage collection. |
| gc_type | STRING | Type of garbage collection. |
| is_mark_compact | LONG | Whether gargage collection is mark compact or copying. |
| reclaimed_mb | DOUBLE | MB reclaimed after garbage collection. |
| min_heap_mb | DOUBLE | Minimum heap size in MB during garbage collection. |
| max_heap_mb | DOUBLE | Maximum heap size in MB during garbage collection. |
| gc_id | LONG | Garbage collection id. |
| gc_ts | TIMESTAMP | Garbage collection timestamp. |
| gc_dur | DURATION | Garbage collection wall duration. |
| gc_running_dur | DURATION | Garbage collection duration spent executing on CPU. |
| gc_runnable_dur | DURATION | Garbage collection duration spent waiting for CPU. |
| gc_unint_io_dur | DURATION | Garbage collection duration spent waiting in the Linux kernel on IO. |
| gc_unint_non_io_dur | DURATION | Garbage collection duration spent waiting in the Linux kernel without IO. |
| gc_int_dur | LONG | Garbage collection duration spent waiting in interruptible sleep. |

### android.gpu.frequency

#### Views/Tables

**android_gpu_frequency**

TABLE
GPU frequency counter per GPU.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp |
| dur | DURATION | Duration |
| gpu_id | LONG | GPU id. Joinable with `gpu_counter_track.gpu_id`. |
| gpu_freq | LONG | GPU frequency |
| prev_gpu_freq | LONG | GPU frequency from previous slice |
| next_gpu_freq | LONG | GPU frequency from next slice |

### android.gpu.mali_power_state

#### Views/Tables

**android_mali_gpu_power_state**

TABLE

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp |
| dur | DURATION | Duration |
| power_state | LONG | GPU power state |

### android.gpu.memory

#### Views/Tables

**android_gpu_memory_per_process**

TABLE
Counter for GPU memory per process with duration.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp |
| dur | DURATION | Duration |
| upid | JOINID(process.id) | Upid of the process |
| gpu_memory | LONG | GPU memory |

### android.gpu.work_period

#### Views/Tables

**android_gpu_work_period_track**

TABLE
Tracks for GPU work period events originating from the
`power/gpu_work_period` Linux ftrace tracepoint.

This tracepoint is usually only available on selected Android devices.

| Column | Type | Description |
|---|---|---|
| id | LONG | Unique identifier for this track. Joinable with track.id. |
| machine_id | LONG | Machine identifier, non-null for tracks on a remote machine. |
| uid | LONG | The UID of the package for which the GPU work period events were emitted. |
| gpu_id | LONG | The GPU identifier for which the GPU work period events were emitted. |

### android.input

#### Views/Tables

**android_input_events**

TABLE
All input events with round trip latency breakdown. Input delivery is socket based and every
input event sent from the OS needs to be ACK'ed by the app. This gives us 4 subevents to measure
latencies between:

1. Input dispatch event sent from OS.
2. Input dispatch event received in app.
3. Input ACK event sent from app.
4. Input ACK event received in OS.

| Column | Type | Description |
|---|---|---|
| dispatch_latency_dur | DURATION | Duration from input dispatch to input received. |
| handling_latency_dur | DURATION | Duration from input received to input ACK sent. |
| ack_latency_dur | DURATION | Duration from input ACK sent to input ACK received. |
| total_latency_dur | DURATION | Duration from input dispatch to input event ACK received. |
| end_to_end_latency_dur | DURATION | Duration from input read to frame present time. Null if an input event has no associated frame event. |
| tid | LONG | Tid of thread receiving the input event. |
| thread_name | STRING | Name of thread receiving the input event. |
| pid | LONG | Pid of process receiving the input event. |
| process_name | STRING | Name of process receiving the input event. |
| event_type | STRING | Input event type. See InputTransport.h: InputMessage#Type |
| event_action | STRING | Input event action. |
| event_seq | STRING | Input event sequence number, monotonically increasing for an event channel and pid. |
| event_channel | STRING | Input event channel name. |
| input_event_id | STRING | Unique identifier for the input event. |
| read_time | LONG | Timestamp input event was read by InputReader. |
| dispatch_track_id | JOINID(track.id) | Thread track id of input event dispatching thread. |
| dispatch_ts | TIMESTAMP | Timestamp input event was dispatched. |
| dispatch_dur | DURATION | Duration of input event dispatch. |
| receive_track_id | JOINID(track.id) | Thread track id of input event receiving thread. |
| receive_ts | TIMESTAMP | Timestamp input event was received. |
| receive_dur | DURATION | Duration of input event receipt. |
| frame_id | LONG | Vsync Id associated with the input. Null if an input event has no associated frame event. |

**android_key_events**

VIEW
Key events processed by the Android framework (from android.input.inputevent data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the trace entry |
| event_id | LONG | The randomly-generated ID associated with each input event processed by Android Framework, used to track the event through the input pipeline |
| ts | TIMESTAMP | The timestamp of when the input event was processed by the system |
| arg_set_id | ARGSETID | Details of the input event parsed from the proto message |
| source | LONG | Event source e.g. touchscreen, keyboard |
| action | LONG | Action e.g. down, move |
| device_id | LONG | Device id |
| display_id | LONG | Display id |
| key_code | LONG | Key code |

**android_motion_events**

VIEW
Motion events processed by the Android framework (from android.input.inputevent data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the trace entry |
| event_id | LONG | The randomly-generated ID associated with each input event processed by Android Framework, used to track the event through the input pipeline |
| ts | TIMESTAMP | The timestamp of when the input event was processed by the system |
| arg_set_id | ARGSETID | Details of the input event parsed from the proto message |
| source | LONG | Event source e.g. touchscreen, keyboard |
| action | LONG | Action e.g. down, move |
| device_id | LONG | Device id |
| display_id | LONG | Display id |

**android_input_event_dispatch**

VIEW
Input event dispatching information in Android (from android.input.inputevent data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | ID of the trace entry |
| event_id | LONG | Event ID of the input event that was dispatched |
| arg_set_id | ARGSETID | Details of the input event parsed from the proto message |
| vsync_id | LONG | Vsync ID that identifies the state of the windows during which the dispatch decision was made |
| window_id | LONG | Window ID of the window receiving the event |

### android.job_scheduler

#### Views/Tables

**android_job_scheduler_events**

TABLE
All scheduled jobs and their latencies.

The table is populated by ATrace using the system server ATrace category
(`atrace_categories: "ss"`). You can also set the `atrace_apps` of interest.

This differs from the `android_job_scheduler_states` table
in the `android.job_scheduler_states` module which is populated
by the `ScheduledJobStateChanged` atom.

Using `android_job_scheduler_states` is preferred when the
`ATOM_SCHEDULED_JOB_STATE_CHANGED` is available in the trace since
it includes the constraint, screen, or charging state changes for
each job in a trace.

| Column | Type | Description |
|---|---|---|
| job_id | LONG | Id of the scheduled job assigned by the app developer. |
| uid | LONG | Uid of the process running the scheduled job. |
| package_name | STRING | Package name of the process running the scheduled job. |
| job_service_name | STRING | Service component name of the scheduled job. |
| track_id | JOINID(track.id) | Thread track id of the job scheduler event slice. |
| id | LONG | Slice id of the job scheduler event slice. |
| ts | TIMESTAMP | Timestamp the job was scheduled. |
| dur | DURATION | Duration of the scheduled job. |

### android.job_scheduler_states

#### Views/Tables

**android_job_scheduler_states**

TABLE
This table returns constraint changes that a
job will go through in a single trace.

Values in this table are derived from the the `ScheduledJobStateChanged`
atom. This table differs from the
`android_job_scheduler_with_screen_charging_states` in this module
(`android.job_scheduler_states`) by only having job constraint information.

See documentation for the `android_job_scheduler_with_screen_charging_states`
for how tables in this module differ from `android_job_scheduler_events`
table in the `android.job_scheduler` module and how to populate this table.

| Column | Type | Description |
|---|---|---|
| id | ID | Unique identifier for job scheduler state. |
| ts | TIMESTAMP | Timestamp of job state slice. |
| dur | DURATION | Duration of job state slice. |
| slice_id | JOINID(slice.id) | Id of the slice. |
| job_name | STRING | Name of the job (as named by the app). |
| uid | LONG | Uid associated with job. |
| job_id | LONG | Id of job (assigned by app for T- builds and system generated in U+ builds). |
| package_name | STRING | Package that the job belongs (ex: associated app). |
| job_namespace | STRING | Namespace of job. |
| effective_priority | LONG | Priority at which JobScheduler ran the job. |
| has_battery_not_low_constraint | BOOL | True if app requested job should run when the device battery is not low. |
| has_charging_constraint | BOOL | True if app requested job should run when the device is charging. |
| has_connectivity_constraint | BOOL | True if app requested job should run when device has connectivity. |
| has_content_trigger_constraint | BOOL | True if app requested job should run when there is a content trigger. |
| has_deadline_constraint | BOOL | True if app requested there is a deadline by which the job should run. |
| has_idle_constraint | BOOL | True if app requested job should run when device is idle. |
| has_storage_not_low_constraint | BOOL | True if app requested job should run when device storage is not low. |
| has_timing_delay_constraint | BOOL | True if app requested job has a timing delay. |
| is_prefetch | BOOL | True if app requested job should run within hours of app launch. |
| is_requested_expedited_job | BOOL | True if app requested that the job is run as an expedited job. |
| is_running_as_expedited_job | BOOL | The job is run as an expedited job. |
| num_previous_attempts | TIMESTAMP | Number of previous attempts at running job. |
| requested_priority | LONG | The requested priority at which the job should run. |
| standby_bucket | STRING | The job's standby bucket (one of: Active, Working Set, Frequent, Rare, Never, Restricted, Exempt). |
| is_periodic | BOOL | Job should run in intervals. |
| has_flex_constraint | BOOL | True if the job should run as a flex job. |
| is_requested_as_user_initiated_job | BOOL | True is app has requested that a job be run as a user initiated job. |
| is_running_as_user_initiated_job | BOOL | True if job is running as a user initiated job. |
| deadline_ms | LONG | Deadline that job has requested and valid if has_deadline_constraint is true. |
| job_start_latency_ms | LONG | The latency in ms between when a job is scheduled and when it actually starts. |
| num_uncompleted_work_items | LONG | Number of uncompleted job work items. |
| proc_state | STRING | Process state of the process responsible for running the job. |
| internal_stop_reason | STRING | Internal stop reason for a job. |
| public_stop_reason | STRING | Public stop reason for a job. |

**android_job_scheduler_with_screen_charging_states**

TABLE
This table returns the constraint, charging,
and screen state changes that a job will go through
in a single trace.

Values from this table are derived from
the `ScheduledJobStateChanged` atom. This differs from the
`android_job_scheduler_events` table in the `android.job_scheduler` module
which is derived from ATrace the system server category
(`atrace_categories: "ss"`).

This also differs from the `android_job_scheduler_states` in this module
(`android.job_scheduler_states`) by providing charging and screen state
changes.

To populate this table, enable the Statsd Tracing Config with the
ATOM_SCHEDULED_JOB_STATE_CHANGED push atom id.
<https://perfetto.dev/docs/reference/trace-config-proto#StatsdTracingConfig>

This table is preferred over `android_job_scheduler_events`
since it contains more information and should be used whenever
`ATOM_SCHEDULED_JOB_STATE_CHANGED` is available in a trace.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp of job. |
| dur | DURATION | Duration of slice in ns. |
| slice_id | JOINID(slice.id) | Id of the slice. |
| job_name | STRING | Name of the job (as named by the app). |
| job_id | LONG | Id of job (assigned by app for T- builds and system generated in U+ builds). |
| uid | LONG | Uid associated with job. |
| job_dur | DURATION | Duration of entire job in ns. |
| package_name | STRING | Package that the job belongs (ex: associated app). |
| job_namespace | STRING | Namespace of job. |
| charging_state | STRING | Device charging state during job (one of: Charging, Discharging, Not charging, Full, Unknown). |
| screen_state | STRING | Device screen state during job (one of: Screen off, Screen on, Always-on display (doze), Unknown). |
| effective_priority | LONG | Priority at which JobScheduler ran the job. |
| has_battery_not_low_constraint | BOOL | True if app requested job should run when the device battery is not low. |
| has_charging_constraint | BOOL | True if app requested job should run when the device is charging. |
| has_connectivity_constraint | BOOL | True if app requested job should run when device has connectivity. |
| has_content_trigger_constraint | BOOL | True if app requested job should run when there is a content trigger. |
| has_deadline_constraint | BOOL | True if app requested there is a deadline by which the job should run. |
| has_idle_constraint | BOOL | True if app requested job should run when device is idle. |
| has_storage_not_low_constraint | BOOL | True if app requested job should run when device storage is not low. |
| has_timing_delay_constraint | BOOL | True if app requested job has a timing delay. |
| is_prefetch | BOOL | True if app requested job should run within hours of app launch. |
| is_requested_expedited_job | BOOL | True if app requested that the job is run as an expedited job. |
| is_running_as_expedited_job | BOOL | The job is run as an expedited job. |
| num_previous_attempts | TIMESTAMP | Number of previous attempts at running job. |
| requested_priority | LONG | The requested priority at which the job should run. |
| standby_bucket | STRING | The job's standby bucket (one of: Active, Working Set, Frequent, Rare, Never, Restricted, Exempt). |
| is_periodic | BOOL | Job should run in intervals. |
| has_flex_constraint | BOOL | True if the job should run as a flex job. |
| is_requested_as_user_initiated_job | BOOL | True is app has requested that a job be run as a user initiated job. |
| is_running_as_user_initiated_job | BOOL | True if job is running as a user initiated job. |
| deadline_ms | LONG | Deadline that job has requested and valid if has_deadline_constraint is true. |
| job_start_latency_ms | LONG | The latency in ms between when a job is scheduled and when it actually starts. |
| num_uncompleted_work_items | LONG | Number of uncompleted job work items. |
| proc_state | STRING | Process state of the process responsible for running the job. |
| internal_stop_reason | STRING | Internal stop reason for a job. |
| public_stop_reason | STRING | Public stop reason for a job. |

### android.kernel_wakelocks

#### Views/Tables

**android_kernel_wakelocks**

TABLE
Table of kernel (or native) wakelocks with held duration.

Subtracts suspended time from each period to calculate the
fraction of awake time for which the wakelock was held.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Duration. |
| awake_dur | DURATION | Duration spent awake. |
| name | STRING | Kernel or native wakelock name. |
| type | STRING | 'kernel' or 'native'. |
| held_dur | DURATION | Time the wakelock was held. |
| held_ratio | DOUBLE | Fraction of awake (not suspended) time the wakelock was held. |

### android.memory.dmabuf

#### Views/Tables

**android_dmabuf_allocs**

TABLE
Track dmabuf allocations, re-attributing gralloc allocations to their source
(if binder transactions to gralloc are recorded).

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | timestamp of the allocation |
| buf_size | LONG | allocation size (will be negative for release) |
| inode | LONG | dmabuf inode |
| utid | JOINID(thread.id) | utid of thread responsible for the allocation if a dmabuf is allocated by gralloc we follow the binder transaction to the requesting thread (requires binder tracing) |
| tid | LONG | tid of thread responsible for the allocation |
| thread_name | STRING | thread name |
| upid | JOINID(process.id) | upid of process responsible for the allocation (matches utid) |
| pid | LONG | pid of process responsible for the allocation |
| process_name | STRING | process name |

**android_memory_cumulative_dmabuf**

TABLE
Provides a timeseries of dmabuf allocations for each process.
To populate this table, tracing must be enabled with the "dmabuf_allocs" ftrace event.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | upid of process responsible for the allocation (matches utid) |
| process_name | STRING | process name |
| utid | JOINID(thread.id) | utid of thread responsible for the allocation if a dmabuf is allocated by gralloc we follow the binder transaction to the requesting thread (requires binder tracing) |
| thread_name | STRING | thread name |
| ts | TIMESTAMP | timestamp of the allocation |
| value | LONG | total allocation size per process and thread |

### android.memory.heap_graph.class_relationship

#### Macros

**android_heap_graph_class_find_descendants**

Given a list of classes as ancestor classes, return all the classes that
descend from them.
Returns: TableOrSubquery, Table of the schema (id JOINID(heap_graph_class.id), ancestor_class_id JOINID(heap_graph_class.id), ancestor_class_name STRING) id: `id` of the class as in heap_graph_class ancestor_class_id: `id` of the ancestor class as given in the input ancestor_class_name: `name` of the ancestor class as in heap_graph_class

| Argument | Type | Description |
|---|---|---|
| ancestor_class_ids | TableOrSubquery | ancestor class `id`s from the heap_graph_class table containing a single column: `id` |

### android.memory.heap_graph.class_summary_tree

#### Views/Tables

**android_heap_graph_class_summary_tree**

TABLE
Table containing all the Android heap graphs in the trace converted to a
shortest-path tree and then aggregated by class name.

This table contains a "flamegraph-like" representation of the contents of the
heap graph.

| Column | Type | Description |
|---|---|---|
| graph_sample_ts | TIMESTAMP | The timestamp the heap graph was dumped at. |
| upid | JOINID(process.id) | The upid of the process. |
| id | LONG | The id of the node in the class tree. |
| parent_id | LONG | The parent id of the node in the class tree or NULL if this is the root. |
| name | STRING | The name of the class. |
| root_type | STRING | A string describing the type of Java root if this node is a root or NULL if this node is not a root. |
| self_count | LONG | The count of objects with the same class name and the same path to the root. |
| self_size | LONG | The size of objects with the same class name and the same path to the root. |
| cumulative_count | LONG | The sum of `self_count` of this node and all descendants of this node. |
| cumulative_size | LONG | The sum of `self_size` of this node and all descendants of this node. |

### android.memory.heap_graph.dominator_tree

#### Views/Tables

**heap_graph_dominator_tree**

TABLE
All reachable heap graph objects, their immediate dominators and summary of
their dominated sets.
The heap graph dominator tree is calculated by stdlib graphs.dominator_tree.
Each reachable object is a node in the dominator tree, their immediate
dominator is their parent node in the tree, and their dominated set is all
their descendants in the tree. All size information come from the
heap_graph_object prelude table.

| Column | Type | Description |
|---|---|---|
| id | LONG | Heap graph object id. |
| idom_id | LONG | Immediate dominator object id of the object. If the immediate dominator is the "super-root" (i.e. the object is a root or is dominated by multiple roots) then `idom_id` will be NULL. |
| dominated_obj_count | LONG | Count of all objects dominated by this object, self inclusive. |
| dominated_size_bytes | LONG | Total self_size of all objects dominated by this object, self inclusive. |
| dominated_native_size_bytes | LONG | Total native_size of all objects dominated by this object, self inclusive. |
| depth | LONG | Depth of the object in the dominator tree. Depth of root objects are 1. |

### android.memory.heap_graph.heap_graph_class_aggregation

#### Views/Tables

**android_heap_graph_class_aggregation**

TABLE
Class-level breakdown of the java heap.
Per type name aggregates the object stats and the dominator tree stats.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Process upid |
| graph_sample_ts | TIMESTAMP | Heap dump timestamp |
| type_id | LONG | Class type id |
| type_name | STRING | Class name (deobfuscated if available) |
| is_libcore_or_array | BOOL | Is type an instance of a libcore object (java.\*) or array |
| obj_count | LONG | Count of class instances |
| size_bytes | LONG | Size of class instances |
| native_size_bytes | LONG | Native size of class instances |
| reachable_obj_count | LONG | Count of reachable class instances |
| reachable_size_bytes | LONG | Size of reachable class instances |
| reachable_native_size_bytes | LONG | Native size of reachable class instances |
| dominated_obj_count | LONG | Count of all objects dominated by instances of this class Only applies to reachable objects |
| dominated_size_bytes | LONG | Size of all objects dominated by instances of this class Only applies to reachable objects |
| dominated_native_size_bytes | LONG | Native size of all objects dominated by instances of this class Only applies to reachable objects |

### android.memory.heap_graph.heap_graph_stats

#### Views/Tables

**android_heap_graph_stats**

TABLE
Table summarizing java heap graphs collected with the ART perfetto module.
Contains one row per heap graph, with summary statistics (e.g. total / reachable objects)
and memory stats for the corresponding process at the time of the heap dump.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | The upid of the process. |
| graph_sample_ts | TIMESTAMP | The timestamp the heap graph was dumped at. |
| process_uptime | LONG | The uptime of the process at the time of the heap graph dump. |
| total_heap_size | LONG | The total (reachable + unreachable) size of the Java heap in bytes. |
| total_native_alloc_registry_size | LONG | The total size of native allocations (registered with NativeAllocationRegistry) in bytes. Does *not* overlap with total_heap_size. |
| total_obj_count | LONG | The number of objects in the heap. |
| reachable_heap_size | LONG | The reachable size of the Java heap in bytes. |
| reachable_native_alloc_registry_size | LONG | The size of reachable native allocations (registered with NativeAllocationRegistry) in bytes. |
| reachable_obj_count | LONG | The number of reachable objects in the heap. |
| oom_score_adj | LONG | The OOM score adj of the process at the time of the heap graph dump. |
| anon_rss_and_swap_size | LONG | The anon RSS + swap size of the process (in bytes) at the time of the heap graph dump. |
| dmabuf_rss_size | LONG | The dmabuf size of the process (in bytes) at the time of the heap graph dump. |

### android.memory.heap_profile.summary_tree

#### Views/Tables

**android_heap_profile_summary_tree**

TABLE
Table summarising the amount of memory allocated by each
callstack as seen by Android native heap profiling (i.e.
profiling information collected by heapprofd).

> [!NOTE]
> **Note:** this table collapses data from all processes together into a single table.

| Column | Type | Description |
|---|---|---|
| id | LONG | The id of the callstack. A callstack in this context is a unique set of frames up to the root. |
| parent_id | LONG | The id of the parent callstack for this callstack. |
| name | STRING | The function name of the frame for this callstack. |
| mapping_name | STRING | The name of the mapping containing the frame. This can be a native binary, library, JAR or APK. |
| source_file | STRING | The name of the file containing the function. |
| line_number | LONG | The line number in the file the function is located at. |
| self_size | LONG | The amount of memory allocated and *not freed* with this function as the leaf frame. |
| cumulative_size | LONG | The amount of memory allocated and *not freed* with this function appearing anywhere on the callstack. |
| self_alloc_size | LONG | The amount of memory allocated with this function as the leaf frame. This may include memory which was later freed. |
| cumulative_alloc_size | LONG | The amount of memory allocated with this function appearing anywhere on the callstack. This may include memory which was later freed. |

### android.memory.lmk

#### Views/Tables

**android_lmk_events**

TABLE

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | timestamp of the kill being requested by lmkd |
| upid | JOINID(process.id) | upid of the process being killed |
| pid | LONG | pid of the process being killed |
| process_name | STRING | process name of the process being killed |
| oom_score_adj | LONG | oom_score_adj of the process being killed |
| kill_reason | STRING | lmkd kill_reason (matches lmkd/statslog.h kill_reasons enum) |
| kill_reason_raw | LONG | lmkd kill_reason enum value |

### android.memory.process

#### Views/Tables

**memory_oom_score_with_rss_and_swap_per_process**

TABLE
Process memory and it's OOM adjuster scores. Detects transitions, each new
interval means that either the memory or OOM adjuster score of the process changed.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp the oom_adj score or memory of the process changed |
| dur | DURATION | Duration until the next oom_adj score or memory change of the process. |
| score | LONG | oom adjuster score of the process. |
| bucket | STRING | oom adjuster bucket of the process. |
| upid | JOINID(process.id) | Upid of the process having an oom_adj update. |
| process_name | STRING | Name of the process having an oom_adj update. |
| pid | LONG | Pid of the process having an oom_adj update. |
| oom_adj_id | JOINID(slice.id) | Slice of the latest oom_adj update in the system_server. |
| oom_adj_ts | TIMESTAMP | Timestamp of the latest oom_adj update in the system_server. |
| oom_adj_dur | DURATION | Duration of the latest oom_adj update in the system_server. |
| oom_adj_track_id | JOINID(track.id) | Track of the latest oom_adj update in the system_server. Alias of `track.id`. |
| oom_adj_thread_name | STRING | Thread name of the latest oom_adj update in the system_server. |
| oom_adj_reason | STRING | Reason for the latest oom_adj update in the system_server. |
| oom_adj_trigger | STRING | Trigger for the latest oom_adj update in the system_server. |
| anon_rss | LONG | Anon RSS counter value |
| file_rss | LONG | File RSS counter value |
| shmem_rss | LONG | Shared memory RSS counter value |
| rss | LONG | Total RSS value. Sum of `anon_rss`, `file_rss` and `shmem_rss`. Returns value even if one of the values is NULL. |
| swap | LONG | Swap counter value |
| anon_rss_and_swap | LONG | Sum or `anon_rss` and `swap`. Returns value even if one of the values is NULL. |
| rss_and_swap | LONG | Sum or `rss` and `swap`. Returns value even if one of the values is NULL. |

### android.monitor_contention

#### Views/Tables

**android_monitor_contention**

TABLE
Contains parsed monitor contention slices.

| Column | Type | Description |
|---|---|---|
| blocking_method | STRING | Name of the method holding the lock. |
| blocked_method | STRING | Blocked_method without arguments and return types. |
| short_blocking_method | STRING | Blocking_method without arguments and return types. |
| short_blocked_method | STRING | Blocked_method without arguments and return types. |
| blocking_src | STRING | File location of blocking_method in form <filename:linenumber>. |
| blocked_src | STRING | File location of blocked_method in form <filename:linenumber>. |
| waiter_count | LONG | Zero indexed number of threads trying to acquire the lock. |
| blocked_utid | JOINID(thread.id) | Utid of thread holding the lock. |
| blocked_thread_name | STRING | Thread name of thread holding the lock. |
| blocking_utid | JOINID(thread.id) | Utid of thread holding the lock. |
| blocking_thread_name | STRING | Thread name of thread holding the lock. |
| blocking_tid | LONG | Tid of thread holding the lock. |
| upid | JOINID(process.id) | Upid of process experiencing lock contention. |
| process_name | STRING | Process name of process experiencing lock contention. |
| id | LONG | Slice id of lock contention. |
| ts | TIMESTAMP | Timestamp of lock contention start. |
| dur | DURATION | Wall clock duration of lock contention. |
| monotonic_dur | DURATION | Monotonic clock duration of lock contention. |
| track_id | JOINID(track.id) | Thread track id of blocked thread. |
| is_blocked_thread_main | LONG | Whether the blocked thread is the main thread. |
| blocked_thread_tid | LONG | Tid of the blocked thread |
| is_blocking_thread_main | LONG | Whether the blocking thread is the main thread. |
| blocking_thread_tid | LONG | Tid of thread holding the lock. |
| binder_reply_id | LONG | Slice id of binder reply slice if lock contention was part of a binder txn. |
| binder_reply_ts | TIMESTAMP | Timestamp of binder reply slice if lock contention was part of a binder txn. |
| binder_reply_tid | LONG | Tid of binder reply slice if lock contention was part of a binder txn. |
| pid | LONG | Pid of process experiencing lock contention. |

**android_monitor_contention_chain**

TABLE
Contains parsed monitor contention slices with the parent-child relationships.

| Column | Type | Description |
|---|---|---|
| parent_id | LONG | Id of monitor contention slice blocking this contention. |
| blocking_method | STRING | Name of the method holding the lock. |
| blocked_method | STRING | Blocked_method without arguments and return types. |
| short_blocking_method | STRING | Blocking_method without arguments and return types. |
| short_blocked_method | STRING | Blocked_method without arguments and return types. |
| blocking_src | STRING | File location of blocking_method in form <filename:linenumber>. |
| blocked_src | STRING | File location of blocked_method in form <filename:linenumber>. |
| waiter_count | LONG | Zero indexed number of threads trying to acquire the lock. |
| blocked_utid | JOINID(thread.id) | Utid of thread holding the lock. |
| blocked_thread_name | STRING | Thread name of thread holding the lock. |
| blocking_utid | JOINID(thread.id) | Utid of thread holding the lock. |
| blocking_thread_name | STRING | Thread name of thread holding the lock. |
| blocking_tid | LONG | Tid of thread holding the lock. |
| upid | JOINID(process.id) | Upid of process experiencing lock contention. |
| process_name | STRING | Process name of process experiencing lock contention. |
| id | LONG | Slice id of lock contention. |
| ts | TIMESTAMP | Timestamp of lock contention start. |
| dur | DURATION | Wall clock duration of lock contention. |
| monotonic_dur | DURATION | Monotonic clock duration of lock contention. |
| track_id | JOINID(track.id) | Thread track id of blocked thread. |
| is_blocked_thread_main | LONG | Whether the blocked thread is the main thread. |
| blocked_thread_tid | LONG | Tid of the blocked thread |
| is_blocking_thread_main | LONG | Whether the blocking thread is the main thread. |
| blocking_thread_tid | LONG | Tid of thread holding the lock. |
| binder_reply_id | LONG | Slice id of binder reply slice if lock contention was part of a binder txn. |
| binder_reply_ts | TIMESTAMP | Timestamp of binder reply slice if lock contention was part of a binder txn. |
| binder_reply_tid | LONG | Tid of binder reply slice if lock contention was part of a binder txn. |
| pid | LONG | Pid of process experiencing lock contention. |
| child_id | LONG | Id of monitor contention slice blocked by this contention. |

**android_monitor_contention_chain_thread_state**

TABLE
Contains the span join of the first waiters in the \|android_monitor_contention_chain\| with their
blocking_thread thread state.

Note that we only span join the duration where the lock was actually held and contended.
This can be less than the duration the lock was 'waited on' when a different waiter acquired the
lock earlier than the first waiter.

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice id of lock contention. |
| ts | TIMESTAMP | Timestamp of lock contention start. |
| dur | DURATION | Wall clock duration of lock contention. |
| blocking_utid | JOINID(thread.id) | Utid of the blocking |
| blocked_function | STRING | Blocked kernel function of the blocking thread. |
| state | STRING | Thread state of the blocking thread. |

**android_monitor_contention_chain_thread_state_by_txn**

VIEW
Aggregated thread_states on the 'blocking thread', the thread holding the lock.
This builds on the data from \|android_monitor_contention_chain\| and
for each contention slice, it returns the aggregated sum of all the thread states on the
blocking thread.

Note that this data is only available for the first waiter on a lock.

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice id of the monitor contention. |
| thread_state | STRING | A |
| thread_state_dur | DURATION | Total time the blocking thread spent in the |
| thread_state_count | LONG | Count of all times the blocking thread entered |

**android_monitor_contention_chain_blocked_functions_by_txn**

VIEW
Aggregated blocked_functions on the 'blocking thread', the thread holding the lock.
This builds on the data from \|android_monitor_contention_chain\| and
for each contention, it returns the aggregated sum of all the kernel
blocked function durations on the blocking thread.

Note that this data is only available for the first waiter on a lock.

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice id of the monitor contention. |
| blocked_function | STRING | Blocked kernel function in a thread state in the blocking thread during the contention. |
| blocked_function_dur | DURATION | Total time the blocking thread spent in the |
| blocked_function_count | LONG | Count of all times the blocking thread executed the |

#### Functions

**android_extract_android_monitor_contention_blocking_thread**

Returns STRING: Blocking thread

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_blocking_tid**

Returns LONG: Blocking thread tid

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_blocking_method**

Returns STRING: Blocking thread

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_short_blocking_method**

Extracts a shortened form of the blocking method name from a slice name.
The shortened form discards the parameter and return
types.
Returns STRING: Blocking thread

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_blocked_method**

Returns STRING: Blocking thread

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_short_blocked_method**

Extracts a shortened form of the monitor contention blocked method name
from a slice name. The shortened form discards the parameter and return
types.
Returns STRING: Blocking thread

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_waiter_count**

Returns LONG: Count of waiters on the lock

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_blocking_src**

Returns STRING: Blocking thread

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

**android_extract_android_monitor_contention_blocked_src**

Returns STRING: Blocking thread

| Argument | Type | Description |
|---|---|---|
| slice_name | STRING | Name of slice |

#### Table Functions

**android_monitor_contention_graph**

Returns a DAG of all Java lock contentions in a process.
Each node in the graph is a pair. Each edge connects from a node waiting on a lock to a node holding a lock. The weights of each node represent the cumulative wall time the node blocked other nodes connected to it.

| Argument | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Upid of process to generate a lock graph for. |

| Column | Type | Description |
|---|---|---|
| pprof | BYTES | Pprof of lock graph. |

### android.network_packets

#### Views/Tables

**android_network_packets**

VIEW
Android network packet events (from android.network_packets data source).

| Column | Type | Description |
|---|---|---|
| id | ID | Id of the slice. |
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Duration (non-zero only in aggregate events) |
| track_name | STRING | The track name (interface and direction) |
| package_name | STRING | Traffic package source (or uid=$X if not found) |
| iface | STRING | Traffic interface name (linux interface name) |
| direction | STRING | Traffic direction ('Transmitted' or 'Received') |
| packet_count | LONG | Number of packets in this event |
| packet_length | LONG | Number of bytes in this event (wire size) |
| packet_transport | STRING | Transport used for traffic in this event |
| packet_tcp_flags | LONG | TCP flags used by tcp frames in this event |
| socket_tag | STRING | The Android traffic tag of the network socket |
| socket_uid | LONG | The Linux user id of the network socket |
| local_port | LONG | The local port number (for udp or tcp only) |
| remote_port | LONG | The remote port number (for udp or tcp only) |
| packet_icmp_type | LONG | 1-byte ICMP type identifier. |
| packet_icmp_code | LONG | 1-byte ICMP code identifier. |
| packet_tcp_flags_int | LONG | Packet's tcp flags bitmask (e.g. FIN=0x1, SYN=0x2). |
| socket_tag_int | LONG | Packet's socket tag as an integer. |

#### Macros

**android_network_uptime_spans**

Computes network uptime spans based on an idle timeout model.

It is common in networking to have an interface active for some time after
use. For example, mobile networks are often connected for 10 or more seconds
after the last packet is sent or received. This macro simulates this timeout
and returns spans that approximate the underlying connected regions.
Returns: TableOrSubquery,

| Argument | Type | Description |
|---|---|---|
| src | TableOrSubquery | A table/view/subquery containing the network events to apply the idle timeout model to. The table must contain all partition_columns, ts, dur, packet_count, and packet_length. |
| partition_columns | ColumnNameList | A parenthesized set of columns to partition the analysis by. |
| timeout | Expr | The idle timeout, expressed in nanoseconds. |

**android_network_uptime_cost**

Compute the per-row uptime cost of network activity.

It is common in networking to have an interface active for some time after
use. For example, mobile networks are often connected for 10 or more seconds
after the last packet is sent or received. This macro computes a cost factor
indicating how much each row impacts the idle timer.

For example, assuming a 10s timeout, the first packet will extend the timeout
10s in the future, and be assigned 10s of cost. If a packet arrives 4s later,
it pushes the timer an additional 4s, receiving 4s of cost. In this simple
case, cost is MIN(ts-last_packet_ts, timeout).

The complication is that network events can be aggregates, with more than one
packet. In such cases, we end up with a span with non-zero duration, rather
than an instant, and no easy way to compute time since the last packet.

The solution is to detect overlap regions and compute cost for the region as
a whole. The first event in each group receives the standard uptime cost as
described above. Each group has an additional cost equal to the duration of
the group which is distributed using packet count as weight.

For example (times in seconds, no partition, and 10 second timeout):

`ts=5, dur=0, packet_count=1 -> group=1, uptime_cost=10
ts=7, dur=0, packet_count=1 -> group=2, uptime_cost=2
ts=20, dur=5, packet_count=9 -> group=3, uptime_cost=14.5
ts=22, dur=0, packet_count=1 -> group=3, uptime_cost=0.5` The third group spans ts=20 to ts=25, with a timeout at ts=35. This gives the
group a total cost of 15 which is distributed between the two rows. The 3rd
row receives 10s for being first, and 9/10 the duration cost (5\*9/10=4.5).

The returned table schema is (id ID, uptime_cost INT64) where uptime cost is
in nanoseconds.
Returns: TableOrSubquery,

| Argument | Type | Description |
|---|---|---|
| src | TableOrSubquery | A table/view/subquery containing the network events to apply the idle timeout model to. The table must contain all partition_columns, id, ts, dur, and packet_count. |
| partition_columns | ColumnNameList | A parenthesized set of columns to partition the analysis by. |
| timeout | Expr | The idle timeout, expressed in nanoseconds. |

### android.oom_adjuster

#### Views/Tables

**android_oom_adj_intervals**

VIEW
All oom adj state intervals across all processes along with the reason for the state update.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp the oom_adj score of the process changed |
| dur | DURATION | Duration until the next oom_adj score change of the process. |
| score | LONG | oom_adj score of the process. |
| bucket | STRING | oom_adj bucket of the process. |
| upid | JOINID(process.id) | Upid of the process having an oom_adj update. |
| process_name | STRING | Name of the process having an oom_adj update. |
| oom_adj_id | LONG | Slice id of the latest oom_adj update in the system_server. |
| oom_adj_ts | TIMESTAMP | Timestamp of the latest oom_adj update in the system_server. |
| oom_adj_dur | DURATION | Duration of the latest oom_adj update in the system_server. |
| oom_adj_track_id | JOINID(track.id) | Track id of the latest oom_adj update in the system_server |
| oom_adj_thread_name | STRING | Thread name of the latest oom_adj update in the system_server. |
| oom_adj_reason | STRING | Reason for the latest oom_adj update in the system_server. |
| oom_adj_trigger | STRING | Trigger for the latest oom_adj update in the system_server. |

#### Functions

**android_oom_adj_score_to_bucket_name**

Converts an oom_adj score Integer to String sample name.
One of: cached, background, job, foreground_service, bfgs, foreground and
system.
Returns STRING: Returns the sample bucket based on the oom score.

| Argument | Type | Description |
|---|---|---|
| oom_score | LONG | `oom_score` value |

**android_oom_adj_score_to_detailed_bucket_name**

Converts an oom_adj score Integer to String bucket name.
Deprecated: use `android_oom_adj_score_to_bucket_name` instead.
Returns STRING: Returns the oom_adj bucket.

| Argument | Type | Description |
|---|---|---|
| value | LONG | oom_adj score. |
| android_appid | LONG | android_app id of the process. |

### android.power_rails

#### Views/Tables

**android_power_rails_counters**

TABLE
Android power rails counters data.
For details see: <https://perfetto.dev/docs/data-sources/battery-counters#odpm>
NOTE: Requires dedicated hardware - table is only populated on Pixels.

| Column | Type | Description |
|---|---|---|
| id | ID(counter.id) | `counter.id` |
| ts | TIMESTAMP | Timestamp of the energy measurement. |
| dur | DURATION | Time until the next energy measurement. |
| power_rail_name | STRING | Power rail name. Alias of `counter_track.name`. |
| raw_power_rail_name | STRING | Raw power rail name. |
| energy_since_boot | DOUBLE | Energy accumulated by this rail since boot in microwatt-seconds (uWs) (AKA micro-joules). Alias of `counter.value`. |
| energy_since_boot_at_end | DOUBLE | Energy accumulated by this rail at next energy measurement in microwatt-seconds (uWs) (AKA micro-joules). Alias of `counter.value` of the next meaningful (with value change) counter value. |
| average_power | DOUBLE | Average power in mW (milliwatts) over between ts and the next energy measurement. |
| energy_delta | DOUBLE | The change of energy accumulated by this rails since the last measurement in microwatt-seconds (uWs) (AKA micro-joules). |
| track_id | JOINID(track.id) | Power rail track id. Alias of `counter_track.id`. |
| value | DOUBLE | DEPRECATED. Use `energy_since_boot` instead. |

**android_power_rails_metadata**

TABLE
High level metadata about each of the power rails.

| Column | Type | Description |
|---|---|---|
| power_rail_name | STRING | Power rail name. Alias of `counter_track.name`. |
| raw_power_rail_name | STRING | Raw power rail name from the hardware. |
| friendly_name | STRING | User-friendly name for the power rail. |
| track_id | JOINID(track.id) | Power rail track id. Alias of `counter_track.id`. |
| subsystem_name | STRING | Subsystem name that this power rail belongs to. |
| machine_id | JOINID(machine.id) | The device the power rail is associated with. |

### android.process_metadata

#### Views/Tables

**android_process_metadata**

TABLE
Data about packages running on the process.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Process upid. |
| pid | LONG | Process pid. |
| process_name | STRING | Process name. |
| uid | LONG | Android app UID. |
| shared_uid | BOOL | Whether the UID is shared by multiple packages. |
| user_id | LONG | Android user id for multi-user devices |
| user_type | STRING | Type of the Android user (e.g., HEADLESS, SECONDARY) |
| package_name | STRING | Name of the packages running in this process. |
| version_code | LONG | Package version code. |
| debuggable | LONG | Whether package is debuggable. |
| is_kernel_task | BOOL | Whether the task is kernel or not |

#### Functions

**android_is_kernel_task**

Returns true if the process is a kernel task.
Returns BOOL: True for kernel tasks

| Argument | Type | Description |
|---|---|---|
| upid | LONG | Queried process |

### android.screen_state

#### Views/Tables

**android_screen_state**

TABLE
Table of the screen state - on, off or doze (always on display).

| Column | Type | Description |
|---|---|---|
| id | ID | ID. |
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Duration. |
| simple_screen_state | STRING | Simplified screen state: 'unknown', 'off', 'doze' (AoD) or 'on' |
| short_screen_state | STRING | Full screen state, adding VR and suspended-while-displaying states. |
| screen_state | STRING | Human-readable string. |

### android.screenshots

#### Views/Tables

**android_screenshots**

TABLE
Screenshot slices, used in perfetto UI.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Id of the screenshot slice. |
| ts | TIMESTAMP | Slice timestamp. |
| dur | DURATION | Slice duration, should be typically 0 since screeenshot slices are of instant type. |
| name | STRING | Slice name. |

### android.services

#### Views/Tables

**android_service_bindings**

TABLE
All service bindings from client app to server app.

| Column | Type | Description |
|---|---|---|
| client_oom_score | LONG | OOM score of client process making the binding. |
| client_process | STRING | Name of client process making the binding. |
| client_thread | STRING | Name of client thread making the binding. |
| client_pid | LONG | Pid of client process making the binding. |
| client_tid | LONG | Tid of client process making the binding. |
| client_upid | JOINID(process.id) | Upid of client process making the binding. |
| client_utid | JOINID(thread.id) | Utid of client thread making the binding. |
| client_ts | TIMESTAMP | Timestamp the client process made the request. |
| client_dur | DURATION | Duration of the client binding request. |
| server_oom_score | LONG | OOM score of server process getting bound to. |
| server_process | STRING | Name of server process getting bound to |
| server_thread | STRING | Name of server thread getting bound to. |
| server_pid | LONG | Pid of server process getting bound to. |
| server_tid | LONG | Tid of server process getting bound to. |
| server_upid | JOINID(process.id) | Upid of server process getting bound to. |
| server_utid | JOINID(thread.id) | Utid of server process getting bound to. |
| server_ts | TIMESTAMP | Timestamp the server process got bound to. |
| server_dur | DURATION | Duration of the server process handling the binding. |
| token | STRING | Unique binder identifier for the Service binding. |
| act | STRING | Intent action name for the service binding. |
| cmp | STRING | Intent component name for the service binding. |
| flg | STRING | Intent flag for the service binding. |
| bind_seq | LONG | Monotonically increasing id for the service binding. |

### android.slices

#### Functions

**android_standardize_slice_name**

Some slice names have params in them. This functions removes them to make it
possible to aggregate by name.
Some examples are:

- Lock/monitor contention slices. The name includes where the lock contention is in the code. That part is removed.
- DrawFrames/ooFrame. The name also includes the frame number.
- Apk/oat/dex loading: The name of the apk is removed Returns STRING: Simplified name.

| Argument | Type | Description |
|---|---|---|
| name | STRING | The raw slice name. |

### android.startup.startup_breakdowns

#### Views/Tables

**android_startup_opinionated_breakdown**

TABLE
Blended thread state and slice breakdown blocking app startups.

Each row blames a unique period during an app startup with a reason
derived from the slices and thread states on the main thread.

Some helpful events to enables are binder transactions, ART, am and view.

| Column | Type | Description |
|---|---|---|
| startup_id | JOINID(android_startups.startup_id) | Startup id. |
| slice_id | JOINID(slice.id) | Id of relevant slice blocking startup. |
| thread_state_id | JOINID(thread_state.id) | Id of thread_state blocking startup. |
| ts | TIMESTAMP | Timestamp of an exclusive interval during the app startup with a single latency reason. |
| dur | DURATION | Duration of an exclusive interval during the app startup with a single latency reason. |
| reason | STRING | Cause of delay during an exclusive interval of the app startup. |

### android.startup.startups

#### Views/Tables

**android_startup_processes**

TABLE
Maps a startup to the set of processes that handled the activity start.

The vast majority of cases should be a single process. However it is
possible that the process dies during the activity startup and is respawned.

| Column | Type | Description |
|---|---|---|
| startup_id | LONG | Startup id. |
| upid | JOINID(process.id) | Upid of process on which activity started. |
| pid | LONG | Pid of process on which activity started. |
| startup_type | STRING | Type of the startup. |

**android_startups**

VIEW
All activity startups in the trace by startup id.
Populated by different scripts depending on the platform version/contents.

| Column | Type | Description |
|---|---|---|
| startup_id | ID | Startup id. |
| ts | TIMESTAMP | Timestamp of startup start. |
| ts_end | LONG | Timestamp of startup end. |
| dur | DURATION | Startup duration. |
| package | STRING | Package name. |
| startup_type | STRING | Startup type. |

**android_startup_threads**

VIEW
Maps a startup to the set of threads on processes that handled the
activity start.

| Column | Type | Description |
|---|---|---|
| startup_id | LONG | Startup id. |
| ts | TIMESTAMP | Timestamp of start. |
| dur | DURATION | Duration of startup. |
| upid | JOINID(process.id) | Upid of process involved in startup. |
| pid | LONG | Pid if process involved in startup. |
| utid | JOINID(thread.id) | Utid of the thread. |
| tid | LONG | Tid of the thread. |
| thread_name | STRING | Name of the thread. |
| is_main_thread | BOOL | Thread is a main thread. |

**android_thread_slices_for_all_startups**

VIEW
All the slices for all startups in trace.

Generally, this view should not be used. Instead, use one of the view functions related
to the startup slices which are created from this table.

| Column | Type | Description |
|---|---|---|
| startup_ts | TIMESTAMP | Timestamp of startup. |
| startup_ts_end | LONG | Timestamp of startup end. |
| startup_id | LONG | Startup id. |
| utid | JOINID(thread.id) | UTID of thread with slice. |
| tid | LONG | Tid of thread. |
| thread_name | STRING | Name of thread. |
| is_main_thread | BOOL | Whether it is main thread. |
| arg_set_id | ARGSETID | Arg set id. |
| slice_id | JOINID(slice.id) | Slice id. |
| slice_name | STRING | Name of slice. |
| slice_ts | TIMESTAMP | Timestamp of slice start. |
| slice_dur | LONG | Slice duration. |

**android_class_loading_for_startup**

VIEW
A Perfetto view that lists matching slices for class loading during app startup.

| Column | Type | Description |
|---|---|---|
| slice_id | JOINID(slice.id) | Id of the slice. |
| startup_id | LONG | Startup id. |
| slice_name | STRING | Name of the slice. |
| slice_ts | TIMESTAMP | Timestamp of start of the slice. |
| slice_dur | DURATION | Duration of the slice. |
| thread_name | STRING | Name of the thread with the slice. |
| tid | LONG | Tid of the thread with the slice. |
| arg_set_id | ARGSETID | Arg set id. |

#### Functions

**android_sum_dur_for_startup_and_slice**

Returns duration of startup for slice name.

Sums duration of all slices of startup with provided name.
Returns LONG: Sum of duration.

| Argument | Type | Description |
|---|---|---|
| startup_id | LONG | Startup id. |
| slice_name | STRING | Slice name. |

**android_sum_dur_on_main_thread_for_startup_and_slice**

Returns duration of startup for slice name on main thread.

Sums duration of all slices of startup with provided name only on main thread.
Returns LONG: Sum of duration.

| Argument | Type | Description |
|---|---|---|
| startup_id | LONG | Startup id. |
| slice_name | STRING | Slice name. |

#### Table Functions

**android_slices_for_startup_and_slice_name**

Given a startup id and GLOB for a slice name, returns matching slices with data.

| Argument | Type | Description |
|---|---|---|
| startup_id | LONG | Startup id. |
| slice_name | STRING | Glob of the slice. |

| Column | Type | Description |
|---|---|---|
| slice_id | JOINID(slice.id) | Id of the slice. |
| slice_name | STRING | Name of the slice. |
| slice_ts | TIMESTAMP | Timestamp of start of the slice. |
| slice_dur | DURATION | Duration of the slice. |
| thread_name | STRING | Name of the thread with the slice. |
| tid | LONG | Tid of the thread with the slice. |
| arg_set_id | ARGSETID | Arg set id. |

**android_binder_transaction_slices_for_startup**

Returns binder transaction slices for a given startup id with duration over threshold.

| Argument | Type | Description |
|---|---|---|
| startup_id | LONG | Startup id. |
| threshold | DOUBLE | Only return slices with duration over threshold. |

| Column | Type | Description |
|---|---|---|
| id | LONG | Slice id. |
| slice_dur | DURATION | Slice duration. |
| thread_name | STRING | Name of the thread with slice. |
| process | STRING | Name of the process with slice. |
| arg_set_id | ARGSETID | Arg set id. |
| is_main_thread | BOOL | Whether is main thread. |

### android.startup.time_to_display

#### Views/Tables

**android_startup_time_to_display**

TABLE
Startup metric defintions, which focus on the observable time range:
TTID - Time To Initial Display

- <https://developer.android.com/topic/performance/vitals/launch-time#time-initial>
- end of first RenderThread.DrawFrame - bindApplication TTFD - Time To Full Display
- <https://developer.android.com/topic/performance/vitals/launch-time#retrieve-TTFD>
- end of next RT.DrawFrame, after reportFullyDrawn called - bindApplication Googlers: see go/android-performance-metrics-glossary for details.

| Column | Type | Description |
|---|---|---|
| startup_id | LONG | Startup id. |
| time_to_initial_display | LONG | Time to initial display (TTID) |
| time_to_full_display | LONG | Time to full display (TTFD) |
| ttid_frame_id | LONG | `android_frames.frame_id` of frame for initial display |
| ttfd_frame_id | LONG | `android_frames.frame_id` of frame for full display |
| upid | JOINID(process.id) | `process.upid` of the startup |

### android.statsd

#### Views/Tables

**android_statsd_atoms**

VIEW
Statsd atoms.

A subset of the slice table containing statsd atom instant events.

| Column | Type | Description |
|---|---|---|
| id | LONG | Unique identifier for this slice. |
| ts | TIMESTAMP | The timestamp at the start of the slice. |
| dur | DURATION | The duration of the slice. |
| arg_set_id | ARGSETID | The id of the argument set associated with this slice. |
| thread_instruction_count | LONG | The value of the CPU instruction counter at the start of the slice. This column will only be populated if thread instruction collection is enabled with track_event. |
| thread_instruction_delta | LONG | The change in value of the CPU instruction counter between the start and end of the slice. This column will only be populated if thread instruction collection is enabled with track_event. |
| track_id | JOINID(track.id) | The id of the track this slice is located on. |
| category | STRING | The "category" of the slice. If this slice originated with track_event, this column contains the category emitted. Otherwise, it is likely to be null (with limited exceptions). |
| name | STRING | The name of the slice. The name describes what was happening during the slice. |
| depth | LONG | The depth of the slice in the current stack of slices. |
| parent_id | LONG | The id of the parent (i.e. immediate ancestor) slice for this slice. |
| thread_ts | TIMESTAMP | The thread timestamp at the start of the slice. This column will only be populated if thread timestamp collection is enabled with track_event. |
| thread_dur | LONG | The thread time used by this slice. This column will only be populated if thread timestamp collection is enabled with track_event. |

### android.surfaceflinger

#### Views/Tables

**android_app_to_sf_frame_timeline_match**

TABLE
Match the frame timeline on the app side with the frame timeline on the SF side.
In cases where there are multiple layers drawn, there would be separate frame timeline
slice for each of the layers. GROUP BY is used to deduplicate these rows.

| Column | Type | Description |
|---|---|---|
| app_upid | JOINID(process.upid) | upid of the app. |
| app_vsync | LONG | vsync id of the app. |
| sf_upid | JOINID(process.upid) | upid of surfaceflinger process. |
| sf_vsync | LONG | vsync id for surfaceflinger. |

### android.suspend

#### Views/Tables

**android_suspend_state**

TABLE
Table of suspended and awake slices.

Selects either the minimal or full ftrace source depending on what's
available, marks suspended periods, and complements them to give awake
periods.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp |
| dur | DURATION | Duration |
| power_state | STRING | 'awake' or 'suspended' |

### android.thread

#### Functions

**android_standardize_thread_name**

Standardizes an Android thread name by extracting its core identifier to make it
possible to aggregate by name.

Removes extra parts of a thread name, like identifiers, leaving only the main prefix.
Splits the name at ('-', '\[', ':' , ' ').

Some Examples:
Given thread_name = "RenderThread-1\[123\]",
returns "RenderThread".

Given thread_name = "binder:5543_E"
returns "binder".

Given thread_name = "pool-3-thread-5",
returns "pool".

Given thread_name = "MainThread",
returns "MainThread".
Returns STRING: Simplified name

| Argument | Type | Description |
|---|---|---|
| thread_name | STRING | The full android thread name to be processed. |

### android.user_list

#### Views/Tables

**android_user_list**

VIEW
Contains information about Android users in the trace.

This is populated by the `android.user_list` data-source which lives in
traced_probes and is available on default from 26Q2+ devices.

> [!NOTE]
> **Note:** `users` here corresponds to Android users *not* Linux users. So this is not about Linux uids (which in Android correspons to different apps).

| Column | Type | Description |
|---|---|---|
| android_user_id | LONG | The Android user id. Often useful to join with `android_process_metadata.user_id` |
| type | STRING | A string "enum" indicating the type of the user according to the system. Will be one for a few constant values e.g. HEADLESS, SECONDARY, GUEST. |

### android.wakeups

#### Views/Tables

**android_wakeups**

TABLE
Table of parsed wakeup / suspend failure events with suspend backoff.

Certain wakeup events may have multiple causes. When this occurs we
split those causes into multiple rows in this table with the same ts
and raw_wakeup values.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp. |
| dur | DURATION | Duration for which we blame the wakeup for wakefulness. This is the suspend backoff duration if one exists, or the lesser of (5 seconds, time to next suspend event). |
| raw_wakeup | STRING | Original wakeup string from the kernel. |
| on_device_attribution | STRING | Wakeup attribution, as determined on device. May be absent. |
| type | STRING | One of 'normal' (device woke from sleep), 'abort_pending' (suspend failed due to a wakeup that was scheduled by a device during the suspend process), 'abort_last_active' (suspend failed, listing the last active device) or 'abort_other' (suspend failed for another reason). |
| item | STRING | Individual wakeup cause. Usually the name of the device that cause the wakeup, or the raw message in the 'abort_other' case. |
| suspend_quality | STRING | 'good' or 'bad'. 'bad' means failed or short such that suspend backoff is triggered. |
| backoff_state | STRING | 'new', 'continue' or NULL. Set if suspend backoff is triggered. |
| backoff_reason | STRING | 'short', 'failed' or NULL. Set if suspend backoff is triggered. |
| backoff_count | LONG | Number of times suspend backoff has occurred, or NULL. Set if suspend backoff is triggered. |
| backoff_millis | LONG | Next suspend backoff duration, or NULL. Set if suspend backoff is triggered. |

### android.winscope.inputmethod

#### Views/Tables

**android_inputmethod_clients**

VIEW
Android inputmethod clients state dumps (from android.inputmethod data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Dump id |
| ts | TIMESTAMP | Timestamp when the dump was triggered |
| arg_set_id | ARGSETID | Extra args parsed from the proto message |

**android_inputmethod_manager_service**

VIEW
Android inputmethod manager service state dumps (from android.inputmethod data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Dump id |
| ts | TIMESTAMP | Timestamp when the dump was triggered |
| arg_set_id | ARGSETID | Extra args parsed from the proto message |

**android_inputmethod_service**

VIEW
Android inputmethod service state dumps (from android.inputmethod data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Dump id |
| ts | TIMESTAMP | Timestamp when the dump was triggered |
| arg_set_id | ARGSETID | Extra args parsed from the proto message |

### android.winscope.rect

#### Views/Tables

**android_winscope_rect**

VIEW
Android Winscope rects.

| Column | Type | Description |
|---|---|---|
| id | LONG | Rect id |
| x | DOUBLE | x |
| y | DOUBLE | y |
| w | DOUBLE | w |
| h | DOUBLE | h |

**android_winscope_transform**

VIEW
Android Winscope transforms.

| Column | Type | Description |
|---|---|---|
| id | LONG | Transform id |
| dsdx | DOUBLE | dsdx |
| dtdx | DOUBLE | dtdx |
| tx | DOUBLE | tx |
| dtdy | DOUBLE | dtdy |
| dsdy | DOUBLE | dsdy |
| ty | DOUBLE | ty |

**android_winscope_trace_rect**

VIEW
Android Winscope trace rects.

| Column | Type | Description |
|---|---|---|
| id | LONG | Trace rect id |
| rect_id | LONG | Rect id |
| group_id | LONG | Group id |
| depth | LONG | Depth |
| is_spy | LONG | Is spy rect |
| is_visible | LONG | Is visible |
| opacity | DOUBLE | Opacity |
| transform_id | LONG | Transform id |
| border_width | LONG | Border width |
| border_color | DOUBLE | Border color |

### android.winscope.surfaceflinger

#### Views/Tables

**android_surfaceflinger_transaction**

VIEW
Android surfaceflinger transactions (from android.surfaceflinger.transactions data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Row id |
| snapshot_id | LONG | Snapshot id |
| arg_set_id | LONG | Arg set id |
| transaction_id | LONG | Transaction id |
| pid | LONG | PID |
| uid | LONG | UID |
| layer_id | LONG | Layer id |
| display_id | LONG | Display id |
| flags_id | LONG | Flags id |
| transaction_type | STRING | Transaction type |

**android_surfaceflinger_transaction_flag**

VIEW
Android surfaceflinger transaction flags.

| Column | Type | Description |
|---|---|---|
| flags_id | LONG | Flags id |
| flag | STRING | Flag |

**android_surfaceflinger_display**

VIEW
Android surfaceflinger displays (from android.surfaceflinger.layers data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Id |
| snapshot_id | LONG | Snapshot id |
| is_on | LONG | Is on |
| is_virtual | LONG | Is virtual |
| trace_rect_id | LONG | Trace rect id |
| display_id | LONG | Display id |
| display_name | STRING | Display name |

**android_winscope_fill_region**

VIEW
Android surfaceflinger input rect fill regions (from android.surfaceflinger.layers data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Fill region id |
| trace_rect_id | LONG | Trace rect id |
| rect_id | LONG | Rect id |

### android.winscope.transitions

#### Views/Tables

**android_window_manager_shell_transition_participants**

VIEW
Android transition participants (from com.android.wm.shell.transition data source).

| Column | Type | Description |
|---|---|---|
| transition_id | LONG | Transition id |
| layer_id | LONG | Layer participant |
| window_id | LONG | Window participant |

**android_window_manager_shell_transition_protos**

VIEW
Android transition protos (from com.android.wm.shell.transition data source).

| Column | Type | Description |
|---|---|---|
| transition_id | LONG | Transition id |
| base64_proto_id | LONG | Base64 proto id |

### android.winscope.viewcapture

#### Views/Tables

**android_viewcapture**

VIEW
Android viewcapture (from android.viewcapture data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Snapshot id |
| ts | TIMESTAMP | Timestamp when snapshot was triggered |
| arg_set_id | ARGSETID | Extra args parsed from proto message |
| package_name | STRING | Package name deinterned from proto message |
| window_name | STRING | Window name deinterned from proto message |

**android_viewcapture_view**

VIEW
Android viewcapture view (from android.viewcapture data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Row id |
| snapshot_id | LONG | Snapshot id |
| arg_set_id | ARGSETID | Extra args parsed from proto message |
| node_id | LONG | Id from proto message |
| hashcode | LONG | Hashcode from proto message |
| is_visible | LONG | Is visible computed from proto message and view position |
| parent_id | LONG | Parent id from proto message |
| view_id | STRING | View id deinterned from proto message |
| class_name | STRING | Class name deinterned from proto message |
| trace_rect_id | LONG | Trace rect id |

### android.winscope.windowmanager

#### Views/Tables

**android_windowmanager**

VIEW
Android WindowManager (from android.windowmanager data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Snapshot id |
| ts | TIMESTAMP | Timestamp when the snapshot was triggered |
| arg_set_id | ARGSETID | Extra args parsed from the proto message |
| base64_proto_id | LONG | Raw proto message |
| focused_display_id | LONG | Focused display id for this snapshot |
| has_invalid_elapsed_ts | BOOL | Indicates whether snapshot was recorded without elapsed timestamp |

**android_windowmanager_windowcontainer**

VIEW
Android WindowManager WindowContainer (from android.windowmanager data source).

| Column | Type | Description |
|---|---|---|
| id | LONG | Row id |
| snapshot_id | LONG | Snapshot id |
| arg_set_id | ARGSETID | Extra args parsed from the proto message |
| base64_proto_id | LONG | Raw proto message |
| title | STRING | The window container's title |
| token | LONG | The window container's token |
| parent_token | LONG | The parent window container's token |
| child_index | LONG | The index of this window container within the parent's children |
| is_visible | BOOL | The window container visibility |
| window_rect_id | LONG | The rect corresponding to this window container |
| container_type | STRING | The window container type e.g. DisplayContent, TaskFragment |
| name_override | STRING | Optional name override for some container types |

## Package: v8

### v8.jit

#### Views/Tables

**v8_isolate**

VIEW
A V8 Isolate instance. A V8 Isolate represents an isolated instance of the V8
engine.

| Column | Type | Description |
|---|---|---|
| v8_isolate_id | LONG | Unique V8 isolate id. |
| upid | JOINID(process.id) | Process the isolate was created in. |
| internal_isolate_id | LONG | Internal id used by the v8 engine. Unique in a process. |
| embedded_blob_code_start_address | LONG | Absolute start address of the embedded code blob. |
| embedded_blob_code_size | LONG | Size in bytes of the embedded code blob. |
| code_range_base_address | LONG | Base address of the code range if the isolate defines one. |
| code_range_size | LONG | Size of a code range if the isolate defines one. |
| shared_code_range | LONG | Whether the code range for this Isolate is shared with others in the same process. There is at max one such shared code range per process. |
| embedded_blob_code_copy_start_address | LONG | Used when short builtin calls are enabled, where embedded builtins are copied into the CodeRange so calls can be nearer. |

**v8_js_script**

VIEW
Represents a script that was compiled to generate code. Some V8 code is
generated out of scripts and will reference a V8Script other types of code
will not (e.g. builtins).

| Column | Type | Description |
|---|---|---|
| v8_js_script_id | LONG | Unique V8 JS script id. |
| v8_isolate_id | LONG | V8 isolate this script belongs to (joinable with `v8_isolate.v8_isolate_id`). |
| internal_script_id | LONG | Script id used by the V8 engine. |
| script_type | STRING | Script type. |
| name | STRING | Script name. |
| source | STRING | Actual contents of the script. |

**v8_wasm_script**

VIEW
Represents one WASM script.

| Column | Type | Description |
|---|---|---|
| v8_wasm_script_id | LONG | Unique V8 WASM script id. |
| v8_isolate_id | LONG | V8 Isolate this script belongs to (joinable with `v8_isolate.v8_isolate_id`). |
| internal_script_id | LONG | Script id used by the V8 engine. |
| url | STRING | URL of the source. |
| wire_bytes | BYTES | Raw wire bytes of the script. |
| source | STRING | Actual source code of the script. |

**v8_js_function**

VIEW
Represents a v8 Javascript function.

| Column | Type | Description |
|---|---|---|
| v8_js_function_id | LONG | Unique V8 JS function id. |
| name | STRING | Function name. |
| v8_js_script_id | LONG | Script where the function is defined (joinable with `v8_js_script.v8_js_script_id`). |
| is_toplevel | BOOL | Whether this function represents the top level script. |
| kind | STRING | Function kind (e.g. regular function or constructor). |
| line | LONG | Line in script where function is defined. Starts at 1. |
| col | LONG | Column in script where function is defined. Starts at 1. |

## Package: intervals

### intervals.intersect

#### Macros

**interval_self_intersect**

Given a list of intervals (ts, dur), this macro generates a list of interval
end points as well as the intervals that intersect with those points.

e.g. input (10, 20), (20, 25)

`10 30
A |---|
B|---|
20 45` would generate the output:

`ts,dur,group_id,id,interval_ends_at_ts
10,10,1,A,0
20,10,2,A,0
20,10,2,B,0
30,15,3,A,1
30,15,3,B,0
45,0,4,B,1` Runtime is O(n log n + m), where n is the number of intervals and m
is the size of the output.
Returns: TableOrSubquery,

| Argument | Type | Description |
|---|---|---|
| intervals | TableOrSubquery | Table or subquery containing interval data. |

### intervals.overlap

#### Macros

**intervals_overlap_count**

Compute the distribution of the overlap of the given intervals over time.

Each interval is a (ts, dur) pair and the overlap represented as a (ts, value)
counter, with the value corresponding to the number of intervals that overlap
the given timestamp and interval until the next timestamp.
Returns: TableOrSubquery, The returned table has the schema (ts TIMESTAMP, value LONG). \|ts\| is the timestamp when the number of open segments changed. \|value\| is the number of open segments.

| Argument | Type | Description |
|---|---|---|
| segments | TableOrSubquery | Table or subquery containing interval data. |
| ts_column | ColumnName | Column containing interval starts (usually `ts`). |
| dur_column | ColumnName | Column containing interval durations (usually `dur`). |

**intervals_overlap_count_by_group**

Compute the distribution of the overlap of the given intervals over time from
slices in a same group.

Each interval is a (ts, dur, group) triple and the overlap represented as a
(ts, value, group) counter, with the value corresponding to the number of
intervals that belong to the same group and overlap the given timestamp and
interval until the next timestamp.
Returns: TableOrSubquery, The returned table has the schema (ts INT64, value UINT32, group_name) where the type of group_name is the same as that in \|segments\|. \|ts\| is the timestamp when the number of open segments changed. \|value\| is the number of open segments. \|group_name\| is the name of a group used for the overlap calculation.

| Argument | Type | Description |
|---|---|---|
| segments | TableOrSubquery | Table or subquery containing interval data. |
| ts_column | ColumnName | Column containing interval starts (usually `ts`). |
| dur_column | ColumnName | Column containing interval durations (usually `dur`). |
| group_column | ColumnName | Column containing group name for grouping. |

**interval_merge_overlapping**

Merge intervals when they overlap to generate a minimum covering set of
intervals with no overlap. The intervals are closed (contain both endpoints)
and we consider two intervals overlapping
(a) the intervals overlap or
(b) if the end point of one interval is within epsilon of the start point
of the other.
Returns: TableOrSubquery,

| Argument | Type | Description |
|---|---|---|
| intervals | TableOrSubquery | Table or subquery containing interval data. |
| epsilon | Expr | Constant expression for a tolerance in testing overlap (usually `0`) |

**interval_merge_overlapping_partitioned**

Merge overlapping intervals within each partition group to generate a minimum
covering set of intervals with no overlap within each partition.

For each partition, this macro merges overlapping intervals into
non-overlapping intervals. The result contains intervals where at least
one input interval is active.

For example, with partition 'A':
Input: (ts=1, dur=10), (ts=5, dur=12)
Output: (ts=1, dur=16)
Returns: TableOrSubquery, The returned table has the schema (ts TIMESTAMP, dur DURATION, partitions). \|ts\| is the start of the merged interval. \|dur\| is the duration of the merged interval. \|partitions\| is all of the columns in partition_columns.

| Argument | Type | Description |
|---|---|---|
| intervals | TableOrSubquery | Table or subquery containing interval data. |
| partition_columns | ColumnNameList | Column name for partition grouping. |

## Package: counters

### counters.intervals

#### Macros

**counter_leading_intervals**

For a given counter timeline (e.g. a single counter track), returns
intervals of time where the counter has the same value. For every run
of identical values, this macro will return a row for the first one,
the last one, and a row merging all other ones. This to to facilitate
construction of counters from delta_values.

Intervals are computed in a "forward-looking" way. That is, if a counter
changes value at some timestamp, it's assumed it *just* reached that
value and it should continue to have that value until the next
value change. The final value is assumed to hold until the very end of
the trace.

For example, suppose we have the following data:

`ts=0, value=10, track_id=1
ts=0, value=10, track_id=2
ts=10, value=10, track_id=1
ts=10, value=20, track_id=2
ts=20, value=30, track_id=1
[end of trace at ts = 40]` Then this macro will generate the following intervals:

`ts=0, dur=10, value=10, track_id=1
ts=10, dur=10, value=10, track_id=1
ts=20, dur=10, value=30, track_id=1
ts=0, dur=10, value=10, track_id=2
ts=10, dur=30, value=20, track_id=2`Returns: TableOrSubquery, Table with the schema: id LONG, As passed in ts TIMESTAMP, As passed in dur DURATION, Difference to the timestamp for the leading row. track_id JOINID(track.id), As passed in value DOUBLE, As passed in next_value DOUBLE, Value for the leading row. delta_value DOUBLE Delta to the *lagging* row - note that this is not the same thing as (next_value - value).

| Argument | Type | Description |
|---|---|---|
| counter_table | TableOrSubquery | A table/view/subquery corresponding to a "counter-like" table. This table must have the columns "id" and "ts" and "track_id" and "value" corresponding to an id, timestamp, counter track_id and associated counter value. |

## Package: linux

### linux.block_io

#### Views/Tables

**linux_active_block_io_operations_by_device**

VIEW
View tracking the number of IO operations remaining in the kernel IO queue or
a block device

| Column | Type | Description |
|---|---|---|
| ts | LONG | timestamp when block_io_start or block_io_done happened |
| ops_in_queue_or_device | LONG | the number of IO operations in the kernel queue or the device |
| dev | LONG | the device processing the IO operations |

#### Functions

**linux_device_major_id**

Returns LONG: 12 bits major id

| Argument | Type | Description |
|---|---|---|
| dev | LONG | device id (userland dev_t value) |

**linux_device_minor_id**

Returns LONG: 20 bits minor id

| Argument | Type | Description |
|---|---|---|
| dev | LONG | device id (userland dev_t value) |

### linux.cpu.frequency

#### Views/Tables

**cpu_frequency_counters**

TABLE
Counter information for each frequency change for each CPU. Finds each time
region where a CPU frequency is constant.

| Column | Type | Description |
|---|---|---|
| id | LONG | Counter id. |
| track_id | JOINID(track.id) | Joinable with 'counter_track.id'. |
| ts | TIMESTAMP | Starting timestamp of the counter |
| dur | DURATION | Duration in which counter is constant and frequency doesn't change. |
| freq | LONG | Frequency in kHz of the CPU that corresponds to this counter. NULL if not found or undefined. |
| ucpu | LONG | Unique CPU id. |
| cpu | LONG | CPU that corresponds to this counter. |

### linux.cpu.idle

#### Views/Tables

**cpu_idle_counters**

TABLE
Counter information for each idle state change for each CPU. Finds each time
region where a CPU idle state is constant.

| Column | Type | Description |
|---|---|---|
| id | LONG | Counter id. |
| track_id | JOINID(track.id) | Joinable with 'counter_track.id'. |
| ts | TIMESTAMP | Starting timestamp of the counter. |
| dur | DURATION | Duration in which the counter is contant and idle state doesn't change. |
| idle | LONG | Idle state of the CPU that corresponds to this counter. An idle state of -1 is defined to be active state for the CPU, and the larger the integer, the deeper the idle state of the CPU. NULL if not found or undefined. |
| cpu | LONG | CPU that corresponds to this counter. |

### linux.cpu.idle_stats

#### Views/Tables

**cpu_idle_stats**

TABLE
Aggregates cpu idle statistics per core.

| Column | Type | Description |
|---|---|---|
| cpu | LONG | CPU core number. |
| state | LONG | CPU idle state (C-states). |
| count | LONG | The count of entering idle state. |
| dur | DURATION | Total CPU core idle state duration. |
| avg_dur | DURATION | Average CPU core idle state duration. |
| idle_percent | DOUBLE | Idle state percentage of non suspend time (C-states + P-states). |

### linux.cpu.idle_time_in_state

#### Views/Tables

**linux_per_cpu_idle_time_in_state_counters**

TABLE
Percentage counter information for sysfs cpuidle states.
For each state per cpu, report the incremental time spent in one state,
divided by time spent in all states, between two timestamps.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp. |
| machine_id | LONG | The machine this residency is calculated for. |
| state | STRING | State name. |
| cpu | LONG | CPU. |
| idle_percentage | DOUBLE | Percentage of time this cpu spent in this state. |
| total_residency | DOUBLE | Incremental time spent in this state (residency), in microseconds. |
| time_slice | LONG | Time this cpu spent in any state, in microseconds. |

**linux_cpu_idle_time_in_state_counters**

TABLE
Percentage counter information for sysfs cpuidle states.
For each state across all CPUs, report the incremental time spent in one
state, divided by time spent in all states, between two timestamps.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp. |
| machine_id | LONG | The machine this residency is calculated for. |
| state | STRING | State name. |
| idle_percentage | DOUBLE | Percentage of time all CPUS spent in this state. |
| total_residency | DOUBLE | Incremental time spent in this state (residency), in microseconds. |
| time_slice | LONG | Time all CPUS spent in any state, in microseconds. |

### linux.cpu.utilization.process

#### Views/Tables

**cpu_cycles_per_process**

TABLE
Aggregated CPU statistics for each process.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Unique process id |
| millicycles | LONG | Sum of CPU millicycles |
| megacycles | LONG | Sum of CPU megacycles |
| runtime | DURATION | Total runtime duration |
| min_freq | LONG | Minimum CPU frequency in kHz |
| max_freq | LONG | Maximum CPU frequency in kHz |
| avg_freq | LONG | Average CPU frequency in kHz |

#### Table Functions

**cpu_process_utilization_per_period**

Returns a table of process utilization per given period.
Utilization is calculated as sum of average utilization of each CPU in each
period, which is defined as a multiply of \|interval\|. For this reason
first and last period might have lower then real utilization.

| Argument | Type | Description |
|---|---|---|
| interval | LONG | Length of the period on which utilization should be averaged. |
| upid | JOINID(process.id) | Upid of the process. |

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp of start of a second. |
| utilization | DOUBLE | Sum of average utilization over period. Note: as the data is normalized, the values will be in the \[0, 1\] range. |
| unnormalized_utilization | DOUBLE | Sum of average utilization over all CPUs over period. Note: as the data is unnormalized, the values will be in the \[0, cpu_count\] range. |

**cpu_process_utilization_per_second**

Returns a table of process utilization per second.
Utilization is calculated as sum of average utilization of each CPU in each
period, which is defined as a multiply of \|interval\|. For this reason
first and last period might have lower then real utilization.

| Argument | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Upid of the process. |

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp of start of a second. |
| utilization | DOUBLE | Sum of average utilization over period. Note: as the data is normalized, the values will be in the \[0, 1\] range. |
| unnormalized_utilization | DOUBLE | Sum of average utilization over all CPUs over period. Note: as the data is unnormalized, the values will be in the \[0, cpu_count\] range. |

**cpu_cycles_per_process_in_interval**

Aggregated CPU statistics for each process in a provided interval.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Unique process id. |
| millicycles | LONG | Sum of CPU millicycles |
| megacycles | LONG | Sum of CPU megacycles |
| runtime | DURATION | Total runtime duration |
| awake_runtime | DURATION | Total runtime duration, while 'awake' (CPUs not suspended). |
| min_freq | LONG | Minimum CPU frequency in kHz |
| max_freq | LONG | Maximum CPU frequency in kHz |
| avg_freq | LONG | Average CPU frequency in kHz |

**cpu_process_utilization_in_interval**

Returns a table with process utilization over a given interval.

Utilization is computed as runtime over the duration of the interval, aggregated by UPID.
Utilization can be normalized (divide by number of cpus) or unnormalized.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Unique process id. |
| process_name | STRING | The name of the process. |
| awake_dur | LONG | Total runtime of all processes with this UPID, while 'awake' (CPUs not suspended). |
| awake_utilization | DOUBLE | Percentage of 'awake_dur' over the 'awake' duration of the interval, normalized by the number of CPUs. Values in \[0.0, 100.0\] |
| awake_unnormalized_utilization | DOUBLE | Percentage of 'awake_dur' over the 'awake' duration of the interval, unnormalized. Values in \[0.0, 100.0 \* \] |

### linux.cpu.utilization.slice

#### Views/Tables

**cpu_cycles_per_thread_slice**

TABLE
CPU cycles per each slice.

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Id of a slice. |
| name | STRING | Name of the slice. |
| utid | JOINID(thread.id) | Id of the thread the slice is running on. |
| thread_name | STRING | Name of the thread. |
| upid | JOINID(process.id) | Id of the process the slice is running on. |
| process_name | STRING | Name of the process. |
| millicycles | LONG | Sum of CPU millicycles. Null if frequency couldn't be fetched for any period during the runtime of the slice. |
| megacycles | LONG | Sum of CPU megacycles. Null if frequency couldn't be fetched for any period during the runtime of the slice. |

#### Table Functions

**cpu_cycles_per_thread_slice_in_interval**

CPU cycles per each slice in interval.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | DURATION | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Thread slice. |
| name | STRING | Name of the slice. |
| utid | JOINID(thread.id) | Thread the slice is running on. |
| thread_name | STRING | Name of the thread. |
| upid | JOINID(process.id) | Process the slice is running on. |
| process_name | STRING | Name of the process. |
| millicycles | LONG | Sum of CPU millicycles. Null if frequency couldn't be fetched for any period during the runtime of the slice. |
| megacycles | LONG | Sum of CPU megacycles. Null if frequency couldn't be fetched for any period during the runtime of the slice. |

### linux.cpu.utilization.system

#### Views/Tables

**cpu_utilization_per_second**

TABLE
Table with system utilization per second.
Utilization is calculated by sum of average utilization of each CPU every
second. For this reason first and last second might have lower then real
utilization.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp of start of a second. |
| utilization | DOUBLE | Sum of average utilization over period. Note: as the data is normalized, the values will be in the \[0, 1\] range. |
| unnormalized_utilization | DOUBLE | Sum of average utilization over all CPUs over period. Note: as the data is unnormalized, the values will be in the \[0, cpu_count\] range. |

**cpu_cycles**

TABLE
Aggregated CPU statistics for whole trace. Results in only one row.

| Column | Type | Description |
|---|---|---|
| millicycles | LONG | Sum of CPU millicycles. |
| megacycles | LONG | Sum of CPU megacycles. |
| runtime | DURATION | Total runtime of all threads running on all CPUs. |
| min_freq | LONG | Minimum CPU frequency in kHz. |
| max_freq | LONG | Maximum CPU frequency in kHz. |
| avg_freq | LONG | Average CPU frequency in kHz. |

**cpu_cycles_per_cpu**

TABLE
Aggregated CPU statistics for each CPU.

| Column | Type | Description |
|---|---|---|
| ucpu | JOINID(cpu.id) | Unique CPU id. Joinable with `cpu.id`. |
| cpu | LONG | The number of the CPU. Might not be the same as ucpu in multi machine cases. |
| millicycles | LONG | Sum of CPU millicycles. |
| megacycles | LONG | Sum of CPU megacycles. |
| runtime | DURATION | Total runtime of all threads running on CPU. |
| min_freq | LONG | Minimum CPU frequency in kHz. |
| max_freq | LONG | Maximum CPU frequency in kHz. |
| avg_freq | LONG | Average CPU frequency in kHz. |

#### Table Functions

**cpu_utilization_per_period**

Returns a table of system utilization per given period.
Utilization is calculated as sum of average utilization of each CPU in each
period, which is defined as a multiply of \|interval\|. For this reason
first and last period might have lower then real utilization.

| Argument | Type | Description |
|---|---|---|
| interval | LONG | Length of the period on which utilization should be averaged. |

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp of start of a second. |
| utilization | DOUBLE | Sum of average utilization over period. Note: as the data is normalized, the values will be in the \[0, 1\] range. |
| unnormalized_utilization | DOUBLE | Sum of average utilization over all CPUs over period. Note: as the data is unnormalized, the values will be in the \[0, cpu_count\] range. |

**cpu_cycles_in_interval**

Aggregated CPU statistics in a provided interval. Results in one row.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| millicycles | LONG | Sum of CPU millicycles. |
| megacycles | LONG | Sum of CPU megacycles. |
| runtime | DURATION | Total runtime of all threads running on all CPUs. |
| awake_runtime | DURATION | Total runtime of all threads running on all CPUs, while 'awake' (CPUs not suspended). |
| min_freq | LONG | Minimum CPU frequency in kHz. |
| max_freq | LONG | Maximum CPU frequency in kHz. |
| avg_freq | LONG | Average CPU frequency in kHz. |

**cpu_utilization_in_interval**

Returns a table of CPU utilization over a given interval.

Utilization is computed as runtime over the duration of the interval.
Utilization can be normalized (divide by number of cores) or unnormalized.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| awake_dur | LONG | Total runtime of all threads running on all CPUs, while 'awake' (CPUs not suspended). |
| awake_utilization | DOUBLE | Percentage of 'awake_dur' over the 'awake' duration of the interval, normalized by the number of CPUs. Values in \[0.0, 100.0\] |
| awake_unnormalized_utilization | DOUBLE | Percentage of 'awake_dur' over the 'awake' duration of the interval, unnormalized. Values in \[0.0, 100.0 \* \] |

**cpu_cycles_per_cpu_in_interval**

Aggregated CPU statistics for each CPU in a provided interval.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| ucpu | JOINID(cpu.id) | Unique CPU id. Joinable with `cpu.id`. |
| cpu | LONG | CPU number. |
| millicycles | LONG | Sum of CPU millicycles. |
| megacycles | LONG | Sum of CPU megacycles. |
| runtime | DURATION | Total runtime of all threads running on CPU. |
| min_freq | LONG | Minimum CPU frequency in kHz. |
| max_freq | LONG | Maximum CPU frequency in kHz. |
| avg_freq | LONG | Average CPU frequency in kHz. |

### linux.cpu.utilization.thread

#### Views/Tables

**cpu_cycles_per_thread**

TABLE
Aggregated CPU statistics for each thread.

| Column | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | Thread |
| millicycles | LONG | Sum of CPU millicycles |
| megacycles | LONG | Sum of CPU megacycles |
| runtime | DURATION | Total runtime duration |
| min_freq | LONG | Minimum CPU frequency in kHz |
| max_freq | LONG | Maximum CPU frequency in kHz |
| avg_freq | LONG | Average CPU frequency in kHz |

#### Table Functions

**cpu_thread_utilization_per_period**

Returns a table of thread utilization per given period.
Utilization is calculated as sum of average utilization of each CPU in each
period, which is defined as a multiply of \|interval\|. For this reason
first and last period might have lower then real utilization.

| Argument | Type | Description |
|---|---|---|
| interval | LONG | Length of the period on which utilization should be averaged. |
| utid | JOINID(thread.id) | Utid of the thread. |

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp of start of a second. |
| utilization | DOUBLE | Sum of average utilization over period. Note: as the data is normalized, the values will be in the \[0, 1\] range. |
| unnormalized_utilization | DOUBLE | Sum of average utilization over all CPUs over period. Note: as the data is unnormalized, the values will be in the \[0, cpu_count\] range. |

**cpu_thread_utilization_per_second**

Returns a table of thread utilization per second.
Utilization is calculated as sum of average utilization of each CPU in each
period, which is defined as a multiply of \|interval\|. For this reason
first and last period might have lower then real utilization.

| Argument | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | Utid of the thread. |

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp of start of a second. |
| utilization | DOUBLE | Sum of average utilization over period. Note: as the data is normalized, the values will be in the \[0, 1\] range. |
| unnormalized_utilization | DOUBLE | Sum of average utilization over all CPUs over period. Note: as the data is unnormalized, the values will be in the \[0, cpu_count\] range. |

**cpu_cycles_per_thread_in_interval**

Aggregated CPU statistics for each thread in a provided interval.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | Thread with CPU cycles and frequency statistics. |
| millicycles | LONG | Sum of CPU millicycles |
| megacycles | LONG | Sum of CPU megacycles |
| runtime | DURATION | Total runtime duration |
| awake_runtime | DURATION | Total runtime duration, while 'awake' (CPUs not suspended). |
| min_freq | LONG | Minimum CPU frequency in kHz |
| max_freq | LONG | Maximum CPU frequency in kHz |
| avg_freq | LONG | Average CPU frequency in kHz |

**cpu_thread_utilization_in_interval**

Returns a table of thread utilization over a given interval.

Utilization is computed as runtime over the duration of the interval, aggregated by UTID.
Utilization can be normalized (divide by number of CPUs) or unnormalized.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Unique process id. |
| utid | JOINID(thread.id) | Unique thread id. |
| thread_name | STRING | The name of the thread |
| awake_dur | LONG | Total runtime of all threads with this UTID, while 'awake' (CPUs not suspended). |
| awake_utilization | DOUBLE | Percentage of 'awake_dur' over the 'awake' duration of the interval, normalized by the number of CPUs. Values in \[0.0, 100.0\] |
| awake_unnormalized_utilization | DOUBLE | Percentage of 'awake_dur' over the 'awake' duration of the interval, unnormalized. Values in \[0.0, 100.0 \* \] |

### linux.cpu.utilization.thread_cpu

#### Views/Tables

**cpu_cycles_per_thread_per_cpu**

TABLE
Aggregated CPU statistics for each thread per CPU combination.
To operate properly this requires sched/sched_switch and power/cpu_frequency
ftrace events to be present in the trace.

| Column | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | Thread |
| ucpu | JOINID(cpu.id) | Unique CPU id. Joinable with `cpu.id`. |
| cpu | LONG | The number of the CPU. Might not be the same as ucpu in multi machine cases. |
| millicycles | LONG | Sum of CPU millicycles |
| megacycles | LONG | Sum of CPU megacycles |
| runtime | DURATION | Total runtime duration |
| min_freq | LONG | Minimum CPU frequency in kHz |
| max_freq | LONG | Maximum CPU frequency in kHz |
| avg_freq | LONG | Average CPU frequency in kHz |

#### Table Functions

**cpu_cycles_per_thread_per_cpu_in_interval**

Aggregated CPU statistics for each thread per CPU combination in a provided interval.
To operate properly this requires sched/sched_switch and power/cpu_frequency
ftrace events to be present in the trace.
Warning: this query is expensive and might take a long time to execute when joined
with a large number of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Start of the interval. |
| dur | LONG | Duration of the interval. |

| Column | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | Thread with CPU cycles and frequency statistics. |
| ucpu | JOINID(cpu.id) | Unique CPU id. Joinable with `cpu.id`. |
| cpu | LONG | The number of the CPU. Might not be the same as ucpu in multi machine cases. |
| millicycles | LONG | Sum of CPU millicycles |
| megacycles | LONG | Sum of CPU megacycles |
| runtime | DURATION | Total runtime duration |
| min_freq | LONG | Minimum CPU frequency in kHz |
| max_freq | LONG | Maximum CPU frequency in kHz |
| avg_freq | LONG | Average CPU frequency in kHz |

### linux.devfreq

#### Views/Tables

**linux_devfreq_dsu_counter**

TABLE
ARM DSU device frequency counters. This table will only be populated on
traces collected with "devfreq/devfreq_frequency" ftrace event enabled,
and from ARM devices with the DSU (DynamIQ Shared Unit) hardware.

| Column | Type | Description |
|---|---|---|
| id | LONG | Unique identifier for this counter. |
| ts | TIMESTAMP | Starting timestamp of the counter. |
| dur | DURATION | Duration in which counter is constant and frequency doesn't chamge. |
| dsu_freq | LONG | Frequency in kHz of the device that corresponds to the counter. |

### linux.irqs

#### Views/Tables

**linux_hard_irqs**

VIEW
All hard IRQs of the trace represented as slices.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Starting timestamp of this IRQ. |
| dur | DURATION | Duration of this IRQ. |
| name | STRING | The name of the IRQ. |
| id | JOINID(slice.id) | The id of the IRQ. |
| parent_id | JOINID(slice.id) | The id of this IRQ's parent IRQ (i.e. the IRQ that this IRQ preempted). |

**linux_soft_irqs**

VIEW
All soft IRQs of the trace represented as slices.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Starting timestamp of this IRQ. |
| dur | DURATION | Duration of this IRQ. |
| name | STRING | The name of the IRQ. |
| id | JOINID(slice.id) | The id of the IRQ. |

**linux_irqs**

VIEW
All IRQs, including hard and soft IRQs, of the trace represented as slices.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Starting timestamp of this IRQ. |
| dur | DURATION | Duration of this IRQ. |
| name | STRING | The name of the IRQ. |
| id | JOINID(slice.id) | The id of the IRQ. |
| parent_id | JOINID(slice.id) | The id of this IRQ's parent IRQ (i.e. the IRQ that this IRQ preempted). |
| is_soft_irq | BOOL | Flag indicating if IRQ is soft IRQ |

### linux.memory.high_watermark

#### Views/Tables

**memory_rss_high_watermark_per_process**

VIEW
For each process fetches the memory high watermark until or during
timestamp.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp |
| dur | DURATION | Duration |
| upid | JOINID(process.id) | Upid of the process |
| pid | LONG | Pid of the process |
| process_name | STRING | Name of the process |
| rss_high_watermark | LONG | Maximum `rss` value until now |

### linux.memory.process

#### Views/Tables

**memory_rss_and_swap_per_process**

VIEW
Memory metrics timeline for each process.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp |
| dur | DURATION | Duration |
| upid | JOINID(process.id) | Upid of the process |
| pid | LONG | Pid of the process |
| process_name | STRING | Name of the process |
| anon_rss | LONG | Anon RSS counter value |
| file_rss | LONG | File RSS counter value |
| shmem_rss | LONG | Shared memory RSS counter value |
| rss | LONG | Total RSS value. Sum of `anon_rss`, `file_rss` and `shmem_rss`. Returns value even if one of the values is NULL. |
| swap | LONG | Swap counter value |
| anon_rss_and_swap | LONG | Sum or `anon_rss` and `swap`. Returns value even if one of the values is NULL. |
| rss_and_swap | LONG | Sum or `rss` and `swap`. Returns value even if one of the values is NULL. |

### linux.perf.samples

#### Views/Tables

**linux_perf_samples_summary_tree**

TABLE
Table summarising the callstacks captured during all
perf samples in the trace.

Specifically, this table returns a tree containing all
the callstacks seen during the trace with `self_count`
equal to the number of samples with that frame as the
leaf and `cumulative_count` equal to the number of
samples with the frame anywhere in the tree.

| Column | Type | Description |
|---|---|---|
| id | LONG | The id of the callstack. A callstack in this context is a unique set of frames up to the root. |
| parent_id | LONG | The id of the parent callstack for this callstack. |
| name | STRING | The function name of the frame for this callstack. |
| mapping_name | STRING | The name of the mapping containing the frame. This can be a native binary, library, JAR or APK. |
| source_file | STRING | The name of the file containing the function. |
| line_number | LONG | The line number in the file the function is located at. |
| self_count | LONG | The number of samples with this function as the leaf frame. |
| cumulative_count | LONG | The number of samples with this function appearing anywhere on the callstack. |

### linux.perf.spe

#### Views/Tables

**linux_perf_spe_record**

VIEW

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestap when the operation was sampled |
| utid | JOINID(thread.id) | Thread the operation executed in |
| exception_level | STRING | Exception level the instruction was executed in |
| instruction_frame_id | LONG | Instruction virtual address |
| operation | STRING | Type of operation sampled |
| data_virtual_address | LONG | The virtual address accessed by the operation (0 if no memory access was performed) |
| data_physical_address | LONG | The physical address accessed by the operation (0 if no memory access was performed) |
| total_latency | LONG | Cycle count from the operation being dispatched for issue to the operation being complete. |
| issue_latency | LONG | Cycle count from the operation being dispatched for issue to the operation being issued for execution. |
| translation_latency | LONG | Cycle count from a virtual address being passed to the MMU for translation to the result of the translation being available. |
| data_source | STRING | Where the data returned for a load operation was sourced |
| exception_gen | BOOL | Operation generated an exception |
| retired | BOOL | Operation architecturally retired |
| l1d_access | BOOL | Operation caused a level 1 data cache access |
| l1d_refill | BOOL | Operation caused a level 1 data cache refill |
| tlb_access | BOOL | Operation caused a TLB access |
| tlb_refill | BOOL | Operation caused a TLB refill involving at least one translation table walk |
| not_taken | BOOL | Conditional instruction failed its condition code check |
| mispred | BOOL | Whether a branch caused a correction to the predicted program flow |
| llc_access | BOOL | Operation caused a last level data or unified cache access |
| llc_refill | BOOL | Whether the operation could not be completed by the last level data cache (or any above) |
| remote_access | BOOL | Operation caused an access to another socket in a multi-socket system |
| alignment | BOOL | Operation that incurred additional latency due to the alignment of the address and the size of the data being accessed |
| tme_transaction | BOOL | Whether the operation executed in transactional state |
| sve_partial_pred | BOOL | SVE or SME operation with at least one false element in the governing predicate(s) |
| sve_empty_pred | BOOL | SVE or SME operation with no true element in the governing predicate(s) |
| l2d_access | BOOL | Whether a load operation caused a cache access to at least the level 2 data or unified cache |
| l2d_hit | BOOL | Whether a load operation accessed and missed the level 2 data or unified cache. Not set for accesses that are satisfied from refilling data of a previous miss |
| cache_data_modified | BOOL | Whether a load operation accessed modified data in a cache |
| recenty_fetched | BOOL | Wheter a load operation hit a recently fetched line in a cache |
| data_snooped | BOOL | Whether a load operation snooped data from a cache outside the cache hierarchy of this core |

### linux.threads

#### Views/Tables

**linux_kernel_threads**

TABLE
All kernel threads of the trace. As kernel threads are processes, provides
also process data.

| Column | Type | Description |
|---|---|---|
| upid | JOINID(process.id) | Upid of kernel thread. Alias of |
| utid | JOINID(thread.id) | Utid of kernel thread. Alias of |
| pid | LONG | Pid of kernel thread. Alias of |
| tid | LONG | Tid of kernel thread. Alias of |
| process_name | STRING | Name of kernel process. Alias of |
| thread_name | STRING | Name of kernel thread. Alias of |
| machine_id | LONG | Machine id of kernel thread. If NULL then it's a single machine trace. Alias of |

## Package: pixel

### pixel.camera

#### Views/Tables

**pixel_camera_frames**

TABLE
Break down camera Camera graph execution slices per node, port group, and frame.
This table extracts key identifiers from Camera graph execution slice names and
provides timing information for each processing stage.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Unique identifier for this slice. |
| ts | TIMESTAMP | Start timestamp of the slice. |
| dur | DURATION | Duration of the slice execution. |
| track_id | JOINID(track.id) | Track ID for this slice. |
| utid | JOINID(thread.id) | Thread ID (utid) executing this slice. |
| thread_name | STRING | Name of the thread executing this slice. |
| node | STRING | Name of the processing node in the Camera graph. |
| port_group | STRING | Port group name for the node. |
| frame_number | LONG | Frame number being processed. |
| cam_id | LONG | Camera ID associated with this slice. |

## Package: slices

### slices.cpu_time

#### Views/Tables

**thread_slice_cpu_time**

TABLE
Time each thread slice spent running on CPU.
Requires scheduling data to be available in the trace.

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Slice. |
| name | STRING | Name of the slice. |
| utid | JOINID(thread.id) | Id of the thread the slice is running on. |
| thread_name | STRING | Name of the thread. |
| upid | JOINID(process.id) | Id of the process the slice is running on. |
| process_name | STRING | Name of the process. |
| cpu_time | LONG | Duration of the time the slice was running. |

**thread_slice_cpu_cycles**

VIEW
CPU cycles per each slice.

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Id of a slice. |
| name | STRING | Name of the slice. |
| utid | JOINID(thread.id) | Id of the thread the slice is running on. |
| thread_name | STRING | Name of the thread. |
| upid | JOINID(process.id) | Id of the process the slice is running on. |
| process_name | STRING | Name of the process. |
| millicycles | LONG | Sum of CPU millicycles. Null if frequency couldn't be fetched for any period during the runtime of the slice. |
| megacycles | LONG | Sum of CPU megacycles. Null if frequency couldn't be fetched for any period during the runtime of the slice. |

### slices.self_dur

#### Views/Tables

**slice_self_dur**

TABLE
For every slice in the `slice` table, computes the "self-duration": the time
spent in the slice but *not* spent in any child slices.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | The id of the slice. |
| self_dur | DURATION | The self duration for the slice: the time spent in the slice but not any child slices. |

### slices.stack

#### Views/Tables

**slice_with_stack_id**

VIEW
View that provides stack_id and parent_stack_id for all slices by computing
them on-demand.

> [!NOTE]
> **Note:** This view computes stack hashes on-demand, which may be slower than the previous C++ implementation.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Slice id. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | ARGSETID | Alias of `slice.arg_set_id`. |
| thread_ts | TIMESTAMP | Alias of `slice.thread_ts`. |
| thread_dur | LONG | Alias of `slice.thread_dur`. |
| thread_instruction_count | LONG | Alias of `slice.thread_instruction_count`. |
| thread_instruction_delta | LONG | Alias of `slice.thread_instruction_delta`. |
| stack_id | LONG | A unique identifier obtained from the names and categories of all slices in this stack. Computed on-demand. |
| parent_stack_id | LONG | The stack_id for the parent of this slice. 0 if there is no parent. |

#### Table Functions

**ancestor_slice_by_stack**

Returns all slices that have the given stack_id, along with their ancestors.

The stack_id can be obtained from the slice_with_stack_id view.

| Argument | Type | Description |
|---|---|---|
| stack_hash | LONG | The stack hash to search for. |

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Slice id. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | ARGSETID | Alias of `slice.arg_set_id`. |
| thread_ts | TIMESTAMP | Alias of `slice.thread_ts`. |
| thread_dur | LONG | Alias of `slice.thread_dur`. |

**descendant_slice_by_stack**

Returns all slices that have the given stack_id, along with their descendants.

The stack_id can be obtained from the slice_with_stack_id view.

| Argument | Type | Description |
|---|---|---|
| stack_hash | LONG | The stack hash to search for. |

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Slice id. |
| ts | TIMESTAMP | Alias of `slice.ts`. |
| dur | DURATION | Alias of `slice.dur`. |
| track_id | JOINID(track.id) | Alias of `slice.track_id`. |
| category | STRING | Alias of `slice.category`. |
| name | STRING | Alias of `slice.name`. |
| depth | LONG | Alias of `slice.depth`. |
| parent_id | JOINID(slice.id) | Alias of `slice.parent_id`. |
| arg_set_id | ARGSETID | Alias of `slice.arg_set_id`. |
| thread_ts | TIMESTAMP | Alias of `slice.thread_ts`. |
| thread_dur | LONG | Alias of `slice.thread_dur`. |

### slices.time_in_state

#### Views/Tables

**thread_slice_time_in_state**

TABLE
For each thread slice, returns the sum of the time it spent in various
scheduling states.

Requires scheduling data to be available in the trace.

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Thread slice. |
| name | STRING | Name of the slice. |
| utid | JOINID(thread.id) | Thread the slice is running on. |
| thread_name | STRING | Name of the thread. |
| upid | JOINID(process.id) | Id of the process the slice is running on. |
| process_name | STRING | Name of the process. |
| state | STRING | The scheduling state (from the `thread_state` table). Use the `sched_state_to_human_readable_string` function in the `sched` package to get full name. |
| io_wait | BOOL | If the `state` is uninterruptible sleep, `io_wait` indicates if it was an IO sleep. Will be null if `state` is *not* uninterruptible sleep or if we cannot tell if it was an IO sleep or not. Only available on Android when `sched/sched_blocked_reason` ftrace tracepoint is enabled. |
| blocked_function | STRING | If in uninterruptible sleep (D), the kernel function on which was blocked. Only available on userdebug Android builds when `sched/sched_blocked_reason` ftrace tracepoint is enabled. |
| dur | DURATION | The duration of time the threads slice spent for each (state, io_wait, blocked_function) tuple. |

### slices.with_context

#### Views/Tables

**thread_slice**

VIEW
All thread slices with data about thread, thread track and process.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Slice |
| ts | TIMESTAMP | Alias for `slice.ts`. |
| dur | DURATION | Alias for `slice.dur`. |
| category | STRING | Alias for `slice.category`. |
| name | STRING | Alias for `slice.name`. |
| track_id | JOINID(track.id) | Alias for `slice.track_id`. |
| track_name | STRING | Alias for `thread_track.name`. |
| thread_name | STRING | Alias for `thread.name`. |
| utid | JOINID(thread.id) | Alias for `thread.utid`. |
| tid | LONG | Alias for `thread.tid`. |
| is_main_thread | BOOL | Alias for `thread.is_main_thread`. |
| process_name | STRING | Alias for `process.name`. |
| upid | JOINID(process.id) | Alias for `process.upid`. |
| pid | LONG | Alias for `process.pid`. |
| depth | LONG | Alias for `slice.depth`. |
| parent_id | JOINID(slice.id) | Alias for `slice.parent_id`. |
| arg_set_id | ARGSETID | Alias for `slice.arg_set_id`. |
| thread_ts | TIMESTAMP | Alias for `slice.thread_ts`. |
| thread_dur | LONG | Alias for `slice.thread_dur`. |

**process_slice**

VIEW
All process slices with data about process track and process.

| Column | Type | Description |
|---|---|---|
| id | ID(slice.id) | Slice |
| ts | TIMESTAMP | Alias for `slice.ts`. |
| dur | DURATION | Alias for `slice.dur`. |
| category | STRING | Alias for `slice.category`. |
| name | STRING | Alias for `slice.name`. |
| track_id | JOINID(track.id) | Alias for `slice.track_id`. |
| track_name | STRING | Alias for `process_track.name`. |
| process_name | STRING | Alias for `process.name`. |
| upid | JOINID(process.id) | Alias for `process.upid`. |
| pid | LONG | Alias for `process.pid`. |
| depth | LONG | Alias for `slice.depth`. |
| parent_id | JOINID(slice.id) | Alias for `slice.parent_id`. |
| arg_set_id | ARGSETID | Alias for `slice.arg_set_id`. |
| thread_ts | TIMESTAMP | Alias for `slice.thread_ts`. |
| thread_dur | LONG | Alias for `slice.thread_dur`. |

**thread_or_process_slice**

VIEW
All the slices in the trace associated to a thread or a process along
with contextual information about them (e.g. thread name, process name, tid etc).

| Column | Type | Description |
|---|---|---|
| id | JOINID(slice.id) | Slice |
| ts | TIMESTAMP | Alias for `slice.ts`. |
| dur | DURATION | Alias for `slice.dur`. |
| category | STRING | Alias for `slice.category`. |
| name | STRING | Alias for `slice.name`. |
| track_id | JOINID(track.id) | Alias for `slice.track_id`. |
| track_name | STRING | Alias for `track.name`. |
| thread_name | STRING | Alias for `thread.name`. |
| utid | JOINID(thread.id) | Alias for `thread.utid`. |
| tid | LONG | Alias for `thread.tid` |
| process_name | STRING | Alias for `process.name`. |
| upid | JOINID(process.id) | Alias for `process.upid`. |
| pid | LONG | Alias for `process.pid`. |
| depth | LONG | Alias for `slice.depth`. |
| parent_id | JOINID(slice.id) | Alias for `slice.parent_id`. |
| arg_set_id | ARGSETID | Alias for `slice.arg_set_id`. |

## Package: appleos

### appleos.instruments.samples

#### Views/Tables

**appleos_instruments_samples_summary_tree**

TABLE
Table summarising the callstacks captured during all
instruments samples in the trace.

Specifically, this table returns a tree containing all
the callstacks seen during the trace with `self_count`
equal to the number of samples with that frame as the
leaf and `cumulative_count` equal to the number of
samples with the frame anywhere in the tree.

| Column | Type | Description |
|---|---|---|
| id | LONG | The id of the callstack. A callstack in this context is a unique set of frames up to the root. |
| parent_id | LONG | The id of the parent callstack for this callstack. |
| name | STRING | The function name of the frame for this callstack. |
| mapping_name | STRING | The name of the mapping containing the frame. This can be a native binary, library, or JIT. |
| source_file | STRING | The name of the file containing the function. |
| line_number | LONG | The line number in the file the function is located at. |
| self_count | LONG | The number of samples with this function as the leaf frame. |
| cumulative_count | LONG | The number of samples with this function appearing anywhere on the callstack. |

## Package: graphs

### graphs.dominator_tree

#### Macros

**graph_dominator_tree**

Given a table containing a directed flow-graph and an entry node, computes
the "dominator tree" for the graph. See \[1\] for an explanation of what a
dominator tree is.

\[1\] <https://en.wikipedia.org/wiki/Dominator_(graph_theory)>

Example usage on traces containing heap graphs:

\`CREATE PERFETTO VIEW dominator_compatible_heap_graph AS
-- Extract the edges from the heap graph which correspond to references
-- between objects.
SELECT
owner_id AS source_node_id,
owned_id as dest_node_id
FROM heap_graph_reference
JOIN heap_graph_object owner on heap_graph_reference.owner_id = owner.id
WHERE owned_id IS NOT NULL AND owner.reachable
UNION ALL
-- Since a Java heap graph is a "forest" structure, we need to add a dummy
-- "root" node which connects all the roots of the forest into a single
-- connected component.
SELECT
(SELECT max(id) + 1 FROM heap_graph_object) as source_node_id,
id
FROM heap_graph_object
WHERE root_type IS NOT NULL;

SELECT \*
FROM graph_dominator_tree!(
dominator_compatible_heap_graph,
(SELECT max(id) + 1 FROM heap_graph_object)
);\`Returns: TableOrSubquery, The returned table has the schema (node_id LONG, dominator_node_id LONG). \|node_id\| is the id of the node from the input graph and \|dominator_node_id\| is the id of the node in the input flow-graph which is the "dominator" of \|node_id\|.

| Argument | Type | Description |
|---|---|---|
| graph_table | TableOrSubquery | A table/view/subquery corresponding to a directed flow-graph on which the dominator tree should be computed. This table must have the columns "source_node_id" and "dest_node_id" corresponding to the two nodes on either end of the edges in the graph. Note: the columns must contain uint32 similar to ids in trace processor tables (i.e. the values should be relatively dense and close to zero). The implementation makes assumptions on this for performance reasons and, if this criteria is not, can lead to enormous amounts of memory being allocated. Note: this means that the graph *must* be a single fully connected component with |
| root_node_id | Expr | The entry node to |

### graphs.partition

#### Macros

**tree_structural_partition_by_group**

Partitions a tree into a forest of trees based on a given grouping key
in a structure-preserving way.

Specifically, for each tree in the output forest, all the nodes in that tree
have the same ancestors and descendants as in the original tree *iff* that
ancestor/descendent belonged to the same group.

Example:
Input

| id | parent_id | group_key |
|---|---|---|
| 1 | NULL | 1 |
| 2 | 1 | 1 |
| 3 | NULL | 2 |
| 4 | NULL | 2 |
| 5 | 2 | 1 |
| 6 | NULL | 3 |
| 7 | 4 | 2 |
| 8 | 4 | 1 |

Or as a graph:

`1 (1)
/
2 (1)
/ \
3 (2) 4 (2)
/ \
5 (1) 8 (1)
/ \
6 (3) 7 (2)` Possible output (order of rows is implementation-defined)

| id | parent_id | group_key |
|---|---|---|
| 1 | NULL | 1 |
| 2 | 1 | 1 |
| 3 | NULL | 2 |
| 4 | NULL | 2 |
| 5 | 2 | 1 |
| 6 | NULL | 3 |
| 7 | 4 | 2 |
| 8 | 2 | 1 |

Or as a forest:

`1 (1) 3 (2) 4 (2) 6 (3)
| |
2 (1) 7 (2)
/ \
5 (1) 8 (1)`Returns: TableOrSubquery, The returned table has the schema (id LONG, parent_id LONG, group_key LONG).

| Argument | Type | Description |
|---|---|---|
| tree_table | TableOrSubquery | A table/view/subquery corresponding to a tree which should be partitioned. This table must have the columns "id", "parent_id" and "group_key". Note: the columns must contain uint32 similar to ids in trace processor tables (i.e. the values should be relatively dense and close to zero). The implementation makes assumptions on this for performance reasons and, if this criteria is not, can lead to enormous amounts of memory being allocated. |

### graphs.search

#### Macros

**graph_reachable_dfs**

Computes the "reachable" set of nodes in a directed graph from a given set
of starting nodes by performing a depth-first search on the graph. The
returned nodes are structured as a tree with parent-child relationships
corresponding to the order in which nodes were encountered by the DFS.

While this macro can be used directly by end users (hence being public),
it is primarily intended as a lower-level building block upon which higher
level functions/macros in the standard library can be built.

Example usage on traces containing heap graphs:

`-- Compute the reachable nodes from the first heap root.
SELECT *
FROM graph_reachable_dfs!(
(
SELECT
owner_id AS source_node_id,
owned_id as dest_node_id
FROM heap_graph_reference
WHERE owned_id IS NOT NULL
),
(SELECT id FROM heap_graph_object WHERE root_type IS NOT NULL)
);`Returns: TableOrSubquery, The returned table has the schema (node_id LONG, parent_node_id LONG). \|node_id\| is the id of the node from the input graph and \|parent_node_id\| is the id of the node which was the first encountered predecessor in a DFS search of the graph.

| Argument | Type | Description |
|---|---|---|
| graph_table | TableOrSubquery | A table/view/subquery corresponding to a directed graph on which the reachability search should be performed. This table must have the columns "source_node_id" and "dest_node_id" corresponding to the two nodes on either end of the edges in the graph. Note: the columns must contain uint32 similar to ids in trace processor tables (i.e. the values should be relatively dense and close to zero). The implementation makes assumptions on this for performance reasons and, if this criteria is not, can lead to enormous amounts of memory being allocated. |
| start_nodes | TableOrSubquery | A table/view/subquery corresponding to the list of start nodes for the BFS. This table must have a single column "node_id". |

**graph_reachable_bfs**

Computes the "reachable" set of nodes in a directed graph from a given
starting node by performing a breadth-first search on the graph. The returned
nodes are structured as a tree with parent-child relationships corresponding
to the order in which nodes were encountered by the BFS.

While this macro can be used directly by end users (hence being public),
it is primarily intended as a lower-level building block upon which higher
level functions/macros in the standard library can be built.

Example usage on traces containing heap graphs:

`-- Compute the reachable nodes from all heap roots.
SELECT *
FROM graph_reachable_bfs!(
(
SELECT
owner_id AS source_node_id,
owned_id as dest_node_id
FROM heap_graph_reference
WHERE owned_id IS NOT NULL
),
(SELECT id FROM heap_graph_object WHERE root_type IS NOT NULL)
);`Returns: TableOrSubquery, The returned table has the schema (node_id LONG, parent_node_id LONG). \|node_id\| is the id of the node from the input graph and \|parent_node_id\| is the id of the node which was the first encountered predecessor in a BFS search of the graph.

| Argument | Type | Description |
|---|---|---|
| graph_table | TableOrSubquery | A table/view/subquery corresponding to a directed graph on which the reachability search should be performed. This table must have the columns "source_node_id" and "dest_node_id" corresponding to the two nodes on either end of the edges in the graph. Note: the columns must contain uint32 similar to ids in trace processor tables (i.e. the values should be relatively dense and close to zero). The implementation makes assumptions on this for performance reasons and, if this criteria is not, can lead to enormous amounts of memory being allocated. |
| start_nodes | TableOrSubquery | A table/view/subquery corresponding to the list of start nodes for the BFS. This table must have a single column "node_id". |

**graph_next_sibling**

Computes the next sibling node in a directed graph. The next node under a parent node
is determined by on the \|sort_key\|, which should be unique for every node under a parent.
The order of the next sibling is undefined if the \|sort_key\| is not unique.

Example usage:

`-- Compute the next sibling:
SELECT *
FROM graph_next_sibling!(
(
SELECT
id AS node_id,
parent_id AS node_parent_id,
ts AS sort_key
FROM slice
)
);`Returns: TableOrSubquery, The returned table has the schema (node_id LONG, next_node_id LONG). \|node_id\| is the id of the node from the input graph and \|next_node_id\| is the id of the node which is its next sibling.

| Argument | Type | Description |
|---|---|---|
| graph_table | TableOrSubquery | A table/view/subquery corresponding to a directed graph for which to find the next sibling. This table must have the columns "node_id", "node_parent_id" and "sort_key". |

**graph_reachable_weight_bounded_dfs**

Computes the "reachable" set of nodes in a directed graph from a set of
starting (root) nodes by performing a depth-first search from each root node on the graph.
The search is bounded by the sum of edge weights on the path and the root node specifies the
max weight (inclusive) allowed before stopping the search.
The returned nodes are structured as a tree with parent-child relationships corresponding
to the order in which nodes were encountered by the DFS. Each row also has the root node from
which where the edge was encountered.

While this macro can be used directly by end users (hence being public),
it is primarily intended as a lower-level building block upon which higher
level functions/macros in the standard library can be built.

Example usage on traces with sched info:

\`-- Compute the reachable nodes from a sched wakeup chain
INCLUDE PERFETTO MODULE sched.thread_executing_spans;

SELECT \*
FROM
graph_reachable_dfs_bounded
!(
(
SELECT
id AS source_node_id,
COALESCE(parent_id, id) AS dest_node_id,
id - COALESCE(parent_id, id) AS edge_weight
FROM _wakeup_chain
),
(
SELECT
id AS root_node_id,
id - COALESCE(prev_id, id) AS root_target_weight
FROM _wakeup_chain
));\`Returns: TableOrSubquery, The returned table has the schema (root_node_id, node_id LONG, parent_node_id LONG). \|root_node_id\| is the id of the starting node under which this edge was encountered. \|node_id\| is the id of the node from the input graph and \|parent_node_id\| is the id of the node which was the first encountered predecessor in a DFS search of the graph.

| Argument | Type | Description |
|---|---|---|
| graph_table | TableOrSubquery | A table/view/subquery corresponding to a directed graph on which the reachability search should be performed. This table must have the columns "source_node_id" and "dest_node_id" corresponding to the two nodes on either end of the edges in the graph and an "edge_weight" corresponding to the weight of the edge between the node. Note: the columns must contain uint32 similar to ids in trace processor tables (i.e. the values should be relatively dense and close to zero). The implementation makes assumptions on this for performance reasons and, if this criteria is not, can lead to enormous amounts of memory being allocated. |
| root_table | TableOrSubquery | A table/view/subquery corresponding to start nodes to |
| is_target_weight_floor | Expr | Whether the target_weight is a floor weight or ceiling weight. If it's floor, the search stops right after we exceed the target weight, and we include the node that pushed just passed the target. If ceiling, the search stops right before the target weight and the node that would have pushed us passed the target is not included. |

## Package: sched

### sched.latency

#### Views/Tables

**sched_latency_for_running_interval**

TABLE
Scheduling latency of running thread states.
For each time the thread was running, returns the duration of the runnable
state directly before.

| Column | Type | Description |
|---|---|---|
| thread_state_id | JOINID(thread_state.id) | Running state of the thread. |
| sched_id | JOINID(sched.id) | Id of a corresponding slice in a `sched` table. |
| utid | JOINID(thread.id) | Thread with running state. |
| runnable_latency_id | JOINID(thread_state.id) | Runnable state before thread is "running". Duration of this thread state is `latency_dur`. One of `thread_state.id`. |
| latency_dur | LONG | Scheduling latency of thread state. Duration of thread state with `runnable_latency_id`. |

### sched.runnable

#### Views/Tables

**sched_previous_runnable_on_thread**

TABLE
Previous runnable slice on the same thread.
For each "Running" thread state finds:

- previous "Runnable" (or runnable preempted) state.
- previous uninterrupted "Runnable" state with a valid waker thread.

| Column | Type | Description |
|---|---|---|
| id | JOINID(thread_state.id) | Running thread state |
| prev_runnable_id | JOINID(thread_state.id) | Previous runnable thread state. |
| prev_wakeup_runnable_id | JOINID(thread_state.id) | Previous runnable thread state with valid waker thread. |

### sched.states

#### Functions

**sched_state_to_human_readable_string**

Translates a single-letter scheduling state to a human-readable string.
Returns STRING: Humanly readable string representing the scheduling state of the kernel thread. The individual characters in the string mean the following: R (runnable), S (awaiting a wakeup), D (in an uninterruptible sleep), T (suspended), t (being traced), X (exiting), P (parked), W (waking), I (idle), N (not contributing to the load average), K (wakeable on fatal signals) and Z (zombie, awaiting cleanup).

| Argument | Type | Description |
|---|---|---|
| short_name | STRING | An individual character string representing the scheduling state of the kernel thread at the end of the slice. |

**sched_state_io_to_human_readable_string**

Translates a single-letter scheduling state and IO wait information to
a human-readable string.
Returns STRING: A human readable string with information about the scheduling state and IO wait.

| Argument | Type | Description |
|---|---|---|
| sched_state | STRING | An individual character string representing the scheduling state of the kernel thread at the end of the slice. |
| io_wait | BOOL | A (posssibly NULL) boolean indicating, if the device was in uninterruptible sleep, if it was an IO sleep. |

### sched.thread_level_parallelism

#### Views/Tables

**sched_runnable_thread_count**

TABLE
The count of runnable threads over time.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp when the runnable thread count changed to the current value. |
| runnable_thread_count | LONG | Number of runnable threads, covering the range from this timestamp to the next row's timestamp. |

**sched_uninterruptible_sleep_thread_count**

TABLE
The count of threads in uninterruptible sleep over time.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp when the thread count changed to the current value. |
| uninterruptible_sleep_thread_count | LONG | Number of threads in uninterrutible sleep, covering the range from this timestamp to the next row's timestamp. |

**sched_active_cpu_count**

TABLE
The count of active CPUs over time.

| Column | Type | Description |
|---|---|---|
| ts | TIMESTAMP | Timestamp when the number of active CPU changed. |
| active_cpu_count | LONG | Number of active CPUs, covering the range from this timestamp to the next row's timestamp. |

### sched.time_in_state

#### Views/Tables

**sched_time_in_state_for_thread**

TABLE
The time a thread spent in each scheduling state during it's lifetime.

| Column | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | Utid of the thread. |
| total_runtime | LONG | Total runtime of thread. |
| state | STRING | One of the scheduling states of kernel thread. |
| time_in_state | LONG | Total time spent in the scheduling state. |
| percentage_in_state | LONG | Percentage of time thread spent in scheduling state in \[0-100\] range. |

**sched_percentage_of_time_in_state**

TABLE
Summary of time spent by thread in each scheduling state, in percentage (\[0, 100\]
ranges). Sum of all states might be smaller than 100, as those values
are rounded down.

| Column | Type | Description |
|---|---|---|
| utid | JOINID(thread.id) | Utid of the thread. |
| running | LONG | Percentage of time thread spent in running ('Running') state in \[0, 100\] range. |
| runnable | LONG | Percentage of time thread spent in runnable ('R') state in \[0, 100\] range. |
| runnable_preempted | LONG | Percentage of time thread spent in preempted runnable ('R+') state in \[0, 100\] range. |
| sleeping | LONG | Percentage of time thread spent in sleeping ('S') state in \[0, 100\] range. |
| uninterruptible_sleep | LONG | Percentage of time thread spent in uninterruptible sleep ('D') state in \[0, 100\] range. |
| other | LONG | Percentage of time thread spent in other ('T', 't', 'X', 'Z', 'x', 'I', 'K', 'W', 'P', 'N') states in \[0, 100\] range. |

#### Table Functions

**sched_time_in_state_for_thread_in_interval**

Time the thread spent each state in a given interval.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

Specifically for any non-trivial subset of thread slices, prefer using
`thread_slice_time_in_state` in the `slices.time_in_state` module for this
purpose instead.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | The start of the interval. |
| dur | DURATION | The duration of the interval. |
| utid | JOINID(thread.id) | The utid of the thread. |

| Column | Type | Description |
|---|---|---|
| state | STRING | The scheduling state (from the `thread_state` table). Use the `sched_state_to_human_readable_string` function in the `sched` package to get full name. |
| io_wait | BOOL | A (posssibly NULL) boolean indicating, if the device was in uninterruptible sleep, if it was an IO sleep. |
| blocked_function | LONG | If the `state` is uninterruptible sleep, `io_wait` indicates if it was an IO sleep. Will be null if `state` is *not* uninterruptible sleep or if we cannot tell if it was an IO sleep or not. Only available on Android when `sched/sched_blocked_reason` ftrace tracepoint is enabled. |
| dur | DURATION | The duration of time the threads slice spent for each (state, io_wait, blocked_function) tuple. |

**sched_time_in_state_and_cpu_for_thread_in_interval**

Time the thread spent each state and cpu in a given interval.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| ts | TIMESTAMP | The start of the interval. |
| dur | DURATION | The duration of the interval. |
| utid | JOINID(thread.id) | The utid of the thread. |

| Column | Type | Description |
|---|---|---|
| state | STRING | Thread state (from the `thread_state` table). Use `sched_state_to_human_readable_string` function to get full name. |
| io_wait | BOOL | A (posssibly NULL) boolean indicating, if the device was in uninterruptible sleep, if it was an IO sleep. |
| cpu | LONG | Id of the CPU. |
| blocked_function | LONG | Some states can specify the blocked function. Usually NULL. |
| dur | DURATION | Total time spent with this state, cpu and blocked function. |

**sched_time_in_state_for_cpu_in_interval**

Time spent by CPU in each scheduling state in a provided interval.

This function is only designed to run over a small number of intervals
(10-100 at most). It will be *very slow* for large sets of intervals.

| Argument | Type | Description |
|---|---|---|
| cpu | LONG | CPU id. |
| ts | TIMESTAMP | Interval start. |
| dur | LONG | Interval duration. |

| Column | Type | Description |
|---|---|---|
| end_state | STRING | End state. From `sched.end_state`. |
| dur | LONG | Duration in state. |

### sched.with_context

#### Views/Tables

**sched_with_thread_process**

VIEW
View of scheduling slices with extended information.
It holds slices with kernel thread scheduling information. These slices are
collected when the Linux "ftrace" data source is used with the
"sched/switch" and "sched/wakeup\*" events enabled.

The rows in this table will always have a matching row in the \|thread_state\|
table with \|thread_state.state\| = 'Running'

| Column | Type | Description |
|---|---|---|
| id | ID(sched.id) | Unique identifier for this scheduling slice (Running period). |
| ts | TIMESTAMP | The timestamp at the start of the Running period. |
| dur | DURATION | The duration of the Running period. |
| utid | JOINID(thread.id) | Unique identifier of the thread that was running. |
| thread_name | STRING | Name of the thread that was running. |
| upid | JOINID(process.id) | Unique identifier of the process that the thread belongs to. |
| process_name | STRING | Name of the process that the thread belongs to. |
| cpu | LONG | The CPU that the slice executed on (meaningful only in single machine traces). For multi-machine, join with the `cpu` table on `ucpu` to get the CPU identifier of each machine. |
| end_state | STRING | A string representing the scheduling state of the kernel thread at the end of the slice. The individual characters in the string mean the following: R (runnable), S (awaiting a wakeup), D (in an uninterruptible sleep), T (suspended), t (being traced), X (exiting), P (parked), W (waking), I (idle), N (not contributing to the load average), K (wakeable on fatal signals) and Z (zombie, awaiting cleanup). |
| priority | LONG | The kernel priority that the thread ran at. |

## Package: export

### export.to_firefox_profile

#### Functions

**export_to_firefox_profile**

Dumps all trace data as a Firefox profile json string
See `Profile` in
<https://github.com/firefox-devtools/profiler/blob/main/src/types/profile.js>
Also
<https://firefox-source-docs.mozilla.org/tools/profiler/code-overview.html>

You would probably want to download the generated json and then open at
<https://https://profiler.firefox.com>
You can easily do this from the UI via the following SQL
`SELECT CAST(export_to_firefox_profile() AS BLOB) AS profile;`
The result will have a link for you to download this json as a file.
Returns STRING: Json profile

## Package: traced

### traced.stats

#### Views/Tables

**traced_clone_flush_latency**

TABLE
Reports the duration of the flush operation for cloned traces (for each
buffer).

| Column | Type | Description |
|---|---|---|
| buffer_id | LONG | Id of the buffer (matches the config). |
| duration_ns | LONG | Interval from the start of the clone operation to the end of the flush for this buffer. |

**traced_trigger_clone_flush_latency**

TABLE
Reports the delay in finalizing the trace from the trigger that causes the
clone operation.

| Column | Type | Description |
|---|---|---|
| buffer_id | LONG | Id of the buffer. |
| duration_ns | LONG | Interval from the trigger that caused the clone operation to the end of the flush for this buffer. |

## Package: pkvm

### pkvm.hypervisor

#### Views/Tables

**pkvm_hypervisor_events**

VIEW
Events when CPU entered hypervisor.

| Column | Type | Description |
|---|---|---|
| slice_id | JOINID(slice.id) | Id of the corresponding slice in slice table. |
| cpu | JOINID(cpu.cpu) | CPU that entered hypervisor. |
| ts | TIMESTAMP | Timestamp when CPU entered hypervisor. |
| dur | DURATION | How much time CPU spent in hypervisor. |
| reason | STRING | Reason for entering hypervisor (e.g. host_hcall, host_mem_abort), or NULL if unknown. |

## Package: stacks

### stacks.cpu_profiling

#### Views/Tables

**cpu_profiling_samples**

TABLE
Table containing all the timestamped samples of CPU profiling which occurred
during the trace.

Currently, this table is backed by the following data sources:

- Linux perf
- Simpleperf proto format
- macOS instruments
- Chrome CPU profiling
- Legacy V8 CPU profiling
- Profiling data in Gecko traces

| Column | Type | Description |
|---|---|---|
| id | LONG | The id of the sample. |
| ts | TIMESTAMP | The timestamp of the sample. |
| utid | JOINID(thread.id) | The utid of the thread of the sample, if available. |
| tid | LONG | The tid of the sample, if available. |
| thread_name | STRING | The thread name of thread of the sample, if available. |
| ucpu | LONG | The ucpu of the sample, if available. |
| cpu | LONG | The cpu of the sample, if available. |
| callsite_id | LONG | The callsite id of the sample. |

**cpu_profiling_summary_tree**

TABLE
Table summarising the callstacks captured during any CPU profiling which
occurred during the trace.

Specifically, this table returns a tree containing all the callstacks seen
during the trace with `self_count` equal to the number of samples with that
frame as the leaf and `cumulative_count` equal to the number of samples with
the frame anywhere in the tree.

The data sources supported are the same as the `cpu_profiling_samples` table.

| Column | Type | Description |
|---|---|---|
| id | LONG | The id of the callstack; by callstack we mean a unique set of frames up to the root frame. |
| parent_id | LONG | The id of the parent callstack for this callstack. NULL if this is root. |
| name | STRING | The function name of the frame for this callstack. |
| mapping_name | STRING | The name of the mapping containing the frame. This can be a native binary, library, JAR or APK. |
| source_file | STRING | The name of the file containing the function. |
| line_number | LONG | The line number in the file the function is located at. |
| self_count | LONG | The number of samples with this function as the leaf frame. |
| cumulative_count | LONG | The number of samples with this function appearing anywhere on the callstack. |

## Package: time

### time.conversion

#### Functions

**time_from_ns**

Returns the provided nanosecond duration, which is the default
representation of time durations in trace processor. Provided for
consistency with other functions.
Returns TIMESTAMP: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| nanos | LONG | Time duration in nanoseconds. |

**time_from_us**

Converts a duration in microseconds to nanoseconds, which is the default
representation of time durations in trace processor.
Returns LONG: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| micros | LONG | Time duration in microseconds. |

**time_from_ms**

Converts a duration in millseconds to nanoseconds, which is the default
representation of time durations in trace processor.
Returns TIMESTAMP: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| millis | LONG | Time duration in milliseconds. |

**time_from_s**

Converts a duration in seconds to nanoseconds, which is the default
representation of time durations in trace processor.
Returns TIMESTAMP: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| seconds | LONG | Time duration in seconds. |

**time_from_min**

Converts a duration in minutes to nanoseconds, which is the default
representation of time durations in trace processor.
Returns TIMESTAMP: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| minutes | LONG | Time duration in minutes. |

**time_from_hours**

Converts a duration in hours to nanoseconds, which is the default
representation of time durations in trace processor.
Returns TIMESTAMP: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| hours | LONG | Time duration in hours. |

**time_from_days**

Converts a duration in days to nanoseconds, which is the default
representation of time durations in trace processor.
Returns LONG: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| days | LONG | Time duration in days. |

**time_to_ns**

Returns the provided nanosecond duration, which is the default
representation of time durations in trace processor. Provided for
consistency with other functions.
Returns LONG: Time duration in nanoseconds.

| Argument | Type | Description |
|---|---|---|
| nanos | TIMESTAMP | Time duration in nanoseconds. |

**time_to_us**

Converts a duration in nanoseconds to microseconds. Nanoseconds is the default
representation of time durations in trace processor.
Returns LONG: Time duration in microseconds.

| Argument | Type | Description |
|---|---|---|
| nanos | TIMESTAMP | Time duration in nanoseconds. |

**time_to_ms**

Converts a duration in nanoseconds to millseconds. Nanoseconds is the default
representation of time durations in trace processor.
Returns LONG: Time duration in milliseconds.

| Argument | Type | Description |
|---|---|---|
| nanos | TIMESTAMP | Time duration in nanoseconds. |

**time_to_s**

Converts a duration in nanoseconds to seconds. Nanoseconds is the default
representation of time durations in trace processor.
Returns LONG: Time duration in seconds.

| Argument | Type | Description |
|---|---|---|
| nanos | TIMESTAMP | Time duration in nanoseconds. |

**time_to_min**

Converts a duration in nanoseconds to minutes. Nanoseconds is the default
representation of time durations in trace processor.
Returns LONG: Time duration in minutes.

| Argument | Type | Description |
|---|---|---|
| nanos | TIMESTAMP | Time duration in nanoseconds. |

**time_to_hours**

Converts a duration in nanoseconds to hours. Nanoseconds is the default
representation of time durations in trace processor.
Returns LONG: Time duration in hours.

| Argument | Type | Description |
|---|---|---|
| nanos | TIMESTAMP | Time duration in nanoseconds. |

**time_to_days**

Converts a duration in nanoseconds to days. Nanoseconds is the default
representation of time durations in trace processor.
Returns LONG: Time duration in days.

| Argument | Type | Description |
|---|---|---|
| nanos | TIMESTAMP | Time duration in nanoseconds. |

Except as otherwise noted, the content of this page is licensed under the
[Creative Commons
Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed
under the [Apache 2.0
License](https://www.apache.org/licenses/LICENSE-2.0). Java is a registered trademark of Oracle and/or its affiliates.

- [Site CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- [Privacy](https://www.google.com/intl/en/policies/privacy/)