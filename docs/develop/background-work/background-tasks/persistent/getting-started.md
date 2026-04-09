---
title: Getting started with WorkManager  |  Background work  |  Android Developers
url: https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Background work](https://developer.android.com/develop/background-work)
* [Guides](https://developer.android.com/develop/background-work/background-tasks)

# Getting started with WorkManager Stay organized with collections Save and categorize content based on your preferences.




To get started using WorkManager, first import the library into your Android
project.

Add the following dependencies to your app's `build.gradle` file:

### Groovy

```
dependencies {
    def work_version = "2.11.2"

    // (Java only)
    implementation "androidx.work:work-runtime:$work_version"

    // Kotlin + coroutines
    implementation "androidx.work:work-runtime-ktx:$work_version"

    // optional - RxJava2 support
    implementation "androidx.work:work-rxjava2:$work_version"

    // optional - GCMNetworkManager support
    implementation "androidx.work:work-gcm:$work_version"

    // optional - Test helpers
    androidTestImplementation "androidx.work:work-testing:$work_version"

    // optional - Multiprocess support
    implementation "androidx.work:work-multiprocess:$work_version"
}
```

### Kotlin

```
dependencies {
    val work_version = "2.11.2"

    // (Java only)
    implementation("androidx.work:work-runtime:$work_version")

    // Kotlin + coroutines
    implementation("androidx.work:work-runtime-ktx:$work_version")

    // optional - RxJava2 support
    implementation("androidx.work:work-rxjava2:$work_version")

    // optional - GCMNetworkManager support
    implementation("androidx.work:work-gcm:$work_version")

    // optional - Test helpers
    androidTestImplementation("androidx.work:work-testing:$work_version")

    // optional - Multiprocess support
    implementation("androidx.work:work-multiprocess:$work_version")
}
```

Once you’ve added the dependencies and synchronized your Gradle project, the
next step is to define some work to run.

**Note:** You can always find the latest version of WorkManager, including beta,
alpha, and release candidate versions on the [WorkManager releases
page](/jetpack/androidx/releases/work).

## Define the work

Work is defined using the `Worker`
class. The `doWork()` method runs asynchronously on a background
thread provided by WorkManager.

To create some work for WorkManager to run, extend the `Worker` class and
override the `doWork()` method. For example, to create a `Worker` that uploads
images, you can do the following:

### Kotlin

```
class UploadWorker(appContext: Context, workerParams: WorkerParameters):
       Worker(appContext, workerParams) {
   override fun doWork(): Result {

       // Do the work here--in this case, upload the images.
       uploadImages()

       // Indicate whether the work finished successfully with the Result
       return Result.success()
   }
}
```

### Java

```
public class UploadWorker extends Worker {
   public UploadWorker(
       @NonNull Context context,
       @NonNull WorkerParameters params) {
       super(context, params);
   }

   @Override
   public Result doWork() {

     // Do the work here--in this case, upload the images.
     uploadImages();

     // Indicate whether the work finished successfully with the Result
     return Result.success();
   }
}
```

The `Result`
returned from `doWork()` informs the WorkManager service whether the
work succeeded and, in the case of failure, whether or not the work should be
retried.

* `Result.success()`: The work finished successfully.
* `Result.failure()`: The work failed.
* `Result.retry()`: The work failed and should be tried at another time
  according to its
  [retry policy](/topic/libraries/architecture/workmanager/how-to/define-work#retries_backoff).

## Create a WorkRequest

Once your work is defined, it must be scheduled with the WorkManager service in
order to run. WorkManager offers a lot of flexibility in how you schedule your
work. You can schedule it to [run
periodically](/topic/libraries/architecture/workmanager/how-to/define-work#schedule_periodic_work)
over an interval of time, or you can schedule it to run only [one
time](/topic/libraries/architecture/workmanager/how-to/define-work#constraints).

However you choose to schedule the work, you will always use a
`WorkRequest`. While a
`Worker` defines the unit of work, a
`WorkRequest` (and its
subclasses) define how and when it should be run. In the simplest case, you can
use a
`OneTimeWorkRequest`,
as shown in the following example.

### Kotlin

```
val uploadWorkRequest: WorkRequest =
   OneTimeWorkRequestBuilder<UploadWorker>()
       .build()
```

### Java

```
WorkRequest uploadWorkRequest =
   new OneTimeWorkRequest.Builder(UploadWorker.class)
       .build();
```

## Submit the WorkRequest to the system

Finally, you need to submit your `WorkRequest` to `WorkManager` using the
`enqueue()`
method.

### Kotlin

```
WorkManager
    .getInstance(myContext)
    .enqueue(uploadWorkRequest)
```

### Java

```
WorkManager
    .getInstance(myContext)
    .enqueue(uploadWorkRequest);
```

The exact time that the worker is going to be executed depends on the
constraints that are used in your `WorkRequest` and on system optimizations.
WorkManager is designed to give the best behavior under these restrictions.

## Next steps

This getting started guide only scratches the surface. The `WorkRequest` can
also include additional information, such as the constraints under which the
work should run, input to the work, a delay, and backoff policy for retrying
work. In the next section, [Define your work
requests](/topic/libraries/architecture/workmanager/how-to/define-work), you’ll
learn more about these options in greater detail as well as get an understanding
of how to schedule unique and reoccurring work.

## Additional resources

In addition to guide documentation, there are several blogs, codelabs, and code
samples available to help you get started.

### Samples

* [Sunflower](https://github.com/android/sunflower),
  a demo app demonstrating best practices with various architecture
  components, including WorkManager.

### Codelabs

* Working with WorkManager [(Kotlin)](https://codelabs.developers.google.com/codelabs/android-workmanager/#0) and [(Java)](https://codelabs.developers.google.com/codelabs/android-workmanager-java/#0)
* [Advanced WorkManager (Kotlin)](https://codelabs.developers.google.com/codelabs/android-adv-workmanager/#0)

### Blogs

* [Introducing WorkManager](https://medium.com/androiddevelopers/introducing-workmanager-2083bcfc4712)
* [WorkManager Basics](https://medium.com/androiddevelopers/workmanager-basics-beba51e94048)
* [WorkManager and Kotlin](https://medium.com/androiddevelopers/workmanager-meets-kotlin-b9ad02f7405e)
* [WorkManager Periodicity](https://medium.com/androiddevelopers/workmanager-periodicity-ff35185ff006)
* [Customizing WorkManager - Fundamentals](https://medium.com/androiddevelopers/customizing-workmanager-fundamentals-fdaa17c46dd2)
* [Customize WorkManager with Dagger](https://medium.com/androiddevelopers/customizing-workmanager-with-dagger-1029688c0978)