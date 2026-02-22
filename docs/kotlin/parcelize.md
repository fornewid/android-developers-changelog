---
title: https://developer.android.com/kotlin/parcelize
url: https://developer.android.com/kotlin/parcelize
source: md.txt
---

# Parcelable implementation generator

The[`kotlin-parcelize`plugin](https://plugins.gradle.org/plugin/org.jetbrains.kotlin.plugin.parcelize)provides a[`Parcelable`](https://developer.android.com/reference/android/os/Parcelable)implementation generator.

To include support for`Parcelable`, add the Gradle plugin to your app's`build.gradle`file:  

### Groovy

```groovy
plugins {
    id 'kotlin-parcelize'
}
```

### Kotlin

```kotlin
plugins {
    id("kotlin-parcelize")
}
```

When you annotate a class with`@Parcelize`, a`Parcelable`implementation is automatically generated, as shown in the following example:  

    import kotlinx.parcelize.Parcelize

    @Parcelize
    class User(val firstName: String, val lastName: String, val age: Int): Parcelable

`@Parcelize`requires all serialized properties to be declared in the primary constructor. The plugin issues a warning on each property with a backing field declared in the class body. Also, you can't apply`@Parcelize`if some of the primary constructor parameters are not properties.

If your class requires more advanced serialization logic, write it inside a companion class:  

    @Parcelize
    data class User(val firstName: String, val lastName: String, val age: Int) : Parcelable {
        private companion object : Parceler<User> {
            override fun User.write(parcel: Parcel, flags: Int) {
                // Custom write implementation
            }

            override fun create(parcel: Parcel): User {
                // Custom read implementation
            }
        }
    }

## Supported types

`@Parcelize`supports a wide range of types:

- Primitive types (and their boxed versions)
- Objects and enums
- `String`,`CharSequence`
- `Duration`
- `Exception`
- `Size`,`SizeF`,`Bundle`,`IBinder`,`IInterface`,`FileDescriptor`
- `SparseArray`,`SparseIntArray`,`SparseLongArray`,`SparseBooleanArray`
- All`Serializable`(including`Date`) and`Parcelable`implementations
- Collections of all supported types:`List`(mapped to`ArrayList`),`Set`(mapped to`LinkedHashSet`),`Map`(mapped to`LinkedHashMap`)
  - Also a number of concrete implementations:`ArrayList`,`LinkedList`,`SortedSet`,`NavigableSet`,`HashSet`,`LinkedHashSet`,`TreeSet`,`SortedMap`,`NavigableMap`,`HashMap`,`LinkedHashMap`,`TreeMap`,`ConcurrentHashMap`
- Arrays of all supported types
- Nullable versions of all supported types

## Custom`Parceler`s

If your type is not supported directly, you can write a`Parceler`mapping object for it.  

    class ExternalClass(val value: Int)

    object ExternalClassParceler : Parceler<ExternalClass> {
        override fun create(parcel: Parcel) = ExternalClass(parcel.readInt())

        override fun ExternalClass.write(parcel: Parcel, flags: Int) {
            parcel.writeInt(value)
        }
    }

You can apply external parcelers using`@TypeParceler`or`@WriteWith`annotations:  

    // Class-local parceler
    @Parcelize
    @TypeParceler<ExternalClass, ExternalClassParceler>()
    class MyClass(val external: ExternalClass) : Parcelable

    // Property-local parceler
    @Parcelize
    class MyClass(@TypeParceler<ExternalClass, ExternalClassParceler>() val external: ExternalClass) : Parcelable

    // Type-local parceler
    @Parcelize
    class MyClass(val external: @WriteWith<ExternalClassParceler>() ExternalClass) : Parcelable

## Create data from Parcel

In Java code, you can access the`CREATOR`field directly.  

    class UserCreator {
        static User fromParcel(Parcel parcel) {
            return User.CREATOR.createFromParcel(parcel);
        }
    }

In Kotlin, you can't use the`CREATOR`field directly. Instead, use`kotlinx.parcelize.parcelableCreator`.  

    import kotlinx.parcelize.parcelableCreator

    fun userFromParcel(parcel: Parcel): User {
        return parcelableCreator<User>().createFromParcel(parcel)
    }

## Skip properties from serialization

If you want to skip some property from being parcelized, use the`@IgnoredOnParcel`annotation. It can also be used on properties within a class's body to silence warnings about the property not being serialized. Constructor properties annotated with`@IgnoredOnParcel`must have a default value.  

    @Parcelize
    class MyClass(
        val include: String,
        // Don't serialize this property
        @IgnoredOnParcel val ignore: String = "default"
    ): Parcelable {
        // Silence a warning
        @IgnoredOnParcel
        val computed: String = include + ignore
    }

## Use android.os.Parcel.writeValue for serializing a property

You can annotate a type with`@RawValue`to make Parcelize use`Parcel.writeValue`for that property.  

    @Parcelize
    class MyClass(val external: @RawValue ExternalClass): Parcelable

This might fail at runtime if the value of the property is not[natively supported by Android](https://developer.android.com/reference/android/os/Parcel#writeValue(java.lang.Object)).

Parcelize might also require you to use this annotation when there is no other way to serialize the property.

## Parcelize with sealed classes and sealed interfaces

Parcelize requires a class to parcelize to not be abstract. This limitation does not hold for sealed classes. When the`@Parcelize`annotation is used on a sealed class, it does not need to be repeated for the deriving classes.  

    @Parcelize
    sealed class SealedClass: Parcelable {
        class A(val a: String): SealedClass()
        class B(val b: Int): SealedClass()
    }

    @Parcelize
    class MyClass(val a: SealedClass.A, val b: SealedClass.B, val c: SealedClass): Parcelable

## Setup Parcelize for Kotlin multiplatform

| **Caution:** The Parcelize library is designed specifically for Android. While it's possible to include this library in multiplatform projects, note that features will be significantly limited.

Prior to Kotlin 2.0, you could use Parcelize by aliasing Parcelize annotations with`expect`and`actual`:  

    // Common code
    package example

    @Target(AnnotationTarget.CLASS)
    @Retention(AnnotationRetention.BINARY)
    expect annotation class MyParcelize()

    expect interface MyParcelable

    @Target(AnnotationTarget.PROPERTY)
    @Retention(AnnotationRetention.SOURCE)
    expect annotation class MyIgnoredOnParcel()

    @MyParcelize
    class MyClass(
        val x: String,
        @MyIgnoredOnParcel val y: String = ""
    ): MyParcelable

    // Platform code
    package example

    actual typealias MyParcelize = kotlinx.parcelize.Parcelize
    actual typealias MyParcelable = android.os.Parcelable
    actual typealias MyIgnoredOnParcel = kotlinx.parcelize.IgnoredOnParcel

In Kotlin 2.0 and higher, aliasing annotations that trigger plugins is unsupported. To circumvent this, provide a new`Parcelize`annotation as the`additionalAnnotation`parameter to the plugin instead.  

    // Gradle build configuration
    kotlin {
        androidTarget {
            compilerOptions {
                // ...
                freeCompilerArgs.addAll("-P", "plugin:org.jetbrains.kotlin.parcelize:additionalAnnotation=example.MyParcelize")
            }
        }
    }

    // Common code
    package example

    @Target(AnnotationTarget.CLASS)
    @Retention(AnnotationRetention.BINARY)
    // No `expect` keyword here
    annotation class MyParcelize()

    expect interface MyParcelable

    @Target(AnnotationTarget.PROPERTY)
    @Retention(AnnotationRetention.SOURCE)
    expect annotation class MyIgnoredOnParcel()

    @MyParcelize
    class MyClass(
        val x: String,
        @MyIgnoredOnParcel val y: String = ""
    ): MyParcelable

    // Platform code
    package example

    // No typealias for MyParcelize here
    actual typealias MyParcelable = android.os.Parcelable
    actual typealias MyIgnoredOnParcel = kotlinx.parcelize.IgnoredOnParcel

Because the`Parcel`interface is only available on Android, Parcelize won't generate any code on other platforms, so any`actual`implementations there can be empty. It is also not possible to use any annotation that requires referencing the`Parcel`class, for example[`@WriteWith`](https://developer.android.com/kotlin/parcelize#custom_parcelers), in common code.

## Experimental features

| **Caution:** Features described in this section are not guaranteed to be stable and may change in future versions without warning. Feel free to[provide feedback](https://developer.android.com/kotlin/parcelize#feedback)if you encounter any issues.

### Data class serializer

Available since Kotlin 2.1.0.

The`DataClass`annotation allows for serializing data classes as if they were themselves annotated with`Parcelize`. This annotation requires the`kotlinx.parcelize.Experimental`opt-in.  

    @file:OptIn(kotlinx.parcelize.Experimental::class)

    data class C(val a: Int, val b: String)

    @Parcelize
    class P(val c: @DataClass C) : Parcelable

The primary constructor and all of its properties must be accessible from the`Parcelable`class. Additionally, all primary constructor properties of the data class must be supported by`Parcelize`.[Custom Parcelers](https://developer.android.com/kotlin/parcelize#custom_parcelers), if chosen, should be specified on the`Parcelable`class,*not* the data class. If the data class implements`Serializable`at the same time, the`@DataClass`annotation takes priority:[`android.os.Parcel.writeSerializable`](https://developer.android.com/reference/android/os/Parcel#writeSerializable(java.io.Serializable))won't be used.

A practical use case for this is serializing[`kotlin.Pair`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-pair/). Another useful example is simplifying[multiplatform code](https://developer.android.com/kotlin/parcelize#setup_parcelize_for_kotlin_multiplatform): common code could declare the data layer as data classes, which Android code could then augment with serialization logic, removing the need for Android-specific annotations and type aliases in common code.  

    // Common code:
    data class MyData(val x: String, val y: MoreData)
    data class MoreData(val a: String, val b: Int)

    // Platform code:
    @OptIn(kotlinx.parcelize.Experimental::class)
    @Parcelize
    class DataWrapper(val wrapped: @DataClass MyData): Parcelable

### Non val or var parameters in primary constructor

Available since Kotlin 2.1.0.

To enable this feature add`experimentalCodeGeneration=true`to the parcelize plugin arguments.  

    kotlin {
        compilerOptions {
            // ...
            freeCompilerArgs.addAll("-P", "plugin:org.jetbrains.kotlin.parcelize:experimentalCodeGeneration=true")
        }
    }

This feature lifts the restriction on primary constructor arguments having to be`val`or`var`. This solves one pain point of using parcelize with inheritance, which earlier required using`open`properties.  

    // base parcelize
    @Parcelize
    open class Base(open val s: String): Parcelable

    @Parcelize
    class Derived(
        val x: Int,
        // all arguments have to be `val` or `var` so we need to override
        // to not introduce new property name
        override val s: String
    ): Base(s)

    // experimental code generation enabled
    @Parcelize
    open class Base(val s: String): Parcelable

    @Parcelize
    class Derived(val x: Int, s: String): Base(s)

Such parameters are only allowed to be used in arguments to the base class constructor. Referencing them in the body of the class is not allowed.  

    @Parcelize
    class Derived(s: String): Base(s) { // allowed
        @IgnoredOnParcel
        val x: String = s // ERROR: not allowed.
        init {
            println(s) // ERROR: not allowed
        }
    }

## Feedback

If you encounter any issues with the`kotlin-parcelize`Gradle plugin, you can[file a bug](https://issuetracker.google.com/issues/new?component=971607).