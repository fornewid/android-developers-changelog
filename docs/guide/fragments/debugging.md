---
title: https://developer.android.com/guide/fragments/debugging
url: https://developer.android.com/guide/fragments/debugging
source: md.txt
---

# Debug your fragments

This guide covers tools that you can use to debug your[fragments](https://developer.android.com/guide/fragments).

## FragmentManager logging

[`FragmentManager`](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)can emit various messages to[Logcat](https://developer.android.com/studio/debug/am-logcat). This is disabled by default, but sometimes these log messages can help you troubleshoot issues with your fragments.`FragmentManager`emits the most meaningful output at the`DEBUG`and`VERBOSE`[log levels](https://developer.android.com/studio/debug/logcat#read-logs).

You can enable logging using the following[`adb shell`](https://developer.android.com/studio/command-line/adb#shellcommands)command:  

```
adb shell setprop log.tag.FragmentManager DEBUG
```

Alternatively, you can enable verbose logging as follows:  

```
adb shell setprop log.tag.FragmentManager VERBOSE
```

If you enable verbose logging, you can then apply a[log level filter](https://developer.android.com/studio/debug/logcat#key-value-search)in the Logcat window. However, this filters all logs, not just the`FragmentManager`logs. It's usually best to enable`FragmentManager`logging only at the log level that you need.

### DEBUG logging

At the`DEBUG`level,`FragmentManager`generally emits log messages relating to lifecycle state changes. Each log entry contains the[`toString()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#toString())dump from the[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment). A log entry consists of the following information:

- The simple class name of the`Fragment`instance.
- The[identity hash code](https://developer.android.com/reference/java/lang/System#identityHashCode(java.lang.Object))of the`Fragment`instance.
- The fragment manager's unique ID of the`Fragment`instance. This is stable across configuration changes and process death and recreation.
- The ID of the container that the`Fragment`is added to, but only if set.
- The`Fragment`tag, but only if set.

The following is a sample`DEBUG`log entry:  

```
D/FragmentManager: moveto ATTACHED: NavHostFragment{92d8f1d} (fd92599e-c349-4660-b2d6-0ece9ec72f7b id=0x7f080116)
```

- The`Fragment`class is`NavHostFragment`.
- The identity hash code is`92d8f1d`.
- The unique ID is`fd92599e-c349-4660-b2d6-0ece9ec72f7b`.
- The container ID is`0x7f080116`.
- The tag is omitted because none was set. When present, it follows the ID in the format`tag=tag_value`.

For brevity and readability, the UUIDs are shortened in the following examples.

Here is a`NavHostFragment`being initialized and then the`startDestination``Fragment`of type`FirstFragment`being created and transitioning through to the`RESUMED`state:  

```
D/FragmentManager: moveto ATTACHED: NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager:   mName=null mIndex=-1 mCommitted=false
D/FragmentManager:   Operations:
D/FragmentManager:     Op #0: SET_PRIMARY_NAV NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager: moveto CREATED: NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager:   mName=null mIndex=-1 mCommitted=false
D/FragmentManager:   Operations:
D/FragmentManager:     Op #0: REPLACE FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager:     Op #1: SET_PRIMARY_NAV FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto ATTACHED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto CREATED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto CREATE_VIEW: NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager: moveto CREATE_VIEW: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto ACTIVITY_CREATED: NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager: moveto RESTORE_VIEW_STATE: NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager: moveto ACTIVITY_CREATED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto RESTORE_VIEW_STATE: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto STARTED: NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager: moveto STARTED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto RESUMED: NavHostFragment{92d8f1d} (<UUID> id=0x7f080116)
D/FragmentManager: moveto RESUMED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
```

Following a user interaction,`FirstFragment`transitions out of the various lifecycle states. Then`SecondFragment`is instantiated and transitions through to the`RESUMED`state:  

```
D/FragmentManager:   mName=07c8a5e8-54a3-4e21-b2cc-c8efc37c4cf5 mIndex=-1 mCommitted=false
D/FragmentManager:   Operations:
D/FragmentManager:     Op #0: REPLACE SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager:     Op #1: SET_PRIMARY_NAV SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager: movefrom RESUMED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: movefrom STARTED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: movefrom ACTIVITY_CREATED: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto ATTACHED: SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager: moveto CREATED: SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager: moveto CREATE_VIEW: SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager: moveto ACTIVITY_CREATED: SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager: moveto RESTORE_VIEW_STATE: SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager: moveto STARTED: SecondFragment{84132db} (<UUID> id=0x7f080116)
D/FragmentManager: movefrom CREATE_VIEW: FirstFragment{ccd2189} (<UUID> id=0x7f080116)
D/FragmentManager: moveto RESUMED: SecondFragment{84132db} (<UUID> id=0x7f080116)
```

All the`Fragment`instances are suffixed by an identifier so that you can track different instances of the same`Fragment`class.

### VERBOSE logging

At`VERBOSE`level,`FragmentManager`generally emits log messages about its internal state:  

```
V/FragmentManager: Run: BackStackEntry{f9d3ff3}
V/FragmentManager: add: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: Added fragment to active set NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
D/FragmentManager: moveto ATTACHED: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: Commit: BackStackEntry{5cfd2ae}
D/FragmentManager:   mName=null mIndex=-1 mCommitted=false
D/FragmentManager:   Operations:
D/FragmentManager:     Op #0: SET_PRIMARY_NAV NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
D/FragmentManager: moveto CREATED: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: Commit: BackStackEntry{e93833f}
D/FragmentManager:   mName=null mIndex=-1 mCommitted=false
D/FragmentManager:   Operations:
D/FragmentManager:     Op #0: REPLACE FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager:     Op #1: SET_PRIMARY_NAV FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: Run: BackStackEntry{e93833f}
V/FragmentManager: add: FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: Added fragment to active set FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager: moveto ATTACHED: FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager: moveto CREATED: FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 1 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
D/FragmentManager: moveto CREATE_VIEW: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 2 for FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager: moveto CREATE_VIEW: FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 2 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 2 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
D/FragmentManager: moveto ACTIVITY_CREATED: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
D/FragmentManager: moveto RESTORE_VIEW_STATE: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager: moveto ACTIVITY_CREATED: FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager: moveto RESTORE_VIEW_STATE: FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: SpecialEffectsController: Enqueuing add operation for fragment FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: SpecialEffectsController: For fragment FirstFragment{886440c} (<UUID> id=0x7f080130) mFinalState = VISIBLE -> VISIBLE.
V/FragmentManager: SpecialEffectsController: Container androidx.fragment.app.FragmentContainerView{7578ffa V.E...... ......I. 0,0-0,0 #7f080130 app:id/nav_host_fragment_content_fragment} is not attached to window. Cancelling pending operation Operation {382a9ab} {mFinalState = VISIBLE} {mLifecycleImpact = ADDING} {mFragment = FirstFragment{886440c} (<UUID> id=0x7f080130)}
V/FragmentManager: SpecialEffectsController: Operation {382a9ab} {mFinalState = VISIBLE} {mLifecycleImpact = ADDING} {mFragment = FirstFragment{886440c} (<UUID> id=0x7f080130)} has called complete.
V/FragmentManager: SpecialEffectsController: Setting view androidx.constraintlayout.widget.ConstraintLayout{3968808 I.E...... ......I. 0,0-0,0} to VISIBLE
V/FragmentManager: computeExpectedState() of 4 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: SpecialEffectsController: Enqueuing add operation for fragment NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: SpecialEffectsController: For fragment NavHostFragment{86274b0} (<UUID> id=0x7f080130) mFinalState = VISIBLE -> VISIBLE.
V/FragmentManager: SpecialEffectsController: Container androidx.fragment.app.FragmentContainerView{2ba8ba1 V.E...... ......I. 0,0-0,0 #7f080130 app:id/nav_host_fragment_content_fragment} is not attached to window. Cancelling pending operation Operation {f7eb1c6} {mFinalState = VISIBLE} {mLifecycleImpact = ADDING} {mFragment = NavHostFragment{86274b0} (<UUID> id=0x7f080130)}
V/FragmentManager: SpecialEffectsController: Operation {f7eb1c6} {mFinalState = VISIBLE} {mLifecycleImpact = ADDING} {mFragment = NavHostFragment{86274b0} (<UUID> id=0x7f080130)} has called complete.
V/FragmentManager: SpecialEffectsController: Setting view androidx.fragment.app.FragmentContainerView{7578ffa I.E...... ......I. 0,0-0,0 #7f080130 app:id/nav_host_fragment_content_fragment} to VISIBLE
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: Run: BackStackEntry{5cfd2ae}
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 4 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 5 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
D/FragmentManager: moveto STARTED: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 5 for FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager: moveto STARTED: FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 5 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 5 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 5 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 5 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
D/FragmentManager: moveto RESUMED: NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for FirstFragment{886440c} (<UUID> id=0x7f080130)
D/FragmentManager: moveto RESUMED: FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for FirstFragment{886440c} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
V/FragmentManager: computeExpectedState() of 7 for NavHostFragment{86274b0} (<UUID> id=0x7f080130)
```

This example only covers the loading on`FirstFragment`. Including the transition to`SecondFragment`increases the log entries considerably. Many of the`VERBOSE`level log messages are of little use to app developers. However, seeing when changes to the back stack occur can help in debugging some issues.

## StrictMode for fragments

Version 1.4.0 and higher of the[Jetpack Fragment](https://developer.android.com/jetpack/androidx/releases/fragment)library includes StrictMode for fragments. It can catch some common issues that may cause your app to behave in unexpected ways. For more information about working with`StrictMode`, see[StrictMode](https://developer.android.com/reference/android/os/StrictMode).

A custom[`Policy`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy)defines which violations are detected and specifies what penalty is applied when violations are detected.
| **Note:** when you enable[`FragmentManager``DEBUG`logging](https://developer.android.com/guide/fragments/debugging#debug-logging), all StrictMode violations are logged, no matter what policy you are using.

To apply a custom StrictMode policy, assign it to the[`FragmentManager`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager). Do this as early as possible. In this case, you do it in an`init`block or in the Java constructor:  

### Kotlin

```kotlin
class ExampleActivity : AppCompatActivity() {

    init {
        supportFragmentManager.strictModePolicy =
            FragmentStrictMode.Policy.Builder()
                .penaltyDeath()
                .detectFragmentReuse()
                .allowViolation(FirstFragment::class.java,
                                FragmentReuseViolation::class.java)
                .build()
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding = ActivityExampleBinding.inflate(layoutInflater)
        setContentView(binding.root)
        ...
   }
}
```

### Java

```java
class ExampleActivity extends AppCompatActivity() {

    ExampleActivity() {
        getSupportFragmentManager().setStrictModePolicy(
                new FragmentStrictMode.Policy.Builder()
                        .penaltyDeath()
                        .detectFragmentReuse()
                        .allowViolation(FirstFragment.class,
                                        FragmentReuseViolation.class)
                        .build()
        );
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)

        ActivityExampleBinding binding =
            ActivityExampleBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        ...
   }
}
```

For cases where you need to know the`Context`to determine whether to enable StrictMode, such as from the value of a boolean resource, you can defer assigning a StrictMode policy to the`FragmentManager`using an[`OnContextAvailableListener`](https://developer.android.com/reference/androidx/activity/contextaware/OnContextAvailableListener):  

### Kotlin

```kotlin
class ExampleActivity : AppCompatActivity() {

    init {
        addOnContextAvailableListener { context ->
            if(context.resources.getBoolean(R.bool.enable_strict_mode)) {
                supportFragmentManager.strictModePolicy = FragmentStrictMode.Policy.Builder()
                    .penaltyDeath()
                    .detectFragmentReuse()
                    .allowViolation(FirstFragment::class.java, FragmentReuseViolation::class.java)
                    .build()
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding = ActivityExampleBinding.inflate(layoutInflater)
        setContentView(binding.root)
        ...
   }
}
```

### Java

```java
class ExampleActivity extends AppCompatActivity() {

    ExampleActivity() {
        addOnContextAvailableListener((context) -> {
            if(context.getResources().getBoolean(R.bool.enable_strict_mode)) {
                getSupportFragmentManager().setStrictModePolicy(
                        new FragmentStrictMode.Policy.Builder()
                                .penaltyDeath()
                                .detectFragmentReuse()
                                .allowViolation(FirstFragment.class, FragmentReuseViolation.class)
                                .build()
                );
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)

        ActivityExampleBinding binding = ActivityExampleBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        ...
   }
}
```

The latest point at which you can configure StrictMode to catch all possible violations is in[`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)), before the call to`super.onCreate()`:  

### Kotlin

```kotlin
class ExampleActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        supportFragmentManager.strictModePolicy = FragmentStrictMode.Policy.Builder()
            .penaltyDeath()
            .detectFragmentReuse()
            .allowViolation(FirstFragment::class.java, FragmentReuseViolation::class.java)
            .build()

        super.onCreate(savedInstanceState)

        val binding = ActivityExampleBinding.inflate(layoutInflater)
        setContentView(binding.root)
        ...
   }
}
```

### Java

```java
class ExampleActivity extends AppCompatActivity() {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getSupportFragmentManager().setStrictModePolicy(
                new FragmentStrictMode.Policy.Builder()
                        .penaltyDeath()
                        .detectFragmentReuse()
                        .allowViolation(FirstFragment.class, FragmentReuseViolation.class)
                        .build()
                );

        super.onCreate(savedInstanceState)

        ActivityExampleBinding binding = ActivityExampleBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        ...
   }
}
```

This policy used in these examples detects only fragment reuse violations, and the app terminates whenever one occurs.`penaltyDeath()`can be helpful in debug builds because it fails quickly enough that you can't ignore violations.

It is also possible to selectively allow certain violations. The policy used in the preceding example, however, enforces this violation for all other fragment types. This is useful for cases where a third-party library component might contain StrictMode violations.

In such cases, you can temporarily add those violations to the allowlist of your StrictMode for components that you don't own until the library fixes their violation.

For details about how to configure other violations, see the documentation for[`FragmentStrictMode.Policy.Builder`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder).

There are three penalty types.

- [`penaltyLog()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#penaltylog)dumps details of violations to Logcat.
- [`penaltyDeath()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#penaltyDeath())terminates the app when violations are detected.
- [`penaltyListener()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#penaltylistener)lets you add a custom listener that is called whenever violations are detected.

You can apply any combination of penalties in your`Policy`. If your policy does not explicitly specify a penalty, a default of`penaltyLog()`is applied. If you apply a penalty other than`penaltyLog()`in your custom`Policy`, then`penaltyLog()`is disabled unless you explicitly set it.

`penaltyListener()`can be useful when you have a third-party logging library to which you want to log violations. Alternatively, you might want to enable non-fatal violation catching in release builds and log them to a crash reporting library. This strategy can detect violations otherwise missed.

To set a global StrictMode policy, set a default policy that applies to all[`FragmentManager`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager)instances using the[`FragmentStrictMode.setDefaultPolicy()`](https://developer.android.com/reference/androidx/fragment/app/strictmode/FragmentStrictMode#setDefaultPolicy(androidx.fragment.app.strictmode.FragmentStrictMode.Policy))method:  

### Kotlin

```kotlin
class MyApplication : Application() {

    override fun onCreate() {
        super.onCreate()

        FragmentStrictMode.defaultPolicy =
            FragmentStrictMode.Policy.Builder()
                .detectFragmentReuse()
                .detectFragmentTagUsage()
                .detectRetainInstanceUsage()
                .detectSetUserVisibleHint()
                .detectTargetFragmentUsage()
                .detectWrongFragmentContainer()
                .apply {
                    if (BuildConfig.DEBUG) {
                        // Fail early on DEBUG builds
                        penaltyDeath()
                    } else {
                        // Log to Crashlytics on RELEASE builds
                        penaltyListener {
                            FirebaseCrashlytics.getInstance().recordException(it)
                        }
                    }
                }
                .build()
    }
}
```

### Java

```java
public class MyApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();

        FragmentStrictMode.Policy.Builder builder = new FragmentStrictMode.Policy.Builder();
        builder.detectFragmentReuse()
                .detectFragmentTagUsage()
                .detectRetainInstanceUsage()
                .detectSetUserVisibleHint()
                .detectTargetFragmentUsage()
                .detectWrongFragmentContainer();
        if (BuildConfig.DEBUG) {
            // Fail early on DEBUG builds
            builder.penaltyDeath();
        } else {
            // Log to Crashlytics on RELEASE builds
            builder.penaltyListener((exception) ->
                    FirebaseCrashlytics.getInstance().recordException(exception)
            );
        }
        FragmentStrictMode.setDefaultPolicy(builder.build());
    }
}
```

The following sections describe types of violations and possible workarounds.

### Fragment reuse

The fragment reuse violation is enabled using[`detectFragmentReuse()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#detectFragmentReuse())and throws a[`FragmentReuseViolation`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentReuseViolation).

This violation indicates the reuse of a`Fragment`instance after its removal from`FragmentManager`. This reuse can cause issues because the`Fragment`might retain state from its previous use and not behave consistently. If you create a new instance each time, it is always in the initial state when added to`FragmentManager`.

### Fragment tag usage

The fragment tag usage violation is enabled using[`detectFragmentTagUsage()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#detectFragmentTagUsage())and throws a[`FragmentTagUsageViolation`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentTagUsageViolation).

This violation indicates that a`Fragment`is inflated using the`<fragment>`tag in an XML layout. To resolve this, inflate your`Fragment`inside`<androidx.fragment.app.FragmentContainerView>`rather than in the`<fragment>`tag. Fragments inflated using a`FragmentContainerView`can reliably handle`Fragment`transactions and configuration changes. These might not work as expected if you use the`<fragment>`tag instead.

### Retain instance usage

The retain instance usage violation is enabled using[`detectRetainInstanceUsage()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#detectRetainInstanceUsage())and throws a[`RetainInstanceUsageViolation`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/RetainInstanceUsageViolation).

This violation indicates the usage of a retained`Fragment`, specifically, if there are calls to[`setRetainInstance()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setRetainInstance(boolean))or[`getRetainInstance()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getRetainInstance()), which are both deprecated.

Instead of using these methods to manage retained`Fragment`instances yourself, store state in a[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)that handles this for you.

### Set user visible hint

The set user visible hint violation is enabled using[`detectSetUserVisibleHint()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#detectSetUserVisibleHint())and throws a[`SetUserVisibleHintViolation`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/SetUserVisibleHintViolation).

This violation indicates a call to[`setUserVisibleHint()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setuservisiblehint), which is deprecated.

If you are manually calling this method, then call[`setMaxLifecycle()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setMaxLifecycle(androidx.fragment.app.Fragment,%20androidx.lifecycle.Lifecycle.State))instead. If you override this method, move the behavior to[`onResume()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onResume())when passing in`true`and[`onPause()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onPause())when passing in`false`.

### Target fragment usage

The target fragment usage violation is enabled using[`detectTargetFragmentUsage()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#detectTargetFragmentUsage())and throws a[`TargetFragmentUsageViolation`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/TargetFragmentUsageViolation).

This violation indicates a call to[`setTargetFragment()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setTargetFragment(androidx.fragment.app.Fragment,int)),[`getTargetFragment()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTargetFragment()), or[`getTargetRequestCode()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTargetRequestCode()), which are all deprecated. Instead of using these methods, register a`FragmentResultListener`. For more information about passing results, see[Pass results between fragments](https://developer.android.com/guide/fragments/communicate#pass-between-fragments).

### Wrong fragment container

The wrong fragment container violation is enabled using[`detectWrongFragmentContainer()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/FragmentStrictMode.Policy.Builder#detectWrongFragmentContainer())and throws a[`WrongFragmentContainerViolation`](https://developer.android.com/reference/kotlin/androidx/fragment/app/strictmode/WrongFragmentContainerViolation).

This violation indicates the addition of a`Fragment`to a container other than`FragmentContainerView`. As with[`Fragment`tag usage](https://developer.android.com/guide/fragments/debugging#fragment-tag-usage), fragment transactions might not work as expected unless hosted inside a`FragmentContainerView`. Using a container view also helps address an issue in the`View`API that causes fragments using exit animations to be drawn on top of all other fragments.