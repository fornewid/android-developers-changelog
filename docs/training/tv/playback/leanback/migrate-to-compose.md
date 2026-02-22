---
title: https://developer.android.com/training/tv/playback/leanback/migrate-to-compose
url: https://developer.android.com/training/tv/playback/leanback/migrate-to-compose
source: md.txt
---

# Migrate to Compose for TV

To migrate from the Leanback UI toolkit to Compose for Android TV, follow these steps:

- **Assess your current Leanback implementation**by identifying the components you're using (including those that are provided inside the prefabricated fragments) and understanding how your UI is structured and how data flows through your app.

- **Migrate individual screens**of your TV app to Compose so you can learn and adapt to Compose gradually.

  - While you can use both Leanback and Compose within the same app to allow for a gradual migration process, begin by replacing entire fragments at a time with a goal of converting your TV application into a single activity.

  - Start small. Don't try to migrate everything at once. Begin with smaller components like settings or account screens and gradually work your way through the app.

  - Refer to documentation and examples in the resources listed in the[Resources](https://developer.android.com/training/tv/playback/leanback/migrate-to-compose#resources)section.

- **Leverage dedicated components** from Compose for TV by using[the Jetpack libraries](https://developer.android.com/jetpack/androidx/releases/tv). Consult our[design guides](https://developer.android.com/design/ui/tv/guides/components)to explore how you can customize and extend ready-to-use composables to build beautiful TV UIs.

- **Adapt your data and state management** to support the Compose[declarative programming paradigm](https://developer.android.com/develop/ui/compose/mental-model#paradigm). Adaptation might require changes in how you manage data and state in your app. Use[`ViewModel`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)and Jetpack Compose internal state management mechanisms to manage data and state in your app.

- **[Test](https://developer.android.com/develop/ui/compose/testing)and iterate**as you migrate more complex parts of your app.

Engage with the active Android[developer community on Stack Overflow](https://stackoverflow.com/questions/tagged/android-jetpack-compose-tv)for any bugs you encounter, or submit the bugs through our[public bug tracker](https://developer.android.com/jetpack/androidx/releases/tv#feedback).

## Resources

Whether you're new to Compose or are in the process of migrating to Compose already, our large collection of resources are here to help you learn best practices for building TV UIs with the modern Android development toolkit, Jetpack Compose:

- [Compose for TV integration guides](https://developer.android.com/training/tv/playback/compose)
- [TV design guides](https://developer.android.com/design/ui/tv/guides/components)
- [Introduction to Compose for TV](https://developer.android.com/codelabs/compose-for-tv-introduction)codelab
- [Library release notes](https://developer.android.com/jetpack/androidx/releases/tv)
- [JetStream](https://github.com/android/tv-samples/tree/main/JetStreamCompose)video streaming sample app
- [JetCaster](https://github.com/android/compose-samples/tree/main/Jetcaster/tv-app)audio streaming sample app
- [Component samples](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:tv/samples/src/main/java/androidx/tv/samples/)