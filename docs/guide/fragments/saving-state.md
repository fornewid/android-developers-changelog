---
title: https://developer.android.com/guide/fragments/saving-state
url: https://developer.android.com/guide/fragments/saving-state
source: md.txt
---

# Saving state with fragments

Various Android system operations can affect the state of your fragment. To ensure the user's state is saved, the Android framework automatically saves and restores the fragments and the back stack. Therefore, you need to ensure that any data in your fragment is saved and restored as well.

The following table outlines the operations that cause your fragment to lose state, along with whether the various types of state persist through those changes. The state types mentioned in the table are as follows:

- Variables: local variables in the fragment.
- View State: any data that is**owned by one or more views**in the fragment.
- SavedState: data inherent to this fragment instance that should be saved in`onSaveInstanceState()`.
- NonConfig: data pulled from an external source, such as a server or local repository, or user-created data that is sent to a server once committed.

Oftentimes*Variables* are treated the same as*SavedState*, but the following table distinguishes between the two to demonstrate the effect of the various operations on each.

|            Operation            | Variables | View State | SavedState | NonConfig |
|---------------------------------|-----------|------------|------------|-----------|
| Added to back stack             | ✓         | ✓          | x          | ✓         |
| Config Change                   | x         | ✓          | ✓          | ✓         |
| Process Death/Recreation        | x         | ✓          | ✓          | ✓\*       |
| Removed not added to back stack | x         | x          | x          | x         |
| Host finished                   | x         | x          | x          | x         |

*\* NonConfig state can be retained across process death using the[Saved State module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate).*

**Table 1:**Various fragment destructive operations and the effects they have on different state types.

