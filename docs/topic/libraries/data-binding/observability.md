---
title: Work with observable data objects  |  App architecture  |  Android Developers
url: https://developer.android.com/topic/libraries/data-binding/observability
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Work with observable data objects Stay organized with collections Save and categorize content based on your preferences.



*Observability* refers to the capability of an object to notify others about
changes in its data. The Data Binding Library lets you make objects, fields, or
collections observable.

You can use any object for data binding, but modifying the object doesn't
automatically cause the UI to update. You can use data binding to give your data
objects the ability to notify other objects—known as listeners—when
their data changes. There are three types of observable classes:
[fields](#observable_fields), [collections](#observable_collections), and
[objects](#observable_objects).

When one of these observable data objects is bound to the UI and a property of
the data object changes, the UI updates automatically.

## Observable fields

If your classes only have a few properties, it might not be worth the effort to
create classes that implement the
[`Observable`](/reference/android/databinding/Observable) interface. In this
case, you can use the generic `Observable` class and the following
primitive-specific classes to make fields observable:

* [`ObservableBoolean`](/reference/android/databinding/ObservableBoolean)
* [`ObservableByte`](/reference/android/databinding/ObservableByte)
* [`ObservableChar`](/reference/android/databinding/ObservableChar)
* [`ObservableShort`](/reference/android/databinding/ObservableShort)
* [`ObservableInt`](/reference/android/databinding/ObservableInt)
* [`ObservableLong`](/reference/android/databinding/ObservableLong)
* [`ObservableFloat`](/reference/android/databinding/ObservableFloat)
* [`ObservableDouble`](/reference/android/databinding/ObservableDouble)
* [`ObservableParcelable`](/reference/android/databinding/ObservableParcelable)

Observable fields are self-contained observable objects that have a single
field. The primitive versions avoid boxing and unboxing during access
operations. To use this mechanism, create a `public final` property in the Java
programming language or a read-only property in Kotlin, as shown in the
following example:

### Kotlin

```
class User {
    val firstName = ObservableField<String>()
    val lastName = ObservableField<String>()
    val age = ObservableInt()
}
```

### Java

```
private static class User {
    public final ObservableField<String> firstName = new ObservableField<>();
    public final ObservableField<String> lastName = new ObservableField<>();
    public final ObservableInt age = new ObservableInt();
}
```

To access the field value, use the
[`set()`](/reference/android/databinding/ObservableField#set) and
[`get()`](/reference/android/databinding/ObservableField#get) accessor methods
or use [Kotlin property
syntax](https://kotlinlang.org/docs/reference/properties.html#declaring-properties):

### Kotlin

```
user.firstName = "Google"
val age = user.age
```

### Java

```
user.firstName.set("Google");
int age = user.age.get();
```

## Observable collections

Some apps use dynamic structures to hold data. Observable collections allow
access to these structures by using a key. The
[`ObservableArrayMap`](/reference/android/databinding/ObservableArrayMap) class
is useful when the key is a reference type, such as `String`, as shown in the
following example:

### Kotlin

```
ObservableArrayMap<String, Any>().apply {
    put("firstName", "Google")
    put("lastName", "Inc.")
    put("age", 17)
}
```

### Java

```
ObservableArrayMap<String, Object> user = new ObservableArrayMap<>();
user.put("firstName", "Google");
user.put("lastName", "Inc.");
user.put("age", 17);
```

In the layout, you can find the map using the string keys, as shown in the
following example:

```
<data>
    <import type="android.databinding.ObservableMap"/>
    <variable name="user" type="ObservableMap&lt;String, Object&gt;"/>
</data>
…
<TextView
    android:text="@{user.lastName}"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
<TextView
    android:text="@{String.valueOf(1 + (Integer)user.age)}"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
```

The [`ObservableArrayList`](/reference/android/databinding/ObservableArrayList)
class is useful when the key is an integer, as follows:

### Kotlin

```
ObservableArrayList<Any>().apply {
    add("Google")
    add("Inc.")
    add(17)
}
```

### Java

```
ObservableArrayList<Object> user = new ObservableArrayList<>();
user.add("Google");
user.add("Inc.");
user.add(17);
```

In the layout, you can access the list through the indexes, as shown in the
following example:

```
<data>
    <import type="android.databinding.ObservableList"/>
    <import type="com.example.my.app.Fields"/>
    <variable name="user" type="ObservableList&lt;Object&gt;"/>
</data>
…
<TextView
    android:text='@{user[Fields.LAST_NAME]}'
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
<TextView
    android:text='@{String.valueOf(1 + (Integer)user[Fields.AGE])}'
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"/>
```

## Observable objects

A class that implements the `Observable` interface allows the registration of
listeners that want to be notified of property changes from the observable
object.

The `Observable` interface has a mechanism to add and remove listeners, but you
decide when notifications are sent. To make development easier, the Data
Binding Library provides the
[`BaseObservable`](/reference/android/databinding/BaseObservable) class, which
implements the listener registration mechanism. The data class that implements
`BaseObservable` is responsible for notifying when the properties change. To do
this, assign a [`Bindable`](/reference/android/databinding/Bindable) annotation
to the getter and call the
[`notifyPropertyChanged()`](/reference/android/databinding/BaseObservable#notifypropertychanged)
method in the setter, as shown in the following example:

### Kotlin

```
class User : BaseObservable() {

    @get:Bindable
    var firstName: String = ""
        set(value) {
            field = value
            notifyPropertyChanged(BR.firstName)
        }

    @get:Bindable
    var lastName: String = ""
        set(value) {
            field = value
            notifyPropertyChanged(BR.lastName)
        }
}
```

### Java

```
private static class User extends BaseObservable {
    private String firstName;
    private String lastName;

    @Bindable
    public String getFirstName() {
        return this.firstName;
    }

    @Bindable
    public String getLastName() {
        return this.lastName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
        notifyPropertyChanged(BR.firstName);
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
        notifyPropertyChanged(BR.lastName);
    }
}
```

Data binding generates a class named `BR` in the module package, which contains
the IDs of the resources used for data binding. The `Bindable` annotation
generates an entry in the `BR` class file during compilation. If the base class
for data classes can't be changed, you can implement the `Observable` interface
using a
[`PropertyChangeRegistry`](/reference/android/databinding/PropertyChangeRegistry)
object to register and notify listeners efficiently.

## Lifecycle-aware objects

The layouts in your app can also bind to data binding sources that automatically
notify the UI about changes in the data. That way, your bindings are
lifecycle aware and are only triggered when the UI is visible on the screen.

Data binding supports
[`StateFlow`](/kotlin/flow/stateflow-and-sharedflow) and
[`LiveData`](/topic/libraries/architecture/livedata). For more information about
using `LiveData` in data binding, see [Use LiveData to notify the UI about data
changes](/topic/libraries/data-binding/architecture#livedata).

**Note:** Consider using `LiveData` if your project already depends on the `LiveData`
library. If you don't have an initial value to provide, make sure `StateFlow`
has one. If you don't want to manually unregister the consumer, `LiveData`
automatically unregisters when the view goes to the `STOPPED` state.

### Use StateFlow

If your app uses Kotlin with [coroutines](/kotlin/coroutines), you can use
`StateFlow` objects as the data binding source. To use a `StateFlow` object with
your binding class, specify a lifecycle owner to define the scope of the
`StateFlow` object. The following example specifies the activity as the
lifecycle owner after the binding class is instantiated:

```
class ViewModelActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        // Inflate view and obtain an instance of the binding class.
        val binding: UserBinding = DataBindingUtil.setContentView(this, R.layout.user)

        // Specify the current activity as the lifecycle owner.
        binding.lifecycleOwner = this
    }
}
```

As described in [Bind layout views to Architecture
Components](/topic/libraries/data-binding/architecture#viewmodel), data binding
works seamlessly with [`ViewModel`](/reference/androidx/lifecycle/ViewModel)
objects. You can use `StateFlow` and `ViewModel` together as follows:

```
class ScheduleViewModel : ViewModel() {

    private val _username = MutableStateFlow<String>("")
    val username: StateFlow<String> = _username

    init {
        viewModelScope.launch {
            _username.value = Repository.loadUserName()
        }
    }
}
```

In your layout, assign the properties and methods of your `ViewModel` object to
the corresponding views using binding expressions, as shown in the following
example:

```
<TextView
    android:id="@+id/name"
    android:text="@{viewmodel.username}" />
```

The UI automatically updates whenever the user's name value changes.

**Note:** `StateFlow` support is a preview feature that requires version
`7.0.0-alpha04` or higher of the [Android Gradle
plugin](/studio/releases/gradle-plugin).

#### Disable StateFlow support

For apps that use Kotlin and AndroidX, `StateFlow` support is automatically
included with data binding. This means that the coroutines dependency is
automatically included in your app if the dependency isn't already available.

You can opt out of this functionality by adding the following to your
`build.gradle` file:

### Groovy

```
android {
    ...
    dataBinding {
        addKtx = false
    }
}
```

### Kotlin

```
android {
    ...
    dataBinding {
        addKtx = false
    }
}
```

Alternatively, you can disable `StateFlow` globally in your project by adding
the following line to the `gradle.properties` file:

### Groovy

```
android.defaults.databinding.addKtx = false
```

### Kotlin

```
android.defaults.databinding.addKtx = false
```

## Additional resources

To learn more about data binding, see the following for additional resources:

### Samples

* [Android Data Binding Library samples](https://github.com/android/databinding-samples)

### Codelabs

* [Data Binding in Android](https://codelabs.developers.google.com/codelabs/android-databinding)

### Blog posts

* [Data Binding — lessons learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Saved State module for ViewModel](/topic/libraries/architecture/viewmodel/viewmodel-savedstate)
* [Bind layout views to Architecture Components](/topic/libraries/data-binding/architecture)
* [Paging library overview](/topic/libraries/architecture/paging/v3-overview)