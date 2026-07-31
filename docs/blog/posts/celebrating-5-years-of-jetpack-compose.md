---
title: https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose
url: https://developer.android.com/blog/posts/celebrating-5-years-of-jetpack-compose
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Celebrating 5 years of Jetpack Compose

5-min read ![](https://developer.android.com/static/blog/assets/Jetpack_compose_Strapi_123481f79e_Z1F9b9M.webp) 28 Jul 2026 3 Authors [Rebecca Franks,](https://developer.android.com/blog/authors/rebecca-franks) [Nick Butcher,](https://developer.android.com/blog/authors/nick-butcher) [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) Today, we officially celebrate five years since the release of Jetpack Compose 1.0. From version [1.0, announced on July 28th, 2021](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html), to our latest [1.11 release](https://android-developers.googleblog.com/2026/04/jetpack-compose-april-2026-updates.html), we've seen the APIs evolve significantly over the years, and we're taking a moment to celebrate.

When we officially announced the 1.0 release, we promised a simpler, faster, and more intuitive way to build native interfaces on Android. Looking back, it's safe to say that Compose didn't just deliver on that promise, but also completely changed the Android ecosystem, with more than 68% of the top 1,000 apps using it in production today.
[Video](https://www.youtube.com/watch?v=6qyCXugCU6w)

## History

Over the last five years, Compose has grown steadily. In the [early days](https://www.youtube.com/watch?v=VsStyq4Lzxo), we explored showing you how to build layouts with the basic Box, Row, and Column. Today, we've expanded Compose to work not just on mobile devices, but to other form factors such as [Compose for TV](https://developer.android.com/training/tv/playback/compose), [WearOS](https://developer.android.com/training/wearables/compose?version=3), [Glance for Widgets](https://developer.android.com/develop/ui/compose/glance), and even display glasses with [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer).
![jetpack_compose_everywhere.png](https://developer.android.com/static/blog/assets/jetpack_compose_everywhere_644011c17b_LvUla.webp)

We recorded an Android Developers Backstage episode with [Clara Bayarri](https://uk.linkedin.com/in/clara-bayarri-815b7333), Engineering Lead for Jetpack, and two former leads of the team, [Romain Guy](https://www.romainguy.dev/) and [Chet Haase](https://www.chethaase.com/), along with [Tor Norbye](https://www.linkedin.com/in/tor-norbye), Senior Engineering Director. In this episode, they discuss the history of Compose and the early days of development.
[Video](https://www.youtube.com/watch?v=HEqXwUm6vd0) ![timeline.png](https://developer.android.com/static/blog/assets/timeline_abf1093a92_Z1WabAH.webp) Compose highlights over the years

## Looking back

The beginnings of Compose were very different from what you know today. Two projects were happening in parallel inside the Android team.

At the time, the Views toolkit team was thinking of unbundling the UI Toolkit into a library to help with development speed, and make it easier for developers to adopt and control updates. Meanwhile, a team was working on a novel idea to build declarative layouts by embedding XML inside Kotlin, which looked something like this:
![jetpack_compose_early_code.png](https://developer.android.com/static/blog/assets/jetpack_compose_early_code_cf4e4e9b15_2rSuJf.webp)

Those two efforts merged to produce what you know today - a fully declarative UI Toolkit that utilizes the power of a compiler plugin, runtime, and Kotlin:

```kotlin
@Composable
fun Newsfeed(stories: List<Story>) {
    LazyColumn {
        items(stories) { story ->
            Card {
                val author = story.author
                Image(painterResource(author.profilePhoto),
                    contentDescription = author.name)
                Text(author.name)
                Text(story.content)
                if (story.hasCommentsEnabled()) {
                    for(comment in story.comments) {
                        Text(comment.mainContent)
                    }
                }
            }
        }
    }
}
```

And you, the community, helped us very early on! Before 2021, Compose had a pre-alpha phase, which helped ensure Compose was fit to solve the problems of our developers.

One of our favorite memories is the Android Dev Challenge. We challenged the community to build four different tasks with Compose, filling our feeds with Puppy apps, clocks, and weather apps, and giving us a ton of direct feedback that helped shape the 1.0 release.
[Video](https://www.youtube.com/watch?v=9AAmOcgdA2s)

Compose has continued to evolve, from launching with a set of Material 2 components to now supporting [Material 3 Expressive](https://m3.material.io/blog/building-with-m3-expressive).
![material2.png](https://developer.android.com/static/blog/assets/material2_dea8334b65_ZnHpUk.webp) Material 2 in Compose

## Looking ahead

As of today, Compose 1.11 is the latest version with 1.12 coming soon, offering so much more than 1.0, 5 years ago. This year, we introduced more adaptive APIs, such as [FlexBox](https://developer.android.com/develop/adaptive-apps/guides/flexbox), [Grid](https://developer.android.com/develop/adaptive-apps/guides/grid), [MediaQuery](https://developer.android.com/develop/adaptive-apps/guides/mediaquery), and [Styles](https://developer.android.com/develop/ui/compose/styles). These APIs let you advance to the next level of premium, adaptive UI development with Compose.

At Google I/O 2026, we announced that we are now [Compose-first](https://developer.android.com/develop/ui/compose/first), meaning that all future UI development will happen only in Compose, while the Views toolkit enters maintenance mode. Material Design is also [shifting focus](https://m3.material.io/blog/material-is-compose-first) entirely to Compose, signaling an end to the `findViewById era`.

## Community is at the heart of Compose

Over the years, you've inspired us with creative examples of how you've used Compose, and we'd love to highlight a few more examples of where we've seen exciting work. JetBrains has been a great partner for Google with Compose, expanding Compose to work across platforms with [Compose Multiplatform](https://kotlinlang.org/compose-multiplatform/) and enabling desktop, iOS, and web developers to also enjoy the benefits of Compose.

We've really enjoyed following our most beloved newsletters from [JetpackCompose.app's Dispatch](https://www.jetpackcompose.app/newsletter), [AndroidWeekly](https://androidweekly.net/), to [jetc](https://jetc.dev/) - helping Android Developers stay up-to-date with the latest in the world of Compose and Android.

Another standout contributor is [sinasamaki](https://www.sinasamaki.com/). They've created many delightful experiences using Compose, such as this fun ribbon modifier and the glitchy effect:
![ribbon_modifier_sinasamaki.gif](https://developer.android.com/static/blog/assets/ribbon_modifier_sinasamaki_78f5da0296_Z1oSbMA.webp)

[Saket Narayan](https://github.com/saket) has also always been an inspiration when it comes to creating useful tools for Compose, such as [telephoto](https://github.com/saket/telephoto), a library featuring support for pan and zoom gestures and automatic sub-sampling of large images, or the latest library, [Touch Robot](https://github.com/saket/touch-robot), which allows you to easily test interaction animations:

|---|---|
| ```kotlin paparazzi.gif(end = 3_000) { DebitCard( Modifier.testTag("card") ) val touchRobot = rememberTouchRobot() LaunchedEffect(Unit) { touchRobot.onNode(hasTestTag("card")).performGesture { draw( path = createAndroidHeadPath(), duration = 3.seconds, ) } } } /** A path drawing the Android head. */ fun createAndroidHeadPath(bounds: Rect): Path = TODO() ``` | ![saket_touch_robot.gif](https://developer.android.com/static/blog/assets/saket_touch_robot_2618c77371_ZSWECt.webp) |

[Jake Wharton](https://jakewharton.com/), who has used Compose in innovative ways (like [molecule](https://github.com/cashapp/molecule), and even building UI with Compose for the terminal with [mosaic](https://github.com/JakeWharton/mosaic)). Chris Banes, who has built many Compose libraries over the years, with our most recent favourite - [Haze](https://github.com/chrisbanes/haze) for background blurring, and many of the [Android Google Developer Experts](https://developers.google.com/community/experts) like [Akshay Chordiya](https://github.com/AkshayChordiya), [Huyen Tue Dao](https://www.randomlytyping.com/), and [Katie Barnett](https://katiebarnett.dev/), who've contributed to the success of Compose. But this is not about selecting individuals - there have been so many great contributors to the Compose codebase, and many of you continue to inspire us with your fun examples, libraries, and in-depth talks. Without the community, Jetpack Compose wouldn't be as successful as it is today.

## Cheers to the next 5 years, and more!

Jetpack Compose has grown from an experimental idea into the standard for Android UI Development. Thank you to the entire Toolkit team at Google, and to the incredible global developer community that wrote libraries, filed bugs, and pushed the boundaries of what declarative UI can do.

This week, we'll be celebrating with some in-person birthday parties across the globe, and a live "Birthday party" on the [Android Developers YouTube channel](https://www.youtube.com/user/androiddevelopers) on July 30th at 13:00 UTC. During this time, we'll hang out and discuss Compose and answer your questions!

Cheers to the next 5 years, and happy composing!
Written by:

-

  ## [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/rebecca-franks) ![View Rebecca Franks's profile](https://developer.android.com/static/blog/assets/unnamed_12_b05cc1bf55_ZVxp9e.webp) ![View Rebecca Franks's profile](https://developer.android.com/static/blog/assets/unnamed_12_b05cc1bf55_ZVxp9e.webp)
-

  ## [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/nick-butcher) ![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp) ![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)
-

  ## [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston)

  ###### Product Marketing Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/loryn-hairston) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_Z1Y5zeh.webp) ![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_Z1Y5zeh.webp)
Continue reading
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Compose_first_Meta_04fd0498ba_1T1vC6.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android UI Development is Compose First](https://developer.android.com/blog/posts/android-ui-development-is-compose-first)

  [arrow_forward](https://developer.android.com/blog/posts/android-ui-development-is-compose-first) In the almost-5-years since Jetpack Compose launched, we've invested in bringing you all the features, performance and tools that you need to build amazing UIs across the variety of Android devices.
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 2 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 03 Dec 2025 03 Dec 2025 ![](https://developer.android.com/static/blog/assets/jetpack_Compose_99733114d6_Z2c0xrB.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose December '25 release](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-december-release)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-december-release) Today, the Jetpack Compose December '25 release is stable. This contains version 1.10 of the core Compose modules and version 1.4 of Material 3, adding new features and major performance improvements.
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 6 min read
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 29 Jul 2026 29 Jul 2026 ![](https://developer.android.com/static/blog/assets/Google_Play_Age_Signals_API_Blog_Strapi_d532f6c0b8_Z298Ads.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Delivering safer, age-appropriate experiences on Google Play](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/delivering-safer-age-appropriate-experiences-on-google-play) Providing a safe online experience and protecting users from harm is a top priority at Google Play.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 2 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)