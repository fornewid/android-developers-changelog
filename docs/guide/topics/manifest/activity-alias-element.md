---
title: https://developer.android.com/guide/topics/manifest/activity-alias-element
url: https://developer.android.com/guide/topics/manifest/activity-alias-element
source: md.txt
---

syntax:
:

    ```xml
    <activity-alias android:enabled=["true" | "false"]
                    android:exported=["true" | "false"]
                    android:icon="drawable resource"
                    android:intentMatchingFlags=["none" | "enforceIntentFilter" | "allowNullAction"]
                    android:label="string resource"
                    android:name="string"
                    android:permission="string"
                    android:targetActivity="string" >
        ...
    </activity-alias>
    ```

contained in:
:   `https://developer.android.com/guide/topics/manifest/application-element`

can contain:
:   `https://developer.android.com/guide/topics/manifest/intent-filter-element`

    `https://developer.android.com/guide/topics/manifest/meta-data-element`

    `https://developer.android.com/guide/topics/manifest/property-element`

description:
:   An alias for an activity, named by the `targetActivity`
    attribute. The target must be in the same application as the
    alias and declared before the alias in the manifest.


    The alias presents the target activity as an independent entity, and can have its own set of intent
    filters. They, rather than the
    intent filters on the target activity itself, determine which intents
    can activate the target through the alias and how the system
    treats the alias.

    For example, the intent filters on the alias might
    specify the `https://developer.android.com/reference/android/content/Intent#ACTION_MAIN`
    and `https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER`" flags, causing it to
    be represented in the application launcher, even though none of the
    filters on the target activity itself set these flags.


    With the exception of `targetActivity`, `<activity-alias>`
    attributes are a subset of `https://developer.android.com/guide/topics/manifest/activity-element` attributes.
    For attributes in the subset, none of the values set for the target carry over
    to the alias. However, for attributes not in the subset, the values set for
    the target activity also apply to the alias.

attributes:
:

    `android:enabled`
    :   Whether the target activity can be instantiated by the system through
        this alias. `"true"` if it can be, and `"false"` if not.
        The default value is `"true"`.


        The `https://developer.android.com/guide/topics/manifest/application-element` element has its own
        `https://developer.android.com/guide/topics/manifest/application-element#enabled` attribute that applies to all
        application components, including activity aliases. The
        `<application>` and `<activity-alias>`
        attributes must both be `"true"` for the system to be able to instantiate
        the target activity through the alias. If either is `"false"`, the alias
        doesn't work.

    `android:exported`
    :   Whether the components of other applications can launch the target activity
        through this alias. `"true"` if they can, and `"false"` if not.
        If `"false"`, the target activity can be launched through the alias only by
        components of the same application as the alias or applications with the same user ID.


        The default value depends on whether the alias contains intent filters. The
        absence of any filters means that the activity can be invoked through the alias
        only by specifying the exact name of the alias. This implies that the alias
        is intended only for application-internal use, since others don't know its name.
        So, the default value is `"false"`.
        On the other hand, the presence of at least one filter implies that the alias
        is intended for external use, so the default value is `"true"`.

    `android:icon`
    :   An icon for the target activity when presented to users through the alias.
        For more information, see the `https://developer.android.com/guide/topics/manifest/activity-element` element's
        `https://developer.android.com/guide/topics/manifest/activity-element#icon` attribute.

    `android:intentMatchingFlags`

    :
        Use this attribute to fine-tune how the system matches incoming intents to app
        components. By default, no special matching rules are applied.


        The value set on an `<activity-alias>` tag overrides the
        value set on the target `<activity>` or inherited from the
        `<application>` for that specific alias. If not explicitly
        defined on the alias, it inherits the behavior from the target activity or
        the application.


        The value must be one or more of the following flags, separated by '`|`':

        | Flag | Description |
        |---|---|
        | `none` | Disables all special matching rules for incoming intents. When specifying multiple flags, conflicting values are resolved by giving precedence to the `none` flag. |
        | `enforceIntentFilter` | Enforces stricter matching for incoming intents: - Explicit intents must match the target component's intent filter. - Intents without an action don't match any intent filter. |
        | `allowNullAction` | Relaxes the matching rules to allow intents without an action to match. This flag is used in conjunction with `enforceIntentFilter` to achieve the following behavior: - Explicit intents must match the target component's intent filter. - Intents without an action are allowed to match any intent filter. |

        For more information, see the
        [Safer Intents](https://developer.android.com/about/versions/16/behavior-changes-16#safer-intents)
        section in the Android 16 (API level 36) behavior changes.

    `android:label`
    :   A user-readable label for the alias when presented to users through the alias.
        For more information, see the `https://developer.android.com/guide/topics/manifest/activity-element` element's
        `https://developer.android.com/guide/topics/manifest/activity-element#label` attribute.

    `android:name`
    :   A unique name for the alias. The name resembles a fully qualified class
        name. Unlike the name of the target activity, the alias name is arbitrary. It
        doesn't refer to an actual class.

    `android:permission`
    :   The name of a permission that clients must have to launch the target activity
        or get it to do something using the alias. If a caller of
        `https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)` or
        `https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent, int)`
        isn't granted the specified permission, the target activity isn't activated.

        This attribute supplants any permission set for the target activity itself. If
        it isn't set, a permission isn't needed to activate the target through the alias.


        For more information about permissions, see the
        [Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro#perms)
        section in the app manifest overview.

    `android:targetActivity`
    :   The name of the activity that can be activated through the alias.
        This name must match the `name` attribute of an
        `https://developer.android.com/guide/topics/manifest/activity-element` element that precedes
        the alias in the manifest.

introduced in:
:   API level 1

see also:
:   `https://developer.android.com/guide/topics/manifest/activity-element`