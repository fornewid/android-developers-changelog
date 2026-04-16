---
title: https://developer.android.com/blog/posts/bringing-androidify-to-xr-with-the-jetpack-xr-sdk
url: https://developer.android.com/blog/posts/bringing-androidify-to-xr-with-the-jetpack-xr-sdk
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Bringing Androidify to XR with the Jetpack XR SDK

###### 9-min read

![](https://developer.android.com/static/blog/assets/xr_Week6_1e2e4ab4ae_e4Cvs.webp) 22 Oct 2025 [![](https://developer.android.com/static/blog/assets/unnamed_2fdf36b3fa_1F9de3.webp)](https://developer.android.com/blog/authors/dereck-bridie) [##### Dereck Bridie](https://developer.android.com/blog/authors/dereck-bridie)

###### Developer Relations Engineer

[*Samsung Galaxy XR is here*](https://android-developers.googleblog.com/2025/10/giving-your-apps-new-home-on-samsung.html)*, powered by Android XR! This blog post is part of our *[*Android XR Spotlight Week*](https://android-developers.googleblog.com/2025/10/welcome-to-android-xr-spotlight-week.html)*, where we provide resources---blog posts, videos, sample code, and more---all designed to help you learn, build, and prepare your apps for Android XR.*

With the [launch of Samsung Galaxy XR](https://android-developers.googleblog.com/2025/10/giving-your-apps-new-home-on-samsung.html) , the first device powered by Android XR is officially here. People can now enjoy many of their favorite apps from the Play Store in a whole new dimension: the third dimension!

The third dimension is a spacious one, with plenty of room for your apps too. Get started today using [whichever tools work for your app](https://developer.android.com/develop/xr/get-started#select-development). For example, you can use the [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk) to build immersive XR experiences using modern Android development tools such as Kotlin and Compose.

In this blog post, we'll tell you about our own journey as we brought the whimsy of our beloved [Androidify app](https://android-developers.googleblog.com/2025/05/androidify-building-ai-driven-experiences-jetpack-compose-gemini-camerax.html) to XR, and we'll cover the basics of what it takes to bring your apps to XR too.

**A tour through Androidify**

Androidify is an open source app that lets you create Android bots, using some of the latest technologies like Gemini, CameraX, Navigation 3, and of course, Jetpack Compose. Androidify was initially designed to look great on phones, foldables, and tablets by creating [adaptive layouts](https://developer.android.com/adaptive-apps).
![customize.png](https://developer.android.com/static/blog/assets/customize_f193e77d06_ZdNHdf.webp)

*Androidify looks great across multiple form factors*

A key pillar of adaptive layouts is reusable composables. Jetpack Compose helps you create bite-sized UI components that can be laid out in different ways to create intuitive user experiences, no matter what type of device the user is on. In fact, Androidify is compatible with Android XR with zero modifications to the app!
![customize_2.png](https://developer.android.com/static/blog/assets/customize_2_d96b6262eb_pG1B2.webp)

*Androidify adapts to XR using its large-screen-responsive layout with no code changes*

Apps that have no special handling for Android XR can be multi-tasked in an appropriately sized window and work much like they would on a large screen. Because of this, Androidify is already fully featured on Android XR with no additional work! But we didn't want to stop there, so we decided to go the extra mile and create an XR-differentiated app to bring a delightful experience to our XR users.

**Orienting yourself in XR**

Let's go over key basic concepts for Android XR, starting with the two modes apps can be run in: Home Space and Full Space.
![homespace.png](https://developer.android.com/static/blog/assets/homespace_cd0f028f26_16G2ol.webp) Apps in Home Space ![homespace2.png](https://developer.android.com/static/blog/assets/homespace2_0ff1119102_PpJyR.webp) App in Full Space

In *Home Space*, multiple apps can be run side-by-side so users can multitask across different windows. In that sense, it's a lot like desktop windowing on a large screen Android device, but in virtual space!

In *Full Space*, the app has no space boundaries and can make use of Android XR's full spatial features, like spatial UI and controlling the virtual environment.

While it might seem tempting to make your app run only in Full Space, your users might want to multi-task with your app, so supporting both promotes a better user experience.

**Designing for Androidify's new dimension**

A delightful app starts with a great design. Ivy Knight, Senior Design Advocate on Android DevRel, took on the task of taking existing designs for Androidify and coming up with a new design for XR. Take it away, Ivy!

Designing for XR required a unique approach, but actually still had a lot in common with mobile design. We started by thinking about containment: how to organize and group our UI elements in subspace, either by clearly showing boundaries or by subtly implying them. We also learned to embrace all the various sizes of spatial UI elements, which are meant to adjust and move in response to the user. As we did with Androidify, [build with adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive), so you can break your layouts down into parts for your spatial UI.

**Starting the design with Home Space**

Luckily, Android XR lets you start with your app as it is today for Home Space, so we could transition to the expanded XR designs by just adding a window toolbar and Full Space transition button.

We also considered possible hardware features and how the user would interact with them. The mobile layouts for Androidify adapt across various postures, class sizes, and the number of cameras to give more photo options. Following this model, we had to adapt the camera layout for headset devices as well. We also needed to make [adjustments for text to work](https://developer.android.com/design/ui/xr/guides/visual-design#xr-typography) to account for the proximity of the UI to the user.

**Designing for the bigger shift to Full Space**

[Full Space](https://developer.android.com/design/ui/xr/guides/foundations#full-space) was the biggest shift, but gave us the most creative room to adapt our design.
![tablet_to_xr.webp](https://developer.android.com/static/blog/assets/tablet_to_xr_2c9197db81_1QUPDc.webp) From tablet to XR

Androidify uses visual containment, or panes, to group features with a background and outline, like the "Take or choose a photo" pane. We also used components like the [top app bar](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#top-app-bars) to create natural containment by framing the other panes. Finally, intrinsic containment is suggested by the proximity of certain elements to others, such as the "Start transformation" bottom button, which is near the "Choose my bot color" pane.

[Spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels) made for easy separation. To decide how to adapt your mobile designs for spatial panels, try removing surfaces starting with the surface that is the furthest back and then moving forward. See how many backgrounds you can remove and what remains. After we did this exercise for Androidify, the large green Android squiggle was what remained. The squiggle not only acted as a branding moment and background, but an anchor for the content in 3D space.

Establishing this anchor both made it easier to imagine how elements could move around it, and how we could use proximity to break out and translate the rest of the user experience.

**Other design tips for helping your app get spatial**

- **Let things be uncontained**: Break out components and give them some real (spatial) space. It's time to give those UI elements some breathing space.
- **Remove surfaces**: Hide the background, see what that does to your designs.
- **Motivate with motion**: How are you using transitions in your app? Use that character to imagine your app breaking out into VR.
- **Choose an anchor**: Don't lose your users in the space. Have an element that helps collect or ground the UI.

For more about XR UI design patterns, check out [Design for Android XR on Android Developers](https://developer.android.com/design/ui/xr).

**Spatial UI basics**

Now that we've covered Ivy's experience adapting her mindset while designing Androidify for XR, let's talk about developing spatial UI. Developing a spatial UI with the [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk) should seem familiar if you're used to working with modern Android tools and libraries. You'll find concepts you're already familiar with, like creating layouts with Compose. In fact, spatial layouts are really similar to 2D layouts using rows, columns, and spacers:
![spatialrows.png](https://developer.android.com/static/blog/assets/spatialrows_e2bbf24319_ZQrcce.webp)

*These elements are arranged in *`*SpatialRows*`* and *`*SpatialColumns*`

The spatial elements shown here are [SpatialPanel](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/package-summary#SpatialPanel(androidx.xr.compose.subspace.layout.SubspaceModifier,androidx.xr.compose.subspace.layout.SpatialShape,androidx.xr.compose.subspace.DragPolicy,androidx.xr.compose.subspace.ResizePolicy,kotlin.Function0)) composables, which let you display 2D content like text, buttons, and videos.

```
Subspace {
    SpatialPanel(
        SubspaceModifier
            .height(824.dp)
            .width(1400.dp)
    ) {
        Text("I'm a panel!")
    }
}
```

A SpatialPanel is a *subspace composable*. Subspace composables must be contained within a Subspace, and are modified by `SubspaceModifier` objects. Subspaces can be placed anywhere within your app's UI hierarchy, and can only contain Subspace composables. [SubspaceModifier objects](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspacemodifiers) are also really similar to Modifier objects: they control parameters like sizing and positioning.

An `Orbiter`* *can be attached to a `SpatialPanel` and move along with the content it's attached to. They're often used to provide contextual controls about the content they're attached to, giving the content the primary focus. They can be placed at any of the four sides of the content, at a configurable distance.
![orbiter.png](https://developer.android.com/static/blog/assets/orbiter_511f360873_22MELU.webp) An Orbiter is attached to the bottom of a SpatialPanel

There are [many more spatial UI elements](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui), but these are the main ones we used to create spatial layouts for Androidify.

**Getting started with XR development**

Let's start with the project setup. We added the Jetpack XR Compose dependency, which you can find on the [Jetpack XR dependencies](https://developer.android.com/develop/xr/jetpack-xr-sdk/getting-started) page.

We added code for a button that transitions the user into Full Space, starting with detecting the capability to do so:

```
@Composable
fun couldRequestFullSpace(): Boolean =
   LocalSpatialConfiguration.current.hasXrSpatialFeature && 
   !LocalSpatialCapabilities.current.isSpatialUiEnabled
}
```

Then, we made a new button component that uses the [Expand Content icon](https://fonts.google.com/icons?selected=Material+Symbols+Outlined:expand_content:FILL@0;wght@400;GRAD@0;opsz@24&icon.query=expand+content&icon.size=24&icon.color=%2300000) to our existing layouts, and gave it an onClick behavior:

```
@Composable

fun RequestFullSpaceIconButton() {
   if (!couldRequestFullSpace()) return
   val session = LocalSession.current ?: return

   IconButton(
       onClick = {
           session.scene.requestFullSpaceMode()
       },
   ) {
       Icon(
           imageVector =  
               vectorResource(R.drawable.expand_content_24px),
           contentDescription = 
               stringResource("To Full Space"),
       )
   }
}
```

Now, clicking that button just shows the Medium layout in Full Space. We can check the spatial capabilities and determine if spatial UI can be displayed -- in that case, we'll show our new spatial layout instead:

```
@Composable

fun HomeScreenContents(layoutType: HomeScreenLayoutType) {
   val layoutType = when {
      LocalSpatialCapabilities.current.isSpatialUiEnabled -> 
          HomeScreenLayoutType.Spatial
      isAtLeastMedium() -> HomeScreenLayoutType.Medium
      else -> HomeScreenLayoutType.Compact
   }

   when (layoutType) {
      HomeScreenLayoutType.Compact ->
          HomeScreenCompactPager(...)

      HomeScreenLayoutType.Medium ->
          HomeScreenMediumContents(...)

      HomeScreenLayoutType.Spatial ->
          HomeScreenContentsSpatial(...)
   }
}
```

**Implementing the design for the Home Screen**

Let's go back to the spatial design for the Home Screen in Full Space to understand how it was implemented.
![customize_3.png](https://developer.android.com/static/blog/assets/customize_3_b59e9428e8_QK9TK.webp)

We identified two SpatialPanel elements here: one panel that the video card is in on the right, and one that contains the main UI. Finally, there's an Orbiter attached to the top. Let's start with the video player panel:

```
@Composable
fun HomeScreenContentsSpatial(...) {
   Subspace {
      SpatialPanel(SubspaceModifier
                   .fillMaxWidth(0.2f)
                   .fillMaxHeight(0.8f)
                   .aspectRatio(0.77f)
                   .rotate(0f, 0f, 5f),
      ) {
          VideoPlayer(videoLink)
      }
   }
}
```

We simply reused the 2D VideoPlayer component from the regular layouts into a `SpatialPanel` with no additional changes! Here's what it looks like standalone:
![bluetiel.png](https://developer.android.com/static/blog/assets/bluetiel_2a543900ff_Z14Ob5K.webp)

The main content panel followed the same story: we reused medium panel content in a `SpatialPanel`.

```
SpatialPanel(SubspaceModifier.fillMaxSize(),
             resizePolicy = ResizePolicy(
                 shouldMaintainAspectRatio = true
             ),
             dragPolicy = MovePolicy()
) {
    Box {
        FillBackground(R.drawable.squiggle_full)
        HomeScreenSpatialMainContent(...)
    }
}
```

We gave this panel a ResizePolicy, which gives the panel some handles near the edges that let the user resize the panel. It also has a MovePolicy, which lets the user drag it around.
![customize_4.png](https://developer.android.com/static/blog/assets/customize_4_c9dbdcece9_19Bwnt.webp)

Placing them in the same Subspace makes them independent of each other, so we made the VideoPlayer panel a child of the main content panel. This makes the VideoPlayer panel move when the main content panel is dragged through a parent-child relationship.

```
@Composable
fun HomeScreenContentsSpatial(...) {
   Subspace {
       SpatialPanel(SubspaceModifier..., resizePolicy, dragPolicy) {
           Box {
               FillBackground(R.drawable.squiggle_full)
               HomeScreenSpatialMainContent(...)
           }
           Subspace {
              SpatialPanel(SubspaceModifier...) {
                  VideoPlayer(videoLink)
              }
           }
       }
   }
}
```

That's how we did the first screen!

**Moving on to the other screens**

I'll go over some of the other screens briefly too, highlighting specific considerations made for each one.
![fullspace.png](https://developer.android.com/static/blog/assets/fullspace_385f4fedd1_1MPgw3.webp) The creation screen in Full Space

Here, we used SpatialRow and SpatialColumn composables to create a layout that fits the recommended viewing space, again reusing components from the Medium layout.
![fullspace_2.png](https://developer.android.com/static/blog/assets/fullspace_2_08248eb67e_Z1jz8TL.webp)

Results Screen in Full Space: *A bot generated with a prompt: red baseball cap, aviator sunglasses, a light blue t-shirt, red and white checkered shorts, green flip flops, and is holding a tennis racket.*

<br />

The results screen shows the complimentary quotes using a feathering effect, allowing them to fade out near the edges of the screen. It also uses an actual 3D transition when viewing the input that was used, flipping the picture over in space.

**Publishing to the Google Play Store**

Now that the app is ready for XR with the spatial layouts, we went on to release it onto the Play Store. There's one final, important change we made to the app's AndroidManifest.xml file:

```
<!-- Androidify can use XR features if they're available; they're not required. -->
<uses-feature android:name="android.software.xr.api.spatial" 
              android:required="false" />
```

This lets the Play Store know that this app has XR-differentiated features, showing a badge that lets users know that the app was made with XR in mind:
![androidify2.png](https://developer.android.com/static/blog/assets/androidify2_e1a4f46a6c_pdEDq.webp) Androidify as shown in the Google Play Store on Android XR

<br />

When uploading the release, we don't need any special steps to release for XR: the same app is distributed as normal to users on the mobile track as to users on an XR device! However, you can choose to add XR-specific screenshots of your app, or even upload an immersive preview of your app using a spatial video asset. On Android XR devices, the Play Store automatically displays this as an immersive 3D preview, allowing users to experience the depth and scale of your content before they install the app.

**Start building your own experiences today**

Androidify is a great example of how to spatialize an existing 2D Jetpack Compose app. Today, we showed the full process of developing a spatial UI for Androidify, from design to code to publishing. We modified the existing designs to work with spatial paradigms, used SpatialPanel and Orbiter composables to create spatial layouts that show when the user enters Full Space, and finally, released the new version of the app onto the Play Store.

We hope that this blog post helped you understand how you can bring your own apps to Android XR! Here's a few more links that can help you on your way:

- Check out the [source code for Androidify](https://github.com/android/androidify), and make your own bot using [Androidify on Google Play](https://play.google.com/store/apps/details?id=com.android.developers.androidify).
- [Get started with our developer documentation](https://developer.android.com/develop/xr/get-started) and learn more about [Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui).
- [Download the Android XR emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/studio-tools) and try your own app out!

###### Written by:

-

  ## [Dereck Bridie](https://developer.android.com/blog/authors/dereck-bridie)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/dereck-bridie) ![](https://developer.android.com/static/blog/assets/unnamed_2fdf36b3fa_1F9de3.webp) ![](https://developer.android.com/static/blog/assets/unnamed_2fdf36b3fa_1F9de3.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](https://developer.android.com/blog/authors/ivy-knight) 02 Dec 2025 02 Dec 2025 ![](https://developer.android.com/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow_forward](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app) We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 20 Nov 2025 20 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Leveling Guide for your Performance Journey](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey)

  [arrow_forward](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey) The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  9 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)