---
title: https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back
url: https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back
source: md.txt
---

# Predictive back design

![](https://developer.android.com/static/images/design/ui/mobile/predictive-back-hero.png)

Predictive back is the result of a gesture navigation operation in which a user has swiped back to preview their destination of the back gesture before fully completing it. This lets the user decide whether to continue---in other words, to "commit" to the back gesture---or stay in the current view.

Predictive back provides a smoother, more intuitive navigation experience while using[gesture navigation](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars). It leverages built-in animations to inform users where their actions will take them to reduce unexpected outcomes.

Use the design guidance on this page if your app design calls for providing back navigation for custom transitions and animations for key moments.

## Support for predictive back

Supporting predictive back is available whether using a default or custom back navigation. If you're using the default back navigation, you can easily opt-into the feature. Read more about[supporting predictive back](https://developer.android.com/guide/navigation/predictive-back-gesture#update-default).

After you opt-in, your app has built in animations such as back-to-home, cross-activity, and cross-task.

You can also upgrade your Material component dependency to 1.10.0-alpha02 or above of MDC Android to receive the following Material component animations:

- [Bottom sheets](https://m3.material.io/components/bottom-sheets/guidelines#3d7735e2-73ea-4f3e-bd42-e70161fc1085)
- [Side sheets](https://m3.material.io/components/side-sheets/guidelines#d77245e3-1013-48f8-a9d7-76f484e1be13)
- [Search](https://m3.material.io/components/search/guidelines#3f2d4e47-2cf5-4c33-b6e1-5368ceaade55)

## Ensure your app has edge-to-edge support

To help your users, predictive back navigation respects gesture insets defined in[edge-to-edge features](https://developer.android.com/develop/ui/views/layout/edge-to-edge). Avoid adding touch gestures or drag targets under these gesture areas.
![](https://developer.android.com/static/images/design/ui/mobile/predictive-back-1-system-gesture-insets.png)**Figure 1:**System gesture insets. Avoid placing touch targets completely under these areas

## Full screen surfaces

If your app creates custom in-app transitions for full-screen surfaces, follow this design guidance.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/predictive-back_commit_inner-surface_fade-through-dismiss.mp4)and watch it with a video player.**Video 1.**Example of full screen surface predictive back.

<br />

### Back preview

When a user performs a back gesture on a full-screen surface, the inner area should scale down as the gesture progresses. As soon as the user crosses the commit threshold, the contents should swap to the next state using a fade through, informing the user where their action will take them.

### Interpolation

The interpolator used ensures the screen quickly exits. The parameters are (.1, .1, 0, 1) to match the interpolator used for the SystemUI animations

### Cancel action

If the user releases the gesture in a non-commit state, the contents swiftly return and scale back to their original state and size before the gesture begins, undoing any state changes.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/predictiveBack_full-deactivate_innersurface.mp4)and watch it with a video player.**Video 2.**Example non-commit state and cancel action.

### Motion specs

|  Parameter  | Initial Value | Target Value |                       Context                       |
|-------------|---------------|--------------|-----------------------------------------------------|
| Exit Scale  | **100%**      | **90%**      |
| Enter Scale | **110%**      | **100%**     |
| Exit Fade   | **100%**      | **0%**       | Fades to target value at the 35% progress threshold |
| Enter Fade  | **0%**        | **100%**     | Enter fade starts at the 35% progress threshold     |

**Note:** For full screen surface transitions, there is a fade through progress threshold set at 35%. The progress threshold represents the progress value at which the exiting screen fully fades out and the entering screen starts to fade in. At the 35% mark, neither screen is showing.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/predictive-back-video-1-calendar-event-example.mp4)and watch it with a video player.**Video 3.**Adding a subtle overshoot to absorb spring tension built up during gesture

## Shared element transition

| **Note:** This shared element transition works between views and composables in the same fragment or screen. It also works if you're managing your own back stack without the Navigation component and are using`PredictiveBackHandler`. This transition does not work with`FragmentManager`, the Navigation Component, or Navigation Compose. In these cases, avoid scaling the screen by 90%. Instead, run the shared element transition as the user navigates back.

If your app creates custom in-app transitions for shared element transitions, use the following design guidance.

When a user makes a back gesture on a shared element transitions, the surface fully detaches from the edge of the screen during the back preview, and the user can directly manipulate it. However, the design shouldn't visually suggest to the user that completing a back gesture dismisses an item in the direction of the back gesture.

For example, you can use shared element transitions when dismissing detail screens back to vertical lists to visually hint to the user that they're undoing the previous action. In video 3, a calendar event is dismissed back to a day view. To improve tactility, the design adds a subtle overshoot to absorb some of the spring tension built up during the gesture.
| **Note:** Only the system can dismiss the app window itself.

<br />

### Back preview

When presenting predictive animations to the user, a*pre-commit*state maintained by your app measures when the user has performed an edge-to-edge back gesture but hasn't committed to it by letting go. You need to provide parameters that apply to this pre-commit state.

The amount of movement displayed is based on the furthest the user can move from the location at which the gesture began.  
Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/predictive-back-video-2-back-preview.mp4)and watch it with a video player.**Video 4.**An example of back preview

### Motion specs

Shared element transitions are directly affected by the x and y shift from the beginning of the gesture. This section describes specifications and values that govern the mechanics used for onscreen feedback.

The following figures show recommended motion specs for surface animations.
![](https://developer.android.com/static/images/design/ui/mobile/predictive-back-2-surface-scale-left-hand-swiping.png)**Figure 2:**Surface shift, scale and margin parameters for swiping from the left edge"

1Margins: 5% of the width on either side (related to the surface area described in3)

2Calculated shift if scaling window to the center. Calculate for required 8dp margin: ((screen width / 20) - 8) dp

3Surface scales to 90% size, leaving 10% available for margins (see1)

4Leave an 8 dp gap from the screen edge

We recommend keeping the listed parameters for a consistent experience, but you can alter the specifications to create a custom animation.

In the preceding figure, the screen width is 1280, making the x-shift 56 dp. The formula for that is:

((1280/20)-8)= 56 dp x-shift
![](https://developer.android.com/static/images/design/ui/mobile/predictive-back-3-delta-params-left-hand-swiping.png)**Figure 3:**Y shift and scale parameters for swiping from the left edge. The full screen surface displays a back preview.

1Space between edge and device margin available for y-shift

2If the surface shifts off screen, scale the surface down by no more than 50%.

2Surface starts off vertically centered, with y-shift defined as the following:

- Limit y-shift so the surface never passes the 8 dp screen margin
- To prevent the surface from abruptly stopping, use a decelerate interpolator and map to the y-shift limit

3Preserve the 8 dp margin once the surface is short enough

For custom animation, you must define all of the following parameters.

| Parameter |                  Value                  |              Context               |
|-----------|-----------------------------------------|------------------------------------|
| X shift   | ((screen width / 20) - 8)*dp*           | Maximum shift, leaves**8dp**margin |
| Y shift   | ((available screen height / 20) -8)*dp* | Maximum shift, leaves**8dp**margin |
| Scale     | **90%**                                 | Minimum scale of window size       |

Developers implementing the custom animation using the Predictive Back Progress APIs use these parameters.

### Interpolating gesture progress

A linear progress value can be derived from the user's gesture, but it shouldn't be directly used for preview animations. Instead, feedback should be tailored to what helps the user during the backward action. Feed the progress value with a[`STANDARD_DECELERATE`token](https://m3.material.io/styles/motion/easing-and-duration/tokens-specs)or[PathInterpolator(0f, 0f, 0f, 1f)](https://developer.android.com/reference/androidx/core/animation/PathInterpolator)so that the gesture is more apparent in the beginning. This feedback enhances movement detection at the start of the gesture and employs deceleration to control feedback in a visually pleasing and clear manner.

### Commit to action

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/predictive-back-video-3-fling-to-commit.mp4)and watch it with a video player.**Video 5.**An example of flinging to commit

When a user gestures past the commit point and releases, an animation is displayed which confirms the completion of the action.

When the users perform gestures swiftly, these are generally interpreted as flings. This kind of interaction can apply high velocities to on-screen elements, so in the context of back previews, the system absorbs that velocity by momentarily animating the surface toward its maximum preview state before running the commit animation.

The strength of the fling determines how much of the preview animation is displayed before running the commit animation. The kind of animation shown depends on the content being dismissed, as shown in video 2.

### Cancel action

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/images/design/ui/mobile/predictive-back-video-4-cancel-action.mp4)and watch it with a video player.**Video 6.**An example of canceling an action

Video 6 shows an example of what happens when a user releases before the threshold, displaying an animation confirming that the action has been canceled. For shared element transitions, the window swiftly moves and scales back to its original edge-to-edge state before the gesture began.