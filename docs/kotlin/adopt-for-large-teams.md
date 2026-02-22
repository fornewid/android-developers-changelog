---
title: https://developer.android.com/kotlin/adopt-for-large-teams
url: https://developer.android.com/kotlin/adopt-for-large-teams
source: md.txt
---

# Adopt Kotlin for large teams

Moving to any new language can be a daunting task. The recipe for success is to start slow, move in chunks, and test frequently to align your team for success. Kotlin makes migrating easy, as it compiles down to JVM bytecode and is fully interoperable with Java.

### Building the team

The first step before migrating is to build a common baseline understanding for your team. Here are a few tips that you might find useful to accelerate your team's learning.

#### Form study groups

Study groups are an effective way to facilitate learning and retention.[Studies suggest](https://source.wustl.edu/2006/07/discovering-why-study-groups-are-more-effective/)that reciting what you've learned in a group setting helps to reinforce the material. Get a[Kotlin book](https://kotlinlang.org/docs/books.html)or other study material for each member of the group, and ask the group to go through a couple of chapters each week. During each meet, the group should compare what they've learned and discuss any questions or observations.

#### Build a culture of teaching

While not everyone considers themselves to be a teacher, everyone can teach. From a technology or team lead to an individual contributor, everyone can encourage a learning environment that can help to ensure success. One way to facilitate this is to hold periodic presentations where one person on the team is designated to talk about something they've learned or want to share. You can leverage your study group by asking for volunteers to present a new chapter each week until you get to a point where your team feels comfortable with the language.

#### Designate a champion

Finally, designate a champion to lead a learning effort. This person can act as a*subject matter expert*(SME) as you start the adoption process. It is important to include this person in all of your practice meetings related to Kotlin. Ideally, this person is already passionate about Kotlin and has some working knowledge.

### Integrate slowly

Starting slowly and thinking strategically about what parts of your ecosystem to move first is key. It's often best to isolate this to a single app within your organization rather than a flagship app. In terms of migrating the chosen app, each situation is different, but here are a few common places to start.

#### Data model

Your data model likely consists of a lot of state information along with a few methods. The data model might also have common methods such as`toString()`,`equals()`and`hashcode()`. These methods can usually be transitioned and unit tested easily in isolation.

For example, assume the following snippet of Java:  

    public class Person {

       private String firstName;
       private String lastName;
       // ...

       public String getFirstName() {
           return firstName;
       }

       public void setFirstName(String firstName) {
           this.firstName = firstName;
       }

       public String getLastName() {
           return lastName;
       }

       public void setLastName(String lastName) {
           this.lastName = lastName;
       }

       @Override
       public boolean equals(Object o) {
           if (this == o) return true;
           if (o == null || getClass() != o.getClass()) return false;
           Person person = (Person) o;
           return Objects.equals(firstName, person.firstName) &&
                   Objects.equals(lastName, person.lastName);
       }

       @Override
       public int hashCode() {
           return Objects.hash(firstName, lastName);
       }

       @Override
       public String toString() {
           return "Person{" +
                   "firstName='" + firstName + '\'' +
                   ", lastName='" + lastName + '\'' +
                   '}';
       }
    }

You can replace the Java class with a single line of Kotlin, as shown here:  

    data class Person(var firstName: String?, var lastName : String?)

This code can then be unit tested against your current test suite. The idea here is to start small with one model at a time and transition classes that are mostly state and not behavior. Be sure to test often along the way.

#### Migrate tests

Another starting path to consider is to convert existing tests and start writing new tests in Kotlin. This can give your team time to feel comfortable with the language before writing code that you plan to ship with your app.

#### Move utility methods to extension functions

Any static utility classes (`StringUtils`,`IntegerUtils`,`DateUtils`,`YourCustomTypeUtils`, and so on) can be represented as[Kotlin extension functions](https://kotlinlang.org/docs/reference/extensions.html)and used by your existing Java codebase.

For example, consider you have a`StringUtils`class with a few methods:  

    package com.java.project;

    public class StringUtils {

       public static String foo(String receiver) {
           return receiver...;  // Transform the receiver in some way
       }

       public static String bar(String receiver) {
           return receiver...;  // Transform the receiver in some way
       }

    }

These methods might then be used elsewhere in your app, as shown in the following example:  

    ...

    String myString = ...
    String fooString = StringUtils.foo(myString);

    ...

Using Kotlin extension functions, you can provide the same`Utils`interface to Java callers while at the same time offering a more succinct API for your growing Kotlin code base.

To do this, you could start by converting this`Utils`class to Kotlin using the automatic conversion provided by the IDE. Example output might look similar to the following:  

    package com.java.project

    object StringUtils {

       fun foo(receiver: String): String {
           return receiver...;  // Transform the receiver in some way
       }

       fun bar(receiver: String): String {
           return receiver...;  // Transform the receiver in some way
       }

    }

Next, remove the class or object definition, prefix each function name with the type on which this function should apply, and use this to reference the type inside the function, as shown in the following example:  

    package com.java.project

    fun String.foo(): String {
        return this...;  // Transform the receiver in some way
    }

    fun String.bar(): String {
        return this...;  // Transform the receiver in some way
    }

Finally, add a`JvmName`annotation to the top of the source file to make the compiled name compatible with the rest of your app, as shown in the following example:  

    @file:JvmName("StringUtils")
    package com.java.project
    ...

The final version should look similar to the following:  

    @file:JvmName("StringUtils")
    package com.java.project

    fun String.foo(): String {
        return this...;  // Transform `this` string in some way
    }

    fun String.bar(): String {
        return this...;  // Transform `this` string in some way
    }

Note that these functions can now be called using Java or Kotlin with conventions that match each language.  

### Kotlin

```kotlin
...
val myString: String = ...
val fooString = myString.foo()
...
```

### Java

```java
...
String myString = ...
String fooString = StringUtils.foo(myString);
...
```

#### Complete the migration

Once your team is comfortable with Kotlin and you have migrated smaller areas, you can move on to tackling larger components such as fragments, activities,`ViewModel`objects, and other class that are related to business logic.

## Considerations

Much like Java has a specific style, Kotlin has its own idiomatic style that contributes to its succinctness. However, you might find initially that the Kotlin code your team produces looks more like the Java code it's replacing. This changes over time as your team's Kotlin experience grows. Remember, gradual change is the key to success.

Here are a few things you can do to attain consistency as your Kotlin code base grows:

### Common coding standards

Be sure to define a standard set of coding conventions early on in your adoption process. You can diverge from the Android[Kotlin style guide](https://developer.android.com/kotlin/style-guide)where it makes sense.

### Static analysis tools

Enforce the coding standards set for your team by using[Android lint](https://developer.android.com/studio/write/lint)and other static analysis tools.[klint](https://github.com/pinterest/ktlint), a third-party Kotlin linter, also provides additional rules for Kotlin.

### Continuous integration

Be sure to conform to common coding standards, and provide sufficient test coverage for your Kotlin code. Making this part of an automated build process can help to ensure consistency and adherence to these standards.

### Interoperability

Kotlin interoperates with Java seamlessly for the most part, but note the following.

#### Nullability

Kotlin relies on nullability annotations in compiled code to infer nullability on the Kotlin side. If annotations are not provided, Kotlin defaults to a platform type which can be treated as the nullable or non-nullable type. This can lead to runtime`NullPointerException`issues, however, if not treated carefully.

#### Adopt New Features

Kotlin provides a lot of[new libraries](https://kotlinlang.org/api/latest/jvm/stdlib/index.html)and syntactic sugar to reduce boilerplate, which helps to increase development speed. That said, be cautious and methodical when using Kotlin's standard library functions, such as[collection functions](https://kotlinlang.org/docs/reference/scope-functions.html#function-selection),[coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html), and[lambdas](https://kotlinlang.org/docs/reference/lambdas.html).

Here's a very common trap that newer Kotlin developers encounter. Assume the following Kotlin code:  

    val nullableFoo: Foo? = ...

    // This lambda executes only if nullableFoo is not null
    // and `foo` is of the non-nullable Foo type
    nullableFoo?.let { foo ->
       foo.baz()
       foo.zap()
    }

The intent in this example is to execute`foo.baz()`and`foo.zap()`if`nullableFoo`is not null, thus avoiding a`NullPointerException`. While this code works as expected, it's less intuitive to read than a simple null check and[smart cast](https://kotlinlang.org/docs/reference/typecasts.html#smart-casts), as shown in the following example:  

    val nullableFoo: Foo? = null
    if (nullableFoo != null) {
        nullableFoo.baz() // Using !! or ?. isn't required; the Kotlin compiler infers non-nullability
        nullableFoo.zap() // from guard condition; smart casts nullableFoo to Foo inside this block
    }

| **Note:** Smart casting works only for read-only class properties (like those declared as a`val`) and local function variables, as the Kotlin compiler can't otherwise guarantee the variable reference wasn't set back to`null`between the`if`guard and the variable's usage.

#### Testing

Classes and their functions are closed for extension by default in Kotlin. You must explicitly open the classes and functions that you want to subclass. This behavior is a language design decision that was chosen to promote composition over inheritance. Kotlin has built-in support to implement behavior through[delegation](https://kotlinlang.org/docs/reference/delegation.html)to help simplify composition.

This behavior poses a problem for mocking frameworks, such as Mockito, that rely on interface implementation or inheritance to override behaviors during testing. For unit tests, you can enable the use of the[Mock Maker Inline](https://github.com/mockito/mockito/wiki/What%27s-new-in-Mockito-2#mock-the-unmockable-opt-in-mocking-of-final-classesmethods)feature of Mockito, which allows you to mock final classes and methods. Alternatively, you can use the[All-Open compiler plugin](https://kotlinlang.org/docs/reference/compiler-plugins.html#all-open-compiler-plugin)to open any Kotlin class and its members that you want to test as part of the compilation process. The primary advantage to using this plugin is that it works with both unit and instrumented tests.

## More information

For more information on using Kotlin, check out the following links:

- [Android's Kotlin-first approach](https://developer.android.com/kotlin/first)
- [Resources for getting started with Kotlin](https://developer.android.com/kotlin/getting-started-resources)
- [Resources for Java users learning Kotlin](https://developer.android.com/kotlin/kotlin-java-resources)
- [Java to Kotlin learning pathway](https://developer.android.com/courses/pathways/kotlin-for-java), a collection of resources that help Java programmers learn and write idiomatic Kotlin.