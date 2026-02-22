---
title: https://developer.android.com/design/ui/xr/guides/visual-design
url: https://developer.android.com/design/ui/xr/guides/visual-design
source: md.txt
---

You can build immersive Android XR applications using OpenXR, native Android APIs, or WebXR. The visual design recommendations outlined on this page apply regardless of which platform you choose.

- **For Unity, OpenXR, or WebXR apps** : You are free to follow any design language you choose. Although the[Material Design](https://m3.material.io/)library is only accessible to Android apps, you can still follow its design recommendations to help apply colors, spacing, scale, buttons, and typography.

- **For Android apps** : 2D mobile or large-screen Android apps can take advantage of Full Space capabilities with very little additional development work. For high XR impact, consider using[spatial UI](https://developer.android.com/design/ui/xr/guides/spatial-ui). To create a more immersive app experience you can also add[3D models](https://developer.android.com/design/ui/xr/guides/3d-content)and[environments](https://developer.android.com/design/ui/xr/guides/environments)to your app.

  You can maintain the design language of existing Android apps in Android XR. For new apps or redesigns, consider following Material Design guidelines for UI size, accessibility, typography, color schemes, and components, which will give your app the benefits of Android's familiar, proven design and usability.

  If you build your Android app using the[Material Design 3](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design)library, you can easily add spatial UI behaviors to its components and adaptive layouts.

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/visual-design-ls-adapted-opt.mp4)and watch it with a video player.

## How to test your app's visual design

Testing your app's visual design is crucial to ensure a comfortable and accessible user experience. Here's how to test across different XR platforms and environments.

**Use emulators, simulators, and real devices**

- If you're developing an Android app, test your app on the[Android XR emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/immersive). This helps you identify potential issues and quickly iterate without a physical device.

**Visual design testing checklist**

- Test any movement or animations to ensure they don't trigger motion sickness. Check for smooth transitions, stable frame rates, and predictable motion.
- Try out passthrough in real-world settings to ensure virtual elements blend with physical surroundings.
- Test your app in different lighting conditions, including bright and dim environments.
- Check text readability at different distances and angles.
- Evaluate the color scheme for accessibility and comfort.

**Gather user feedback**

Conduct user testing to identify any areas for improvement. Include users with varying levels of XR experience and visual abilities for a comprehensive perspective.

## Targets in Android XR

In an XR app, a target is the tappable or pointable area that users interact with. Larger targets increase precision, comfort, and usability. To make your app accessible, follow[Material Design target guidelines](https://m3.material.io/foundations/designing/structure#dab862b1-e042-4c40-b680-b484b9f077f6). They will work with Android, Unity, OpenXR, and WebXR apps. If your app already follows Material Design recommendations, your target sizes meet the minimum, though 56dp is optimal.

![A sample icon showing a recommended 56dp target and a 48dp affordance.](https://developer.android.com/static/images/design/ui/xr/guides/visual-design-target.jpg)

### All interactive UI elements should consider:

- Recommended target: 56dp x 56dp or larger
- Visual affordance (icon): 48dp x 48dp or larger
- Offset between target and visual affordance: 4dp
- For accurate interactions, pointer targets of different UI elements shouldn't overlap
- The target and icon scale with the parent container or label, as needed.

### Make sure you add hover states

**For increased accessibility, incorporate** [hover and focus states](https://m3.material.io/foundations/interaction/states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844)in addition to the[basic interactive states](https://m3.material.io/foundations/interaction/states/overview)for interactive components. Hover states can be helpful for everyone, and are particularly crucial for users who rely on pointer inputs to select UI elements.

**Hover states play an important role in enabling eye tracking**functionality within the system. However, when eye tracking is enabled, hover states are inaccessible to the application to protect user privacy and prevent data sharing. The system will draw a user-visible-only highlight state to convey which UI components are interactable.

### Distance between targets

Material Design recommends a minimum 8dp of space between targets, including buttons. This spacing ensures that users can easily distinguish between interactive elements and avoid accidental selections.

The specific distance between buttons can vary depending on their context and size. Some factors to consider:

- **Button size**: Larger buttons may require more space between them to maintain visual clarity.
- **Button grouping**: Buttons that are closely related functionally can be grouped closer together, while unrelated buttons should have more separation.
- **Layout**: The overall layout of the screen can influence the spacing between buttons. For example, buttons in a toolbar may be spaced more closely than buttons in a dialog.

## Panel size and scale

Android XR is designed to make your app comfortable, legible, and accessible to a wide audience. For an optimal experience, Android XR uses 0.868 dp-to-dmm.
| **Key Term:** Dmm, or distance-independent millimeters, are angular units that remain constant regardless of the distance between a user and a virtual object.[Dp](https://developer.android.com/training/multiscreen/screendensities), or density-independent pixels, are units that scale to have uniform dimensions on any screen. They provide a flexible way to accommodate a design across platforms.

![A visualization of a user who is 1.75 meters from an XR app, with a panel size of 1024 dp x 720 dp, and 32 dp rounded corners.](https://developer.android.com/static/images/design/ui/xr/guides/visual-design-size-scale.jpg)

If you are using panels, your XR app will most likely be farther away from a user than a physical screen. Consider the user is wearing a headset. For optimal comfort, place primary content in a 41° field of view so users don't have to move their head to interact.

**Recommendations**

- Panels have 32dp rounded corners. You can override this default.

**Panel depth behaviors**

- **Home Space**: Apps launch 1.75 meters from the user, and developers can't override this.
- **Full Space**: By default, apps launch at the same position they were in Home Space. You can use spatial logic to place panels based on the user's position, though we recommend a launch distance of 1.75 meters.

**When an app is 1.75 meters from the user**:

- 1024dp is perceived as 1556.24 millimeters
- 720dp is perceived as 1093.66 millimeters
- 1 meter in physical reality = 1 meter in XR

## Buttons and icons

If you have an existing Android app, you don't need to design special components for Android XR. Follow Material Design's guidelines for[buttons](https://m3.material.io/components/all-buttons)and[icons](https://m3.material.io/styles/icons/overview). If you have a Unity, OpenXR, or WebXR app, you can keep your buttons and icons as-is, or be inspired by Material Design.

If you decide to build your own buttons or icons, opt for simple forms, clean lines, basic shapes, and a limited color palette. Avoid overly detailed designs. Make them scalable and legible across varying resolutions and viewing distances. For accessibility, ensure sufficient contrast between the component and its background, and provide text descriptions or tooltips for users with screen readers or other assistive technologies.

## Colors

Android XR follows Material Design's[color system](https://m3.material.io/styles/color/system/how-the-system-works)to ensure a consistent and visually-appealing interface. To create an immersive visual style tailored to XR, design with sufficient contrast, choose a balanced palette, use colors accessible for those with color vision deficiencies, and avoid jarring combinations that can cause eye strain or disorientation.

![The Material Design system uses a color space called HCT, which defines all colors using three dimensions: hue, chroma, and tone.](https://developer.android.com/static/images/design/ui/xr/guides/visual-design-colors.png)

### Optimize color for display differences

The display on wired XR glasses works differently than the screen on an XR headset. Instead of a solid screen that replaces your view, think of wired XR glasses as a projector beaming light onto a clear lens.

- **Headsets replace the world**: They use cameras to capture the room and show it to you on an opaque screen. If the app wants to show black, it turns the pixels off, creating a true dark spot that blocks the world behind it.
- **Wired XR Glasses overlay the world**: They allow you to see the room directly through the glass. The display adds light on top of that view. Although you can't project "darkness" with pixels, hardware dimming can darken the lenses to block out the physical world.

### Designing for transparency

Because the display on wired XR glasses is additive, your color choices directly affect how solid or transparent your interface appears.

- **Black renders as transparent**: You cannot display pure black. Fully black pixels are simply off, meaning the user sees the real world directly through that part of the glass.
- **Brightness enhances visibility**: Brighter colors appear more solid. Darker colors emit less light and look more transparent. Adding white improves visibility, but avoid excessive brightness to prevent eyestrain.
- **Environment blending**: Your UI colors will visually mix with the real world. Using bright, high-contrast colors helps your UI stand out against unpredictable backgrounds.
- **Dimming lenses increases solidity**: The darker the lenses, the less transparent and more solid digital content appears. Increasing electrochromatic dimming blocks more background light, which helps colors look solid and makes dark elements stand out.

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/xr/adjustable-dimming.mp4)and watch it with a video player.

## Dark and light themes in XR

Use dark and light themes as you would on an Android mobile app. Users can switch between dark and light themes in Android XR, choosing the visual style that best meets their individual preferences.

[Learn more about Material Design color schemes](https://m3.material.io/styles/color/static/baseline).

## XR typography

Font legibility is critical to a comfortable user experience in XR. We recommend using typescale options with a font size of 14dp or larger, and a font weight of normal or higher for improved legibility.

To create an app that is easy to use, consider following[Material Design's typography guidance](https://m3.material.io/styles/typography/overview).

![A close up of a large R and o, with typographic numbers along the bottom. The dark purple letters clearly contrast against a light purple background.](https://developer.android.com/static/images/design/ui/xr/guides/visual-design-typography.png)

### Best practices for typography in XR

- **Size for variable distances**: Remember that users will be moving and viewing text from varying locations. Ensure font sizes are large enough to be read from a distance.
- **Position text in the user's natural field of view**: This avoids excessive head movement and neck strain.
- **Consider depth and scale**: Use depth cues and scale to create hierarchy in the 3D space.
- **Make sure text is legible against a user's background**: Heavier weights offer more contrast. Adjust depending on the environment's colors, lighting, and complexity. Note that brighter text values help maintain legibility on wired XR glasses.
- **Use adaptable typography**: Panels may be too close, too far, and at awkward viewing angles from a user.
- **Limit text attached to moving objects**: This can cause motion sickness.

### Accessible typography in XR

- **Select fonts for legibility**: Prioritize fonts with clear letterforms at small sizes and far distances.
- **Use sentence case text**: Sentence case text is easier to read than uppercase text.
- **Limit line length**: Aim for shorter line lengths to improve readability.
- **Select accessible colors**: Use color combinations that are legible to users with color vision differences.
- **Avoid overcrowding**: Give text ample breathing room.
- **Allow text scaling**: Let users adjust text size to meet their individual needs.

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.