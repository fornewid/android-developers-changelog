---
title: PgsSnapshotMetadataChange Struct Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# PgsSnapshotMetadataChange

Represents metadata changes for an instance of `PgsSnapshot`.

## Summary

| Public attributes | |
| --- | --- |
| `cover_image_png_data` | `const uint8_t *`  The new cover image for snapshot, in PNG format. |
| `cover_image_png_data_size` | `size_t`  Size of cover\_image\_png\_data in bytes. |
| `cover_image_updated` | `bool`  If true, cover\_image\_png\_data field is valid and should be used to update snapshot metadata. |
| `description` | `const char *`  The new description for the snapshot. |
| `description_updated` | `bool`  If true, description field is valid and should be used to update snapshot metadata. |
| `played_time_millis` | `int64_t`  The new played time for snapshot in milliseconds. |
| `played_time_millis_updated` | `bool`  If true, played\_time\_millis field is valid and should be used to update snapshot metadata. |
| `progress_value` | `int64_t`  The new progress value for snapshot. |
| `progress_value_updated` | `bool`  If true, progress\_value field is valid and should be used to update snapshot metadata. |

## Public attributes

### cover\_image\_png\_data

```
const uint8_t * PgsSnapshotMetadataChange::cover_image_png_data
```

The new cover image for snapshot, in PNG format.

### cover\_image\_png\_data\_size

```
size_t PgsSnapshotMetadataChange::cover_image_png_data_size
```

Size of cover\_image\_png\_data in bytes.

### cover\_image\_updated

```
bool PgsSnapshotMetadataChange::cover_image_updated
```

If true, cover\_image\_png\_data field is valid and should be used to update snapshot metadata.

### description

```
const char * PgsSnapshotMetadataChange::description
```

The new description for the snapshot.

### description\_updated

```
bool PgsSnapshotMetadataChange::description_updated
```

If true, description field is valid and should be used to update snapshot metadata.

### played\_time\_millis

```
int64_t PgsSnapshotMetadataChange::played_time_millis
```

The new played time for snapshot in milliseconds.

### played\_time\_millis\_updated

```
bool PgsSnapshotMetadataChange::played_time_millis_updated
```

If true, played\_time\_millis field is valid and should be used to update snapshot metadata.

### progress\_value

```
int64_t PgsSnapshotMetadataChange::progress_value
```

The new progress value for snapshot.

### progress\_value\_updated

```
bool PgsSnapshotMetadataChange::progress_value_updated
```

If true, progress\_value field is valid and should be used to update snapshot metadata.