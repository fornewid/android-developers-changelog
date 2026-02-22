---
title: https://developer.android.com/studio/releases/past-releases/as-meerkat-feature-drop-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-meerkat-feature-drop-release-notes
source: md.txt
---

# Android Studio Meerkat Feature Drop | 2024.3.2 (May 2025)

The following are new features in Android Studio Meerkat Feature Drop.

## Themed icon support

To ensure your app icon looks its best when users enable "Theme icons" in the Android 13 Developer Options, Android Studio Meerkat Feature Drop \| 2024.3.2 Canary 1 now lets you preview how your icon will look with the new theming algorithm.

For full control over your icon's appearance, you should provide your own themed icon by[adding a custom monochromatic layer](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive). But even if you haven't done that yet, you can still use this new preview tool to get an idea of how your icon will look and identify any potential color contrast issues.
![Themed app icon preview](https://developer.android.com/static/studio/images/design/theme-app-icon-preview.gif)Themed app icon preview

<br />

## Android Studio config directories changing

Starting with Meerkat Feature Drop Canary 2, Android Studio uses the same user configurations across canary, beta, and stable releases. As a result, "Preview" has been dropped from the[configuration directory path](https://developer.android.com/studio/troubleshoot#directories)for Android Studio in canary and beta releases.

Additionally, to let feature drop releases run simultaneously with platform update releases, we've added a micro version to the config directory path. For example,`AndroidStudio2024.3.2`is used instead of`AndroidStudio2024.3`.

See[Export and import IDE settings](https://developer.android.com/studio/intro/studio-config#ExportImportSettings)if you'd like to import configurations manually.

## Prompt Library

Gemini in Android Studio's new Prompt Library feature enhances productivity by allowing you to save and manage frequently used prompts. Access the Prompt Library from**Settings \> Gemini \> Prompt Library**to store and retrieve prompts. You can store prompts at the IDE level or the project level:

- IDE-level prompts are private to yourself and can be used across multiple projects.
- Project-level prompts can be shared among teammates working on the same project. To share prompts across the team you must add the`.idea`folder to the version control system.

You can also right-click on a prompt in chat to save it for later use. To apply a saved prompt, right-click in the Editor and navigate to**Gemini \> Prompt Library**to apply the prompt. This streamlined workflow eliminates the need to retype commonly used prompts, saving you time and effort.

![](https://developer.android.com/static/studio/images/prompt-library.png)

## Motion editor deprecation

At Android Studio, we're continuously striving to provide developers with the most efficient and modern tools for building exceptional Android applications. As part of this commitment, we're deprecating the Motion Editor in Android Studio Meerkat Feature Drop.

For some time, the Motion Editor has served as a valuable tool for creating animations built with motion layout. However, with the rapid evolution of Jetpack Compose, we've recognized the immense potential of this modern UI toolkit for animation development. Compose offers a declarative and intuitive approach, simplifying the creation of smooth and engaging animations.

Jetpack Compose provides several key advantages:

1. **Modern and declarative**:Compose's declarative syntax makes animation code more readable and maintainable.
2. **Integrated animation tools**: Compose Animation Preview offers a streamlined workflow for creating and testing animations directly within your Compose code.
3. **Future-proof development**: By focusing on Compose, we're investing in the future of Android UI development.

Our goal is to provide a unified and powerful animation experience within the Compose ecosystem. While the Motion Editor has been a valuable tool, we believe that Compose represents the future of Android animation. We want to focus our efforts on making Compose as good as it can be. We encourage you to learn more about[building animations with Jetpack Compose](https://developer.android.com/develop/ui/compose/animation/introduction)and[Compose animation tools](https://developer.android.com/develop/ui/compose/tooling/animation-preview).