---
title: Match URI deep links  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/deep-links/uri-matcher
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Match URI deep links Stay organized with collections Save and categorize content based on your preferences.





For matching hierarchical URIs against patterns and extracting arguments, use
[`UriDeepLinkMatcher`](/reference/kotlin/androidx/navigation3/runtime/deeplink/UriDeepLinkMatcher). It relies on `kotlinx.serialization` to deserialize
matched arguments into your key classes.

To create a `UriDeepLinkMatcher`, provide a pattern [`DeepLinkUri`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkUri) and the
serializer for the corresponding key:

```
@Serializable
data class UserProfileKey(val id: String) : NavKey

val userProfilePattern = DeepLinkUri("www.example.com/users/{id}")
val userProfileMatcher = UriDeepLinkMatcher(userProfilePattern, serializer<UserProfileKey>())

val request = DeepLinkRequest(uri = "https://www.example.com/users/123")
val matchResult = userProfileMatcher.match(request)
val key = matchResult?.key // UserProfileKey(id = "123")

UriMatcherSnippets.kt
```

For non-hierarchical URIs or custom schemes (such as `tel:`), see
[Create custom deep link matchers](/guide/navigation/navigation-3/deep-links/custom-matchers).

## Supported matching patterns

`UriDeepLinkMatcher` matches URIs based on their five components: scheme,
authority, path, query, and fragment. The following sections describe the
supported pattern syntax, argument placeholders, and matching rules for each
component.

### Scheme matching

If no scheme is present in the URI pattern, both `http` and `https` are matched.
To match a specific scheme, include it in the pattern. As an exception, an
`http` scheme in a pattern matches both `http` and `https` request URIs, while
`https` in a pattern only matches `https` requests.

| Pattern URI | Request URI | Match |
| --- | --- | --- |
| `www.example.com` | `https://www.example.com` | ✅ |
| `www.example.com` | `http://www.example.com` | ✅ |
| `http://www.example.com` | `http://www.example.com` | ✅ |
| `http://www.example.com` | `https://www.example.com` | ✅ |
| `https://www.example.com` | `http://www.example.com` | ❌ |
| `myapp://www.example.com` | `myapp://www.example.com` | ✅ |

### Authority matching

`UriDeepLinkMatcher` performs a case-insensitive exact match on the URI
authority (host and optional port). Placeholders or wildcards aren't supported
in the authority, and no arguments are extracted:

| Pattern URI | Request URI | Match |
| --- | --- | --- |
| `example.com` | `https://example.com` | ✅ |
| `example.com` | `https://EXAMPLE.COM` | ✅ |
| `example.com` | `https://sub.example.com` | ❌ |
| `example.com` | `https://www.example.com` | ❌ |
| `example.com` | `https://example.com:8080` | ❌ |
| `example.com:8080` | `https://example.com:8080` | ✅ |
| `example.com:8080` | `https://example.com` | ❌ |

