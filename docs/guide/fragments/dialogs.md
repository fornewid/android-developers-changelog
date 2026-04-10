---
title: https://developer.android.com/guide/fragments/dialogs
url: https://developer.android.com/guide/fragments/dialogs
source: md.txt
---

# Display dialogs with DialogFragment

A[`DialogFragment`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment)is a special fragment subclass that is designed for creating and hosting[dialogs](https://developer.android.com/guide/topics/ui/dialogs). Although you don't need to host your dialog within a fragment, doing so lets the[`FragmentManager`](https://developer.android.com/guide/fragments/fragmentmanager)manage the state of the dialog and automatically restore the dialog when a configuration change occurs.
| **Note:** This guide assumes familiarity with creating dialogs. For more information, see the[guide to dialogs](https://developer.android.com/guide/topics/ui/dialogs).

## Create a DialogFragment

To create a`DialogFragment`, create a class that extends[`DialogFragment`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment)and override[`onCreateDialog()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#onCreateDialog(android.os.Bundle)), as shown in the following example.  

### Kotlin

```kotlin
class PurchaseConfirmationDialogFragment : DialogFragment() {
    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog =
            AlertDialog.Builder(requireContext())
                .setMessage(getString(R.string.order_confirmation))
                .setPositiveButton(getString(R.string.ok)) { _,_ -> }
                .create()

    companion object {
        const val TAG = "PurchaseConfirmationDialog"
    }
}
```

### Java

```java
public class PurchaseConfirmationDialogFragment extends DialogFragment {
   @NonNull
   @Override
   public Dialog onCreateDialog(@Nullable Bundle savedInstanceState) {
       return new AlertDialog.Builder(requireContext())
               .setMessage(getString(R.string.order_confirmation))
               .setPositiveButton(getString(R.string.ok), (dialog, which) -> {} )
               .create();
   }

   public static String TAG = "PurchaseConfirmationDialog";
}
```

Similar to how[`onCreateView()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreateView(android.view.LayoutInflater,%20android.view.ViewGroup,%20android.os.Bundle))creates a root`View`in an ordinary fragment,`onCreateDialog()`creates a[`Dialog`](https://developer.android.com/reference/android/app/Dialog)to display as part of the`DialogFragment`. The`DialogFragment`handles displaying the`Dialog`at appropriate states in the fragment's lifecycle.
| **Note:** `DialogFragment`owns the[`Dialog.setOnCancelListener()`](https://developer.android.com/reference/android/app/Dialog#setOnCancelListener(android.content.DialogInterface.OnCancelListener))and[`Dialog.setOnDismissListener()`](https://developer.android.com/reference/android/app/Dialog#setOnDismissListener(android.content.DialogInterface.OnDismissListener))callbacks. You must not set them yourself. To find out about these events, override[`onCancel()`](https://developer.android.com/reference/android/content/DialogInterface.OnCancelListener#onCancel(android.content.DialogInterface))and[`onDismiss()`](https://developer.android.com/reference/android/content/DialogInterface.OnDismissListener#onDismiss(android.content.DialogInterface)).

As with`onCreateView()`, you can return any subclass of`Dialog`from`onCreateDialog()`and aren't limited to using[`AlertDialog`](https://developer.android.com/reference/androidx/appcompat/app/AlertDialog).

## Show the DialogFragment

You don't have to manually create a`FragmentTransaction`to display your`DialogFragment`. Instead, use the`show()`method to display your dialog. You can pass a reference to a`FragmentManager`and a`String`to use as a`FragmentTransaction`tag.

When creating a`DialogFragment`from within a`Fragment`, use the fragment's child`FragmentManager`so that the state properly restores after configuration changes. A non-null tag lets you use`findFragmentByTag()`to retrieve the`DialogFragment`at a later time.  

### Kotlin

```kotlin
// From another Fragment or Activity where you wish to show this
// PurchaseConfirmationDialogFragment.
PurchaseConfirmationDialogFragment().show(
     childFragmentManager, PurchaseConfirmationDialog.TAG)
```

### Java

```java
// From another Fragment or Activity where you wish to show this
// PurchaseConfirmationDialogFragment.
new PurchaseConfirmationDialogFragment().show(
       getChildFragmentManager(), PurchaseConfirmationDialog.TAG);
```

For more control over the[`FragmentTransaction`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction), you can use the[`show()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#show(androidx.fragment.app.FragmentManager,%20java.lang.String))overload that accepts an existing`FragmentTransaction`.
| **Note:** Because the`DialogFragment`automatically restores after configuration changes, consider only calling`show()`based on user actions or when`findFragmentByTag()`returns`null`, indicating that the dialog is not already present.

## DialogFragment lifecycle

A`DialogFragment`follows the standard fragment lifecycle, with a few additional lifecycle callbacks. The most common ones are as follows:

- [`onCreateDialog()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#onCreateDialog(android.os.Bundle)): override this callback to provide a`Dialog`for the fragment to manage and display.
- [`onDismiss()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#onDismiss(android.content.DialogInterface)): override this callback if you need to perform any custom logic when your`Dialog`is dismissed, such as releasing resources or unsubscribing from observable resources.
- [`onCancel()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#onCancel(android.content.DialogInterface)): override this callback if you need to perform any custom logic when your`Dialog`is canceled.

`DialogFragment`also contains methods to dismiss or set the cancelability of your`DialogFragment`:

- [`dismiss()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#dismiss()): dismiss the fragment and its dialog. If the fragment was added to the back stack, all back stack state up to and including this entry are popped. Otherwise, a new transaction is committed to remove the fragment.
- [`setCancelable()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#setCancelable(boolean)): control whether the shown`Dialog`is cancelable. Use this method instead of directly calling[`Dialog.setCancelable(boolean)`](https://developer.android.com/reference/android/app/Dialog#setCancelable(boolean)).

You don't override[`onCreateView()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#oncreateview)or[`onViewCreated()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onViewCreated(android.view.View,%20android.os.Bundle))when using a`DialogFragment`with a`Dialog`. Dialogs aren't only views---they have their own window. As such, it's not enough to override`onCreateView()`. Moreover,`onViewCreated()`is never called on a custom`DialogFragment`unless you've overridden`onCreateView()`and provided a non-null view.
| **Note:** When subscribing to lifecycle-aware components such as`LiveData`, never use[`viewLifecycleOwner`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getviewlifecycleowner)as the[LifecycleOwner](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner)in a`DialogFragment`that uses`Dialog`objects. Instead, use the`DialogFragment`itself, or, if you're using[Jetpack Navigation](https://developer.android.com/guide/navigation), use the[`NavBackStackEntry`](https://developer.android.com/reference/androidx/navigation/NavBackStackEntry).

## Use custom views

You can create a`DialogFragment`and display a dialog by overriding[`onCreateView()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreateView(android.view.LayoutInflater,%20android.view.ViewGroup,%20android.os.Bundle)). You can either give it a`layoutId`, as with a typical fragment, or use the[`DialogFragment`constructor](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#DialogFragment(int)).

The`View`returned by`onCreateView()`is automatically added to the dialog. In most cases, this means that you don't need to override[`onCreateDialog()`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment#onCreateDialog(android.os.Bundle)), as the default empty dialog is populated with your view.

Certain subclasses of`DialogFragment`, such as[`BottomSheetDialogFragment`](https://developer.android.com/reference/com/google/android/material/bottomsheet/BottomSheetDialogFragment), embed your view in a dialog that is styled as a bottom sheet.