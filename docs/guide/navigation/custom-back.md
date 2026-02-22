---
title: https://developer.android.com/guide/navigation/custom-back
url: https://developer.android.com/guide/navigation/custom-back
source: md.txt
---

# Provide custom back navigation

Users navigate backward through screens using *back navigation* . Most Android
devices have a back button---physical, software, or gesture-based. Usually, you
shouldn't add a back button to your app. However, Android Automotive OS (AAOS)
devices in compatibility mode use a system back button. This handles navigation,
so you don't need to add your own. For details, see
[AAOS Compatibility Mode](https://developer.android.com/training/cars/platforms/automotive-os/compatibility-mode).

Android maintains a *back stack* of destinations as the user navigates
throughout your application. This usually allows Android to properly navigate to
previous destinations when the Back button is pressed. However, there are a few
cases where your app might need to implement its own Back behavior in order to
provide the best possible user experience. For example, when using a `WebView`,
you might want to override the default Back button behavior to allow the user to
navigate back through their web browsing history instead of the previous screens
in your app.
| **Note:** Android 13 introduces predictive back navigation, which works with custom back navigation, for Android devices. We strongly recommend that you implement predictive back navigation as soon as possible. Otherwise, users might experience unexpected behavior in a future Android release. To learn more, see [Add support for the predictive back gesture](https://developer.android.com/guide/navigation/predictive-back-gesture).

## Implement custom back navigation

[`ComponentActivity`](https://developer.android.com/reference/androidx/activity/ComponentActivity), the base
class for [`FragmentActivity`](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity)
and [`AppCompatActivity`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity),
allows you to control the behavior of the Back button by using its
[`OnBackPressedDispatcher`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher),
which you can retrieve by calling [`getOnBackPressedDispatcher()`](https://developer.android.com/reference/androidx/activity/ComponentActivity#getOnBackPressedDispatcher()).
| **Note:** If your app uses Activity 1.5.0 or higher, you can also implement custom back navigation for a dialog by using [`ComponentDialog`](https://developer.android.com/reference/androidx/activity/ComponentDialog) and its `OnBackPressedDispatcher`.

The `OnBackPressedDispatcher` controls how Back button events are dispatched
to one or more [`OnBackPressedCallback`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback)
objects. The constructor for `OnBackPressedCallback` takes a boolean for the
initial enabled state. Only when a callback is enabled (i.e.,
[`isEnabled()`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback#isEnabled())
returns `true`) will the dispatcher call the callback's
[`handleOnBackPressed()`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback#handleOnBackPressed())
to handle the Back button event. You can change the enabled state by calling
[`setEnabled()`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback#setEnabled(boolean)).

Callbacks are added via the `addCallback` methods. It is strongly recommended to
use the [`addCallback()`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher#addCallback(androidx.lifecycle.LifecycleOwner,%20androidx.activity.OnBackPressedCallback))
method which takes a [`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner).
This ensures that the `OnBackPressedCallback` is only added when the `LifecycleOwner` is
[`Lifecycle.State.STARTED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#STARTED).
The activity also removes registered callbacks when their associated
`LifecycleOwner` is destroyed, which prevents memory leaks and makes it suitable
for use in fragments or other lifecycle owners that have a shorter lifetime
than the activity.

Here's an example callback implementation:  

### Kotlin

```kotlin
class MyFragment : Fragment() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // This callback will only be called when MyFragment is at least Started.
        val callback = requireActivity().onBackPressedDispatcher.addCallback(this) {
            // Handle the back button event
        }

        // The callback can be enabled or disabled here or in the lambda
    }
    ...
}
```

### Java

```java
public class MyFragment extends Fragment {

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // This callback will only be called when MyFragment is at least Started.
        OnBackPressedCallback callback = new OnBackPressedCallback(true /* enabled by default */) {
            @Override
            public void handleOnBackPressed() {
                // Handle the back button event
            }
        };
        requireActivity().getOnBackPressedDispatcher().addCallback(this, callback);

        // The callback can be enabled or disabled here or in handleOnBackPressed()
    }
    ...
}
```

You can provide multiple callbacks via [`addCallback()`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher#addCallback(%20androidx.activity.OnBackPressedCallback)).
When doing so, the callbacks are invoked in the reverse order in which they are
added - the callback added last is the first given a chance to handle the
Back button event. For example, if you added three callbacks named
`one`, `two` and `three` in order, they would be invoked in the order of
`three`, `two`, and `one`, respectively.

Callbacks follow the
[Chain of Responsibility](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
pattern. Each callback in the chain is invoked only if the preceding
callback was not enabled. This means that in the
preceding example, callback `two` would be invoked only if callback `three`
was not enabled. Callback `one` would only be invoked if callback `two`
was not enabled, and so on.

Note that when added via [`addCallback()`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher#addCallback(androidx.lifecycle.LifecycleOwner,%20androidx.activity.OnBackPressedCallback)),
the callback is not added to the chain of responsibility until the
`LifecycleOwner` enters the
[`Lifecycle.State.STARTED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#STARTED)
state.

Changing the enabled state on the `OnBackPressedCallback` is strongly
recommended for temporary changes as it maintains the ordering described above,
which is particularly important if you have callbacks registered on multiple
different nested lifecycle owners.

However, in cases where you want to remove the `OnBackPressedCallback` entirely,
you should call
[`remove()`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback#remove()).
This is usually not necessary, however, because callbacks are automatically removed when their associated [`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner) is
[destroyed](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#DESTROYED).

## Activity onBackPressed()

If you are using
[`onBackPressed()`](https://developer.android.com/reference/androidx/activity/ComponentActivity#onBackPressed())
to handle Back button events, we recommend using a
[`OnBackPressedCallback`](https://developer.android.com/reference/androidx/activity/OnBackPressedCallback) instead.
However, if you are unable to make this change, the following rules apply:

- All callbacks registered via `addCallback` are evaluated when you call `super.onBackPressed()`.
- In Android 12 (API level 32) and lower, `onBackPressed` is always called, regardless of any registered instances of `OnBackPressedCallback`.