---
title: https://developer.android.com/training/tv/playback/compose/details
url: https://developer.android.com/training/tv/playback/compose/details
source: md.txt
---

Many TV apps include content detail pages with relevant metadata for a given
piece of content (i.e. a specific movie). Detail pages can be implemented as a
composable function, taking metadata of the selected content as its argument.

The following code is a typical implementation of the details screen. It
[loads an image](https://developer.android.com/jetpack/compose/graphics/images/loading#internet-loading)
of the given movie with its title and description. The user's able to make a
screen transition to the player screen, which can be triggered by clicking a
button to start movie playback. You can handle this action to make the screen
transition by setting a callback function.  

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

| **Note:** `AsyncImage` is a composable to load an image from the internet. See [Loading Images](https://developer.android.com/develop/ui/compose/graphics/images/loading#internet-loading) for details.