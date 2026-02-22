---
title: https://developer.android.com/stories/apps/twitter-kotlin
url: https://developer.android.com/stories/apps/twitter-kotlin
source: md.txt
---

# Twitter increases developer productivity and code reliability with Kotlin

![](https://developer.android.com/static/images/distribute/stories/twitter-logo.png)

[Twitter](https://play.google.com/store/apps/details?id=com.twitter.android&hl=en)
is one of the most widely used social media platforms where users can see what's
happening in the world at any given moment.
The engineering team introduced Kotlin in 2017 with the goal of making their
codebase more maintainable and their Android app more reliable as a result of
Kotlin's [null safety features](https://developer.android.com/kotlin/common-patterns#nullability).

## What they did

The team initially introduced Kotlin into [Periscope](https://play.google.com/store/apps/details?id=tv.periscope.android&referrer)'s
codebase and into the Periscope feature of the Twitter app, and were able to
test the benefits and tradeoffs of using Kotlin. Impressed with the improvements
to productivity and code reliability, they gradually began adding Kotlin to
other features of the Twitter app.

Kotlin has helped Twitter decrease the amount of code in their app,
minimizing boilerplate maintenance and **enabling the team to be more
productive.** They used language features such as data classes, sealed
classes, and default parameters, which allowed them to be able to write less
code, and faster. Kotlin's smart casting has also reduced the amount of code
their team needs to write and maintain.

*"Kotlin is a joy to use. The reduction in boilerplate reduces the amount of
code we need to write." - Andy Fox, Senior Software Engineer at Twitter*

Kotlin's null safety features have also increased Twitter's code reliability.
Initially when the team introduced Kotlin, they uncovered silent failures that
had previously gone undetected. Compile time null checking allows the team to
**detect issues sooner, and handle nullability errors more
proactively.**

## Results

After adopting Kotlin, the team has continued to see excellent system health
and performance for their app. At the same time, they've improved their team's
productivity and made their app safer by catching critical errors at compile
time instead of runtime. With the increases in productivity and code
reliability, the team has decided to write many new features such as Fleets,
DM Reactions, and Lists in Kotlin.

## Get started

Learn more about [developing an Android app with Kotlin](https://developer.android.com/kotlin).