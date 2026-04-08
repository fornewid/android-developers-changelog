---
title: https://developer.android.com/develop/background-work
url: https://developer.android.com/develop/background-work
source: md.txt
---

# Background Work

![](http://developer.android.com/static/images/cluster-illustrations/mad.svg)  

### Background work

Background work is any task your app needs to perform when it's not visible in the foreground, such as fetching data from a server or processing images.

Navigating the complexities of background execution is key to building apps that are "good citizens"---that is, resilient, responsive, and efficient applications that work well on all devices.  
[About background tasks](http://developer.android.com/develop/background-work/background-tasks)

## Get started with background work

View the guide on choosing the right background work API for your use case, and consider it in the context of Android's process and app lifecycle.  
[![](http://developer.android.com/static/images/cluster-illustrations/apis.svg)](http://developer.android.com/develop/background-work/background-tasks#choose-right-option)  
Guide

### [Choose the right option](http://developer.android.com/develop/background-work/background-tasks#choose-right-option)

Choosing the right background work API can be complex. This page gives you clear guidance on when to use asynchronous work, WorkManager, foreground services, or an alternative choice. Learn which API is best for your specific use case.  
[View the guide](http://developer.android.com/develop/background-work/background-tasks#choose-right-option)  
[![](http://developer.android.com/static/images/picto-icons/pathway-2.svg)](http://developer.android.com/guide/components/activities/process-lifecycle)  
Guide

### [Process and app lifecycle](http://developer.android.com/guide/components/activities/process-lifecycle)

Explore the fundamental concepts of the Android process lifecycle and how it impacts your app's behavior and resource management. Learn how the system manages app processes based on activity state, enabling you to design resilient and efficient applications that respond gracefully to system-initiated terminations.  
[View the guide](http://developer.android.com/guide/components/activities/process-lifecycle)![](http://developer.android.com/static/images/picto-icons/brackets.svg)  

## Key solutions

Some of the more common APIs and tools for performing work in the background, include WorkManager, foreground services, alarms, and broadcasts. Each solution will have varying implications for the battery life of your users's devices.  

### [WorkManager](http://developer.android.com/develop/background-work/background-tasks/persistent)

WorkManager is the recommended solution for persistent background work on Android. Learn how to use this powerful library to schedule tasks that persist across app restarts and device reboots, and understand its key features for handling constraints and flexible retry policies.  
[Learn more](http://developer.android.com/develop/background-work/background-tasks/persistent)  

### [Foreground Services](http://developer.android.com/develop/background-work/services/fgs)

Foreground services offer a powerful way to run tasks immediately that out not to be interrupted. Learn when and how to declare, launch, and stop a foreground service with a persistent notification, ensuring your app performs critical tasks without being terminated by the system.  
[Learn more](http://developer.android.com/develop/background-work/services/fgs)  

### [Alarms](http://developer.android.com/develop/background-work/services/alarms)

Alarms are a critical tool for scheduling time-based work. This page explains how to use AlarmManager to schedule both exact and inexact alarms for tasks that must run at a specific time or within a given window, even when your app is not running. It also covers best practices for managing alarms and ensuring they are optimized for battery life.  
[Learn more](http://developer.android.com/develop/background-work/services/alarms)  

### [Broadcasts](http://developer.android.com/develop/background-work/background-tasks/broadcasts)

Learn how to send and receive broadcasts to handle system events and messages from other apps. You'll also learn about context-registered and manifest-declared receivers and the modern system restrictions that apply to them.  
[Learn more](http://developer.android.com/develop/background-work/background-tasks/broadcasts)![](http://developer.android.com/static/images/picto-icons/professional.svg)  

## Background guidance by use case

The right solution varies by your use case. Android provides many task-specific APIs, which are optimized for particular scenarios, and will often lead to greater power savings and fewer restrictions than when using WorkManager and Foreground Services.

This section lists some of the more common use cases, and the recommended solution.  
[![](http://developer.android.com/static/images/spot-icons/location.svg)](https://developers.google.com/location-context/fused-location-provider)  

### [Location](https://developers.google.com/location-context/fused-location-provider)

Most use cases only require location when the user is engaging with the app. However, if your app needs to access location in the background, use the Fused Location Provider API. Leverage this API to get the cached last known location, or request periodic location updates.  
[![](http://developer.android.com/static/images/picto-icons/ui-elements.svg)](http://developer.android.com/develop/ui/compose/glance/glance-app-widget)  

### [Widgets](http://developer.android.com/develop/ui/compose/glance/glance-app-widget)

Update GlanceAppWidgets efficiently when the app is in the background by using the update method.  
[![](http://developer.android.com/static/images/picto-icons/sync-2.svg)](http://developer.android.com/develop/connectivity/bluetooth/ble/background)  

### [Bluetooth and Connected Devices](http://developer.android.com/develop/connectivity/bluetooth/ble/background)

Use Bluetooth Low Energy (BLE) to communicate with peripheral devices in the background. Learn how to scan, connect, and maintain a persistent connection to devices while respecting system-level restrictions and conserving battery.[![](http://developer.android.com/static/images/picto-icons/health-connect-logo.svg)](http://developer.android.com/health-and-fitness/guides/health-connect)  

### [Step Tracking](http://developer.android.com/health-and-fitness/guides/health-connect)

For tracking steps on mobile devices, consider reading steps from Health Connect, the Android data store for Health \& Fitness data.  
[![](http://developer.android.com/static/images/picto-icons/send-data.svg)](http://developer.android.com/develop/background-work/background-tasks/uidt)  

### [User-Initiated Data Transfer](http://developer.android.com/develop/background-work/background-tasks/uidt)

For user-initiated background tasks that involve data transfer (including download and upload) and are meant to keep the user informed on progress, use the User-Initiated-Data Transfer Job type. This job type is optimized for long-running data transfers, and is granted priority by the system.  
[![](http://developer.android.com/static/images/picto-icons/storage.svg)](http://developer.android.com/media/media3/session/background-playback)  

### [Media Playback](http://developer.android.com/media/media3/session/background-playback)

Use the Media3 library to support background playback while your app is not visible to the user.![](http://developer.android.com/static/images/picto-icons/lightning.svg)  

## Understand power optimizations

Considering your background work's effects on power is crucial for creating high-quality Android apps. It allows you to build more resilient and battery-efficient apps by understanding how the system manages resources. Optimizing for power reduces battery drain, prevents your app from being terminated by the system, and delivers a smoother user experience.  
Guide

### [Understand Power Management Resource Limits](http://developer.android.com/topic/performance/power/power-details)

The system prioritizes apps' requests for resources based on the device state, app state and the app's standby bucket.

Learn more about how your app can work within the device's power management resource limits to reliably execute work in the background.  
[View the guide](http://developer.android.com/topic/performance/power/power-details)  
Guide

### [Keep the Device Awake](http://developer.android.com/develop/background-work/background-tasks/awake)

Your app may need to keep the device's CPU from going into the suspended state in order to complete critical work. This guide helps you select the most appropriate methods for keeping a device awake.  
[View the guide](http://developer.android.com/develop/background-work/background-tasks/awake)  
Guide

### [Optimize for doze and standby](http://developer.android.com/training/monitoring-device-state/doze-standby)

Learn how to adapt your app to Doze and App Standby to improve battery efficiency and enhance the user experience. By understanding these power-saving modes, you can ensure your app runs optimally while minimizing its impact on device battery life.  
[View the guide](http://developer.android.com/training/monitoring-device-state/doze-standby)  
Guide

### [Test power-related issues](http://developer.android.com/topic/performance/power/test-power)

Beginning with Android 9, devices have power-management features that affect all apps. Learn how to test your app to make sure it runs properly on all devices, including with features such as battery saver, App Standby Buckets, and background restrictions.  
[View the guide](http://developer.android.com/topic/performance/power/test-power)

## Latest news