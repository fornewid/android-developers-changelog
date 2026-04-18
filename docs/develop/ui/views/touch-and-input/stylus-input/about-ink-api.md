---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/about-ink-api
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/about-ink-api
source: md.txt
---

The [`Ink API`](https://developer.android.com/jetpack/androidx/releases/ink) helps you
add beautiful, low-latency freehand drawing to your Android app. Ink API
simplifies the complexities of input handling and graphics rendering, allowing
you to quickly implement responsive drawing surfaces for styluses and other
pointer inputs.

The API uses the
[Jetpack Graphics Library for low latency](https://developer.android.com/jetpack/androidx/releases/graphics) to help
provide the smoothest and most responsive inking experience possible.

The Ink API uses Google's [Ink](https://github.com/google/ink) library as the core of its
implementation. Jetpack supports using the Ink API on all supported Android
architectures. You can use Ink API modules that aren't Android-specific in
server-side JVM code under Linux for x86_64. This enables high-fidelity
server-side rendering, ensuring that digital ink looks identical across mobile
previews and exported documents like PDFs or PNGs.