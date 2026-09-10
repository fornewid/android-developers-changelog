---
title: https://developer.android.com/guide/navigation/navigation-3/deep-links
url: https://developer.android.com/guide/navigation/navigation-3/deep-links
source: md.txt
---

Starting in version [1.2.0](https://developer.android.com/jetpack/androidx/releases/navigation3#navigation3_version_12_2), Navigation 3 supports deep linking to
destinations in your app using the [`DeepLinkRequest`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest) and
[`DeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher) classes.

To support deep links in your app, complete the following steps:

1. **Define intent filters** in your `AndroidManifest.xml` to specify which URIs your app can handle.
2. **Create `DeepLinkMatcher` instances** to map incoming requests to your navigation keys.
3. **Match incoming requests** in your activity's `onCreate` or `onNewIntent` method and update your back stack accordingly.

## Create a `DeepLinkRequest`

A `DeepLinkRequest` represents an incoming deep link. It contains a
[`DeepLinkUri`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkUri) and optional [`RequestExtras`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/RequestExtras) with additional
information, such as the intent action or MIME type.

> [!NOTE]
> **Note:** On Android, `DeepLinkUri` is a typealias of [`android.net.Uri`](https://developer.android.com/reference/android/net/Uri).


```kotlin
// Create a request with a String URI
val request = DeepLinkRequest(uri = "https://www.example.com/home")

// Create a request from a DeepLinkUri
val deepLinkUri = DeepLinkUri("https://www.example.com/home")
val requestFromUri = DeepLinkRequest(uri = deepLinkUri)

// Create a request with a URI and action
val requestWithAction = DeepLinkRequest(
    uri = "https://www.example.com/home",
    extras = DeepLinkRequest.actionExtra("android.intent.action.VIEW")
)

// Create a request with URI, action and mimeType
val requestWithMimeType = DeepLinkRequest(
    uri = "https://www.example.com/image",
    extras = requestExtras {
        put(DeepLinkRequest.ActionExtrasKey, "android.intent.action.VIEW")
        put(DeepLinkRequest.Companion.MimeTypeExtrasKey, "image/png")
    }
)
```

<br />

### Provide `DeepLinkRequest` extras

To store additional information related to the deep link, use the
[`RequestExtras`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/RequestExtras) class. To make defining and instantiating extras type-safe,
the library provides the [`RequestExtrasKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/RequestExtrasKey) interface and
[`requestExtras`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/package-summary#requestExtras(kotlin.Function1)) DSL.

Additionally, the library provides two extras keys and associated helpers:

- [`MimeTypeExtrasKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest.Companion#MimeTypeExtrasKey): Used to store a MIME type `String`.
- [`ActionExtrasKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest.Companion#(androidx.navigation3.runtime.deeplink.DeepLinkRequest.Companion).ActionExtrasKey) (Android-only): Used to store an `Intent`'s action `String`.


```kotlin
val extras: RequestExtras = requestExtras {
    put(DeepLinkRequest.Companion.MimeTypeExtrasKey, "application/json")
    put(DeepLinkRequest.ActionExtrasKey, Intent.ACTION_VIEW)
}

// Access typed values using the get operator
val mimeType: String? = extras[DeepLinkRequest.Companion.MimeTypeExtrasKey]
val action: String? = extras[DeepLinkRequest.ActionExtrasKey]

// Create extras using helper functions and combine them
val mimeTypeExtras: RequestExtras = DeepLinkRequest.mimeTypeExtra("application/json")
val combinedExtras: RequestExtras = extras + DeepLinkRequest.actionExtra(Intent.ACTION_VIEW)
```

<br />

To define your own custom extras, implement the [`RequestExtrasKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/RequestExtrasKey)
interface with a typed generic:


```kotlin
// Define a custom typed key:
object CampaignIdExtrasKey : RequestExtrasKey<String>

val customExtras: RequestExtras = requestExtras {
    put(CampaignIdExtrasKey, "123")
}

val campaignId: String? = customExtras[CampaignIdExtrasKey]
```

<br />

You can also use [`emptyRequestExtras()`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/package-summary#emptyRequestExtras()) to construct an empty instance, or
combine extras using the `+` (`plus`) and `-` (`minus`) operators.

### Create a `DeepLinkRequest` from an `Intent`

On Android, you can create a `DeepLinkRequest` directly from an `Intent`. When
constructed this way, the `DeepLinkRequest` is built as follows:

- The `uri` is copied from the intent's [`data`](https://developer.android.com/reference/kotlin/android/content/Intent#getdata) field.
- If not null, the MIME type and action [extras](https://developer.android.com/guide/navigation/navigation-3/deep-links#request-extras) are set from the corresponding intent fields.
- All of the [`intent.extras`](https://developer.android.com/training/basics/intents/sending#add-extras) with non-null values are saved as a [`SavedState`](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedState) in [`DeepLinkRequest.IntentExtrasKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest.Companion#(androidx.navigation3.runtime.deeplink.DeepLinkRequest.Companion).IntentExtrasKey).
- Any additional extras provided using the `extras` parameter are added.


```kotlin
object CampaignIdExtrasKey : RequestExtrasKey<String>

val intent = Intent(Intent.ACTION_VIEW).apply {
    data = Uri.parse("https://www.example.com/item/42")
    type = "application/json"
    putExtra("user_id", "123")
}

val request = DeepLinkRequest(
    intent = intent,
    extras = requestExtras {
        put(CampaignIdExtrasKey, "spring_promo")
    }
)

// The resulting DeepLinkRequest contains:
val uri = request.uri // "https://www.example.com/item/42"
val action = request.extras[DeepLinkRequest.ActionExtrasKey] // "android.intent.action.VIEW"
val mimeType = request.extras[DeepLinkRequest.Companion.MimeTypeExtrasKey] // "application/json"
val intentExtras: SavedState? =
    request.extras[DeepLinkRequest.IntentExtrasKey]
val userId: String? = intentExtras?.read { getStringOrNull("user_id") } // "123"
val campaignId: String? = request.extras[CampaignIdExtrasKey] // "spring_promo"
```

<br />

## Create `DeepLinkMatcher` instances

A [`DeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher) maps incoming [`DeepLinkRequest`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest) instances to
navigation keys that can be added to your app's back stack. Navigation 3
provides three built-in matchers: [`UriDeepLinkMatcher`](https://developer.android.com/guide/navigation/navigation-3/deep-links/uri-matcher) for
pattern-based URI matching, `StaticKeyDeepLinkMatcher` for basic links, and
`BackStackMatcher` for building synthetic back stacks. The library also
supports [custom matchers](https://developer.android.com/guide/navigation/navigation-3/deep-links/custom-matchers) for use cases not covered by the built-in
matchers.

For more information, see [Create DeepLinkMatchers](https://developer.android.com/guide/navigation/navigation-3/deep-links/create-matchers).

## Add intent filters

To enable a deep link to start your activity, you must define the matching
`<intent-filter>` elements in your app's `AndroidManifest.xml`. For more
information, see [Add intent filters for incoming links](https://developer.android.com/training/app-links/create-deeplinks#add-intent).

## Match an incoming request

After you've [created your `DeepLinkMatcher` instances](https://developer.android.com/guide/navigation/navigation-3/deep-links/create-matchers), you can match
incoming requests in your activity.

To match an incoming request, complete the following steps:

1. **Instantiate** your `DeepLinkMatcher` instances.
2. **Collate** all of your `DeepLinkMatcher` instances, either explicitly or by using [multibindings](https://developer.android.com/guide/navigation/navigation-3/modularize#modularize-deeplinks).
3. **Create** a `DeepLinkRequest` from the incoming `Intent`.
4. **Match** the request against all matchers and find the best match.
5. **Create** the back stack from the match result.


```kotlin
// 1. Instantiate your DeepLinkMatcher instances.
val homeMatcher = StaticKeyDeepLinkMatcher(HomeKey, listOf(DeepLinkMatcher.actionFilter(Intent.ACTION_VIEW)))

val userProfileMatcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/users/{id}"),
    serializer<UserProfileKey>()
).withBackStack { matchResult ->
    listOf(HomeKey, matchResult.key)
}

val telMatcher = TelDeepLinkMatcher()

// 2. Collate all of your DeepLinkMatcher instances.
//    Note: Collating matchers with different generic types requires wildcards,
//    erasing the specific generic types.
val deepLinkMatchers: List<DeepLinkMatcher<*, *>> = listOf(
    homeMatcher,
    userProfileMatcher,
    telMatcher
)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // ...

        // 3. Create a DeepLinkRequest from the incoming Intent
        val request = DeepLinkRequest(intent = intent)

        // 4. Match the request against all matchers and find the best match.
        //    Because DeepLinkMatcher.MatchResult implements Comparable, you can
        //    use maxOrNull() to find the best match.
        val matchResult = deepLinkMatchers
            .mapNotNull { it.match(request) } // List<DeepLinkMatcher.MatchResult<*>>
            .maxOrNull() // DeepLinkMatcher.MatchResult<*>?

        // 5. Create the back stack from the match result (or fall back to a default).
        val backStack: List<NavKey> = when (matchResult) {
            // If no match is found, use the default back stack (e.g., HomeKey)
            null -> listOf(HomeKey)
            // If a BackStackMatchResult is found, use the back stack from the result
            is BackStackMatchResult<*, *> -> {
                // Because star-projected matchers erase the key type, cast the back stack to List<NavKey>.
                @Suppress("UNCHECKED_CAST")
                matchResult.backStack as List<NavKey>
            }
            // Otherwise, use the key from the match result to make a single-item back stack
            else -> listOf(matchResult.key as NavKey)
        }
    }
}
```

<br />