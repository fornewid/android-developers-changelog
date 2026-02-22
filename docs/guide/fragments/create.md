---
title: https://developer.android.com/guide/fragments/create
url: https://developer.android.com/guide/fragments/create
source: md.txt
---

# Create a fragment

A[fragment](https://developer.android.com/guide/fragments)represents a modular portion of the user interface within an activity. A fragment has its own lifecycle, receives its own input events, and you can add or remove fragments while the containing activity is running.

This document describes how to create a fragment and include it in an activity.

## Setup your environment

Fragments require a dependency on the[AndroidX Fragment library](https://developer.android.com/jetpack/androidx/releases/fragment). You need to add the[Google Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)to your project's`settings.gradle`file in order to include this dependency.  

### Groovy

```groovy
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        ...
    }
}
```

### Kotlin

```kotlin
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        ...
    }
}
```

To include the AndroidX Fragment library to your project, add the following dependencies in your app's`build.gradle`file:  

### Groovy

```groovy
dependencies {
    def fragment_version = "1.8.9"

    // Java language implementation
    implementation "androidx.fragment:fragment:$fragment_version"
    // Kotlin
    implementation "androidx.fragment:fragment-ktx:$fragment_version"
}
```

### Kotlin

```kotlin
dependencies {
    val fragment_version = "1.8.9"

    // Java language implementation
    implementation("androidx.fragment:fragment:$fragment_version")
    // Kotlin
    implementation("androidx.fragment:fragment-ktx:$fragment_version")
}
```

## Create a fragment class

To create a fragment, extend the AndroidX[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment)class, and override its methods to insert your app logic, similar to the way you would create an[`Activity`](https://developer.android.com/reference/android/app/Activity)class. To create a minimal fragment that defines its own layout, provide your fragment's layout resource to the base constructor, as shown in the following example:  

### Kotlin

```kotlin
class ExampleFragment : Fragment(R.layout.example_fragment)
```

### Java

```java
class ExampleFragment extends Fragment {
    public ExampleFragment() {
        super(R.layout.example_fragment);
    }
}
```

The Fragment library also provides more specialized fragment base classes:

[`DialogFragment`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment)
:   Displays a floating dialog. Using this class to create a dialog is a good alternative to using the dialog helper methods in the[`Activity`](https://developer.android.com/reference/android/app/Activity)class, as fragments automatically handle the creation and cleanup of the`Dialog`. See[Displaying dialogs with`DialogFragment`](https://developer.android.com/guide/fragments/dialogs)for more details.

[`PreferenceFragmentCompat`](https://developer.android.com/reference/androidx/preference/PreferenceFragmentCompat)
:   Displays a hierarchy of[`Preference`](https://developer.android.com/reference/androidx/preference/Preference)objects as a list. You can use`PreferenceFragmentCompat`to[create a settings screen](https://developer.android.com/develop/ui/views/components/settings)for your app.

## Add a fragment to an activity

Generally, your fragment must be embedded within an AndroidX[`FragmentActivity`](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity)to contribute a portion of UI to that activity's layout.`FragmentActivity`is the base class for[`AppCompatActivity`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity), so if you're already subclassing`AppCompatActivity`to provide backward compatibility in your app, then you do not need to change your activity base class.

You can add your fragment to the activity's view hierarchy either by defining the fragment in your activity's layout file or by defining a fragment container in your activity's layout file and then programmatically adding the fragment from within your activity. In either case, you need to add a[`FragmentContainerView`](https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView)that defines the location where the fragment should be placed within the activity's view hierarchy. It is strongly recommended to always use a`FragmentContainerView`as the container for fragments, as`FragmentContainerView`includes fixes specific to fragments that other view groups such as`FrameLayout`do not provide.

### Add a fragment via XML

To declaratively add a fragment to your activity layout's XML, use a`FragmentContainerView`element.

Here's an example activity layout containing a single`FragmentContainerView`:  

    <!-- res/layout/example_activity.xml -->
    <androidx.fragment.app.FragmentContainerView
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/fragment_container_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:name="com.example.ExampleFragment" />

The`android:name`attribute specifies the class name of the`Fragment`to instantiate. When the activity's layout is inflated, the specified fragment is instantiated,[`onInflate()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onInflate(android.content.Context,%2520android.util.AttributeSet,%2520android.os.Bundle))is called on the newly instantiated fragment, and a`FragmentTransaction`is created to add the fragment to the`FragmentManager`.
| **Note:** You can use the`class`attribute instead of`android:name`as an alternative way to specify which`Fragment`to instantiate.

### Add a fragment programmatically

To programmatically add a fragment to your activity's layout, the layout should include a`FragmentContainerView`to serve as a fragment container, as shown in the following example:  

    <!-- res/layout/example_activity.xml -->
    <androidx.fragment.app.FragmentContainerView
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/fragment_container_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

Unlike the XML approach, the`android:name`attribute isn't used on the`FragmentContainerView`here, so no specific fragment is automatically instantiated. Instead, a[`FragmentTransaction`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction)is used to instantiate a fragment and add it to the activity's layout.

While your activity is running, you can make fragment transactions such as adding, removing, or replacing a fragment. In your`FragmentActivity`, you can get an instance of the[`FragmentManager`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager), which can be used to create a`FragmentTransaction`. Then, you can instantiate your fragment within your activity's`onCreate()`method using[`FragmentTransaction.add()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#add(int,%20java.lang.Class%3C?%20extends%20androidx.fragment.app.Fragment%3E,%20android.os.Bundle)), passing in the`ViewGroup`ID of the container in your layout and the fragment class you want to add and then commit the transaction, as shown in the following example:  

### Kotlin

```kotlin
class ExampleActivity : AppCompatActivity(R.layout.example_activity) {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        if (savedInstanceState == null) {
            supportFragmentManager.commit {
                setReorderingAllowed(true)
                add<ExampleFragment>(R.id.fragment_container_view)
            }
        }
    }
}
```

### Java

```java
public class ExampleActivity extends AppCompatActivity {
    public ExampleActivity() {
        super(R.layout.example_activity);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (savedInstanceState == null) {
            getSupportFragmentManager().beginTransaction()
                .setReorderingAllowed(true)
                .add(R.id.fragment_container_view, ExampleFragment.class, null)
                .commit();
        }
    }
}
```
| **Note:** You should**always** use`setReorderingAllowed(true)`when performing a`FragmentTransaction`. For more information on reordered transactions, see[Fragment transactions](https://developer.android.com/guide/fragments/transactions#reordering).

In the previous example, note that the fragment transaction is only created when`savedInstanceState`is`null`. This is to ensure that the fragment is added only once, when the activity is first created. When a configuration change occurs and the activity is recreated,`savedInstanceState`is no longer`null`, and the fragment does not need to be added a second time, as the fragment is automatically restored from the`savedInstanceState`.

If your fragment requires some initial data, arguments can be passed to your fragment by providing a[Bundle](https://developer.android.com/reference/android/os/Bundle)in the call to`FragmentTransaction.add()`, as shown below:  

### Kotlin

```kotlin
class ExampleActivity : AppCompatActivity(R.layout.example_activity) {
      override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        if (savedInstanceState == null) {
            val bundle = bundleOf("some_int" to 0)
            supportFragmentManager.commit {
                setReorderingAllowed(true)
                add<ExampleFragment>(R.id.fragment_container_view, args = bundle)
            }
        }
    }
}
```

### Java

```java
public class ExampleActivity extends AppCompatActivity {
    public ExampleActivity() {
        super(R.layout.example_activity);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (savedInstanceState == null) {
            Bundle bundle = new Bundle();
            bundle.putInt("some_int", 0);

            getSupportFragmentManager().beginTransaction()
                .setReorderingAllowed(true)
                .add(R.id.fragment_container_view, ExampleFragment.class, bundle)
                .commit();
        }
    }
}
```

The arguments`Bundle`can then be retrieved from within your fragment by calling[`requireArguments()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#requireArguments()), and the appropriate`Bundle`getter methods can be used to retrieve each argument.  

### Kotlin

```kotlin
class ExampleFragment : Fragment(R.layout.example_fragment) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val someInt = requireArguments().getInt("some_int")
        ...
    }
}
```

### Java

```java
class ExampleFragment extends Fragment {
    public ExampleFragment() {
        super(R.layout.example_fragment);
    }

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        int someInt = requireArguments().getInt("some_int");
        ...
    }
}
```

## See also

Fragment transactions and the`FragmentManager`are covered in more detail in the[Fragment manager guide](https://developer.android.com/guide/fragments/fragmentmanager).