---
title: https://developer.android.com/training/cars/media/create-media-browser/browsable-search
url: https://developer.android.com/training/cars/media/create-media-browser/browsable-search
source: md.txt
---

# Display browsable search results

All apps must support voice searches. This page describes how to further enhance the search experience by supporting the initiation of searches without voice and by showing a list of search results so that users can pick another result. For example, if the suggested result isn't the most relevant.

Your media app can provide contextual search results in Android Auto and Android Automotive OS (AAOS). These results appear when a user initiates a search query or views the results of the most recent search.

To enable and provide these search results:

- Declare search support in your service's`onGetRoot`method.

- Override the`onSearch`method in your media browser service to handle user search terms.

- Organize Search results using title items for improved browsability.

Your app can provide contextual search results that appear when a search query is started. Android Auto and AAOS show these results through search query interfaces or through affordances that pivot on queries made earlier. To learn more, see the[Support voice actions](https://developer.android.com/training/cars/media/voice-actions#support_voice).

![Playback view with a **Search results** option to view media items related to the user's voice search](https://developer.android.com/static/images/training/cars/search_results.png)

**Figure 1.** Playback view with a**Search results**option to view media items related to the user's voice search.

To indicate that your app supports the display of search results, include the constant key[`BROWSER_SERVICE_EXTRAS_KEY_SEARCH_SUPPORTED`](https://developer.android.com/reference/androidx/media/utils/MediaConstants#BROWSER_SERVICE_EXTRAS_KEY_SEARCH_SUPPORTED())in the extras bundle returned by your service's[`onGetRoot`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onGetRoot(java.lang.String,%20int,%20android.os.Bundle))method, mapping to the Boolean`true`.  

### Kotlin

    import androidx.media.utils.MediaConstants

    @Nullable
    override fun onGetRoot(
        @NonNull clientPackageName: String,
        clientUid: Int,
        @Nullable rootHints: Bundle
    ): BrowserRoot {
        val extras = Bundle()
        extras.putBoolean(
            MediaConstants.BROWSER_SERVICE_EXTRAS_KEY_SEARCH_SUPPORTED, true)
        return BrowserRoot(ROOT_ID, extras)
    }

### Java

    import androidx.media.utils.MediaConstants;

    @Nullable
    @Override
    public BrowserRoot onGetRoot(
        @NonNull String clientPackageName,
        int clientUid,
        @Nullable Bundle rootHints) {
        Bundle extras = new Bundle();
        extras.putBoolean(
            MediaConstants.BROWSER_SERVICE_EXTRAS_KEY_SEARCH_SUPPORTED, true);
        return new BrowserRoot(ROOT_ID, extras);
    }

To provide search results, override the[`onSearch`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onSearch(java.lang.String,android.os.Bundle,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E))method in your media browser service. Android Auto and AAOS forward the user's search terms to this method when a user invokes a search query interface or**Search results**affordance.

To make search results more browsable, you can use[title items](https://developer.android.com/training/cars/media/create-media-browser/content-styles#group-items). For example, if your app plays music, you can organize search results by album, artist, and song. This code snippet shows an implementation of the`onSearch`method:  

### Kotlin

    fun onSearch(query: String, extras: Bundle) {
      // Detach from results to unblock the caller (if a search is expensive).
      result.detach()
      object:AsyncTask() {
        internal var searchResponse:ArrayList
        internal var succeeded = false
        protected fun doInBackground(vararg params:Void):Void {
          searchResponse = ArrayList()
          if (doSearch(query, extras, searchResponse))
          {
            succeeded = true
          }
          return null
        }
        protected fun onPostExecute(param:Void) {
          if (succeeded)
          {
            // Sending an empty List informs the caller that there were no results.
            result.sendResult(searchResponse)
          }
          else
          {
            // This invokes onError() on the search callback.
            result.sendResult(null)
          }
          return null
        }
      }.execute()
    }
    // Populates resultsToFill with search results. Returns true on success or false on error.
    private fun doSearch(
        query: String,
        extras: Bundle,
        resultsToFill: ArrayList
    ): Boolean {
      // Implement this method.
    }

### Java

    @Override
    public void onSearch(final String query, final Bundle extras,
                            Result&lt;List&lt;MediaItem>> result) {

      // Detach from results to unblock the caller (if a search is expensive).
      result.detach();

      new AsyncTask<Void, Void, Void>() {
        List>MediaItem> searchResponse;
        boolean succeeded = false;
        @Override
        protected Void doInBackground(Void... params) {
          searchResponse = new ArrayList&lt;MediaItem>();
          if (doSearch(query, extras, searchResponse)) {
            succeeded = true;
          }
          return null;
        }

        @Override
        protected void onPostExecute(Void param) {
          if (succeeded) {
           // Sending an empty List informs the caller that there were no results.
           result.sendResult(searchResponse);
          } else {
            // This invokes onError() on the search callback.
            result.sendResult(null);
          }
        }
      }.execute()
    }

    /** Populates resultsToFill with search results. Returns true on success or false on error. */
    private boolean doSearch(String query, Bundle extras, ArrayList&lt;MediaItem> resultsToFill) {
        // Implement this method.
    }