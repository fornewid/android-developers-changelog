---
title: Add inking to your app with the Ink API  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/about-ink-api
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add inking to your app with the Ink API Stay organized with collections Save and categorize content based on your preferences.



The [`Ink API`](/jetpack/androidx/releases/ink) helps you
add beautiful, low-latency freehand drawing to your Android app. Ink API
simplifies the complexities of input handling and graphics rendering, allowing
you to quickly implement responsive drawing surfaces for styluses and other
pointer inputs.

The API uses the
[Jetpack Graphics Library for low latency](/jetpack/androidx/releases/graphics) to help
provide the smoothest and most responsive inking experience possible.

The Ink API uses Google's [Ink](https://github.com/google/ink) library as the core of its
implementation. Jetpack supports using the Ink API on all supported Android
architectures. You can use Ink API modules that aren't Android-specific in
server-side JVM code under Linux for x86\_64. This enables high-fidelity
server-side rendering, ensuring that digital ink looks identical across mobile
previews and exported documents like PDFs or PNGs.