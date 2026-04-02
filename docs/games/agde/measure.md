---
title: Measure app performance  |  Android game development  |  Android Developers
url: https://developer.android.com/games/agde/measure
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Measure app performance Stay organized with collections Save and categorize content based on your preferences.




You can measure the performance of your app using a standalone version of the
Android Studio Profiler. To start the profiler, do the following:

1. Run the debugger.
2. Click the profiler ![Profiler icon](/static/images/agde/profile-button.png)
   button in the Visual Studio toolbar.
3. Next to **SESSIONS**, click the + button and select a debuggable process.

   ![Select debuggable process](/static/images/agde/profile-demo-app.png)  
   **Figure
   1**. Select a process in the profiler

The profiler displays real time usage statistics for the following categories:
CPU, memory, network, and energy.

![Profiler statistics](/static/images/agde/profile-usage.png)  
**Figure
2**. Profiler statistics for the sample endless tunnel app

For more details on a certain category, click the graph for that category.

![Profiler memory statistics](/static/images/agde/profile-memory-categories.png)  
**Figure
3**. Detailed memory statistics

For more information on how to use the profiler, see the [Android Studio
Profiler documentation](/studio/profile).






Send feedback