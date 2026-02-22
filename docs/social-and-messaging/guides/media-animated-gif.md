---
title: https://developer.android.com/social-and-messaging/guides/media-animated-gif
url: https://developer.android.com/social-and-messaging/guides/media-animated-gif
source: md.txt
---

Animated GIFs enhance communication and self expression, adding a dynamic and
engaging element to conversations that allow users to convey emotions,
reactions, and humor more effectively than static images or text alone.
The popularity of GIFs in online culture makes their integration essential
for staying relevant and appealing to users who expect modern features and a
rich multimedia experience.

## Display an animated GIF using an image loading library

Image loading libraries do a lot of the heavy lifting for you, often adding
backwards-compatible support for features such as animated GIFs. The following
code demonstrates how to implement animated GIF playback using the
[Coil image loading library](https://coil-kt.github.io/coil/):

**Add the Coil dependency for GIF:**  

    implementation("io.coil-kt:coil-gif:2.6.0")

**Create the GIF-enabled loader** using both the platform ImageDecoder, added
in Android 9 (API level 28), as well as Coil's GifDecoder for backwards compatibility:  

    val gifEnabledLoader = ImageLoader.Builder(this)
        .components {
            if ( SDK_INT >= 28 ) {
                add(ImageDecoderDecoder.Factory())
            } else {
                add(GifDecoder.Factory())
            }
        }.build()

**Use the gifEnabledLoader in your Coil AsyncImage composable:**  

    AsyncImage(
        imageLoader = gifEnabledLoader,
        ...
    )

## Display an animated GIF using Android platform support

    AsyncImage(
         model = request,
         imageLoader = videoEnabledLoader,
         contentDescription = null
     )

Android 9+ (API level 28) has built-in support for animated GIF files. With a
little help from an [Accompanist library](https://medium.com/androiddevelopers/jetpack-compose-accompanist-an-faq-b55117b02712), Jetpack Compose can
play these animations with just a few lines of code.

**Add the Accompanist library dependency to support drawable painters:**  

    implementation("com.google.accompanist:accompanist-drawablepainter:0.35.0-alpha")

**Create a method that loads the animated GIF** into an [AnimatedImageDrawable](https://developer.android.com/reference/android/graphics/drawable/AnimatedImageDrawable)
using [ImageDecoder](https://developer.android.com/reference/android/graphics/ImageDecoder):  

    private fun createAnimatedImageDrawableFromImageDecoder(context: Context, uri: Uri): AnimatedImageDrawable {
        val source = ImageDecoder.createSource(context.contentResolver, uri)
        val drawable = ImageDecoder.decodeDrawable(source)
        return drawable as AnimatedImageDrawable
    }

**Use the [rememberDrawablePainter](https://google.github.io/accompanist/api/drawablepainter/com.google.accompanist.drawablepainter/remember-drawable-painter.html) with the**
**`AnimatedImageDrawable`**:  

    Image(
        painter = rememberDrawablePainter(
            drawable = createAnimatedImageDrawableFromImageDecoder(applicationContext, mediaUri)),
         contentDescription = "animated gif"
    )

### Support GIF files from image keyboards and other rich content

Animated GIF files are popular features in many Android keyboards, including
Gboard from Google. The current recommended way to support any kind of
sticker or animation, whether it comes from the input method or from another
app, is to use an [`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener).

See [Receive rich content](https://developer.android.com/develop/ui/views/receive-rich-content) to learn more about how to implement support for
receiving GIF animations and other rich media in your app.