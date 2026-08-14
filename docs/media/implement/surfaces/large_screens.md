---
title: https://developer.android.com/media/implement/surfaces/large_screens
url: https://developer.android.com/media/implement/surfaces/large_screens
source: md.txt
---

Android devices come in a variety of form factors---phones, tablets, foldables,
ChromeOS devices---which have a wide range of screen sizes. Android supports many
display modes, including multi-window, multi-display, free-form, and
picture-in-picture. Foldable devices can be in various states or postures,
such as tabletop or book.

Consider different use cases for your app as you begin to design it. For
example:

- Large Screen devices give users more room to engage with your media app's
  content in different ways.

- Users might multitask while watching a video in a multi-window configuration or
  take advantage of the larger screen to apply more complex edits after capturing
  an image.

- Users might turn to a tablet to stay connected with video calls and see their
  friends and family in greater detail. Your app can display richer context about
  a title or scene in a custom playback overlay or offer more control options
  on-screen.

- Carousels in a browsing view can feature more variety for greater visual appeal,
  or your media app can keep users engaged by offering a browsable feed side by
  side with playback.

Keep in mind that your media app has the same code running on a standard phone,
a foldable, a tablet, and ChromeOS devices, so you should design for large
screens from the very beginning of your app development. For more information
and visual examples, see [Large screen gallery](https://developer.android.com/large-screens/gallery).

## Make your media app responsive by default

Avoid broken user experiences in your media app by making your app's layout
adaptive across phones, tablets, foldables, and ChromeOS devices.

Your app should be responsive to account for different display sizes,
orientations, and form factors. An adaptive layout changes based on the display
space available to it. For more information, see [Support different display sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes).

### Design according to guidelines

Core app quality is the basis of all Android apps regardless of display size,
device posture, or other device-specific considerations. Your app should meet
these basic requirements before you start designing for a large screen. For
more information, see [Core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality).

Your app should offer an excellent user experience regardless of device form
factor, screen size, display mode, or posture, so design your app according to
the following Tier 1, 2, and 3 guidelines.

The guidelines define a comprehensive set of quality requirements for most
types of Android apps.

#### Tier 3:

At this basic level, your app still must adhere to the [UI and graphics](https://developer.android.com/docs/quality-guidelines/core-app-quality#ui_and_graphics)
requirements. Your app is large screen ready, and users can complete critical
task flows but with a less than optimal user experience.

The app layout might not be ideal, but it does run full screen, or full window
in multi-window mode. It's not letterboxed and it doesn't run in compatibility
mode. The app provides basic support for external input devices, including
keyboard, mouse, and trackpad. For more information, see [Large screen ready](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_ready).

#### Tier 2:

Here, your app implements layout optimizations for all screen sizes and device
configurations, along with enhanced support for external input devices. For
details, see [Large screen optimized](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_optimized).

#### Tier 1:

This is the best level of support and offers the user the most excellent
experience with your app, as it specifies premium features and capabilities.

Where applicable, the app supports multitasking, foldable postures, drag, and
stylus input. At this level, apps are highly differentiated, so pay
close attention to the guidelines for such things as multi-tasking and
foldable postures. To learn more, see [Large screen differentiated](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality#large_screen_differentiated).

## Optimized layouts

Take advantage of the increased space of large screens without letterboxing
(due to restricting orientation) or stretching. By optimizing your app's layout
for media and social media, you expand your app's reach and create a better user
experience across all large screen form factors---tablets, foldables, and
ChromeOS devices---as well as support all phone sizes.

Navigation rail and drawer components provide out-of-the way navigation for UI
convenience and control. The components also complement the canonical layouts
(list-detail, feed, and supporting pane) by positioning primary navigation
destinations within close reach while occupying a minimum of screen space.

### Media layouts

Make your app more usable by implementing media-specific layouts for
list-detail, feed, and supporting pane. For information on MDX, Flutter, and
Compose layouts, see [Layout resources](https://m3.material.io/foundations/layout/canonical-layouts/overview#33e0b9eb-3075-4e29-abe9-2161644583f5).

- **List-detail:**
  Designing your app with an interactive media browser lets users browse different
  media while watching or listening. Media titles are displayed side by side with
  a playing video or audio file. If the device orientation changes, a list-detail
  layout responds to preserve the app state. To learn more, see
  [List-detail layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#list-detail).

- **Feed:**
  A feed layout arranges equivalent content elements in a configurable grid for
  quick, convenient viewing of a large amount of content, such as a music feed or
  movie and TV kiosk in your app. For more information, see [Feed layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#feed).

- **Supporting pane:**
  With primary and secondary display areas, your app can embed a supporting pane
  for context, relevance, or reference, such as a scrolling list of similar
  titles, published reviews, or additional works by the same artists or actors.
  For further details, see [Supporting pane layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#supporting_pane).

For a curated collection of media layouts, see [Media gallery](https://developer.android.com/large-screens/gallery/media).

### Social Media layouts

Large screens give social media users more work space to create, to multitask,
to drag content between apps, and share it. With distinctive
features and capabilities not possible on small screen devices, your large
screen media app can take advantage of list-detail, feed, and supporting pane
layouts.

- **List-detail:**
  This is ideal for messaging apps, contact managers, or file browsers. For
  example, your app can display a list of conversations side by side with details
  to stay current on the latest messages. For more information, see [List-detail layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#list-detail).

- **Feed:**
  Common components in this style of layout are cards and lists. For example,
  create a collage of posts in a flexible grid format, or use size and position
  to draw attention to prominent posts. Users can quickly view large groups of
  content. For more information, see [Feed layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#feed).

- **Supporting pane:**
  Search and reference apps or a productivity app can benefit from this style of
  layout. It keeps content creation tools close at hand for the user. For example,
  your app can let users adjust settings, access color palettes, apply effects,
  and see the changes instantly. For more information, see [Supporting pane layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts#supporting_pane).

For a curated collection of social media layouts, see [Social media gallery](https://developer.android.com/large-screens/gallery/social) page.

## Best practices for large screen media apps

Using best practices for large screens helps you avoid unnecessary reworking of
your app. They also make your app more user friendly across more devices from
the beginning, especially in regards to orientation, keyboard shortcuts, camera
preview support, and foldable postures.

### Orientation and resizing

If your media app declares orientation and resizing restrictions, Android
activates a compatibility mode. Although compatibility mode ensures your app
behaves acceptably, the usability is greatly decreased, and the user experience
suffers.

For example, if your app is on a tablet, the tablet docks in landscape
orientation. If your app is restricted to portrait, this causes letterboxing,
which is not ideal for the end user. Your app should let people use their
preferred orientation, so take advantage of the available size of a large
screen in your design.

Any restrictions to orientation reduces the way users can interact with content
or consume media, which limits the use of your app. Changing orientation can
affect sizing to some degree but resizing won't necessarily change orientation.

### Keyboard shortcuts

On a larger screen, keyboard shortcuts on physical keyboards, like start, stop,
pause, rewind, and forward, are more likely to be used, making the user
experience a consistent user experience with a keyboard.

Users expect these functions in their media apps. To lessen friction points for
users, consider testing your app with a physical keyboard. This helps you to
notice and include these important shortcuts in your app at the start of your
design.

### Camera preview support

With large screens, you can have more issues with stretching, cropping, and
rotation. So, you can't assume the size of the camera preview is what the UI in
your media app actually renders.

For example, if a user takes a picture with their tablet but on their tablet
screen it renders upside down, this is a suboptimal experience. Include camera
preview support for large screens.

For more information, see [CameraX preview](https://developer.android.com/media/camera/camerax/preview), or
[Camera2 preview](https://developer.android.com/media/camera/camera2/camera-preview).

### Foldable postures

Designing your media app for large screens includes foldable postures. Your app,
for example, can let a user have a tabletop configuration for media playback or
use a rear display and dual screen mode for previews and capturing.

With foldable postures included in your development plan, your app is available
to more devices and has a wider impact. You enlarge the media experience for
the user in ways other devices cannot do without foldable postures. For more
information, see [Foldable postures](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables).