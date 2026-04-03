---
title: Threading in RxWorker  |  Background work  |  Android Developers
url: https://developer.android.com/develop/background-work/background-tasks/persistent/threading/rxworker
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Background work](https://developer.android.com/develop/background-work)
* [Guides](https://developer.android.com/develop/background-work/background-tasks)

# Threading in RxWorker Stay organized with collections Save and categorize content based on your preferences.




We provide interoperability between WorkManager and RxJava. To get started,
include [`work-rxjava3` dependency in addition to `work-runtime`](/jetpack/androidx/releases/work#declaring_dependencies) in your gradle file.
There is also a `work-rxjava2` dependency that supports rxjava2 instead.

Then, instead of extending `Worker`, you should extend`RxWorker`. Finally
override the [`RxWorker.createWork()`](/reference/androidx/work/RxWorker#createWork())
method to return a `Single<Result>` indicating the [`Result`](/reference/androidx/work/ListenableWorker.Result) of your execution, as
follows:

### Kotlin

```
class RxDownloadWorker(
        context: Context,
        params: WorkerParameters
) : RxWorker(context, params) {
    override fun createWork(): Single<Result> {
        return Observable.range(0, 100)
                .flatMap { download("https://www.example.com") }
                .toList()
                .map { Result.success() }
    }
}
```

### Java

```
public class RxDownloadWorker extends RxWorker {

    public RxDownloadWorker(Context context, WorkerParameters params) {
        super(context, params);
    }

    @NonNull
    @Override
    public Single<Result> createWork() {
        return Observable.range(0, 100)
            .flatMap { download("https://www.example.com") }
            .toList()
            .map { Result.success() };
    }
}
```

Note that `RxWorker.createWork()` is *called* on the main thread, but the return
value is *subscribed* on a background thread by default. You can override [`RxWorker.getBackgroundScheduler()`](/reference/androidx/work/RxWorker#getBackgroundScheduler()) to change the
subscribing thread.

When an `RxWorker` is `onStopped()`, the subscription will get disposed of, so
you don't need to handle [work stoppages](/topic/libraries/architecture/workmanager/how-to/managing-work#cancelling) in any special way.