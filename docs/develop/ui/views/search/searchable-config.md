---
title: https://developer.android.com/develop/ui/views/search/searchable-config
url: https://developer.android.com/develop/ui/views/search/searchable-config
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to add search functionality in Compose. [Search bar →](https://developer.android.com/develop/ui/compose/components/search-bar) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

To implement search with assistance from the Android system---that is, to deliver search
queries to an activity and provide search suggestions---your application must provide a search
configuration in the form of an XML file.

This page describes the search configuration file in terms of its syntax and usage. For more
information about how to implement search features for your application, see
[Create a search interface](https://developer.android.com/develop/ui/views/search/search-dialog).

file location:
:   `res/xml/filename.xml`  

    Android uses the filename as the resource ID.

syntax:
:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <searchable xmlns:android="http://schemas.android.com/apk/res/android"
        android:label="string resource"
        android:hint="string resource"
        android:searchMode=["queryRewriteFromData" | "queryRewriteFromText"]
        android:searchButtonText="string resource"
        android:inputType="`https://developer.android.com/reference/android/R.attr#inputType`"
        android:imeOptions="`https://developer.android.com/reference/android/R.attr#imeOptions`"
        android:searchSuggestAuthority="string"
        android:searchSuggestPath="string"
        android:searchSuggestSelection="string"
        android:searchSuggestIntentAction="string"
        android:searchSuggestIntentData="string"
        android:searchSuggestThreshold="int"
        android:includeInGlobalSearch=["true" | "false"]
        android:searchSettingsDescription="string resource"
        android:queryAfterZeroResults=["true" | "false"]
        android:voiceSearchMode=["showVoiceSearchButton" | "launchWebSearch" | "launchRecognizer"]
        android:voiceLanguageModel=["free-form" | "web_search"]
        android:voicePromptText="string resource"
        android:voiceLanguage="string"
        android:voiceMaxResults="int"
        >
        <actionkey
            android:keycode="`https://developer.android.com/reference/android/view/KeyEvent`"
            android:queryActionMsg="string"
            android:suggestActionMsg="string"
            android:suggestActionMsgColumn="string" />
    </searchable>
    ```

elements:
:

    `<searchable>`

    :   Defines all search configurations used by the Android system to provide assisted search. **Attributes:**

        `android:label`
        :   *String resource* . (Required.) The name of your application. It must be the same as
            the name applied to the `android:label` attribute of your
            [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element#label)
            or
            [`<application>`](https://developer.android.com/guide/topics/manifest/application-element#label)
            manifest element. This label is only visible to the user when you set
            `android:includeInGlobalSearch` to `"true"`, in which case, this label is used
            to identify your application as a searchable item in the system's search settings.

        `android:hint`
        :   *String resource* . (Recommended.) The text to display in the search text field when
            no text is entered. It provides a hint to the user about what content is searchable. For consistency
            with other Android applications, format the string for `android:hint` as "Search
            *\<content-or-product\>*". For example, "Search songs and artists" or
            "Search YouTube".

        `android:searchMode`
        :   *Keyword* . Sets additional modes that control the search presentation. Available
            modes define how the query text needs to be rewritten when a custom suggestion receives
            focus. The following mode values are accepted:

            | Value | Description |
            |---|---|
            | `"queryRewriteFromData"` | Use the value from the `https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_DATA` column to rewrite thebquery text. This must only be used when the values in `SUGGEST_COLUMN_INTENT_DATA` are suitable for user inspection and editing, such as HTTP URIs. |
            | `"queryRewriteFromText"` | Use the value from the `https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_TEXT_1` column to rewrite the query text. |


            For more information, see the documentation about rewriting the query text in
            [Add custom search suggestions](https://developer.android.com/develop/ui/views/search/adding-custom-suggestions#RewritingQueryText).

        `android:searchButtonText`
        :   *String resource*. The text to display in the button that executes search. By
            default, the button shows a search icon (a magnifying glass), which is ideal for
            internationalization. So don't use this attribute to change the button unless the behavior is
            something other than a search, such as a URL request in a web browser.

        `android:inputType`
        :   *Keyword* . Defines the type of input method to use, such as the type of soft
            keyboard. For most searches, in which free-form text is expected, you don't need this attribute.
            See `https://developer.android.com/reference/android/R.attr#inputType` for a list of
            suitable values for this attribute.

        `android:imeOptions`
        :   *Keyword* . Supplies additional options for the input method. For most searches, in
            which free-form text is expected, you don't need this attribute. The default IME is
            `actionSearch`, which provides the "search" button instead of a carriage return in the
            soft keyboard. See `https://developer.android.com/reference/android/R.attr#imeOptions`
            for a list of suitable values for this attribute.

        #### Search suggestion attributes

        If you define a content provider to generate search suggestions, you need to define
        additional attributes that configure communications with the content provider. When providing search
        suggestions, you need some of the following `<searchable>` attributes:

        `android:searchSuggestAuthority`
        :   *String* . (Required to provide search suggestions.) This value must match the
            authority string provided in the `android:authorities`
            attribute of the Android manifest `<provider>` element.

        `android:searchSuggestPath`
        :   *String* . This path is used as a portion of the suggestions
            query `https://developer.android.com/reference/android/net/Uri`, after the prefix and
            authority and before the standard suggestions path. This is only required if you have a
            single content provider issuing different types of suggestions---such as for different
            data types---and you need a way to disambiguate the suggestions queries when you receive
            them.

        `android:searchSuggestSelection`
        :   *String* . This value is passed into your
            query function as the `selection` parameter. Typically this is a WHERE clause
            for your database, and must contain a single question mark as a placeholder for the
            actual query string entered by the user---for example, `"query=?"`. However,
            you can also use any non-null value to trigger the delivery of the query text using the
            `selectionArgs` parameter, and then ignore the `selection` parameter).

        `android:searchSuggestIntentAction`
        :   *String* . The default intent action to be used when a user
            taps on a custom search suggestion---such as `"android.intent.action.VIEW"`.
            If this value is not overridden by the selected suggestion using the
            `https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_ACTION`
            column, the value is placed in the action field of the
            `https://developer.android.com/reference/android/content/Intent` when the user taps
            a suggestion.

        `android:searchSuggestIntentData`
        :   *String* . The default intent data to be used when a user
            taps on a custom search suggestion.
            If not overridden by the selected suggestion---via the
            `https://developer.android.com/reference/android/app/SearchManager#SUGGEST_COLUMN_INTENT_DATA`
            column---this value is placed in the data field of the
            `https://developer.android.com/reference/android/content/Intent` when the user taps
            a suggestion.

        `android:searchSuggestThreshold`
        :   *Integer*. The minimum number of characters needed to
            trigger a suggestion look-up. This only guarantees that the system doesn't query your
            content provider for anything shorter than the threshold. The default value is 0.

        For more information about the above attributes for search suggestions, see the documentation
        for [adding custom search suggestions](https://developer.android.com/develop/ui/views/search/adding-recent-query-suggestions) and
        [adding custom suggestions](https://developer.android.com/develop/ui/views/search/adding-custom-suggestions).

        #### Quick Search Box attributes

        To make your custom search suggestions available to Quick Search Box, you need some of the
        following `<searchable>` attributes:

        `android:includeInGlobalSearch`
        :   *Boolean* . (Required to provide search suggestions in the
            Quick Search Box.) Set to `"true"` if you want your suggestions to be
            included in the globally accessible Quick Search Box. The user must
            still enable your application as a searchable item in the system search settings before
            your suggestions appear in Quick Search Box.

        `android:searchSettingsDescription`
        :   *String resource*. Provides a brief description of the search suggestions that
            you provide to Quick Search Box, which is displayed in the searchable items entry for your
            application. Your description must concisely describe the content that is searchable. For
            example, "Artists, albums, and tracks" for a music application, or "Saved notes" for a
            notepad application.

        `android:queryAfterZeroResults`
        :   *Boolean* . Set to `"true"` if you want your content provider to be
            invoked for supersets of queries that previously returned zero results. For example, if
            your content provider returns zero results for "bo", it must be requeried for "bob". If
            set to `"false"`, supersets are ignored for a single session---"bob"
            doesn't invoke a requery. This lasts only for the life of the search dialog or the life of
            the activity when using the search widget. When the search dialog or activity is reopened,
            "bo" queries your content provider again. The default value is false.

        #### Voice search attributes

        To enable voice search, you need some of the
        following `<searchable>` attributes:

        `android:voiceSearchMode`
        :   *Keyword* . (Required to provide voice search capabilities.)
            Enables voice search, with a specific mode for voice search.
            Voice search might not be provided by the device, in which case these flags
            have no effect. The following mode values are accepted:

            | Value | Description |
            |---|---|
            | `"showVoiceSearchButton"` | Display a voice search button, if voice search is available on the device. If set, then either `"launchWebSearch"` or `"launchRecognizer"` must also be set, separated by the pipe (`|`) character. |
            | `"launchWebSearch"` | The voice search button takes the user directly to a built-in voice web search activity. Most applications don't use this flag, as it takes the user away from the activity in which search was invoked. |
            | `"launchRecognizer"` | The voice search button takes the user directly to a built-in voice recording activity. This activity prompts the user to speak, transcribes the spoken text, and forwards the resulting query text to the searchable activity, just as if the user typed it into the search UI and tapped the search button. |


        `android:voiceLanguageModel`
        :   *Keyword* . The language model that
            must be used by the voice recognition system. The following values are accepted:

            | Value | Description |
            |---|---|
            | `"free_form"` | Use free-form speech recognition for dictating queries. This is primarily optimized for English. This is the default. |
            | `"web_search"` | Use web-search-term recognition for shorter, search-like phrases. This is available in more languages than `"free_form"`. |


            See
            `https://developer.android.com/reference/android/speech/RecognizerIntent#EXTRA_LANGUAGE_MODEL` for more
            information.

        `android:voicePromptText`
        :   *String resource*. An additional message to display in the voice input dialog.

        `android:voiceLanguage`
        :   *String* . The spoken language to be expected, expressed as the string value of
            a constant in `https://developer.android.com/reference/java/util/Locale`, such as
            `"de"` for German or `"fr"` for French. This is needed only if it is different
            from the current value of `https://developer.android.com/reference/java/util/Locale#getDefault()`.

        `android:voiceMaxResults`
        :   *Integer* . Sets the maximum number of results to return,
            including the "best" result, which is always provided as the
            `https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH`
            intent's primary query. Must be 1 or greater. Use
            `https://developer.android.com/reference/android/speech/RecognizerIntent#EXTRA_RESULTS`
            to get the results from the intent.
            If not provided, the recognizer chooses how many results to return.

    `<actionkey>`

    :   Defines a device key and behavior for a search action. A search action provides a special behavior at the tap of a button on the device, based on the current query or focused suggestion. For example, the Contacts application provides a search action to initiate a phone call to the currently focused contact suggestion when the CALL button is tapped.<br />

        Not all action keys are available on every device, and not all keys can be overridden in this
        way. For example, the "Home" key can't be overridden and must always return to the home
        screen. Also, be sure not to define an action key for a key that's needed for typing a search
        query. This limits the available and reasonable action keys to the call button and menu
        button.
        | **Note:** Action keys are not generally discoverable, so don't provide them as a core user feature.

        You must define the `android:keycode` to define the key and at least one of the
        other three attributes to define the search action.

        **Attributes:**

        `android:keycode`
        :   *String* . (Required.) A key code from
            `https://developer.android.com/reference/android/view/KeyEvent` that represents
            the action key you want to respond to---for example, `"KEYCODE_CALL"`. This
            is added to the
            `https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH`
            intent that is passed to your searchable activity. To examine the key code, use
            `https://developer.android.com/reference/android/content/Intent#getIntExtra(java.lang.String, int)`.
            Not all keys are supported for a search action, as many of them are used for typing,
            navigation, or system functions.

        `android:queryActionMsg`
        :   *String* . An action message to be sent if the action key is pressed while the
            user is entering query text. This is added to the
            `https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH`
            intent that the system passes to your searchable activity. To examine the string, use
            `https://developer.android.com/reference/android/content/Intent#getStringExtra(java.lang.String)`.

        `android:suggestActionMsg`
        :   *String* . An action message to be sent if the action key is pressed while a
            suggestion is in focus. This is added to the intent that the system passes to your
            searchable activity---using the action you define for the suggestion. To examine the
            string, use
            `https://developer.android.com/reference/android/content/Intent#getStringExtra(java.lang.String)`.
            This must only be used if all your suggestions support this action key. If not all
            suggestions can handle the same action key, then you must instead use the following
            `android:suggestActionMsgColumn` attribute.

        `android:suggestActionMsgColumn`
        :   *String* . The name of the column in your content provider that defines the
            action message for this action key, which is to be sent if the user presses the action key
            while a suggestion is in focus. This attribute lets you control the action key on a
            suggestion-by-suggestion basis, because, instead of using the
            `android:suggestActionMsg` attribute to define the action message for all
            suggestions, each entry in your content provider provides its own action message.

            First, you must define a column in your content provider for each suggestion to provide
            an action message for, then provide the name of that column in this attribute. The system
            looks at your suggestion cursor, using the string provided here to select your action
            message column, and then selects the action message string from the cursor. That string is
            added to the intent that the system passes to your searchable activity, using the action you
            define for suggestions. To examine the string, use
            `https://developer.android.com/reference/android/content/Intent#getStringExtra(java.lang.String)`.
            If the data doesn't exist for the selected suggestion, the action key is ignored.

example:
:   XML file saved at `res/xml/searchable.xml`:

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <searchable xmlns:android="http://schemas.android.com/apk/res/android"
        android:label="@string/search_label"
        android:hint="@string/search_hint"
        android:searchSuggestAuthority="dictionary"
        android:searchSuggestIntentAction="android.intent.action.VIEW"
        android:includeInGlobalSearch="true"
        android:searchSettingsDescription="@string/settings_description" >
    </searchable>
    ```