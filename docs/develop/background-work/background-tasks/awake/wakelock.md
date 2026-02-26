---
title: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock
url: https://developer.android.com/develop/background-work/background-tasks/awake/wakelock
source: md.txt
---

When it's necessary, you can use wake locks to keep the device from going to
sleep.

Under some circumstances, you may need to keep the device awake even when your
app is in the background. To do this, you can create a *wake lock*.

Your feedback is a crucial part of improving our documentation. Please give us
your feedback using the following link:


[Give feedback](https://docs.google.com/forms/d/e/1FAIpQLSc0OMFG-G88ZyHh_xwauaM2gimwP9-MFvRd6C49q0atZNpZ9w/viewform?usp=dialog)

> [!NOTE]
> **Note:** Creating and holding wake locks can have a dramatic impact on the device's battery life. You shouldn't use wake locks if there are any suitable alternatives. For other options, see the [Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake) documentation. If you do need to use a wake lock, make sure to hold it for as short a time as possible.

This guide explains the following areas:

- [Set a wake lock](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/set)
- [Release a wake lock](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/release)
- [Follow wake lock best practices](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/best-practices)
- [Debug wake locks locally](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/debug-locally)
- [Identify wake locks created by other APIs](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock/identify-wls)

This guide assumes you're familiar with the following topics:

- [Choose the right API to keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake)
- [Request runtime permissions](https://developer.android.com/training/permissions/requesting)