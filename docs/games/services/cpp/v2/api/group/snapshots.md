---
title: https://developer.android.com/games/services/cpp/v2/api/group/snapshots
url: https://developer.android.com/games/services/cpp/v2/api/group/snapshots
source: md.txt
---

# Play Games Services Snapshots

Native API for Play Games Services Snapshots.

## Summary

| ### Enumerations ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaa10cf8a1564d21af27420623d63d62e5` | enum |

| ### Typedefs ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaee3bcc2f9438ea9299930b0e35111760` | typedef `struct PgsSnapshot` An opaque handle to a Snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gafb2b8260c8b2240d88c355adf8726feb` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gafb2b8260c8b2240d88c355adf8726feb` An opaque handle to a Snapshot Conflict. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga8b9bfb3a5cb9f9494e443376658a7c9f` | typedef `struct https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga8b9bfb3a5cb9f9494e443376658a7c9f` An opaque handle to Snapshot Contents. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaf5f967f93da3e14356e67337a5be3a5c)(PgsStatusCode status_code, PgsSnapshotMetadata *metadata, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_commitAndClose. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gacb42225272ca4c26a34d6e805d9972a7)(PgsStatusCode status_code, const char *snapshot_id, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_delete. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaa632b9ed71fa531d9baccb35cfca7326)(PgsStatusCode status_code, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_discardAndClose. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga0cdcb93b96d7801d861d6599349bb408)(PgsStatusCode status_code, int32_t max_size, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_getMaxCoverImageSize. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga8c2b82bf7114135cc1b28322daa3ea43)(PgsStatusCode status_code, int32_t max_size, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_getMaxDataSize. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga04295f5ecc4fc8b78039f4c5f1d5b52a)(PgsStatusCode status_code, PgsSnapshotMetadata *snapshots_array, size_t snapshots_count, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_load. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga83d4bc05f88f6cd81213366f6bf6f1c5)(PgsStatusCode status_code, PgsSnapshot *snapshot, PgsSnapshotConflict *conflict, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_open and PgsSnapshotsClient_resolveConflict. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaf220026e09486a99362c54551c9e3518)(PgsStatusCode status_code, void *user_data)` | typedef `void(*` Callback for PgsSnapshotsClient_showSelectSnapshotUI. |

| ### Functions ||
|---|---|
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga845645382771116b0903a2e345f32147(https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gafb2b8260c8b2240d88c355adf8726feb *conflict)` | `void` Destroys a PgsSnapshotConflict instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gadd1a8b24f551abdf7f951ade71da8294(https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga8b9bfb3a5cb9f9494e443376658a7c9f *contents)` | `void` Destroys a PgsSnapshotContents instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga69710af173d8fed22920284b13f89f53(https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaee3bcc2f9438ea9299930b0e35111760 *snapshot)` | `void` Destroys a PgsSnapshot instance. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga81fa75604cf0446f0cbbc511057756bc(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaee3bcc2f9438ea9299930b0e35111760 *snapshot, https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change *metadata_change, const uint8_t *data, size_t data_size, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaf5f967f93da3e14356e67337a5be3a5c callback, void *user_data)` | `void` Asynchronously commits and closes a snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga20d607fcd17d57f2bcff2ebaa8a28edb(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaee3bcc2f9438ea9299930b0e35111760 *snapshot, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gacb42225272ca4c26a34d6e805d9972a7 callback, void *user_data)` | `void` Asynchronously deletes a snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga22181bd79613decdfe61e7db2508f013(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaee3bcc2f9438ea9299930b0e35111760 *snapshot, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaa632b9ed71fa531d9baccb35cfca7326 callback, void *user_data)` | `void` Asynchronously discards and closes a snapshot. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gae3ef9653a7204dca59b6d9f338f17687(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga0cdcb93b96d7801d861d6599349bb408 callback, void *user_data)` | `void` Asynchronously loads the maximum size of snapshot cover image in bytes. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga127c7113db448bcf7a5cfac77cdc64b7(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga8c2b82bf7114135cc1b28322daa3ea43 callback, void *user_data)` | `void` Asynchronously loads the maximum size of snapshot data. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gae264f8b21dcf7d7923c7b4b41a2329a1(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, bool force_reload, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga04295f5ecc4fc8b78039f4c5f1d5b52a callback, void *user_data)` | `void` Asynchronously loads snapshot data for the currently signed-in player for this application, invoking a callback upon completion. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga6925c7d231a1314fbb2eb37de2f4215c(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, const char *file_name, bool create_if_not_found, enum PgsSnapshotConflictPolicy conflict_policy, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga83d4bc05f88f6cd81213366f6bf6f1c5 callback, void *user_data)` | `void` Asynchronously opens a snapshot with given file name. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga5c3f30efbf2abc14661879bb4b2ca0ad(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata *metadata, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga83d4bc05f88f6cd81213366f6bf6f1c5 callback, void *user_data)` | `void` Asynchronously opens a snapshot from metadata with default conflict policy (manual). |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gab14cd7b769ccbd8ca0446e0afc757d19(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata *metadata, enum PgsSnapshotConflictPolicy conflict_policy, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga83d4bc05f88f6cd81213366f6bf6f1c5 callback, void *user_data)` | `void` Asynchronously opens a snapshot from metadata with given conflict policy. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga136f1ee317239de20a4ee180fb8cbb67(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, const char *file_name, bool create_if_not_found, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga83d4bc05f88f6cd81213366f6bf6f1c5 callback, void *user_data)` | `void` Asynchronously opens a snapshot with given file name and default conflict policy (manual). |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga153d11f832a717bd5725e12c9ccfebbc(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, const char *conflict_id, const char *snapshot_id, https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change *metadata_change, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga8b9bfb3a5cb9f9494e443376658a7c9f *contents, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga83d4bc05f88f6cd81213366f6bf6f1c5 callback, void *user_data)` | `void` Asynchronously resolves a snapshot conflict. |
| `https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1ga153d058e2579be62c33e848927c157a7(https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gac5f98c3af7334d48b0346bbee83b5553 *snapshots_client, jobject activity, const char *title, bool allow_add_button, bool allow_delete_button, int max_snapshots, https://developer.android.com/games/services/cpp/v2/api/group/snapshots#group__snapshots_1gaf220026e09486a99362c54551c9e3518 callback, void *user_data)` | `void` Asynchronously shows the snapshot selection UI. |

