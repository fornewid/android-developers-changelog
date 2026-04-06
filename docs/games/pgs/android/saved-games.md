---
title: https://developer.android.com/games/pgs/android/saved-games
url: https://developer.android.com/games/pgs/android/saved-games
source: md.txt
---

> [!NOTE]
> **Note:** This guide is for the Play Games Services v2 SDK. For information on the previous version of this SDK, see the [Play Games Services v1
> documentation](https://developer.android.com/games/pgs/v1/android/saved-games).

This guide shows you how to implement saved games using the snapshots API
provided by Google Play Games Services. The APIs can be found in the
[`com.google.android.gms.games.snapshot`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#isConflict())
and
[`com.google.android.gms.games`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict)
packages.

## Before you begin

For information about the feature, see the [Saved Games
overview](https://developer.android.com/games/pgs/savedgames).

- [Enable saved games support](https://developer.android.com/games/pgs/console/enable-features#enabling_saved_games) for your game in Google Play Console.
- Download and review the saved games code sample in the [Android samples
  page](https://github.com/playgameservices/android-basic-samples)
- Familiarize yourself with the recommendations described in [Quality
  Checklist](https://developer.android.com/games/pgs/quality).

## Get the snapshots client

To start using the snapshots API, your game must first obtain a
[`SnapshotsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient)
object. You can do this by calling the
[`Games.getSnapshotsContents()`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/Snapshot#public-abstract-snapshotcontents-getsnapshotcontents)
method and passing in the activity.

> [!NOTE]
> **Note:** The [`SnapshotsClient`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient) class uses the Google Play services [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) class to return results asynchronously. To learn more about using tasks to manage threaded work, see the [Tasks API developer
> guide](https://developers.google.com/android/guides/tasks).

## Display saved games

You can integrate the snapshots API wherever your game provides players with the
option to save or restore their progress. Your game might display such an option
at designated save or restore points or allow players to save or restore
progress at any time.

Once players select the save or restore option in your game, your game can
optionally bring up a screen that prompts players to enter information for a new
saved game or to select an existing saved game to restore.

To simplify your development, the snapshots API provides a default saved games
selection user interface (UI) that you can use out-of-the-box. The saved games
selection UI allows players to create a new saved game, view details about
existing saved games, and load previous saved games.

To launch the default Saved Games UI:

1. Call [`SnapshotsClient.getSelectSnapshotIntent()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#getSelectSnapshotIntent(java.lang.String,%20boolean,%20boolean,%20int)) to get an [`Intent`](https://developer.android.com/reference/android/content/Intent) for launching the default saved games selection UI.
2. Call [`startActivityForResult()`](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent,%20int)) and pass in that [`Intent`](https://developer.android.com/reference/android/content/Intent). If the call is successful, the game displays the saved game selection UI, along with the options you specified.

Here's an example of how to launch the default saved games selection UI:

```
private static final int RC_SAVED_GAMES = 9009;

private void showSavedGamesUI() {
  SnapshotsClient snapshotsClient =
      PlayGames.getSnapshotsClient(this);
  int maxNumberOfSavedGamesToShow = 5;

  Task<Intent> intentTask = snapshotsClient.getSelectSnapshotIntent(
      "See My Saves", true, true, maxNumberOfSavedGamesToShow);

  intentTask.addOnSuccessListener(new OnSuccessListener<Intent>() {
    @Override
    public void onSuccess(Intent intent) {
      startActivityForResult(intent, RC_SAVED_GAMES);
    }
  });
}
```

If the player selects to create a new saved game or load an existing saved game,
the UI sends a request to Play Games Services. If the request is successful,
Play Games Services returns information to create or restore the saved game
through the
[`onActivityResult()`](https://developer.android.com/reference/android/app/Activity#onActivityResult(int,%0Aint,%20android.content.Intent)) callback. Your game can override this callback to
check if any errors occurred during request.

The following code snippet shows a sample implementation of
[`onActivityResult()`](https://developer.android.com/reference/android/app/Activity#onActivityResult(int,%20int,%20android.content.Intent)):

```
private String mCurrentSaveName = "snapshotTemp";

/**
 * This callback will be triggered after you call startActivityForResult from the
 * showSavedGamesUI method.
 */
@Override
protected void onActivityResult(int requestCode, int resultCode,
                                Intent intent) {
  if (intent != null) {
    if (intent.hasExtra(SnapshotsClient.EXTRA_SNAPSHOT_METADATA)) {
      // Load a snapshot.
      SnapshotMetadata snapshotMetadata =
          intent.getParcelableExtra(SnapshotsClient.EXTRA_SNAPSHOT_METADATA);
      mCurrentSaveName = snapshotMetadata.getUniqueName();

      // Load the game data from the Snapshot
      // ...
    } else if (intent.hasExtra(SnapshotsClient.EXTRA_SNAPSHOT_NEW)) {
      // Create a new snapshot named with a unique string
      String unique = new BigInteger(281, new Random()).toString(13);
      mCurrentSaveName = "snapshotTemp-" + unique;

      // Create the new snapshot
      // ...
    }
  }
}
```

## Write saved games

To store content to a saved game:

1. Asynchronously open a snapshot using
   [`SnapshotsClient.open()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#open(com.google.android.gms.games.snapshot.SnapshotMetadata)).

2. Retrieve the
   [`Snapshot`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/Snapshot)
   object from the task's result by calling
   [`SnapshotsClient.DataOrConflict.getData()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#getData()).

3. Retrieve a [`SnapshotContents`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotContents)
   instance with
   [`SnapshotsClient.SnapshotConflict`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/Snapshot#getSnapshotContents()).

4. Call
   [`SnapshotContents.writeBytes()`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotContents#writeBytes(byte%5B%5D))
   to store the player's data in byte format.

5. Once all your changes are written, call
   [`SnapshotsClient.commitAndClose()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#public-methods) to send your
   changes to Google's servers. In the method call, your game can optionally
   provide additional information to tell Play Games Services how to present
   this saved game to players. This information is represented in a
   [`SnapshotMetaDataChange`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotMetadataChange)
   object, which your game creates using
   [`SnapshotMetadataChange.Builder`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotMetadataChange.Builder).

The following snippet shows how your game might commit changes to a saved game:

```
private Task<SnapshotMetadata> writeSnapshot(Snapshot snapshot,
                                             byte[] data, Bitmap coverImage, String desc) {

  // Set the data payload for the snapshot
  snapshot.getSnapshotContents().writeBytes(data);

  // Create the change operation
  SnapshotMetadataChange metadataChange = new SnapshotMetadataChange.Builder()
      .setCoverImage(coverImage)
      .setDescription(desc)
      .build();

  SnapshotsClient snapshotsClient =
      PlayGames.getSnapshotsClient(this);

  // Commit the operation
  return snapshotsClient.commitAndClose(snapshot, metadataChange);
}
```

If the player's device is not connected to a network when your app calls
[`SnapshotsClient.commitAndClose()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#commitAndClose(com.google.android.gms.games.snapshot.Snapshot,%20com.google.android.gms.games.snapshot.SnapshotMetadataChange)),
Play Games Services stores the saved game data locally on the device. Upon device
re-connection, Play Games Services syncs the locally cached saved game changes to
Google's servers.

## Load saved games

To retrieve saved games for the authenticated player:

1. Asynchronously open a snapshot with
   [`SnapshotsClient.open()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#open(com.google.android.gms.games.snapshot.SnapshotMetadata,%20int)).

2. Retrieve the [`Snapshot`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/Snapshot)
   object from the task's result by calling
   [`SnapshotsClient.DataOrConflict.getData()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#getData()).
   Alternatively, your game can also retrieve a specific snapshot through the
   saved games selection UI, as described in [Display saved
   games](https://developer.android.com/games/pgs/android/saved-games#display-saved-games).

3. Retrieve the [`SnapshotContents`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotContents)
   instance with
   [`SnapshotsClient.SnapshotConflict`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/Snapshot#getSnapshotContents()).

4. Call
   [`SnapshotContents.readFully()`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotContents#readFully())
   to read the contents of the snapshot.

The following snippet shows how you might load a specific saved game:

```
Task<byte[]> loadSnapshot() {
  // Display a progress dialog
  // ...

  // Get the SnapshotsClient from the signed in account.
  SnapshotsClient snapshotsClient =
      PlayGames.getSnapshotsClient(this);

  // In the case of a conflict, the most recently modified version of this snapshot will be used.
  int conflictResolutionPolicy = SnapshotsClient.RESOLUTION_POLICY_MOST_RECENTLY_MODIFIED;

  // Open the saved game using its name.
  return snapshotsClient.open(mCurrentSaveName, true, conflictResolutionPolicy)
      .addOnFailureListener(new OnFailureListener() {
        @Override
        public void onFailure(@NonNull Exception e) {
          Log.e(TAG, "Error while opening Snapshot.", e);
        }
      }).continueWith(new Continuation<SnapshotsClient.DataOrConflict<Snapshot>, byte[]>() {
        @Override
        public byte[] then(@NonNull Task<SnapshotsClient.DataOrConflict<Snapshot>> task) throws Exception {
          Snapshot snapshot = task.getResult().getData();

          // Opening the snapshot was a success and any conflicts have been resolved.
          try {
            // Extract the raw data from the snapshot.
            return snapshot.getSnapshotContents().readFully();
          } catch (IOException e) {
            Log.e(TAG, "Error while reading Snapshot.", e);
          }

          return null;
        }
      }).addOnCompleteListener(new OnCompleteListener<byte[]>() {
        @Override
        public void onComplete(@NonNull Task<byte[]> task) {
          // Dismiss progress dialog and reflect the changes in the UI when complete.
          // ...
        }
      });
}
```

## Handle saved game conflicts

When using the snapshots API in your game, it is possible for multiple devices
to perform reads and writes on the same saved game. In the event that a device
temporarily loses its network connection and later reconnects, this might cause
data conflicts whereby the saved game stored on a player's local device is
out-of-sync with the remote version stored in Google's servers.

The snapshots API provides a conflict resolution mechanism that presents both
sets of conflicting saved games at read-time and lets you implement a resolution
strategy that is appropriate for your game.

When Play Games Services detects a data conflict, the
[`SnapshotsClient.DataOrConflict.isConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#isConflict())
method returns a value of `true` In this event, the
[`SnapshotsClient.SnapshotConflict`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict)
class provides two versions of the saved game:

- **Server version**: The most-up-to-date version known by Play Games Services
  to be accurate for the player's device.

- **Local version**: A modified version detected on one of the player's
  devices that contains conflicting content or metadata. This may not be the
  same as the version that you tried to save.

Your game must decide how to resolve the conflict by picking one of the provided
versions or merging the data of the two saved game versions.

To detect and resolve saved game conflicts:

1. Call
   [`SnapshotsClient.open()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#open(com.google.android.gms.games.snapshot.SnapshotMetadata,%20int)).
   The task result contains a `SnapshotsClient.DataOrConflict` class.

2. Call the
   [`SnapshotsClient.DataOrConflict.isConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#isConflict())
   method. If the result is true, you have a conflict to resolve.

3. Call
   [`SnapshotsClient.DataOrConflict.getConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#getConflict())
   to retrieve a
   [`SnapshotsClient.snapshotConflict`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict) instance.

4. Call
   [`SnapshotsClient.SnapshotConflict.getConflictId()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict#getConflictId())
   to retrieve the conflict ID that uniquely identifies the detected conflict.
   Your game needs this value to send a conflict resolution request later.

5. Call
   [`SnapshotsClient.SnapshotConflict.getConflictingSnapshot()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict#getConflictingSnapshot())
   to get the local version.

6. Call
   [`SnapshotsClient.SnapshotConflict.getSnapshot()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict#getSnapshot())
   to get the server version.

7. To resolve the saved game conflict, select a version that you want to save
   to the server as the final version, and pass it to the
   [`SnapshotsClient.resolveConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#resolveConflict(java.lang.String,%20java.lang.String,%20com.google.android.gms.games.snapshot.SnapshotMetadataChange,%20com.google.android.gms.games.snapshot.SnapshotContents))
   method.

The following snippet shows and example of how your game might handle a saved
game conflict by selecting the most recently modified saved game as the final
version to save:

```
private static final int MAX_SNAPSHOT_RESOLVE_RETRIES = 10;

Task<Snapshot> processSnapshotOpenResult(SnapshotsClient.DataOrConflict<Snapshot> result,
                                         final int retryCount) {

  if (!result.isConflict()) {
    // There was no conflict, so return the result of the source.
    TaskCompletionSource<Snapshot> source = new TaskCompletionSource<>();
    source.setResult(result.getData());
    return source.getTask();
  }

  // There was a conflict.  Try resolving it by selecting the newest of the conflicting snapshots.
  // This is the same as using RESOLUTION_POLICY_MOST_RECENTLY_MODIFIED as a conflict resolution
  // policy, but we are implementing it as an example of a manual resolution.
  // One option is to present a UI to the user to choose which snapshot to resolve.
  SnapshotsClient.SnapshotConflict conflict = result.getConflict();

  Snapshot snapshot = conflict.getSnapshot();
  Snapshot conflictSnapshot = conflict.getConflictingSnapshot();

  // Resolve between conflicts by selecting the newest of the conflicting snapshots.
  Snapshot resolvedSnapshot = snapshot;

  if (snapshot.getMetadata().getLastModifiedTimestamp() <
      conflictSnapshot.getMetadata().getLastModifiedTimestamp()) {
    resolvedSnapshot = conflictSnapshot;
  }

  return PlayGames.getSnapshotsClient(theActivity)
      .resolveConflict(conflict.getConflictId(), resolvedSnapshot)
      .continueWithTask(
          new Continuation<
              SnapshotsClient.DataOrConflict<Snapshot>,
              Task<Snapshot>>() {
            @Override
            public Task<Snapshot> then(
                @NonNull Task<SnapshotsClient.DataOrConflict<Snapshot>> task)
                throws Exception {
              // Resolving the conflict may cause another conflict,
              // so recurse and try another resolution.
              if (retryCount < MAX_SNAPSHOT_RESOLVE_RETRIES) {
                return processSnapshotOpenResult(task.getResult(), retryCount + 1);
              } else {
                throw new Exception("Could not resolve snapshot conflicts");
              }
            }
          });
}
```

### Modify saved games

If you want to merge data from multiple saved games or modify an existing
`Snapshot` to save to the server as the resolved final version, follow these
steps:

1. Call
   [`SnapshotsClient.open()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#open(com.google.android.gms.games.snapshot.SnapshotMetadata,%20int)).

2. Call
   [`SnapshotsClient.SnapshotConflict.getResolutionSnapshotsContent()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict#getResolutionSnapshotContents())
   to get a new
   [`SnapshotContents`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotContents) object.

3. Merge the data from
   [`SnapshotsClient.SnapshotConflict.getConflictingSnapshot()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict#getConflictingSnapshot())
   and
   [`SnapshotsClient.SnapshotConflict.getSnapshot()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict#getSnapshot())
   into the
   [`SnapshotContents`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotContents) object from the previous step.

4. Optionally, create a [`SnapshotMetadataChange`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotMetadataChange) instance if there
   are any changes to the metadata fields.

5. Call
   [`SnapshotsClient.resolveConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#resolveConflict(java.lang.String,%20java.lang.String,%20com.google.android.gms.games.snapshot.SnapshotMetadataChange,%20com.google.android.gms.games.snapshot.SnapshotContents)).
   In your method call, pass
   [`SnapshotsClient.SnapshotConflict.getConflictId()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.SnapshotConflict#getConflictId())
   as the first argument, and the
   [`SnapshotMetadataChange`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotMetadataChange)
   and
   [`SnapshotContents`](https://developers.google.com/android/reference/com/google/android/gms/games/snapshot/SnapshotContents)
   objects that you modified earlier as the second and third arguments
   respectively.

6. If the
   [`SnapshotsClient.resolveConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient#resolveConflict(java.lang.String,%20java.lang.String,%20com.google.android.gms.games.snapshot.SnapshotMetadataChange,%20com.google.android.gms.games.snapshot.SnapshotContents))
   call is successful, the API stores the `Snapshot` object to the server and
   attempts to open the Snapshot object on your local device.

   - If there is a conflict, [`SnapshotsClient.DataOrConflict.isConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#isConflict()) returns `true`. In this case, your game should return to step 2 and repeat the steps to modify the snapshot until conflicts are resolved.
   - If there's no conflict, [`SnapshotsClient.DataOrConflict.isConflict()`](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.DataOrConflict#isConflict()) returns `false` and the `Snapshot` object is open for your game to modify.