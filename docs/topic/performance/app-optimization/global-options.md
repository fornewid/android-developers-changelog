---
title: https://developer.android.com/topic/performance/app-optimization/global-options
url: https://developer.android.com/topic/performance/app-optimization/global-options
source: md.txt
---

R8 provides global options that either modify R8's optimizations throughout the
app or affect every keep rule. These options are maintained in the
`proguard-rules.pro` file, along with keep rules. A few of these global options
configure additional optimization, while others turn off certain aspects of the
optimization.

> [!NOTE]
> **Note:** For information about various keep rules , see [Add keep rules](https://developer.android.com/topic/performance/app-optimization/add-keep-rules), [Additional rule types](https://developer.android.com/topic/performance/app-optimization/additional-rule-types), and[Troubleshooting rules](https://developer.android.com/topic/performance/app-optimization/troubleshooting-rules).

## Global options for additional optimization

The following global options enable additional optimization:

- `-repackageclasses [<optional-package-name>]`: Repackages classes into a single package to reduce app size. If you don't supply the optional package name, classes are moved into the unnamed default package. This is the recommended setting for apps because it results in smaller DEX files by omitting the package prefix from class names.
- `-allowaccessmodification`: Lets R8 change (typically widen) the visibility of classes, fields, and methods to perform more extensive optimizations. Enabled when `proguard-android-optimize.txt` is used. Since Android Gradle Plugin (AGP) 8.2, this is the default configuration if you enable [full
  optimization with R8](https://developer.android.com/topic/performance/app-optimization/full-mode).
- `-processkotlinnullchecks [level]`: Lets R8 change the Kotlin Intrinsics
  null checks to either just remove the error message or completely remove
  the explicit null check.

  The `level` values, ordered from the weakest to the strongest, have the
  following effect:
  - `keep` doesn't change the checks.
  - `remove_message` rewrites each check method call to a call to `getClass()` on the first argument of the call (effectively keeping the null check, but without any message).
  - `remove` completely removes the checks.

  By default R8 uses `remove_message`. Any specification of
  `-processkotlinnullchecks` overrides that. If specified multiple times
  the strongest value is used.

  `-processkotlinnullchecks` is supported from AGP 9.0.0.

> [!WARNING]
> **Warning:** If you are a library author, you must never add any of the global options for additional optimizations in consumer keep rules. For more details about optimizing libraries, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization).

The following is an example of a configuration with additional optimization
enabled:

    -repackageclasses
    -allowaccessmodification

## Global options to limit optimization

The following global options let you turn off certain aspects of app
optimization, and are helpful when you're refining your keep rules or turning on
R8 for the first time.

- `-dontoptimize`: Prevents code optimization, for example method inlining. This option can be used during development but shouldn't be used in production builds.
- `-dontshrink`: Prevents the removal of unreferenced code and code optimizations. This option can be used during development but shouldn't be used in production builds.
- `-dontobfuscate`: Prevents shortening the names of classes and methods. It can be especially helpful to turn off obfuscation during debugging so stack traces are easier to read. This option can be used during development but shouldn't be used in production builds.
- `-keepattributes <attributes>`: Accepts a comma-separated list of attributes that should be preserved. If you're *not* using the default `proguard-android-optimize.txt`, R8 strips all attributes including `RuntimeVisibleAnnotations` and `Signature`, however it can be helpful to preserve these attributes if they are needed in cases like reflection. For a list of attributes you can specify, see [Keep attributes](https://developer.android.com/topic/performance/app-optimization/global-options#keep-attributes).

> [!WARNING]
> **Warning:** You should only use the options `-dontoptimize`, `-dontshrink`, and `-dontobfuscate` temporarily during debugging or development. Remove these options in production builds since they significantly limit the extent of optimizations.

### Keep attributes

Attributes are extra pieces of information attached to different parts of your
code. Attributes store information like annotations and generic signatures from
your code.

Certain reflective operations require specific attributes to be kept for
successful execution. For example:

- When accessing the inner or outer class structure using `getEnclosingMethod()` or `getDeclaredClasses()`, the attributes `EnclosingMethod` and `InnerClasses` are needed.
- When accessing generic signatures using `getTypeParameters()`, the attribute `Signature` is needed.
- When accessing annotations using `getAnnotation()`, the attribute
  `RuntimeVisibleAnnotations` is needed.

  > [!NOTE]
  > **Note:** When working on a keep rule for an annotation, make sure to keep the annotation and the classes that the annotation is applied to.

#### Commonly required attributes

When using the default Proguard file (`proguard-android-optimize.txt` or
`proguard-android.txt`), the Android Gradle plugin (AGP) keeps the following
attributes. Note that some of these attributes require newer versions of AGP:

| Attribute | Description |
|---|---|
| `AnnotationDefault` | This attribute is found on annotation types themselves and stores the default value for an annotation element. **Note:** This attribute is kept by default since AGP 7.1, and only needs to be explicitly kept in apps using earlier versions of AGP. |
| `EnclosingMethod` | This attribute is present in inner classes that are not local or anonymous classes. It identifies the method or initializer that immediately contains the class. |
| `InnerClasses` | This attribute records information about nested classes (inner classes, static nested classes, local classes, and anonymous classes) defined within another class. |
| `LineNumberTable` | This attribute maps bytecode instructions to their corresponding line numbers in the original source file. **Note:** This attribute is kept by default since Android Gradle Plugin (AGP) 8.6, and only needs to be explicitly kept in apps using earlier versions of AGP. |
| `RuntimeVisibleAnnotations` | This attribute stores annotations that are visible at runtime by reflection. Typically, if annotations are used at runtime, this is the only annotation from the `*Annotation` attributes that is needed by apps and in library consumer rules. |
| `RuntimeVisibleParameterAnnotations` | This attribute stores annotations that are visible at runtime by reflection on the parameters of a method. |
| `RuntimeVisibleTypeAnnotations` | This attribute stores annotations that apply to type uses rather than just declarations. This attribute is visible at runtime. |
| `Signature` | This attribute stores a more generic type signature for classes, methods, and fields, particularly when they use generics (like `List<String>`). |
| `SourceFile` | This attribute stores the name of the source file (`.kt` or `.java` file) from which a class was compiled. It is primarily used by debuggers to display the original source code lines when stepping through compiled Java code. It helps developers trace execution back to their written code. **Note:** This attribute is kept by default since AGP 8.2, and only needs to be explicitly kept in apps using earlier versions of AGP. |

For apps that use `proguard-android-optimize.txt`, the keep rules defined by AGP
are adequate in most scenarios. However, if you are writing code for a library,
you should specify all the attributes required by your library in its [consumer
keep rules](https://developer.android.com/topic/performance/app-optimization/library-optimization#write-consumer-rules), even if they are defined in this list. This makes sure that your
library is robust if developers decide not to include
`proguard-android-optimize.txt`.

> [!TIP]
> **Tip:** It is recommended to keep as few attributes as possible because each attribute that you keep limits a global optimization.

> [!NOTE]
> **Note:** Additional attributes with debug information (such as `LocalVariableTable` and `LocalVariableTypeTable`) are controlled by whether the R8 build is in release or debug mode- including them with `-keepattributes` has no effect.

#### Additional keep attributes

You can specify additional attributes to be kept, however they are not needed
for the vast majority of reflective or JNI access scenarios. However, some of
these might still frequently be used while [optimizing libraries](https://developer.android.com/topic/performance/app-optimization/library-optimization).

| Attribute | Description |
|---|---|
| `MethodParameters` | This attribute provides information about the parameters of a method, specifically their names and access flags. |
| `Exceptions` | This attribute lists the checked exceptions that a method is declared to throw. This attribute is not typically used for apps. For library authors, it is not typically used in consumer keep rules, but is often used when building libraries. For details about optimizing libraries, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization). |
| `RuntimeInvisibleAnnotations` | This attribute stores annotations that are not visible with reflection at runtime on a class, field, or method. App developers shouldn't keep this attribute. For library authors, this attribute is not relevant in consumer keep rules, but is often used when building libraries. For details about optimizing libraries, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization). |
| `RuntimeInvisibleParameterAnnotations` | This attribute stores annotations that are not visible with reflection at runtime on the parameters of a method. App developers shouldn't keep this attribute. For library authors, this attribute is not relevant in consumer keep rules, but is often used when building libraries. For details about optimizing libraries, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization). |
| `RuntimeInvisibleTypeAnnotations` | This attribute stores annotations that apply to type uses rather than just declarations. This attribute is not visible at runtime. App developers shouldn't keep this attribute. For library authors, this attribute is not relevant in consumer keep rules, but is often used when building libraries. For details about optimizing libraries, see [Optimization for library authors](https://developer.android.com/topic/performance/app-optimization/library-optimization). |