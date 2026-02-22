---
title: https://developer.android.com/training/dependency-injection/dagger-basics
url: https://developer.android.com/training/dependency-injection/dagger-basics
source: md.txt
---

# Dagger basics

Manual dependency injection or service locators in an Android app can be problematic depending on the size of your project. You can limit your project's complexity as it scales up by using[Dagger](https://dagger.dev/)to manage dependencies.

Dagger automatically generates code that mimics the code you would otherwise have hand-written. Because the code is generated at compile time, it's traceable and more performant than other reflection-based solutions such as[Guice](https://en.wikipedia.org/wiki/Google_Guice).
| **Note:** Use[Hilt](https://developer.android.com/training/dependency-injection/hilt-android)for dependency injection on Android. Hilt is built on top of Dagger and it provides a standard way to incorporate Dagger dependency injection into an Android application.

## Benefits of using Dagger

Dagger frees you from writing tedious and error-prone boilerplate code by:

- Generating the`AppContainer`code (application graph) that you manually implemented in the manual DI section.

- Creating factories for the classes available in the application graph. This is how dependencies are satisfied internally.

- Deciding whether to reuse a dependency or create a new instance through the use of*scopes*.

- Creating containers for specific flows as you did with the login flow in the previous section using Dagger*subcomponents*. This improves your app's performance by releasing objects in memory when they're no longer needed.

Dagger automatically does all of this at build time as long as you declare dependencies of a class and specify how to satisfy them using annotations. Dagger generates code similar to what you would have written manually. Internally, Dagger creates a graph of objects that it can reference to find the way to provide an instance of a class. For every class in the graph, Dagger generates a[factory-type](https://en.wikipedia.org/wiki/Factory_method_pattern)class that it uses internally to get instances of that type.

At build time, Dagger walks through your code and:

- Builds and validates dependency graphs, ensuring that:

  - Every object's dependencies can be satisfied, so there are no runtime exceptions.
  - No dependency cycles exist, so there are no infinite loops.
- Generates the classes that are used at runtime to create the actual objects and their dependencies.

## A simple use case in Dagger: Generating a factory

To demonstrate how you can work with Dagger, let's create a simple[factory](https://en.wikipedia.org/wiki/Factory_method_pattern)for the`UserRepository`class shown in the following diagram:

![](https://developer.android.com/static/images/training/dependency-injection/3-factory-diagram.png)

Define`UserRepository`as follows:  

### Kotlin

```kotlin
class UserRepository(
    private val localDataSource: UserLocalDataSource,
    private val remoteDataSource: UserRemoteDataSource
) { ... }
```

### Java

```java
public class UserRepository {

    private final UserLocalDataSource userLocalDataSource;
    private final UserRemoteDataSource userRemoteDataSource;

    public UserRepository(UserLocalDataSource userLocalDataSource, UserRemoteDataSource userRemoteDataSource) {
        this.userLocalDataSource = userLocalDataSource;
        this.userRemoteDataSource = userRemoteDataSource;
    }

    ...
}
```

Add an`@Inject`annotation to the`UserRepository`constructor so Dagger knows how to create a`UserRepository`:  

### Kotlin

```kotlin
// @Inject lets Dagger know how to create instances of this object
class UserRepository @Inject constructor(
    private val localDataSource: UserLocalDataSource,
    private val remoteDataSource: UserRemoteDataSource
) { ... }
```

### Java

```java
public class UserRepository {

    private final UserLocalDataSource userLocalDataSource;
    private final UserRemoteDataSource userRemoteDataSource;

    // @Inject lets Dagger know how to create instances of this object
    @Inject
    public UserRepository(UserLocalDataSource userLocalDataSource, UserRemoteDataSource userRemoteDataSource) {
        this.userLocalDataSource = userLocalDataSource;
        this.userRemoteDataSource = userRemoteDataSource;
    }
}
```

In the above snippet of code, you're telling Dagger:

1. How to create a`UserRepository`instance with the`@Inject`annotated constructor.

2. What its dependencies are:`UserLocalDataSource`and`UserRemoteDataSource`.

Now Dagger knows how to create an instance of`UserRepository`, but it doesn't know how to create its dependencies. If you annotate the other classes too, Dagger knows how to create them:  

### Kotlin

```kotlin
// @Inject lets Dagger know how to create instances of these objects
class UserLocalDataSource @Inject constructor() { ... }
class UserRemoteDataSource @Inject constructor() { ... }
```

### Java

```java
public class UserLocalDataSource {
    @Inject
    public UserLocalDataSource() { }
}

public class UserRemoteDataSource {
    @Inject
    public UserRemoteDataSource() { }
}
```

## Dagger components

Dagger can create a graph of the dependencies in your project that it can use to find out where it should get those dependencies when they are needed. To make Dagger do this, you need to create an interface and annotate it with`@Component`. Dagger creates a container as you would have done with manual dependency injection.

Inside the`@Component`interface, you can define functions that return instances of the classes you need (i.e.`UserRepository`).`@Component`tells Dagger to generate a container with all the dependencies required to satisfy the types it exposes. This is called a*Dagger component*; it contains a graph that consists of the objects that Dagger knows how to provide and their respective dependencies.  

### Kotlin

```kotlin
// @Component makes Dagger create a graph of dependencies
@Component
interface ApplicationGraph {
    // The return type  of functions inside the component interface is
    // what can be provided from the container
    fun repository(): UserRepository
}
```

### Java

```java
// @Component makes Dagger create a graph of dependencies
@Component
public interface ApplicationGraph {
    // The return type  of functions inside the component interface is
    // what can be consumed from the graph
    UserRepository userRepository();
}
```

When you build the project, Dagger generates an implementation of the`ApplicationGraph`interface for you:`DaggerApplicationGraph`. With its annotation processor, Dagger creates a dependency graph that consists of the relationships between the three classes (`UserRepository`,`UserLocalDatasource`, and`UserRemoteDataSource`) with only one entry point: getting a`UserRepository`instance. You can use it as follows:  

### Kotlin

```kotlin
// Create an instance of the application graph
val applicationGraph: ApplicationGraph = DaggerApplicationGraph.create()
// Grab an instance of UserRepository from the application graph
val userRepository: UserRepository = applicationGraph.repository()
```

### Java

```java
// Create an instance of the application graph
ApplicationGraph applicationGraph = DaggerApplicationGraph.create();

// Grab an instance of UserRepository from the application graph
UserRepository userRepository = applicationGraph.userRepository();
```

Dagger creates a new instance of`UserRepository`every time it's requested.  

### Kotlin

```kotlin
val applicationGraph: ApplicationGraph = DaggerApplicationGraph.create()

val userRepository: UserRepository = applicationGraph.repository()
val userRepository2: UserRepository = applicationGraph.repository()

assert(userRepository != userRepository2)
```

### Java

```java
ApplicationGraph applicationGraph = DaggerApplicationGraph.create();

UserRepository userRepository = applicationGraph.userRepository();
UserRepository userRepository2 = applicationGraph.userRepository();

assert(userRepository != userRepository2)
```

Sometimes, you need to have a unique instance of a dependency in a container. You might want this for several reasons:

1. You want other types that have this type as a dependency to share the same instance, such as multiple`ViewModel`objects in the login flow using the same`LoginUserData`.

2. An object is expensive to create and you don't want to create a new instance every time it's declared as a dependency (for example, a JSON parser).

In the example, you might want to have a unique instance of`UserRepository`available in the graph so that every time you ask for a`UserRepository`, you always get the same instance. This is useful in your example because in a real-life application with a more complex application graph, you might have multiple`ViewModel`objects depending on`UserRepository`and you don't want to create new instances of`UserLocalDataSource`and`UserRemoteDataSource`every time`UserRepository`needs to be provided.

In manual dependency injection, you do this by passing in the same instance of`UserRepository`to the constructors of the ViewModel classes; but in Dagger, because you are not writing that code manually, you have to let Dagger know you want to use the same instance. This can be done with*scope annotations*.

### Scoping with Dagger

You can use scope annotations to limit the lifetime of an object to the lifetime of its component. This means that the same instance of a dependency is used every time that type needs to be provided.

To have a unique instance of a`UserRepository`when you ask for the repository in`ApplicationGraph`, use the same scope annotation for the`@Component`interface and`UserRepository`. You can use the`@Singleton`annotation that already comes with the`javax.inject`package that Dagger uses:  

### Kotlin

```kotlin
// Scope annotations on a @Component interface informs Dagger that classes annotated
// with this annotation (i.e. @Singleton) are bound to the life of the graph and so
// the same instance of that type is provided every time the type is requested.
@Singleton
@Component
interface ApplicationGraph {
    fun repository(): UserRepository
}

// Scope this class to a component using @Singleton scope (i.e. ApplicationGraph)
@Singleton
class UserRepository @Inject constructor(
    private val localDataSource: UserLocalDataSource,
    private val remoteDataSource: UserRemoteDataSource
) { ... }
```

### Java

```java
// Scope annotations on a @Component interface informs Dagger that classes annotated
// with this annotation (i.e. @Singleton) are scoped to the graph and the same
// instance of that type is provided every time the type is requested.
@Singleton
@Component
public interface ApplicationGraph {
    UserRepository userRepository();
}

// Scope this class to a component using @Singleton scope (i.e. ApplicationGraph)
@Singleton
public class UserRepository {

    private final UserLocalDataSource userLocalDataSource;
    private final UserRemoteDataSource userRemoteDataSource;

    @Inject
    public UserRepository(UserLocalDataSource userLocalDataSource, UserRemoteDataSource userRemoteDataSource) {
        this.userLocalDataSource = userLocalDataSource;
        this.userRemoteDataSource = userRemoteDataSource;
    }
}
```

Alternatively, you can create and use a custom scope annotation. You can create a scope annotation as follows:  

### Kotlin

```kotlin
// Creates MyCustomScope
@Scope
@MustBeDocumented
@Retention(value = AnnotationRetention.RUNTIME)
annotation class MyCustomScope
```

### Java

```java
// Creates MyCustomScope
@Scope
@Retention(RetentionPolicy.RUNTIME)
public @interface MyCustomScope {}
```

Then, you can use it as before:  

### Kotlin

```kotlin
@MyCustomScope
@Component
interface ApplicationGraph {
    fun repository(): UserRepository
}

@MyCustomScope
class UserRepository @Inject constructor(
    private val localDataSource: UserLocalDataSource,
    private val service: UserService
) { ... }
```

### Java

```java
@MyCustomScope
@Component
public interface ApplicationGraph {
    UserRepository userRepository();
}

@MyCustomScope
public class UserRepository {

    private final UserLocalDataSource userLocalDataSource;
    private final UserRemoteDataSource userRemoteDataSource;

    @Inject
    public UserRepository(UserLocalDataSource userLocalDataSource, UserRemoteDataSource userRemoteDataSource) {
        this.userLocalDataSource = userLocalDataSource;
        this.userRemoteDataSource = userRemoteDataSource;
    }
}
```

In both cases, the object is provided with the same scope used to annotate the`@Component`interface. Thus, every time you call`applicationGraph.repository()`, you get the same instance of`UserRepository`.  

### Kotlin

```kotlin
val applicationGraph: ApplicationGraph = DaggerApplicationGraph.create()

val userRepository: UserRepository = applicationGraph.repository()
val userRepository2: UserRepository = applicationGraph.repository()

assert(userRepository == userRepository2)
```

### Java

```java
ApplicationGraph applicationGraph = DaggerApplicationGraph.create();

UserRepository userRepository = applicationGraph.userRepository();
UserRepository userRepository2 = applicationGraph.userRepository();

assert(userRepository == userRepository2)
```

## Conclusion

It is important to be aware of Dagger's benefits and the basics of how it works before you can use it in more complicated scenarios.

In the[next page](https://developer.android.com/training/dependency-injection/dagger-android), you'll learn how to add Dagger to an Android application.