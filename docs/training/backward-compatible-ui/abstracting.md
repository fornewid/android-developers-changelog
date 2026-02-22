---
title: https://developer.android.com/training/backward-compatible-ui/abstracting
url: https://developer.android.com/training/backward-compatible-ui/abstracting
source: md.txt
---

# Abstract the new APIs

Suppose you want to use[action bar tabs](https://developer.android.com/guide/topics/ui/actionbar#Tabs)as the primary form of top-level navigation in your application. Unfortunately, the[ActionBar](https://developer.android.com/reference/android/app/ActionBar)APIs are only available in Android 3.0 or later (API level 11+). Thus, if you want to distribute your application to devices running earlier versions of the platform, you need to provide an implementation that supports the newer API while providing a fallback mechanism that uses older APIs.

In this class, you build a tabbed user interface (UI) component that uses abstract classes with version-specific implementations to provide backward-compatibility. This lesson describes how to create an abstraction layer for the new tab APIs as the first step toward building the tab component.

## Prepare for abstraction

[Abstraction](https://en.wikipedia.org/wiki/Abstraction_(computer_science))in the Java programming language involves the creation of one or more interfaces or abstract classes to hide implementation details. In the case of newer Android APIs, you can use abstraction to build version-aware components that use the current APIs on newer devices, and fallback to older, more compatible APIs on older devices.

When using this approach, you first determine what newer classes you want to be able to use in a backward compatible way, then create abstract classes, based on the public interfaces of the newer classes. In defining the abstraction interfaces, you should mirror the newer API as much as possible. This maximizes forward-compatibility and makes it easier to drop the abstraction layer in the future when it is no longer necessary.

After creating abstract classes for these new APIs, any number of implementations can be created and chosen at runtime. For the purposes of backward-compatibility, these implementations can vary by required API level. Thus, one implementation may use recently released APIs, while others can use older APIs.

## Create an abstract tab interface

In order to create a backward-compatible version of tabs, you should first determine which features and specific APIs your application requires. In the case of top-level section tabs, suppose you have the following functional requirements:

1. Tab indicators should show text and an icon.
2. Tabs can be associated with a fragment instance.
3. The activity should be able to listen for tab changes.

Preparing these requirements in advance allows you to control the scope of your abstraction layer. This means that you can spend less time creating multiple implementations of your abstraction layer and begin using your new backward-compatible implementation sooner.

The key APIs for tabs are in[ActionBar](https://developer.android.com/reference/android/app/ActionBar)and[ActionBar.Tab](https://developer.android.com/reference/android/app/ActionBar.Tab). These are the APIs to abstract in order to make your tabs version-aware. The requirements for this example project call for compatibility back to Eclair (API level 5) while taking advantage of the new tab features in Honeycomb (API Level 11). A diagram of the class structure to support these two implementations and their abstract base classes (or interfaces) is shown below.
![Class diagram of abstract base classes and version-specific implementations.](https://developer.android.com/static/images/training/backward-compatible-ui-classes.png)

**Figure 1.**Class diagram of abstract base classes and version-specific implementations.

## Abstract ActionBar.Tab

Get started on building your tab abstraction layer by creating an abstract class representing a tab, that mirrors the[ActionBar.Tab](https://developer.android.com/reference/android/app/ActionBar.Tab)interface:  

### Kotlin

```kotlin
sealed class CompatTab(val tag: String) {
    ...
    abstract fun getText(): CharSequence
    abstract fun getIcon(): Drawable
    abstract fun getCallback(): CompatTabListener
    abstract fun getFragment(): Fragment

    abstract fun setText(text: String): CompatTab
    abstract fun setIcon(icon: Drawable): CompatTab
    abstract fun setCallback(callback: CompatTabListener): CompatTab
    abstract fun setFragment(fragment: Fragment): CompatTab
    ...
}
```

### Java

```java
public abstract class CompatTab {
    ...
    public abstract CompatTab setText(int resId);
    public abstract CompatTab setIcon(int resId);
    public abstract CompatTab setTabListener(
            CompatTabListener callback);
    public abstract CompatTab setFragment(Fragment fragment);

    public abstract CharSequence getText();
    public abstract Drawable getIcon();
    public abstract CompatTabListener getCallback();
    public abstract Fragment getFragment();
    ...
}
```

You can use an abstract class instead of an interface here to simplify the implementation of common features such as association of tab objects with activities (not shown in the code snippet).

## Abstract ActionBar tab methods

Next, define an abstract class that allows you to create and add tabs to an activity, like[ActionBar.newTab()](https://developer.android.com/reference/android/app/ActionBar#newTab())and[ActionBar.addTab()](https://developer.android.com/reference/android/app/ActionBar#addTab(android.app.ActionBar.Tab)):  

### Kotlin

```kotlin
sealed class TabHelper(protected val activity: FragmentActivity) {
    ...

    abstract fun setUp()

    fun newTab(tag: String): CompatTab {
        // This method is implemented in a later lesson.
    }

    abstract fun addTab(tab: CompatTab)

    ...
}
```

### Java

```java
public abstract class TabHelper {
    ...

    public CompatTab newTab(String tag) {
        // This method is implemented in a later lesson.
    }

    public abstract void addTab(CompatTab tab);

    ...
}
```

In the next lessons, you create implementations for`TabHelper`and`CompatTab`that work across both older and newer platform versions.

### You should also read

- [Action Bar](https://developer.android.com/guide/topics/ui/actionbar)
- [Action Bar Tabs](https://developer.android.com/guide/topics/ui/actionbar#Tabs)