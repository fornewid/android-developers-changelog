---
title: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change
source: md.txt
---

# PgsSnapshotMetadataChange

Represents metadata changes for an instance of `PgsSnapshot`.

## Summary

| ### Public attributes ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1a0aeb8d6053032be4a735ff4413b71981` | `const uint8_t *` The new cover image for snapshot, in PNG format. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1ad8284de9cf1f767879692c2197600e27` | `size_t` Size of cover_image_png_data in bytes. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1a9b89bbdecc95be04612620e0bdb8fa78` | `bool` If true, cover_image_png_data field is valid and should be used to update snapshot metadata. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1a4da286746c7881b2c9092807e1b4386f` | `const char *` The new description for the snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1ac6e24b540d112991da2275b1eb06766e` | `bool` If true, description field is valid and should be used to update snapshot metadata. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1a3277baa7ebc7e731686369283fbb661f` | `int64_t` The new played time for snapshot in milliseconds. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1a93c0680d666a142b09573b2cee7dff43` | `bool` If true, played_time_millis field is valid and should be used to update snapshot metadata. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1a2fdbf773f8e24e07d3272d042ec05ccd` | `int64_t` The new progress value for snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change_1a145ddcdc64fa7dae396b6c069f0911e9` | `bool` If true, progress_value field is valid and should be used to update snapshot metadata. |

## Public attributes

### cover_image_png_data

```c++
const uint8_t * PgsSnapshotMetadataChange::cover_image_png_data
```
The new cover image for snapshot, in PNG format.

### cover_image_png_data_size

```c++
size_t PgsSnapshotMetadataChange::cover_image_png_data_size
```
Size of cover_image_png_data in bytes.

### cover_image_updated

```c++
bool PgsSnapshotMetadataChange::cover_image_updated
```
If true, cover_image_png_data field is valid and should be used to update snapshot metadata.

### description

```c++
const char * PgsSnapshotMetadataChange::description
```
The new description for the snapshot.

### description_updated

```c++
bool PgsSnapshotMetadataChange::description_updated
```
If true, description field is valid and should be used to update snapshot metadata.

### played_time_millis

```c++
int64_t PgsSnapshotMetadataChange::played_time_millis
```
The new played time for snapshot in milliseconds.

### played_time_millis_updated

```c++
bool PgsSnapshotMetadataChange::played_time_millis_updated
```
If true, played_time_millis field is valid and should be used to update snapshot metadata.

### progress_value

```c++
int64_t PgsSnapshotMetadataChange::progress_value
```
The new progress value for snapshot.

### progress_value_updated

```c++
bool PgsSnapshotMetadataChange::progress_value_updated
```
If true, progress_value field is valid and should be used to update snapshot metadata.