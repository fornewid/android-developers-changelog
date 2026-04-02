---
title: https://developer.android.com/stories/apps/twitter-compose
url: https://developer.android.com/stories/apps/twitter-compose
source: md.txt
---

[Twitter](https://twitter.com) is one of the most widely used social
media platforms where users can see what's happening in the world at any given
moment. The engineering team started using Jetpack Compose to **modernise their
design system.**

## What they did

Because the Twitter app's UI components and theming system was developed around
10 years ago and was comprised of legacy components that required tremendous
maintenance efforts, the engineering team wanted to build a new, scalable
design system; with stateless UI components that were easy to use and maintain;
and intuitive to implement, extend and customize, so they decided to use
Compose.

The team started a component-by-component replacement through their internal
design system and by introducing Compose into new screens that don't depend on
their legacy setup.

## Results

Compose provided a solid answer to their goal of improving developer velocity,
developer happiness, and UI code/component maintainability. After starting to
use Compose, Twitter engineers say that it's *"In a word: incredible.
Internally we refer to it as Android UI 2.0, and it makes it very difficult to
delve back into our legacy view system. It has **increased our efficiency and
velocity** for things we've developed specifically in Compose."*

They've seen improvements in the speed of development and experimentation: *"The
**turn-around on design changes** for anything we've adopted in Compose **is much
faster** than we would have experienced previously. Additionally, we experiment
very heavily within our product changes, and this is facilitated much better
and quicker when written in Compose and Kotlin."*

The code they write is not only more intuitive, but also faster to write, and easier to
read: *"Additionally, **our theming layer is vastly more intuitive and legible**
and we've been able to accomplish within a single Kotlin file what otherwise
extended across multiple XML files that were responsible for attribute
definitions and assignments via multiple layered theme overlays. Reimplementing
our entire theming structure within the context of Compose took only a matter
of days to weeks, and has already proven to be much **more robust and intuitive**
than our legacy theme system ever has been."*

## Get started

Learn more about [Compose](https://developer.android.com/jetpack/compose).