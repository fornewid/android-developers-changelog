---
title: https://developer.android.com/develop/ui/views/components/settings/programmatic-hierarchy
url: https://developer.android.com/develop/ui/views/components/settings/programmatic-hierarchy
source: md.txt
---

# Create a hierarchy in code
Part of [Android Jetpack](https://developer.android.com/jetpack).

You can create a hierarchy programmatically in
[`onCreatePreferences()`](https://developer.android.com/reference/androidx/preference/PreferenceFragmentCompat#oncreatepreferences).
The following example demonstrates a programmatic approach to creating the same
preference screen created through XML on the
[overview](https://developer.android.com/develop/ui/views/components/settings#create_a_hierarchy) page. To
create the screen programmatically, create each setting and set its relevant
properties, then add it to the preference screen:

### Kotlin

```kotlin
override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
    val context = preferenceManager.context
    val screen = preferenceManager.createPreferenceScreen(context)

    val notificationPreference = SwitchPreferenceCompat(context)
    notificationPreference.key = "notifications"
    notificationPreference.title = "Enable message notifications"

    val feedbackPreference = Preference(context)
    feedbackPreference.key = "feedback"
    feedbackPreference.title = "Send feedback"
    feedbackPreference.summary = "Report technical issues or suggest new features"

    screen.addPreference(notificationPreference)
    screen.addPreference(feedbackPreference)

    preferenceScreen = screen
}
```

### Java

```java
@Override
public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
    Context context = getPreferenceManager().getContext();
    PreferenceScreen screen = getPreferenceManager().createPreferenceScreen(context);

    SwitchPreferenceCompat notificationPreference = new SwitchPreferenceCompat(context);
    notificationPreference.setKey("notifications");
    notificationPreference.setTitle("Enable message notifications");

    Preference feedbackPreference = new Preference(context);
    feedbackPreference.setKey("feedback");
    feedbackPreference.setTitle("Send feedback");
    feedbackPreference.setSummary("Report technical issues or suggest new features");

    screen.addPreference(notificationPreference);
    screen.addPreference(feedbackPreference);

    setPreferenceScreen(screen);
}
```

Adding a
[`PreferenceCategory`](https://developer.android.com/reference/androidx/preference/PreferenceCategory) is
similar. The following example demonstrates a programmatic approach to creating
the preference screen seen in
[Organize your settings](https://developer.android.com/develop/ui/views/components/settings/organize-your-settings#preference_categories).
The children are added to the `PreferenceCategory` and not to the root
`PreferenceScreen`.

### Kotlin

```kotlin
override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
    val context = preferenceManager.context
    val screen = preferenceManager.createPreferenceScreen(context)

    val notificationPreference = SwitchPreferenceCompat(context)
    notificationPreference.key = "notifications"
    notificationPreference.title = "Enable message notifications"

    val notificationCategory = PreferenceCategory(context)
    notificationCategory.key = "notifications_category"
    notificationCategory.title = "Notifications"
    screen.addPreference(notificationCategory)
    notificationCategory.addPreference(notificationPreference)

    val feedbackPreference = Preference(context)
    feedbackPreference.key = "feedback"
    feedbackPreference.title = "Send feedback"
    feedbackPreference.summary = "Report technical issues or suggest new features"

    val helpCategory = PreferenceCategory(context)
    helpCategory.key = "help"
    helpCategory.title = "Help"
    screen.addPreference(helpCategory)
    helpCategory.addPreference(feedbackPreference)

    preferenceScreen = screen
}
```

### Java

```java
@Override
public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
    Context context = getPreferenceManager().getContext();
    PreferenceScreen screen = getPreferenceManager().createPreferenceScreen(context);

    SwitchPreferenceCompat notificationPreference = new SwitchPreferenceCompat(context);
    notificationPreference.setKey("notifications");
    notificationPreference.setTitle("Enable message notifications");

    PreferenceCategory notificationCategory = new PreferenceCategory(context);
    notificationCategory.setKey("notifications_category");
    notificationCategory.setTitle("Notifications");
    screen.addPreference(notificationCategory);
    notificationCategory.addPreference(notificationPreference);

    Preference feedbackPreference = new Preference(context);
    feedbackPreference.setKey("feedback");
    feedbackPreference.setTitle("Send feedback");
    feedbackPreference.setSummary("Report technical issues or suggest new features");

    PreferenceCategory helpCategory = new PreferenceCategory(context);
    helpCategory.setKey("help");
    helpCategory.setTitle("Help");
    screen.addPreference(helpCategory);
    helpCategory.addPreference(feedbackPreference);

    setPreferenceScreen(screen);
}
```

> [!WARNING]
> **Warning:** Add the `PreferenceCategory` to the `PreferenceScreen` before adding children to it. Preferences can't be added to a `PreferenceCategory` that isn't attached to the root screen.