---
title: https://developer.android.com/kotlin/interop
url: https://developer.android.com/kotlin/interop
source: md.txt
---

# Kotlin-Java interop guide

This document is a set of rules for authoring public APIs in Java and Kotlin with the intent that the code will feel idiomatic when consumed from the other language.

[Last update: 2024-07-29](https://developer.android.com/kotlin/guides-changelog)

## Java (for Kotlin consumption)

### No hard keywords

Don't use any of Kotlin's[hard keywords](https://kotlinlang.org/docs/reference/keyword-reference.html#hard-keywords)as the name of methods or fields. These require the use of backticks to escape when calling from Kotlin.[Soft keywords](https://kotlinlang.org/docs/reference/keyword-reference.html#soft-keywords),[modifier keywords](https://kotlinlang.org/docs/reference/keyword-reference.html#modifier-keywords), and[special identifiers](https://kotlinlang.org/docs/reference/keyword-reference.html#special-identifiers)are allowed.

For example, Mockito's`when`function requires backticks when used from Kotlin:  

    val callable = Mockito.mock(Callable::class.java)
    Mockito.`when`(callable.call()).thenReturn(/* ... */)

### Avoid`Any`extension names

Avoid using the names of the[extension functions on`Any`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html#extension-functions)for methods or the names of the[extension properties on`Any`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html#extension-properties)for fields unless absolutely necessary. While member methods and fields will always have precedence over`Any`'s extension functions or properties, it can be difficult when reading the code to know which one is being called.

### Nullability annotations

Every non-primitive parameter, return, and field type in a public API should have a nullability annotation. Non-annotated types are interpreted as["platform" types](https://kotlinlang.org/docs/reference/java-interop.html#null-safety-and-platform-types), which have ambiguous nullability.

By default, the Kotlin compiler flags honors JSR 305 annotations but flags them with warnings. You can also set a flag to have the compiler treat the annotations as errors.

### Lambda parameters last

Parameter types eligible for[SAM conversion](https://kotlinlang.org/docs/reference/java-interop.html#sam-conversions)should be last.

For example, RxJava 2's`Flowable.create()`method signature is defined as:  

    public static <T> Flowable<T> create(
        FlowableOnSubscribe<T> source,
        BackpressureStrategy mode) { /* ... */ }

Because FlowableOnSubscribe is eligible for SAM conversion, function calls of this method from Kotlin look like this:  

    Flowable.create({ /* ... */ }, BackpressureStrategy.LATEST)

If the parameters were reversed in the method signature, though, function calls could use the trailing-lambda syntax:  

    Flowable.create(BackpressureStrategy.LATEST) { /* ... */ }

### Property prefixes

For a method to be represented as a property in Kotlin, strict "bean"-style prefixing must be used.

Accessor methods require a`get`prefix or for boolean-returning methods an`is`prefix can be used.  

    public final class User {
      public String getName() { /* ... */ }
      public boolean isActive() { /* ... */ }
    }

    val name = user.name // Invokes user.getName()
    val active = user.isActive // Invokes user.isActive()

Associated mutator methods require a`set`prefix.  

    public final class User {
      public String getName() { /* ... */ }
      public void setName(String name) { /* ... */ }
      public boolean isActive() { /* ... */ }
      public void setActive(boolean active) { /* ... */ }
    }

    user.name = "Bob" // Invokes user.setName(String)
    user.isActive = true // Invokes user.setActive(boolean)

If you want methods exposed as properties, don't use non-standard prefixes like`has`,`set`or non-`get`-prefixed accessors. Methods with non-standard prefixes are still callable as functions, which may be acceptable depending on the behavior of the method.

### Operator overloading

Be mindful of method names that allow special call-site syntax (such as[operator overloading](https://kotlinlang.org/docs/reference/operator-overloading.html))in Kotlin). Ensure that methods names as such make sense to use with the shortened syntax.  

    public final class IntBox {
      private final int value;
      public IntBox(int value) {
        this.value = value;
      }
      public IntBox plus(IntBox other) {
        return new IntBox(value + other.value);
      }
    }

    val one = IntBox(1)
    val two = IntBox(2)
    val three = one + two // Invokes one.plus(two)

## Kotlin (for Java consumption)

### Filename

When a file contains top-level functions or properties,*always* annotate it with`@file:JvmName("Foo")`to provide a nice name.

By default, top-level members in a file MyClass.kt will end up in a class called`MyClassKt`which is unappealing and leaks the language as an implementation detail.

Consider adding`@file:JvmMultifileClass`to combine the top-level members from multiple files into a single class.

### Lambda arguments

Single method interfaces (SAM) defined in Java can be implemented in both Kotlin and Java using lambda syntax, which inlines the implementation in an idiomatic way. Kotlin has several options for defining such interfaces, each with a slight difference.

#### Preferable definition

[Higher-order functions](https://kotlinlang.org/docs/lambdas.html#higher-order-functions)that are meant to be used from Java shouldn't take[function types](https://kotlinlang.org/docs/reference/lambdas.html#function-types)that return`Unit`as that would require Java callers to return`Unit.INSTANCE`. Instead of inlining the function type in the signature, use[functional (SAM) interfaces](https://kotlinlang.org/docs/fun-interfaces.html). Also consider using[functional (SAM) interfaces](https://kotlinlang.org/docs/fun-interfaces.html)instead of regular interfaces when defining interfaces that are expected to be used as lambdas, which allows idiomatic usage from Kotlin.

Consider this Kotlin definition:  

    fun interface GreeterCallback {
      fun greetName(String name)
    }

    fun sayHi(greeter: GreeterCallback) = /* ... */

When invoked from Kotlin:  

    sayHi { println("Hello, $it!") }

When invoked from Java:  

    sayHi(name -> System.out.println("Hello, " + name + "!"));

Even when the function type does not return a`Unit`it might still be a good idea to make it a named interface to allow callers to implement it with a named class and not just lambdas (in both Kotlin and Java).  

    class MyGreeterCallback : GreeterCallback {
      override fun greetName(name: String) {
        println("Hello, $name!");
      }
    }

#### Avoid function types that return`Unit`

Consider this Kotlin definition:  

    fun sayHi(greeter: (String) -> Unit) = /* ... */

It requires Java callers to return`Unit.INSTANCE`:  

    sayHi(name -> {
      System.out.println("Hello, " + name + "!");
      return Unit.INSTANCE;
    });

#### Avoid functional interfaces when the implementation is meant to have state

When the interface implementation is meant to have a state, using the lambda syntax doesn't make sense.[Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html)is a prominent example, as it's meant to compare`this`to`other`, and lambdas don't have`this`. Not prefixing the interface with`fun`forces the caller to use`object : ...`syntax, which allows it to have state, providing a hint to the caller.

Consider this Kotlin definition:  

    // No "fun" prefix.
    interface Counter {
      fun increment()
    }

It prevents lambda syntax in Kotlin, requiring this longer version:  

    runCounter(object : Counter {
      private var increments = 0 // State

      override fun increment() {
        increments++
      }
    })

### Avoid`Nothing`generics

A type whose generic parameter is`Nothing`is exposed as raw types to Java. Raw types are rarely used in Java and should be avoided.

### Document exceptions

Functions which can throw checked exceptions should document them with`@Throws`. Runtime exceptions should be documented in KDoc.

Be mindful of the APIs a function delegates to as they may throw checked exceptions which Kotlin otherwise silently allows to propagate.

### Defensive copies

When returning shared or unowned read-only collections from public APIs, wrap them in an unmodifiable container or perform a defensive copy. Despite Kotlin enforcing their read-only property, there is no such enforcement on the Java side. Without the wrapper or defensive copy, invariants can be violated by returning a long-lived collection reference.

### Companion functions

Public functions in a**companion object** must be annotated with`@JvmStatic`to be exposed as a static method.

Without the annotation, these functions are only available as instance methods on a static`Companion`field.

*Incorrect: no annotation*  

    class KotlinClass {
        companion object {
            fun doWork() {
                /* ... */
            }
        }
    }

    public final class JavaClass {
        public static void main(String... args) {
            KotlinClass.Companion.doWork();
        }
    }

*Correct:* `@JvmStatic`*annotation*  

    class KotlinClass {
        companion object {
            @JvmStatic fun doWork() {
                /* ... */
            }
        }
    }

    public final class JavaClass {
        public static void main(String... args) {
            KotlinClass.doWork();
        }
    }

### Companion constants

Public, non-`const`properties which are effective constants in a`companion
object`must be annotated with`@JvmField`to be exposed as a static field.

Without the annotation, these properties are only available as oddly-named instance "getters" on the static`Companion`field. Using`@JvmStatic`instead of`@JvmField`moves the oddly-named "getters" to static methods on the class, which is still incorrect.

*Incorrect: no annotation*  

    class KotlinClass {
        companion object {
            const val INTEGER_ONE = 1
            val BIG_INTEGER_ONE = BigInteger.ONE
        }
    }

    public final class JavaClass {
        public static void main(String... args) {
            System.out.println(KotlinClass.INTEGER_ONE);
            System.out.println(KotlinClass.Companion.getBIG_INTEGER_ONE());
        }
    }

*Incorrect:* `@JvmStatic`*annotation*  

    class KotlinClass {
        companion object {
            const val INTEGER_ONE = 1
            @JvmStatic val BIG_INTEGER_ONE = BigInteger.ONE
        }
    }

    public final class JavaClass {
        public static void main(String... args) {
            System.out.println(KotlinClass.INTEGER_ONE);
            System.out.println(KotlinClass.getBIG_INTEGER_ONE());
        }
    }

*Correct:* `@JvmField`*annotation*  

    class KotlinClass {
        companion object {
            const val INTEGER_ONE = 1
            @JvmField val BIG_INTEGER_ONE = BigInteger.ONE
        }
    }

    public final class JavaClass {
        public static void main(String... args) {
            System.out.println(KotlinClass.INTEGER_ONE);
            System.out.println(KotlinClass.BIG_INTEGER_ONE);
        }
    }

### Idiomatic naming

Kotlin has different calling conventions than Java which can change the way you name functions. Use`@JvmName`to design names such that they'll feel idiomatic for both language's conventions or to match their respective standard library naming.

This most frequently occurs for extension functions and extension properties because the location of the receiver type is different.  

    sealed class Optional<T : Any>
    data class Some<T : Any>(val value: T): Optional<T>()
    object None : Optional<Nothing>()

    @JvmName("ofNullable")
    fun <T> T?.asOptional() = if (this == null) None else Some(this)

    // FROM KOTLIN:
    fun main(vararg args: String) {
        val nullableString: String? = "foo"
        val optionalString = nullableString.asOptional()
    }

    // FROM JAVA:
    public static void main(String... args) {
        String nullableString = "Foo";
        Optional<String> optionalString =
              Optionals.ofNullable(nullableString);
    }

### Function overloads for defaults

Functions with parameters having a default value must use`@JvmOverloads`. Without this annotation it is impossible to invoke the function using any default values.

When using`@JvmOverloads`, inspect the generated methods to ensure they each make sense. If they don't, perform one or both of the following refactorings until satisfied:

- Change the parameter order to prefer those with defaults being towards the end.
- Move the defaults into manual function overloads.

*Incorrect: No* `@JvmOverloads`  

    class Greeting {
        fun sayHello(prefix: String = "Mr.", name: String) {
            println("Hello, $prefix $name")
        }
    }

    public class JavaClass {
        public static void main(String... args) {
            Greeting greeting = new Greeting();
            greeting.sayHello("Mr.", "Bob");
        }
    }

*Correct:* `@JvmOverloads`*annotation.*  

    class Greeting {
        @JvmOverloads
        fun sayHello(prefix: String = "Mr.", name: String) {
            println("Hello, $prefix $name")
        }
    }

    public class JavaClass {
        public static void main(String... args) {
            Greeting greeting = new Greeting();
            greeting.sayHello("Bob");
        }
    }

## Lint Checks

### Requirements

- **Android Studio version:**3.2 Canary 10 or later
- **Android Gradle Plugin version:**3.2 or later

### Supported Checks

There are now Android Lint checks that will help you detect and flag some of the interoperability issues described previously. Only issues in Java (for Kotlin consumption) are detected. Specifically, the supported checks are:

- Unknown Nullness
- Property Access
- No Hard Kotlin keywords
- Lambda Parameters Last

### Android Studio

To enable these checks, go to**File \> Preferences \> Editor \> Inspections**and check the rules that you want to enable under Kotlin Interoperability:

![](https://developer.android.com/static/kotlin/images/kotlin_interop_checks_settings.png)

**Figure 1.**Kotlin interoperability settings in Android Studio.

Once you have checked the rules you would like to enable, the new checks will run when you run your code inspections (**Analyze \> Inspect Code...**)

### Command-line builds

To enable these checks from the command-line builds, add the following line in your`build.gradle`file:  

### Groovy

```groovy
android {

    ...

    lintOptions {
        enable 'Interoperability'
    }
}
```

### Kotlin

```kotlin
android {
    ...

    lintOptions {
        enable("Interoperability")
    }
}
```

For the full set of configurations supported inside lintOptions, refer to the Android[Gradle DSL reference](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.LintOptions.html).

Then, run`./gradlew lint`from the command line.