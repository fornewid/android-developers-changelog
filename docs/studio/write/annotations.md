---
title: https://developer.android.com/studio/write/annotations
url: https://developer.android.com/studio/write/annotations
source: md.txt
---

Using code inspections tools, such as [lint](https://developer.android.com/studio/write/lint), can help you find
problems and improve your code, but inspection tools can only infer so much. Android resource IDs,
for example, use an `int` to identify strings, graphics, colors, and other resource types,
so inspection tools can't tell when you have specified a string resource where you should have
specified a color. This situation means that your app may render incorrectly or fail to run at all,
even if you use code inspection.

Annotations let you provide hints to code inspections tools, such as lint, to help detect these
more subtle code problems. Annotations are added as metadata tags that you attach to variables,
parameters, and return values to inspect method return values, passed parameters, local variables,
and fields. When used with code inspection tools, annotations can help you detect problems such as
null pointer exceptions and resource type conflicts.

Android supports a variety of annotations through the
[Jetpack Annotations Library](https://developer.android.com/jetpack/androidx/releases/annotation).
You can access the library through the
`https://developer.android.com/reference/androidx/annotation/package-summary`
package.

**Note:** If a module has a dependency on an annotation processor,
you must use either the `kapt` or `ksp` dependency configuration for Kotlin
or the `annotationProcessor` dependency configuration for Java to add that
dependency.

## Add annotations to your project

To enable annotations in your project, add the `androidx.annotation:annotation`
dependency to your library or app. Any annotations you add are checked when you run a code
inspection or `lint` task.

### Add the Jetpack Annotations library dependency

The Jetpack Annotations library is published on
[Google's Maven Repository](https://developer.android.com/studio/build/dependencies#google-maven).
To add the Jetpack Anotations library to your project, include the following
line in the `dependencies` block of your `build.gradle` or
`build.gradle.kts` file:

### Kotlin

```kotlin
dependencies {
    implementation("androidx.annotation:annotation:1.9.1")
}
```

### Groovy

```groovy
dependencies {
    implementation 'androidx.annotation:annotation:1.9.1'
}
```
Then, in the toolbar or sync notification that appears, click **Sync Now** .

<br />

If you use annotations in your own library module, the annotations are included as part of the
Android Archive (AAR) artifact in XML format in the `annotations.zip` file. Adding the
`androidx.annotation` dependency doesn't introduce a dependency for any downstream users
of your library.

**Note:** If you're using other Jetpack libraries,
you might not need to add the `androidx.annotation` dependency. Because many other
Jetpack libraries depend on the Annotations Library, you might already have access to the
annotations.

For a complete list of annotations included in the Jetpack repository, either see the
[Jetpack Annotations library
reference](https://developer.android.com/reference/androidx/annotation/package-summary) or use the autocomplete feature to display the available options for the
`import androidx.annotation.` statement.

### Run code inspections

To start a code inspection from Android Studio, which includes validating annotations and
automatic lint checking, select **Analyze** **\> Inspect Code** from the
menu. Android Studio displays conflict messages to flag potential problems where your code
conflicts with annotations and to suggest possible resolutions.

You can also enforce annotations by [running the
`lint` task using the command line](https://developer.android.com/studio/write/lint#commandline). Although this might be useful for flagging problems
with a continuous integration server, the `lint` task doesn't enforce nullness
annotations (described in the following section); only Android Studio does this. For more
information on enabling and running lint
inspections, see [Improving your code with lint
checks](https://developer.android.com/tools/debugging/improving-w-lint).

Although annotation conflicts generate warnings, these warnings don't prevent your app
from compiling.

## Nullness annotations

Nullness annotations can be useful in Java code to enforce whether values can be null. They are less useful in Kotlin code, as Kotlin has built in nullability rules that are enforced at compile time.

Add `https://developer.android.com/reference/androidx/annotation/Nullable` and
`https://developer.android.com/reference/androidx/annotation/NonNull` annotations
to check the nullness of a given variable, parameter, or return value. The `@Nullable`
annotation indicates a variable, parameter, or return value that can be null.
`@NonNull` indicates a variable, parameter, or return value that can't be null.

For example, if a local variable that contains a null value is passed as a parameter to a method
with the `@NonNull` annotation attached to that parameter, building the code generates a
warning indicating a non-null conflict. Also, attempting to reference the result of a
method marked by `@Nullable` without first checking whether the result is null generates
a nullness warning. Only use `@Nullable` on a method's return value
if every use of the method must be explicitly null-checked.

The following example demonstrates nullability in action. The Kotlin example code doesn't leverage
the `@NonNull` annotation because it's automatically added to the generated bytecode
when a non-nullable type is specified. The Java example leverages the `@NonNull` annotation
on the `context` and `attrs` parameters to check that the passed parameter values
aren't null. It also checks that the `onCreateView()` method itself doesn't return null:

### Kotlin

```kotlin
...
    /** Annotation not used because of the safe-call operator(?)**/
    override fun onCreateView(
            name: String?,
            context: Context,
            attrs: AttributeSet
    ): View? {
        ...
    }
...
```

### Java

```java
import androidx.annotation.NonNull;
...
    /** Add support for inflating the <fragment> tag. **/
    @NonNull
    @Override
    public View onCreateView(String name, @NonNull Context context,
      @NonNull AttributeSet attrs) {
      ...
      }
...
```

### Nullability analysis


Android Studio supports running a nullability analysis to automatically infer
and insert nullness annotations in your code. A nullability analysis scans
the contracts throughout the method hierarchies in your code to detect:

- Calling methods that can return null.
- Methods that should not return null.
- Variables, such as fields, local variables, and parameters, that can be null.
- Variables, such as fields, local variables, and parameters, that can't hold a null value.


The analysis then automatically inserts the appropriate null annotations in
the detected locations.

To run a nullability analysis in Android Studio, select **Analyze** \>
**Infer Nullity** . Android Studio inserts the Android `https://developer.android.com/reference/androidx/annotation/Nullable` and `https://developer.android.com/reference/androidx/annotation/NonNull` annotations in
detected locations in your code. After running a null analysis, it's a good practice to verify the
injected annotations.


**Note:** When adding nullness annotations, autocomplete may
suggest the IntelliJ [`@Nullable` and
`@NotNull`](https://www.jetbrains.com/help/idea/2025.3/nullable-and-notnull-annotations.html) annotations instead of the Android null annotations
and may auto-import the corresponding library. However, the Android Studio
lint checker only looks for the Android null annotations. When verifying your
annotations, confirm that your project uses the Android null annotations so the
lint checker can properly notify you during code inspection.

## Resource annotations

Validating resource types can be useful because Android references to resources, such as [drawable](https://developer.android.com/guide/topics/resources/drawable-resource) and [string](https://developer.android.com/guide/topics/resources/string-resource) resources, are passed as integers.

Code that expects a parameter to reference a specific type of resource, such as a `String`,
can be passed to the expected reference type of `int`, but actually reference a different
type of resource, such as an `R.string` resource.

For example, add `https://developer.android.com/reference/androidx/annotation/StringRes` annotations to
check whether a resource parameter contains an `R.string` reference, as shown here:

### Kotlin

```kotlin
abstract fun setTitle(@StringRes resId: Int)
```

### Java

```java
public abstract void setTitle(@StringRes int resId)
```

During code inspection, the annotation generates a warning if an `R.string` reference
isn't passed in the parameter.

Annotations for other resource types, such as `https://developer.android.com/reference/androidx/annotation/DrawableRes`, `https://developer.android.com/reference/androidx/annotation/DimenRes`, `https://developer.android.com/reference/androidx/annotation/ColorRes`, and `https://developer.android.com/reference/androidx/annotation/InterpolatorRes`, can be
added using the same annotation format and run during the code inspection.

If your parameter
supports multiple resource types, you can put more than one resource type annotation on a given
parameter. Use `https://developer.android.com/reference/androidx/annotation/AnyRes`
to indicate that the annotated parameter can be any type of `R` resource.

Although you can use `@ColorRes` to specify that a
parameter should be a color resource, a color integer (in the `RRGGBB` or
`AARRGGBB` format) isn't recognized as a color resource. Instead, use the `https://developer.android.com/reference/androidx/annotation/ColorInt` annotation to
indicate that a parameter must be a color integer. The build tools will flag incorrect code that
passes a color resource ID such as `android.R.color.black`, rather than a color integer,
to annotated methods.

## Thread annotations

Thread annotations check whether a method is called from a specific type of
[thread](https://developer.android.com/guide/components/processes-and-threads). The following thread
annotations are supported:

- `https://developer.android.com/reference/androidx/annotation/MainThread`
- `https://developer.android.com/reference/androidx/annotation/UiThread`
- `https://developer.android.com/reference/androidx/annotation/WorkerThread`
- `https://developer.android.com/reference/androidx/annotation/BinderThread`
- `https://developer.android.com/reference/androidx/annotation/AnyThread`

The build tools treat the `@MainThread` and
`@UiThread` annotations as interchangeable, so you can call `@UiThread`
methods from `@MainThread` methods and vice versa. However, it's possible for a UI
thread to be different from the main thread, in the case of system apps with multiple views
on different threads. Therefore, you should annotate methods associated with an app's view hierarchy
with `@UiThread` and annotate only methods associated with an app's lifecycle with
`@MainThread`.

If all methods in a class share the same threading requirement, you can add a single thread
annotation to the class to verify that all methods in the class are called from the same type of
thread.

A common use of thread annotations is to validate that methods or classes annotated with
`@WorkerThread` are only called from an appropriate background thread.

## Value constraint annotations

Use the `https://developer.android.com/reference/androidx/annotation/IntRange`,
`https://developer.android.com/reference/androidx/annotation/FloatRange`, and
`https://developer.android.com/reference/androidx/annotation/Size` annotations to
validate the values of passed parameters. Both `@IntRange` and `@FloatRange`
are most useful when applied to parameters where users are likely to get the range wrong.

The `@IntRange` annotation validates that an integer or long parameter
value is within a specified range. The following example indicates that the `alpha`
parameter must contain an integer value from 0 to 255:

### Kotlin

```kotlin
fun setAlpha(@IntRange(from = 0, to = 255) alpha: Int) { ... }
```

### Java

```java
public void setAlpha(@IntRange(from=0,to=255) int alpha) { ... }
```

The `@FloatRange` annotation checks whether a float or double parameter
value is within a specified range of floating point values. The following example indicates that the
`alpha` parameter must contain a float value from 0.0 to 1.0:

### Kotlin

```kotlin
fun setAlpha(@FloatRange(from = 0.0, to = 1.0) alpha: Float) {...}
```

### Java

```java
public void setAlpha(@FloatRange(from=0.0, to=1.0) float alpha) {...}
```

The `@Size` annotation checks the size of a collection or
array or the length of a string. The `@Size` annotation can be used to verify
the following qualities:

- Minimum size, such as `@Size(min=2)`
- Maximum size, such as `@Size(max=2)`
- Exact size, such as `@Size(2)`
- A number that the size must be a multiple of, such as `@Size(multiple=2)`


For example, `@Size(min=1)`
checks whether a collection is not empty, and `@Size(3)`
validates that an array contains exactly three values.

The following example indicates that the
`location` array must contain at least one element:

### Kotlin

```kotlin
fun getLocation(button: View, @Size(min=1) location: IntArray) {
    button.getLocationOnScreen(location)
}
```

### Java

```java
void getLocation(View button, @Size(min=1) int[] location) {
    button.getLocationOnScreen(location);
}
```

## Permission annotations

Use the `https://developer.android.com/reference/androidx/annotation/RequiresPermission`
annotation to validate the permissions of the caller of a method. To check for a single permission
from a list of valid permissions, use the `anyOf` attribute. To check for a set of
permissions, use the `allOf` attribute. The following example annotates the
`setWallpaper()` method to indicate that the caller of the method must have the
`permission.SET_WALLPAPERS` permission:

### Kotlin

```kotlin
@RequiresPermission(Manifest.permission.SET_WALLPAPER)
@Throws(IOException::class)
abstract fun setWallpaper(bitmap: Bitmap)
```

### Java

```java
@RequiresPermission(Manifest.permission.SET_WALLPAPER)
public abstract void setWallpaper(Bitmap bitmap) throws IOException;
```

The following example requires the caller of the `copyImageFile()` method
to have both read access to external storage and read access to location
metadata in the copied image:

### Kotlin

```kotlin
@RequiresPermission(allOf = [
    Manifest.permission.READ_EXTERNAL_STORAGE,
    Manifest.permission.ACCESS_MEDIA_LOCATION
])
fun copyImageFile(dest: String, source: String) {
    ...
}
```

### Java

```java
@RequiresPermission(allOf = {
    Manifest.permission.READ_EXTERNAL_STORAGE,
    Manifest.permission.ACCESS_MEDIA_LOCATION})
public static final void copyImageFile(String dest, String source) {
    //...
}
```

For permissions on intents, place the permission requirement on the string field that defines the
intent action name:

### Kotlin

```kotlin
@RequiresPermission(android.Manifest.permission.BLUETOOTH)
const val ACTION_REQUEST_DISCOVERABLE = "android.bluetooth.adapter.action.REQUEST_DISCOVERABLE"
```

### Java

```java
@RequiresPermission(android.Manifest.permission.BLUETOOTH)
public static final String ACTION_REQUEST_DISCOVERABLE =
            "android.bluetooth.adapter.action.REQUEST_DISCOVERABLE";
```

For permissions on content providers that need separate permissions for read and write
access, wrap each permission requirement in an `https://developer.android.com/reference/androidx/annotation/RequiresPermission.Read`
or `https://developer.android.com/reference/androidx/annotation/RequiresPermission.Write`
annotation:

### Kotlin

```kotlin
@RequiresPermission.Read(RequiresPermission(READ_HISTORY_BOOKMARKS))
@RequiresPermission.Write(RequiresPermission(WRITE_HISTORY_BOOKMARKS))
val BOOKMARKS_URI = Uri.parse("content://browser/bookmarks")
```

### Java

```java
@RequiresPermission.Read(@RequiresPermission(READ_HISTORY_BOOKMARKS))
@RequiresPermission.Write(@RequiresPermission(WRITE_HISTORY_BOOKMARKS))
public static final Uri BOOKMARKS_URI = Uri.parse("content://browser/bookmarks");
```

### Indirect permissions

When a permission depends on the specific value supplied to a method's parameter, use
`@RequiresPermission` on the parameter itself without listing the specific permissions.
For example, the `https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)`
method uses an indirect permission on the intent passed to the method:

### Kotlin

```kotlin
abstract fun startActivity(@RequiresPermission intent: Intent, bundle: Bundle?)
```

### Java

```java
public abstract void startActivity(@RequiresPermission Intent intent, @Nullable Bundle)
```

When you use indirect permissions, the build tools perform data flow analysis to check whether the
argument passed into the method has any `@RequiresPermission` annotations. They then
enforce any existing annotations from the parameter on the method itself. In the
`startActivity(Intent)` example, annotations in the `https://developer.android.com/reference/android/content/Intent` class cause the resulting warnings
on invalid uses of `startActivity(Intent)` when an intent without the appropriate
permissions is passed to the method, as shown in figure 1.
![](https://developer.android.com/static/studio/images/write/indirect-permissions-warning_2-2_2x.png)

**Figure 1.** The warning generated from an indirect
permissions annotation on the `startActivity(Intent)` method.

The build tools generate the warning on `startActivity(Intent)` from the annotation
on the corresponding intent action name in the `Intent` class:

### Kotlin

```kotlin
@RequiresPermission(Manifest.permission.CALL_PHONE)
const val ACTION_CALL = "android.intent.action.CALL"
```

### Java

```java
@RequiresPermission(Manifest.permission.CALL_PHONE)
public static final String ACTION_CALL = "android.intent.action.CALL";
```

If necessary, you can substitute `@RequiresPermission` for
`@RequiresPermission.Read` or `@RequiresPermission.Write` when annotating
a method's parameter. However, for indirect permissions `@RequiresPermission` should
not be used in conjunction with either the read or the write permissions annotations.

## Return value annotations

Use the `https://developer.android.com/reference/androidx/annotation/CheckResult` annotation to
validate that a method's result or return value is actually used. Instead of annotating every
non-void method with `@CheckResult`, add the annotation to clarify the results of
potentially confusing methods.

For example, new Java developers often mistakenly think that
`<String>.trim()` removes whitespace from the original string. Annotating
the method with `@CheckResult` flags uses of `<String>.trim()`
where the caller doesn't do anything with the method's return value.

The following example annotates the `https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission(java.lang.String,%20java.lang.String)`
method to check whether the return value of the method is
actually referenced. It also names the `https://developer.android.com/reference/android/content/ContextWrapper#enforcePermission(java.lang.String,%20int,%20int,%20java.lang.String)`
method as a method to be suggested to the developer as a replacement:

### Kotlin

```kotlin
@CheckResult(suggest = "#enforcePermission(String,int,int,String)")
abstract fun checkPermission(permission: String, pid: Int, uid: Int): Int
```

### Java

```java
@CheckResult(suggest="#enforcePermission(String,int,int,String)")
public abstract int checkPermission(@NonNull String permission, int pid, int uid);
```

## CallSuper annotations

Use the `https://developer.android.com/reference/androidx/annotation/CallSuper` annotation to
validate that an overriding method calls the super implementation of the method.

The following
example annotates the `onCreate()` method to ensure that any overriding method
implementations call `super.onCreate()`:

### Kotlin

```kotlin
@CallSuper
override fun onCreate(savedInstanceState: Bundle?) {
}
```

### Java

```java
@CallSuper
protected void onCreate(Bundle savedInstanceState) {
}
```

## Typedef annotations

Typedef annotations check whether a particular parameter, return value,
or field references a specific set of constants. They also enable code completion to automatically
offer the allowed constants.

Use the `https://developer.android.com/reference/androidx/annotation/IntDef` and
`https://developer.android.com/reference/androidx/annotation/StringDef`
annotations to create enumerated annotations of integer and string sets to validate other
types of code references.

Typedef annotations use `@interface` to declare the new enumerated annotation type.
The `@IntDef` and `@StringDef` annotations, along with
`@Retention`, annotate the new annotation and are necessary to define the
enumerated type. The `@Retention(RetentionPolicy.SOURCE)` annotation tells the compiler
not to store the enumerated annotation data in the `.class` file.

The following example shows the steps to create an annotation that checks whether a value passed
as a method parameter references one of the defined constants:

### Kotlin

```kotlin
import androidx.annotation.IntDef
//...
// Define the list of accepted constants and declare the NavigationMode annotation.
@Retention(AnnotationRetention.SOURCE)
@IntDef(NAVIGATION_MODE_STANDARD, NAVIGATION_MODE_LIST, NAVIGATION_MODE_TABS)
annotation class NavigationMode

// Declare the constants.
const val NAVIGATION_MODE_STANDARD = 0
const val NAVIGATION_MODE_LIST = 1
const val NAVIGATION_MODE_TABS = 2

abstract class ActionBar {

    // Decorate the target methods with the annotation.
    // Attach the annotation.
    @get:NavigationMode
    @setparam:NavigationMode
    abstract var navigationMode: Int

}
```

### Java

```java
import androidx.annotation.IntDef;
//...
public abstract class ActionBar {
    //...
    // Define the list of accepted constants and declare the NavigationMode annotation.
    @Retention(RetentionPolicy.SOURCE)
    @IntDef({NAVIGATION_MODE_STANDARD, NAVIGATION_MODE_LIST, NAVIGATION_MODE_TABS})
    public @interface NavigationMode {}

    // Declare the constants.
    public static final int NAVIGATION_MODE_STANDARD = 0;
    public static final int NAVIGATION_MODE_LIST = 1;
    public static final int NAVIGATION_MODE_TABS = 2;

    // Decorate the target methods with the annotation.
    @NavigationMode
    public abstract int getNavigationMode();

    // Attach the annotation.
    public abstract void setNavigationMode(@NavigationMode int mode);
}
```

When you build this code, a warning is generated if the `mode` parameter doesn't
reference one of the defined constants (`NAVIGATION_MODE_STANDARD`,
`NAVIGATION_MODE_LIST`, or `NAVIGATION_MODE_TABS`).

Combine `@IntDef` and `@IntRange` to indicate that an
integer can be either a given set of constants or a value within a range.

### Enable combining constants with flags

If users can combine the allowed constants with a flag (such as `|`,
`&`, `^`, and so on), you can define an annotation with a
`flag` attribute to check whether a parameter or return value references a valid pattern.

The following example creates the `DisplayOptions` annotation with a list of valid
`DISPLAY_` constants:

### Kotlin

```kotlin
import androidx.annotation.IntDef
...

@IntDef(flag = true, value = [
    DISPLAY_USE_LOGO,
    DISPLAY_SHOW_HOME,
    DISPLAY_HOME_AS_UP,
    DISPLAY_SHOW_TITLE,
    DISPLAY_SHOW_CUSTOM
])
@Retention(AnnotationRetention.SOURCE)
annotation class DisplayOptions
...
```

### Java

```java
import androidx.annotation.IntDef;
...

@IntDef(flag=true, value={
        DISPLAY_USE_LOGO,
        DISPLAY_SHOW_HOME,
        DISPLAY_HOME_AS_UP,
        DISPLAY_SHOW_TITLE,
        DISPLAY_SHOW_CUSTOM
})
@Retention(RetentionPolicy.SOURCE)
public @interface DisplayOptions {}

...
```

When you build code with an annotation flag, a warning is generated if the decorated parameter
or return value doesn't reference a valid pattern.

## Keep annotation


The `https://developer.android.com/reference/androidx/annotation/Keep`
annotation ensures that an annotated class or method is not removed when the code
is minified at build time. This annotation is typically
added to methods and classes that are accessed through reflection to prevent the compiler from
treating the code as unused.
**Caution:** The classes and methods that you annotate
using `@Keep` always appear in your app's APK, even if you never
reference these classes and methods within your app's logic.

To keep your app's size small, consider whether it's necessary to preserve
each `@Keep` annotation in your app. If you use reflection to
access an annotated class or method, use an
[`-if`](https://www.guardsquare.com/en/products/proguard/manual/usage#if) conditional in your ProGuard rules, specifying the class
that makes the reflection calls.


For more information about how to minify your code and specify which code is not to be removed,
see [Shrink, obfuscate, and optimize your app](https://developer.android.com/studio/build/shrink-code).

## Code visibility annotations


Use the following annotations to denote the visibility of specific portions of code, such as
methods, classes, fields, or packages.

### Make code visible for testing


The
`https://developer.android.com/reference/androidx/annotation/VisibleForTesting`
annotation indicates that an annotated method is more visible than normally necessary to make the
method testable. This annotation has an optional `otherwise` argument that lets you
designate what the visibility of the method would be if not for the need to make it visible
for testing. Lint uses the `otherwise` argument to enforce the intended visibility.


In the following example, `myMethod()` is normally `private`, but it is
`package-private` for tests. With the `VisibleForTesting.PRIVATE`
designation, lint displays a message if this method is called from outside the
context allowed by `private` access, such as from a different compilation unit.

### Kotlin

```kotlin
@VisibleForTesting(otherwise = VisibleForTesting.PRIVATE)
fun myMethod() {
    ...
}
```

### Java

```java
@VisibleForTesting(otherwise = VisibleForTesting.PRIVATE)
void myMethod() { ... }
```


You can also specify `@VisibleForTesting(otherwise = VisibleForTesting.NONE)`
to indicate that a method exists only for testing. This form is the same as using
`@RestrictTo(TESTS)`. They both perform the same lint check.

### Restrict an API


The `https://developer.android.com/reference/androidx/annotation/RestrictTo`
annotation indicates that access to the annotated API (package, class, or method) is limited,
as follows:

#### Subclasses


Use the annotation form `@RestrictTo(RestrictTo.Scope.SUBCLASSES)` to restrict
API access to subclasses only.


Only classes that extend the annotated class can access this API. The Java
`protected` modifier is not restrictive enough, because it allows access
from unrelated classes within the same package. Also, there are cases when you want to leave a
method `public` for future flexibility, because you can never make a previously
`protected` and overridden method `public`, but you want to provide a
hint that the class is intended for usages within the class or from subclasses only.

#### Libraries


Use the annotation form `@RestrictTo(RestrictTo.Scope.LIBRARY_GROUP_PREFIX)` to
restrict API access to your libraries only.


Only your library code can access the annotated API. This lets you not only organize your code
in whatever package hierarchy you want but also share
the code among a group of related libraries. This option is already available to the Jetpack
libraries that have a lot of implementation code that is not meant for external use, but that
has to be `public` to share it across the various complementary Jetpack libraries.

#### Testing


Use the annotation form `@RestrictTo(RestrictTo.Scope.TESTS)` to prevent other
developers from accessing your testing APIs.


Only testing code can access the annotated API. This prevents other developers
from using APIs for development that you intend for testing purposes only.