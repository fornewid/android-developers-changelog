---
title: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata
source: md.txt
---

# PgsSnapshotMetadata

Represents metadata about a `PgsSnapshot`.

## Summary

| ### Public attributes ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a6a52d4b9e2aeca6c83749b228c17b6de` | `float` The aspect ratio of cover image for snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a32abf57349589541ae4153489b0ca1e6` | `const char *` The URI of the cover image for this snapshot. Can be null. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1aca1e24b5ad0a93b34095b625ac771c51` | `const char *` The description of this snapshot. Can be null. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a076994e71d2c9b4d78cc45df42a49057` | `const char *` The name of device which wrote snapshot. Can be null. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a885964d662bfe0911c7f61113540dd5b` | `bool` Whether or not this snapshot has any changes pending that have not been uploaded to the server. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a9fcee56f17c4ce2b7efc3af67bd98ba3` | `int64_t` The last time this snapshot was modified, in millis since epoch. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a6b817c8152b08c77a5257d53d42a6726` | `int64_t` The played time of this snapshot in milliseconds. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a9d02f0a07d4be4ee899b8784bc15a250` | `int64_t` The progress value for this snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1a3062db3b717f397a7724f1f71604e942` | `const char *` The ID of this snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata_1add74e9335414af0675cfd0d97357726b` | `const char *` The unique name of this snapshot. Can be null. |

## Public attributes

### cover_image_aspect_ratio

```c++
float PgsSnapshotMetadata::cover_image_aspect_ratio
```
The aspect ratio of cover image for snapshot.

### cover_image_uri

```c++
const char * PgsSnapshotMetadata::cover_image_uri
```
The URI of the cover image for this snapshot. Can be null.

### description

```c++
const char * PgsSnapshotMetadata::description
```
The description of this snapshot. Can be null.

### device_name

```c++
const char * PgsSnapshotMetadata::device_name
```
The name of device which wrote snapshot. Can be null.

### has_change_pending

```c++
bool PgsSnapshotMetadata::has_change_pending
```
Whether or not this snapshot has any changes pending that have not been uploaded to the server.

### last_modified_timestamp

```c++
int64_t PgsSnapshotMetadata::last_modified_timestamp
```
The last time this snapshot was modified, in millis since epoch.

### played_time

```c++
int64_t PgsSnapshotMetadata::played_time
```
The played time of this snapshot in milliseconds.

### progress_value

```c++
int64_t PgsSnapshotMetadata::progress_value
```
The progress value for this snapshot.

### snapshot_id

```c++
const char * PgsSnapshotMetadata::snapshot_id
```
The ID of this snapshot.

### unique_name

```c++
const char * PgsSnapshotMetadata::unique_name
```
The unique name of this snapshot. Can be null.