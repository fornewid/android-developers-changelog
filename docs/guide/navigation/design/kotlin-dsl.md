---
title: https://developer.android.com/guide/navigation/design/kotlin-dsl
url: https://developer.android.com/guide/navigation/design/kotlin-dsl
source: md.txt
---

The Navigation component provides a Kotlin-based domain-specific language, or
DSL, that relies on Kotlin's [type-safe
builders](https://kotlinlang.org/docs/reference/type-safe-builders.html)
. This API lets you declaratively compose your graph in your Kotlin code, rather
than inside an XML resource. This can be useful if you want to build your app's
navigation dynamically. For example, your app could download and cache a
navigation configuration from an external web service and then use that
configuration to dynamically build a navigation graph in your activity's
`onCreate()` function.

## Dependencies

To use the Kotlin DSL with Fragments, add the following dependency to your app's
`build.gradle` file:  

### Groovy

```groovy
dependencies {
    def nav_version = "2.9.7"

    api "androidx.navigation:navigation-fragment-ktx:$nav_version"
}
```

### Kotlin

```kotlin
dependencies {
    val nav_version = "2.9.7"

    api("androidx.navigation:navigation-fragment-ktx:$nav_version")
}
```

## Building a graph

Here is a basic example based on the [Sunflower
app](https://github.com/android/sunflower/tree/views). For this
example, we have two destinations: `home` and `plant_detail`. The `home`
destination is present when the user first launches the app. This destination
displays a list of plants from the user's garden. When the user selects one of
the plants, the app navigates to the `plant_detail` destination.

Figure 1 shows these destinations along with the arguments required by the
`plant_detail` destination and an action, `to_plant_detail`, that the app uses
to navigate from `home` to `plant_detail`.
![The Sunflower app has two destinations along with an action that
connects them.](https://developer.android.com/static/images/guide/navigation/navigation-kotlin-dsl-1.png) **Figure 1.** The Sunflower app has two destinations, `home` and `plant_detail`, along with an action that connects them.

### Hosting a Kotlin DSL Nav Graph

Before you can build your app's navigation graph, you need a place to host the
graph. This example uses fragments, so it hosts the graph in a
[`NavHostFragment`](https://developer.android.com/reference/androidx/navigation/fragment/NavHostFragment)
inside of a
[`FragmentContainerView`](https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView):  

    <!-- activity_garden.xml -->
    <FrameLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto">
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <androidx.fragment.app.FragmentContainerView
            android:id="@+id/nav_host"
            android:name="androidx.navigation.fragment.NavHostFragment"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:defaultNavHost="true" />

    </FrameLayout>

Notice that the `app:navGraph` attribute is not set in this example. The graph
isn't defined as a [resource](https://developer.android.com/guide/topics/resources/providing-resources) in
the `res/navigation` folder so it needs to be set as part of the `onCreate()`
process in the activity.

In XML, an action ties together a destination ID with one or more arguments.
However, when using the Navigation DSL a route can contain arguments as part of
the route. This means that there is no concept of actions when using the DSL.

The next step is to define the routes that you will use when defining your
graph.

### Create routes for your graph

[XML-based navigation graphs](https://developer.android.com/guide/navigation/design#xml) are parsed as part
of the Android build process. A numeric constant is created for each `id`
attribute defined in the graph. These build time generated static IDs are not
available when building your navigation graph at runtime so the Navigation DSL
uses [serializable
types](https://kotlinlang.org/docs/serialization.html) instead of
IDs. Each route is represented by a unique type.

When dealing with arguments, these are [built into the route
type](https://developer.android.com/jetpack/compose/navigation#nav-with-args). This lets you have type safety
for your navigation arguments.  

    @Serializable data object Home
    @Serializable data class Plant(val id: String)

### Build a graph with the NavGraphBuilder DSL

Once you've defined your routes, you can build the navigation graph.  

    val navController = findNavController(R.id.nav_host_fragment)
    navController.graph = navController.createGraph(
        startDestination = Home
    ) {
        fragment<HomeFragment, Home> {
            label = resources.getString(R.string.home_title)
        }
        fragment<PlantDetailFragment, PlantDetail> {
            label = resources.getString(R.string.plant_detail_title)
        }
    }

In this example, two fragment destinations are defined using the
[`fragment()`](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.navigation.NavGraphBuilder).fragment(kotlin.collections.Map,kotlin.Function1))
DSL builder function. This function requires two [type
arguments](https://kotlinlang.org/docs/generics.html#generic-functions)
.

First, a [`Fragment`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) class
that provides the UI for this destination. Setting this has the same effect as
setting the `android:name` attribute on fragment destinations that are defined
using XML.

Second, the route. This must be a serializable type which extends from `Any`. It
should contain any navigation arguments that will be used by this destination,
and their types.

The function also accepts an optional lambda for additional configuration, such
as the destination label, as well as embedded builder functions for custom
arguments and deep links.

### Navigating with your Kotlin DSL graph

Finally, you can navigate from `home` to `plant_detail` using
[`NavController.navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(kotlin.Any,kotlin.Function1))
calls:  

    private fun navigateToPlant(plantId: String) {
       findNavController().navigate(route = PlantDetail(id = plantId))
    }

In `PlantDetailFragment`, you can obtain the navigation arguments by obtaining
the current
[`NavBackStackEntry`](https://developer.android.com/reference/kotlin/androidx/navigation/NavBackStackEntry)
and calling
[`toRoute`](https://developer.android.com/reference/kotlin/androidx/navigation/NavBackStackEntry#(androidx.navigation.NavBackStackEntry).toRoute())
on it to obtain the route instance.  

    val plantDetailRoute = findNavController().getBackStackEntry<PlantDetail>().toRoute<PlantDetail>()
    val plantId = plantDetailRoute.id

If `PlantDetailFragment` is using a `ViewModel`, obtain the route instance using
[`SavedStateHandle.toRoute`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle#(androidx.lifecycle.SavedStateHandle).toRoute(kotlin.collections.Map)).  

    val plantDetailRoute = savedStateHandle.toRoute<PlantDetail>()
    val plantId = plantDetailRoute.id

The rest of this guide describes common navigation graph elements, destinations,
and how to use them when building your graph.

## Destinations

The Kotlin DSL provides built-in support for three destination types:
`Fragment`, `Activity`, and `NavGraph` destinations, each of which has its own
inline extension function available for building and configuring the
destination.

### Fragment destinations

The
[`fragment()`](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.navigation.NavGraphBuilder).fragment(kotlin.collections.Map,kotlin.Function1))
DSL function can be parameterized with the fragment class for the UI and the
route type used to uniquely identify this destination, followed by a lambda
where you can provide additional configuration as described in the [Navigating
with your Kotlin DSL graph](https://developer.android.com/guide/navigation/design/kotlin-dsl#navigate) section.  

    fragment<MyFragment, MyRoute> {
       label = getString(R.string.fragment_title)
       // custom argument types, deepLinks
    }

### Activity destination

The
[`activity()`](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraphBuilder).activity(kotlin.collections.Map,kotlin.Function1))
DSL function takes a type parameter for the route but is not parameterized to
any implementing activity class. Instead, you set an optional `activityClass` in
a trailing lambda. This flexibility lets you define an activity destination for
an activity that should be launched using an [implicit
intent](https://developer.android.com/guide/components/intents-filters#ExampleSend), where an explicit
activity class wouldn't make sense. As with fragment destinations, you can also
configure a label, custom arguments, and deep links.  

    activity<MyRoute> {
       label = getString(R.string.activity_title)
       // custom argument types, deepLinks...

       activityClass = MyActivity::class
    }

### Navigation graph destination

The
[`navigation()`](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(androidx.navigation.NavGraphBuilder).navigation(kotlin.Any,kotlin.collections.Map,kotlin.Function1))
DSL function can be used to build a [nested navigation
graph](https://developer.android.com/guide/navigation/navigation-nested-graphs). This function takes a type
parameter for the route to assign to this graph. It also takes two arguments:
the route of the starting destination of the graph, and a lambda to further
configure the graph. Valid elements include other destinations, custom argument
types, deep links, and a [descriptive label for the
destination](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#label()).
This label can be useful for binding the navigation graph to UI components using
[`NavigationUI`](https://developer.android.com/guide/navigation/navigation-ui).  

    @Serializable data object HomeGraph
    @Serializable data object Home

    navigation<HomeGraph>(startDestination = Home) {
       // label, other destinations, deep links
    }

### Supporting custom destinations

If you're using a [new destination type](https://developer.android.com/guide/navigation/navigation-add-new)
that does not directly support the Kotlin DSL, you can add these destinations to
your Kotlin DSL using
[`addDestination()`](https://developer.android.com/reference/androidx/navigation/NavGraph#addDestination(androidx.navigation.NavDestination)):  

    // The NavigatorProvider is retrieved from the NavController
    val customDestination = navigatorProvider[CustomNavigator::class].createDestination().apply {
        route = Graph.CustomDestination.route
    }
    addDestination(customDestination)

As an alternative, you can also use the unary plus operator to add a newly
constructed destination directly to the graph:  

    // The NavigatorProvider is retrieved from the NavController
    +navigatorProvider[CustomNavigator::class].createDestination().apply {
        route = Graph.CustomDestination.route
    }

### Providing destination arguments

Destination arguments can be defined as part of the route class. These can be
defined the same way you would for any Kotlin class. Required arguments are
defined as non-nullable types and optional arguments are defined with default
values.

The underlying mechanism for representing routes and their arguments is string
based. Using strings to model routes allows navigation state to be stored and
restored from disk during [configuration
changes](https://developer.android.com/guide/topics/resources/runtime-changes) and [system-initiated process
death](https://developer.android.com/topic/libraries/architecture/saving-states#options). For this reason,
each navigation argument needs to be serializable, that is, it should have a
method that converts the in-memory representation of the argument value to a
`String`.

The [Kotlin serialization
plugin](https://kotlinlang.org/docs/serialization.html)
automatically generates serialization methods for [basic
types](https://kotlinlang.org/docs/basic-types.html) when the
`@Serializable` annotation is added to an object.  

    @Serializable
    data class MyRoute(
      val id: String,
      val myList: List<Int>,
      val optionalArg: String? = null
    )

    fragment<MyFragment, MyRoute>

#### Providing custom types

For custom argument types, you'll need to provide a custom `NavType` class. This
lets you control exactly how your type is parsed from a route or deep link.

For example, a route used to define a search screen could contain a class that
represents the search parameters:  

    @Serializable
    data class SearchRoute(val parameters: SearchParameters)

    @Serializable
    @Parcelize
    data class SearchParameters(
      val searchQuery: String,
      val filters: List<String>
    )

A custom `NavType` could be written as:  

    val SearchParametersType = object : NavType<SearchParameters>(
      isNullableAllowed = false
    ) {
      override fun put(bundle: Bundle, key: String, value: SearchParameters) {
        bundle.putParcelable(key, value)
      }
      override fun get(bundle: Bundle, key: String): SearchParameters {
        return bundle.getParcelable(key) as SearchParameters
      }

      override fun serializeAsValue(value: SearchParameters): String {
        // Serialized values must always be Uri encoded
        return Uri.encode(Json.encodeToString(value))
      }

      override fun parseValue(value: String): SearchParameters {
        // Navigation takes care of decoding the string
        // before passing it to parseValue()
        return Json.decodeFromString<SearchParameters>(value)
      }
    }

This can then be used in your Kotlin DSL like any other type:  

    fragment<SearchFragment, SearchRoute>(
        typeMap = mapOf(typeOf<SearchParameters>() to SearchParametersType)
    ) {
        label = getString(R.string.plant_search_title)
    }

When navigating to the destination, create an instance of your route:  

    val params = SearchParameters("rose", listOf("available"))
    navController.navigate(route = SearchRoute(params))

The parameter can be obtained from the route in the destination:  

    val searchRoute = navController().getBackStackEntry<SearchRoute>().toRoute<SearchRoute>()
    val params = searchRoute.parameters

## Deep links

Deep links can be added to any destination, just as they can with an XML driven
navigation graph. All of the same procedures defined in [Creating a deep link
for a destination](https://developer.android.com/guide/navigation/navigation-deep-link) apply to the process
of creating a deep link using the Kotlin DSL.

When creating an [implicit deep link](https://developer.android.com/guide/navigation/navigation-deep-link)
however, you don't have an XML navigation resource that can be analyzed for
`<deepLink>` elements. Therefore, you cannot rely on placing a `<nav-graph>`
element in your `AndroidManifest.xml` file and must instead add [intent
filters](https://developer.android.com/training/app-links/deep-linking) to your activity manually. The intent
filter you supply should match the base path, action, and mimetype of
your app's deep links.

Deep links are added to a destination by calling the `deepLink` function inside
the destination's lambda. It accepts the route as a parameterized type, and a
parameter `basePath` for the base path of the URL used for the deep link.

You can also add an action and mimetype using the
[`deepLinkBuilder`](https://developer.android.com/reference/kotlin/androidx/navigation/NavDeepLinkDslBuilder)
trailing lambda.

The following example creates a deep link URI for the `Home` destination.  

    @Serializable data object Home

    fragment<HomeFragment, Home>{
      deepLink<Home>(basePath = "www.example.com/home"){
        // Optionally, specify the action and/or mime type that this destination
        // supports
        action = "android.intent.action.MY_ACTION"
        mimeType = "image/*"
      }
    }

### URI format

The deep link URI format is automatically generated from the route's fields
using the following rules:

- Required parameters are appended as *path parameters* (example: `/{id}`)
- Parameters with a default value (optional parameters) are appended as *query
  parameters* (example: `?name={name}`)
- Collections are appended as *query parameters* (example: `?items={value1}&items={value2}`)
- The order of parameters matches the order of the fields in the route

For example, the following route type:  

    @Serializable data class PlantDetail(
      val id: String,
      val name: String,
      val colors: List<String>,
      val latinName: String? = null,
    )

has a generated URI format of:

`basePath/{id}/{name}/?colors={color1}&colors={color2}&latinName={latinName}`

There is no limit to the number of deep links you can add. Each time you call
[`deepLink()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestinationBuilder#deepLink(kotlin.String))
a new deep link is appended to a list that is maintained for that destination.

## Limitations

The [Safe Args](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args) plugin is
incompatible with the Kotlin DSL, as the plugin looks for XML resource files to
generate `Directions` and `Arguments` classes.