---
title: https://developer.android.com/guide/components/activities/tasks-and-back-stack
url: https://developer.android.com/guide/components/activities/tasks-and-back-stack
source: md.txt
---

# Tasks and the back stack

A*task* is a collection of activities that users interact with when trying to do something in your app. These activities are arranged in a stack called the*back stack*in the order in which each activity is opened.

For example, an email app might have one activity to show a list of new messages. When the user selects a message, a new activity opens to view that message. This new activity is added to the back stack. Then, when the user taps or gestures Back, that new activity finishes and is popped off the stack.

<br />

## Lifecycle of a task and its back stack

The device Home screen is the starting place for most tasks. When a user touches the icon for an app or shortcut in the app launcher or on the Home screen, that app's task comes to the foreground. If no task exists for the app, then a new task is created and the[main activity](https://developer.android.com/guide/components/activities/intro-activities#tcoa)for that app opens as the root activity in the stack.

When the current activity starts another, the new activity is pushed on the top of the stack and takes focus. The previous activity remains in the stack, but is stopped. When an activity is stopped, the system retains the current state of its user interface. When the user performs the back action, the current activity is popped from the top of the stack and destroyed. The previous activity resumes, and the previous state of its UI is restored.

Activities in the stack are never rearranged, only pushed onto and popped from the stack as they are started by the current activity and dismissed by the user through the Back button or gesture. Therefore, the back stack operates as a*last in, first out*object structure. Figure 1 shows a timeline with activities being pushed onto and popped from a back stack.
![](https://developer.android.com/static/images/fundamentals/diagram_backstack.png)**Figure 1.**A representation of how each new activity in a task adds an item to the back stack. When the user taps or gestures Back, the current activity is destroyed and the previous activity resumes.

As the user continues to tap or gesture Back, each activity in the stack is popped off to reveal the previous one, until the user returns to the Home screen or to whichever activity was running when the task began. When all activities are removed from the stack, the task no longer exists.

### Back tap behavior for root launcher activities

Root launcher activities are activities that declare an[intent filter](https://developer.android.com/reference/android/content/IntentFilter)with both[`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN)and[`CATEGORY_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER). These activities are unique because they act as entry points into your app from the app launcher and are used to[start a task](https://developer.android.com/guide/components/activities/tasks-and-back-stack#Starting).

When a user taps or gestures Back from a root launcher activity, the system handles the event differently depending on the version of Android that the device is running.

System behavior on Android 11 and lower
:   The system finishes the activity.

System behavior on Android 12 and higher

:   The system moves the activity and its task to the background instead of finishing the activity. This behavior matches the default system behavior when navigating out of an app using the Home button or gesture.

    In most cases, this behavior means that users can more quickly resume your app from a[warm state](https://developer.android.com/topic/performance/vitals/launch-time#warm), instead of having to completely restart the app from a[cold state](https://developer.android.com/topic/performance/vitals/launch-time#cold).

    If you need to[provide custom back navigation](https://developer.android.com/guide/navigation/navigation-custom-back), we recommend using the AndroidX Activity APIs rather than overriding`onBackPressed()`. The AndroidX Activity APIs automatically defer to the appropriate system behavior if there are no components intercepting the system Back tap.

    However, if your app overrides[`onBackPressed()`](https://developer.android.com/reference/android/app/Activity#onBackPressed())to handle Back navigation and finish the activity, update your implementation to call through to`super.onBackPressed()`instead of finishing. Calling`super.onBackPressed()`moves the activity and its task to the background when appropriate and provides a more consistent navigation experience for users across apps.

### Background and foreground tasks

![](https://developer.android.com/static/images/fundamentals/diagram_multitasking.png)**Figure 2.**Two tasks: Task B receives user interaction in the foreground, while Task A is in the background, waiting to resume.

A task is a cohesive unit that can move to the*background* when a user begins a new task or goes to the Home screen. While in the background, all the activities in the task are stopped, but the back stack for the task remains intact---the task loses focus while another task takes place, as shown in figure 2. A task can then return to the*foreground*so users can pick up where they left off.

Consider the following task flow for current Task A that has three activities in its stack, including two under the current activity:

1. The user uses the Home button or gesture, then starts a new app from the app launcher.

   When the Home screen appears, Task A goes into the background. When the new app starts, the system starts a task for that app (Task B) with its own stack of activities.
2. After interacting with that app, the user returns Home again and selects the app that originally started Task A.

   Now, Task A comes to the foreground---all three activities in its stack are intact, and the activity at the top of the stack resumes. At this point, the user can also switch back to Task B by going Home and selecting the app icon that started that task or by selecting the app's task from the[Recents screen](https://developer.android.com/guide/components/recents).

| **Note:** Multiple tasks can be held in the background at once. However, if the user runs many background tasks at the same time, the system might begin destroying background activities to recover memory. If this happens, the activity states are lost.

### Multiple activity instances

![](https://developer.android.com/static/images/fundamentals/diagram_multiple_instances.png)**Figure 3.**A single activity can be instantiated multiple times.

Because the activities in the back stack are never rearranged, if your app lets users start a particular activity from more than one activity, a new instance of that activity is created and pushed onto the stack, rather than bringing any previous instance of the activity to the top. As such, one activity in your app might be instantiated multiple times, even from different tasks, as shown in figure 3.

If the user navigates backward using the Back button or gesture, the instances of the activity are revealed in the order they opened, each with its own UI state. However, you can modify this behavior if you don't want an activity instantiated more than once. Learn more about this in the section about[managing tasks](https://developer.android.com/guide/components/activities/tasks-and-back-stack#ManagingTasks).

### Multi-window environments

When apps run simultaneously in a[multi-windowed environment](https://developer.android.com/guide/topics/ui/multi-window), supported in Android 7.0 (API level 24) and higher, the system manages tasks separately for each window. Each window can have multiple tasks. The same holds true for[Android apps running on Chromebooks](https://developer.android.com/topic/arc): the system manages tasks, or groups of tasks, on a per-window basis.

### Lifecycle recap

To summarize the default behavior for activities and tasks:

- When Activity A starts Activity B, Activity A is stopped but the system retains its state, such as its scroll position and any text entered into forms. If the user taps or uses the Back gesture while in Activity B, Activity A resumes with its state restored.

- When the user leaves a task using the Home button or gesture, the current activity is stopped and its task goes into the background. The system retains the state of every activity in the task. If the user later resumes the task by selecting the launcher icon that began the task, the task comes to the foreground and resumes the activity at the top of the stack.

- If the user taps or gestures Back, the current activity is popped from the stack and destroyed. The previous activity in the stack resumes. When an activity is destroyed, the system*does not*retain the activity's state.

  [This behavior is different for root launcher activities](https://developer.android.com/guide/components/activities/tasks-and-back-stack#back-press-behavior)when your app is running on a device that runs Android 12 or higher.
- Activities can be instantiated multiple times, even from other tasks.

| **Note:** For more about how to design your app's navigation structure for Android, see[Design navigation graphs](https://developer.android.com/guide/navigation/navigation-design-graph).

## Manage tasks

Android manages tasks and the back stack by placing all activities started in succession in the same task, in a last in, first out stack. This works great for most apps, and you usually don't have to worry about how your activities are associated with tasks or how they exist in the back stack.

However, you might decide that you want to interrupt the normal behavior. For example, you might want an activity in your app to begin a new task when it is started, instead of being placed within the current task. Or, when you start an activity, you might want to bring forward an existing instance of it, instead of creating a new instance on top of the back stack. Or you might want your back stack to be cleared of all activities except for the root activity when the user leaves the task.

You can do these things and more using attributes in the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)manifest element and flags in the intent that you pass to[`startActivity()`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)).
| **Caution:** Most apps don't interrupt the default behavior for activities and tasks. If you determine that it's necessary for your activity to modify the default behaviors, use caution and test the usability of the activity during launch and when navigating back to it from other activities and tasks with the Back button or gesture. Also, test for navigation behaviors that might conflict with the user's expectations.

These are the principal`<activity>`attributes that you can use to manage tasks:

- [`taskAffinity`](https://developer.android.com/guide/topics/manifest/activity-element#aff)
- [`launchMode`](https://developer.android.com/guide/topics/manifest/activity-element#lmode)
- [`allowTaskReparenting`](https://developer.android.com/guide/topics/manifest/activity-element#reparent)
- [`clearTaskOnLaunch`](https://developer.android.com/guide/topics/manifest/activity-element#clear)
- [`alwaysRetainTaskState`](https://developer.android.com/guide/topics/manifest/activity-element#always)
- [`finishOnTaskLaunch`](https://developer.android.com/guide/topics/manifest/activity-element#finish)

And these are the principal intent flags that you can use:

- [`FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK)
- [`FLAG_ACTIVITY_CLEAR_TOP`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_CLEAR_TOP)
- [`FLAG_ACTIVITY_SINGLE_TOP`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_SINGLE_TOP)

The following sections discuss how to use these manifest attributes and intent flags to define how activities associate with tasks and how they behave in the back stack.

Also discussed are the considerations for how tasks and activities are represented and managed in the Recents screen. Normally, you let the system define how your task and activities are represented in the Recents screen, and you don't need to modify this behavior. For more information, see[Recents screen](https://developer.android.com/guide/components/recents).

### Define launch modes

Launch modes let you define how a new instance of an activity is associated with the current task. You can define launch modes in two ways, described in the sections that follow:

- [Using the manifest file](https://developer.android.com/guide/components/activities/tasks-and-back-stack#ManifestForTasks)

  When you declare an activity in your manifest file, you can specify how the activity associates with tasks when it starts.
- [Using intent flags](https://developer.android.com/guide/components/activities/tasks-and-back-stack#IntentFlagsForTasks)

  When you call[`startActivity()`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)), you can include a flag in the[`Intent`](https://developer.android.com/reference/android/content/Intent)that declares how (or whether) the new activity associates with the current task.

So, if Activity A starts Activity B, Activity B can define in its manifest how it associates with the current task, and Activity A can use an intent flag to request how Activity B can associate with current task.

If both activities define how Activity B associates with a task, then Activity A's request, as defined in the intent, is honored over Activity B's request, as defined in its manifest.
| **Note:** Some launch modes available for the manifest file aren't available as flags for an intent. Likewise, some launch modes available as flags for an intent can't be defined in the manifest.

#### Define launch modes using the manifest file

When declaring an activity in your manifest file, you can specify how the activity associates with a task using the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)element's[`launchMode`](https://developer.android.com/guide/topics/manifest/activity-element#lmode)attribute.

There are five launch modes you can assign to the`launchMode`attribute:

1.

   `"standard"`
   :   The default mode. The system creates a new instance of the activity in the task it was started from and routes the intent to it. The activity can be instantiated multiple times, each instance can belong to different tasks, and one task can have multiple instances.
2.

   `"singleTop"`
   :   If an instance of the activity already exists at the top of the current task, the system routes the intent to that instance through a call to its[`onNewIntent()`](https://developer.android.com/reference/android/app/Activity#onNewIntent(android.content.Intent))method, rather than creating a new instance of the activity. The activity is instantiated multiple times, each instance can belong to different tasks, and one task can have multiple instances (but only if the activity at the top of the back stack is*not*an existing instance of the activity).

   For example, suppose a task's back stack consists of root activity A with activities B, C, and D on top (so the stack is A-B-C-D, with D on top). An intent arrives for an activity of type D. If D has the default`"standard"`launch mode, a new instance of the class is launched, and the stack becomes A-B-C-D-D. However, if D's launch mode is`"singleTop"`, the existing instance of D receives the intent through`onNewIntent()`, because it's at the top of the stack, and the stack remains A-B-C-D. If, on the other hand, an intent arrives for an activity of type B, then a new instance of B is added to the stack even if its launch mode is`"singleTop"`.
   | **Note:** When a new instance of an activity is created, the user can tap or gesture Back to return to the previous activity. But when an existing instance of an activity handles a new intent, the user can't tap or gesture Back to return to the state of the activity before the new intent arrived in`onNewIntent()`.
3.

   `"singleTask"`
   :   The system creates the activity at the root of a new task or locates the activity on an existing task with the same affinity. If an instance of the activity already exists, the system routes the intent to the existing instance through a call to its[`onNewIntent()`](https://developer.android.com/reference/android/app/Activity#onNewIntent(android.content.Intent))method, rather than creating a new instance. Meanwhile all of the other activities on top of it are destroyed.
   | **Note:** Although the activity starts in a new task, the Back button and gesture still return the user to the previous activity.
4.

   `"singleInstance"`.
   :   The behavior is the same as for`"singleTask"`, except that the system doesn't launch any other activities into the task holding the instance. The activity is always the single and only member of its task. Any activities started by this one open in a separate task.
5.

   `"singleInstancePerTask"`.
   :   The activity can only run as the root activity of the task, the first activity that created the task, and therefore there can only be one instance of this activity in a task. In contrast to the`singleTask`launch mode, this activity can be started in multiple instances in different tasks if the[`FLAG_ACTIVITY_MULTIPLE_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_MULTIPLE_TASK)or[`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_DOCUMENT)flag is set.

| **Note:** `"singleTask"`and`"singleInstancePerTask"`remove all activities that are above the starting activity from the task. For example, suppose a task consists of root activity A with activities B and C. The task is A-B-C, with C on top. An intent arrives for an activity of type A. If A's launch mode is`"singleTask"`or`"singleInstancePerTask"`, the existing instance of A receives the intent through`onNewIntent()`. B and C are finished, and the task is now A.

As another example, the Android Browser app declares that the web browser activity always opens in its own task by specifying the`singleTask`launch mode in the`<activity>`element. This means that if your app issues an intent to open the Android Browser, its activity is*not*placed in the same task as your app. Instead, either a new task starts for the Browser or, if the Browser already has a task running in the background, that task is brought forward to handle the new intent.

Regardless of whether an activity starts in a new task or in the same task as the activity that started it, the Back button and gesture always take the user to the previous activity. However, if you start an activity that specifies the`singleTask`launch mode and an instance of that activity exists in a background task, then that whole task is brought to the foreground. At this point, the back stack includes all activities from the task brought forward at the top of the stack. Figure 4 shows this type of scenario.
![](https://developer.android.com/static/images/fundamentals/diagram_backstack_singletask_multiactivity.png)**Figure 4.** A representation of how an activity with launch mode`"singleTask"`is added to the back stack. If the activity is already part of a background task with its own back stack, then that entire back stack also comes forward, on top of the current task.

For more information about using launch modes in the manifest file, see the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)element documentation.
| **Note:** The behaviors that you specify for your activity with the`launchMode`attribute can be overridden by flags included with the intent that start your activity, as discussed in the next section.

#### Define launch modes using Intent flags

When starting an activity, you can modify the default association of an activity to its task by including flags in the intent that you deliver to[`startActivity()`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)). The flags you can use to modify the default behavior are the following:

[`FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK)

:   The system starts the activity in a new task. If a task is already running for the activity being started, that task is brought to the foreground with its last state restored, and the activity receives the new intent in[`onNewIntent()`](https://developer.android.com/reference/android/app/Activity#onNewIntent(android.content.Intent)).

    This produces the same behavior as the`"singleTask"`[`launchMode`](https://developer.android.com/guide/topics/manifest/activity-element#lmode)value discussed in the preceding section.

[`FLAG_ACTIVITY_SINGLE_TOP`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_SINGLE_TOP)

:   If the activity being started is the current activity, at the top of the back stack, then the existing instance receives a call to`onNewIntent()`instead of creating a new instance of the activity.

    This produces the same behavior as the`"singleTop"``launchMode`value discussed in the preceding section.

[`FLAG_ACTIVITY_CLEAR_TOP`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_CLEAR_TOP)

:   If the activity being started is already running in the current task, then---instead of launching a new instance of that activity---the system destroys all the other activities on top of it. The intent is delivered to the resumed instance of the activity, now on top, through`onNewIntent()`.

    There is no value for the`launchMode`attribute that produces this behavior.

    `FLAG_ACTIVITY_CLEAR_TOP`is most often used in conjunction with`FLAG_ACTIVITY_NEW_TASK`. When used together, these flags locate an existing activity in another task and put it in a position where it can respond to the intent.
    | **Note:** If the launch mode of the designated activity is`"standard"`, it too is removed from the stack and a new instance is launched in its place to handle the incoming intent. That's because a new instance is always created for a new intent when the launch mode is`"standard"`.

### Handle affinities

An*affinity*indicates which task an activity "prefers" to belong to. By default, all the activities from the same app have an affinity for each other: they "prefer" to be in the same task.

However, you can modify the default affinity for an activity. Activities defined in different apps can share an affinity, and activities defined in the same app can be assigned different task affinities.

You can modify an activity's affinity using the[`taskAffinity`](https://developer.android.com/guide/topics/manifest/activity-element#aff)attribute of the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)element.

The`taskAffinity`attribute takes a string value that must be different than the default package name declared in the[`<manifest>`](https://developer.android.com/guide/topics/manifest/manifest-element)element, because the system uses that name to identify the default task affinity for the app.

The affinity comes into play in two circumstances:

1. When the intent that launches an activity contains the[`FLAG_ACTIVITY_NEW_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_TASK)flag.

   A new activity, by default, is launched into the task of the activity that called[`startActivity()`](https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)). It's pushed onto the same back stack as the caller.

   However, if the intent passed to`startActivity()`contains the`FLAG_ACTIVITY_NEW_TASK`flag, the system looks for a different task to house the new activity. Often, this is a new task. However, it doesn't have to be. If there's an existing task with the same affinity as the new activity, the activity is launched into that task. If not, it begins a new task.

   If this flag causes an activity to begin a new task and the user uses the Home button or gesture to leave it, there must be some way for the user to navigate back to the task. Some entities, such as the notification manager, always start activities in an external task, never as part of their own, so they always put`FLAG_ACTIVITY_NEW_TASK`in the intents they pass to`startActivity()`.

   If an external entity that might use this flag can invoke your activity, take care that the user has an independent way to get back to the task that's started, such as with a launcher icon, where the root activity of the task has a[`CATEGORY_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)intent filter. For more information, see the section about[starting tasks](https://developer.android.com/guide/components/activities/tasks-and-back-stack#Starting).
2. When an activity has its[`allowTaskReparenting`](https://developer.android.com/guide/topics/manifest/activity-element#reparent)attribute set to`"true"`.

   In this case, the activity can move from the task it starts in to the task it has an affinity for when that task comes to the foreground.

   For example, suppose an activity that reports weather conditions in selected cities is defined as part of a travel app. It has the same affinity as other activities in the same app, the default app affinity, and it can be re-parented with this attribute.

   When one of your activities starts the weather reporter activity, it initially belongs to the same task as your activity. However, when the travel app's task comes to the foreground, the weather reporter activity is reassigned to that task and displayed within it.

| **Note:** If an APK file contains more than one "app" from the user's point of view, you probably want to use the[`taskAffinity`](https://developer.android.com/guide/topics/manifest/activity-element#aff)attribute to assign different affinities to the activities associated with each "app".

### Clear the back stack

If the user leaves a task for a long time, the system clears the task of all activities except the root activity. When the user returns to the task, only the root activity is restored. The system behaves this way based on the assumption that after an extended amount of time users have abandoned what they were doing before and are returning to the task to begin something new.

There are some activity attributes that you can use to modify this behavior:

[`alwaysRetainTaskState`](https://developer.android.com/guide/topics/manifest/activity-element#always)
:   When this attribute is set to`"true"`in the root activity of a task, the default behavior just described does not happen. The task retains all activities in its stack even after a long period.

[`clearTaskOnLaunch`](https://developer.android.com/guide/topics/manifest/activity-element#clear)

:   When this attribute is set to`"true"`in the root activity of a task, the task is cleared down to the root activity whenever the user leaves the task and returns to it. In other words, it's the opposite of`alwaysRetainTaskState`. The user always returns to the task in its initial state, even after leaving the task for only a moment.

    | **Note:** This attribute is ignored if[`FLAG_ACTIVITY_RESET_TASK_IF_NEEDED`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_RESET_TASK_IF_NEEDED)isn't set.

[`finishOnTaskLaunch`](https://developer.android.com/guide/topics/manifest/activity-element#finish)

:   This attribute is like`clearTaskOnLaunch`, but it operates on a single activity, not an entire task. It can also cause any activity to finish except for the root activity. When it's set to`"true"`, the activity remains part of the task only for the current session. If the user leaves and then returns to the task, it is no longer present.

    | **Note:** This attribute is ignored if[`FLAG_ACTIVITY_RESET_TASK_IF_NEEDED`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_RESET_TASK_IF_NEEDED)isn't set.

### Start a task

You can set up an activity as the entry point for a task by giving it an intent filter with`"android.intent.action.MAIN"`as the specified action and`"android.intent.category.LAUNCHER"`as the specified category:  

    <activity ... >
        <intent-filter ... >
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
        ...
    </activity>

An intent filter of this kind causes an icon and label for the activity to display in the app launcher, giving users a way to launch the activity and to return to the task it creates any time after it launches.

This second ability is important. Users must be able to leave a task and then come back to it later using this activity launcher. For this reason, only use the two launch modes that mark activities as always initiating a task,`"singleTask"`and`"singleInstance"`, when the activity has an[`ACTION_MAIN`](https://developer.android.com/reference/android/content/Intent#ACTION_MAIN)and a[`CATEGORY_LAUNCHER`](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)filter.

Imagine, for example, what might happen if the filter were missing: an intent launches a`"singleTask"`activity, initiating a new task, and the user spends some time working in that task. The user then uses the Home button or gesture. The task is now sent to the background and is not visible. Now the user has no way to return to the task, because it is not represented in the app launcher.

For those cases where you don't want the user to be able to return to an activity, set the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)element's[`finishOnTaskLaunch`](https://developer.android.com/guide/topics/manifest/activity-element#finish)to`"true"`. For more information, see the section on[clearing the back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack#Clearing).

Further information about how tasks and activities are represented and managed in the Recents screen is available in[Recents screen](https://developer.android.com/guide/components/activities/recents).

## More resources

- [Design navigation graphs](https://developer.android.com/guide/navigation/navigation-design-graph)
- [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)
- [Recents screen](https://developer.android.com/guide/components/recents)