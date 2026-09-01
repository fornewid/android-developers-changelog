---
title: https://developer.android.com/games/services/cpp/v2/api/namespace/pgs
url: https://developer.android.com/games/services/cpp/v2/api/namespace/pgs
source: md.txt
---

# pgs

## Summary

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/namespace/pgs#namespacepgs_1a8cb1933748d4712fec404e2922961a0e(JNIEnv *env, https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change *change)` | `jobject` |
| `https://developer.android.com/games/services/cpp/v2/api/namespace/pgs#namespacepgs_1a1b0ab9e50c87c8dd24b4d6d9f8b3cc07(JNIEnv *env)` | `void` |
| `https://developer.android.com/games/services/cpp/v2/api/namespace/pgs#namespacepgs_1a47cf9a6aa684514d7dfeba704b2e58ba(JNIEnv *env, jobject snapshot_metadata_jobject, https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata *metadata)` | `bool` |

## Functions

### BuildJavaSnapshotMetadataChange

```c++
jobject BuildJavaSnapshotMetadataChange(
  JNIEnv *env,
  PgsSnapshotMetadataChange *change
)
```

### ClearSnapshotMetadataChangeCache

```c++
void ClearSnapshotMetadataChangeCache(
  JNIEnv *env
)
```

### PopulatePgsSnapshotMetadataFromJavaSnapshotMetadata

```c++
bool PopulatePgsSnapshotMetadataFromJavaSnapshotMetadata(
  JNIEnv *env,
  jobject snapshot_metadata_jobject,
  PgsSnapshotMetadata *metadata
)
```