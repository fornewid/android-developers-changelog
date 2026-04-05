---
title: Use wake locks  |  Background work  |  Android Developers
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Background work](https://developer.android.com/develop/background-work)
* [Guides](https://developer.android.com/develop/background-work/background-tasks)

# Use wake locks Stay organized with collections Save and categorize content based on your preferences.



When it's necessary, you can use wake locks to keep the device from going to
sleep.

Under some circumstances, you may need to keep the device awake even when your
app is in the background. To do this, you can create a *wake lock*.

Your feedback is a crucial part of improving our documentation. Please give us
your feedback using the following link:

[Give feedback](https://docs.google.com/forms/d/e/1FAIpQLSc0OMFG-G88ZyHh_xwauaM2gimwP9-MFvRd6C49q0atZNpZ9w/viewform?usp=dialog)

**Note:** Creating and holding wake locks can have a dramatic impact on the device's
battery life. You shouldn't use wake locks if there are any suitable
alternatives. For other options, see the
[Choose the right API to keep the device awake](/develop/background-work/background-tasks/awake)
documentation. If you do need to use a wake lock, make sure to hold it for as
short a time as possible.

This guide explains the following areas:

* [Set a wake lock](/develop/background-work/background-tasks/awake/wakelock/set)
* [Release a wake lock](/develop/background-work/background-tasks/awake/wakelock/release)
* [Follow wake lock best practices](/develop/background-work/background-tasks/awake/wakelock/best-practices)
* [Debug wake locks locally](/develop/background-work/background-tasks/awake/wakelock/debug-locally)
* [Identify and optimize wake lock use cases](/develop/background-work/background-tasks/awake/wakelock/identify-wls)

This guide assumes you're familiar with the following topics:

* [Choose the right API to keep the device awake](/develop/background-work/background-tasks/awake)
* [Request runtime permissions](/training/permissions/requesting)