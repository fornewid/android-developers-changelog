---
title: https://developer.android.com/topic/performance/app-optimization/add-keep-rules
url: https://developer.android.com/topic/performance/app-optimization/add-keep-rules
source: md.txt
---

At a high level, a keep rule specifies a class (or subclass or implementation),
and then members---methods, constructors, or fields---within that class to preserve.

The general syntax for a keep rule is as follows:


    -https://developer.android.com/topic/performance/app-optimization/add-keep-rules#keep-option[,https://developer.android.com/topic/performance/app-optimization/add-keep-rules#keep-option-modifier,<keep_option_modifier_2>,...] https://developer.android.com/topic/performance/app-optimization/add-keep-rules#class-spec

The following is an example of a keep rule that uses `keepclassmembers` as the
keep option, `allowoptimization` as the modifier, and keeps
`someSpecificMethod()` from `com.example.MyClass`:

    -keepclassmembers,allowoptimization class com.example.MyClass {
      void someSpecificMethod();
    }

> [!NOTE]
> **Note:** Apart from rules that specify items that must be kept, R8 also lets you configure additional rules that impact the optimization. For more information, see [Additional rule types](https://developer.android.com/topic/performance/app-optimization/additional-rules-types), [Troubleshooting rules](https://developer.android.com/topic/performance/app-optimization/troubleshooting-rules), and [Global options](https://developer.android.com/topic/performance/app-optimization/global-options).

## Keep option

The keep option is the first part of your keep rule. It specifies what aspects
of a class to preserve. There are six different keep options, namely `keep`,
`keepclassmembers`, `keepclasseswithmembers`, `keepnames`,
`keepclassmembernames`, `keepclasseswithmembernames`.

The following table describes these keep options:

| **Keep option** | **Description** |
|---|---|
| `keepclassmembers` | Preserves specified members only *if the class exists after optimization*. |
| `keep` | Preserves specified classes and the specified members (fields and methods), preventing them from being optimized. **Note** : `keep` should generally only be used with [keep option modifiers](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#keep-option-modifier) because `keep` by itself prevents optimizations of any kind from happening on matched classes. |
| `keepclasseswithmembers` | Preserves a class and its specified members only if the class has all of the members from the class specification. |
| `keepclassmembernames` | Prevents the renaming of specified class members, but does not prevent the class or its members from being removed. **Note:** The meaning of this option is often misunderstood; consider using the equivalent `-keepclassmembers,allowshrinking` instead. |
| `keepnames` | Prevents the renaming of classes and their members, but it does not prevent them from being removed entirely if they are deemed unused. **Note:** The meaning of this option is often misunderstood; consider using the equivalent `-keep,allowshrinking` instead. |
| `keepclasseswithmembernames` | Prevents the renaming of classes and their specified members, but only if the members exist in the final code. It does not prevent the removal of code. **Note:** The meaning of this option is often misunderstood; consider using the equivalent `-keepclasseswithmembers,allowshrinking` instead. |

### Choose the right keep option

Picking the right keep option is crucial in determining the right optimization
for your app. Certain keep options shrink code, a process by which
unreferenced code is removed, while others obfuscate, or rename, code. The
following table indicates the actions of the various keep options:

| **Keep option** | **Shrinks classes** | **Obfuscates classes** | **Shrinks members** | **Obfuscates members** |
|---|---|---|---|---|
| `keep` |   |   |   |   |
| `keepclassmembers` |   |   |   |   |
| `keepclasseswithmembers` |   |   |   |   |
| `keepnames` |   |   |   |   |
| `keepclassmembernames` |   |   |   |   |
| `keepclasseswithmembernames` |   |   |   |   |

> [!TIP]
> **Tip:** Avoid using `keep` without keep option modifiers because this limits optimizations, and the options that end with 'names', such as `keepnames`, because their meaning is often misunderstood. We recommend mostly using `keepclassmembers`, since it enables the most optimizations.

## Keep option modifier

A keep option modifier is used to control the scope and behavior of a keep rule.
You can add 0 or more keep option modifiers to your keep rule.

The possible values for a keep option modifier are described in the following
table:

| Value | Description |
|---|---|
| `allowoptimization` | Allows optimization of the specified elements. However, the specified elements are not renamed or removed. |
| `allowobfucastion` | Allows renaming of the specified elements. However, the elements are not be removed or otherwise optimized. |
| `allowshrinking` | Allows removal of the specified elements if R8 finds no references to them. However, the elements are not renamed or otherwise optimized. |
| `includedescriptorclasses` | Instructs R8 to keep all classes that appear in the descriptors of the methods (parameter types and return types) and fields (field types) being kept. |
| `allowaccessmodification` | Allows R8 to change (typically widen) the access modifiers (`public`, `private`, `protected`) of classes, methods, and fields during the optimization process. |
| `allowrepackage` | Allows R8 to move classes into different packages, including the default (root) package. |

## Class specification

You must specify a class (including interface, enum, and annotation classes) in
every keep rule. You can optionally restrict the rule based on annotations, by
specifying a superclass or implemented interface, or by specifying the access
modifier for the class. All classes, including
classes from the `java.lang` namespace like `java.lang.String`, must be
specified using their fully qualified Java name. To understand the names that
should be used, inspect the bytecode using the tools described in [Inspect
generated Java names](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#inspect-java-names).

The following example shows how you should specify the `MaterialButton` class:

- Correct: `com.google.android.material.button.MaterialButton`
- Incorrect: `MaterialButton`

Class specifications also [specify the members](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#member-spec) within a class that should be
kept. For example, the following rule keeps the `MyClass` class and the
`someSpecificMethod()` method:

    -keep class com.example.MyClass {
      void someSpecificMethod();
    }

> [!IMPORTANT]
> **Important:** If you don't specify members, R8 implicitly changes the rule to keep the default constructor for the class. For more information, see [Omitting the member specification](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#omit-member-spec). It is recommended to [specify members](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#member-spec) in your keep rules.

### Specify classes based on annotations

To specify classes based on their annotations, prefix the annotation's fully
qualified Java name with an `@` symbol. For example:

    -keep class @com.example.MyAnnotation com.example.MyClass

If a keep rule has more than one annotation, it keeps classes that have all of
the listed annotations. You can list multiple annotations, but the rule applies
only if the class has every listed annotation. For example, the following rule
keeps all the classes annotated by both `Annotation1` and `Annotation2`.

    -keep class @com.example.Annotation1 @com.example.Annotation2 *

### Specify subclasses and implementations

To target a subclass, or class that implements an interface, use `extend` and
`implements`, respectively.

For example, if you have class `Bar` with subclass `Foo` as follows:

    class Foo : Bar()

The following keep rule preserves all the subclasses of `Bar`. Note that the
keep rule doesn't include the superclass `Bar` itself.

    -keep class * extends Bar

If you have class `Foo` that implements the interface `Bar`:

    class Foo : Bar

The following keep rule preserves all classes that implement `Bar`. Note that
the keep rule doesn't include the interface `Bar` itself.

    -keep class * implements Bar

> [!NOTE]
> **Note:** You can use `extends` or `implements` interchangeably to match classes that inherit from a specific type, whether it's a class or an interface. For example, R8 treats `-keep class * extends Bar` and `-keep class * implements
> Bar` the same.

### Specify classes based on access modifiers

You can specify access modifiers such as `public`, `private`, `static`, and
`final` to make your keep rules more precise.

For example, the following rule keeps all the `public` classes within the `api`
package and its sub-packages, and all the public and protected members in these
classes.

> [!NOTE]
> **Note:** [Package-wide keep rules should only be used temporarily](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally#use-package-wide) when enabling R8.

    -keep public class com.example.api.** { public protected *; }

You can also use modifiers for the members within a class. For example, the
following rule keeps only the `public static` methods of a `Utils` class:

    -keep class com.example.Utils {
      public static void *(...);
    }

> [!NOTE]
> **Note:** You can use `!` to invert the scope of the modifier, however it is not recommended because you could unintentionally apply a rule to almost every class in your app.

#### Kotlin-specific modifiers

R8 doesn't support Kotlin-specific modifiers such as `internal` and `suspend`.
Use the following guidelines to keep such fields.

- To keep an `internal` class, method or field, treat it as public. For
  example, consider the following Kotlin source:

      package com.example
      internal class ImportantInternalClass {
        internal val f: Int
        internal fun m() {}
      }

  The `internal` classes, methods and fields are `public` in the `.class`
  files produced by the Kotlin compiler, so you must use the `public` keyword
  as shown in the following example:

      -keepclassmembers public class com.example.ImportantInternalClass {
        public int f;
        public void m();
      }

- When a `suspend` member is compiled, match its compiled signature in the
  keep rule.

  For example, if you have the function `fetchUser` defined as shown in the
  following snippet:

      suspend fun fetchUser(id: String): User

  When compiled, its signature in the bytecode looks like the following:

      public final Object fetchUser(String id, Continuation<? super User> continuation);

  To write a keep rule for this function, you must match this compiled
  signature, or use `...`.

  An example of using the compiled signature is as follows:

      -keepclassmembers class com.example.repository.UserRepository {
        public java.lang.Object fetchUser(java.lang.String,  kotlin.coroutines.Continuation);
      }

  An example using `...` is as follows:

      -keepclassmembers class com.example.repository.UserRepository {
        public java.lang.Object fetchUser(...);
      }

## Member specification

The class specification optionally includes the class members to be preserved.
If you specify one or more members for a class, the rule does not apply to other
members.

### Specify members based on annotations

You can specify members based on their annotations. Similar to classes, you
prefix the annotation's fully qualified Java name with `@`. This lets you
keep only those members within a class that are marked with specific
annotations. For example, to keep methods and fields annotated with
`@com.example.MyAnnotation`:

    -keep class com.example.MyClass {
      @com.example.MyAnnotation <methods>;
      @com.example.MyAnnotation <fields>;
    }

You can combine this with class-level annotation matching for powerful, targeted
rules:

    -keep class @com.example.ClassAnnotation * {
      @com.example.MethodAnnotation <methods>;
      @com.example.FieldAnnotation <fields>;
    }

This keeps classes annotated with `@ClassAnnotation`, and on those classes, it
keeps methods annotated by `@MethodAnnotation` and fields annotated by
`@FieldAnnotation`.

Consider using annotation-based keep rules when possible. This approach provides
an explicit link between your code and your keep rules and often leads to more
robust configurations. The `androidx.annotation` annotation library, for
example, uses this mechanism.

> [!NOTE]
> **Note:** You can also use [wildcards](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#wildcards) and [access specifiers](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#access-modifier) while specifying members in keep rules.

### Methods

The syntax for specifying a method in the member specification for a keep rule
is as follows:

    [<access_modifier>] [<return_type>] <method_name>(<parameter_types>);

For example, the following keep rule keeps a public method called `setLabel()`
that returns void and takes a `String`.

    -keep class com.example.MyView {
        public void setLabel(java.lang.String);
    }

You can use `<methods>` as a shortcut to match all methods in a class as
follows:

    -keep class com.example.MyView {
        <methods>;
    }

To learn more about how to specify types for return types and parameter types,
see [Types](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#types).

### Constructors

To specify a constructor, use `<init>`. The syntax for specifying a constructor
in the member specification for a keep rule is as follows:

    [<access_modifier>] <init>(parameter_types);

For example, the following keep rule keeps a custom `View` constructor that
takes a `Context` and an `AttributeSet`.

    -keep class com.example.ui.MyCustomView {
        public <init>(android.content.Context, android.util.AttributeSet);
    }

To keep all public constructors, use the following example as a reference:

    -keep class com.example.ui.MyCustomView {
        public <init>(...);
    }

### Fields

The syntax for specifying a field in the member specification for a keep rule is
as follows:

    [<access_modifier>...] [<type>] <field_name>;

For example, the following keep rule keeps a private string field called
`userId` and a public static integer field called `STATUS_ACTIVE`:

    -keep class com.example.models.User {
        private java.lang.String userId;
        public static int STATUS_ACTIVE;
    }

You can use `<fields>` as a shortcut to match all the fields in a class as
follows:

    -keep class com.example.models.User {
        <fields>;
    }

### Types

This section describes how to specify return types, parameter types, and field
types in keep rule member specifications. Remember to use the
[generated Java names](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#inspect-java-names) to specify types if they're different from the Kotlin
source code.

#### Primitive types

To specify a primitive type, use its Java keyword. R8 recognizes the following
primitive types: `boolean`, `byte`, `short`, `char`, `int`, `long`, `float`,
`double`.

An example rule with a primitive type is as follows:

    # Keeps a method that takes an int and a float as parameters.
    -keepclassmembers class com.example.Calculator {
        public void setValues(int, float);
    }

> [!NOTE]
> **Note:** Make sure to handle Kotlin primitive types, such as `Int`, distinctly from the Kotlin nullable number references, such as `Int?`, because they are compiled to different Java types. For example, when compiled `Int` is typically mapped to the Java primitive type `int`, and `Int?` is mapped to the Java wrapper class `java.lang.Integer`.

#### Generic types

During compilation, the Kotlin/Java compiler erases generic type information, so
when you write keep rules that involve generic types you must [target the
compiled representation of your code](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#inspect-java-names), and not the original source code. To
learn more about how generic types are changed, see [Type erasure](https://kotlinlang.org/docs/generics.html#type-erasure).

For example, if you have the following code with an unbounded generic type
defined in `Box.kt`:

    package com.myapp.data

    class Box<T>(val item: T) {
        fun getItem(): T {
            return item
        }
    }

After type erasure, the `T` is replaced by `Object`. To keep the class
constructor and method, your rule must use `java.lang.Object` in place of the
generic `T`.

An example keep rule would be as follows:

    # Keep the constructor and methods of the Box class.
    -keep class com.myapp.data.Box {
        public init(java.lang.Object);
        public java.lang.Object getItem();
    }

If you have the following code with a bounded generic type in `NumberBox.kt`:

    package com.myapp.data

    // T is constrained to be a subtype of Number
    class NumberBox<T : Number>(val number: T)

In this case, type erasure replaces `T` with its bound, `java.lang.Number`.

An example keep rule would be as follows:

    -keep class com.myapp.data.NumberBox {
        public init(java.lang.Number);
    }

When using app-specific generic types as a base class, it's necessary to
include keep rules for the base classes as well.

For example, for the following code:

    package com.myapp.data

    data class UnpackOptions(val useHighPriority: Boolean)

    // The generic Box class with UnpackOptions as the bounded type
    class Box<T: UnpackOptions>(val item: T) {
    }

You can use a keep rule with `includedescriptorclasses` to preserve both the
`UnpackOptions` class and `Box` class method with a single rule as follows:

    -keep,includedescriptorclasses class com.myapp.data.Box {
        public <init>(com.myapp.data.UnpackOptions);
    }

To keep a specific function that processes a list of objects, you need to write
a rule that precisely matches the function's signature. Note that because generic
types are erased, a parameter like `List<Product>` is seen as
`java.util.List`.

For example, if you have a utility class with a function that processes a list
of `Product` objects as follows:

    package com.myapp.utils

    import com.myapp.data.Product
    import android.util.Log

    class DataProcessor {
        // This is the function we want to keep
        fun processProducts(products: List<Product>) {
            Log.d("DataProcessor", "Processing ${products.size} products.")
            // Business logic ...
        }
    }

    // The data class used in the list (from the previous example)
    package com.myapp.data
    data class Product(val id: String, val name: String)

You could use the following keep rule to protect only the `processProducts`
function:

    -keep class com.myapp.utils.DataProcessor {
        public void processProducts(java.util.List);
    }

#### Array types

Specify an array type by appending `[]` to the component type for each dimension
of the array. This applies to both class types and primitive types.

- One-dimensional class array: `java.lang.String[]`
- Two-dimensional primitive array: `int[][]`

For example, if you have the following code:

    package com.example.data

    class ImageProcessor {
      fun process(): ByteArray {
        // process image to return a byte array
      }
    }

You could use the following keep rule:

    # Keeps a method that returns a byte array.
    -keepclassmembers class com.example.data.ImageProcessor {
        public byte[] process();
    }

### Examples

For example, to preserve a specific class and all its members, use the
following:

    -keep class com.myapp.MyClass { *; }

To preserve only the class, along with its default constructor, but not other
members, use the following:

    -keep class com.myapp.MyClass

It is recommended that you always specify some members. For example, the
following example keeps the public field `text` and the public method
`updateText()` within the class `MyClass`.

    -keep class com.myapp.MyClass {
        public java.lang.String text;
        public void updateText(java.lang.String);
    }

To keep all public fields and public methods, see the following example:

    -keep public class com.example.api.ApiClient {
        public *;
    }

### Omitting the member specification

Omitting the member specification causes R8 to keep the default constructor for
the class.

For example, if you write either `-keep class com.example.MyClass` or
`-keep class com.example.MyClass {}`, R8 treats them as if you wrote the
following:

    -keep class com.example.MyClass{
      void <init>();
    }

## Package-level functions

To reference a Kotlin function that's defined outside of a class (commonly
called top level functions), make sure to use the [generated Java name](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#inspect-java-names) for
the class implicitly added by the Kotlin compiler. The class name is the Kotlin
filename with `Kt` appended. For example, if you have a Kotlin file called
`MyClass.kt` defined as follows:

    package com.example.myapp.utils

    // A top-level function not inside a class
    fun isEmailValid(email: String): Boolean {
        return email.contains("@")
    }

To write a keep rule for the `isEmailValid` function, the class specification
needs to target the generated class `MyClassKt`:

    -keep class com.example.myapp.utils.MyClassKt {
        public static boolean isEmailValid(java.lang.String);
    }

## Wildcards

The following table shows how to use wildcards to apply keep rules to multiple
classes or members that match a certain pattern.

| **Wildcard** | **Applies to classes or members** | **Description** |
|---|---|---|
| \*\* | Both | Most commonly used. Matches any type name, including any number of package separators. This is useful for matching all classes within a package and its sub-packages. |
| \* | Both | For class specifications, matches any part of a type name that doesn't contain package separators (`.`) For member specifications, matches any method or field name. When used by itself, it is also an alias for `**`. |
| ? | Both | Matches any single character in a class or member name. |
| \*\*\* | Members | Matches any type, including primitive types (like `int`), class types (like `java.lang.String`), and array types of any dimension (like `byte[][]`). |
| ... | Members | Matches any list of parameters for a method. |
| % | Members | Matches any primitive type (such as \`int\`, \`float\`, \`boolean\`, or others). |

Here are some examples of how to use the special wildcards:

- If you have multiple methods with the same name that take different
  primitive types as inputs, you can use `%` to write a keep rule that keeps
  them all. For example, this `DataStore` class has multiple `setValue`
  methods:

      class DataStore {
          fun setValue(key: String, value: Int) { ... }
          fun setValue(key: String, value: Boolean) { ... }
          fun setValue(key: String, value: Float) { ... }
      }

  The following keep rule keeps all the methods:

      -keep class com.example.DataStore {
          public void setValue(java.lang.String, %);
      }

- If you have multiple classes with names that vary by one character, use `?`
  to write a keep rule that keeps them all. For example, if you have the
  following classes:

      com.example.models.UserV1 {...}
      com.example.models.UserV2 {...}
      com.example.models.UserV3 {...}

  The following keep rule keeps all of the classes:

      -keep class com.example.models.UserV?

- To match the classes `Example` and `AnotherExample` (if they were root-level
  classes), but not `com.foo.Example`, use the following keep rule:

      -keep class *Example

- If you use \* by itself, it acts as an alias for \*\*. For example, the
  following keep rules are equivalent:

      -keepclasseswithmembers class * { public static void main(java.lang.String[];) }

      -keepclasseswithmembers class ** { public static void main(java.lang.String[];) }

## Inspect generated Java names

When writing keep rules, you must specify classes and other reference types
using their names after they're compiled into Java bytecode (see [Class
specification](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#class-spec) and [Types](https://developer.android.com/topic/performance/app-optimization/add-keep-rules#types) for examples). To check what the generated Java
names for your code are, use either of the following tools in Android Studio:

- [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer#show_bytecode_find_usages_and_generate_keep_rule)
- With the Kotlin source file open, inspect the bytecode by going to **Tools \>
  Kotlin \> Show Kotlin Bytecode \> Decompile**.