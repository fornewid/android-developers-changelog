---
title: https://developer.android.com/design/ui/xr/guides/motion
url: https://developer.android.com/design/ui/xr/guides/motion
source: md.txt
---

# Motion can transform your XR app from a static scene into a vibrant, interactive experience. It's important to consider a user's visual and physical comfort when designing with motion.

- **UI motion** : For user interface elements, you can follow established UI motion design standards, such as[Material Design's motion guidelines](https://m3.material.io/styles/motion/overview).
- **3D motion in XR apps**: When building an app with 3D objects and environment interactions, keep in mind large movements may be uncomfortable to users. Be thoughtful when moving UI or environments that ground a user in your virtual world. If moved too quickly, a user may experience physical discomfort or motion sickness.
- **Design for comfort**: Avoid motion that makes people feel sick.
- **Start small**: Use subtle movements to encourage users to explore your app. Save big movements for specific moments.
- **Provide guidance**: Use motion to help users understand what's happening and where to look.

### How to add user-friendly motion

Consider how any movements in your app make a user feel. Motion in space is more comfortable to users when they are in control.

Discomfort can happen when an app decides to move something in space without a user expecting it. If your eyes perceive movement in the virtual world while your inner ear detects that you're still, this sensory mismatch can trigger motion sickness.

Follow these best practices to keep users feeling safe and comfortable.

- **Clear onboarding**: To help users acclimate to your app, introduce motion mechanics gradually.
- **Rest stops**: Moments of stillness or reduced motion allow users to rest and avoid fatigue.
- **Consider making motion optional**: Some users may be more comfortable when they can adjust the level of motion.
- **Predictable camera motions**: Smooth and predictable camera movements can help prevent discomfort.
- **Consider animated feedback**: If you want to create a believable experience, you can use animations that follow real-world physics.
- **Whole world movements can make people feel sick**. In cases where big movements are necessary, you may want to fade out and fade in, hide a user's peripheral vision, accelerate slowly, or avoid rotating.
- **Limit motion of large objects**, because it can feel like the user is moving as well. To prevent users from experiencing discomfort, consider making these objects semi-transparent or less noticeable.