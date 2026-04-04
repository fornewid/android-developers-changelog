---
title: https://developer.android.com/stories/apps/monzo-compose
url: https://developer.android.com/stories/apps/monzo-compose
source: md.txt
---

[Monzo](https://monzo.com/) is a bank and app offering
digital financial services. Their mission is to make money work
for everyone. Monzo's design system started to deviate from Material Design so
they wanted an **easy way to write and maintain custom components** that are
constantly evolving---so they chose Jetpack Compose.

## What they did

With Compose the Material Design components are provided as a layer over the
design-system-agnostic foundation APIs. Monzo used the foundation APIs to build
their own component library, using the Material components as reference. They
started by migrating a screen at a time, now using Compose in all new screens.
Now, Compose is used in production, by all of the Android engineers: *"We
didn't encounter any major problems, and so we felt confident enough to start
using it for some select new features, and eventually for all new features."*

## Results

The Monzo team created components that enable them to easily build new
screens: *"The components we provide out of the box make building a screen
while learning Compose a **much smoother experience**. The slot-based APIs is a
fantastic pattern that makes it really easy for us to build larger components
out of lots of small building blocks."*

With Compose, the Monzo team were able to build a higher quality app, adding
delightful features that previously they couldn't get to in their
sprints: *"One example is animations - they're so easy to add in Compose that
**there's very little reason not to animate things** like color/size/elevation
changes. These 'nice to have' animations are often too difficult to be worth
the effort and complexity in the View system."*

Their code is now shorter, and it's easier to read, understand, and
maintain: *"Declarative code is **much easier to reason about** than code that
manipulates a mutable UI hierarchy. It's also much **easier to trace through code**
when it's all written in the same language and often the same file, rather than
jumping back and forth between Kotlin and XML. Don't even get me started on XML
themes and styles! **Theming is a lot easier to understand** in Compose. Our theme
only consists of the properties we define, the values are consistent across
devices, and because it's in Kotlin it is really easy to search and follow in
the IDE."*

Compose allowed the Monzo team to easily test their app and ensure their app is
accessible: *"It's helped us **write tests that are less fragile, run reliably,
and give us a lot of confidence** that our app actually works in the hands of our
users. Testing through the semantics system also ensures that our screens are
at least reasonably **accessible by default**."*

## Get started

Learn more about [Compose](https://developer.android.com/jetpack/compose).