**Note:** `UriDeepLinkMatcher` treats `example.com` and `www.example.com` as
distinct authorities. To match both apex domains and subdomains, define
separate `UriDeepLinkMatcher` instances for each authority or normalize incoming
URIs by [subclassing `UriDeepLinkMatcher`](#customize-matcher).

### Path matching

The following path patterns are supported:

| Pattern URI | Request URI | Match | Extracted Arguments |
| --- | --- | --- | --- |
| `www.example.com/users` | `https://www.example.com/users` | ✅ | None |
| `www.example.com/users/{id}` | `https://www.example.com/users/123` | ✅ | `id`: `"123"` |
| `www.example.com/users/{first}-{last}` | `https://www.example.com/users/john-doe` | ✅ | `first`: `"john"`, `last`: `"doe"` |
| `www.example.com/users/{id}/profile` | `https://www.example.com/users//profile` | ✅ | `id`: `""` (Empty string) |
| `www.example.com/users/user_{id}` | `https://www.example.com/users/user_123` | ✅ | `id`: `"123"` |
| `www.example.com/users/{userId}/posts/{postId}` | `https://www.example.com/users/123/posts/456` | ✅ | `userId`: `"123"`, `postId`: `"456"` |
| `www.example.com/users/.*` | `https://www.example.com/users/john-doe` | ✅ | None |
| `www.example.com/users` | `https://www.example.com/users/` | ❌ (Trailing slash creates an extra segment) | N/A |

### Query matching

Query parameter order in the request URI doesn't need to match the order in the
pattern URI. Additionally, parameters present in the request URI but not the
pattern URI are ignored.

The following query parameter patterns are supported:

| Pattern URI | Request URI | Extracted Arguments |
| --- | --- | --- |
| `www.example.com/users?name={name}` | `https://www.example.com/users?name=john` | `name`: `"john"` |
| `www.example.com/users?name={name}` | `https://www.example.com/users?name=` | `name`: `""` (Empty string) |
| `www.example.com/users?{rawQuery}` | `https://www.example.com/users?anything&else` | `rawQuery`: `["anything", "else"]` |
| `www.example.com/users?type=user_{id}` | `https://www.example.com/users?type=user_123` | `id`: `"123"` |
| `www.example.com/users?name={first}_{last}` | `https://www.example.com/users?name=john_doe` | `first`: `"john"`, `last`: `"doe"` |
| `www.example.com/users?list={list}` | `https://www.example.com/users?list=10&list=20` | `list`: `["10", "20"]` |
| `www.example.com/users?name={name}&{other}` | `https://www.example.com/users?name=john&tab=info` | `name`: `"john"`, `other`: `["tab=info"]` |
| `www.example.com/users?type=user_.*` | `https://www.example.com/users?type=user_admin` | `type`: `"admin"` |

### Fragment matching

The following fragment pattern types are supported:

| Pattern URI | Request URI | Extracted Arguments |
| --- | --- | --- |
| `www.example.com/#section1` | `https://www.example.com/#section1` | None |
| `www.example.com/#section_{id}` | `https://www.example.com/#section_123` | `id`: `"123"` |
| `www.example.com/#section_.*` | `https://www.example.com/#section_123` | None |

## Supported data types

`UriDeepLinkMatcher` supports deserializing URI arguments into primitive
types, enums, collections, and custom objects. Serialization falls into two
categories:

* **Standard serialization**: Uses `kotlinx.serialization` to deserialize
  into:
  + Primitives (`Boolean`, `Int`, `Long`, `Float`, `Double`, `Char`, `Byte`,
    `Short`) and `String`
  + Enums
  + `Set`, `List`, or `Array` of primitives, strings, or enums
  + Nested `@Serializable` classes (whose properties are flattened into
    individual URI placeholders)
* **Custom serialization with [`DeepLinkSerializer`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkSerializer)**: Converts between a
  single `String` and custom objects, external types (such as
  `java.time.LocalDate`), or custom-delimited collections.

### Standard serialization

`UriDeepLinkMatcher` works out of the box for standard types and flattened
structures without requiring custom serializer implementations.

#### Primitives and strings

`UriDeepLinkMatcher` automatically decodes primitive types (`Boolean`, `Int`,
`Long`, `Float`, `Double`, `Char`, `Byte`, `Short`) and `String`:

```
@Serializable
data class UserProfileKey(val id: Int) : NavKey

val matcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/users/{id}"),
    serializer<UserProfileKey>()
)

val request = DeepLinkRequest(uri = "https://www.example.com/users/123")
val key = matcher.match(request)?.key // UserProfileKey(id = 123)

UriMatcherSnippets.kt
```

#### Enums

Enum values are matched case-sensitively against the enum element names:

```
enum class SortOrder { RELEVANCE, DATE, POPULARITY }

@Serializable
data class ProductsKey(val sort: SortOrder) : NavKey

val matcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/products?sort={sort}"),
    serializer<ProductsKey>()
)

val request = DeepLinkRequest(uri = "https://www.example.com/products?sort=DATE")
val key = matcher.match(request)?.key // ProductsKey(sort = SortOrder.DATE)

UriMatcherSnippets.kt
```

#### Repeated query collections

Query parameters with repeated keys (such as `?id=10&id=20`) automatically
deserialize into `List<T>`, `Set<T>`, or `Array<T>` where `T` is a primitive
type, `String`, or enum:

```
@Serializable
data class FilteredItemsKey(val ids: List<Int>) : NavKey

val matcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/items?id={ids}"),
    serializer<FilteredItemsKey>()
)

val request = DeepLinkRequest(uri = "https://www.example.com/items?id=10&id=20")
val key = matcher.match(request)?.key // FilteredItemsKey(ids = listOf(10, 20))

UriMatcherSnippets.kt
```

#### Nested @Serializable classes

When a `NavKey` contains a property whose type is another `@Serializable` class,
`UriDeepLinkMatcher` flattens its properties so each property of the nested
class maps directly to an individual URI parameter of the same name:

```
enum class SortOrder { RELEVANCE, DATE, POPULARITY }

@Serializable
data class SearchFilters(
    val category: String,
    val sortBy: SortOrder = SortOrder.RELEVANCE
)

@Serializable
data class SearchKey(
    val query: String,
    val page: Int = 1,
    // Flattened into {category} and {sortBy}
    val filters: SearchFilters
) : NavKey

val matcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/search?q={query}&page={page}&category={category}&sortBy={sortBy}"),
    serializer<SearchKey>()
)

val request = DeepLinkRequest(uri = "https://www.example.com/search?q=kotlin&category=books&sortBy=DATE")
val key = matcher.match(request)?.key
// SearchKey(query = "kotlin", page = 1, filters = SearchFilters(category = "books", sortBy = SortOrder.DATE))

UriMatcherSnippets.kt
```

**Caution:** Because properties are flattened into a single URI parameter namespace,
avoid duplicate property names across parent and nested classes (for example,
having `id` properties in both the key class and the nested filter class). You
can use `@SerialName` to change the name of a property in the URI pattern to
avoid collisions.

### Custom serialization with `DeepLinkSerializer`

To deserialize custom objects (such as `Filter(key = "brand", value =
"pixel")`), external types (such as `java.time.LocalDate`), or custom delimited
strings (such as comma-separated values), extend [`DeepLinkSerializer<T>`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkSerializer).

`DeepLinkSerializer<T>` is an abstract [`KSerializer<T>`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html) that converts
between a `String` and `T`:

```
abstract class DeepLinkSerializer<T : Any> : KSerializer<T> {
    abstract val serialName: String
    abstract fun deserialize(value: String): T
    abstract fun serialize(value: T): String
}
```

For example, consider the `Filter` and `FilterSerializer` definitions that are
used in the following snippets:

```
@Serializable
data class Filter(val key: String, val value: String)

object FilterSerializer : DeepLinkSerializer<Filter>() {
    override val serialName: String = "com.example.Filter"

    override fun deserialize(value: String): Filter {
        val parts = value.split(":", limit = 2)
        if (parts.size < 2) {
            throw SerializationException("Invalid filter: $value. Expected key:value.")
        }
        return Filter(key = parts[0], value = parts[1])
    }

    override fun serialize(value: Filter): String = "${value.key}:${value.value}"
}

UriMatcherSnippets.kt
```

#### Single custom objects

To decode an object from a single URI parameter string (such as
`?filter=brand:google`), annotate the property with `@Serializable(with = ...)`:

```
@Serializable
data class CatalogKey(
    @Serializable(with = FilterSerializer::class)
    val filter: Filter
) : NavKey

val matcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/catalog?filter={filter}"),
    serializer<CatalogKey>()
)

val request = DeepLinkRequest(uri = "https://www.example.com/catalog?filter=brand:google")
val key = matcher.match(request)?.key // CatalogKey(filter = Filter("brand", "google"))

UriMatcherSnippets.kt
```

#### Custom objects in repeated query parameters

To deserialize repeated query parameters into a collection of custom objects
(`List<T>`, `Set<T>`, or `Array<T>`), implement `DeepLinkSerializer<T>` for the
**element type** `T` and annotate the type argument of the property with
`@Serializable(with = ...)`:

```
@Serializable
data class SearchResultsKey(
    val query: String,
    val filters: List<@Serializable(with = FilterSerializer::class) Filter> = emptyList()
) : NavKey

val searchResultsPattern = DeepLinkUri("www.example.com/search?q={query}&filter={filters}")
val searchResultsMatcher = UriDeepLinkMatcher(searchResultsPattern, serializer<SearchResultsKey>())

val request = DeepLinkRequest(uri = "https://www.example.com/search?q=phone&filter=brand:google&filter=color:hazel")
val matchResult = searchResultsMatcher.match(request)
val key = matchResult?.key
// SearchResultsKey(query = "phone", filters = listOf(Filter("brand", "google"), Filter("color", "hazel")))

UriMatcherSnippets.kt
```

#### Delimited collections in single parameters

To parse comma-separated or custom-delimited values (such as `?ids=1,2,3`) into
a collection, implement `DeepLinkSerializer` for the **entire collection type**
and annotate the property with `@Serializable(with = ...)`:

```
object IntListCsvSerializer : DeepLinkSerializer<List<Int>>() {
    override val serialName: String = "com.example.IntListCsv"

    override fun deserialize(value: String): List<Int> {
        if (value.isEmpty()) return emptyList()
        return value.split(",").map { it.trim().toInt() }
    }

    override fun serialize(value: List<Int>): String = value.joinToString(",")
}

@Serializable
data class ItemListKey(
    @Serializable(with = IntListCsvSerializer::class)
    val ids: List<Int>
) : NavKey

val itemListPattern = DeepLinkUri("www.example.com/items/{ids}")
val itemListMatcher = UriDeepLinkMatcher(itemListPattern, serializer<ItemListKey>())

val request = DeepLinkRequest(uri = "https://www.example.com/items/10,20,30")
val key = itemListMatcher.match(request)?.key // ItemListKey(ids = listOf(10, 20, 30))

UriMatcherSnippets.kt
```

## Argument validation and matching outcomes

`UriDeepLinkMatcher` distinguishes between **mismatches** (returns `null` so
other matchers can be attempted) and **unsupported configurations** (throws an
exception).

### Mismatches

A mismatch occurs when an incoming request URI doesn't satisfy the pattern or
type requirements:

* **Missing required parameters**: Non-nullable key properties without default
  values whose corresponding URI parameters are absent from the request URI.
* **Type parsing failures**: Extracted argument values that can't be parsed
  into the expected property type (for example, `"abc"` for an `Int`
  property).

When a mismatch occurs, `UriDeepLinkMatcher.match` returns `null`, allowing
subsequent matchers to be evaluated.

Consider a key class and matcher configured with default values, nested objects,
and enums:

```
enum class MapLayer { STANDARD, SATELLITE, TERRAIN }

@Serializable
data class LayerOptions(
    val style: String,
    val layer: MapLayer = MapLayer.STANDARD
)

@Serializable
data class MapKey(
    val location: String,
    val zoom: Int = 12,
    val options: LayerOptions
) : NavKey

val matcher = UriDeepLinkMatcher(
    DeepLinkUri("www.example.com/map/{location}?zoom={zoom}&style={style}&layer={layer}"),
    serializer<MapKey>()
)

UriMatcherSnippets.kt
```

The following table demonstrates matching outcomes for various request URIs:

| Request URI | Decoding Outcome | Match Result |
| --- | --- | --- |
| `https://www.example.com/map/paris?zoom=15&style=dark&layer=SATELLITE` | **Success** (All parameters provided) | `UriMatchResult(MapKey("paris", 15, LayerOptions("dark", MapLayer.SATELLITE)))` |
| `https://www.example.com/map/paris?style=dark` | **Success** (`zoom` defaults to `12`, `layer` to `STANDARD`) | `UriMatchResult(MapKey("paris", 12, LayerOptions("dark", MapLayer.STANDARD)))` |
| `https://www.example.com/map/paris?zoom=&style=dark` | **Success** (Empty optional query parameter uses default `12`) | `UriMatchResult(MapKey("paris", 12, LayerOptions("dark", MapLayer.STANDARD)))` |
| `https://www.example.com/map?style=dark` | **Mismatch** (Missing required `location` parameter) | `null` |
| `https://www.example.com/map/paris?zoom=close&style=dark` | **Mismatch** (`"close"` isn't an `Int`) | `null` |
| `https://www.example.com/map/paris?style=dark&layer=HYBRID` | **Mismatch** (`"HYBRID"` isn't in enum) | `null` |

### Unsupported configurations

If your key class contains unsupported data types, `UriDeepLinkMatcher` throws
an exception during matching instead of returning `null`.

* **Maps and multi-dimensional collections**: `UriDeepLinkMatcher` only
  supports single-dimensional collections of primitives, strings, enums, or
  custom types annotated with a [`DeepLinkSerializer`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkSerializer). `Map` types throw
  an `IllegalArgumentException`, while nested collections (such as
  `List<List<String>>`) throw a `SerializationException`.
* **Unannotated custom object collections**: Collections of custom types (such
  as `List<Filter>`) throw a `SerializationException` unless the element type
  is annotated with a [`DeepLinkSerializer`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkSerializer).
* **Unflattened nested classes**: Nested `@Serializable` classes can't be
  mapped to a single placeholder (such as `?user={user}`) without a
  [`DeepLinkSerializer`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkSerializer).

```
// Throws IllegalArgumentException: Map decoding is not supported.
@Serializable
data class InvalidKey(val tags: Map<String, String>) : NavKey
// Throws SerializationException: Only collections of primitives are supported.
@Serializable
data class InvalidKey(val filters: List<Filter>) : NavKey

UriMatcherSnippets

.kt
```

## `UriMatchResult` comparison

[`UriMatchResult`](/reference/kotlin/androidx/navigation3/runtime/deeplink/UriMatchResult) instances are ranked using the following criteria in
order:

1. **MatchResult type**: `UriMatchResult` ranks higher than other `MatchResult`
   types.
2. **Exact path**: Literal path matches rank higher than placeholder or
   wildcard matches.
3. **Path argument count**: Matches with more path arguments rank higher.
4. **Presence of arguments**: Matches that capture arguments rank higher than
   those that don't.
5. **Total argument count**: The total number of arguments (path, query,
   fragment) is the final tie-breaker.

## Customize `UriDeepLinkMatcher`

`UriDeepLinkMatcher` is an `open` class that you can subclass to customize URI
matching and argument extraction behavior:

* [`matchRequest`](/reference/kotlin/androidx/navigation3/runtime/deeplink/UriDeepLinkMatcher#matchRequest(androidx.navigation3.runtime.deeplink.DeepLinkRequest)): Top-level matching entry point for an incoming
  [`DeepLinkRequest`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkRequest). Override this to inspect request extras or apply
  custom preconditions before URI matching.
* [`matchUri`](/reference/kotlin/androidx/navigation3/runtime/deeplink/UriDeepLinkMatcher#matchUri(androidx.navigation3.runtime.deeplink.DeepLinkUri)): Matches the [`DeepLinkUri`](/reference/kotlin/androidx/navigation3/runtime/deeplink/DeepLinkUri) against the configured
  pattern. Override this to intercept and normalize incoming URIs (for
  example, rewriting dynamic subdomains or legacy path formats) before calling
  `super.matchUri`.
* [`matchArguments`](/reference/kotlin/androidx/navigation3/runtime/deeplink/UriDeepLinkMatcher#matchArguments(kotlin.collections.Map,kotlin.collections.Map,kotlin.collections.Map)): Deserializes the extracted path, query, and fragment
  argument maps into a navigation key instance using the provided
  `serializer`. Override this to inject dynamic values or transform arguments
  before key instantiation.

The following example demonstrates subclassing `UriDeepLinkMatcher` to normalize
legacy URL path prefixes before matching:

```
class LegacyPrefixUriDeepLinkMatcher<T : Any>(
    uriPattern: DeepLinkUri,
    serializer: KSerializer<T>
) : UriDeepLinkMatcher<T>(uriPattern, serializer) {

    override fun matchUri(uri: DeepLinkUri): UriMatchResult<T>? {
        val path = uri.path
        val normalizedUri = if (path != null && path.startsWith("/legacy/")) {
            DeepLinkUri(uri.toString().replaceFirst("/legacy", ""))
        } else {
            uri
        }
        return super.matchUri(normalizedUri)
    }
}

UriMatcherSnippets.kt
```