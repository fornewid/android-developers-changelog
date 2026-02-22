---
title: https://developer.android.com/develop/ui/views/components/settings/components-and-attributes
url: https://developer.android.com/develop/ui/views/components/settings/components-and-attributes
source: md.txt
---

# Preference components and attributes

# Preference components and attributesPart of[Android Jetpack](https://developer.android.com/jetpack).

This topic describes some of the most commonly-used`Preference`components and attributes used when building a settings screen.

## Preference components

This section describes common`Preference`components. For more information, see the corresponding reference pages for each component.

### Preference infrastructure

[`PreferenceFragmentCompat`](https://developer.android.com/reference/androidx/preference/PreferenceFragmentCompat)- a[`Fragment`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)that handles displaying an interactive hierarchy of`Preference`objects.

### Preference containers

[`PreferenceScreen`](https://developer.android.com/reference/androidx/preference/PreferenceScreen)- a top-level container that represents a settings screen. This is the root component of your`Preference`hierarchy.

[`PreferenceCategory`](https://developer.android.com/reference/androidx/preference/PreferenceCategory)- a container that is used to group similar`Preferences`. A`PreferenceCategory`displays a category title and visually separates groups of`Preferences`.

### Individual Preferences

[`Preference`](https://developer.android.com/reference/androidx/preference/Preference)- the basic building block that represents an individual setting. If a`Preference`is set to persist, it has a corresponding key-value pair that holds the user's choice for the setting that can be accessed elsewhere in the application.

[`EditTextPreference`](https://developer.android.com/reference/androidx/preference/EditTextPreference)- a`Preference`that persists a`String`value. Users can tap on the`Preference`to launch a dialog containing the text field that allows the user to change the persisted value.

[`ListPreference`](https://developer.android.com/reference/androidx/preference/ListPreference)- a`Preference`that persists a String value. Users can change this value in a dialog that contains a list of radio buttons with corresponding labels.

[`MultiSelectListPreference`](https://developer.android.com/reference/androidx/preference/MultiSelectListPreference)- a`Preference`that persists a set of Strings. Users can change these values in a dialog that contains a list of checkboxes with corresponding labels.

[`SeekBarPreference`](https://developer.android.com/reference/androidx/preference/SeekBarPreference)- a`Preference`that persists an integer value. This value can be changed by dragging a corresponding seekbar that is displayed in the`Preference`layout.

[`SwitchPreferenceCompat`](https://developer.android.com/reference/androidx/preference/SwitchPreferenceCompat)- a`Preference`that persists a boolean value. This value can be changed by interacting with the corresponding switch widget or by tapping on the`Preference`layout.

[`CheckBoxPreference`](https://developer.android.com/reference/androidx/preference/CheckBoxPreference)- a`Preference`that persists a boolean value. This value can be changed by interacting with the corresponding checkbox or by tapping on the`Preference`layout.
| **Note:** Although`SwitchPreferenceCompat`and`CheckBoxPreference`store a boolean value and function in similar ways, we recommend using a`SwitchPreferenceCompat`where possible. For more information, see the[Android Settings Design Guidelines](https://source.android.com/devices/tech/settings/settings-guidelines#checkbox).

## Preference attributes

Listed below are some of the most commonly-used attributes that configure`Preference`appearance and behavior.
| **Note:** Each attribute listed below has a corresponding getter and setter. For mostly static hierarchies, however, we recommend configuring these attributes via the`Preference`XML resource.

### Generic attributes

`title`

:   A`String`value that represents the title of the`Preference`.

    **Example:** `app:title="Title"`

`summary`

:   A`String`value that represents the`Preference`summary.

    **Example:** `app:summary="Summary"`

`icon`

:   A`Drawable`that represents the`Preference`icon.

    **Example:** `app:icon="@drawable/ic_camera"`

`key`

:   A`String`value that represents the key that is used to persist the value for the associated`Preference`. A key allows you to further customize the`Preference`during runtime. You should set a key for each`Preference`in your hierarchy.

    **Example:** `app:key="key"`

`enabled`

:   A boolean value that indicates whether users can interact with the`Preference`. When this value is`false`, the`Preference`appears grayed out, and users cannot interact with it. The default value is`true`.

    **Example:** `app:enabled="false"`

`selectable`

:   A boolean value that indicates whether users can interact with the`Preference`. The default value is`true`.

    **Example:** `app:selectable="false"`

`isPreferenceVisible`

:   A boolean value that indicates whether a`Preference`or`Preference`category is visible. This is equivalent to calling[`setVisible()`](https://developer.android.com/reference/androidx/preference/Preference#setVisible(boolean)).

    **Example:** `app:isPreferenceVisible="false"`

`defaultValue`

:   Represents the default value for a`Preference`. This value is set and persisted when no other persisted value for this`Preference`is found. The value type depends on the associated`Preference`.

    **Example:** `app:defaultValue="true"`

`dependency`

:   Represents the key of a`SwitchPreferenceCompat`that controls the state of this`Preference`. When the corresponding switch is turned off, this`Preference`is disabled and is unable to be modified.

    **Example:** `app:dependency="parent"`

### PreferenceCategory attributes

`initialExpandedChildrenCount`

:   An integer value that enables expandable`Preference`behavior. This value represents the maximum number of children to show in the`PreferenceGroup`. Any extra children are collapsed and can be shown by tapping the expand button. By default, this value is`Integer.MAX_VALUE`, and all children are shown.

    **Warning:** Ensure that you set a key on the`PreferenceCategory`if using this attribute so that the state is correctly saved and restored when the configuration changes (such as when rotating the screen).

    **Example:** `app:initialExpandedChildrenCount="0"`

### ListPreference / MultiSelectListPreference attributes

`entries`

:   An array of Strings that corresponds to the list entries to be displayed to the user. Each of these values correspond by index to the array of values that are internally persisted. For example, when a user selects the first list entry, the first element in the corresponding array of values is persisted.

    **Example:** `app:entries="@array/entries"`

    **Warning:**Ensure the length of both arrays are the same, and the indexes of each array match the correct entry / value pair.

`entryValues`

:   The array of entries to be persisted. Each of these values correspond by index to the array of list entries that are displayed to the user.

    **Example:** `app:entryValues="@array/values"`