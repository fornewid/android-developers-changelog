---
title: https://developer.android.com/training/sync-adapters
url: https://developer.android.com/training/sync-adapters
source: md.txt
---

# Transfer data using sync adapters

**Note:** We recommended [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)
as the recommended solution for most background processing use cases. Please reference the
[background processing guide](https://developer.android.com/guide/background) to learn which solution works best for you.


Synchronizing data between an Android device and web servers can make your application
significantly more useful and compelling for your users. For example, transferring data to a web
server makes a useful backup, and transferring data from a server makes it available to the user
even when the device is offline. In some cases, users may find it easier to enter and edit their
data in a web interface and then have that data available on their device, or they may want to
collect data over time and then upload it to a central storage area.


Although you can design your own system for doing data transfers in your app, you should
consider using Android's sync adapter framework. This framework helps manage and automate data
transfers, and coordinates synchronization operations across different apps. When you use
this framework, you can take advantage of several features that aren't available to data
transfer schemes you design yourself:


Plug-in architecture
:
    Allows you to add data transfer code to the system in the form of callable components.


Automated execution
:
    Allows you to automate data transfer based on a variety of criteria, including data changes,
    elapsed time, or time of day. In addition, the system adds transfers that are unable to
    run to a queue, and runs them when possible.


Automated network checking
:
    The system only runs your data transfer when the device has network connectivity.


Improved battery performance
:
    Allows you to centralize all of your app's data transfer tasks in one place, so that they
    all run at the same time. Your data transfer is also scheduled in conjunction with data
    transfers from other apps. These factors reduce the number of times the system has to
    switch on the network, which reduces battery usage.


Account management and authentication
:
    If your app requires user credentials or server login, you can optionally
    integrate account management and authentication into your data transfer.


This class shows you how to create a sync adapter and the bound [Service](https://developer.android.com/reference/android/app/Service) that
wraps it, how to provide the other components that help you plug the sync adapter into the
framework, and how to run the sync adapter to run in various ways.


**Note:** Sync adapters run asynchronously, so you should use them with the
expectation that they transfer data regularly and efficiently, but not instantaneously. If
you need to do real-time data transfer, you should do it in an [AsyncTask](https://developer.android.com/reference/android/os/AsyncTask) or
an [IntentService](https://developer.android.com/reference/android/app/IntentService).

## Lessons


**[Create a stub authenticator](https://developer.android.com/training/sync-adapters/creating-authenticator)**
:
    Learn how to add an account-handling component that the sync adapter framework expects to be
    part of your app. This lesson shows you how to create a stub authentication component for
    simplicity.


**[Create a stub content provider](https://developer.android.com/training/sync-adapters/creating-stub-provider)**
:
    Learn how to add a content provider component that the sync adapter framework expects to be
    part of your app. This lesson assumes that your app doesn't use a content provider, so it
    shows you how to add a stub component. If you have a content provider already in your app,
    you can skip this lesson.


**[Create a sync adapter](https://developer.android.com/training/sync-adapters/creating-sync-adapter)**
:
    Learn how to encapsulate your data transfer code in a component that the sync
    adapter framework can run automatically.


**[Run a sync adapter](https://developer.android.com/training/sync-adapters/running-sync-adapter)**
:
    Learn how to trigger and schedule data transfers using the sync adapter framework.