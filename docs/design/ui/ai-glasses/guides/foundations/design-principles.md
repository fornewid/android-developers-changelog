---
title: https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles
url: https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles
source: md.txt
---

Designing for intelligent eyewear with Android XR requires a thoughtful approach
to user experience, prioritizing comfort and seamless integration with the
user's daily life. Apps on glasses should feel like a natural extension of the
user's perception, providing convenient access to information without being
intrusive.

## Audio glasses and display glasses

Audio glasses are lightweight and portable for all day wear. With built-in
speakers, a camera, and microphone; designers and developers are able to build
intelligent and hands-free augmented experiences.

Display glasses provide the addition of a small display, giving users a private
screen for seeing additional information, harmonizing with audio output.

Design your augmented experience to take into account both types of glasses with
both displayless and display capabilities.

## Glasses prioritize multi-modal interactions

Design the user interface for hands-free modalities such as voice or gesture.
Carefully consider the limitations of indirect control and less-precise input
when designing interactions.

![An XR differentiated app has a user experience explicitly designed for XR, and
it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_principle_hands-free.png)

## Prioritize glanceable, transient elements

Craft user interfaces with an emphasis on glanceable views and temporary
elements, acknowledging the transient nature of interactions on display glasses.

Design UI to appear only when needed and recede when the task is complete,
minimizing persistent on-screen distractions.

![An XR differentiated app has a user experience explicitly designed for XR, and
it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundations_principle_glance.gif)

## Transparent UI always competes with the real-world

Present information concisely and adaptively, considering the glasses' small
field of view, varying focal distances, and potentially dynamic backgrounds.

Optimize typography for legibility to prevent overwhelming the user with
information.

![An XR differentiated app has a user experience explicitly designed for XR, and
it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_principle_optimize_depth.png)

## Optimize for focus

Design layouts that prioritize essential information, reducing the number of
actions and visual elements to maintain user focus.

Thoughtfully manage content density to respect the limited field of view and
prevent cognitive overload for comfortable readability.

![An XR differentiated app has a user experience explicitly designed for XR, and
it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_principle_optimize_focus.png)

## Comfort

User comfort is paramount. Avoid overwhelming the user with excessive visual
information or audio alerts. Prioritize clear, concise communication and
interactions that don't distract from real-world activities, especially when the
user is in motion or requires full attention to their surroundings. This unique
form factor and its hardware features come with specialized considerations.

- Be transparent about what data you collect, why you collect it, and how it is stored.
- Avoid sudden, distracting visual notifications that could obstruct the user's view at critical moments.
- If your app provides audio, the volume shouldn't block out environmental sounds. Users must remain aware of their surroundings.
- Avoid UI and motion that could induce motion sickness, such as expecting users to read large amounts of text while walking.
- Account for reading and legibility in a spectrum of possible environments by following Jetpack Compose Glimmer UI best practices.