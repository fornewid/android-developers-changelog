---
title: pgs Namespace  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/cpp/v2/api/namespace/pgs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.





# pgs

## Summary

| Functions | |
| --- | --- |
| `BuildJavaSnapshotMetadataChange(JNIEnv *env, PgsSnapshotMetadataChange *change)` | `jobject` |
| `ClearSnapshotMetadataChangeCache(JNIEnv *env)` | `void` |
| `PopulatePgsSnapshotMetadataFromJavaSnapshotMetadata(JNIEnv *env, jobject snapshot_metadata_jobject, PgsSnapshotMetadata *metadata)` | `bool` |

## Functions

### BuildJavaSnapshotMetadataChange

```
jobject BuildJavaSnapshotMetadataChange(
  JNIEnv *env,
  PgsSnapshotMetadataChange *change
)
```

### ClearSnapshotMetadataChangeCache

```
void ClearSnapshotMetadataChangeCache(
  JNIEnv *env
)
```

### PopulatePgsSnapshotMetadataFromJavaSnapshotMetadata

```
bool PopulatePgsSnapshotMetadataFromJavaSnapshotMetadata(
  JNIEnv *env,
  jobject snapshot_metadata_jobject,
  PgsSnapshotMetadata *metadata
)
```