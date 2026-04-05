---
title: Provide custom back navigation  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-custom-back
source: html-scrape
---

* [Android Developers](https://developer.android.com/)

# Provide custom back navigation Stay organized with collections Save and categorize content based on your preferences.



*Back navigation* is how users move backward through the history of screens they
previously visited. All Android devices provide a Back button for this type of
navigation, so don't add a Back button to your app’s UI. Depending on
the user’s Android device, this button might be a physical button or a software
button.

Android maintains a *back stack* of destinations as the user navigates
throughout your application. This lets Android properly navigate to
previous destinations when the Back button is pressed. However, there are a few
cases where your app might need to implement its own Back behavior to
provide the best possible user experience.

For example, when using a `WebView`,
you might want to override the default Back button behavior to let the user
navigate back through their web browsing history instead of the previous screens
in your app.

Android 13 and higher includes a predictive back gesture for Android devices. To
learn more about this feature, check out [Add support for the predictive back gesture](/guide/navigation/predictive-back-gesture).

## Implement custom back navigation

[`ComponentActivity`](/reference/androidx/activity/ComponentActivity), the base
class for [`FragmentActivity`](/reference/androidx/fragment/app/FragmentActivity)
and [`AppCompatActivity`](/reference/androidx/appcompat/app/AppCompatActivity),
lets you control the behavior of the Back button by using its
[`OnBackPressedDispatcher`](/reference/androidx/activity/OnBackPressedDispatcher),
which you can retrieve by calling [`getOnBackPressedDispatcher()`](/reference/androidx/activity/ComponentActivity#getOnBackPressedDispatcher()).

**Note:** If your app uses Activity 1.5.0 or higher, you can also implement custom
back navigation for a dialog by using
[`ComponentDialog`](/reference/androidx/activity/ComponentDialog) and its
`OnBackPressedDispatcher`.

The `OnBackPressedDispatcher` controls how Back button events are dispatched
to one or more [`OnBackPressedCallback`](/reference/androidx/activity/OnBackPressedCallback)
objects. The constructor for `OnBackPressedCallback` takes a boolean for the
initial enabled state. When a callback is enabled—that is,
[`isEnabled()`](/reference/androidx/activity/OnBackPressedCallback#isEnabled())
returns `true`—the dispatcher calls the callback's
[`handleOnBackPressed()`](/reference/androidx/activity/OnBackPressedCallback#handleOnBackPressed())
to handle the Back button event. You can change the enabled state by calling
[`setEnabled()`](/reference/androidx/activity/OnBackPressedCallback#setEnabled(boolean)).

Callbacks are added using the `addCallback` methods. We recommend using
the [`addCallback()`](/reference/androidx/activity/OnBackPressedDispatcher#addCallback(androidx.activity.OnBackPressedCallback))
method, which takes a [`LifecycleOwner`](/reference/androidx/lifecycle/LifecycleOwner).
This ensures that the `OnBackPressedCallback` is only added when the `LifecycleOwner` is
[`Lifecycle.State.STARTED`](/reference/androidx/lifecycle/Lifecycle.State#STARTED).
The activity also removes registered callbacks when their associated
`LifecycleOwner` is destroyed, which prevents memory leaks and makes the
`LifecycleOwner` suitable
for use in fragments or other lifecycle owners that have a shorter lifetime
than the activity.

Here is an example callback implementation:

### Kotlin

```
class MyFragment : Fragment() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // This callback is only called when MyFragment is at least started
        val callback = requireActivity().onBackPressedDispatcher.addCallback(this) {
            // Handle the back button event
        }

        // The callback can be enabled or disabled here or in the lambda
    }
    ...
}
```

### Java

```
public class MyFragment extends Fragment {

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // This callback is only called when MyFragment is at least started
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

You can provide multiple callbacks using `addCallback()`.
When you do, the callbacks are invoked in the reverse order from the order you
add them—the callback added last is the first given a chance to handle the
Back button event. For example, if you add three callbacks named
`one`, `two`, and `three`, in that order, they are invoked in the order
`three`, `two`, `one`.

Callbacks follow the
[Chain of Responsibility](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
pattern. Each callback in the chain is invoked only if the preceding
callback was not enabled. This means that, in the
preceding example, callback `two` is invoked only if callback `three`
is not enabled, and callback `one` is only invoked if callback `two`
is not enabled.

Note that when the callback is added using `addCallback()`,
it is not added to the chain of responsibility until the
`LifecycleOwner` enters the `Lifecycle.State.STARTED` state.

We recommend changing the enabled state on the `OnBackPressedCallback`
for temporary changes, as doing so maintains the ordering described above.
This is particularly important if you have callbacks registered on multiple
nested lifecycle owners.

In cases where you want to remove the `OnBackPressedCallback` entirely,
you can call
[`remove()`](/reference/androidx/activity/OnBackPressedCallback#remove()).
This is usually not necessary, because callbacks are automatically removed when
their associated `LifecycleOwner` is
[destroyed](/reference/androidx/lifecycle/Lifecycle.State#DESTROYED).

## Activity onBackPressed()

If you are using
[`onBackPressed()`](/reference/androidx/activity/ComponentActivity#onBackPressed())
to handle Back button events, we recommend using an
[`OnBackPressedCallback`](/reference/androidx/activity/OnBackPressedCallback) instead.
However, if you can't make this change, the following rules apply:

* All callbacks registered via `addCallback` are evaluated when you call
  `super.onBackPressed()`.
* In Android 12 (API level 32) and lower, `onBackPressed` is always called,
  regardless of any registered instances of `OnBackPressedCallback`.