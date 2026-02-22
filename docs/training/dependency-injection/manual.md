---
title: https://developer.android.com/training/dependency-injection/manual
url: https://developer.android.com/training/dependency-injection/manual
source: md.txt
---

# Manual dependency injection

[Android's recommended app architecture](https://developer.android.com/jetpack/docs/guide#recommended-app-arch)encourages dividing your code into classes to benefit from separation of concerns, a principle where each class of the hierarchy has a single defined responsibility. This leads to more, smaller classes that need to be connected together to fulfill each other's dependencies.  
![Android apps are usually made up of many classes, and some of them depend on each other.](https://developer.android.com/static/topic/libraries/architecture/images/final-architecture.png)**Figure 1.**A model of an Android app's application graph

The dependencies between classes can be represented as a graph, in which each class is connected to the classes it depends on. The representation of all your classes and their dependencies makes up the*application graph* . In figure 1, you can see an abstraction of the application graph. When class A (`ViewModel`) depends on class B (`Repository`), there's a line that points from A to B representing that dependency.

Dependency injection helps make these connections and enables you to swap out implementations for testing. For example, when testing a`ViewModel`that depends on a repository, you can pass different implementations of`Repository`with either fakes or mocks to test the different cases.

## Basics of manual dependency injection

This section covers how to apply manual dependency injection in a real Android app scenario. It walks through an iterated approach of how you might start using dependency injection in your app. The approach improves until it reaches a point that is very similar to what Dagger would automatically generate for you. For more information about Dagger, read[Dagger basics](https://developer.android.com/training/dependency-injection/dagger-basics).

Consider a**flow**to be a group of screens in your app that correspond to a feature. Login, registration, and checkout are all examples of flows.

When covering a login flow for a typical Android app, the`LoginActivity`depends on`LoginViewModel`, which in turn depends on`UserRepository`. Then`UserRepository`depends on a`UserLocalDataSource`and a`UserRemoteDataSource`, which in turn depends on a[`Retrofit`](https://square.github.io/retrofit/)service.  
![](https://developer.android.com/static/images/training/dependency-injection/2-application-graph.png)

`LoginActivity`is the entry point to the login flow and the user interacts with the activity. Thus,`LoginActivity`needs to create the`LoginViewModel`with all its dependencies.

The`Repository`and`DataSource`classes of the flow look like this:  

### Kotlin

```kotlin
class UserRepository(
    private val localDataSource: UserLocalDataSource,
    private val remoteDataSource: UserRemoteDataSource
) { ... }

class UserLocalDataSource { ... }
class UserRemoteDataSource(
    private val loginService: LoginRetrofitService
) { ... }
```

### Java

```java
class UserLocalDataSource {
    public UserLocalDataSource() { }
    ...
}

class UserRemoteDataSource {

    private final Retrofit retrofit;

    public UserRemoteDataSource(Retrofit retrofit) {
        this.retrofit = retrofit;
    }

    ...
}

class UserRepository {

    private final UserLocalDataSource userLocalDataSource;
    private final UserRemoteDataSource userRemoteDataSource;

    public UserRepository(UserLocalDataSource userLocalDataSource, UserRemoteDataSource userRemoteDataSource) {
        this.userLocalDataSource = userLocalDataSource;
        this.userRemoteDataSource = userRemoteDataSource;
    }

    ...
}
```

Here's what`LoginActivity`looks like:  

### Kotlin

```kotlin
class LoginActivity: Activity() {

    private lateinit var loginViewModel: LoginViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // In order to satisfy the dependencies of LoginViewModel, you have to also
        // satisfy the dependencies of all of its dependencies recursively.
        // First, create retrofit which is the dependency of UserRemoteDataSource
        val retrofit = Retrofit.Builder()
            .baseUrl("https://example.com")
            .build()
            .create(LoginService::class.java)

        // Then, satisfy the dependencies of UserRepository
        val remoteDataSource = UserRemoteDataSource(retrofit)
        val localDataSource = UserLocalDataSource()

        // Now you can create an instance of UserRepository that LoginViewModel needs
        val userRepository = UserRepository(localDataSource, remoteDataSource)

        // Lastly, create an instance of LoginViewModel with userRepository
        loginViewModel = LoginViewModel(userRepository)
    }
}
```

### Java

```java
public class MainActivity extends Activity {

    private LoginViewModel loginViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // In order to satisfy the dependencies of LoginViewModel, you have to also
        // satisfy the dependencies of all of its dependencies recursively.
        // First, create retrofit which is the dependency of UserRemoteDataSource
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("https://example.com")
                .build()
                .create(LoginService.class);

        // Then, satisfy the dependencies of UserRepository
        UserRemoteDataSource remoteDataSource = new UserRemoteDataSource(retrofit);
        UserLocalDataSource localDataSource = new UserLocalDataSource();

        // Now you can create an instance of UserRepository that LoginViewModel needs
        UserRepository userRepository = new UserRepository(localDataSource, remoteDataSource);

        // Lastly, create an instance of LoginViewModel with userRepository
        loginViewModel = new LoginViewModel(userRepository);
    }
}
```

There are issues with this approach:

1. There's a lot of boilerplate code. If you wanted to create another instance of`LoginViewModel`in another part of the code, you'd have code duplication.

2. Dependencies have to be declared in order. You have to instantiate`UserRepository`before`LoginViewModel`in order to create it.

3. It's difficult to reuse objects. If you wanted to reuse`UserRepository`across multiple features, you'd have to make it follow the[singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern). The singleton pattern makes testing more difficult because all tests share the same singleton instance.

## Managing dependencies with a container

To solve the issue of reusing objects, you can create your own*dependencies container* class that you use to get dependencies. All instances provided by this container can be public. In the example, because you only need an instance of`UserRepository`, you can make its dependencies private with the option of making them public in the future if they need to be provided:  

### Kotlin

```kotlin
// Container of objects shared across the whole app
class AppContainer {

    // Since you want to expose userRepository out of the container, you need to satisfy
    // its dependencies as you did before
    private val retrofit = Retrofit.Builder()
                            .baseUrl("https://example.com")
                            .build()
                            .create(LoginService::class.java)

    private val remoteDataSource = UserRemoteDataSource(retrofit)
    private val localDataSource = UserLocalDataSource()

    // userRepository is not private; it'll be exposed
    val userRepository = UserRepository(localDataSource, remoteDataSource)
}
```

### Java

```java
// Container of objects shared across the whole app
public class AppContainer {

    // Since you want to expose userRepository out of the container, you need to satisfy
    // its dependencies as you did before
    private Retrofit retrofit = new Retrofit.Builder()
            .baseUrl("https://example.com")
            .build()
            .create(LoginService.class);

    private UserRemoteDataSource remoteDataSource = new UserRemoteDataSource(retrofit);
    private UserLocalDataSource localDataSource = new UserLocalDataSource();

    // userRepository is not private; it'll be exposed
    public UserRepository userRepository = new UserRepository(localDataSource, remoteDataSource);
}
```

Because these dependencies are used across the whole application, they need to be placed in a common place all activities can use: the[`Application`](https://developer.android.com/reference/android/app/Application)class. Create a custom`Application`class that contains an`AppContainer`instance.  

### Kotlin

```kotlin
// Custom Application class that needs to be specified
// in the AndroidManifest.xml file
class MyApplication : Application() {

    // Instance of AppContainer that will be used by all the Activities of the app
    val appContainer = AppContainer()
}
```

### Java

```java
// Custom Application class that needs to be specified
// in the AndroidManifest.xml file
public class MyApplication extends Application {

    // Instance of AppContainer that will be used by all the Activities of the app
    public AppContainer appContainer = new AppContainer();
}
```
| **Note:** `AppContainer`is just a regular class with a unique instance shared across the app placed in your`Application`class. However,`AppContainer`is not following the[singleton](https://en.wikipedia.org/wiki/Singleton_pattern)pattern; in Kotlin, it's not an`object`, and in Java, it's not accessed with the typical`Singleton.getInstance()`method.

Now you can get the instance of the`AppContainer`from the application and obtain the shared`UserRepository`instance:  

### Kotlin

```kotlin
class LoginActivity: Activity() {

    private lateinit var loginViewModel: LoginViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Gets userRepository from the instance of AppContainer in Application
        val appContainer = (application as MyApplication).appContainer
        loginViewModel = LoginViewModel(appContainer.userRepository)
    }
}
```

### Java

```java
public class MainActivity extends Activity {

    private LoginViewModel loginViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Gets userRepository from the instance of AppContainer in Application
        AppContainer appContainer = ((MyApplication) getApplication()).appContainer;
        loginViewModel = new LoginViewModel(appContainer.userRepository);
    }
}
```

In this way, you don't have a singleton`UserRepository`. Instead, you have an`AppContainer`shared across all activities that contains objects from the graph and creates instances of those objects that other classes can consume.

If`LoginViewModel`is needed in more places in the application, having a centralized place where you create instances of`LoginViewModel`makes sense. You can move the creation of`LoginViewModel`to the container and provide new objects of that type with a factory. The code for a`LoginViewModelFactory`looks like this:  

### Kotlin

```kotlin
// Definition of a Factory interface with a function to create objects of a type
interface Factory<T> {
    fun create(): T
}

// Factory for LoginViewModel.
// Since LoginViewModel depends on UserRepository, in order to create instances of
// LoginViewModel, you need an instance of UserRepository that you pass as a parameter.
class LoginViewModelFactory(private val userRepository: UserRepository) : Factory {
    override fun create(): LoginViewModel {
        return LoginViewModel(userRepository)
    }
}
```

### Java

```java
// Definition of a Factory interface with a function to create objects of a type
public interface Factory<T> {
    T create();
}

// Factory for LoginViewModel.
// Since LoginViewModel depends on UserRepository, in order to create instances of
// LoginViewModel, you need an instance of UserRepository that you pass as a parameter.
class LoginViewModelFactory implements Factory {

    private final UserRepository userRepository;

    public LoginViewModelFactory(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public LoginViewModel create() {
        return new LoginViewModel(userRepository);
    }
}
```

You can include the`LoginViewModelFactory`in the`AppContainer`and make the`LoginActivity`consume it:  

### Kotlin

```kotlin
// AppContainer can now provide instances of LoginViewModel with LoginViewModelFactory
class AppContainer {
    ...
    val userRepository = UserRepository(localDataSource, remoteDataSource)

    val loginViewModelFactory = LoginViewModelFactory(userRepository)
}

class LoginActivity: Activity() {

    private lateinit var loginViewModel: LoginViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Gets LoginViewModelFactory from the application instance of AppContainer
        // to create a new LoginViewModel instance
        val appContainer = (application as MyApplication).appContainer
        loginViewModel = appContainer.loginViewModelFactory.create()
    }
}
```

### Java

```java
// AppContainer can now provide instances of LoginViewModel with LoginViewModelFactory
public class AppContainer {
    ...

    public UserRepository userRepository = new UserRepository(localDataSource, remoteDataSource);

    public LoginViewModelFactory loginViewModelFactory = new LoginViewModelFactory(userRepository);
}

public class MainActivity extends Activity {

    private LoginViewModel loginViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Gets LoginViewModelFactory from the application instance of AppContainer
        // to create a new LoginViewModel instance
        AppContainer appContainer = ((MyApplication) getApplication()).appContainer;
        loginViewModel = appContainer.loginViewModelFactory.create();
    }
}
```

This approach is better than the previous one, but there are still some challenges to consider:

1. You have to manage`AppContainer`yourself, creating instances for all dependencies by hand.

2. There is still a lot of boilerplate code. You need to create factories or parameters by hand depending on whether you want to reuse an object or not.

## Managing dependencies in application flows

`AppContainer`gets complicated when you want to include more functionality in the project. When your app becomes larger and you start introducing different feature flows, there are even more problems that arise:

1. When you have different flows, you might want objects to just live in the scope of that flow. For example, when creating`LoginUserData`(that might consist of the username and password used only in the login flow) you don't want to persist data from an old login flow from a different user. You want a new instance for every new flow. You can achieve that by creating`FlowContainer`objects inside the`AppContainer`as demonstrated in the next code example.

2. Optimizing the application graph and flow containers can also be difficult. You need to remember to delete instances that you don't need, depending on the flow you're in.

Imagine you have a login flow that consists of one activity (`LoginActivity`) and multiple fragments (`LoginUsernameFragment`and`LoginPasswordFragment`). These views want to:

1. Access the same`LoginUserData`instance that needs to be shared until the login flow finishes.

2. Create a new instance of`LoginUserData`when the flow starts again.

You can achieve that with a login flow container. This container needs to be created when the login flow starts and removed from memory when the flow ends.

Let's add a`LoginContainer`to the example code. You want to be able to create multiple instances of`LoginContainer`in the app, so instead of making it a singleton, make it a class with the dependencies the login flow needs from the`AppContainer`.  

### Kotlin

```kotlin
class LoginContainer(val userRepository: UserRepository) {

    val loginData = LoginUserData()

    val loginViewModelFactory = LoginViewModelFactory(userRepository)
}

// AppContainer contains LoginContainer now
class AppContainer {
    ...
    val userRepository = UserRepository(localDataSource, remoteDataSource)

    // LoginContainer will be null when the user is NOT in the login flow
    var loginContainer: LoginContainer? = null
}
```

### Java

```java
// Container with Login-specific dependencies
class LoginContainer {

    private final UserRepository userRepository;

    public LoginContainer(UserRepository userRepository) {
        this.userRepository = userRepository;
        loginViewModelFactory = new LoginViewModelFactory(userRepository);
    }

    public LoginUserData loginData = new LoginUserData();

    public LoginViewModelFactory loginViewModelFactory;
}

// AppContainer contains LoginContainer now
public class AppContainer {
    ...
    public UserRepository userRepository = new UserRepository(localDataSource, remoteDataSource);

    // LoginContainer will be null when the user is NOT in the login flow
    public LoginContainer loginContainer;
}
```

Once you have a container specific to a flow, you have to decide when to create and delete the container instance. Because your login flow is self-contained in an activity (`LoginActivity`), the activity is the one managing the lifecycle of that container.`LoginActivity`can create the instance in`onCreate()`and delete it in`onDestroy()`.  

### Kotlin

```kotlin
class LoginActivity: Activity() {

    private lateinit var loginViewModel: LoginViewModel
    private lateinit var loginData: LoginUserData
    private lateinit var appContainer: AppContainer


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        appContainer = (application as MyApplication).appContainer

        // Login flow has started. Populate loginContainer in AppContainer
        appContainer.loginContainer = LoginContainer(appContainer.userRepository)

        loginViewModel = appContainer.loginContainer.loginViewModelFactory.create()
        loginData = appContainer.loginContainer.loginData
    }

    override fun onDestroy() {
        // Login flow is finishing
        // Removing the instance of loginContainer in the AppContainer
        appContainer.loginContainer = null
        super.onDestroy()
    }
}
```

### Java

```java
public class LoginActivity extends Activity {

    private LoginViewModel loginViewModel;
    private LoginData loginData;
    private AppContainer appContainer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        appContainer = ((MyApplication) getApplication()).appContainer;

        // Login flow has started. Populate loginContainer in AppContainer
        appContainer.loginContainer = new LoginContainer(appContainer.userRepository);

        loginViewModel = appContainer.loginContainer.loginViewModelFactory.create();
        loginData = appContainer.loginContainer.loginData;
    }

    @Override
    protected void onDestroy() {
        // Login flow is finishing
        // Removing the instance of loginContainer in the AppContainer
        appContainer.loginContainer = null;

        super.onDestroy();
    }
}
```

Like`LoginActivity`, login fragments can access the`LoginContainer`from`AppContainer`and use the shared`LoginUserData`instance.

Because in this case you're dealing with view lifecycle logic, using[lifecycle observation](https://developer.android.com/topic/libraries/architecture/lifecycle)makes sense.
| **Note:** If you need the container to survive configuration changes, follow the[Saving UI States guide](https://developer.android.com/topic/libraries/architecture/saving-states). You need to handle it the same way you handle process death; otherwise, your app might lose state on devices with less memory.

## Conclusion

Dependency injection is a good technique for creating scalable and testable Android apps. Use containers as a way to share instances of classes in different parts of your app and as a centralized place to create instances of classes using factories.

When your application gets larger, you will start seeing that you write a lot of boilerplate code (such as factories), which can be error-prone. You also have to manage the scope and lifecycle of the containers yourself, optimizing and discarding containers that are no longer needed in order to free up memory. Doing this incorrectly can lead to subtle bugs and memory leaks in your app.

In the[Dagger section](https://developer.android.com/training/dependency-injection/dagger-basics), you'll learn how you can use Dagger to automate this process and generate the same code you would have written by hand otherwise.