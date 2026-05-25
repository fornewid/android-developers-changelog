---
title: https://developer.android.com/games/pgs/cpp/saved-games
url: https://developer.android.com/games/pgs/cpp/saved-games
source: md.txt
---

This guide shows you how to implement saved games using the snapshots API
provided by Google Play Games Services in the C++ SDK. The APIs can be found
in [`PgsSnapshotsClient`](https://developer.android.com/games/services/cpp/v2/api/group/play-games#pgssnapshotsclient).

### Before you begin

- For information about the feature, see [Saved games](https://developer.android.com/games/pgs/savedgames).
- Follow the instructions for installing and setting up your app to use
  Google Play Games Services in the
  [Set Up Google Play services SDK](https://developers.google.com/android/guides/setup) guide.

- Define the saved games support for your game, by
  following the instructions in the
  [Google Play Console guide](https://developer.android.com/games/pgs/leaderboards#creating_a_leaderboard).

- Familiarize yourself with the recommendations described in
  [Quality Checklist](https://developer.android.com/games/pgs/quality).

### Get the snapshots client

To start using the snapshots API, your game must first obtain a
[`PgsSnapshotsClient`](https://developer.android.com/games/services/cpp/v2/api/group/play-games#pgssnapshotsclient) handle. You can do this by calling the
[`PgsSnapshotsClient_create()`](https://developer.android.com/games/services/cpp/v2/api/group/play-games#pgssnapshotsclient_create) method, passing in the Android Activity.

**Note:** The C++ SDK functions return results asynchronously through
callbacks.

```c++
// Assuming 'android_activity' is a jobject referencing your Android Activity
PgsSnapshotsClient* snapshots_client = PgsSnapshotsClient_create(android_activity);

// ... use the client ...

// When done, destroy the client to free resources
// PgsSnapshotsClient_destroy(snapshots_client);
```

### Display saved games

You can integrate the snapshots API wherever your game provides players with
the option to save or restore their progress.
To simplify development, the snapshots API provides a default saved games
selection user interface (UI). To launch this UI, call
[`PgsSnapshotsClient_showSelectSnapshotUI`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotsclient_showselectsnapshotui).

```c++
// Callback function to handle the result of showing the UI
void OnShowSavedGamesUI(PgsStatusCode status_code, void* user_data) {
  if (status_code == PGS_STATUS_SUCCESS) {
    // UI was shown successfully. The player can now interact with it.
    // The game doesn't receive direct data back from this callback about
    // which snapshot was selected. Your game should typically provide options
    // to load or open snapshots by name after the UI is dismissed.
  } else {
    // Handle error or failure to show UI
  }
}

// Function to show the default Saved Games UI
void ShowSavedGamesUI(PgsSnapshotsClient* client, jobject activity) {
  const char* title = "See My Saves";
  bool allow_add_button = true;
  bool allow_delete_button = true;
  int max_snapshots = 5;

  PgsSnapshotsClient_showSelectSnapshotUI(
      client,
      activity,
      title,
      allow_add_button,
      allow_delete_button,
      max_snapshots,
      OnShowSavedGamesUI,
      NULL // user_data
  );
}

// Example usage:
// ShowSavedGamesUI(snapshots_client, android_activity);
```

## Write saved games

To store content to a saved game:

1. Asynchronously open a snapshot using [`PgsSnapshotsClient_open()`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotsclient_open). Specify `create_if_not_found` as true if you want to create a new save.
2. The result is provided in the [`PgsSnapshotsClient_OpenCallback`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotsclient_opencallback). If successful and there's no conflict, you'll get a `PgsSnapshot*`.
3. Prepare the data you want to save as a byte array (`uint8_t*`).
4. Create a [`PgsSnapshotMetadataChange*`](https://developer.android.com/games/services/cpp/v2/api/struct/pgs-snapshot-metadata-change#struct_pgs_snapshot_metadata_change) object to describe the save.
5. Call [`PgsSnapshotsClient_commitAndClose`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotsclient_commitandclose) to send the changes to
   Google's servers.

   ```c++
   // Callback for commitAndClose
   void OnSnapshotCommitted(PgsStatusCode status_code, PgsSnapshotMetadata* metadata, void* user_data) {
       if (status_code == PGS_STATUS_SUCCESS) {
       // Save successful
       if (metadata) {
       // Metadata for the committed snapshot
       PgsSnapshotMetadata_Release(metadata);
     }
   } else {
       // Handle error
     }
   }

   // Function to write data to a snapshot
   void WriteSnapshot(PgsSnapshotsClient* client, PgsSnapshot* snapshot,
                  const uint8_t* data, size_t data_size,
                  const char* description /*, Bitmap coverImage */) {

   PgsSnapshotMetadataChange* metadataChange = NULL; // Placeholder

     // Commit the operation
     PgsSnapshotsClient_commitAndClose(
         client,
         snapshot,
         metadataChange,
         data,
         data_size,
         OnSnapshotCommitted,
         NULL // user_data
     );

     // if (metadataChange) PgsSnapshotMetadataChange_Release(metadataChange);
   }

   // Callback for opening the snapshot before writing
   void OnSnapshotOpenForWrite(PgsStatusCode status_code,
                           PgsSnapshot* snapshot,
                           PgsSnapshotConflict* conflict,
                           void* user_data) {
     if (status_code == PGS_STATUS_SUCCESS) {
       if (snapshot) {
         // Successfully opened/created. Now write to it.
        const char* save_data_str = "MY_GAME_SAVE_DATA";
        const uint8_t* data = (const uint8_t*)save_data_str;
        size_t data_size = strlen(save_data_str);

         WriteSnapshot((PgsSnapshotsClient*)user_data, snapshot, data, data_size, "My Save Description");
         // PgsSnapshot_destroy(snapshot) is likely called after commitAndClose by the SDK
       } else if (conflict) {
         // Handle conflict before writing, or open with a policy that auto-resolves.
         PgsSnapshotConflict_destroy(conflict);
       }
     } else {
       // Handle error opening
     }
   }

   // Example: Open and write to a snapshot
   void OpenAndWriteExample(PgsSnapshotsClient* client, const char* snapshot_name) {
   PgsSnapshotsClient_open(
     client,
     snapshot_name,
     true, // create_if_not_found
     kPgsSnapshotConflictPolicyManual, // Or another policy
     OnSnapshotOpenForWrite,
     client // user_data
   );
   }
   ```

## Load saved games

To retrieve saved games:

1. Asynchronously open the snapshot by name using `PgsSnapshotsClient_open()`.
2. In the [`PgsSnapshotsClient_OpenCallback`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotsclient_opencallback), if successful, access the
   data. The API provides a way to get the `uint8_t*` data and size, although
   the method for reading bytes from [`PgsSnapshot`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshot) or an associated
   [`PgsSnapshotContents`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotcontents) is not detailed in this document.

   ```c++
   // Assuming functions exist to read data from PgsSnapshotContents
   // For example, PgsSnapshotContents* PgsSnapshot_getContents(PgsSnapshot* snapshot);
   // For example, bool PgsSnapshotContents_readFully(PgsSnapshotContents* contents, uint8_t** out_data, size_t* out_size);
   // For example, void PgsSnapshotContents_releaseData(uint8_t* data);

   void OnSnapshotOpenForRead(PgsStatusCode status_code,
                          PgsSnapshot* snapshot,
                          PgsSnapshotConflict* conflict,
                          void* user_data) {
       if (status_code == PGS_STATUS_SUCCESS) {
       if (snapshot) {
       // Successfully opened. Now read from it.
       // THE FOLLOWING IS HYPOTHETICAL based on common patterns:
       // PgsSnapshotContents* contents = PgsSnapshot_getContents(snapshot);
       // uint8_t* data = NULL;
       // size_t data_size = 0;
       // if (contents && PgsSnapshotContents_readFully(contents, &data, &data_size)) {
       //   // Successfully read data
       //   Log("Snapshot data loaded, size: %zu", data_size);
       //   ... process data ...
       //   PgsSnapshotContents_releaseData(data);
       // }
       // PgsSnapshotContents_destroy(contents); // If necessary
         PgsSnapshot_destroy(snapshot);
       } else if (conflict) {
         // Handle conflict
         Log("Snapshot open resulted in a conflict.");
         PgsSnapshotConflict_destroy(conflict);
       }
     } else {
       // Handle error opening
       Log("Error while opening Snapshot: %d", status_code);
     }
   }

   // Example: Load a specific saved game
   void LoadSnapshotByName(PgsSnapshotsClient* client, const char* snapshot_name) {
     int conflictResolutionPolicy = kPgsSnapshotConflictPolicyMostRecentlyModified;

     PgsSnapshotsClient_open(
         client,
         snapshot_name,
         false, // create_if_not_found
         conflictResolutionPolicy,
         OnSnapshotOpenForRead,
         NULL // user_data
     );
   }
   ```

### Handle saved game conflicts

When [`PgsSnapshotsClient_open`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotsclient_open) callback is called, if the `conflict`
parameter is not `NULL`, a conflict has occurred use
[`PgsSnapshotsClient_resolveConflict`](https://developer.android.com/games/services/cpp/v2/api/group/snapshots#pgssnapshotsclient_resolveconflict) to resolve conflict.

```c++
/// @brief Asynchronously resolves a snapshot conflict.
///
/// @param snapshots_client The client handle.
/// @param conflict_id The ID of the conflict to resolve.
/// @param snapshot_id The ID of the snapshot to use for resolution.
/// @param metadata_change The metadata changes to apply to the snapshot, or
/// NULL for no changes.
/// @param contents The contents to resolve the conflict with.
/// @param callback Function to be called with result of asynchronous
/// operation. See PgsSnapshotsClient_OpenCallback.
/// @param user_data Arbitrary data pointer to be passed back to callback.
void PgsSnapshotsClient_resolveConflict(
    PgsSnapshotsClient* snapshots_client,
    const char* conflict_id,
    const char* snapshot_id,
    PgsSnapshotMetadataChange* metadata_change,
    PgsSnapshotContents* contents,
    PgsSnapshotsClient_OpenCallback callback,
    void* user_data);
```