Let's look at a specific example. Consider a screen that generates a random string, displays it in a`TextView`, and provides an option to edit the string before sending it to a friend:
![random text generator app that demonstrates various types of state](https://developer.android.com/static/images/guide/fragments/text-generator-app.png)**Figure 1.**Random text generator app that demonstrates various types of state.

For this example, assume that once the user presses the edit button, the app displays an`EditText`view where the user can edit the message. If the user clicks on**CANCEL** , the`EditText`view should be cleared and it's visibility set to[`View.GONE`](https://developer.android.com/reference/android/view/View#GONE). Such a screen might require managing four pieces of data to ensure a seamless experience:

|       Data       |    Type    |           State type            |                                                                                     Description                                                                                     |
|------------------|------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `seed`           | `Long`     | NonConfig                       | Seed used for randomly generating a new good deed. Generated when the`ViewModel`is created.                                                                                         |
| `randomGoodDeed` | `String`   | SavedState + Variable           | Generated when the fragment is created for the very first time.`randomGoodDeed`is saved to ensure that users see the same random good deed even after process death and recreation. |
| `isEditing`      | `Boolean`  | SavedState + Variable           | Boolean flag set to`true`when the user begins editing.`isEditing`is saved to ensure that the editing portion of the screen remains visible when the fragment is recreated.          |
| Edited text      | `Editable` | View State (owned by`EditText`) | The edited text in the`EditText`view. The`EditText`view saves this text to ensure that the user's in-progress changes are not lost.                                                 |

**Table 2:**States that the random text generator app must manage.

The following sections describe how to properly manage the state of your data through destructive operations.

## View state

Views are responsible for managing their own state. For example, when a view accepts user input, it is the view's responsibility to save and restore that input to handle configuration changes. All Android framework-provided views have their own implementation of`onSaveInstanceState()`and`onRestoreInstanceState()`, so you don't have to manage view state within your fragment.
| **Note:** To ensure proper handling during configuration changes, you should implement`onSaveInstanceState()`and`onRestoreInstanceState()`for any custom views that you create.

For example, in the previous scenario, the edited string is held in an[`EditText`](https://developer.android.com/reference/android/widget/EditText). An`EditText`knows the value of the text it's displaying, as well as other details, such as the beginning and end of any selected text.

A view needs an ID to retain its state. This ID must be unique within the fragment and its view hierarchy.**Views without an ID cannot retain their state.**  

```xml
<EditText
    android:id="@+id/good_deed_edit_text"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

As mentioned in table 1, views save and restore their`ViewState`through all operations that don't remove the fragment or destroy the host.

## `SavedState`

Your fragment is responsible for managing small amounts of dynamic state that are integral to how the fragment functions. You can retain easily-serialized data using[`Fragment.onSaveInstanceState(Bundle)`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onsaveinstancestate). Similar to[`Activity.onSaveInstanceState(Bundle)`](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle)), the data you place in the bundle is retained through configuration changes and process death and recreation and is available in your fragment's[`onCreate(Bundle)`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate(android.os.Bundle)),[`onCreateView(LayoutInflater, ViewGroup, Bundle)`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView(android.view.LayoutInflater,%20android.view.ViewGroup,%20android.os.Bundle)), and[`onViewCreated(View, Bundle)`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated(android.view.View,%20android.os.Bundle))methods.
| **Caution:** `onSaveInstanceState(Bundle)`is called only when the fragment's host activity calls its own`onSaveInstanceState(Bundle)`.
| **Tip:** When using a`ViewModel`, you can save state directly within the`ViewModel`using a`SavedStateHandle`. For more information, see[Saved State module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate).

Continuing with the previous example,`randomGoodDeed`is the deed that's displayed to the user, and`isEditing`is a flag to determine whether the fragment shows or hides the`EditText`. This saved state should be persisted using`onSaveInstanceState(Bundle)`, as shown in the following example:  

### Kotlin

```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putBoolean(IS_EDITING_KEY, isEditing)
    outState.putString(RANDOM_GOOD_DEED_KEY, randomGoodDeed)
}
```

### Java

```java
@Override
public void onSaveInstanceState(@NonNull Bundle outState) {
    super.onSaveInstanceState(outState);
    outState.putBoolean(IS_EDITING_KEY, isEditing);
    outState.putString(RANDOM_GOOD_DEED_KEY, randomGoodDeed);
}
```

To restore the state in`onCreate(Bundle)`retrieve the stored value from the bundle:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    isEditing = savedInstanceState?.getBoolean(IS_EDITING_KEY, false)
    randomGoodDeed = savedInstanceState?.getString(RANDOM_GOOD_DEED_KEY)
            ?: viewModel.generateRandomGoodDeed()
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    if (savedInstanceState != null) {
        isEditing = savedInstanceState.getBoolean(IS_EDITING_KEY, false);
        randomGoodDeed = savedInstanceState.getString(RANDOM_GOOD_DEED_KEY);
    } else {
        randomGoodDeed = viewModel.generateRandomGoodDeed();
    }
}
```

As mentioned in table 1, note that the variables are retained when the fragment is placed on the backstack. Treating them as saved state ensures they persist through all destructive operations.

## NonConfig

NonConfig data should be placed outside of your fragment, such as in a[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel). In the previous example above,`seed`(our NonConfig state) is generated in the`ViewModel`. The logic to maintain its state is owned by the`ViewModel`.  

### Kotlin

```kotlin
public class RandomGoodDeedViewModel : ViewModel() {
    private val seed = ... // Generate the seed

    private fun generateRandomGoodDeed(): String {
        val goodDeed = ... // Generate a random good deed using the seed
        return goodDeed
    }
}
```

### Java

```java
public class RandomGoodDeedViewModel extends ViewModel {
    private Long seed = ... // Generate the seed

    private String generateRandomGoodDeed() {
        String goodDeed = ... // Generate a random good deed using the seed
        return goodDeed;
    }
}
```

The`ViewModel`class inherently allows data to survive configuration changes, such as screen rotations, and remains in memory when the fragment is placed on the back stack. After process death and recreation, the`ViewModel`is recreated, and a new`seed`is generated. Adding a[`SavedState`](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate)module to your`ViewModel`allows the`ViewModel`to retain simple state through process death and recreation.

## Additional resources

For more information about managing fragment state, see the following additional resources.

### Codelabs

- [Lifecycle-Aware Components](https://codelabs.developers.google.com/codelabs/android-lifecycles/#0)codelab

### Guides

- [Saved State Module for View Model](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate)
- [Saving UI States](https://developer.android.com/topic/libraries/architecture/saving-states)