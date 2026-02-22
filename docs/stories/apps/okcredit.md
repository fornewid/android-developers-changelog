---
title: https://developer.android.com/stories/apps/okcredit
url: https://developer.android.com/stories/apps/okcredit
source: md.txt
---

# OkCredit’s average merchant transaction goes up by 30% after reducing ANR

OkCredit is a credit account management app for millions of shop owners and their customers in India. With 140M transactions month over month, and 50M+ downloads, last year alone saw OkCredit recording $50 billion worth of transactions on the app.

Considering the scale that OkCredit operated in, and the millions of businesses that depend on its app for managing their accounts, it is imperative that OkCredit ensures a smooth and seamless experience for all its users, irrespective of the device they are using.

Users reward the best performing apps with positive reviews and high ratings. An app that has stability or performance issues often leads to frustration and even worse, bad ratings. This makes ANRs (Application Not Responding) an important performance metric to track if you're aiming to delight your users and give them a consistently good user experience.

OkCredit's investments in improving Android Vitals, like reducing ANR and improving app startup time led them to reap dividends, especially on low-end devices (which are already resource limited). They saw both improvements in customer retention as well as merchant transactions on the app.

## The Challenge

One of the key segments for OkCredit were users on low-end devices. These devices are resource limited and running taxing tasks on them can easily create a sub-optimal user experience. For example, a major maintenance challenge was tracking and adding instrumentation for ANRs. The goal was to address these issues with the aim of improving the overall user experience and increasing merchant transactions.

## What did they do?

Reducing ANR and improving app startup times for an app like OkCredit meant happy customers and moreover an increase in merchant transactions on the app.

The most important clue in debugging an ANR is finding out what the main thread was doing when the ANR happened. Working with feedback from Google, OkCredit created a structured approach for identifying these ANRs.

- Monitored performance using Android Vitals and used custom reporting on Firebase Crashlytics to learn about ANRs
- Optimized initialization of third party libraries from App start, by moving these to a background thread
- Used tools like Systrace and Profiler to identify ANRs in broadcast receivers and Services. Macrobenchmark on CI also helped benchmark cold startups.
- Using method profiler, objects were identified to be loaded lazily.
- Using perfetto, high inflation layouts were identified.
- ANR in shared preferences were solved by changing all apply() to commit() in a background thread.

The above tasks were validated to confirm their impact by comparing metrics or using tools such as systrace, CPU profiler etc.

## The Results

Beyond improving metrics and the user experience, the OkCredit development team gained insights that helped them improve their development process going forward.  
![](https://developer.android.com/static/images/distribute/stories/OkCredit.png)

- On low-end devices -
  - Reduced ANR by 60%
  - Improved Day 1 customer retention of low-end devices by about 22%
  - The average transaction for each merchant increased by 30%
- Improved app rating from 4.3 to 4.6 on the Play Store
- Cold startup time improved by \~70%
- Saw 60 % improvement in user click to full draw of first frame on any screen

This exercise has brought the team together to create best practices and encouraged them to focus on improving the user experience. The team has started using tools like Perfetto and CPU profiler during development itself in order to improve their understanding of the system and make decisions faster.
> "Focusing on reducing ANRs has helped us differentiate ourselves by offering a delightful experience. This has led to increased retention, and reduced churn. Additionally, due to the teams' engineering excellence, practices such as these have a profound influence on organization's culture. This makes us proud as a team, and company setting new benchmarks of app performance in the nascent Indian SMB digitisation industry."
>
> **-- Gaurav Kunwar (Cofounder \& CPO - OkCredit)**