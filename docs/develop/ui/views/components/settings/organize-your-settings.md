---
title: https://developer.android.com/develop/ui/views/components/settings/organize-your-settings
url: https://developer.android.com/develop/ui/views/components/settings/organize-your-settings
source: md.txt
---

# Organize your settings

# Organize your settingsPart of[Android Jetpack](https://developer.android.com/jetpack).

Large and complex settings screens can make it difficult for a user to find a specific setting they want to change. The Preference library offers the following ways to better organize your settings screens.

## Preference categories

If you have several related[`Preference`](https://developer.android.com/jetpack/androidx/releases/preference)objects on a single screen, you can group them using a[`PreferenceCategory`](https://developer.android.com/reference/androidx/preference/PreferenceCategory). A`PreferenceCategory`displays a category title and visually separates the category.

To define a`PreferenceCategory`in XML, wrap the`Preference`tags with a`PreferenceCategory`, as follows:  

```xml
<PreferenceScreen
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <PreferenceCategory
        app:key="notifications_category"
        app:title="Notifications">

        <SwitchPreferenceCompat
            app:key="notifications"
            app:title="Enable message notifications"/>

    </PreferenceCategory>

    <PreferenceCategory
        app:key="help_category"
        app:title="Help">

        <Preference
            app:key="feedback"
            app:summary="Report technical issues or suggest new features"
            app:title="Send feedback"/>

    </PreferenceCategory>

</PreferenceScreen>
```

The result looks like the following:
![An image showing preferences with categories](https://developer.android.com/static/develop/ui/views/components/settings/images/settings-preferencecategory.png)**Figure 1.**Preferences within categories.

## Split your hierarchy into multiple screens

If you have a large number of`Preference`objects or distinct categories, you can display them on separate screens. Each screen is a`PreferenceFragmentCompat`with its own separate hierarchy.`Preference`objects on your initial screen can then link to subscreens that contain related preferences.

Figure 2 shows a simple hierarchy that contains two categories:**Messages** and**Sync**.
![An image showing a preference screen with hierarchies](https://developer.android.com/static/develop/ui/views/components/settings/images/settings-simplehierarchy.png)**Figure 2.**A simple hierarchy with two categories.

Figure 3 shows the same set of preferences split into multiple screens:
![An image showing a hierarchy split into multiple screens](https://developer.android.com/static/develop/ui/views/components/settings/images/settings-screens.png)**Figure 3.**A hierarchy split into multiple screens.

To link screens with a`Preference`, you can declare an`app:fragment`in XML or you can use[`Preference.setFragment()`](https://developer.android.com/reference/androidx/preference/Preference#setFragment(java.lang.String)). Launch the full package name of the`PreferenceFragmentCompat`when the`Preference`is tapped, as shown in the following example:  

```xml
<Preference
        app:fragment="com.example.SyncFragment"
        .../>
```

When a user taps a`Preference`with an associated`Fragment`, the interface method[`PreferenceFragmentCompat.OnPreferenceStartFragmentCallback.onPreferenceStartFragment()`](https://developer.android.com/reference/androidx/preference/PreferenceFragmentCompat.OnPreferenceStartFragmentCallback#onPreferenceStartFragment(androidx.preference.PreferenceFragmentCompat,%20androidx.preference.Preference))is called. This method is where you handle displaying the new screen and where the screen is implemented in the surrounding`Activity`.
| **Note:** if you don't implement`onPreferenceStartFragment()`, a fallback implementation is used instead. While this works in most cases, we strongly recommend implementing this method so you can fully configure transitions between`Fragment`objects and update the title displayed in your`Activity`toolbar, if applicable.

A typical implementation looks similar to the following:  

### Kotlin

```kotlin
class MyActivity : AppCompatActivity(),
    PreferenceFragmentCompat.OnPreferenceStartFragmentCallback {
    ...
    override fun onPreferenceStartFragment(caller: PreferenceFragmentCompat, pref: Preference): Boolean {
        // Instantiate the new Fragment.
        val args = pref.extras
        val fragment = supportFragmentManager.fragmentFactory.instantiate(
                classLoader,
                pref.fragment)
        fragment.arguments = args
        fragment.setTargetFragment(caller, 0)
        // Replace the existing Fragment with the new Fragment.
        supportFragmentManager.beginTransaction()
                .replace(R.id.settings_container, fragment)
                .addToBackStack(null)
                .commit()
        return true
    }
}
```

### Java

```java
public class MyActivity extends AppCompatActivity implements
        PreferenceFragmentCompat.OnPreferenceStartFragmentCallback {
    ...
    @Override
    public boolean onPreferenceStartFragment(PreferenceFragmentCompat caller, Preference pref) {
        // Instantiate the new Fragment.
        final Bundle args = pref.getExtras();
        final Fragment fragment = getSupportFragmentManager().getFragmentFactory().instantiate(
                getClassLoader(),
                pref.getFragment());
        fragment.setArguments(args);
        fragment.setTargetFragment(caller, 0);
        // Replace the existing Fragment with the new Fragment.
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.settings_container, fragment)
                .addToBackStack(null)
                .commit();
        return true;
    }
}
```

### PreferenceScreens

Declaring nested hierarchies within the same XML resource using a nested`&lt;PreferenceScreen&gt;`is no longer supported. Use nested`Fragment`objects instead.

### Use separate Activities

Alternatively, if you need to heavily customize each screen, or if you want full`Activity`transitions between screens, you can use a separate`Activity`for each`PreferenceFragmentCompat`. By doing this, you can fully customize each`Activity`and its corresponding settings screen. For most apps, we don't recommended this; instead, use`Fragments`as previously described.

For more information about launching an`Activity`from a`Preference`, see[Preference actions](https://developer.android.com/guide/topics/ui/settings/customize-your-settings#actions).