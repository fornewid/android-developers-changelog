---
title: Create custom DeepLinkMatcher classes  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/deep-links/custom-matchers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Create custom DeepLinkMatcher classes Stay organized with collections Save and categorize content based on your preferences.





If the [provided matchers](/guide/navigation/navigation-3/deep-links/create-matchers#use-provided-matchers) aren't sufficient for your use cases, you can
create your own by extending the [`DeepLinkMatcher`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher) class.

When extending `DeepLinkMatcher<T, R>`, you must specify two type arguments: the
destination navigation key type (`T : Any`) and the match result type
(`R : DeepLinkMatcher.MatchResult<T>`). If your matcher doesn't need custom
result ranking or extra metadata, use `DeepLinkMatcher.MatchResult<T>` as the
second type argument.

For example, here's a basic implementation of a `TelDeepLinkMatcher` that
supports `tel` URIs (such as `tel:5550100`). Because `tel` URIs are opaque,
`UriDeepLinkMatcher` doesn't support them:

```
class TelDeepLinkMatcher : DeepLinkMatcher<DialerKey, DeepLinkMatcher.MatchResult<DialerKey>>() {
    override fun matchRequest(request: DeepLinkRequest): MatchResult<DialerKey>? {
        val uri = request.uri ?: return null
        if (uri.scheme != "tel") return null

        // Note: schemeSpecificPart is only available on Android
        val phoneNumber = uri.schemeSpecificPart ?: return null
        return MatchResult(DialerKey(phoneNumber = phoneNumber))
    }
}

CustomMatchersSnippets.kt
```

## Rank custom `MatchResult` classes

If there's a meaningful way to compare match results from your custom matcher,
you should extend [`DeepLinkMatcher.MatchResult`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher.MatchResult) and override the
[`compareTo`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkMatcher.MatchResult#compareTo-androidx.navigation3.runtime.deeplink.DeepLinkMatcher.MatchResult-) method to rank results.

When you create a custom `MatchResult` subclass, update your matcher's class
declaration to specify that subclass as its second type parameter `R` (such as
`class TelDeepLinkMatcher : DeepLinkMatcher<DialerKey, TelMatchResult>()`).
This lets callers access your custom result properties without unchecked
downcasting.

For example, to support wildcard pattern matching in `TelDeepLinkMatcher`, you
can implement a `TelMatchResult` to ensure exact matches rank higher than
wildcard matches. If the matcher is wrapped in [`withBackStack`](/reference/kotlin/androidx/navigation3/runtime/deeplink/package-summary#(androidx.navigation3.runtime.deeplink.DeepLinkMatcher).withBackStack(kotlin.Function1)), unwrap
[`WrappedMatchResult`](/reference/kotlin/androidx/navigation3/runtime/deeplink/WrappedMatchResult) before comparing so that precedence is evaluated
against the underlying match result:

```
class TelMatchResult(
    key: DialerKey,
    val isExactMatch: Boolean,
    val patternLength: Int
) : DeepLinkMatcher.MatchResult<DialerKey>(key) {
    override fun compareTo(other: DeepLinkMatcher.MatchResult<DialerKey>): Int {
        // Unwrap if the other result is wrapped in a BackStackMatchResult or custom WrappedMatchResult
        val target = if (other is WrappedMatchResult<*>) other.matchResult else other
        if (target !is TelMatchResult) {
            // Determine precedence relative to other MatchResult types (e.g. UriMatchResult)
            return 1
        }

        // An exact match wins over a wildcard/prefix match
        if (isExactMatch && !target.isExactMatch) return 1
        if (!isExactMatch && target.isExactMatch) return -1

        // The more specific (longer) pattern wins (e.g., tel:1800* versus tel:*)
        val lengthDiff = this.patternLength - target.patternLength
        if (lengthDiff != 0) {
            return lengthDiff
        }

        return 0
    }
}

CustomMatchersSnippets.kt
```