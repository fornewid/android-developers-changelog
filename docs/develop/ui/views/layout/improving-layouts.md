---
title: https://developer.android.com/develop/ui/views/layout/improving-layouts
url: https://developer.android.com/develop/ui/views/layout/improving-layouts
source: md.txt
---

# Improve layout performance

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to work with layouts in Compose.  
[Performance in Compose →](https://developer.android.com/jetpack/compose/performance)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)  

Layouts are a key part of Android applications that directly affect the user experience. If implemented poorly, your layout can make your app memory-intensive with slow UIs. The Android SDK includes tools to help identify problems in your layout performance. With this documentation, you can implement smooth scrolling interfaces with a minimal memory footprint.

## Lessons

**[Optimize layout hierarchies](https://developer.android.com/develop/ui/views/layout/improving-layouts/optimizing-layouts)**
:   In the same way that a complex web page can slow down load time, a complex layout hierarchy can also cause performance problems. This documentation shows how you can use SDK tools to inspect your layout and discover performance bottlenecks.

**[Reuse layouts with \<include\>](https://developer.android.com/develop/ui/views/layout/improving-layouts/reusing-layouts)**
:   If your application UI repeats certain layout constructs in multiple places, this documentation shows you how to create efficient, reusable layout constructs and include them in the appropriate UI layouts.

**[Load views on demand](https://developer.android.com/develop/ui/views/layout/improving-layouts/loading-ondemand)**
:   Beyond including one layout component within another layout, you might want to make the included layout visible only when it's needed after the activity is running. This documentation shows how you can improve your layout's initialization performance by loading portions of your layout on demand.