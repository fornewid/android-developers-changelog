---
title: https://developer.android.com/stories/apps/mercari
url: https://developer.android.com/stories/apps/mercari
source: md.txt
---

# Mercari improves UI development productivity by 56% with Jetpack Compose

[Mercari](https://play.google.com/store/apps/details?id=com.kouzoh.mercari)allows millions of people to shop and sell almost anything. The company was founded in 2013 in Japan, and it now is the largest smartphone-focused C2C marketplace in Japan. Mercari's Client Architect Team started using[Jetpack Compose](https://developer.android.com/jetpack/compose)in 2020 with the goal of using modern solutions and technologies that can scale for the long term to build their tech stack for new applications.

## What they did

The Mercari team needed to implement a design system with complex state management and styling on Android Views --- a very complex task. Using Jetpack Compose, they were not only able to implement this complex system, it helped them spend less time developing each screen.

Jetpack Compose also helped the team write UI code for their new app utilizing the design system, making their UI code concise and easy to understand. As a result, the team can spend more time writing screens and business logic, such as practical support for the dark theme.

In addition, the Mercari team wrote a proof-of-concept tool for integrating Figma with the design system, which automatically generates UI code from the component designs. The team said that developing this tool was easier with Compose due to its declarative nature.

*"Once Android developers get used to writing Jetpack Compose code, they wouldn't wish to go back." - Anthony Allan Conda, Android Tech Lead at Mercari*

## Results

Between Jetpack Compose and their new design system, Mercari was able to use far less code to write screens. On screens with infinitely-scrollable content --- a common use case --- they actually reduced their code by about 56%. As a result, they were able to write more screens in the same amount of time, giving them more time to write business logic and other parts of the code.

Also, they were able to do more with the UI itself, such as incorporating animations and using intuitive APIs such as*AnimatedVisibility* ,*Crossfade* , and*Animatable*.

Mercari is planning to continue using Jetpack Compose in their new application until its release. Their design system, with the Android SDK written in Jetpack Compose, is also designed to work with multiple applications within Mercari.

## Get started

Learn more about[Jetpack Compose](https://developer.android.com/jetpack/compose).