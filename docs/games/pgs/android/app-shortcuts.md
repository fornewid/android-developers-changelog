---
title: https://developer.android.com/games/pgs/android/app-shortcuts
url: https://developer.android.com/games/pgs/android/app-shortcuts
source: md.txt
---

The Play Games services may automatically add [app shortcuts](https://developer.android.com/develop/ui/views/launch/shortcuts), for
example to allow users to quickly choose the Play Games Services profile to use.
The app shortcuts could be added or removed based on the number of the accounts
on the device and the game usage.

## Available shortcuts

**Profile switcher** : shortcut for players to switch between different Play
Games Profiles. See [How to switch Play Games profiles](https://support.google.com/googleplay/answer/14754238), for
corresponding Help Center article.

## Manage the Play Games services populated app shortcuts

In case your game actively uses the app shortcuts, you could limit the number of
app shortcuts populated by the Play Games services. For that add a
[meta-data](https://developer.android.com/guide/topics/manifest/meta-data-element)
element to any `"android.intent.category.LAUNCHER"` activity declaration,
setting the following:

- `android:name` to `"com.google.android.gms.games.APP_SHORTCUTS_MAX_NUMBER"`
- `android:value` to the maximum number of the app shortcuts slots that can be used by the Play Games services.

### Example

In this example, we show how to limit the maximum number of the app shortcuts
slots that the Play Games services can use to **two** . For our example, we
initially would have an
[app manifest](https://developer.android.com/guide/topics/manifest/manifest-intro)
that looks like the following:

    <manifest ... >
        <application ... >
            <activity android:name=".ExampleActivity" >
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity >
            ...
        </application >
        ...
    </manifest >

And to apply the limits the app manifest should be updated to the following:

    <manifest ... >
        <application ... >
            <activity android:name=".ExampleActivity" >
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
                <meta-data
                    android:name="com.google.android.gms.games.APP_SHORTCUTS_MAX_NUMBER"
                    android:value="2" />
            </activity >
            ...
        </application >
        ...
    </manifest >

That's it. Now the maximum number of the app shortcuts slots that the Play Games
services can use is limited to **two**.