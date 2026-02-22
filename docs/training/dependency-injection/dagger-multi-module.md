---
title: https://developer.android.com/training/dependency-injection/dagger-multi-module
url: https://developer.android.com/training/dependency-injection/dagger-multi-module
source: md.txt
---

# Using Dagger in multi-module apps

| **Note:** In this page, references to modules refer to Gradle modules and not to Dagger modules.

A project with multiple Gradle modules is known as a multi-module project. In a multi-module project that ships as a single APK with no feature modules, it's common to have an`app`module that can depend on most modules of your project and a`base`or`core`module that the rest of the modules usually depend on. The`app`module typically contains your[`Application`](https://developer.android.com/reference/android/app/Application)class, whereas the`base`module contains all common classes shared across all modules in your project.

The`app`module is a good place to declare your application component (for example,`ApplicationComponent`in the image below) that can provide objects that other components might need as well as the singletons of your app. As an example, classes like`OkHttpClient`, JSON parsers, accessors for your database, or`SharedPreferences`objects that may be defined in the`core`module, will be provided by the`ApplicationComponent`defined in the`app`module.

In the`app`module, you could also have other components with shorter lifespans. An example could be a`UserComponent`with user-specific configuration (like a`UserSession`) after a log in.

In the different modules of your project, you can define at least one subcomponent that has logic specific to that module as seen in figure 1.  
![](https://developer.android.com/static/images/training/dependency-injection/5-graph-modules.png)

**Figure 1.**Example of a Dagger graph in a multi-module project

For example, in a`login`module, you could have a`LoginComponent`scoped with a custom`@ModuleScope`annotation that can provide objects common to that feature such as a`LoginRepository`. Inside that module, you can also have other components that depend on a`LoginComponent`with a different custom scope, for example`@FeatureScope`for a`LoginActivityComponent`or a`TermsAndConditionsComponent`where you can scope more feature-specific logic such as`ViewModel`objects.

For other modules such as`Registration`, you would have a similar setup.

A general rule for a multi-module project is that modules of the same level shouldn't depend on each other. If they do, consider whether that shared logic (the dependencies between them) should be part of the parent module. If so, refactor to move the classes to the parent module; if not, create a new module that extends the parent module and have both of the original modules extend the new module.

As a best practice, you would generally create a component in a module in the following cases:

- You need to perform field injection, as with`LoginActivityComponent`.

- You need to scope objects, as with`LoginComponent`.

If neither of these casses apply and you need to tell Dagger how to provide objects from that module, create and expose a Dagger module with`@Provides`or`@Binds`methods if construction injection is not possible for those classes.

## Implementation with Dagger subcomponents

The[Using Dagger in Android apps](https://developer.android.com/training/dependency-injection/dagger-android#dagger-subcomponents)doc page covers how to create and use subcomponents. However, you cannot use the same code because feature modules don't know about the`app`module. As an example, if you think about a typical Login flow and the code we have in the previous page, it doesn't compile any more:  

### Kotlin

```kotlin
class LoginActivity: Activity() {
  ...

  override fun onCreate(savedInstanceState: Bundle?) {
    // Creation of the login graph using the application graph
    loginComponent = (applicationContext as MyDaggerApplication)
                        .appComponent.loginComponent().create()

    // Make Dagger instantiate @Inject fields in LoginActivity
    loginComponent.inject(this)
    ...
  }
}
```

### Java

```java
public class LoginActivity extends Activity {
    ...

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Creation of the login graph using the application graph
        loginComponent = ((MyApplication) getApplicationContext())
                                .appComponent.loginComponent().create();

        // Make Dagger instantiate @Inject fields in LoginActivity
        loginComponent.inject(this);

        ...
    }
}
```

The reason is that the`login`module doesn't know about`MyApplication`nor`appComponent`. To make it work, you need to define an interface in the feature module that provides a`FeatureComponent`that`MyApplication`needs to implement.

In the following example, you can define a`LoginComponentProvider`interface that provides a`LoginComponent`in the`login`module for the Login flow:  

### Kotlin

```kotlin
interface LoginComponentProvider {
    fun provideLoginComponent(): LoginComponent
}
```

### Java

```java
public interface LoginComponentProvider {
   public LoginComponent provideLoginComponent();
}
```

Now, the`LoginActivity`will use that interface instead of the snippet of code defined above:  

### Kotlin

```kotlin
class LoginActivity: Activity() {
  ...

  override fun onCreate(savedInstanceState: Bundle?) {
    loginComponent = (applicationContext as LoginComponentProvider)
                        .provideLoginComponent()

    loginComponent.inject(this)
    ...
  }
}
```

### Java

```java
public class LoginActivity extends Activity {
    ...

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        loginComponent = ((LoginComponentProvider) getApplicationContext())
                                .provideLoginComponent();

        loginComponent.inject(this);

        ...
    }
}
```

Now,`MyApplication`needs to implement that interface and implement the required methods:  

### Kotlin

```kotlin
class MyApplication: Application(), LoginComponentProvider {
  // Reference to the application graph that is used across the whole app
  val appComponent = DaggerApplicationComponent.create()

  override fun provideLoginComponent(): LoginComponent {
    return appComponent.loginComponent().create()
  }
}
```

### Java

```java
public class MyApplication extends Application implements LoginComponentProvider {
  // Reference to the application graph that is used across the whole app
  ApplicationComponent appComponent = DaggerApplicationComponent.create();

  @Override
  public LoginComponent provideLoginComponent() {
    return appComponent.loginComponent.create();
  }
}
```

This is how you can use Dagger subcomponents in a multi-module project. With feature modules, the solution is different due to the way modules depend on each other.

## Component dependencies with feature modules

With[feature modules](https://developer.android.com/studio/projects/dynamic-delivery#customize_delivery), the way modules usually depend on each other is inverted. Instead of the`app`module including feature modules, the feature modules depend on the`app`module. See figure 2 for a representation of how modules are structured.  
![](https://developer.android.com/static/images/training/dependency-injection/5-graph-dynamic-modules.png)

**Figure 2.**Example of a Dagger graph in a project with feature modules

In Dagger, components need to know about their subcomponents. This information is included in a Dagger module added to the parent component (like the`SubcomponentsModule`module in[Using Dagger in Android apps](https://developer.android.com/training/dependency-injection/dagger-android#dagger-subcomponents)).

Unfortunately, with the reversed dependency between the app and the feature module, the subcomponent is not visible from the`app`module because it's not in the build path. As an example, a`LoginComponent`defined in a`login`feature module cannot be a subcomponent of the`ApplicationComponent`defined in the`app`module.

Dagger has a mechanism called**component dependencies** that you can use to solve this issue. Instead of the child component being a subcomponent of the parent component, the child component is dependent on the parent component. With that, there is no parent-child relationship; now**components** depend on others to get certain**dependencies**. Components need to expose types from the graph for dependent components to consume them.
| **Note:** This issue happens whenever you want to create a subcomponent of`ApplicationComponent`. If you need to create a regular gradle module that depends on a feature module and needs to create a component that depends on a component defined in that feature module, you can use subcomponents as usual.

For example: a feature module called`login`wants to build a`LoginComponent`that depends on the`AppComponent`available in the`app`Gradle module.

Below are definitions for the classes and the`AppComponent`that are part of the`app`Gradle module:  

### Kotlin

```kotlin
// UserRepository's dependencies
class UserLocalDataSource @Inject constructor() { ... }
class UserRemoteDataSource @Inject constructor() { ... }

// UserRepository is scoped to AppComponent
@Singleton
class UserRepository @Inject constructor(
    private val localDataSource: UserLocalDataSource,
    private val remoteDataSource: UserRemoteDataSource
) { ... }

@Singleton
@Component
interface AppComponent { ... }
```

### Java

```java
// UserRepository's dependencies
public class UserLocalDataSource {

    @Inject
    public UserLocalDataSource() {}
}

public class UserRemoteDataSource {

    @Inject
    public UserRemoteDataSource() { }
}

// UserRepository is scoped to AppComponent
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

@Singleton
@Component
public interface ApplicationComponent { ... }
```

In your`login`gradle module that includes the`app`gradle module, you have a`LoginActivity`that needs a`LoginViewModel`instance to be injected:  

### Kotlin

```kotlin
// LoginViewModel depends on UserRepository that is scoped to AppComponent
class LoginViewModel @Inject constructor(
    private val userRepository: UserRepository
) { ... }
```

### Java

```java
// LoginViewModel depends on UserRepository that is scoped to AppComponent
public class LoginViewModel {

    private final UserRepository userRepository;

    @Inject
    public LoginViewModel(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

`LoginViewModel`has a dependency on`UserRepository`that is available and scoped to`AppComponent`. Let's create a`LoginComponent`that depends on`AppComponent`to inject`LoginActivity`:  

### Kotlin

```kotlin
// Use the dependencies attribute in the Component annotation to specify the
// dependencies of this Component
@Component(dependencies = [AppComponent::class])
interface LoginComponent {
    fun inject(activity: LoginActivity)
}
```

### Java

```java
// Use the dependencies attribute in the Component annotation to specify the
// dependencies of this Component
@Component(dependencies = AppComponent.class)
public interface LoginComponent {

    void inject(LoginActivity loginActivity);
}
```

`LoginComponent`specifies a dependency on`AppComponent`by adding it to the dependencies parameter of the component annotation. Because`LoginActivity`will be injected by Dagger, add the`inject()`method to the interface.
| **Note:** `LoginComponent`is annotated with`@Component`and not with`@Subcomponent`as you did in the[Using Dagger in an Android app page](https://developer.android.com/training/dependency-injection/dagger-android#dagger-subcomponents).

When creating a`LoginComponent`, an instance of`AppComponent`needs to be passed in. Use the component factory to do it:  

### Kotlin

```kotlin
@Component(dependencies = [AppComponent::class])
interface LoginComponent {

    @Component.Factory
    interface Factory {
        // Takes an instance of AppComponent when creating
        // an instance of LoginComponent
        fun create(appComponent: AppComponent): LoginComponent
    }

    fun inject(activity: LoginActivity)
}
```

### Java

```java
@Component(dependencies = AppComponent.class)
public interface LoginComponent {

    @Component.Factory
    interface Factory {
        // Takes an instance of AppComponent when creating
        // an instance of LoginComponent
        LoginComponent create(AppComponent appComponent);
    }

    void inject(LoginActivity loginActivity);
}
```

Now,`LoginActivity`can create an instance of`LoginComponent`and call the`inject()`method.  

### Kotlin

```kotlin
class LoginActivity: Activity() {

    // You want Dagger to provide an instance of LoginViewModel from the Login graph
    @Inject lateinit var loginViewModel: LoginViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        // Gets appComponent from MyApplication available in the base Gradle module
        val appComponent = (applicationContext as MyApplication).appComponent

        // Creates a new instance of LoginComponent
        // Injects the component to populate the @Inject fields
        DaggerLoginComponent.factory().create(appComponent).inject(this)

        super.onCreate(savedInstanceState)

        // Now you can access loginViewModel
    }
}
```

### Java

```java
public class LoginActivity extends Activity {

    // You want Dagger to provide an instance of LoginViewModel from the Login graph
    @Inject
    LoginViewModel loginViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Gets appComponent from MyApplication available in the base Gradle module
        AppComponent appComponent = ((MyApplication) getApplicationContext()).appComponent;

        // Creates a new instance of LoginComponent
        // Injects the component to populate the @Inject fields
        DaggerLoginComponent.factory().create(appComponent).inject(this);

        // Now you can access loginViewModel
    }
}
```

`LoginViewModel`depends on`UserRepository`; and for`LoginComponent`to be able to access it from`AppComponent`,`AppComponent`needs to expose it in its interface:  

### Kotlin

```kotlin
@Singleton
@Component
interface AppComponent {
    fun userRepository(): UserRepository
}
```

### Java

```java
@Singleton
@Component
public interface AppComponent {
    UserRepository userRepository();
}
```

The scoping rules with dependent components work in the same way as with subcomponents. Because`LoginComponent`uses an instance of`AppComponent`, they cannot use the same scope annotation.

If you wanted to scope`LoginViewModel`to`LoginComponent`, you would do it as you did previously using the custom`@ActivityScope`annotation.  

### Kotlin

```kotlin
@ActivityScope
@Component(dependencies = [AppComponent::class])
interface LoginComponent { ... }

@ActivityScope
class LoginViewModel @Inject constructor(
    private val userRepository: UserRepository
) { ... }
```

### Java

```java
@ActivityScope
@Component(dependencies = AppComponent.class)
public interface LoginComponent { ... }

@ActivityScope
public class LoginViewModel {

    private final UserRepository userRepository;

    @Inject
    public LoginViewModel(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```
| **Note:** Not exposing all the types that a dependent component needs from a component will result in a Dagger compile time error because it cannot provide certain types for the dependent component.

## Best practices

- The`ApplicationComponent`should always be in the`app`module.

- Create Dagger components in modules if you need to perform field injection in that module or you need to scope objects for a specific flow of your application.

- For Gradle modules that are meant to be utilities or helpers and don't need to build a graph (that's why you'd need a Dagger component), create and expose public Dagger modules with @Provides and @Binds methods of those classes that don't support constructor injection.

- To use Dagger in an Android app with feature modules, use component dependencies to be able to access dependencies provided by the`ApplicationComponent`defined in the`app`module.