## Enumerations

### PgsSnapshotConflictPolicy

```c++
 PgsSnapshotConflictPolicy
```

## Typedefs

### PgsSnapshot

```c++
struct PgsSnapshot PgsSnapshot
```
An opaque handle to a Snapshot.

### PgsSnapshotConflict

```c++
struct PgsSnapshotConflict PgsSnapshotConflict
```
An opaque handle to a Snapshot Conflict.

### PgsSnapshotContents

```c++
struct PgsSnapshotContents PgsSnapshotContents
```
An opaque handle to Snapshot Contents.

### PgsSnapshotsClient_CommitAndCloseCallback

```c++
void(* PgsSnapshotsClient_CommitAndCloseCallback)(PgsStatusCode status_code, PgsSnapshotMetadata *metadata, void *user_data)
```
Callback for PgsSnapshotsClient_commitAndClose.

This is invoked after the asynchronous operation to commit and close completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `metadata` | The metadata of committed snapshot, or NULL if status_code is not PGS_STATUS_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsSnapshotsClient_DeleteCallback

```c++
void(* PgsSnapshotsClient_DeleteCallback)(PgsStatusCode status_code, const char *snapshot_id, void *user_data)
```
Callback for PgsSnapshotsClient_delete.

This is invoked after the asynchronous operation to delete completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `snapshot_id` | The ID of deleted snapshot, or false if status_code is not PGS_STATUS_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsSnapshotsClient_DiscardAndCloseCallback

```c++
void(* PgsSnapshotsClient_DiscardAndCloseCallback)(PgsStatusCode status_code, void *user_data)
```
Callback for PgsSnapshotsClient_discardAndClose.

This is invoked after the asynchronous operation to discard and close completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsSnapshotsClient_GetMaxCoverImageSizeCallback

```c++
void(* PgsSnapshotsClient_GetMaxCoverImageSizeCallback)(PgsStatusCode status_code, int32_t max_size, void *user_data)
```
Callback for PgsSnapshotsClient_getMaxCoverImageSize.

This is invoked after the asynchronous operation to get max cover image size completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `max_size` | The maximum size of snapshot cover image in bytes, or 0 if status_code is not PGS_STATUS_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsSnapshotsClient_GetMaxDataSizeCallback

```c++
void(* PgsSnapshotsClient_GetMaxDataSizeCallback)(PgsStatusCode status_code, int32_t max_size, void *user_data)
```
Callback for PgsSnapshotsClient_getMaxDataSize.

This is invoked after the asynchronous operation to get max data size completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `max_size` | The maximum size of snapshot data in bytes, or 0 if status_code is not PGS_STATUS_SUCCESS. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsSnapshotsClient_LoadCallback

```c++
void(* PgsSnapshotsClient_LoadCallback)(PgsStatusCode status_code, PgsSnapshotMetadata *snapshots_array, size_t snapshots_count, void *user_data)
```
Callback for PgsSnapshotsClient_load.

