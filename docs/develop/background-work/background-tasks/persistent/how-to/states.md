---
title: https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/states
url: https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/states
source: md.txt
---

> Documentation index: https://developer.android.com/develop/background-work/background-tasks/persistent/llms.txt

Work goes through a series of [`State`](https://developer.android.com/reference/androidx/work/WorkInfo.State.md.txt) changes over its lifetime.

## One-time work states

For a [`one-time`](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#schedule_one-time_work) work request, your work begins in an [`ENQUEUED`](https://developer.android.com/reference/androidx/work/WorkInfo.State.md.txt#ENQUEUED)
state.

In the `ENQUEUED` state, your work is eligible to run as soon as its
[`Constraints`](https://developer.android.com/reference/androidx/work/Constraints.md.txt) and initial delay timing requirements are met. From there it
moves to a [`RUNNING`](https://developer.android.com/reference/androidx/work/WorkInfo.State.md.txt#RUNNING) state. Depending on the outcome of the work, it can
move to [`SUCCEEDED`](https://developer.android.com/reference/androidx/work/WorkInfo.State.md.txt#SUCCEEDED), [`FAILED`](https://developer.android.com/reference/androidx/work/WorkInfo.State.md.txt#FAILED), or possibly back to `ENQUEUED` if the
result is [`retry`](https://developer.android.com/reference/androidx/work/ListenableWorker.Result.md.txt#retry()). At any point in the process, work can be canceled, at
which point it moves to the [`CANCELLED`](https://developer.android.com/reference/androidx/work/WorkInfo.State.md.txt#CANCELLED) state.

Figure 1 illustrates the life of one-time work, with the events that can take it
to another state.
![Flowchart of one-time work states showing transitions between ENQUEUED, RUNNING, SUCCEEDED, FAILED, and CANCELLED.](https://developer.android.com/static/images/topic/libraries/architecture/workmanager/how-to/one-time-work-flow.png) **Figure 1.** State diagram for one-time work.

`SUCCEEDED`, `FAILED` and `CANCELLED` all represent a terminal state for this
work. If your work is in any of these states,
[`WorkInfo.State.isFinished()`](https://developer.android.com/reference/androidx/work/WorkInfo.State.md.txt#isFinished()) returns true.

## Periodic work states

Success and failed states apply only to one-time and [chained work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/chain-work). For
[periodic work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#schedule_periodic_work), there is only one terminal state, `CANCELLED`. This is
because periodic work never ends. After each run, it's rescheduled, regardless
of the result. Figure 2 depicts the condensed state diagram for periodic work.
![Flowchart of periodic work states showing transitions between ENQUEUED, RUNNING, and CANCELLED.](https://developer.android.com/static/images/topic/libraries/architecture/workmanager/how-to/periodic-work-states.png) **Figure 2.** State diagram for periodic work.

## Blocked state

One final state is `BLOCKED`. This state applies to work that is orchestrated
in a series, or chain of work. Work chains, and their state diagram, are covered
in [Chaining work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/chain-work).

## Next steps

In [Managing work](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/managing-work), you'll learn more about how to manage and monitor the
progress of your work.