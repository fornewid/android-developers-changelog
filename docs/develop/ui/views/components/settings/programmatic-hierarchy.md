---
title: Create a hierarchy in code  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/components/settings/programmatic-hierarchy
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

Stay organized with collections

Save and categorize content based on your preferences.



# Create a hierarchy in code   Part of [Android Jetpack](/jetpack).

You can create a hierarchy programmatically in
[`onCreatePreferences()`](/reference/androidx/preference/PreferenceFragmentCompat#oncreatepreferences).
The following example demonstrates a programmatic approach to creating the same
preference screen created through XML on the
[overview](/develop/ui/views/components/settings#create_a_hierarchy) page. To
create the screen programmatically, create each setting and set its relevant
properties, then add it to the preference screen:

### Kotlin

```
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

```
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
[`PreferenceCategory`](/reference/androidx/preference/PreferenceCategory) is
similar. The following example demonstrates a programmatic approach to creating
the preference screen seen in
[Organize your settings](/develop/ui/views/components/settings/organize-your-settings#preference_categories).
The children are added to the `PreferenceCategory` and not to the root
`PreferenceScreen`.

### Kotlin

```
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

```
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

**Warning:** Add the `PreferenceCategory` to the `PreferenceScreen` before adding
children to it. Preferences can't be added to a `PreferenceCategory` that isn't
attached to the root screen.