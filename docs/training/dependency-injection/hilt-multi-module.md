---
title: Hilt in multi-module apps  |  App architecture  |  Android Developers
url: https://developer.android.com/training/dependency-injection/hilt-multi-module
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Hilt in multi-module apps Stay organized with collections Save and categorize content based on your preferences.



Hilt code generation needs access to all the Gradle modules that use Hilt. The
Gradle module that compiles your
[`Application`](/reference/android/app/Application) class needs to have all Hilt
modules and constructor-injected classes in its transitive dependencies.

If your multi-module project is composed of regular Gradle modules, then you can
use Hilt as described in [Dependency injection with
Hilt](/training/dependency-injection/hilt-android). However, this is not the
case with apps that include [feature
modules](/guide/app-bundle/dynamic-delivery#customize_delivery).

**Note:** For deep multi-module projects, consider enabling the
`enableExperimentalClasspathAggregation` flag in your `build.gradle` file. Read
more about it in the [Hilt documentation](https://dagger.dev/hilt/gradle-setup#classpath-aggregation).

## Hilt in feature modules

In feature modules, the way that modules usually depend on each other is inverted.
Therefore, Hilt cannot process annotations in feature modules. You must
use [Dagger](/training/dependency-injection/dagger-basics) to perform
dependency injection in your feature modules.

You must use component dependencies to solve this problem with feature modules. Follow
these steps:

1. Declare an
   [`@EntryPoint` interface](/training/dependency-injection/hilt-android#not-supported)
   in the `app` module (or in any other module that can be processed by Hilt)
   with the dependencies that the feature module needs.
2. Create a Dagger component that depends on the `@EntryPoint` interface.
3. Use Dagger as usual in the feature module.

Consider the example from the [Dependency injection with
Hilt](/training/dependency-injection/hilt-android) page. Suppose you add a
`login` feature module to your project. You implement the login feature
with an activity called `LoginActivity`. This means that you can get bindings
only from the application component.

For this feature, you need an `OkHttpClient` with the `authInterceptor` binding.

First, create an `@EntryPoint` interface installed in the `SingletonComponent`
with the bindings that the `login` module needs:

### Kotlin

```
// LoginModuleDependencies.kt - File in the app module.

@EntryPoint
@InstallIn(SingletonComponent::class)
interface LoginModuleDependencies {

  @AuthInterceptorOkHttpClient
  fun okHttpClient(): OkHttpClient
}
```

### Java

```
// LoginModuleDependencies.java - File in the app module.

@EntryPoint
@InstallIn(SingletonComponent.class)
public interface LoginModuleDependencies {

  @AuthInterceptorOkHttpClient
  OkHttpClient okHttpClient();
}
```

To perform field injection in the `LoginActivity`, create a Dagger
component that depends on the `@EntryPoint` interface:

### Kotlin

```
// LoginComponent.kt - File in the login module.

@Component(dependencies = [LoginModuleDependencies::class])
interface LoginComponent {

  fun inject(activity: LoginActivity)

  @Component.Builder
  interface Builder {
    fun context(@BindsInstance context: Context): Builder
    fun appDependencies(loginModuleDependencies: LoginModuleDependencies): Builder
    fun build(): LoginComponent
  }
}
```

### Java

```
// LoginComponent.java - File in the login module.

@Component(dependencies = LoginModuleDependencies.class)
public interface LoginComponent {

  void inject(LoginActivity loginActivity);

  @Component.Builder
  interface Builder {
    Builder context(@BindsInstance Context context);
    Builder appDependencies(LoginModuleDependencies loginModuleDependencies);
    LoginComponent build();
  }
}
```

Once those steps are complete, use Dagger as usual in your feature module. For
example, you can use the bindings from the `SingletonComponent` as a
dependency of a class:

### Kotlin

```
// LoginAnalyticsAdapter.kt - File in the login module.

class LoginAnalyticsAdapter @Inject constructor(
  @AuthInterceptorOkHttpClient okHttpClient: OkHttpClient
) { ... }
```

### Java

```
// LoginAnalyticsAdapter.java - File in the login module.

public class LoginAnalyticsAdapter {

  private final OkHttpClient okHttpClient;

  @Inject
  LoginAnalyticsAdapter(
    @AuthInterceptorOkHttpClient OkHttpClient okHttpClient
  ) {
    this.okHttpClient = okHttpClient;
  }
  ...
}
```

To perform field injection, create an instance of the Dagger component
using the `applicationContext` to get the `SingletonComponent` dependencies:

### Kotlin

```
// LoginActivity.kt - File in the login module.

class LoginActivity : AppCompatActivity() {

  @Inject
  lateinit var loginAnalyticsAdapter: LoginAnalyticsAdapter

  override fun onCreate(savedInstanceState: Bundle?) {
    DaggerLoginComponent.builder()
        .context(this)
        .appDependencies(
          EntryPointAccessors.fromApplication(
            applicationContext,
            LoginModuleDependencies::class.java
          )
        )
        .build()
        .inject(this)

    super.onCreate(savedInstanceState)
    ...
  }
}
```

### Java

```
// LoginActivity.java - File in the login module.

public class LoginActivity extends AppCompatActivity {

  @Inject
  LoginAnalyticsAdapter loginAnalyticsAdapter;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    DaggerLoginComponent.builder()
        .context(this)
        .appDependencies(
          EntryPointAccessors.fromApplication(
            getApplicationContext(),
            LoginModuleDependencies.class
          )
        )
        .build()
        .inject(this);

    super.onCreate(savedInstanceState);
    ...
  }
}
```

For more context on module dependencies in feature modules, see
[Component dependencies with feature
modules](/training/dependency-injection/dagger-multi-module#dagger-dfm).

For more information about Dagger on Android, see [Using Dagger in Android
apps](/training/dependency-injection/dagger-android).