This is invoked after the asynchronous operation to load snapshots completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `snapshots_array` | Pointer to an array of [PgsSnapshotMetadata](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata#struct_pgs_snapshot_metadata) objects, or NULL if status_code is not PGS_STATUS_SUCCESS. | | `snapshots_count` | The number of snapshots in snapshots_array. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsSnapshotsClient_OpenCallback

```c++
void(* PgsSnapshotsClient_OpenCallback)(PgsStatusCode status_code, PgsSnapshot *snapshot, PgsSnapshotConflict *conflict, void *user_data)
```
Callback for PgsSnapshotsClient_open and PgsSnapshotsClient_resolveConflict.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `snapshot` | The opened snapshot, if successful and no conflict. NULL otherwise. The caller is responsible for calling PgsSnapshot_destroy. | | `conflict` | The conflict data, if a conflict occurred. NULL otherwise. The caller is responsible for calling PgsSnapshotConflict_destroy. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

### PgsSnapshotsClient_ShowSelectSnapshotUICallback

```c++
void(* PgsSnapshotsClient_ShowSelectSnapshotUICallback)(PgsStatusCode status_code, void *user_data)
```
Callback for PgsSnapshotsClient_showSelectSnapshotUI.

This is invoked after the asynchronous operation to show select snapshot UI completes or fails.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `status_code` | Result of the operation. PGS_STATUS_SUCCESS on success. | | `user_data` | Pointer to the user-provided data passed in the original call. | |

## Functions

### PgsSnapshotConflict_destroy

```c++
void PgsSnapshotConflict_destroy(
  PgsSnapshotConflict *conflict
)
```
Destroys a PgsSnapshotConflict instance.

This function releases all resources associated with the snapshot conflict handle. The handle becomes invalid after this call.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `conflict` | The snapshot conflict handle to destroy. | |

### PgsSnapshotContents_destroy

```c++
void PgsSnapshotContents_destroy(
  PgsSnapshotContents *contents
)
```
Destroys a PgsSnapshotContents instance.

This function releases all resources associated with the snapshot contents handle. The handle becomes invalid after this call.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `contents` | The snapshot contents handle to destroy. | |

### PgsSnapshot_destroy

```c++
void PgsSnapshot_destroy(
  PgsSnapshot *snapshot
)
```
Destroys a PgsSnapshot instance.

This function releases all resources associated with the snapshot handle. The handle becomes invalid after this call.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot handle to destroy. | |

### PgsSnapshotsClient_commitAndClose

```c++
void PgsSnapshotsClient_commitAndClose(
  PgsSnapshotsClient *snapshots_client,
  PgsSnapshot *snapshot,
  PgsSnapshotMetadataChange *metadata_change,
  const uint8_t *data,
  size_t data_size,
  PgsSnapshotsClient_CommitAndCloseCallback callback,
  void *user_data
)
```
Asynchronously commits and closes a snapshot.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `snapshot` | The snapshot to commit and close. | | `metadata_change` | The metadata changes to apply to the snapshot. | | `data` | The binary data to update in the snapshot, or NULL to commit without updating binary data. | | `data_size` | The size of data in bytes. Ignored if data is NULL. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_CommitAndCloseCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_delete

```c++
void PgsSnapshotsClient_delete(
  PgsSnapshotsClient *snapshots_client,
  PgsSnapshot *snapshot,
  PgsSnapshotsClient_DeleteCallback callback,
  void *user_data
)
```
Asynchronously deletes a snapshot.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `snapshot` | The snapshot to delete. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_DeleteCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_discardAndClose

```c++
void PgsSnapshotsClient_discardAndClose(
  PgsSnapshotsClient *snapshots_client,
  PgsSnapshot *snapshot,
  PgsSnapshotsClient_DiscardAndCloseCallback callback,
  void *user_data
)
```
Asynchronously discards and closes a snapshot.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `snapshot` | The snapshot to discard and close. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_DiscardAndCloseCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_getMaxCoverImageSize

```c++
void PgsSnapshotsClient_getMaxCoverImageSize(
  PgsSnapshotsClient *snapshots_client,
  PgsSnapshotsClient_GetMaxCoverImageSizeCallback callback,
  void *user_data
)
```
Asynchronously loads the maximum size of snapshot cover image in bytes.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsSnapshotsClient_GetMaxCoverImageSizeCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsSnapshotsClient_getMaxDataSize

```c++
void PgsSnapshotsClient_getMaxDataSize(
  PgsSnapshotsClient *snapshots_client,
  PgsSnapshotsClient_GetMaxDataSizeCallback callback,
  void *user_data
)
```
Asynchronously loads the maximum size of snapshot data.

The returned value is guaranteed to be at least 3MB, but may increase in the future.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsSnapshotsClient_GetMaxDataSizeCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsSnapshotsClient_load

```c++
void PgsSnapshotsClient_load(
  PgsSnapshotsClient *snapshots_client,
  bool force_reload,
  PgsSnapshotsClient_LoadCallback callback,
  void *user_data
)
```
Asynchronously loads snapshot data for the currently signed-in player for this application, invoking a callback upon completion.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `force_reload` | If true, this call will clear any locally cached data and attempt to fetch the latest data from the server. This would commonly be used for something like a user-initiated refresh. Normally, this should be set to false to gain advantages of data caching. | | `callback` | Function to be called with the result of the asynchronous operation. See PgsSnapshotsClient_LoadCallback. | | `user_data` | Arbitrary data pointer to be passed back to the callback. | |

### PgsSnapshotsClient_open

```c++
void PgsSnapshotsClient_open(
  PgsSnapshotsClient *snapshots_client,
  const char *file_name,
  bool create_if_not_found,
  enum PgsSnapshotConflictPolicy conflict_policy,
  PgsSnapshotsClient_OpenCallback callback,
  void *user_data
)
```
Asynchronously opens a snapshot with given file name.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `file_name` | The file name of snapshot to open. | | `create_if_not_found` | If true, new snapshot will be created if one does not exist. | | `conflict_policy` | Policy for resolving conflicts. See PgsSnapshotConflictPolicy. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_OpenCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_openFromMetadata

```c++
void PgsSnapshotsClient_openFromMetadata(
  PgsSnapshotsClient *snapshots_client,
  PgsSnapshotMetadata *metadata,
  PgsSnapshotsClient_OpenCallback callback,
  void *user_data
)
```
Asynchronously opens a snapshot from metadata with default conflict policy (manual).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `metadata` | The metadata of the snapshot to open. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_OpenCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_openFromMetadataWithPolicy

```c++
void PgsSnapshotsClient_openFromMetadataWithPolicy(
  PgsSnapshotsClient *snapshots_client,
  PgsSnapshotMetadata *metadata,
  enum PgsSnapshotConflictPolicy conflict_policy,
  PgsSnapshotsClient_OpenCallback callback,
  void *user_data
)
```
Asynchronously opens a snapshot from metadata with given conflict policy.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `metadata` | The metadata of the snapshot to open. | | `conflict_policy` | Policy for resolving conflicts. See PgsSnapshotConflictPolicy. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_OpenCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_openWithDefaultPolicy

```c++
void PgsSnapshotsClient_openWithDefaultPolicy(
  PgsSnapshotsClient *snapshots_client,
  const char *file_name,
  bool create_if_not_found,
  PgsSnapshotsClient_OpenCallback callback,
  void *user_data
)
```
Asynchronously opens a snapshot with given file name and default conflict policy (manual).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `file_name` | The file name of snapshot to open. | | `create_if_not_found` | If true, new snapshot will be created if one does not exist. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_OpenCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_resolveConflict

```c++
void PgsSnapshotsClient_resolveConflict(
  PgsSnapshotsClient *snapshots_client,
  const char *conflict_id,
  const char *snapshot_id,
  PgsSnapshotMetadataChange *metadata_change,
  PgsSnapshotContents *contents,
  PgsSnapshotsClient_OpenCallback callback,
  void *user_data
)
```
Asynchronously resolves a snapshot conflict.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `conflict_id` | The ID of the conflict to resolve. | | `snapshot_id` | The ID of the snapshot to use for resolution. | | `metadata_change` | The metadata changes to apply to the snapshot, or NULL for no changes. | | `contents` | The contents to resolve the conflict with. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_OpenCallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |

### PgsSnapshotsClient_showSelectSnapshotUI

```c++
void PgsSnapshotsClient_showSelectSnapshotUI(
  PgsSnapshotsClient *snapshots_client,
  jobject activity,
  const char *title,
  bool allow_add_button,
  bool allow_delete_button,
  int max_snapshots,
  PgsSnapshotsClient_ShowSelectSnapshotUICallback callback,
  void *user_data
)
```
Asynchronously shows the snapshot selection UI.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshots_client` | The client handle. | | `activity` | The activity to use for launching the UI. | | `title` | The title for the UI. | | `allow_add_button` | Whether to allow adding snapshots. | | `allow_delete_button` | Whether to allow deleting snapshots. | | `max_snapshots` | The maximum number of snapshots to display. | | `callback` | Function to be called with result of asynchronous operation. See PgsSnapshotsClient_ShowSelectSnapshotUICallback. | | `user_data` | Arbitrary data pointer to be passed back to callback. | |