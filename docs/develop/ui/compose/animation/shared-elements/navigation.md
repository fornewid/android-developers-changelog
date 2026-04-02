---
title: Shared elements with Navigation Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/animation/shared-elements/navigation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Shared elements with Navigation Compose Stay organized with collections Save and categorize content based on your preferences.



To use shared elements with the [`navigation-compose` dependency](/jetpack/compose/navigation), use the
`Modifier.sharedElement()` that takes an `AnimatedVisibilityScope` as a
parameter. You can use this to decide what should be visible and when.

[

](/static/develop/ui/compose/images/animations/shared-element/nav_snacks_shorter.mp4)

**Figure 1.** Navigation Compose with shared elements.

The following is an example of using `navigation-compose` with shared elements:

```
@Preview
@Composable
fun SharedElement_PredictiveBack() {
    SharedTransitionLayout {
        val navController = rememberNavController()
        NavHost(
            navController = navController,
            startDestination = "home"
        ) {
            composable("home") {
                HomeScreen(
                    this@SharedTransitionLayout,
                    this@composable,
                    { navController.navigate("details/$it") }
                )
            }
            composable(
                "details/{item}",
                arguments = listOf(navArgument("item") { type = NavType.IntType })
            ) { backStackEntry ->
                val id = backStackEntry.arguments?.getInt("item")
                val snack = listSnacks[id!!]
                DetailsScreen(
                    id,
                    snack,
                    this@SharedTransitionLayout,
                    this@composable,
                    {
                        navController.navigate("home")
                    }
                )
            }
        }
    }
}

@Composable
fun DetailsScreen(
    id: Int,
    snack: Snack,
    sharedTransitionScope: SharedTransitionScope,
    animatedContentScope: AnimatedContentScope,
    onBackPressed: () -> Unit
) {
    with(sharedTransitionScope) {
        Column(
            Modifier
                .fillMaxSize()
                .clickable {
                    onBackPressed()
                }
        ) {
            Image(
                painterResource(id = snack.image),
                contentDescription = snack.description,
                contentScale = ContentScale.Crop,
                modifier = Modifier
                    .sharedElement(
                        sharedTransitionScope.rememberSharedContentState(key = "image-$id"),
                        animatedVisibilityScope = animatedContentScope
                    )
                    .aspectRatio(1f)
                    .fillMaxWidth()
            )
            Text(
                snack.name, fontSize = 18.sp,
                modifier =
                Modifier
                    .sharedElement(
                        sharedTransitionScope.rememberSharedContentState(key = "text-$id"),
                        animatedVisibilityScope = animatedContentScope
                    )
                    .fillMaxWidth()
            )
        }
    }
}

@Composable
fun HomeScreen(
    sharedTransitionScope: SharedTransitionScope,
    animatedContentScope: AnimatedContentScope,
    onItemClick: (Int) -> Unit,
) {
    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .padding(8.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        itemsIndexed(listSnacks) { index, item ->
            Row(
                Modifier.clickable {
                    onItemClick(index)
                }
            ) {
                Spacer(modifier = Modifier.width(8.dp))
                with(sharedTransitionScope) {
                    Image(
                        painterResource(id = item.image),
                        contentDescription = item.description,
                        contentScale = ContentScale.Crop,
                        modifier = Modifier
                            .sharedElement(
                                sharedTransitionScope.rememberSharedContentState(key = "image-$index"),
                                animatedVisibilityScope = animatedContentScope
                            )
                            .size(100.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        item.name, fontSize = 18.sp,
                        modifier = Modifier
                            .align(Alignment.CenterVertically)
                            .sharedElement(
                                sharedTransitionScope.rememberSharedContentState(key = "text-$index"),
                                animatedVisibilityScope = animatedContentScope,
                            )
                    )
                }
            }
        }
    }
}

data class Snack(
    val name: String,
    val description: String,
    @DrawableRes val image: Int
)

SharedElementsWithNavigationSnippets.kt
```

## Predictive back with shared elements

To use [predictive back](/guide/navigation/custom-back/predictive-back-gesture) with shared elements, follow these steps:

1. Use the latest [`navigation-compose` dependency](/develop/ui/compose/navigation), using the snippet from
   the preceding section.

   ```
   dependencies {
       def nav_version = "2.8.0-beta02"

       implementation "androidx.navigation:navigation-compose:$nav_version"
   }
   ```
2. Enable the [Predictive back setting](/guide/navigation/custom-back/predictive-back-gesture#dev-option) in developer options.
3. Add `android:enableOnBackInvokedCallback="true"` to your `AndroidManifest.xml`
   file:

   ```
   <manifest xmlns:android="http://schemas.android.com/apk/res/android">
     <uses-permission android:name="android.permission.INTERNET" />
     <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
     <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"
         android:maxSdkVersion="28" />

     <application
         android:allowBackup="true"
         android:icon="@mipmap/ic_launcher"
         android:label="@string/app_name"
         android:roundIcon="@mipmap/ic_launcher_round"
         android:supportsRtl="true"
         android:enableOnBackInvokedCallback="true"
         android:theme="@style/Theme.Snippets">
   ```

[

](/static/develop/ui/compose/images/animations/shared-element/predictive_back_shared_element_snacks_shorter.mp4)

**Figure 2.** Navigation Compose with predictive back.

[Previous

arrow\_back

Common use cases](/develop/ui/compose/animation/shared-elements/common-use-cases)

[Next

Additional samples

arrow\_forward](/develop/ui/compose/animation/shared-elements/additional-samples)