---
title: Add an action to a message  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/notifications/snackbar/action
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Add an action to a message Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to add notifications in Compose.

[Snackbar →](https://developer.android.com/develop/ui/compose/components/snackbar)

![](/static/images/android-compose-ui-logo.png)

You can add an action to a
`Snackbar`
to let the user respond to your message. When you do this, the
`Snackbar` puts a button next to the message text, and the user can
trigger your action by tapping the button. For example, an email app might put
an *undo* button on its "email archived" message. If the user taps the
*undo* button, the app takes the email back out of the archive.

![An image showing a snackbar with an UNDO action button](/static/images/ui/notifications/action_snackbar_undo.png)


**Figure 1.** A `Snackbar` with an undo action button that
restores a removed item.

To add an action to a `Snackbar` message, define a listener object
that implements the
`View.OnClickListener`
interface. The system calls your listener's
`onClick()`
method if the user taps the message action. For example, this snippet shows a
listener for an undo action:

### Kotlin

```
class MyUndoListener : View.OnClickListener {

  fun onClick(v: View) {
    // Code to undo the user's last action.
  }
}
```

### Java

```
public class MyUndoListener implements View.OnClickListener {

    @Override
    public void onClick(View v) {

        // Code to undo the user's last action.
    }
}
```

Use one of the
`setAction()`
methods to attach the listener to your `Snackbar`. Attach the
listener before you call
`show()`,
as shown in this code sample:

### Kotlin

```
val mySnackbar = Snackbar.make(findViewById(R.id.myCoordinatorLayout),
                               R.string.email_archived, Snackbar.LENGTH_SHORT)
mySnackbar.setAction(R.string.undo_string, MyUndoListener())
mySnackbar.show()
```

### Java

```
Snackbar mySnackbar = Snackbar.make(findViewById(R.id.myCoordinatorLayout),
        R.string.email_archived, Snackbar.LENGTH_SHORT);
mySnackbar.setAction(R.string.undo_string, new MyUndoListener());
mySnackbar.show();
```

If you are using [Jetpack Compose](/jetpack/compose), you can show a
`SnackbarHost`,
as shown in the following example:

### Kotlin

```
    override fun onCreate(savedInstanceState: Bundle?) {

      super.onCreate(savedInstanceState)

      setContent {
          DACPlaygroundTheme {
              val snackbarHostState = remember { SnackbarHostState() }
              val scope = rememberCoroutineScope()
              Scaffold(
                  snackbarHost = { SnackbarHost(snackbarHostState) },
                  content = { padding ->
                      Button(
                          modifier = Modifier.padding(padding),
                          onClick = {
                              scope.launch {
                                  snackbarHostState.showSnackbar(
                                      message = "1 item removed",
                                      actionLabel = "UNDO",
                                      duration = SnackbarDuration.Short
                                  ).run {
                                      when (this) {
                                          Dismissed -> Log.d("SNACKBAR", "Dismissed")
                                          ActionPerformed -> Log.d("SNACKBAR", "UNDO CLICKED")
                                      }
                                  }
                              }
                          }
                      ) { Text("Show snackbar") }
                  }
              )
          }
      }
  }
```

**Note:** A `Snackbar` automatically goes away after a short
time, so the user might not see the message or have a chance to tap the button.
For this reason, offer other ways to perform `Snackbar` actions.