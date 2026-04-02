---
title: https://developer.android.com/develop/background-work/background-tasks/awake/screen-on
url: https://developer.android.com/develop/background-work/background-tasks/awake/screen-on
source: md.txt
---

Certain apps need to keep the screen turned on, such as games or movie apps.
Some Android APIs automatically keep the screen on for you. In other cases,
you can set a flag to manually keep the screen on.

> [!NOTE]
> **Note:** Keeping the device's screen on can drain the battery quickly. Ordinarily, you should let the device turn the screen off if the user is not interacting with it. If you do need to keep the screen on, do so for as short a time as possible.

## Manually keep the screen on

To keep the device's screen on, set the [`FLAG_KEEP_SCREEN_ON`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON) flag in your
activity. This flag may only be set in an activity, never in a service or other
app component. For example:

### Kotlin

```kotlin
class MainActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
    }
}
```

### Java

```java
public class MainActivity extends Activity {
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
  }
}
```

Another way to keep the screen on is by setting the
the [`android:keepScreenOn`](https://developer.android.com/reference/android/R.attr#keepScreenOn) attribute
in your application's layout XML file:

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:keepScreenOn="true">
    ...
</RelativeLayout>
```

Using `android:keepScreenOn="true"` is equivalent to using
[`FLAG_KEEP_SCREEN_ON`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON).
You can use whichever approach is best for your app. The advantage of setting
the flag programmatically in your activity is that it gives you the option of
programmatically clearing the flag later and thereby allowing the screen to turn
off.

If an app with the `FLAG_KEEP_SCREEN_ON` flag goes into the background, the
system allows the screen to turn off normally. You don't need to explicitly
clear the flag in this case. If your app no longer needs to keep the screen on,
you should clear the flag. by calling
[`clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)`](https://developer.android.com/reference/android/view/Window#clearFlags(int)).

### Ambient Mode for TV

On TV devices, use [`FLAG_KEEP_SCREEN_ON`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_KEEP_SCREEN_ON) to prevent the device from going
into [Ambient Mode](https://developer.android.com/training/tv/playback/ambient-mode) during active video playback. If the foreground activity
does not set `FLAG_KEEP_SCREEN_ON`, the device automatically enters Ambient Mode
after a period of inactivity.

## See also

- [Keep the device awake](https://developer.android.com/develop/background-work/background-tasks/awake)
- [Use wake locks](https://developer.android.com/develop/background-work/background-tasks/awake/wakelock)