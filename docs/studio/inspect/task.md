---
title: https://developer.android.com/studio/inspect/task
url: https://developer.android.com/studio/inspect/task
source: md.txt
---

# Debug your WorkManager workers with Background Task Inspector

The Background Task Inspector helps you visualize, monitor, and debug your app's background workers when using[WorkManager library](https://developer.android.com/jetpack/androidx/releases/work)2.5.0 or higher.

## Get started

To list workers in the Background Task Inspector, do the following:

1. [Run your app](https://developer.android.com/studio/run)on an emulator or connected device running API level 26 or higher.

2. Select**View \> Tool Windows \> App Inspection**from the menu bar.

3. Select the**Background Task Inspector**tab.

4. Select the running app process from the menu.

5. The workers in the currently running app appear in the**Background Task Inspector**pane. Click on the worker that you want to inspect further.

## View and inspect workers

When you deploy an app using WorkManager 2.5.0 or higher on a device running API level 26 or higher, the**Background Task Inspector** tab shows active workers. The**Background Task Inspector** (shown in a[later section](https://developer.android.com/studio/inspect/task#inspect-jobs-alarms-wakelocks)as figure 3) lists the class name, current status, start time, and retries of all jobs, whether they are running, failed, or completed.

### Work Details

Click a job from the list to open the**Work Details**panel, which displays detailed information about the worker, as shown in figure 1.
![Screenshot of the selected Worker's details.](https://developer.android.com/static/studio/images/inspect/worker-detail-window.png)**Figure 1.** **Work Details**panel.

- **Description**: This section lists the worker class name, with the fully qualified package, as well as the assigned tag and the UUID of the worker.
- **Execution**: This section shows the worker's constraints (if any), running frequency, and state, as well as which class created and queued the worker.
- **WorkContinuation**: This section displays where the worker is in the work chain. To check the details of another worker in the work chain, click its UUID.
- **Results**: This section displays the start time, retry count, and the output data of the selected worker.

### Cancel workers

To stop a currently running or enqueued worker, select the worker and click**Cancel Selected Worker** ![](https://developer.android.com/static/studio/images/app-inspection/task_inspector_stop_button.png)from the toolbar.

### View Graph View

Because workers can be chained together, it's sometimes useful to visualize worker dependencies as a graph.

To see a visual representation of a worker chain, select a worker from the table and click**Show Graph View** ![](https://developer.android.com/static/studio/images/app-inspection/task_inspector_graph_view.png)from the toolbar. Only workers are drawn in the graph.
![Screenshot of the Graph view.](https://developer.android.com/static/studio/images/inspect/worker-graph-view.png)**Figure 2.**Graph View.

The graph lets you quickly see relationships between workers and monitor their progress in complex chaining relationships.

To return to the list view, click**Show List View** ![](https://developer.android.com/static/studio/images/app-inspection/task_inspector_list_view.png).

## View and inspect Jobs, Alarms, and Wakelocks

The Background Task Inspector also lets you inspect your app's Jobs, Alarms, and Wakelocks. Each type of asynchronous task appears under the appropriate heading in the inspector tab, letting you easily monitor its status and progress.

Similar to workers, you can select a Job, Alarm, or Wakelock to inspect its detailed information in the Task Details panel.

To view detailed information for a Worker, Job, Alarm, or Wakelock, select it in the**Task Details**panel on the right.
![Screenshot of the Background Task Inspector window.](https://developer.android.com/static/studio/images/inspect/background-task-inspector.png)**Figure 3.**The Background Task Inspector window.**Note:** This functionality has been migrated from the**Energy profiler** . Use the**Background Task Inspector**to inspect all of your app's asynchronous tasks.

## Additional resources

To learn more about the Background Task Inspector, see the following additional resources:

### Documentation

- [Schedule tasks with WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)

### Codelabs

- [Background work with WorkManager](https://developer.android.com/codelabs/android-workmanager)
- [Advanced WorkManager](https://developer.android.com/codelabs/android-adv-workmanager)

### Blog posts

- [Background Task Inspector](https://medium.com/androiddevelopers/background-task-inspector-30c8706f0380)