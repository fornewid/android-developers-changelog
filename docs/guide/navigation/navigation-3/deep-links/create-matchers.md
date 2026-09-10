---
title: https://developer.android.com/guide/navigation/navigation-3/deep-links/create-matchers
url: https://developer.android.com/guide/navigation/navigation-3/deep-links/create-matchers
source: md.txt
---

To map incoming [`DeepLinkRequest`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest) instances to keys that can be added to
your app's back stack, you define [`DeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher) instances.

`DeepLinkMatcher` is an abstract class that includes two methods, [`match`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher#match(androidx.navigation3.runtime.deeplink.DeepLinkRequest))
and [`matchRequest`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher#matchRequest-androidx.navigation3.runtime.deeplink.DeepLinkRequest-). Subclasses must implement `matchRequest`, which takes a
`DeepLinkRequest` and returns a [`DeepLinkMatcher.MatchResult`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher.MatchResult) if the
request matches, or `null` otherwise.

Because multiple matchers might match a single request, `MatchResult` implements
[`Comparable`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-comparable/index.html) to rank results and select the best match.

## Type parameters

The `DeepLinkMatcher` class declares two generic type parameters:
`DeepLinkMatcher<T : Any, R : DeepLinkMatcher.MatchResult<T>>`.

- **`T : Any`** : The destination navigation key type (such as `UserProfileKey` or `NavKey`) returned when the deep link matches.
- **`R : DeepLinkMatcher.MatchResult<T>`** : The specific `MatchResult` subtype returned by [`matchRequest`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher#matchRequest-androidx.navigation3.runtime.deeplink.DeepLinkRequest-) and [`match`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher#match(androidx.navigation3.runtime.deeplink.DeepLinkRequest)).

The second type parameter, `R`, preserves specialized match information without
requiring unchecked downcasting:

- [`StaticKeyDeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/StaticKeyDeepLinkMatcher) binds `R` to `DeepLinkMatcher.MatchResult<T>`.
- [`UriDeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/UriDeepLinkMatcher) binds `R` to [`UriMatchResult`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/UriMatchResult), retaining parsed path and query arguments alongside pattern-matching scores.
- [`BackStackMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/BackStackMatcher) binds `R` to [`BackStackMatchResult`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/BackStackMatchResult), retaining the synthetic back stack list constructed by [`withBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/package-summary#(androidx.navigation3.runtime.deeplink.DeepLinkMatcher).withBackStack(kotlin.Function1)).

## Pre-filter requests

`DeepLinkMatcher` implementations can specify a list of
[`DeepLinkMatcher.Filter`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher.Filter) instances to filter requests before
evaluating them.

The library includes helper functions to create common filters:

- [`DeepLinkMatcher.mimeTypeFilter`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher.Companion#mimeTypeFilter(kotlin.String)): Matches by exact `mimeType` strings (checks [`MimeTypeExtrasKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest.Companion#MimeTypeExtrasKey)).
- [`DeepLinkMatcher.actionFilter`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher.Companion#(androidx.navigation3.runtime.deeplink.DeepLinkMatcher.Companion).actionFilter(kotlin.String)): Matches by exact `action` strings (checks [`ActionExtrasKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest.Companion#(androidx.navigation3.runtime.deeplink.DeepLinkRequest.Companion).ActionExtrasKey)).

This approach lets you reuse the same URI pattern for different actions, such
as viewing versus editing:


```kotlin
val viewFilter = DeepLinkMatcher.actionFilter(Intent.ACTION_VIEW)
val editFilter = DeepLinkMatcher.actionFilter(Intent.ACTION_EDIT)

val imageUriPattern = DeepLinkUri("www.example.com/image/{id}")

val viewMatcher = UriDeepLinkMatcher(imageUriPattern, serializer<Gallery>(), filters = listOf(viewFilter))
val editMatcher = UriDeepLinkMatcher(imageUriPattern, serializer<Editor>(), filters = listOf(editFilter))
```

<br />

Because `Filter` is a functional (SAM) interface, you can also create filters
using lambda expressions:


```kotlin
val myFilter = DeepLinkMatcher.Filter { request -> request.uri != null }
```

<br />

## Use provided matchers

The library includes three standard `DeepLinkMatcher` implementations:
[`StaticKeyDeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/StaticKeyDeepLinkMatcher), [`UriDeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/UriDeepLinkMatcher), and
[`BackStackMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/BackStackMatcher). If these matchers don't meet your app's requirements,
you can [create custom deep link matchers](https://developer.android.com/guide/navigation/navigation-3/deep-links/custom-matchers).

### Match basic deep links

For basic deep links that don't have arguments to extract, use
[`StaticKeyDeepLinkMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/StaticKeyDeepLinkMatcher) to match requests that meet all
provided filters.

For example, to handle intents for [`ACTION_APPLICATION_PREFERENCES`](https://developer.android.com/reference/android/content/Intent#ACTION_APPLICATION_PREFERENCES):


```kotlin
val preferencesActionFilter = DeepLinkMatcher.actionFilter(Intent.ACTION_APPLICATION_PREFERENCES)

val preferencesActionDeepLinkMatcher = StaticKeyDeepLinkMatcher(PreferencesScreen, listOf(preferencesActionFilter))
```

<br />

> [!CAUTION]
> **Caution:** Don't use `StaticKeyDeepLinkMatcher` for matching fixed URIs, such as `www.example.com/home`. Instead, use `UriDeepLinkMatcher`, because it returns [`UriMatchResult`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/UriMatchResult) instances that can be compared against other URI match results.

### Match URI deep links

For matching hierarchical URIs against patterns and extracting arguments, use
`UriDeepLinkMatcher`. For example, you can match `www.example.com/users/{id}` to
extract the `id` argument into a destination key. For more information, see
[Match URI deep links](https://developer.android.com/guide/navigation/navigation-3/deep-links/uri-matcher).

### Build a synthetic back stack

To define how to build a synthetic back stack from a successful match, use
[`BackStackMatcher`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/BackStackMatcher). Rather than instantiating `BackStackMatcher`
directly, call the [`withBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/package-summary#(androidx.navigation3.runtime.deeplink.DeepLinkMatcher).withBackStack(kotlin.Function1)) extension function on another
`DeepLinkMatcher`. `withBackStack` wraps the receiver in a `BackStackMatcher`
that returns a [`BackStackMatchResult`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/deeplink/BackStackMatchResult) containing a synthetic back stack
`List`. Because `BackStackMatchResult` delegates comparison to the underlying
match result, wrapping a matcher in `withBackStack` preserves its original match
ranking.


```kotlin
val homeMatcher = StaticKeyDeepLinkMatcher(HomeKey, listOf(DeepLinkMatcher.actionFilter(Intent.ACTION_VIEW)))

val userListMatcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/users?page={page}"),
    serializer<UserListKey>()
).withBackStack { matchResult ->
    listOf(HomeKey, matchResult.key)
}

val userProfileMatcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/users/{id}"),
    serializer<UserProfileKey>()
).withBackStack { matchResult ->
    listOf(HomeKey, UserListKey(), matchResult.key)
}
```

<br />

To handle the resulting back stack in your activity, see
[Match an incoming request](https://developer.android.com/guide/navigation/navigation-3/deep-links#match-request).