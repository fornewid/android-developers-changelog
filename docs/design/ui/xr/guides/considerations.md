---
title: https://developer.android.com/design/ui/xr/guides/considerations
url: https://developer.android.com/design/ui/xr/guides/considerations
source: md.txt
---

# Considerations

Unity, OpenXR, and WebXR provide a versatile toolkit for creating diverse interactions in immersive experiences. The objective is to develop immersive apps that users can interact with using existing learned experiences. You can design anything ranging from simple gestures to complex physics-based simulations.

Note that Unity, OpenXR, and WebXR apps only operate in[Full Space](https://developer.android.com/design/ui/xr/guides/foundations#full-space).

[Learn about Android XR's design principles](https://developer.android.com/design/ui/xr/guides/get-started).

## Inputs

XR apps can include interactions with hand, eye, and face tracking; gestures; voice commands; and traditional input devices like keyboards, mice, and controllers. Consider which inputs your app will need to deliver a natural and accessible user experience.

- Support familiar gestures to reduce your app's learning curve. When interacting with 2D UI, use**standard system gestures**such as pinch. For 3D interactions like picking up and throwing a ball, you should design with gestures that mimic the real-world interaction. This builds on a user's existing knowledge and reduces the need for tutorials.
- If additional gestures are necessary, make sure they are easy to learn, remember, and execute. Steer clear of complex, multi-step gestures or unnatural positions that can lead to discomfort and fatigue. Consider providing guides to teach users how to use hand gestures.
- Ensure your experience is usable with either the left or right hand. If that's not possible, follow the system's handedness preference.
- While two-handed interactions can be immersive, they may be challenging for users with limited mobility. Prioritize one-handed interactions for essential actions. If two-handed gestures are necessary, provide alternative one-handed methods to achieve the same result.
- Unity, OpenXR, and WebXR apps don't automatically benefit from[Android's back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack). Consider implementing a back stack to allow users to access Android XR's[back gesture](https://developer.android.com/design/ui/xr/guides/foundations#understanding-system)to undo actions or go back using gesture navigation.

![Two hands using gesture navigation.](https://developer.android.com/static/images/design/ui/xr/guides/input-gestures.jpg)

## UI

User interface elements like buttons, panels, and text are essential for natural interactions in XR apps. The design should prioritize a seamless, intuitive user experience. The specific UI design choices will depend on your app's unique requirements.

- Place primary interactive elements and crucial content within the user's natural line of sight and field of view. This enhances visibility and ensures a comfortable experience. Consider how users are intended to interact with the interface to determine at which distance it should be placed. For example, are they aiming with a laser pointer, or tapping buttons directly with their fingers? Configure the size of your interface based on its intended distance from the user.[Refer to the Android XR size and scale guide](https://developer.android.com/design/ui/xr/guides/visual-design#panel-size).
- When designing interactive UI elements such as buttons, consider how users are intended to interact with them, the level of precision needed for each input method --- hand tracking versus mouse, and adapt factors like target size and spacing accordingly. Ensure UI positions allow for comfortable interactions. Provide visual feedback for user actions.[Refer to the Android XR style guide](https://developer.android.com/design/ui/xr/guides/visual-design).
- 2D UI such as panels are well suited for menu-based interactions. 3D UI such as physical buttons, levers, and switches can be more immersive when interacting with spatial environments. A careful balance of panel-based interactions for high readability and 3D objects for world-focused interactions can create a powerful, immersive experience.
- Ensure text is legible by using appropriate font sizes, types, and contrast. Position UI based on the distance users will be viewing text. Use[Signed Distance Field fonts](https://docs.unity3d.com/Packages/com.unity.textmeshpro@2.2/manual/FontAssetsSDF.html)for smooth text rendering at a variety of font sizes.[Refer to the Android XR typography guide](https://developer.android.com/design/ui/xr/guides/visual-design#accessible-typography).

![A person is fully immersed in a spatial environment with a very large screen. They are standing on rocks, with UI controls in arm's reach.](https://developer.android.com/static/images/design/ui/xr/guides/immersive-ui.jpg)

## Spatial interactions

Some of the richest interactions in XR involve a user's ability to interact directly with 3D objects. This could be as straightforward as picking up, inspecting, and tossing an object. It also includes more complex interactions such as pulling levers, pressing buttons, and interacting with elements that are already held by the user --- like spraying a spray bottle. For intuitive 3D object interactions, design based on a user's pre-existing knowledge of the world.

- Consider integrating a physics engine if you want to create realistic actions. If you're building with Unity, it has a built-in[physics engine](https://docs.unity3d.com/Manual/PhysicsSection.html). Be mindful of how much processing power physics engines consume, and optimize for performance.
- Believability is more important than realism. For example, if a user believes they threw a ball hard, the app should add extra force to the ball beyond what the device's sensors indicate.
- Objects should be built to match their affordances. This means every possible action a user could perform on or with an object should be accounted for in your app. For example, a donut can be picked up, thrown, and eaten. Instead of eating the donut, the app could employ a voice over stating, "I'm not hungry right now". These solutions address the actions a user expects to perform with a donut.
- Objects can be held using various techniques, including parenting, physics joints, following, and physics forces. Each technique has its own advantages and disadvantages. Before implementing a custom grab method, it's crucial to research and test different approaches to determine the most suitable one.
- Ergonomics is important when designing in a 3D environment. For accessibility, consider adding a handle to flat surfaces to allow a user to adjust it to a comfortable height. Be sure to test each object in the space with a variety of users, as everyone's body is different.

![Job Simulator, a fully immersive VR game with a user sitting at a vintage computer in an office cubicle. The game includes virtual hands that can interact with 3D objects.](https://developer.android.com/static/images/design/ui/xr/guides/job-simulator.jpg)

## Scene design

Scenes can range from fully immersive virtual worlds to augmented reality experiences that blend virtual elements with a user's real surroundings. Design scenes that are comfortable, functional, and take advantage of the unique capabilities of XR.

- Limit scenes that move around the user such as flying. This can cause discomfort, especially if a user's physical body remains still. Some[locomotion](https://developer.android.com/design/ui/xr/guides/considerations#locomotion)techniques such as tunnel vision (described in the next section) help reduce discomfort.
- To create mixed reality experiences, you can use Android XR's scene understanding capabilities to integrate virtual objects into a user's physical environment.
- For virtual reality applications, you may want to incorporate limited views of the real world within the virtual space. This helps users stay aware of their surroundings and interact with physical objects without leaving the immersive experience.

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/xr-accessible-design.mp4)and watch it with a video player.

## Locomotion

Android XR experiences are encouraged to allow users to move freely around their physical space as defined by a configured boundary. For example, some users find virtual experiences are more immersive when they're designed around a non-moving authored space. If you expect users to move around a larger virtual space than what the boundary allows, consider using locomotion techniques that amplify movement such as teleportation.

With**teleportation**, a user points and selects, or uses a controller to instantly jump to a new location. It's great for covering large distances quickly, and is often the locomotion method that causes the least amount of motion sickness. Briefly obscuring the screen during the transition can further minimize discomfort.

Other**locomotion methods**

If you use other locomotion methods, consider also offering teleportation as an alternative.

- **Walking in place with arms swinging**: Simulate walking by swinging your arms or moving your controller up and down. Some users may find this tiring or less intuitive.
- **Continuous movement**: Use a controller's joystick or thumbstick to move your virtual self through the environment. In most circumstances, you should avoid this method as it's a common cause of motion sickness.

If you decide to use locomotion in your experience, offer multiple options to accommodate individual preferences and improve the user experience.

Motion sickness can occur when there's a disconnect between a user's physical movement and their virtual experience. To optimize user comfort during locomotion:

- Ensure the virtual horizon remains steady and level.
- If continuous movement is required, avoid any progressive acceleration or deceleration. Keep the speed consistent.
- Tunnel vision can help reduce motion sickness by narrowing the user's field of view during movement, with a vignetting effect that limits the motion perceived in peripheral areas.
- For rotation, snap a user's viewpoint to specific angles. It might cause some disorientation, but will decrease motion sickness.
- Users have different levels of tolerance. Let them adjust comfort settings to their preference, such as choosing their locomotion method, toggling tunnel vision on or off, or adjusting their movement speed.

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/locomotion-horizon.mp4)and watch it with a video player.

## Spatial audio

Sound is a powerful tool to create immersive soundscapes that transport users to another world and evoke specific emotions. Spatial audio accurately positions sounds in the virtual environment.

- Ambisonics is like a skybox for audio, providing an immersive soundscape for your users. Use ambisonics for background environmental sounds or other scenarios where you want to replicate a full-spherical sound field that surrounds the listener.
- Spatialized audio cues can guide a user's attention.
- Spatialize sound effects to increase immersion.
- Spatializing voice audio to a speaker's location gives users a sense of presence even if they're not directly facing the speaker.
- Allow users to adjust their audio. For example, they might want to disable or change the volume of the background music, sound effects, or voice overs.
- Consider adding subtitles for people who are deaf or hard of hearing.

Alas, your browser doesn't support HTML5 video. That's OK! You can still[download the video](https://developer.android.com/static/videos/design/ui/xr/spatial-audio.mp4)and watch it with a video player.

## More considerations for comfort

To prioritize accessibility, provide customizable options that cater to diverse abilities and preferences. This ensures a wide range of users can enjoy the immersive experience.

- **Make your application run at 72 frames per second**: This will help minimize visual judder and prevent nausea.
- **Give users control**: To make your app user friendly for those with varying levels of affinity with XR, let users tailor their experience with customizable settings. Consider letting users remap controller buttons and gestures to fit their physical needs or preferences. For example, users with limited hand mobility may benefit from different button layouts or larger, simple input controls.

## For guidance on specific platforms, refer to:

[Develop for OpenXR](https://developer.android.com/develop/xr/openxr)

[Develop with Unity](https://developer.android.com/develop/xr/unity)

[WebXR documentation](https://immersiveweb.dev/)

*** ** * ** ***

OpenXR™ and the OpenXR logo are trademarks owned by The Khronos Group Inc. and are registered as a trademark in China, the European Union, Japan and the United Kingdom.