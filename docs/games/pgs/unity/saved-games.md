---
title: https://developer.android.com/games/pgs/unity/saved-games
url: https://developer.android.com/games/pgs/unity/saved-games
source: md.txt
---

This topics describes how to use saved games for Play Games Services in Unity
games.

## Before you start

- Set up your project and the Google Play Games plugin for Unity. For details,
  see the [Get started guide](https://developer.android.com/games/pgs/unity/unity-start).

- Enabled saved games. See the
  [saved games](https://developer.android.com/games/pgs/console/enable-features#enable_saved_games) for
  details.

## Display the saved games UI

The standard UI for selecting or creating a saved game entry is displayed by
calling:

        void ShowSelectUI() {
            uint maxNumToDisplay = 5;
            bool allowCreateNew = false;
            bool allowDelete = true;

            ISavedGameClient savedGameClient = PlayGamesPlatform.Instance.SavedGame;
            savedGameClient.ShowSelectSavedGameUI("Select saved game",
                maxNumToDisplay,
                allowCreateNew,
                allowDelete,
                OnSavedGameSelected);
        }

        public void OnSavedGameSelected (SelectUIStatus status, ISavedGameMetadata game) {
            if (status == SelectUIStatus.SavedGameSelected) {
                // handle selected game save
            } else {
                // handle cancel or error
            }
        }

## Open a saved game

In order to read or write data to a saved game, the saved game needs to be
opened. Since the saved game state is cached locally on the device and saved to
the cloud, it is possible to encounter conflicts in the state of the saved data.
A conflict happens when a device attempts to save state to the cloud but the
data currently on the cloud was written by a different device. These conflicts
need to be resolved when opening the saved game data.

There are 2 open methods that handle conflict resolution, the first
**OpenWithAutomaticConflictResolution** accepts a standard resolution strategy
type and automatically resolves the conflicts. The other method,
**OpenWithManualConflictResolution** accepts a callback method to allow the
manual resolution of the conflict.

See [ISavedGameClient](https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/saved-game/i-saved-game-client) for more details
on these methods.

        void OpenSavedGame(string filename) {
            ISavedGameClient savedGameClient = PlayGamesPlatform.Instance.SavedGame;
            savedGameClient.OpenWithAutomaticConflictResolution(filename, DataSource.ReadCacheOrNetwork,
                ConflictResolutionStrategy.UseLongestPlaytime, OnSavedGameOpened);
        }

        public void OnSavedGameOpened(SavedGameRequestStatus status, ISavedGameMetadata game) {
            if (status == SavedGameRequestStatus.Success) {
                // handle reading or writing of saved game.
            } else {
                // handle error
            }
        }

## Write a saved game

Once the saved game file is opened, it can be written to save the game state.
This is done by calling **CommitUpdate**. There are four parameters to
CommitUpdate:

1. the saved game metadata passed to the callback passed to one of the Open calls.
2. the updates to make to the metadata.
3. the actual byte array of data
4. a callback to call when the commit is complete.

        void SaveGame (ISavedGameMetadata game, byte[] savedData, TimeSpan totalPlaytime) {
            ISavedGameClient savedGameClient = PlayGamesPlatform.Instance.SavedGame;

            SavedGameMetadataUpdate.Builder builder = new SavedGameMetadataUpdate.Builder();
            builder = builder
                .WithUpdatedPlayedTime(totalPlaytime)
                .WithUpdatedDescription("Saved game at " + DateTime.Now());
            if (savedImage != null) {
                // This assumes that savedImage is an instance of Texture2D
                // and that you have already called a function equivalent to
                // getScreenshot() to set savedImage
                // NOTE: see sample definition of getScreenshot() method below
                byte[] pngData = savedImage.EncodeToPNG();
                builder = builder.WithUpdatedPngCoverImage(pngData);
            }
            SavedGameMetadataUpdate updatedMetadata = builder.Build();
            savedGameClient.CommitUpdate(game, updatedMetadata, savedData, OnSavedGameWritten);
        }

        public void OnSavedGameWritten (SavedGameRequestStatus status, ISavedGameMetadata game) {
            if (status == SavedGameRequestStatus.Success) {
                // handle reading or writing of saved game.
            } else {
                // handle error
            }
        }

        public Texture2D getScreenshot() {
            // Create a 2D texture that is 1024x700 pixels from which the PNG will be
            // extracted
            Texture2D screenShot = new Texture2D(1024, 700);

            // Takes the screenshot from top left hand corner of screen and maps to top
            // left hand corner of screenShot texture
            screenShot.ReadPixels(
                new Rect(0, 0, Screen.width, (Screen.width/1024)*700), 0, 0);
            return screenShot;
        }

## Read a saved game

Once the saved game file is opened, it can be read to load the game state. This
is done by calling **ReadBinaryData**.

        void LoadGameData (ISavedGameMetadata game) {
            ISavedGameClient savedGameClient = PlayGamesPlatform.Instance.SavedGame;
            savedGameClient.ReadBinaryData(game, OnSavedGameDataRead);
        }

        public void OnSavedGameDataRead (SavedGameRequestStatus status, byte[] data) {
            if (status == SavedGameRequestStatus.Success) {
                // handle processing the byte array data
            } else {
                // handle error
            }
        }

## Delete a saved game

Once the saved game file is opened, it can be deleted. This is done by calling
**Delete**.

        void DeleteGameData (string filename) {
            // Open the file to get the metadata.
            ISavedGameClient savedGameClient = PlayGamesPlatform.Instance.SavedGame;
            savedGameClient.OpenWithAutomaticConflictResolution(filename, DataSource.ReadCacheOrNetwork,
                ConflictResolutionStrategy.UseLongestPlaytime, DeleteSavedGame);
        }

        public void DeleteSavedGame(SavedGameRequestStatus status, ISavedGameMetadata game) {
            if (status == SavedGameRequestStatus.Success) {
                ISavedGameClient savedGameClient = PlayGamesPlatform.Instance.SavedGame;
                savedGameClient.Delete(game);
            } else {
                // handle error
            }
        }