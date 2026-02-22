---
title: https://developer.android.com/jetpack/androidx/releases/archive/arch
url: https://developer.android.com/jetpack/androidx/releases/archive/arch
source: md.txt
---

# Architecture Components Release Notes Archive

| **Note:** These are the original release notes for Architecture Components before they were included in the general AndroidX release notes. For the current release notes see the[AndroidX release notes](https://developer.android.com/jetpack/androidx/releases).

## January 15, 2019

### WorkManager

WorkManager`1.0.0-beta02`is released. This release contains some bug fixes.

**Bug Fixes**

- Fixed an edge case where periodic work could run more than once per interval on devices running Android 6.0 (API level 23).[b/121998363](https://issuetracker.google.com/121998363)
- Fixed a`ConcurrentModificationException`on devices running Android 5.1 (API level 22) or lower.[b/121345393](https://issuetracker.google.com/121345393)
- Fixed erroneous execution of work when Constraints aren't met on devices running Android 5.1 (API level 22) or lower.[b/122578012](https://issuetracker.google.com/122578012)
- Optimized work completion handling to be faster in some edge cases.[b/122358129](https://issuetracker.google.com/122358129)
- Added a change to address potential race conditions among multiple instances of`LiveData`that WorkManager uses.
- Moved to use`Room`dependency`1.1.1`instead of`1.1.1-rc01`; these versions are identical.[b/122578011](https://issuetracker.google.com/122578011)

## December 19, 2018

### WorkManager

WorkManager`1.0.0-beta01`is released. This release contains no API changes; moving forward, WorkManager is expected to stay API stable until the next version unless there is a critical problem. This release contains some bug fixes.

**Bug Fixes**

- Previously-cancelled children of successfully completed parent work will no longer run.[b/120811767](https://issuetracker.google.com/120811767)
- Properly initialized logging classes (primarily surfaced during tests).

## December 18, 2018

### Navigation

Navigation`1.0.0-alpha09`is released. This release contains breaking API changes; please see the*Breaking Changes*section below.

We have chosen not to continue development of the`android.arch.navigation:navigation-testing`artifact. While it has proven helpful for internal testing of`NavController`, we strongly recommend alternate testing strategies, such as mocking the`NavController`instance in order to verify that the correct`navigate()`calls are being done. This approach is discussed in detail in the[Single Activity talk at AndroidDevSummit 2018](https://www.youtube.com/watch?v=2k8x8V77CrU)and we'll be working on additional documentation specifically around testing with Navigation.

**New Features**

- `MenuItem`s with`menuCategory="secondary"`will no longer pop the back stack when used with`NavigationUI`methods.[b/120104424](https://issuetracker.google.com/120104424)
- `AppBarConfiguration`now allows you to set a fallback[`OnNavigateUpListener`](https://developer.android.com/reference/androidx/navigation/ui/AppBarConfiguration.OnNavigateUpListener)instance which will be called when`navController.navigateUp()`returns`false`.[b/79993862](https://issuetracker.google.com/79993862)[b/120690961](https://issuetracker.google.com/120690961)

**Breaking Changes**

- When using an`<argument>`with an`argType="reference"`, Navigation no longer parses the reference, instead providing the raw resource ID itself.[b/111736515](https://issuetracker.google.com/111736515)
- [`onNavDestinationSelected()`](https://developer.android.com/reference/androidx/navigation/ui/NavigationUI#onNavDestinationSelected(android.view.MenuItem,%20androidx.navigation.NavController))now pops back to the start destination of your navigation graph by default, making them consistent with the`setup`methods. Add`menuCategory="secondary"`to your`MenuItem`to avoid popping the back stack.[aosp/852869](https://android-review.googlesource.com/852869)
- The`fromBundle()`methods of generated`Args`classes now take a non-null`Bundle`instead of a nullable`Bundle`[aosp/845616](https://android-review.googlesource.com/845616)

**Bug Fixes**

- Arguments are now properly parsed from deep links as the correct`argType`instead of always as strings[b/110273284](https://issuetracker.google.com/110273284)
- Navigation now correctly exports its public resources[b/121059552](https://issuetracker.google.com/121059552)
- Safe Args is now compatible with Android Gradle Plugin 3.4 Canary 4 and higher[b/119662045](https://issuetracker.google.com/119662045)

## December 12, 2018

### WorkManager

WorkManager`1.0.0-alpha13`is released. This release contains a minor API change that will be helpful for some Kotlin users.

**API Changes**

- `androidx.work.Result`has been moved to be an inner class of`ListenableWorker`. This prevents refactoring conflicts with Kotlin's top-level`Result`class.*This is a breaking API change.* [b/120564418](https://issuetracker.google.com/120564418)

**Breaking API Changes**

- `androidx.work.Result`has been moved to be an inner class of`ListenableWorker`.

## December 6, 2018

### Paging

Paging`2.1.0-rc01`is released with no changes from`2.1.0-beta01`.

### Navigation

Navigation`1.0.0-alpha08`is released. This release contains breaking API changes; please see the*Breaking Changes*section below.

**New Features**

- Destination labels, when used with`NavigationUI`methods, will now automatically replace`{argName}`instances in your`android:label`with the correct argument[b/80267266](https://issuetracker.google.com/80267266)
- Navigation now depends on Support Library 28.0.0[b/120293333](https://issuetracker.google.com/120293333)

**Breaking Changes**

- `OnNavigatedListener`has been renamed to`OnDestinationChangedListener`[b/118670572](https://issuetracker.google.com/118670572)
- `OnDestinationChangedListener`now also passes the`Bundle`of arguments[aosp/837142](https://android-review.googlesource.com/837142)
- The`app:clearTask`and`app:launchDocument`attributes and their associated methods have been removed. Use`app:popUpTo`with the root of your graph to remove all destinations from your back stack.[b/119628354](https://issuetracker.google.com/119628354)
- `ActivityNavigator.Extras`now uses a`Builder`pattern and adds the ability to set any`Intent.FLAG_ACTIVITY_`flags[aosp/828140](https://android-review.googlesource.com/828140)
- `NavController.onHandleDeepLink`has been renamed to`handleDeepLink`[aosp/836063](https://android-review.googlesource.com/836063)
- Many classes and methods not meant for subclassing, such as`NavOptions`,`NavInflater`,`NavDeepLinkBuilder`, and`AppBarConfiguration`, have been made`final`[aosp/835681](https://android-review.googlesource.com/835681)
- The deprecated`NavHostFragment.setGraph()`method has been removed[aosp/835684](https://android-review.googlesource.com/835684)
- The deprecated`NavigationUI.navigateUp(DrawerLayout, NavController)`method has been removed.[aosp/835684](https://android-review.googlesource.com/835684)
- Fragment creation has been moved to`FragmentNavigator`, making it easier to delegate Fragment creation to a`FragmentFactory`.[b/119054429](https://issuetracker.google.com/119054429)
- The constructor for`NavGraphNavigator`no longer takes a`Context`[aosp/835340](https://android-review.googlesource.com/835340)
- [NavigatorProvider](https://developer.android.com/reference/androidx/navigation/NavigatorProvider)is now a class, rather than an interface. The`NavigatorProvider`returned by[`getNavigatorProvider()`](https://developer.android.com/reference/androidx/navigation/NavController#getNavigatorProvider())has not changed its functionality.[aosp/830660](https://android-review.googlesource.com/830660)
- `NavDestination.navigate()`has been removed. Call`navigate()`on the`Navigator`instead.[aosp/830663](https://android-review.googlesource.com/830663)
- Significant refactoring of`Navigator`, removing the need for`OnNavigatorNavigatedListener`and instead having`navigate`return the`NavDestination`that was navigated to.
- `Navigator`instances can no longer send pop events to the`NavController`. Consider using a[`OnBackPressedCallback`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback)to intercept back button presses and call`navController.popBackStack()`.[aosp/833716](https://android-review.googlesource.com/833716)

**Bug Fixes**

- `popUpTo`now works consistently when the destination is a`<navigation>`element[b/116831650](https://issuetracker.google.com/116831650)
- Fixed a number of bugs that resulted in an`IllegalArgumentException`when using nested graphs[b/118713731](https://issuetracker.google.com/118713731)[b/113611083](https://issuetracker.google.com/113611083)[b/113346925](https://issuetracker.google.com/113346925)[b/113305559](https://issuetracker.google.com/113305559)
- The`dataPattern`attribute of`<activity>`destinations will now populate arguments from non-String arguments by calling`toString()`[b/120161365](https://issuetracker.google.com/120161365)

**Safe Args**

- Safe Args supports Serializable objects, including Enum values. Enum types can set a default value by using the enum literal without the class name (e.g.`app:defaultValue="READ"`)[b/111316353](https://issuetracker.google.com/111316353)
- Safe Args supports arrays of all supported types[b/111487504](https://issuetracker.google.com/111487504)
- Safe Args now ignores subfolders of resource directories[b/117893516](https://issuetracker.google.com/117893516)
- Safe Args adds`@Override`annotations where appropriate[b/117145301](https://issuetracker.google.com/117145301)

## December 5, 2018

### WorkManager

WorkManager`1.0.0-alpha12`is released. This release contains some breaking API changes; please see the*Breaking API Changes* section below. This version is likely to be released as our first beta.`alpha12`also contains extensive documentation updates.

**API Changes**

- A new artifact,`work-rxjava2`, introduces`RxWorker`. This is a`ListenableWorker`that expects a`Single<Payload>`.
- Support for Firebase JobDispatcher has been removed because of its impending deprecation. This means that the`work-firebase`artifact will no longer be updated as we head into beta. We will be looking into adding an alternative in the future.
- Combined`Payload`into`Result`.`Result`is now a "sealed class" with three concrete implementations, which you can obtain via`Result.success()`(or`Result.success(Data)`),`Result.failure()`(or`Result.failure(Data)`), and`Result.retry()`. Your`ListenableFuture`s now result`Result`instead of`Payload`.`Worker`s don't have getter and setter methods for output`Data`.*This is a breaking change.*
- Added`Constraints.Builder.setTriggerContentMaxDelay(long, TimeUnit)`and`Constraints.Builder.setTriggerContentUpdateDelay(long, TimeUnit)`and variants to better support slow triggering content URIs.[b/119919774](https://issuetracker.google.com/119919774)
- Added`WorkRequest.Builder.setBackoffCriteria(BackoffPolicy, Duration)`variant. This method requires API 26.
- Added`Operation.await()`and`ListenableFuture.await()`Kotlin extension methods.
- Renamed`Operation.getException()`to`Operation.getThrowable()`.*This is a breaking change.*
- The`ContentUriTriggers`class and methods referencing it are no longer available for public usage.*This is a breaking change.*
- Removed the rest of the varargs methods in`WorkManager`,`WorkContinuation`, and`OneTimeWorkRequest`to streamline the API. To fix any build problems, you can wrap your existing varargs with`Arrays.asList(...)`. We still include single-argument versions of each method.*This is a breaking change.*
- Removed`WorkContinuation.combine(OneTimeWorkRequest, *)`variants. They were presenting a confusing API; the existing`combine`methods are more understandable.*This is a breaking change.*

**Bug Fixes**

- Pre-Marshmallow implementations are now more reliable in recovering from process death of an already-executing task.
- `LiveData`that is observed via`observeForever`is tracked via WorkManager. This is a backport of a Room library fix.[b/74477406](https://issuetracker.google.com/74477406)
- `Data.Builder.build()`now throws an exception if the serialized object exceeds its maximum size. This previously would only happen on a background thread where you couldn't properly handle it.
- Further distinguished stopped vs. cancelled work;`getWorkInfoById()`will return a`WorkInfo`with the`CANCELLED``State`during`ListenableWorker.onStopped()`.
- Treat`null``Result`s as failures in`ListenableWorker`.[b/120362353](https://issuetracker.google.com/120362353)
- Speculative fix for Shield Tablets running API 24 that sometimes threw an`IllegalArgumentException`.[b/119484416](https://issuetracker.google.com/119484416)

**Breaking API Changes**

- Support for Firebase JobDispatcher has been removed because of its impending deprecation. This means that the`work-firebase`artifact will no longer be updated as we head into beta. We will be looking into adding an alternative in the future.
- Combined`Payload`into`Result`.`Result`is now a "sealed class" with three concrete implementations, which you can obtain via`Result.success()`(or`Result.success(Data)`),`Result.failure()`(or`Result.failure(Data)`), and`Result.retry()`. Your`ListenableFuture`s now result`Result`instead of`Payload`.`Worker`s don't have getter and setter methods for output`Data`.
- Added`Operation.await()`and`ListenableFuture.await()`Kotlin extension methods.
- Renamed`Operation.getException()`to`Operation.getThrowable()`.
- The`ContentUriTriggers`class and methods referencing it are no longer available for public usage.
- Removed the rest of the varargs methods in`WorkManager`,`WorkContinuation`, and`OneTimeWorkRequest`to streamline the API. To fix any build problems, you can wrap your existing varargs with`Arrays.asList(...)`. We still include single-argument versions of each method.
- Removed`WorkContinuation.combine(OneTimeWorkRequest, *)`variants. They were presenting a confusing API; the existing`combine`methods are more understandable.

## December 4, 2018

### Room

Room`2.1.0-alpha03`is released with coroutines support and several bug fixes.

**API Changes**

- The FTS`tokenizer`in`@Fts3`/`@Fts4`now takes a String instead of an Enum. This allows custom tokenizers to be used by Room. Built-in tokenizers are still defined in`FtsOptions`as string constants.[b/119234881](https://issuetracker.google.com/119234881)

**New Features**

- **Couroutines** : DAO methods can now be suspend functions. To support suspend functions in Room a new artifact has been released,`room-coroutines`.[b/69474692](https://issuetracker.google.com/69474692)
- DAO methods annotated with`@Insert`,`@Delete`or`@Update`now support`ListenableFuture`as return type.[b/119418331](https://issuetracker.google.com/119418331)

**Bug Fixes**

- Fixed a bug where Room would incorrectly attempt to find a constructor with columns in the`ignoredColumns`property of`@Entity`.[b/119830714](https://issuetracker.google.com/119830714)
- Fixed a bug where Room would not mark DAO method parameters as final in their generated implementation.[b/118015483](https://issuetracker.google.com/118015483)
- Fixed a bug where Room's processor would crash when reporting an error on a query with special symbols.[b/119520136](https://issuetracker.google.com/119520136)
- Fixed a bug where Room would decline other various`Collection`implementations as arguments of an`IN`expression.[b/119884035](https://issuetracker.google.com/119884035)
- Fixed a bug where LiveData returned from Room would get garbage collected when observed forever causing it to no longer emit new data.[b/74477406](https://issuetracker.google.com/74477406)
- Updated`RoomDatabase`'s close lock to reduce lock contention.[b/117900450](https://issuetracker.google.com/117900450)

## Nov 8, 2018

### WorkManager

WorkManager`1.0.0-alpha11`is released. This release contains many changes that will become stable API at`beta`. There are breaking API changes in this release; please see the*Breaking API Changes*section below.

**API Changes**

- `work-runtime-ktx`introduces a new`CoroutineWorker`.
- `WorkStatus`has been renamed to`WorkInfo`. All corresponding`getStatus`method variants have been renamed to the corresponding`getWorkInfo`variants.*This is a breaking change.*
- `ListenableWorker.onStopped()`no longer accepts has a boolean argument representing if the`WorkRequest`was cancelled.`WorkManager`no longer makes this distinction.*This is a breaking change.*
- `androidx.work.test`package has been renamed to`androidx.work.testing`package.*This is a breaking change.*
- Setters on`Constraints`are no longer a part of the public API.*This is a breaking change.*
- `WorkerParameters.getTriggeredContentUris()`and`WorkerParameters.getTriggeredContentAuthorities()`previously returned arrays. Now these methods return Collections.*This is a breaking change.*
- `ListenableWorker.onStartWork()`is renamed to`ListenableWorker.startWork()`.*This is a breaking change.*
- The constructor for`WorkStatus`is no longer a part of the public API.*This is a breaking change.*
- `Configuration.getMaxJobSchedulerID()`and`Configuration.getMinJobSchedulerID()`are renamed to`Configuration.getMinJobSchedulerId()`and`Configuration.getMaxJobSchedulerId()`respectively.*This is a breaking change.*
- Added a lot of`@NonNull`annotations to the public API to improve ergonomics of the API.
- Add`WorkManager.enqueueUniqueWork()`API to enqueue unique`OneTimeWorkRequest`s without having to create a`WorkContinuation`.
- All variants of`enqueue`and`cancel`methods on`WorkManager`now return a new`Operation`type.*This is a breaking change.*
- All variants of`enqueue`no longer accept varargs for`WorkRequest`s.*This is a breaking change.* Use Collections instead. You can use`Arrays.asList()`to modify existing code. We did this to reduce the API surface and method count.
- Attempting to`initialize``WorkManager`more than once per process will now result in an`IllegalStateException`.*This is a breaking change.*

**Bug Fixes**

- `WorkRequest.Builder`s in the`work-runtime-ktx`artifact now use`ListenableWorker`s. Fixes[b/117666259](https://issuetracker.google.com/issues/117666259)
- Ensure the next run time for`PeriodicWork`is in the future. Fixes[b/118204399](https://issuetracker.google.com/issues/118204399)
- Remove potential disk I/O when using WorkManager on app startup. Fixes[b/117796731](https://issuetracker.google.com/issues/117796731)
- Fix a race condition in`WorkConstraintsTracker`. Fixes[android-workmanager/issues/56](https://github.com/googlecodelabs/android-workmanager/issues/56)

**Breaking API Changes**

- `WorkStatus`has been renamed to`WorkInfo`. All corresponding`getStatus`method variants have been renamed to the corresponding`getWorkInfo`variants.
- `ListenableWorker.onStopped()`no longer accepts has a boolean argument representing if the`WorkRequest`was cancelled.`WorkManager`no longer makes this distinction.
- `androidx.work.test`package has been renamed to`androidx.work.testing`package.
- Setters on`Constraints`are no longer a part of the public API.
- `WorkerParameters.getTriggeredContentUris()`and`WorkerParameters.getTriggeredContentAuthorities()`previously returned arrays. Now these methods return Collections.
- `ListenableWorker.onStartWork()`is renamed to`ListenableWorker.startWork()`.
- The constructor for`WorkStatus`is no longer a part of the public API.
- `Configuration.getMaxJobSchedulerID()`and`Configuration.getMinJobSchedulerID()`are renamed to`Configuration.getMinJobSchedulerId()`and`Configuration.getMaxJobSchedulerId()`respectively.
- All variants of`enqueue`and`cancel`methods on`WorkManager`now return a new`Operation`type.
- All variants of`enqueue`no longer accept varargs for`WorkRequest`s.
- Attempting to`initialize``WorkManager`more than once per process will now result in an`IllegalStateException`.

## November 1, 2018

### Paging

Paging`2.1.0-beta01`is released with no changes from`2.1.0-alpha01`.

## October 30, 2018

### Room

Room`2.1.0-alpha02`is released with several bug fixes and a new feature.

**New Features**

- Added support for referencing a`@DatabaseView`in a`@Relation`.[b/117680932](https://issuetracker.google.com/117680932)

**Bug Fixes**

- Fixed a bug where Room would perform disk I/O in the main thread when subscribing and disposing from an Rx return type.[b/117201279](https://issuetracker.google.com/117201279)
- Fixed a bug where Room would fail to find an appropriate type converter for a field in a Kotlin entity class.[b/111404868](https://issuetracker.google.com/111404868)
- Fixed a bug where Room would generate incorrect code for a`DAO`interface implementation containing a Kotlin default method that has no arguments.[b/117527454](https://issuetracker.google.com/117527454)
- Updated Room's SQLite grammar parser, fixing a performance issue that would cause long build times.[b/117401230](https://issuetracker.google.com/117401230)

## October 29, 2018

### Navigation

Navigation`1.0.0-alpha07`is released with bug fixes and API changes.

**New Features**

- A new[AppBarConfiguration](https://developer.android.com/reference/androidx/navigation/ui/AppBarConfiguration)class allows you to customize which destinations are considered*top-level* destinations. See the[updated documentation](https://developer.android.com/topic/libraries/architecture/navigation/navigation-ui)for details.[b/117333663](https://issuetracker.google.com/117333663)
- You can now pass arguments to the start destination of your graph[b/110300470](https://issuetracker.google.com/110300470)
- Deep links now support custom schemes with periods, hyphens, and plus signs.[b/112806402](https://issuetracker.google.com/112806402)

**Breaking Changes**

- The`navigation-testing-ktx`module has been folded into the`navigation-testing artifact`and will no longer be published.
- The`navigation-testing`artifact now has a dependency on the Kotlin standard library. The API has been changed to be more consistent with Kotlin conventions, but you can continue to use it for tests written in Java.
- Metadata manifest registered navigation graphs are no longer supported.[b/118355937](https://issuetracker.google.com/118355937)
- Actions can no longer be attached to \<activity\> destinations.[aosp/785539](https://android-review.googlesource.com/c/platform/frameworks/support/+/785539)

**Bug Fixes**

- Deep links now correctly parse query parameters.[b/110057514](https://issuetracker.google.com/110057514)
- Activity destinations now correctly apply all enter and exit animations.[b/117145284](https://issuetracker.google.com/117145284)
- Fixed crash that occurs after configuration changes when using custom Navigators.[b/110763345](https://issuetracker.google.com/110763345)

**Safe Args**

- Safe args now have a fixed dependency on Android Gradle Plugin 3.2.1.[b/113167627](https://issuetracker.google.com/113167627)
- Directions can now be generated for inner classes.[b/117407555](https://issuetracker.google.com/117407555)
- Fixed an issue with generating Directions to an \<include\> graph.[b/116542123](https://issuetracker.google.com/116542123)

## October 12, 2018

### Paging

Paging`2.1.0-alpha01`is released with two major additions - page dropping, and KTX extension libraries for every artifact - as well as several other API changes and bugfixes.

**API Changes**

- Added`PagedList.Config.Builder.setMaxSize()`for limiting the number of loaded items in memory.
- Added`androidx.paging.Config()`as a Kotlin alternative for`PagedList.Config.Builder`
- Added`androidx.paging.PagedList()`as a Kotlin alternative for`PagedList.Builder`
- Added`DataSourceFactory.toLiveData()`as a Kotlin alternative for`LivePagedListBuilder`
- Added`DataSourceFactory.toObservable()`and`toFlowable()`as Kotlin alternatives for`RxPagedListBuilder`
- Added`AsyncPagedListDiffer.addPagedListListener()`for listening to when PagedList is swapped.[b/111698609](https://issuetracker.google.com/111698609)
- Added`PagedListAdapter.onCurrentListChanged()`variant that passes old and new list, deprecated previous variant.
- Added`PagedListAdapter/AsyncPagedListDiffer.submitList()`variants which take an additional callback that triggers if/when the pagedlist is displayed, after diffing. This allows you to synchronize a PagedList swap with other UI updates.[b/73781068](https://issuetracker.google.com/73781068)
- `PagedList.getLoadedCount()`added to let you know how many items are in memory. Note that the return value is always equal to`.size()`if placeholders are disabled.

**Bug Fixes**

- Fixed a race condition when diffing if lists are reused[b/111591017](https://issuetracker.google.com/111591017)
- `PagedList.loadAround()`now throws`IndexOutOfBoundsException`when index is invalid. Previously it could crash with an unclear other exception.
- Fixed a case where an extremely small initial load size together with unchanged data would result in no further loading[b/113122599](https://issuetracker.google.com/113122599)

| **Note:** page dropping is currently off by default - enable it with the new`PagedList.Config.Builder.setMaxSize()`API. To correctly support page dropping in a custom`ItemKeyedDataSource`, you must implement`loadBefore`.
| **Note:** Page dropping is not currently supported in`PageKeyedDataSource`, due to having no way to re-load the`loadInitial`result incrementally.

## October 11, 2018

### WorkManager

WorkManager`1.0.0-alpha10`is released with support for developer-controlled asynchronous work. There are breaking API changes in this release; please see the*Breaking API Changes*section below.

We anticipate that WorkManager is entering the final phases of its alpha period. We expect to be API stable in beta, so please take some time to file your feedback on our issue tracker.

**API Changes**

- Removed all previously`deprecated`methods and classes, notably the default`Worker`constructor.*This is a breaking API change.*
- Renamed`NonBlockingWorker`to`ListenableWorker`, which is now an unhidden public class and ready for usage.
  - `ListenableWorker`provides access to one abstract method,`ListenableFuture<Payload> onStartWork()`which is called on the main thread. It is up to you to start and process work asynchronously. When finished, you should update the`ListenableFuture`appropriately. Reference implementations of`ListenableFuture`s are provided in the`Futures`package in`alpha02`(see below the`WorkManager`section).
  - `Worker`extends`ListenableWorker`and still operates as before, with an abstract`Result doWork()`method.
  - Shuffled some methods and members from`Worker`to`ListenableWorker`.
  - We shall soon provide reference implementations for`ListenableWorker`s that use Kotlin coroutines (once the stable versions are released) and RxJava2.
- The interface`WorkerFactory`and the concrete implementation`DefaultWorkerFactory`have been merged into an abstract class called`WorkerFactory`. The implementation ensures that the default reflection-based behavior is called as a last-ditch effort for any user-created`WorkerFactory`instances.*This is a breaking change.*
- Removed`WorkManager.synchronous()`and`WorkContinuation.synchronous()`and all related methods. Added`ListenableFuture<Void>`as the return type of many methods in the API.*This is a breaking API change.*
  - You can now synchronously get and observe by using`ListenableFuture`s. For example,`WorkManager.enqueue()`used to return`void`; it now returns a`ListenableFuture<Void>`. You can call`ListenableFuture.addListener(Runnable, Executor)`or`ListenableFuture.get()`to run code once the operation is complete.
  - Note that these`ListenableFuture`s do not tell you if the operation succeeded or failed; only that they finished. You will still need to chain WorkManager methods to find out this information.
  - We ignore`cancel()`calls on these objects, as they are confusing and hard to reason about (are you cancelling the operation or the resulting work?). This is within the`Future`s contract.
  - To maintain parity with the synchronous`getStatus*`methods, we have provided`ListenableFuture`variants, and renamed the existing ones that returned`LiveData`to explicitly have "LiveData" as part of the name (for example,`getStatusesByIdLiveData(UUID)`).*This is a breaking API change.*

**Bug Fixes**

- Fixed the known issue from alpha09 regarding duplicate`androidx-annotations.pro`files. You may remove the workaround from the previous release notes by deleting`exclude 'META-INF/proguard/androidx-annotations.pro'`from your gradle file.
- Added proguard configurations to keep new`Worker`constructor.[b/116296569](https://issuetracker.google.com/116296569)
- Fix potential`NullPointerException`in a race condition where work was`REPLACE`d.[b/116253486](https://issuetracker.google.com/116253486)and[b/116677275](https://issuetracker.google.com/116677275)
- `WorkContinuation.combine()`now accepts one or more`WorkContinuation`s instead of two or more.[b/117266752](https://issuetracker.google.com/117266752)

**Breaking API Changes**

- Removed all previously`deprecated`methods and classes, notably the default`Worker`constructor.
- The interface`WorkerFactory`and the concrete implementation`DefaultWorkerFactory`have been merged into an abstract class called`WorkerFactory`.
- Removed`WorkManager.synchronous()`and`WorkContinuation.synchronous()`.
- `WorkManager.getStatus*()`methods now return`ListenableFuture`s.`WorkManager.getStatus*LiveData()`return`LiveData`s.

### Futures

Futures`1.0.0-alpha02`is released.

**API Changes**

- Developers can now use`ResolvableFuture`and`AbstractResolvableFuture`as lightweight concrete implementations of`ListenableFuture`.

## October 8, 2018

### Room

Room`2.1.0-alpha01`is released.

**New Features**

- **FTS** : Room now supports entities with a mapping[FTS3 or FTS4](https://www.sqlite.org/fts3.html)table. Classes annotated with`@Entity`can now be additionally annotated with`@Fts3`or`@Fts4`to declare a class with a mapping full-text search table. FTS options for further customization are available via the annotation's methods.[b/62356416](https://issuetracker.google.com/62356416)
- **Views** : Room now supports declaring a class as a stored query, also known as a[view](https://www.sqlite.org/lang_createview.html)using the @DatabaseView annotation.[b/67033276](https://issuetracker.google.com/67033276)
- **Auto Value** : Room now supports declaring[AutoValue](https://github.com/google/auto/blob/master/value/userguide/index.md)annotated classes as entities and POJOs. The Room annotations`@PrimaryKey`,`@ColumnInfo`,`@Embedded`and`@Relation`can now be declared in an auto value annotated class' abstract methods. Note that these annotation must also be accompanied by`@CopyAnnotations`for Room to properly understand them.[b/62408420](https://issuetracker.google.com/62408420)
- **Additional Rx Return Types Support** : DAO methods annotated with`@Insert`,`@Delete`or`@Update`now support Rx return types`Completable`,`Single<T>`and`Maybe<T>`.[b/63317956](https://issuetracker.google.com/63317956)
- **Immutable Types with`@Relation`** : Room previously required`@Relation`annotated fields to be settable but now they can be constructor parameters.
- `enableMultiInstanceInvalidation`: Is a new API in`RoomDatabase.Builder`to enable invalidation across multiple instances of RoomDatabase using the same database file. This multi-instance invalidation mechanism also works across multiple processes.[b/62334005](https://issuetracker.google.com/62334005)
- `fallbackToDestructiveMigrationOnDowngrade`: Is a new API in`RoomDatabase.Builder`to automatically re-create the database if a downgrade happens.[b/110416954](https://issuetracker.google.com/110416954)
- `ignoredColumns`: Is a new API in the`@Entity`annotation that can be used to list ignored fields by name. Useful for ignoring inherited fields on an entity.[b/63522075](https://issuetracker.google.com/63522075)

**API / Behavior Changes**

- `mCallback`and`mDatabase`in`RoomDatabase`are now`@Deprecated`and will be removed in the next major version of Room.[b/76109329](https://issuetracker.google.com/76109329)

**Bug Fixes**

- Fixed two issues where Room wouldn't properly recover from a corrupted database or a bad migration during initialization.[b/111504749](https://issuetracker.google.com/111504749)and[b/111519144](https://issuetracker.google.com/111519144)
- Room will now properly use Kotlin's primary constructor in data classes avoiding the need to declare the fields as`vars`.[b/105769985](https://issuetracker.google.com/105769985)

## October 1, 2018

Room`2.0.0`is released with no changes from`2.0.0-rc01`. Paging`2.0.0`is released with a single bugfix.

### Paging

**Bug Fixes**

- Fixed a crash that could occur with very fast scrolling using`PositionalDataSource`and placeholders[b/114635383](https://issuetracker.google.com/114635383).

## September 21, 2018

Lifecycle`2.0.0`is released with one bugfix from`2.0.0-rc01`in ViewModel.

### Lifecycle

**Bug Fixes**

- Fixed a ViewModel proguard rule that incorrectly removed constructors[b/112230489](https://issuetracker.google.com/112230489)

## September 20, 2018

### Navigation

Navigation`1.0.0-alpha06`is released with bug fixes and API changes.

**New Features**

- Shared Element Transitions for Fragment and Activity destinations are now supported[b/79665225](https://issuetracker.google.com/79665225). For more information, see[Implement navigation with the Navigation Architecture Component](https://developer.android.com/topic/libraries/architecture/navigation/navigation-implementing#shared-element)
- Selecting an item in`NavigationView`will now close any containing bottom sheet[b/112158843](https://issuetracker.google.com/112158843)

**API Changes**

- **Breaking Change:** The Navigator`navigate()`method now takes a`Navigator.Extras`parameter.
- NavController's`getGraph()`method is now`NonNull`[b/112243286](https://issuetracker.google.com/112243286)

**Bug Fixes**

- `NavigationUI.setupWithNavController()`no longer leaks views if used with views from individual destinations[b/111961977](https://issuetracker.google.com/111961977)
- Navigator`onSaveState()`is now only called once[b/112627079](https://issuetracker.google.com/112627079)

**Safe Args**

- Navigation destination Directions classes now extend their parent's Directions class if it exists[b/79871405](https://issuetracker.google.com/79871405)
- Directions and Args classes now have a useful`toString()`implementation[b/111843389](https://issuetracker.google.com/111843389)

## September 19, 2018

### WorkManager

WorkManager`1.0.0-alpha09`is released with bug fixes, infrastructure updates, and API changes.

**Known Issue**

If you run into the following issue: "More than one file was found with OS independent path 'META-INF/proguard/androidx-annotations.pro'", please put the following in your gradle file as a temporary workaround while we fix the issue in alpha10:  

### Groovy

```groovy
android {
    packagingOptions {
        exclude 'META-INF/proguard/androidx-annotations.pro'
    }
}
```

### Kotlin

```kotlin
android {
    packagingOptions {
        exclude("META-INF/proguard/androidx-annotations.pro")
    }
}
```

**Bug Fixes**

- Added another fix that was needed for the "100 jobs" error.[b/115560696](https://issuetracker.google.com/115560696)
- Added some fixes for foreign key constraint errors due to race conditions.[b/114705286](https://issuetracker.google.com/114705286)
- Delegated`ConstraintTrackingWorker.onStopped(boolean)`calls to the underlying`Worker`.[b/114125093](https://issuetracker.google.com/114125093)
- Enforce correct minimum backoff delay for Firebase JobDispatcher.[b/113304626](https://issuetracker.google.com/113304626)
- Improved threading guarantees internal to the library.
- Correct potential issue with deduping of`LiveData`internally.

**API Changes**

- You can now create your own`Worker`instances at runtime by specifying a`WorkerFactory`as part of the`WorkManager.Configuration`. The fallback factory is`DefaultWorkerFactory`, which matches behavior of previous versions of WorkManager.
  - The default constructors for`Worker`and`NonBlockingWorker`are now marked as deprecated. Please use the new constructor (`Worker(Context, WorkerParameters)`) and call`super(Context, WorkerParameters)`; future versions of WorkManager will remove the default constructor.
- We have started using the new`ListenableFuture`artifact internally (free of Guava dependencies). We will introduce ListenableFutures to the API in upcoming releases. This change will support the eventual unhiding of`NonBlockingWorker`.
- Add ability to trigger timed work in`TestDriver`via`TestDriver.setInitialDelayMet(UUID)`and`TestDriver.setPeriodDelayMet(UUID)`.[b/113360060](https://issuetracker.google.com/113360060)

**Breaking Changes**

- The default`Worker`and`NonBlockingWorker`constructors are deprecated. Please migrate to the new constructor ASAP. Future versions will remove the default constructor.

## August 27, 2018

### WorkManager

WorkManager`1.0.0-alpha08`is released with bug fixes.

**Bug Fixes**

- Explicitly labelled WorkManager components as direct boot unaware so they don't fire up during direct boot. In the future, we will provide a version of WorkManager that is direct boot-aware.[b/112665532](https://issuetracker.google.com/112665532)
- Fixed an issue where retried work was not running.[b/112604021](https://issuetracker.google.com/112604021)
- Fixed periodic work not executing repeatedly (related to the above issue).[b/112859683](https://issuetracker.google.com/112859683)
- Honored backoff policies when the app process is already running.
- Corrected exception messages in`Data`to indicate the limit is 10KB.
- Lowered maximum value of`Configuration.setMaxSchedulerLimit(int)`to 50 to account for some latency in`JobScheduler`processing completion.[b/112817355](https://issuetracker.google.com/112817355)

## August 16, 2018

### WorkManager

WorkManager`1.0.0-alpha07`is released with bug fixes and minor API changes.

**Bug Fixes**

- Fixed a potential SQL query with negative limits that could return an unbounded number of results.
- Work that has finished execution now correctly cancels all pending copies of that work in other Schedulers. This led to exceeding the`JobScheduler`jobs limit.[b/111569265](https://issuetracker.google.com/111569265)
- Fixed a`ConcurrentModificationException`in`ConstraintTracker`.[b/112272753](https://issuetracker.google.com/112272753)
- Changed return type annotations of`Data.getBooleanArray(String)`and`Data.getIntArray(String)`to`@Nullable`instead of`@NonNull`.[b/112275229](https://issuetracker.google.com/112275229)

**API Changes**

- `Worker`now extends a new class,`NonBlockingWorker`. This does not affect any current usage. In the future,`NonBlockingWorker`will become a fully supported entity for custom threading solutions.
- Changed return type annotations of`Data.getBooleanArray(String)`and`Data.getIntArray(String)`to`@Nullable`instead of`@NonNull`.[b/112275229](https://issuetracker.google.com/112275229)
- Kotlin extensions: deprecated`Map.toWorkData()`and added a top-level`workDataOf(vararg Pair<String, Any?>)`to be more consistent with existing APIs.

## August 10, 2018

### Navigation

Navigation`1.0.0-alpha05`is released with bug fixes.

**Bug Fixes**

- Fix a bug which cause incorrect backstack behavior.[b/111907708](https://issuetracker.google.com/issues/111907708)
- Fix a bug in`equals()`of Generated Args classes.[b/111450897](https://issuetracker.google.com/issues/111450897)
- Fix a build failure in Safe Args.[b/109409713](https://issuetracker.google.com/issues/109409713)
- Fix a conversion from resource identifiers to java names[b/111602491](https://issuetracker.google.com/issues/111602491)
- Fix error messages about nullability in Safe Args plugin.
- Add missing nullability annotations.

## August 6, 2018

AndroidX versions of Lifecycle, Room, and Paging release version`2.0.0-rc01`. All artifacts are unchanged from`2.0.0-beta01`.

## August 1, 2018

### WorkManager

WorkManager`1.0.0-alpha06`is released with bug fixes.

**Bug Fixes**

- Prevent a database lock when scheduling work.[b/111801342](https://issuetracker.google.com/issues/111801342)
- Fix a bug which causes`PeriodicWork`to not run on schedule when in Doze mode.[b/111469837](https://issuetracker.google.com/issues/111469837)
- Fix a race condition when tracking constraints which causes`WorkManager`to crash.[googlecodelabs/android-workmanager/issues/56](https://github.com/googlecodelabs/android-workmanager/issues/56)
- Create unique`WorkRequest`s when using`WorkRequest.Builder#build()`.[b/111408337](https://issuetracker.google.com/issues/111408337)
- Enable the use of`RescheduleReceiver`only when there are`WorkRequest`s that need it.[b/111765853](https://issuetracker.google.com/issues/111765853)

## July 24, 2018

### WorkManager

WorkManager`1.0.0-alpha05`is released with important bug fixes and logging changes.

**API Changes**

- `WorkManager.getInstance()`is now annotated with`@NonNull`instead of`@Nullable`. Instead, if the singleton isn't properly initialized in cases of manual initialization, the method will throw an`IllegalStateException`.**This is a breaking API change.**
- Added a new API,`Configuration.Builder.setMinimumLoggingLevel(int)`, which can control WorkManager verbosity. By default, WorkManager logs`Log.INFO`and above.
- Changed signature of`Data.getString()`so it no longer takes a default value (it is implicitly`null`).**This is a breaking API change.**
- Marked some methods needed only for internal usage as`@hide`. This includes the`Constraints`constructor,`Data.toByteArray()`, and`Data.fromByteArray(byte[])`.**This is a breaking API change.**

**Bug Fixes**

- WorkManager no longer executes work during known cases of auto-backup. This could have resulted in a crash.[b/110564377](https://issuetracker.google.com/issues/110564377)
- Fixed double-scheduling of`PeriodicWorkRequest`s when using`JobScheduler`.[b/110798652](https://issuetracker.google.com/issues/110798652)
- Fixed an issue with`PeriodicWorkRequest`s not executing correctly after device doze.[b/111469837](https://issuetracker.google.com/issues/111469837)
- Fixed an issue with initial delays when using Firebase JobDispatcher.[b/111141023](https://issuetracker.google.com/issues/111141023)
- Fixed some potential race conditions and timing issues.
- Correctly freed up`BroadcastReceiver`s that were no longer needed.
- Optimized rescheduling performance when apps restart after being force closed.
- Allowed`TestScheduler.setAllConstraintsMet(UUID)`to be called before or after enqueuing the given`WorkRequest`.[b/111238024](https://issuetracker.google.com/issues/111238024)

**Breaking Changes**

- `WorkManager.getInstance()`is now annotated with`@NonNull`instead of`@Nullable`.
- Changed signature of`Data.getString()`so it no longer takes a default value (it is implicitly`null`).
- Marked some methods needed only for internal usage as`@hide`. This includes the`Constraints`constructor,`Data.toByteArray()`, and`Data.fromByteArray(byte[])`.

## July 19, 2018

### Navigation

Navigation`1.0.0-alpha04`and the associated Safe Args gradle plugin contains a number of API changes, behavior changes, and bug fixes.

**API / Behavior Changes**

- NavHostFragment will always set the current Fragment as the primary navigation fragment, ensuring that child fragment managers are popped before the outer NavController is popped[b/111345778](https://issuetracker.google.com/issues/111345778)

**Safe Args**

- **Breaking Change:** `app:type`has been changed to`app:argType`to avoid conflicts with other libraries such as ConstraintLayout 2.0.0-alpha1[b/111110548](https://issuetracker.google.com/issues/111110548)
- Error messages from Safe Args are now clickable[b/111534438](https://issuetracker.google.com/issues/111534438)
- Args classes now confirms that`NonNull`attributes are actually not null[b/111451769](https://issuetracker.google.com/issues/111451769)
- Additional`NonNull`annotations have been added to NavDirections and Args generated classes[b/111455455](https://issuetracker.google.com/issues/111455455)[b/111455456](https://issuetracker.google.com/issues/111455456)

**Bug Fixes**

- Fixed an issue with the system back button after deep linking to a fragment destination[b/111515685](https://issuetracker.google.com/issues/111515685)

## July 12, 2018

### Navigation

Navigation`1.0.0-alpha03`and the associated Safe Args gradle plugin contains a number of API changes, behavior changes, and bug fixes.

**API / Behavior Changes**

- A NavigationUI.setupWithNavController method for Toolbar has been added[b/109868820](https://issuetracker.google.com/issues/109868820)
- A NavigationUI.setupWithNavController method for CollapsingToolbarLayout has been added[b/110887183](https://issuetracker.google.com/issues/110887183)
- popBackStack() now returns false when the back stack is empty or when the given destination ID is not in the back stack[b/110893637](https://issuetracker.google.com/issues/110893637)
- FragmentNavigator now ignores navigation operations after FragmentManager has saved state, avoiding "Can not perform this action after onSaveInstanceState" exceptions[b/110987825](https://issuetracker.google.com/issues/110987825)

**Safe Args**

- **Breaking Change:** Non-alphanumeric characters in action and argument names will be replaced by camel casing in the respective NavDirections method names
  - E.g.`DemoController.index`will become`setDemoControllerIndex`[b/79995048](https://issuetracker.google.com/issues/79995048)
  - E.g.`action_show_settings`will become`actionShowSettings`[b/79642240](https://issuetracker.google.com/issues/79642240)
- **Breaking Change:** Arguments are now considered non-null by default. To allow null values on string and parcelable arguments, add`app:nullable="true"`[b/79642307](https://issuetracker.google.com/issues/79642307)
- You can now use`app:type="long"`with defaultValues in the form of "123L"[b/79563966](https://issuetracker.google.com/issues/79563966)
- Parcelable arguments are now supported, using a fully qualified class name for`app:type`. The only default value supported is`"@null"`[b/79563966](https://issuetracker.google.com/issues/79563966)
- Args classes now implement`equals()`and`hashCode()`[b/79642246](https://issuetracker.google.com/issues/79642246)
- The Safe Args plugin can now be applied to library projects[b/80036553](https://issuetracker.google.com/issues/80036553)
- The Safe Args plugin can now be applied to feature projects[b/110011752](https://issuetracker.google.com/issues/110011752)

**Bug Fixes**

- Fixed issues when navigating during Fragment lifecycle methods[b/109916080](https://issuetracker.google.com/issues/109916080)
- Fixed issues when navigating through nested graphs multiple times[b/110178671](https://issuetracker.google.com/issues/110178671)
- Fixed issues when using`setPopUpTo`with the first destination in the graph[b/109909461](https://issuetracker.google.com/issues/109909461)
- Fixed issue where all`app:defaultValue`values were being passed as Strings[b/110710788](https://issuetracker.google.com/issues/110710788)
- aapt2 bundled with Android Gradle Plugin 3.2 Beta 01 now adds keep rules for every`android:name`attribute in Navigation XML files[b/79874119](https://issuetracker.google.com/issues/79874119)
- Fixed memory leak when replacing the default FragmentNavigator[b/110900142](https://issuetracker.google.com/issues/110900142)

## July 2, 2018

AndroidX versions of Lifecycle, Room, and Paging release version`2.0.0-beta01`.

### Lifecycle

**Bug Fixes**

- Fixed LifecycleObserver proguard rule to keep only implementations, not subinterfaces[b/71389427](https://issuetracker.google.com/issues/71389427)
- Fixed ViewModel proguard rules to allow obfuscation and shrinking

### Room

**API / Behavior Changes**

- Added`RoomDatabase.Builder.setQueryExecutor()`to allow customization of where queries are run
- Added RxJava2`Observable`support
- Generated DAO and Database implementations are now final

**Bug Fixes**

- Specify class/field name in "cannot find getter for field" error[b/73334503](https://issuetracker.google.com/issues/73334503)
- Fixed RoomOpenHelper backwards compatibility with older versions of Room[b/110197391](https://issuetracker.google.com/issues/110197391)

### Paging

**Bug Fixes**

- Fixed content disappearing in some prepend cases (placeholders disabled, PositionalDataSource)[b/80149146](https://issuetracker.google.com/issues/80149146)
- (Already released in`1.0.1`) Fixed crashes where`PagedListAdapter`and`AsyncPagedListDiffer`would fail to signal move events.[b/110711937](https://issuetracker.google.com/issues/110711937)

## June 26, 2018

### Paging

Paging`1.0.1`is released with a single bugfix in`runtime`. We highly recommend using`1.0.1`for stability. Paging RxJava2`1.0.1`is also released, and is identical to`1.0.0-rc1`.

**Bug Fixes**

- Fixed crashes where`PagedListAdapter`and`AsyncPagedListDiffer`would fail to signal move events.[b/110711937](https://issuetracker.google.com/issues/110711937)

### WorkManager

WorkManager`1.0.0-alpha04`is released.

**Bug Fixes**

- `PeriodicWorkRequest`s are now correctly rescheduled when using the`AlarmManager`based implementation.

- Fixed a potential ANR when rescheduling all workers after a force stop or a reboot.[b/110507716](https://issuetracker.google.com/issues/110507716)

- Added nullability annotations to various WorkManager APIs.[b/110344065](https://issuetracker.google.com/issues/110344065)

- Log uncaught exceptions that occur during Worker execution.[b/109900862](https://issuetracker.google.com/issues/109900862)

- Allowed destructive database migrations in case you decide to roll back to an older version of WorkManager.[b/74633270](https://issuetracker.google.com/issues/74633270)

- Fixed a migration crash if creating duplicate implicit tags. This is a very rare issue that occurred only if you used the same implicit tag format yourself.

## June 19, 2018

### Room

Room`1.1.1`is released. This release is identical to Room`1.1.1-rc1`.

### WorkManager

WorkManager`1.0.0-alpha03`is released.

**Bug Fixes**

- Fixed a race condition in the`AlarmManager`based implementation.[b/80346526](https://issuetracker.google.com/issues/80346526).

- Fixed duplicate jobs when using`JobScheduler`after a device reboot.

- Jobs with Content URI triggers now persist across reboots.[b/80234744](https://issuetracker.google.com/issues/80234744)

- Documentation updates.[b/109827628](https://issuetracker.google.com/issues/109827628),[b/109758949](https://issuetracker.google.com/issues/109758949),[b/80230748](https://issuetracker.google.com/issues/80230748)

- Fixed a crash when re-enqueuing a`WorkRequest`.[b/109572353](https://issuetracker.google.com/issues/109572353).

- Fixed Kotlin compiler warnings when using the`work-runtime-ktx`dependency.

- WorkManager now uses`Room`version`1.1.1-rc1`.

**API Changes**

- Added`getStatusesSync()`, the synchronous version of`WorkContinuation.getStatuses()`.

- `Worker`has the ability to distinguish between user-initiated cancellation and temporary os-requested stopping.`Worker.isStopped()`returns`true`if any kind of stop has been requested.`Worker.isCancelled()`returns`true`when the work has been explicitly cancelled.[b/79632247](https://issuetracker.google.com/issues/79632247)

- Add support for[JobParameters#getNetwork()](https://developer.android.com/reference/android/app/job/JobParameters.html#getNetwork())on API 28. This is exposed via`Worker.getNetwork()`.

- Added`Configuration.Builder.setMaxSchedulerLimit(int maxSchedulerLimit)`so you can enforce how many jobs can be sent to`JobScheduler`or`AlarmManager`. This helps prevent`WorkManager`from taking all your available`JobScheduler`slots.

- Added`Configuration.setJobSchedulerJobIdRange(int minJobSchedulerId, int maxJobSchedulerId)`which helps define a range of`JobScheduler`job ids safe for`WorkManager`to use.[b/79996760](https://issuetracker.google.com/issues/79716516)

- `Worker.getRunAttemptCount()`returns the current run count for a given`Worker`.[b/79716516](https://issuetracker.google.com/issues/79716516)

- `WorkManager.enqueueUniquePeriodicWork(String uniqueWorkName, ExistingPeriodicWorkPolicy existingPeriodicWorkPolicy, PeriodicWorkRequest periodicWork)`allows you to enqueue a unique`PeriodicWorkRequest`s.[b/79600647](https://issuetracker.google.com/issues/79600647)

- `WorkManager.cancelAllWork()`cancels all`Worker`s. Libraries that depend on`WorkManager`can query when this method was called last by using`WorkManager.getLastCancelAllTimeMillis()`for additional cleanup of internal state.

- Added`WorkManager.pruneWork()`to remove completed jobs from the internal database.[b/79950952](https://issuetracker.google.com/issues/79950952),[b/109710758](https://issuetracker.google.com/issues/109710758)

**Behavior Changes**

- Added an implicit tag for all`WorkRequest`s, which is the fully qualified class name for the`Worker`. This allows the ability to remove`WorkRequest`s without`tag`s or when the`id`is not available.[b/109572351](https://issuetracker.google.com/issues/109572351)

**Breaking Changes**

- Renamed`Worker.WorkerResult`to`Worker.Result`.

- `Worker.onStopped`now has an**additional** `isCancelled`parameter which is set to`true`when the`Worker`has explicitly been cancelled.

## June 7, 2018

Navigation`1.0.0-alpha02`is released.

### Navigation

**Behavior Changes**

- `FragmentNavigator`now uses`setReorderingAllowed(true)`.[b/109826220](https://issuetracker.google.com/issues/109826220)

- Navigation now URLDecodes arguments parsed from deep links URLs.[b/79982454](https://issuetracker.google.com/issues/79982454)

**Bug Fixes**

- Fixed an`IllegalStateException`when calling navigate from Fragment lifecycle methods.[b/79632233](https://issuetracker.google.com/issues/79632233)

- Navigation now depends on Support Library 27.1.1 to fix flickering when using animations.[b/80160903](https://issuetracker.google.com/issues/80160903)

- Fixed an`IllegalArgumentException`when using defaultNavHost="true" as a child fragment.[b/79656847](https://issuetracker.google.com/issues/79656847)

- Fixed a`StackOverflowError`when using NavDeepLinkBuilder.[b/109653065](https://issuetracker.google.com/issues/109653065)

- Fixed an`IllegalArgumentException`when navigating back to a nested graph.[b/80453447](https://issuetracker.google.com/issues/80453447)

- Fixed an issue with overlapping Fragments when using`launchSingleTop`.[b/79407969](https://issuetracker.google.com/issues/79407969)

- Navigation now builds the correct synthetic back stack for nested graphs.[b/79734195](https://issuetracker.google.com/issues/79734195)

- NavigationUI will now highlight the correct item when using a nested graph as a`MenuItem`.[b/109675998](https://issuetracker.google.com/issues/109675998)

**API Changes**

- The`clearTask`attribute for actions and the associated API in`NavOptions`has been deprecated.[b/80338878](https://issuetracker.google.com/issues/80338878)

- The`launchDocument`attribute for actions and the associated API in`NavOptions`has been deprecated.[b/109806636](https://issuetracker.google.com/issues/109806636)

## May 24, 2018

WorkManager`1.0.0-alpha02`is released.

### WorkManager

**Bug Fixes**

- Fixed a`NullPointerException`on`State.isFinished()`.[b/79550068](https://issuetracker.google.com/issues/79550068)

- Fixed an issue which caused`Worker`s to be rescheduled on`Application.onCreate()`.[b/79660657](https://issuetracker.google.com/issues/79660657)

- Fixed an issue where you could schedule more work than is allowed by the OS.[b/79497378](https://issuetracker.google.com/issues/79497378)

- Moved cleanup of wake locks associated with`Worker`s to the background thread.

- The`AlarmManager`implementation now correctly cleans up when all pending work is complete.

- Fixed cleanup SQL queries which affected non-English locales.[b/80065360](https://issuetracker.google.com/issues/80065360)

- Added support for`float`s in`Data`.[b/79443878](https://issuetracker.google.com/issues/79443878)

- `Data.Builder.putAll()`now returns an instance of the`Builder`.[b/79699162](https://issuetracker.google.com/issues/79699162)

- More javadoc and fixes in documentation.[b/79691663](https://issuetracker.google.com/issues/79691663)

**API Changes**

- `Worker`s can react to being stopped.`Worker.isStopped()`can be used to check if a`Worker`has been stopped.`Worker.onStopped()`can be used to perform lightweight cleanup operations.

- `Worker.getTags()`API returns a`Set`of tags associated with the`Worker`.

- Added`javax.time.Duration`overloads for APIs which take a combination of duration and`TimeUnit`s. This is guarded by`@RequiresApi(26)`.

- `WorkManager`extensions have moved from the`androidx.work.ktx`package to the`androidx.work`package. The old extensions are deprecated and will be removed in a future version.

- `Configuration.withExecutor()`is deprecated. Use`Configuration.setExecutor()`instead.

## May 16, 2018

Paging RxJava2`1.0.0-rc1`and Room`1.1.1-rc1`are released. We highly recommend using Room`1.1.1-rc1`instead of`1.1.0`if you are using migrations.

### Room

Fixed a bug where Room would not handle post migration initialization properly[b/79362399](https://issuetracker.google.com/issues/79362399)

### Paging

Paging`rxjava2`is moving to release candidate with no changes from the initial alpha.

## May 8, 2018

Paging 1.0, Navigation and WorkManager Alphas, Room 1.1, AndroidX

[Paging](https://developer.android.com/topic/libraries/architecture/paging)`1.0.0`and[Room](https://developer.android.com/topic/libraries/architecture/room)`1.1.0`are released, along with alphas for two new Architecture Components - Navigation, and WorkManager.

Paging and Room have no changes since the latest release candidates.

### New Library: Navigation

[Navigation](https://developer.android.com/topic/libraries/architecture/navigation/navigation-implementing)provides a framework for building in-app navigation. This initial release is`1.0.0-alpha01`.

### New Library: WorkManager

[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)simplifies scheduling and execution of guaranteed, constraint-aware background work. This initial release is`1.0.0-alpha01`.

### AndroidX

Architecture components are moving to become part of AndroidX, including updated package names, artifact names, and dependencies on other AndroidX libraries. These are released under version`2.0.0-alpha1`to use in conjunction with other AndroidX libraries.

### Kotlin Extensions

ViewModel, ReactiveStreams, and Sqlite (previously 'Database' component of Room) all have Kotlin extension libraries added as part of the AndroidX alpha release. In addition, Navigation and WorkManager include -ktx modules. Each of these extension modules can be found in[adding components](https://developer.android.com/topic/libraries/architecture/adding-components#kotlin).

## May 2, 2018

- Room 1.1.0 Release Candidate
- Room`1.1.0-rc1`is released.

**Bug Fixes**

- Room is now compatible with Kotlin`1.2.40`.[b/78328708](https://issuetracker.google.com/issues/78328708)

## April 19, 2018

Paging Release Candidate

Paging`1.0.0-rc1`and Room`1.1.0-beta3`are released.

### Paging

We**do not have** any more known issues or new features scheduled for the Paging`1.0.0`release. Please upgrade your projects to use`1.0.0-rc1`and help us battle test it so that we can ship a rock solid`1.0.0`.

There are no changes in this release, it is the same as`1.0.0-beta1`.

### Room

**Bug Fixes**

- Fix compilation error when a Kotlin POJO references a relation entity that was defined in Java[b/78199923](https://issuetracker.google.com/issues/78199923)

## April 5, 2018

Room`1.1.0-beta2`, Paging`1.0.0-beta1`, and Paging RxJava`1.0.0-alpha1`are released.

Paging will be in beta for a short time before progressing to release candidate. We are not planning further API changes for`Paging 1.0`, and the bar for any API changes is very high.

Alpha RxJava2 support for Paging is released as a separate optional module (`android.arch.paging:rxjava2:1.0.0-alpha1`) and will temporarily be versioned separately until it stabilizes.

This new library provides an RxJava2 alternative to`LivePagedListBuilder`, capable of constructing`Observable`s and`Flowable`s, taking`Scheduler`s instead of`Executor`s:  

### Kotlin

```kotlin
val pagedItems = RxPagedListBuilder(myDataSource, /* page size */ 50)
        .setFetchScheduler(myNetworkScheduler)
        .buildObservable()
```

### Java

```java
Observable<PagedList<Item>> pagedItems =
        RxPagedListBuilder(myDataSource, /* page size */ 50)
                .setFetchScheduler(myNetworkScheduler)
                .buildObservable();
```

### Paging

**New Features**

- `RxPagedListBuilder`is added via the new`android.arch.paging:rxjava2`artifact.

**API Changes**

- API changes to clarify the role of executors in builders:

  - Renamed`setBackgroundThreadExecutor()`to`setFetchExecutor()`(in`PagedList.Builder`and`LivePagedListBuilder`)

  - Renamed`setMainThreadExecutor()`to`setNotifyExecutor()`(in`PagedList.Builder`).

- Fixed`PagedList.mCallbacks`member to be private.

**Bug Fixes**

- `LivePagedListBuilder`triggers initial`PagedList`load on the specified executor, instead of the Arch Components IO thread pool.

- Fixed invalidate behavior in internal`DataSource`wrappers (used to implement`DataSource.map`, as well as placeholder-disabled`PositionalDataSource`loading)[b/77237534](https://issuetracker.google.com/issues/77237534)

### Room

**Bug Fixes**

- Fixed a critical bug in Room's Rx`Single`and`Maybe`implementations where it would recycle the query ahead of time, causing problems if you add more than 1 observer to the returned`Single`or`Maybe`instancces.[b/76031240](https://issuetracker.google.com/issues/76031240)

- [RoomDatabase.clearAllTables](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase#clearAllTables())will not`VACUUM`the database if it is called inside a transaction.[b/77235565](https://issuetracker.google.com/issues/77235565)

## March 21, 2018

Room`1.1.0-beta1`, Paging`1.0.0-alpha7`and Lifecycles`1.1.1`are released.

### Room

**API Changes**

- Based on API Review feedback,`@RawQuery`does not accept passing a`String`as the query parameter anymore. You need to use[SupportSQLiteQuery](https://developer.android.com/reference/android/arch/persistence/db/SupportSQLiteQuery). (see[SimpleSQLiteQuery](https://developer.android.com/reference/android/arch/persistence/db/SimpleSQLiteQuery)to easily create an instance of[SupportSQLiteQuery](https://developer.android.com/reference/android/arch/persistence/db/SupportSQLiteQuery)with argument support).
- RoomDatabase.Builder's[fallbackToDestructiveMigrationFrom](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase.Builder#fallbackToDestructiveMigrationFrom(java.lang.Integer...))method now accepts`vararg int`instead of`vararg Integer`.

**Bug Fixes**

- [RoomDatabase.clearAllTables](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase#clearAllTables())now tries to return space back to the operating system by setting a WAL checkpoint and`VACUUM`ing the database.

- [`@RawQuery`](https://developer.android.com/reference/android/arch/persistence/room/RawQuery)now accepts any Pojo for the`observedEntities`property as long as the Pojo references to one or more entities via its`Embedded`fields or`Relation`s.[b/74041772](https://issuetracker.google.com/issues/74041772)

- Paging: Room's DataSource implementation now correctly handles multi-table dependencies (such as relations, and joins). Previously these would fail to trigger new results, or could fail to compile.[b/74128314](https://issuetracker.google.com/issues/74128314)

### Lifecycles

Only one small change:`android.arch.core.util.Function`is moved from`arch:runtime`to`arch:common`. This allows it to be used without the runtime dependency, e.g. in`paging:common`below.

`lifecycle:common`is a dependency of`lifecycle:runtime`, so this change doesn't affect`lifecycle:runtime`directly, only modules that depend directly on`lifecycle:common`, as Paging does.

### Paging

Paging`1.0.0-alpha7`is released alongside Lifecycles`1.1.1`. As Paging alpha7 depends on the move of the`Function`class mentioned above, you will need to update your`lifecycle:runtime`dependency to`android.arch.lifecycle:runtime:1.1.1`.

Paging`alpha7`is planned to be the final release before Paging hits beta.

**API Changes**

- `DataSource.LoadParams`objects now have a public constructor and`DataSource.LoadCallback`objects are now abstract. This enables wrapping a`DataSource`or directly testing a`DataSource`with a mock callback.[b/72600421](https://issuetracker.google.com/issues/72600421)
- Mappers for DataSource and DataSource.Factory
  - `map(Function<IN,OUT>)`allows you to transform, wrap, or decorate results loaded by a`DataSource`.
  - `mapByPage(<List<IN>,List<OUT>>)`enables the same for batch processing (e.g. if items loaded from SQL need to additionally query a separate database, that can be done as a batch.)
- `PagedList#getDataSource()`is added as a convenience method[b/72611341](https://issuetracker.google.com/issues/72611341)
- All deprecated classes have been removed from the API, including the remains of`recyclerview.extensions`package, and the`LivePagedListProvider`.
- `DataSource.Factory`is changed from an interface to an abstract class to enable map functionality.

**Bug Fixes**

- Changed Builders to be final.[b/70848565](https://issuetracker.google.com/issues/70848565)
- Room`DataSource`implementation is now fixed to handle multi-table queries - this fix is contained within Room 1.1.0-beta1, see above.
- Fixed a bug where`BoundaryCallback.onItemAtEndLoaded`would not be invoked for`PositionalDataSource`if placeholders are enabled and the total size is an exact multiple of the page size.

## March 2, 2018

Room`1.1.0-alpha3`is released. This is the last planned alpha release for Room`1.1.0`.

**API Changes**

- [InvalidationTracker](https://developer.android.com/reference/android/arch/persistence/room/InvalidationTracker)'s`addObserver`and`removeObserver`methods are now synchronous and need to be called on a non-ui thread. This prevents some race conditions while observing tables.

- There is a new`clearAllTables()`method on the[RoomDatabase](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase)class that will truncate all table contents.[b/63807999](https://issuetracker.google.com/issues/63807999)

- `SupportSQLiteQuery`now has a`getArgCount()`method that returns the number of query parameters.[b/67038952](https://issuetracker.google.com/issues/67038952)

**Bug Fixes**

- `@RawQuery`is now properly supported for Paging queries.[b/72600425](https://issuetracker.google.com/issues/72600425)

- Room now properly names generated`Dao`classes to avoid name conflicts when 2 or more`Dao`interfaces are inner classes in the same package and have the same name.[b/73536380](https://issuetracker.google.com/issues/73536380)

- Generic field types in`Pojo`s are properly parsed as member of the extending class.[b/73534868](https://issuetracker.google.com/issues/73534868)

- Query parameters in`Dao`interfaces that are inherited from dependency artifacts are now properly parsed.[b/68118746](https://issuetracker.google.com/issues/68118746)

- Queries generated for`@Relation`s now properly escape the field names.[b/70925483](https://issuetracker.google.com/issues/70925483)

## February 27, 2018

Paging`1.0.0-alpha6`is released alongside Support Library release 27.1.0.`ListAdapter`and a few related classes have been moved from the Paging Library directly to Recyclerview, alongside a few renames to make the function of certain classes clearer. This alpha release of paging is likely the last to have significant API breaking changes.

**API Changes**

- Classes moved to recyclerview-v7:
  - `ListAdapter`
- Classes renamed, and moved to recyclerview-v7:
  - `ListAdapterHelper`-\>`AsyncListDiffer`
  - `ListAdapterConfig`-\>`AsyncDifferConfig`
  - `DiffCallback`-\>`DiffUtil.ItemCallback`
- Classes renamed inside paging-runtime:
  - `PagedListAdapterHelper`-\>`AsyncPagedListDiffer`

The classes that were moved were useful alongside RecyclerView, independent of the Paging Library. This means they can be used without depending upon a Paging alpha release, but also means apps using Paging must upgrade to Alpha 6, and Support Library 27.1.0 at the same time.

\*\* Migration guide for Paging Alpha6: \*\*

- Update paging and recyclerview dependencies to`android.arch.paging:runtime:1.0.0-alpha6`and`com.android.support:recyclerview-v7:27.1.0`
  - these must be done simultaneously, as ListAdapter was moved from Paging to RecyclerView
- Update any references of`ListAdapterHelper`to`AsyncListDiffer`
  - `getItem(index)`/`getItemCount()`have been removed, in favor of the pattern of calling`getCurrentList().getItem(index)`and`getCurrentList().size()`, which are more explicit.
- Update any references of`ListAdapterConfig`to`AsyncDifferConfig`
- Update any references of`DiffCallback`to`DiffUtil.IttemCallback`
- Update any references of`PagedListAdapterHelper`to`AsyncPagedListDiffer`
- Update references of`setList()`to`submitList()`
  - renamed to clarify async nature of list diffing

**Bug Fixes**

- Fixed passing incorrect initial position to initial load when placeholders are disabled.[b/73513780](https://issuetracker.google.com/issues/73513780)

## February 15, 2018

Room`1.1.0-alpha2`is released.

**New Features**

- Room now supports opening database in[write ahead logging](https://www.sqlite.org/wal.html)mode. In this mode, your writes will no longer block your read queries. Even though it consumes more memory (due to multiple connections), this mode is usually faster. By default, Room will use WAL if the device is`API 16`or above and it is**not** a low memory device. You can control this behavior by using the[`setJournalMode()`](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase.Builder#setJournalMode(android.arch.persistence.room.RoomDatabase.JournalMode))method on the`RoomDatabase.Builder`.[b/67757002](https://issuetracker.google.com/issues/67757002)

- **Guava Support** : Room now supports returning[Guava](https://github.com/google/guava/tree/master/android)`Optional<T>`or`ListenableFuture<T>`in`DAO`queries. To use`ListenableFuture<T>`, you need to import`guava`artifact from Room (`android.arch.persistence.room:guava:1.1.0-alpha2`).

- Room now support returning`java.util.Optional<T>`from`DAO`queries.

- Interface methods with default implementations are now supported in`@Transaction`methods in`DAO`classes. This works for both`Java 8`and`Kotlin`.[b/72416735](https://issuetracker.google.com/issues/72416735)

**Bug Fixes**

- Constructors with`@Relation`will not cause a compilation error if there is another constructor that can be used.[b/72884434](https://issuetracker.google.com/issues/72884434)

- Table names escaped with`'`in`@Query`methods are now properly escaped for invalidation tracker.[b/72366965](https://issuetracker.google.com/issues/72366965)

- Room now uses the Kotlin`@Metadata`annotations to read class structure during the annotation processing. This means, even if a pojo is inherited from a dependency, its constructor parameter names can be read properly.[b/67181813](https://issuetracker.google.com/issues/67181813)

- An issue with finding downgrade migration paths is fixed.[b/72153525](https://issuetracker.google.com/issues/72153525)

- Non default column types are now properly handled when migrating from an existing database to Room.[b/71953987](https://issuetracker.google.com/issues/71953987)

- Room now properly handles persisting`boolean?`fields in Kotlin classes.[b/72786402](https://issuetracker.google.com/issues/72786402)

## January 22, 2018

Lifecycles`1.1.0`, Room`1.1.0-alpha1`and Paging`1.0.0-alpha5`are released.

### Lifecycle 1.1.0

**Packaging Changes**

New, much smaller dependencies are now available:

- `android.arch.lifecycle:livedata:1.1.0`
- `android.arch.lifecycle:viewmodel:1.1.0`

| **Note:** Lifecycle Extensions`1.0.0`(`android.arch.lifecycle:extensions:1.0.0`) is**not** compatible with`livedata:1.1.0`or`viewmodel:1.1.0`. Please update to`extensions:1.1.0`, which includes a transitive dependency on`livedata:1.1.0`and`viewmodel 1.1.0`.
| **Note:** `android.arch.lifecycle:reactivestreams:1.1.0`now only depends on`android.arch.lifecycle:livedata:1.1.0`, not all of`android.arch.lifecycle:extensions:1.1.0`.

**API Changes**

- The deprecated`LifecycleActivity`and`LifecycleFragment`have now been**removed** - please use`FragmentActivity`,`AppCompatActivity`or support`Fragment`.
- `@NonNull`annotations have been added to`ViewModelProviders`and`ViewModelStores`
- `ViewModelProviders`constructor has been deprecated - please use its static methods directly
- `ViewModelProviders.DefaultFactory`has been deprecated - please use`ViewModelProvider.AndroidViewModelFactory`
- The static`ViewModelProvider.AndroidViewModelFactory.getInstance(Application)`method has been added to retrieve a static`Factory`suitable for creating`ViewModel`and`AndroidViewModel`instances.

### Room 1.1.0-alpha1

**New Features**

- `RawQuery`: This new API allows`@Dao`methods to receive the SQL as a query parameter[b/62103290](https://issuetracker.google.com/issues/62103290),[b/71458963](https://issuetracker.google.com/issues/71458963)
- `fallBackToDestructiveMigrationsFrom`: This new API in`RoomDatabase.Builder`allows for finer grained control over from which starting schema versions destructive migrations are allowed (as compared to fallbackToDestructiveMigration)[b/64989640](https://issuetracker.google.com/issues/64989640)
- Room now only supports newer Paging APIs (alpha-4+), dropping support for the deprecated`LivePagedListProvider`. To use the new Room alpha, you'll need to use paging`alpha-4`or higher, and switch from`LivePagedListProvider`to`LivePagedListBuilder`if you haven't already.

**Bug Fixes**

- Improved support for Kotlin Kapt types.[b/69164099](https://issuetracker.google.com/issues/69164099)
- Order of fields do not invalidate schema anymore.[b/64290754](https://issuetracker.google.com/issues/64290754)

### Paging 1.0.0-alpha5

**Bug Fixes**

- Fix page loading when placeholders are disabled[b/70573345](https://issuetracker.google.com/issues/70573345)
- Additional logging for tracking down IllegalArgumentException bug[b/70360195](https://issuetracker.google.com/issues/70360195)(and speculative Room-side fix)
- Javadoc sample code fixes[b/70411933](https://issuetracker.google.com/issues/70411933),[b/71467637](https://issuetracker.google.com/issues/71467637)

## December 11, 2017

Paging`alpha4-1`is released. This is a small bugfix release for Paging alpha 4.

**Bug Fixes**

- Don't check callback parameters for invalid data sources.[b/70353706](https://issuetracker.google.com/issues/70353706),[b/70360195](https://issuetracker.google.com/issues/70360195)

## December 7, 2017

Paging`alpha4`is released, with significant changes and additions, mostly targeting network, and network + database usecases.

**API Changes**

- `DataSource`is now an async API, to make paging directly from network easier:

  - Single entry point for initial size and data
  - Supports network retry by holding onto callback, and dispatching later
  - Threadsafe callbacks allow async loading for creating single network backed`PagedList`on UI thread.
  - Clearer error behavior around initial load parameters
- `TiledDataSource`is renamed to`PositionalDataSource`to reflect its position-based indexing, and the fact that it doesn't tile when placeholders are disabled.

- `PageKeyedDataSource`is added to support next/previous tokens embedded in network page loads.`KeyedDataSource`renamed to`ItemKeyedDataSource`to make difference clear.

- `LivePagedListBuilder`and`DataSource.Factory`replace`LivePagedListProvider`. The builder provides the same capability with more customization and simpler defaults. The factory allows`DataSource`generation code to remain independent of`LiveData`.

- `PagedList.BoundaryCallback`added for the database + network usecase.

- `PagedList.Builder`constructor takes`DataSource`+`PagedList.Config`, now more similar to`LivePagedListBuilder`, and allows diamond operator in Java language, or inferred types in Kotlin.

- `PagedList.getConfig()`added, and`PagedList.Config`now has public member properties.

- `KeyedDataSource.loadBefore()`no longer expects results reversed.

- `PagedListAdapter.onCurrentListChanged()`added to listen for updates on which PagedList is being displayed.

**Bug Fixes**

- Fixed IndexOutOfBoundsException in PagedListAdapter(Helper)[b/67883658](https://issuetracker.google.com/issues/67883658)

## 1.0.0 - November 6, 2017

All major components (except Paging) are now`1.0.0`. This is the exact same release as`rc1`except for one change to the`reactivestreams`library.

**Bug Fixes**

- [`LiveDataReactiveStreams`](https://developer.android.com/reference/android/arch/lifecycle/LiveDataReactiveStreams)now properly implements the[Reactive Streams](https://github.com/reactive-streams/reactive-streams-jvm/blob/v1.0.1/README.md#specification)specification.[b/67999342](https://issuetracker.google.com/issues/67999342)

## Release Candidate - October 18, 2017

All major artifacts (except Paging) are now`1.0.0-rc1`.

We**do not have** any more known issues or new features scheduled for the`1.0.0`release. Please upgrade your projects to use`1.0.0-rc1`and help us to battle test it so that we can ship a rock solid`1.0.0`.

**Behavior Change**

- With this release,`Lifecycle.Event#ON_STOP`is now dispatched when`onSaveInstanceState`is called (previous, it was just marked as`CREATED`without dispatching`ON_STOP`). You can read more about it in the[Lifecycles documentation](https://developer.android.com/topic/libraries/architecture/lifecycle#onStop-and-savedState).

**Bug Fixes**

- Room:

  - Room now depends on the latest xerial artifact which fixes the`OutOfMemory`problems during compilation.[b/62473121](https://issuetracker.google.com/issues/62473121)
  - `Query`methods can now be annotated with[`@Transaction`](https://developer.android.com/reference/android/arch/persistence/room/Transaction). See[reference docs on`@Transaction`](https://developer.android.com/reference/android/arch/persistence/room/Transaction)for details.[b/65112315](https://issuetracker.google.com/issues/65112315)
  - `StringUtil`class in Room is removed from the public API (it was never intended as a public API).
- Lifecycles:

  - `LiveData`properly works when Activity is partially covered on API \< 24.[b/65665621](https://issuetracker.google.com/issues/65665621)

  - `OnLifecycleEvent`methods in parent classes are now properly called or a warning is printed during compilation if it is not possible.[b/63474615](https://issuetracker.google.com/issues/63474615)

  - [Lifecycle](https://developer.android.com/reference/android/arch/lifecycle/Lifecycle)now holds a`WeakReference`back to its[LifecycleOwner](https://developer.android.com/reference/android/arch/lifecycle/LifecycleOwner)to avoid leaking the[LifecycleOwner](https://developer.android.com/reference/android/arch/lifecycle/LifecycleOwner)if Lifecycle is kept in memory longer than usual (this is just a precaution, you should still be careful not to leak the`Lifecycle`).

## October 9, 2017

Paging`alpha-3`is released; which makes it compatible with the`beta 2`release of Lifecycles and Room.

**Bug Fixes**

- Improved Paging documentation.

## October 5, 2017

All major artifacts (except Paging) are now`beta 2`. There is no new version of Paging in this release.

**Bug Fixes**

- Lifecycles:

  - `LiveDataReactiveStreams`now properly unsubscribes from the source publisher when`LiveData`is not active.[b/62609183](https://issuetracker.google.com/issues/62609183)
  - Lifecycle events are properly propagated to parent classes when the parent class is from another module.[b/63474615](https://issuetracker.google.com/issues/63474615)
  - LiveData properly handles observers when they unsubscribe during subscrition creation.[b/66337741](https://issuetracker.google.com/issues/66337741)
  - `FullLifecycleObserver`for Java 8 Language artifact is now available in the dependency tree.[b/66525578](https://issuetracker.google.com/issues/66525578)

  - For proguard, please add the following lines to your proguard file. (This won't be necessary when 1.0.0 ships)

    - `-keep class * implements android.arch.lifecycle.GeneratedAdapter {<init>(...);}`
- Room:

  - Room now prints an error at compile time when the returned Pojo in a`@Query`method has a`@NonNull`field that does not match any of the columns in the query response. If the field is`@Nullable`, Room only prints a warning.[b/67115337](https://issuetracker.google.com/issues/67115337)
  - Room now validates indices in newer OS versions.[b/63132683](https://issuetracker.google.com/issues/63132683)
  - Room picks no-arg constructor by default if there are multiple matching constructors in a Pojo.[b/67353427](https://issuetracker.google.com/issues/67353427)
  - Single column primary keys can be`Nullable`if it is an`Integer`or a`Long`.[b/67086876](https://issuetracker.google.com/issues/67086876)
  - Invalidation tracker properly handles re-entry in test mode.[b/65471397](https://issuetracker.google.com/issues/65471397)
  - Room now checks for invalid characters in column and table names at compile time (invalid characters:`````,`"`).[b/64749111](https://issuetracker.google.com/issues/64749111)

## September 21, 2017

With this release, all Architecture Components modules reach to at least`beta 1`(except the new Paging Library which is`alpha 2`).

We are not planning any more API changes. Unplanned changes might happen, but the bar for changing any API before`1.0.0`stable is very high and unlikely to happen.

- LifecycleActivity \& LifecycleFragment will be removed before`1.0.0`stable. They are not needed when using Support Library`26.1.0`or later.

Unlike the alpha phase, beta phase is scheduled to be a very short duration.

**Version Changes**

- Lifecycle Extensions and Room are now`beta 1`
- Paging is now`alpha 2`
- No changes in Lifecycles (runtime, common) and Arch Core (common). Both of these artifacts are version`1.0.0`since September 13.

**New Artifacts**

- Lifecycles now have a new artifact called`common-java8`. This artifact contains a new interface called[DefaultLifecycleObserver](https://developer.android.com/reference/android/arch/lifecycle/DefaultLifecycleObserver); which has default implementations for all Lifecycle methods. If you are using Java 8 language, you should prefer this artifact over annotations.

  - Due to a bug in`beta1`, you need to add an explicit dependency on`android.arch.lifecycle:common:1.0.1`module to use the new`common-java8`artifact. This issue will be fixed in`beta2`.

**Packaging Changes**

- `android.arch.persistence.room.db`has been moved to`android.arch.persistence.db`
- `android.arch.persistence.room.db-impl`has been moved and renamed to`android.arch.persistence.db-framework`

Both of these artifacts are already a dependency on Room so unless you were directly using them, you should not need to change anything in your build files.

**API Changes**

- Room:

  - [@ColumnInfo](https://developer.android.com/reference/android/arch/persistence/room/ColumnInfo)annotation now supports setting a collation on the column.[b/62007004](https://issuetracker.google.com/issues/62007004)
  - `transient`fields are now ignored by default unless they are annotated with`@ColumnInfo`,`@Embedded`or`@Relation`.[b/62600692](https://issuetracker.google.com/issues/62600692)
  - Primary Keys must be annotated with`@NonNull`unless they are auto generated.[b/64292391](https://issuetracker.google.com/issues/64292391)
    - This change may require a schema migration. Sorry for the inconvenience.
  - Added a new convenience annotation ([@Transaction](https://developer.android.com/reference/android/arch/persistence/room/Transaction)) which overrides a`DAO`method and runs it inside a transaction.
- Support SQLite Database:

  - API changes in database configuration.[b/65349673](https://issuetracker.google.com/issues/65349673)[b/65499876](https://issuetracker.google.com/issues/65499876)
- Paging:

  - Improved Paging documentation with more examples and thread annotations.

**Bug Fixes**

- Room:
  - Kotlin multi-line strings in`@Query`methods are handled properly.[b/65809374](https://issuetracker.google.com/issues/65809374)
- Paging:
  - Paging artifact does not depend on junit anymore.[b/65690261](https://issuetracker.google.com/issues/65690261)

## 1.0.0 Alpha 9-1 - September 13, 2017

This is a major release where core lifecycle artifacts (runtime, common) and arch core (common) reach to stable version`1.0.0`.

Along with this change, Support Library 26.1.0 now depends on these libraries. Both[AppCompatActivity](https://developer.android.com/reference/android/support/v7/app/AppCompatActivity)and[Support Fragment](https://developer.android.com/reference/android/support/v4/app/Fragment)now implement the[LifecycleOwner](https://developer.android.com/reference/android/arch/lifecycle/LifecycleOwner)interface.

This release also depends on Support Library`26.1.0`to take advantage of the new integration.

**New Library: Paging**

This release also includes a new library called[Paging](https://developer.android.com/jetpack/androidx/releases/archive/paging), which allows easily loading large data sets into a RecyclerView in chunks when necessary.[Paging](https://developer.android.com/jetpack/androidx/releases/archive/paging)is released as`alpha1`and will have its own release cycle.

**API Changes**

- The following classes are deprecated and will be removed in a future release:
  - [LifecycleRegistryOwner](https://developer.android.com/reference/android/arch/lifecycle/LifecycleRegistryOwner)
  - [LifecycleActivity](https://developer.android.com/reference/android/arch/lifecycle/LifecycleActivity)
  - [LifecycleFragment](https://developer.android.com/reference/android/arch/lifecycle/LifecycleFragment)

**Bug Fixes**

- Generated classes are now annotated with`@Generated`if the app has the annotation in the classpath.[b/35754819](https://issuetracker.google.com/issues/35754819)

- Fixed MediatorLiveData's observer comparison bug.[b/64413274](https://issuetracker.google.com/issues/64413274)

- SQLite`WITH`queries are now supported with \[LiveData\]. \[ref-LiveData\][b/62510164](https://issuetracker.google.com/issues/62510164)

- Fixed a bug where InvalidationTracker would not send the right list if more than 1 table is observed.[b/65099281](https://issuetracker.google.com/issues/65099281)

- Fixed a bug where Room would generate different files on Windows.[b/64470691](https://issuetracker.google.com/issues/64470691)

- LifecycleObservers in root package are now supported.[b/62310817](https://issuetracker.google.com/issues/62310817)

## 1.0.0 Alpha 9 - August 16, 2017

**Bug fixes**

- Fixed a bug in[LiveData](https://developer.android.com/reference/android/arch/lifecycle/LiveData), that second[Observer](https://developer.android.com/reference/android/arch/lifecycle/Observer)was ignored when first one was removed from its`onChanged`method.[b/64285805](https://issuetracker.google.com/issues/64285805)

## 1.0.0 Alpha 8 - August 1, 2017

**Behavior Changes**

- `NOT NULL`constraint is added for columns of primitive types or columns annotated with[NonNull](https://developer.android.com/reference/android/support/annotation/NonNull). This changes the structure of your tables, so if you're already using Architecture Components alpha 7 or earlier, you need to implement a migration if you want to keep the data, or use the`fallbackToDestructiveMigration()`method in the builder.[b/62007004](https://issuetracker.google.com/issues/62007004)

**API Changes**

- [SupportSQLiteProgram](https://developer.android.com/reference/android/arch/persistence/db/SupportSQLiteProgram)now extends[AutoCloseable](https://developer.android.com/reference/java/lang/AutoCloseable).[b/63131997](https://issuetracker.google.com/issues/63131997)

## 1.0.0 Alpha 7 - July 26, 2017

**Bug fixes**

- Fixed**critical** bug in[LifecycleRegistry](https://developer.android.com/reference/android/arch/lifecycle/LifecycleRegistry)`removeObserver`method, which broke a[LifecycleObserver](https://developer.android.com/reference/android/arch/lifecycle/LifecycleObserver)readdition.

- Fixed InvalidationTracker for custom databases[b/63162311](https://issuetracker.google.com/issues/63162311)

## 1.0.0 Alpha 6 - July 25, 2017

**Behavior changes**

- The order of[LifecycleObserver](https://developer.android.com/reference/android/arch/lifecycle/LifecycleObserver)calls was changed. Previously observers were always called in the order of their addition: if`observer1`is added before`observer2`, it will receive`ON_CREATE`and all other events before`observer2`. This is no longer true for destruction events, for them observers are called in the reverse order of addition. So current behavior is: if`observer1`is added before`observer2`, then`ON_CREATE`is sent first to`observer1`, then to`observer2`(same happens for`ON_START`and`ON_RESUME`), but`ON_PAUSE`event is sent first to`observer2`and only then to`observer1`(same for`ON_STOP`and`ON_DESTROY`).

- Room throws an exception if migration is missing. Previously Room would just clear the database, but now it crashes. Developers can opt-in to the clearing behavior by calling the builder API.[b/63872392](https://issuetracker.google.com/issues/63872392)

**API Changes**

- Added`fallbackToDestructiveMigration()`method to[`RoomDatabase.Builder`](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase.Builder)to clear the database if migration is missing.[b/63872392](https://issuetracker.google.com/issues/63872392)

- Architecture components now depend on support library 26.0.0

**Bug fixes**

- Fixed handling[@Relation](https://developer.android.com/reference/android/arch/persistence/room/Relation)nested into[@Embedded](https://developer.android.com/reference/android/arch/persistence/room/Embedded).[b/63736065](https://issuetracker.google.com/issues/63736065)

- Fixed testing migrations for tables with autoincremented primary key.[b/63393618](https://issuetracker.google.com/issues/63393618)

- Now[@Queries](https://developer.android.com/reference/android/arch/persistence/room/Query)that run DELETE or UPDATE queries correctly receive arguments.[b/63872538](https://issuetracker.google.com/issues/63872538)

- Now[ViewModels](https://developer.android.com/reference/android/arch/lifecycle/ViewModel)are retained, when owner fragment is in the backstack and configuration change happens twice.[b/38445801](https://issuetracker.google.com/issues/38445801)

## 1.0.0 Alpha 5 - July 18, 2017

**API Changes**

- Added a new callback method to[`RoomDatabase.Builder`](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase.Builder)to observe when a database is created or opened.[b/62699324](https://issuetracker.google.com/issues/62699324)

- [@Query](https://developer.android.com/reference/android/arch/persistence/room/Query)now may return RxJava[`Maybe`](http://reactivex.io/RxJava/javadoc/io/reactivex/Maybe.html)or[`Single`](http://reactivex.io/RxJava/javadoc/io/reactivex/Single.html).[b/62231019](https://issuetracker.google.com/issues/62231019)

You need to depend on`android.arch.persistence.room:rxjava2`artifact to add RxJava support to Room.

**Bug fixes**

- Fixed`@Delete`queries without any parameters.[b/63608092](https://issuetracker.google.com/issues/63608092)

- Fixed Room type checks for getters and setters.[b/63733651](https://issuetracker.google.com/issues/63733651)

## 1.0.0 Alpha 4 - July 11, 2017

**API Changes**

- Added a new convenience method (`runInTransaction()`) to[RoomDatabase](https://developer.android.com/reference/android/arch/persistence/room/RoomDatabase).

- `@Insert`,`@Delete`and`@Update`methods can now have parameters from different entity types.[b/62682405](https://issuetracker.google.com/issues/62682405)

**Bug Fixes**

- Fixed`byte[]`handling in`@Dao`methods.[b/62460045](https://issuetracker.google.com/issues/62460045)

- Migration check in Room now uses case-insensitive comparison.[b/62875382](https://issuetracker.google.com/issues/62875382)

- Fixed the proguard configuration for the Lifecycles artifact.[b/62113696](https://issuetracker.google.com/issues/62113696)

## 1.0.0 Alpha 3 - June 15, 2017

**API Changes**

- [`@OnLifecycleEvent`](https://developer.android.com/reference/android/arch/lifecycle/OnLifecycleEvent)supports only 1 event parameter now. This is a change in preparation for Java 8 support so that we can migrate to interfaces with default methods in the future. In relation to this change, only the`@OnLifecycleEvent(ON_ANY)`annotated methods can receive a second parameter of type`Event`(first parameter is the`LifecycleOwner`). See[Lifecycle](https://developer.android.com/reference/android/arch/lifecycle/Lifecycle)docs for details.

- [`LifecycleActivity`](https://developer.android.com/reference/android/arch/lifecycle/LifecycleActivity)and[`LifecycleFragment`](https://developer.android.com/reference/android/arch/lifecycle/LifecycleFragment)classes are moved into the`android.arch.lifecycle:extensions`artifact.

- [MigrationTestHelper](https://developer.android.com/reference/android/arch/persistence/room/testing/MigrationTestHelper)receives the[Instrumentation](https://developer.android.com/reference/android/app/Instrumentation)instance instead of the[`Context`](https://developer.android.com/reference/android/content/Context)to be able to read the schema from the test assets and create the database in the application context.

- [`@Insert`](https://developer.android.com/reference/android/arch/persistence/room/Insert),[`@Delete`](https://developer.android.com/reference/android/arch/persistence/room/Delete)and[`@Update`](https://developer.android.com/reference/android/arch/persistence/room/Update)annotations in`@DAO`methods can now have[`Iterable`](https://developer.android.com/reference/java/lang/Iterable)as the parameter type.[b/62259820](https://issuetracker.google.com/issues/62259820)

**Bug Fixes**

- Overridden methods with lifecycle events are not called multiple times anymore.

- Multiple`IN`parameters are now handled properly.[b/62608681](https://issuetracker.google.com/issues/62608681)

- Abstract DAO classes can now have a constructor that receives the`@Database`instance.[b/38488747](https://issuetracker.google.com/issues/38488747)

- `DAO`'s can now have a super class/interface with type parameters.[b/62103620](https://issuetracker.google.com/issues/62103620)

## 1.0.0 Alpha 2 - June 2, 2017

**API Changes**

- [InvalidationTracker](https://developer.android.com/reference/android/arch/persistence/room/InvalidationTracker)callback now receives the list of changed table names. ([b/38468740](https://issuetracker.google.com/issues/38468740))

- Reduced the API surface of the[SupportSQLiteDatabase](https://developer.android.com/reference/android/arch/persistence/db/SupportSQLiteDatabase)class. ([b/38481640](https://issuetracker.google.com/issues/38481640))

**Bug Fixes**

- Proguard files for lifecycles. ([b/62113696](https://issuetracker.google.com/issues/62113696))
- Loss of data with Type Converters. ([b/62100716](https://issuetracker.google.com/issues/62100716))
- Allow returning`Long[]`from`@Insert`queries.

## 1.0.0 Alpha 1 - May 17, 2017

**MinSDK:**14

### General advisories

- While we did a lot of testing prior to launch,[Architecture Components](https://developer.android.com/jetpack/androidx/releases/archive)are currently in alpha. If you're building a production app, be aware that the API will change before the 1.0 release and might not be fully robust. If you're not comfortable debugging problems in libraries you use, we recommend trying Architecture Components in side projects first.

- We're not recommending that everyone migrate today. We'll have a migration guide ready for the 1.0 release of architecture components.

### Known limitations and issues

- [Lifecycle](https://developer.android.com/jetpack/androidx/releases/archive/lifecycle)[Fragment](https://developer.android.com/reference/android/support/v4/app/Fragment)and[ActivityCompat](https://developer.android.com/reference/android/support/v4/app/ActivityCompat)in the[Support Library](https://developer.android.com/topic/libraries/support-library)do not yet implement[`LifecycleOwner`](https://developer.android.com/reference/android/arch/lifecycle/LifecycleOwner)interface. They will when Architecture Components reaches 1.0.0 version.