---
title: https://developer.android.com/stories/apps/sharechat
url: https://developer.android.com/stories/apps/sharechat
source: md.txt
---

# ShareChat addresses Jank issues to increase feed scrolling by 60%

## Introduction

ShareChat is a leading social media platform in India that allows users to share their opinions, document their lives, and make new friends in their native language. Other features include chatrooms, and private messaging, enabling users to share videos, jokes, songs and other language-based social content. On a mission to spearhead India's internet revolution, ShareChat is changing how the next billion users will interact on the internet.

The app in numbers

- **100 Million+** downloads
- **180 Million+** Monthly Active Users
- **32 Million+** content creators
- **15** different Indian languages
- **\~1.5** Million posts created daily

## The Challenge

As ShareChat grew to be loved by thousands of people daily, the app faced a challenge in consistently delivering new frames leading to poor response times that impeded user experience.

As a result, the app saw an increased number of dropped or delayed frames (also known as "Jank"). Fixing these jank issues by improving slow \& frozen frames was critical in delivering a seamless experience to all its users. This would also play an important role in making users spend more time on the app, increasing engagement and, in turn, improving ShareChat's rating on the Android Play Store.

## How They Did It

ShareChat worked with Google's developer relations team to reduce Jank and yield a positive business impact by improving slow \& frozen frames (Jank) on the app. Specifically they worked on improving the following issues -

- **Shared RecyclerView Pool** - Through profiling, it was observed that creating different viewholders takes longer and to minimize that, a Shared RecyclerView Pool was created. This also helped in removing the viewholders creational cost for similar feeds.

- **Excessive Layout Passesl** - Through [profiling](https://perfetto.dev/), it was also observed that some viewholders were requesting additional requestLayouts. To optimize, the code was updated to take value in creation time instead of every bind, thus saving extra requestLayout costs.

- **[OverDraw](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering)** - Simplified the layouts to reduce layering and removing colors that were being set separately for each of the layers.

- **Flattening of hierarchy** - Observed long inflation through profiling and manual inspection of many screens. The hierarchy was flattened using [ConstraintLayout](https://developer.android.com/reference/androidx/constraintlayout/widget/ConstraintLayout) to solve for this.

- **Excessive View Inflation** - Identified long inflation time for certain views while profiling. These views were converted to viewstubs.

- **Removing heavy tasks from UI thread** - Using a profiler allowed for observation of a couple of places where heavy tasks were being done on the main thread, such as creating SpannableStringBuilder with tagging and styling of every recyclerView bind, BlurHash decoding, etc. These tasks were removed from the UI thread and moved to a background thread.

- **Migrating from Rx to [Coroutine](https://developer.android.com/kotlin/coroutines#:%7E:text=A%20coroutine%20is%20a%20concurrency,established%20concepts%20from%20other%20languages)** - Memory consumption also led to frequent GC calls, and there were very high thread counts via the \>100 RX thread. Many of the use cases were moved to Coroutine to fix these issues.

- **Adoption of [Coil](https://coil-kt.github.io/coil/) for image loading** - Glide was causing issues while loading images, specifically in the components built via jetpack compose. It was also identified that while loading images in LazyColumn, the rendering threshold bar was high. These occurrences led to the adoption of Coil for image loading.

- **Old code cleanup and refactoring** - Removal of old code and experiments helped to remove unnecessary hidden views from the UI and helped rewrite some of the screens in a better way.

## Results

By analyzing improvement areas and identifying optimization strategies, ShareChat could improve the overall experience for users while increasing its engagement rate and Play Store ratings. Below is the quantitative overview of the results ShareChat achieved -

- \~45% reduction in 'Slow rendered' frames on Play Store
- \~30% reduction in 'Frozen' frames on Play Store
- Janky frame rates for every 10K frames rendered reduced from 10.72% to 3.98%
- Feed-scrolling increased by 60%
- The overall ratings on the Store increased from \~4.0 to 4.3
- 10% increase in consumption of posts

> "At ShareChat, our goal is to be the best social media app out there that
> delights our users.This also means being the best in terms of app performance.
> Our collaboration with Google's developer relations team helped us identify
> areas of improvement on our most used low-end user devices. We learned the best
> performance practices and tools to identify and fix frozen frames, janks,
> overdraws, and ANRs."
>
> **-- Vihaan Verma, Engineering Manager, Android Team at ShareChat**