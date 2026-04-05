---
title: https://developer.android.com/stories/apps/jiosaavn
url: https://developer.android.com/stories/apps/jiosaavn
source: md.txt
---

# JioSaavn increases DAUs by improving app startup time by 30%

Founded in 2007, JioSaavn is a leading audio streaming service for music and podcasts. They have 900+ label partnerships and stream 80+ million tracks in 16 languages. JioSaavn app is also available in 6 regional Indian languages.

With a tech stack that supports over 100 million monthly active users (MAUs), JioSaavn operates at scale and speed. This audience usually has resource-limited Android phones, making their user experience of paramount importance to the JioSaavn team.

## The Challenge

Optimizing in an environment of constraints, like those found in low-mid end mobile devices, can be both challenging and exciting from an engineering perspective. The challenge JioSaavn faced was to optimize user experience for their key target audience using low-mid end mobile devices and primarily found in Tier 2 \& 3 cities of India.

Analysing the funnel, it was evident that there was a considerable section of users who would launch the app but not listen to a song. The team determined the app startup time to be the cause for this. Thus, improving the app startup time was associated with an increase in the number of listeners on the app.

## How They Did It

JioSaavn relied on comprehensive analysis and a robust set of tools like Perfetto, dumpsys, etc to analyze this problem and arrive at a sustainable solution. The team approached this challenge using two principles - parallelize work and be lazy.

With the help of Google's analysis, the team prioritized tasks -

- Used systrace and perfetto to study the app flow, analyze pain points, validate improvements in app startup time.
- Delayed initialization: Identified fragments/instances/classes initialization that could be delayed until the homepage is displayed -
  - Ads
  - Music Service (Foreground Service) and Player Resources (e.g. Exoplayer, cached player queue etc)
  - Player Fragment which is minimized at the time of launch.
- On-demand initialization: of various libraries as and when the library is required (eg Facebook lib).
- viewStubs: View Inflation and resource loading was heavy. The team flattened their layouts using viewStubs and converted the images to webP.
- Worker thread: Some tasks which didn't require UI thread were moved to b/g threads to free up the UI thread.
- Split Cache Data - Reading and parsing huge cached data from a file takes a lot of time. The team split it into critical (necessary for showing homepage) and non-critical data.
- Async LayoutInflater: Some of the views required for homepage recyclerview were pre-inflated using Async LayoutInflater.

Tools Used - Perfetto, Systrace, Google play vitals, Android studio Profilers, Firebase performance SDK

## Results

The JioSaavn team released these changes over multiple versions of the app to maintain app stability. They achieved the following results -

- 30% improvement in app startup time on all devices and 35 - 40% in low-mid end devices.
- 5% improvement in Home Screen Viewers/ DAU, thus reducing the bounce rate.

This optimization exercise brought the whole team together. Detailed walkthroughs were done to make the team comfortable with the changes, and inculcate a performance-focused approach towards the app.
> "JioSaavn aims to better the listening experience of our users who come from various regions  
> and cities in India, and span across the spectrum in terms of affordability. Thus going past the mobile connectivity infrastructure of their region, and optimizing the user experience across the users' device capabilities is a constant challenge we work for. Thanks to Google's developer relations guidance, we were able to take a definitive step in this direction."
>
> **-- JioSaavn Product Team**