---
title: https://developer.android.com/training/cars/media/create-media-browser/custom-browse-actions
url: https://developer.android.com/training/cars/media/create-media-browser/custom-browse-actions
source: md.txt
---

# Implement custom browse actions

Similar to how you use[custom playback actions](https://developer.android.com/training/cars/media/enable-playback#custom-icons)to support unique capabilities in the playback view, you can use custom browse actions to support unique capabilities in browsing views. For example, you can use custom browse actions so that users can download playlists or add an item to a queue.

When more custom actions exist than displayed by the Original Equipment Manufacturer (OEM), an overflow menu is displayed to the user. Each custom browse action is defined with an:

- **Action ID:**Unique string identifier
- **Action label:**Text displayed to the user
- **Action icon uniform resource identifier (URI):**Vector drawable that can be tintable

![Custom browse action overflow](https://developer.android.com/static/images/training/cars/custom_browse_action_overflow.png)

**Figure 1.**Custom browse action overflow.

You define a list of custom browse actions globally as part of your`BrowseRoot`. Then attach a subset of these actions to individual`MediaItem`.

When a user interacts with a custom browse action, your app receives a callback in`onCustomAction`. You then handle the action and update the list of actions for the`MediaItem`, if necessary. This is useful for stateful actions like Favorite and Download. For actions that need no updating, such as Play Radio, you needn't update the list of actions.

![Custom browse action toolbar](https://developer.android.com/static/images/training/cars/custom_browse_action_toolbar.png)

**Figure 2.**Custom browse action toolbar.

You can also attach custom browse actions to a browse node root. These actions are displayed in a secondary toolbar under the primary toolbar.

To add custom browse actions to your app:

1. Override two methods in your[`MediaBrowserServiceCompat`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat)implementation:

   - [`onLoadItem(String itemId, @NonNull Result<MediaBrowserCompat.MediaItem> result)`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onLoadItem(java.lang.String,androidx.media.MediaBrowserServiceCompat.Result%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E))
   - [`onCustomAction(@NonNull String action, Bundle extras, @NonNull Result<Bundle> result)`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onCustomAction(java.lang.String,android.os.Bundle,androidx.media.MediaBrowserServiceCompat.Result%3Candroid.os.Bundle%3E))
2. Parse the action limits at runtime:

   In`onGetRoot`, get the maximum number of actions allowed for each`MediaItem`using the key[`BROWSER_ROOT_HINTS_KEY_CUSTOM_BROWSER_ACTION_LIMIT`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_ROOT_HINTS_KEY_CUSTOM_BROWSER_ACTION_LIMIT())in the`rootHints``Bundle`. A limit of 0 indicates that the feature is not supported by the system.
3. Build the global list of custom browse actions. For each action, create a`Bundle`object with these keys:

   - Action ID`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ID`
   - Action label`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_LABEL`
   - Action icon URI`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ICON_URI`
4. Add all the action`Bundle`objects to a list.

5. Add the global list to your`BrowseRoot`. In the`BrowseRoot`extras`Bundle`, add the list of actions as a`Parcelable``ArrayList`using the key[`BROWSER_SERVICE_EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ROOT_LIST`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_SERVICE_EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ROOT_LIST()).

6. Add actions to your`MediaItem`objects. You can add actions to individual`MediaItem`objects by including the list of action IDs in the`MediaDescriptionCompat`extras using the key[`DESCRIPTION_EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ID_LIST`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#DESCRIPTION_EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ID_LIST()). This list must be a subset of the global list of actions you defined in the`BrowseRoot`.

7. Handle actions and return progress or results:

   - In`onCustomAction`, handle the action based on the action ID and any other data you need. You can get the ID of the`MediaItem`that triggered the action from the extras using the key[`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_MEDIA_ITEM_ID`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#EXTRAS_KEY_CUSTOM_BROWSER_ACTION_MEDIA_ITEM_ID()).

   - You can update the list of actions for a`MediaItem`by including the key[`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM())in the progress or result bundle.

### Update the action state

To override these methods in`MediaBrowserServiceCompat`:  

    public void onLoadItem(String itemId, @NonNull Result<MediaBrowserCompat.MediaItem> result)

and  

    public void onCustomAction(@NonNull String action, Bundle extras, @NonNull Result<Bundle> result)

## Parse actions limit

Check how many custom browse actions are supported:  

    public BrowserRoot onGetRoot(@NonNull String clientPackageName, int clientUid, Bundle rootHints) {
        rootHints.getInt(
                MediaConstants.BROWSER_ROOT_HINTS_KEY_CUSTOM_BROWSER_ACTION_LIMIT, 0)
    }

| **Note:** An action limit of`0`or less indicates the feature is not supported.

## Build a custom browse action

Each action needs to be packed into a separate`Bundle`.

- Action ID:

      bundle.putString(MediaConstants.EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ID,
                      "<ACTION_ID>")

- Action label:

      bundle.putString(MediaConstants.EXTRAS_KEY_CUSTOM_BROWSER_ACTION_LABEL,
                      "<ACTION_LABEL>")

- Action icon URI:

      bundle.putString(MediaConstants.EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ICON_URI,
                      "<ACTION_ICON_URI>")

## Add custom browse actions to Parcelable ArrayList

Add all custom browse action`Bundle`objects into an`ArrayList`:  

    private ArrayList<Bundle> createCustomActionsList(
                                            CustomBrowseAction browseActions) {
        ArrayList<Bundle> browseActionsBundle = new ArrayList<>();
        for (CustomBrowseAction browseAction : browseActions) {
            Bundle action = new Bundle();
            action.putString(EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ID,
                    browseAction.mId);
            action.putString(EXTRAS_KEY_CUSTOM_BROWSER_ACTION_LABEL,
                    getString(browseAction.mLabelResId));
            action.putString(EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ICON_URI,
                    browseAction.mIcon);
            browseActionsBundle.add(action);
        }
        return browseActionsBundle;
    }

## Add custom browse action list to browse root

    public BrowserRoot onGetRoot(@NonNull String clientPackageName, int clientUid,
                                 Bundle rootHints) {
        Bundle browserRootExtras = new Bundle();
        browserRootExtras.putParcelableArrayList(
                BROWSER_SERVICE_EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ROOT_LIST,
                createCustomActionsList()));
        mRoot = new BrowserRoot(ROOT_ID, browserRootExtras);
        return mRoot;
    }

## Add actions to a MediaItem

Browse Actions IDs in a`MediaItem`need to be a subset of the global list of Browse Actions given on`onGetRoot`. Actions not in the global list are ignored.  

    MediaDescriptionCompat buildDescription (long id, String title, String subtitle,
                    String description, Uri iconUri, Uri mediaUri,
                    ArrayList<String> browseActionIds) {

        MediaDescriptionCompat.Builder bob = new MediaDescriptionCompat.Builder();
        bob.setMediaId(id);
        bob.setTitle(title);
        bob.setSubtitle(subtitle);
        bob.setDescription(description);
        bob.setIconUri(iconUri);
        bob.setMediaUri(mediaUri);

        Bundle extras = new Bundle();
        extras.putStringArrayList(
              DESCRIPTION_EXTRAS_KEY_CUSTOM_BROWSER_ACTION_ID_LIST,
              browseActionIds);

        bob.setExtras(extras);
        return bob.build();
    }
    MediaItem mediaItem = new MediaItem(buildDescription(...), flags);

| **Note:** Put only`String`action IDs in the`MediaItem`. The ID is mapped from the global list passed to the`BrowseRoot`.

## Build onCustomAction result

To build the result:

1. Parse`mediaId`from`Bundle extras`

       @Override
       public void onCustomAction(
                   @NonNull String action, Bundle extras, @NonNull Result<Bundle> result){
           String mediaId = extras.getString(MediaConstans.EXTRAS_KEY_CUSTOM_BROWSER_ACTION_MEDIA_ITEM_ID);
                   }

2. For asynchronous results, detach the result,`result.detach`.

3. Build the result bundle:

   1. Display a message to the user:

          mResultBundle.putString(EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_MESSAGE,
                        mContext.getString(stringRes))

   2. Update the item (use to update actions in an item):

          mResultBundle.putString(EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM, mediaId);

   3. Open the playback view:

          //Shows user the PBV without changing the playback state
          mResultBundle.putString(EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_SHOW_PLAYING_ITEM, null);

   4. Update the browse node:

          //Change current browse node to mediaId
          mResultBundle.putString(EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_BROWSE_NODE, mediaId);

4. Check the result:

   - **Error:** Call`result.sendError(resultBundle)`
   - **Progress update:** Call`result.sendProgressUpdate(resultBundle)`
   - **Finish:** Call`result.sendResult(resultBundle)`

## Update the action state

By using the`result.sendProgressUpdate(resultBundle)`method with the[`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM())key, you can update the`MediaItem`to reflect the new state of the action. This lets you provide real-time feedback to the user about the progress and result of their action.

## Sample download action

This example describes how you can use this feature to implement a download action with three states:

- **Download** is the initial state of the action. When the user selects this action, you can swap it with Downloading and call`sendProgressUpdate`to update the user interface (UI).

- **Downloading**state indicates that the download is in progress. You can use this state to show a progress bar or another indicator to the user.

- **Downloaded** state indicates that the download is complete. When the download finishes, you can swap Downloading with Downloaded and call`sendResult`with the[`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM())key to indicate that the item should be refreshed. Additionally, you can use the[`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_MESSAGE`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM())key to display a success message to the user.

This approach lets you provide clear feedback to the user about the download process and its current state. You can add more detail with icons to show 25%, 50%, and 75% download states.

## Sample favorite action

Another example is a favorite action with two states:

- **Favorite** is displayed for items not in the user's favorites list. When the user selects this action, swap it with**Favorited** and call`sendResult`with the[`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM())key to update the UI.

- **Favorited** is displayed for items in the user's favorites list. When the user selects this action, swap it with**Favorite** and call`sendResult`with the[`EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#EXTRAS_KEY_CUSTOM_BROWSER_ACTION_RESULT_REFRESH_ITEM())key to update the UI.

This approach provides a clear and consistent way for users to manage their favorite items. These examples showcase the flexibility of custom browse actions and how you can use them to implement a variety of functionalities with real-time feedback for an enhanced user experience in the car's Media app.

You can see a comprehensive sample implementation of this feature in the[`TestMediaApp`](https://android.googlesource.com/platform/packages/apps/Car/tests/+/refs/heads/mirror-car-apps-aosp-release/TestMediaApp/)project.