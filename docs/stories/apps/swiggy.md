---
title: https://developer.android.com/stories/apps/swiggy
url: https://developer.android.com/stories/apps/swiggy
source: md.txt
---

# Swiggy boosts user interaction by 50% after addressing Jank issues on their Android app

## Introduction

Swiggy is India's leading on-demand convenience platform with a tech-first approach to logistics and a solution-first approach to consumer demands.

Swiggy currently holds an impressive resume;

- **100M+**Installs on Android
- Active in**500+**cities
- **270k+**delivery executives
- **185k+**restaurant partners
- Delivering \>**1M+**orders daily

Built on the back of robust**ML technology** and fuelled by**terabytes of data processed every day**, Swiggy offers a fast, seamless and reliable delivery experience for millions of customers across India.

## The challenge

As a brand that provides convenience to consumers on a day to day basis, Swiggy's tech team's goal is to make the ordering experience as convenient and seamless as possible. As the team proceeded to analyse and identify areas of improvement, one area that stood out was that, while the app worked well for most of their users, they still had a lot of room to improve, especially for users experiencing jank (skipped frames from slow UI rendering) with**mid to low-end devices**.

With their next version of the UX on the way,**dev, and QA** time were important. This resulted in**time-sharing** between**feature development** and**performance improvements**, which required picking and choosing the improvements they wanted to release that quarter.

After observing and understanding the major pain points in the UX, they decided that they wanted to make sure that a user's discovery experience was as**seamless** as possible, by taking out any Janks and distractions in their**Home to Menu to Cart funnel**.

So, in H2 2021,**Swiggy and the Android DevRel team at Google** got together to work on**reducing Jank on the Swiggy app**for a smooth and uninterrupted user experience.

## How they did it

To counteract the slow launch time and jank problems that the Swiggy app was facing while scrolling the discovery pages, the right tools needed to be identified and applied.

Google's analysis helped them get started in the right direction. By helping them with the right tools like**Perfetto and gfxinfo**, the process was accelerated.

**Google Play Vitals**were used to monitor the app's Launch and Rendering performance. Through the vitals dashboard, they were able to confirm that the changes being made were leading to a significant impact on the end UX.

At the same time,**Firebase crashlytics**helped them catch performance-related crashes and non-fatal errors early. Because of this, they were able to identify some errors related to instrumentation very early into the release and raised hotfixes immediately.

Tools such as**Perfetto, Android Studio Profiler, Layout Inspector** and**gfxinfo**were then used to improve launch time to identify inflated views that needed to be placed in ViewStubs, to recognize layouts which had very large inflation times and to overall measure the app's Jank.

With the constant guidance that Android DevRel (ADR) provided regarding performance queries, they were able to move quickly and make progress in record times. They took in many of ADR's recommendations, made during the analysis, and worked on top of that to**deliver the best possible UX for their users**.

## Results

With their arsenal of tools, Swiggy was able to improve their**Application load time, Main activity load time, and also reduce Jank in Menu/Search pages** . All of this led to some significant improvements in their**Time to Interactive engagement metric**.  
![](https://developer.android.com/static/images/distribute/stories/swiggy_app.png)

- Bounce rate decreased by \~28%
- Additional 11M+ INR revenue per month
- Getting to the homepage and browsing their favorite restaurants was improved by \~50%.

|----------------------|---------|
| Vitals improved by the following percentages: ||
| **Slow Cold Start:** | -50.54% |
| **Slow Warm Start:** | -51.59% |
| **Slow Hot Start:**  | -17.68% |
| **Slow Frames:**     | -58.97% |
| **Frozen Frames:**   | -19.66% |

With**Jank reduction** , users are now able to**discover more restaurants** , with**less friction**.

All in all, this**increased user engagement and satisfaction** , leading to Swiggy app users being quite vocal with their**positive feedback on various social media platforms**.

This further reinforced Swiggy's belief that**focus on App experience** is one of the crucial elements for any app that wants**to serve millions of users everyday**.

As for the future, creating a**top notch user experience and expanding their consumer base**is their top priority.
> "Providing an unparalleled consumer experience across all categories is the core focus area for the Consumer Apps team at Swiggy. We strongly believe a highly performant app can help in delivering an engaging and delightful experience for our end users. Hence making that experience fluid, seamless and super fast is the most important thing. We started working with the Google Dev relations team on improving our critical App vitals and improved all metrics significantly in a short time. Our goal is to make the Swiggy App as the benchmark for app experiences across the industry."
>
> **-- Tushar Tayal, Senior Engineering Manager**