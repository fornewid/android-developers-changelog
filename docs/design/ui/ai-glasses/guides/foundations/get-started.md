---
title: https://developer.android.com/design/ui/ai-glasses/guides/foundations/get-started
url: https://developer.android.com/design/ui/ai-glasses/guides/foundations/get-started
source: md.txt
---

Build your AI Glasses app using the Jetpack Compose Glimmer UI framework for augmented experiences that work across AI Glasses. Jetpack Compose Glimmer is one of the first UI frameworks to be optimized for transparent displays and the AI glasses form-factor.

## 1. Decide on user journeys

Focus on critical user journeys (CUJs) that are compatible with the AI glasses form factor's glanceable principles. That could be expressed with minimal UI or audio only while allowing the user to stay present in their surroundings. To find opportunities, consider starting entry points in your current app that would benefit from Glasses.

For example, a user may benefit with hands-free, turn-by-turn walking directions to help them navigate to their destination.

The chosen user journey should also account for safety, comfort, and performance principles. For example, don't choose tasks that would require the user's camera for unnecessarily long periods or infringe on their privacy.

Learn about[foundational principles](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles).  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step1_dont.png)  
check_circle

### Do

Extract features from your mobile app that benefit from the glasses form factor. For example, glanceable experiences.  
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step1_do.png)  
cancel

### Don't

Port your entire phone app to glasses as they do not scale to the glasses form factor.

## 2. Minimize \& Translate

For display mode UI, start with a CUJ from your core app:

- **Optimize layouts for focus**: Layouts prioritize essential information, reducing the number of actions and visual elements to maintain user focus.

- **Use depth for hierarchy**: Depth is used to communicate element priority.

- **Design from the bottom up**: When building mocks, start from the bottom, laying out components upward.

- **Translate visual components**: For display AI glasses, use Jetpack Compose Glimmer components and layout patterns.

Read more on[components](https://developer.android.com/design/ui/ai-glasses/guides/surfaces/overview)and[app view](https://developer.android.com/design/ui/ai-glasses/guidea/surfaces/app).
![The shopping list app reduces the list view down to a minimal list experience and needs feedback UI only.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step.png)A shopping list app translated to Display AI glasses elements. The system bars are visually distinct, AI glasses are usually empty. Here the app bar could translate to a title chip while the Material list elements be translated to the Jetpack Compose Glimmer list.

### Optimized components

<br />

**A. Surface color** : The surface color of components is black to maximize contrast for card content.

<br />

**B. Outline \& Highlight**: The Outline color is optimized for contrast. The use of a highlight provides visual expression and might be used to indicate some types of input.

**C. Shape**: A softer shape system is used to improve glanceability by reducing the sharpness of corners and improving comfort. On Surface color: The On Surface color of content is white to maximize contrast against the world.

**D. Typography**: Glimmer's typography scale uses a small set of refined Body and Title styles that optimize kerning, size and weight for optimal readability \& legibility.

**E. Iconography**: The use of rounded Material Symbols coheres with the rounded typography scale.  
![Glimmer components are optimized for transparent display.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step2_optimized.png)

<br />

<br />

## 3. Audio flow \& cues

Get conversational with the Audio. While audio should make up a large part of your AI Glasses app without overwhelming the user, you also need to account for an audio-only experience for certain devices. You can do this by creating an audio-only flow map to describe this experience. Notate interactions and feedback with audio cues and dialogue.
![Create an audio-only flow map to help you plan conversational experiences that don't overwhelm the user.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step4.png)

## 4. Map input controls

Make sure to map out the inputs for the device controls and gestures. You can start by translating basic app interactions, like tap, to a trackpad tap.

[Continue to inputs.](https://developer.android.com/design/ui/ai-glasses/guides/interaction/inputs)

![An XR differentiated app has a user experience explicitly designed for XR, and it implements features that are only offered on XR.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step3.png)

<br />

## 5. Consider SysUI

Account for other system interfaces.

Your app will appear in the home and other system features, like notifications if used. These can appear in the system bar.

[More on System UI](https://developer.android.com/design/ui/ai-glasses/guides/surfaces/sysui)  
![Create an audio-only flow map to help you plan conversational experiences that don't overwhelm the user.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step5.png)

<br />

## 6. Additional states

Your app will encounter different scenarios on AI glasses, such as connection or permission issues. Account for these different states both within your core app and glasses app.

Make sure to ask for device feature permissions.

Remember, you will need to consider these through visual UI and audio. For example, give audio feedback to communicate that they should complete a permission flow on their mobile device or to read out errors.
![Account for different app states both within your core app and glasses app.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_foundation_getstarted_step6.png)**Note:** Get started with the[Jetpack Compose Glimmer UI Kit on Figma](http://www.figma.com/@androiddesign).