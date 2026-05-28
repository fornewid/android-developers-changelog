---
title: https://developer.android.com/develop/connectivity/network-ops/connecting
url: https://developer.android.com/develop/connectivity/network-ops/connecting
source: md.txt
---

To perform network operations in your application, your manifest must include
the following permissions:

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

> [!NOTE]
> **Note:** Both the [`INTERNET`](https://developer.android.com/reference/android/Manifest.permission#INTERNET) and [`ACCESS_NETWORK_STATE`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE) permissions are [normal
> permissions](https://developer.android.com/develop/permissions/overview#normal-dangerous), which means they're granted at install time and don't need to be [requested at runtime](https://developer.android.com/training/permissions/requesting).

## Best practices for secure network communication

Before you add networking functionality to your app, you need to ensure that
data and information within your app stay safe when you are transmitting over a
network. To do so, follow these networking security best practices:

- Minimize the amount of sensitive or personal [user
  data](https://developer.android.com/privacy-and-security/security-tips#user-data) that you transmit over the network.
- Send all network traffic from your app over [SSL](https://developer.android.com/training/articles/security-ssl).
- Consider creating a [network security
  configuration](https://developer.android.com/training/articles/security-config), which lets your app trust custom certificate authorities (CAs) or restrict the set of system CAs that it trusts for secure communication.

For more information on how to apply secure networking principles, see the
[networking security tips](https://developer.android.com/privacy-and-security/security-tips#networking).

## Choose an HTTP client

Most network-connected apps use HTTP to send and receive data. The Android
platform includes the
[`HttpsURLConnection`](https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection) client,
which supports TLS, streaming uploads and downloads, configurable timeouts,
IPv6, and connection pooling.

Third-party libraries that offer higher-level APIs for networking operations are
also available. These support various convenience features, such as the
serialization of request bodies and deserialization of response bodies.

- [Retrofit](https://square.github.io/retrofit/): a type-safe HTTP client for the JVM from Square, built on top of OkHttp. Retrofit lets you create a client interface declaratively and has support for several serialization libraries.
- [Ktor](https://ktor.io/): an HTTP client from JetBrains, built entirely for Kotlin and powered by coroutines. Ktor supports various engines, serializers, and platforms.

## Resolve DNS queries

Devices that run Android 10 (API level 29) and higher have built-in support for
specialized DNS lookups through both cleartext lookups and DNS-over-TLS mode.
The [`DnsResolver`](https://developer.android.com/reference/android/net/DnsResolver) API provides generic,
asynchronous resolution, which lets you look up `SRV`, `NAPTR`, and other
record types. Parsing the response is left to the app to perform.

On devices that run Android 9 (API level 28) and lower, the platform DNS
resolver supports only `A` and `AAAA` records. This lets you look up the IP
addresses associated with a name but doesn't support any other record types.

For NDK-based apps, see
[`android_res_nsend`](https://developer.android.com/ndk/reference/group/networking#android_res_nsend).

## Encapsulate network operations with a repository

To simplify the process of performing network operations and reduce code
duplication in various parts of your app, you can use the repository design
pattern. A repository is a class that handles data operations and provides a
clean API abstraction over some specific data or resource.

You can use Retrofit to declare an interface that specifies the HTTP method,
URL, arguments, and response type for network operations, as in the following
example:

### Kotlin

```kotlin
interface UserService {
    @GET("/users/{id}")
    suspend fun getUser(@Path("id") id: String): User
}
```

### Java

```java
public interface UserService {
    @GET("/user/{id}")
    Call<User> getUserById(@Path("id") String id);
}
```

Within a repository class, functions can encapsulate network operations and
expose their results. This encapsulation ensures that the components that call
the repository don't need to know how the data is stored. Any future changes to
how the data is stored are isolated to the repository class as well. For
example, you might have a remote change such as an update to API endpoints, or
you might want to implement local caching.

### Kotlin

```kotlin
class UserRepository constructor(
    private val userService: UserService
) {
    suspend fun getUserById(id: String): User {
        return userService.getUser(id)
    }
}
```

### Java

```java
class UserRepository {
    private UserService userService;

    public UserRepository(
            UserService userService
    ) {
        this.userService = userService;
    }

    public Call<User> getUserById(String id) {
        return userService.getUser(id);
    }
}
```

To avoid creating an unresponsive UI, don't perform network operations on the
main thread. By default, Android requires you to perform network operations on a
thread other than the main UI thread. If you try to perform network operations
on the main thread, a
[`NetworkOnMainThreadException`](https://developer.android.com/reference/android/os/NetworkOnMainThreadException)
is thrown.

In the previous code example, the
network operation isn't actually triggered. The caller of the `UserRepository`
must implement the threading either using coroutines or using the `enqueue()`
function. For more information, see the codelab [Get data from the
internet](https://developer.android.com/codelabs/basic-android-kotlin-training-getting-data-internet),
which demonstrates how to implement threading using Kotlin coroutines.

## Survive configuration changes

When a configuration change occurs, such as a screen rotation, your fragment or
activity is destroyed and recreated. Any data not saved in the instance
state for your fragment activity, which can only hold small amounts of data,
is lost. If this occurs, you might need to make your network requests again.

You can use a [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel) to let
your data survive configuration changes. The `ViewModel` component is
designed to store and manage UI-related data in a lifecycle-conscious
way. Using the preceding `UserRepository`, the `ViewModel` can make the
necessary network requests and provide the result to your fragment or activity
using [`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata):

### Kotlin

```kotlin
class MainViewModel constructor(
    savedStateHandle: SavedStateHandle,
    userRepository: UserRepository
) : ViewModel() {
    private val userId: String = savedStateHandle["uid"] ?:
        throw IllegalArgumentException("Missing user ID")

    private val _user = MutableLiveData<User>()
    val user = _user as LiveData<User>

    init {
        viewModelScope.launch {
            try {
                // Calling the repository is safe as it moves execution off
                // the main thread
                val user = userRepository.getUserById(userId)
                _user.value = user
            } catch (error: Exception) {
                // Show error message to user
            }

        }
    }
}
```

### Java

```java
class MainViewModel extends ViewModel {

    private final MutableLiveData<User> _user = new MutableLiveData<>();
    LiveData<User> user = (LiveData<User>) _user;

    public MainViewModel(
            SavedStateHandle savedStateHandle,
            UserRepository userRepository
    ) {
        String userId = savedStateHandle.get("uid");
        Call<User> userCall = userRepository.getUserById(userId);
        userCall.enqueue(new Callback<User>() {
            @Override
            public void onResponse(Call<User> call, Response<User> response) {
                if (response.isSuccessful()) {
                    _user.setValue(response.body());
                }
            }

            @Override
            public void onFailure(Call<User> call, Throwable t) {
                // Show error message to user
            }
        });
    }
}
```

## Read related guides

To learn more about this topic, see the following related guides:

- [Reduce network battery drain: Overview](https://developer.android.com/topic/performance/power)
- [Minimize the effect of regular updates](https://developer.android.com/training/efficient-downloads)
- [Web-based content](https://developer.android.com/guide/webapps)
- [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
- [Guide to app architecture](https://developer.android.com/jetpack/guide)