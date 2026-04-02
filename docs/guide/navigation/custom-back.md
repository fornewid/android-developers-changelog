---
title: Provide custom back navigation  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/custom-back
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Provide custom back navigation Stay organized with collections Save and categorize content based on your preferences.



Users navigate backward through screens using *back navigation*. Most Android
devices have a back button—physical, software, or gesture-based. Usually, you
shouldn't add a back button to your app. However, Android Automotive OS (AAOS)
devices in compatibility mode use a system back button. This handles navigation,
so you don't need to add your own. For details, see
[AAOS Compatibility Mode](/training/cars/platforms/automotive-os/compatibility-mode).

Android maintains a *back stack* of destinations as the user navigates
throughout your application. This usually allows Android to properly navigate to
previous destinations when the Back button is pressed. However, there are a few
cases where your app might need to implement its own Back behavior in order to
provide the best possible user experience. For example, when using a `WebView`,
you might want to override the default Back button behavior to allow the user to
navigate back through their web browsing history instead of the previous screens
in your app.

**Note:** Android 13 introduces predictive back navigation, which works with custom
back navigation, for Android devices. We strongly recommend that you implement
predictive back navigation as soon as possible. Otherwise, users might
experience unexpected behavior in a future Android release. To learn more,
see [Add support for the predictive back gesture](/guide/navigation/predictive-back-gesture).

## Implement custom back navigation in Compose

In Jetpack Compose, you can handle custom back navigation using the
[`BackHandler`](/reference/kotlin/androidx/activity/compose/package-summary#BackHandler(kotlin.Boolean,kotlin.Function0)) composable.

When using [Navigation Compose](/develop/ui/compose/navigation), you typically use
[`NavController.navigateUp()`](/reference/kotlin/androidx/navigation/NavController#navigateUp()) or [`NavController.popBackStack()`](/reference/kotlin/androidx/navigation/NavController#popBackStack())
to navigate to the previous screen in the back stack. However, `BackHandler`
is useful for cases where you want to implement custom behavior when the user
presses the system back button or uses the back gesture. For example, if you
are displaying a [`WebView`](/develop/ui/views/layout/webapps/webview) in your app, you might want to allow users to
navigate back through browsing history when they press the system back button.

If you have multiple enabled `BackHandler` composables at different levels of
your composable tree, only the innermost one intercepts the back event.

## Implement custom back navigation with Views

[`ComponentActivity`](/reference/androidx/activity/ComponentActivity), the base class for [`FragmentActivity`](/reference/androidx/fragment/app/FragmentActivity) and
[`AppCompatActivity`](/reference/androidx/appcompat/app/AppCompatActivity), lets you control the behavior of the Back button
by using its [`OnBackPressedDispatcher`](/reference/androidx/activity/OnBackPressedDispatcher), which you can retrieve by calling
[`getOnBackPressedDispatcher()`](/reference/androidx/activity/ComponentActivity#getOnBackPressedDispatcher()).

**Note:** If your app uses Activity 1.5.0 or higher, you can also implement custom
back navigation for a dialog by using
[`ComponentDialog`](/reference/androidx/activity/ComponentDialog) and its
`OnBackPressedDispatcher`.

The `OnBackPressedDispatcher` controls how Back button events are dispatched
to one or more [`OnBackPressedCallback`](/reference/androidx/activity/OnBackPressedCallback) objects. The constructor for
`OnBackPressedCallback` takes a boolean for the initial enabled state. Only when
a callback is enabled, for example when [`isEnabled()`](/reference/androidx/activity/OnBackPressedCallback#isEnabled()) returns `true`, will
the dispatcher call the callback's [`handleOnBackPressed()`](/reference/androidx/activity/OnBackPressedCallback#handleOnBackPressed()) to handle the
Back button event. You can change the enabled state by calling
[`setEnabled()`](/reference/androidx/activity/OnBackPressedCallback#setEnabled(boolean)).

Callbacks are added using the `addCallback` methods. Use the
[`addCallback()`](/reference/androidx/activity/OnBackPressedDispatcher#addCallback(androidx.lifecycle.LifecycleOwner,%20androidx.activity.OnBackPressedCallback)) method which takes a [`LifecycleOwner`](/reference/androidx/lifecycle/LifecycleOwner). This way the
`OnBackPressedCallback` is only added when the `LifecycleOwner` is
[`Lifecycle.State.STARTED`](/reference/androidx/lifecycle/Lifecycle.State#STARTED). The activity also removes registered callbacks
when their associated `LifecycleOwner` is destroyed, which prevents memory leaks
and makes it suitable for use in fragments or other lifecycle owners that have a
shorter lifetime than the activity.

Here's an example callback implementation:

### Kotlin

```
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

```
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

You can provide multiple callbacks using [`addCallback()`](/reference/androidx/activity/OnBackPressedDispatcher#addCallback(%20androidx.activity.OnBackPressedCallback)).
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

Note that when added using [`addCallback()`](/reference/androidx/activity/OnBackPressedDispatcher#addCallback(androidx.lifecycle.LifecycleOwner,%20androidx.activity.OnBackPressedCallback)),
the callback is not added to the chain of responsibility until the
`LifecycleOwner` enters the
[`Lifecycle.State.STARTED`](/reference/androidx/lifecycle/Lifecycle.State#STARTED)
state.

Changing the enabled state on the `OnBackPressedCallback` is strongly
recommended for temporary changes as it maintains the ordering described above,
which is particularly important if you have callbacks registered on multiple
different nested lifecycle owners.

However, in cases where you want to remove the `OnBackPressedCallback` entirely,
you should call
[`remove()`](/reference/androidx/activity/OnBackPressedCallback#remove()).
This is usually not necessary, however, because callbacks are automatically
removed when their associated [`LifecycleOwner`](/reference/androidx/lifecycle/LifecycleOwner) is [destroyed](/reference/androidx/lifecycle/Lifecycle.State#DESTROYED).