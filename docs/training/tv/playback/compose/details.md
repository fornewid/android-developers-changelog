---
title: Build a details screen  |  Android TV  |  Android Developers
url: https://developer.android.com/training/tv/playback/compose/details
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android TV](https://developer.android.com/training/tv)

# Build a details screen Stay organized with collections Save and categorize content based on your preferences.




Many TV apps include content detail pages with relevant metadata for a given
piece of content (i.e. a specific movie). Detail pages can be implemented as a
composable function, taking metadata of the selected content as its argument.

The following code is a typical implementation of the details screen. It
[loads an image](/jetpack/compose/graphics/images/loading#internet-loading)
of the given movie with its title and description. The user's able to make a
screen transition to the player screen, which can be triggered by clicking a
button to start movie playback. You can handle this action to make the screen
transition by setting a callback function.

```
@Composable
fun DetailsScreen(
  movie: Movie,
  modifier: Modifier = Modifier,
  onStartPlayback: (Movie) -> Unit = {}
) {
  Box(modifier = modifier.fillMaxSize()){
     AsyncImage(
       modifier = Modifier.fillMaxSize()
       model = movie.image,
       contentDescription = null,
       contentScale = ContentScale.Crop,
     )
     Column(modifier = Modifier.padding(32.dp)){
       Text(
         text = movie.title,
         style = MaterialTheme.typeography.heading2
       )
       Text(text = movie.description)
       Button(onClick = { onStartPlayBack(movie) }){
         Text(text = R.string.startPlayback)
       }
     }
  }
}
```

**Note:** `AsyncImage` is a composable to load an image from the internet.
See [Loading Images](/develop/ui/compose/graphics/images/loading#internet-loading) for details.

[Previous

arrow\_back

Create a catalog browser](/training/tv/playback/compose/browse)

[Next

Create scrollable layouts

arrow\_forward](/training/tv/playback/compose/lists)