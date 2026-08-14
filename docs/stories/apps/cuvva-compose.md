---
title: https://developer.android.com/stories/apps/cuvva-compose
url: https://developer.android.com/stories/apps/cuvva-compose
source: md.txt
---

[Cuvva](https://www.cuvva.com/) is making insurance radically better
by giving you a truly flexible way to manage your cover, all from your phone.
The Android engineers at Cuvva got to spend some time re-architecting their app
and decided to adopt a unidirectional data flow and Jetpack Compose. That way
they could **move away from their custom View based design system**, which was
slower and harder to work with, and less predictable on older versions of
Android.

## What they did

The Cuvva team created new design components from scratch, then used the
interoperability APIs to place Composables inside existing layouts and, with
time, replace View-based screens and build new screens with Compose. *"We found
that Compose lets us create new design components from scratch **much more
rapidly** and spend less time trying to work around state management or
fragmentation. Once we had built up a large enough library of these components,
shipping a new screen became very fast, and it has definitely helped us to be
more productive."*

## Results

Compose allowed them to build a higher quality app faster: *"The speed at which
Compose allows us to put together a new feature means **we can iterate more
rapidly, providing a higher-quality experience** for our customers faster than
before."*

With Compose the number of lines you need to write, and therefore read,
understand, and maintain, decreases: *"we were very pleased to see how few lines
were required to create lists or animations in our app. Compose has definitely
**dramatically reduced the number of lines of code** required to build our UI."*

Custom components are easier to implement: *"We created a circular dial
component which is used to show customers their driving score. **Animating** its
progress and colours with Compose was **far easier and a lot more fun** than it
would have been previously. Doing anything custom, whether that's new
components or changing the behaviour of existing ones, is far easier in
Compose."*

## Get started

Learn more about [Compose](https://developer.android.com/jetpack/compose).