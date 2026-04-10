---
title: https://developer.android.com/develop/ui/views/components/menus
url: https://developer.android.com/develop/ui/views/components/menus
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to add components in Compose. [Menus →](https://developer.android.com/develop/ui/compose/components/menu) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Menus are a common user interface component in many types of apps. To
provide a familiar and consistent user experience, use the
`https://developer.android.com/reference/android/view/Menu` APIs to
present user actions and other options in your activities.
| **Note:** For a better user experience, see [Material Design
| Menus](https://m3.material.io/components/menus/overview).
![An image showing an example of overflow menu](https://lh3.googleusercontent.com/kyUjfdA4kbCLZTJCQY0gqPCCVdTr74WMzCScfyuZkFGx8GQXU6uVvcSExckK28csQqWAdLXvLiQpD1a_DpJlX2c15GD4bLYrNu4c_W7-AOE6og=s0) **Figure 1.** A menu triggered by an icon tap, appearing below the overflow menu icon.

This document shows how to create the three fundamental types of menus or
action presentations on all versions of Android:

**Options menu and app bar**

:   The options menu is the primary collection of menu items for an activity. It's where you place actions that have a global impact on the app, such as "Search," "Compose email," and "Settings." See the [Create an options menu](https://developer.android.com/develop/ui/views/components/menus#options-menu)
    section.

**Context menu and contextual action mode**
:   A context menu is a [floating menu](https://developer.android.com/develop/ui/views/components/menus#FloatingContextMenu)
    that appears when the user performs a touch \& hold on an element. It
    provides actions that affect the selected content or context frame.

    The [contextual action mode](https://developer.android.com/develop/ui/views/components/menus#CAB) displays action items that
    affect the selected content in a bar at the top of the screen and lets the
    user select multiple items.

    See the [Create a contextual menu](https://developer.android.com/develop/ui/views/components/menus#context-menu)
    section.

**Popup menu**

:   A popup menu displays a vertical list of items that's anchored to the view that invokes the menu. It's good for providing an overflow of actions that relate to specific content or to provide options for the second part of a command. Actions in a popup menu don't directly affect the corresponding content---that's what contextual actions are for. Rather, the popup menu is for extended actions that relate to regions of content in your activity. See the [Create a popup menu](https://developer.android.com/develop/ui/views/components/menus#PopupMenu) section.

## Define a menu in XML

For all menu types, Android provides a standard XML format to define menu
items. Instead of building a menu in your activity's code, define a menu and
all its items in an XML
[menu resource](https://developer.android.com/guide/topics/resources/menu-resource). You can
then inflate the menu resource---loading it as a `Menu`
object---in your activity or fragment.

Using a menu resource is good practice for the following reasons:

- It's easier to visualize the menu structure in XML.
- It separates the content for the menu from your app's behavioral code.
- It lets you create alternative menu configurations for different platform versions, screen sizes, and other configurations by leveraging the [app resources](https://developer.android.com/guide/topics/resources) framework.

To define a menu, create an XML file inside your project's
`res/menu/` directory and build the menu with the following
elements:

`<menu>`
:   Defines a `Menu`, which is a container for menu items. A
    `<menu>` element must be the root node for the file, and it
    can hold one or more `<item>` and `<group>`
    elements.

`<item>`
:   Creates a
    `https://developer.android.com/reference/android/view/MenuItem`,
    which represents a single item in a menu. This element can contain a nested
    `<menu>` element to create a submenu.

`<group>`
:   An optional, invisible container for `<item>`
    elements. It lets you categorize menu items so they share properties, such
    as active state and visibility. For more information, see the
    [Create a menu group](https://developer.android.com/develop/ui/views/components/menus#groups) section.

Here's an example menu named `game_menu.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/new_game"
          android:icon="@drawable/ic_new_game"
          android:title="@string/new_game"
          app:showAsAction="ifRoom"/>
    <item android:id="@+id/help"
          android:icon="@drawable/ic_help"
          android:title="@string/help" />
</menu>
```

The `<item>` element supports several attributes you can use
to define an item's appearance and behavior. The items in the preceding menu
include the following attributes:

`android:id`
:   A resource ID that's unique to the item, which lets the app
    recognize the item when
    the user selects it.

`android:icon`
:   A reference to a drawable to use as the item's icon.

`android:title`
:   A reference to a string to use as the item's title.

`android:showAsAction`
:   The specification for when and how this item appears as an action item
    in the app bar.

These are the most important attributes you use, but there are many more
available. For information about all the supported attributes, see the
[Menu resource](https://developer.android.com/guide/topics/resources/menu-resource)
documentation.

You can add a submenu to an item in any menu by adding a
`<menu>` element as the child of an `<item>`.
Submenus are useful when your app has a lot of functions that can be organized
into topics, like items in a PC app's menu bar---such as **File** ,
**Edit** , and **View**. See the following example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/file"
          android:title="@string/file" >
        <!-- "file" submenu -->
        <menu>
            <item android:id="@+id/create_new"
                  android:title="@string/create_new" />
            <item android:id="@+id/open"
                  android:title="@string/open" />
        </menu>
    </item>
</menu>
```

To use the menu in your activity, _inflate_ the menu resource, converting
the XML resource into a programmable object using
`https://developer.android.com/reference/android/view/MenuInflater#inflate(int, android.view.Menu)`.
The following sections show how to inflate a menu for each menu type.

## Create an options menu

The options menu, like the one shown in figure 1, is where you include
actions and other options that are relevant to the current activity context,
such as "Search," "Compose email," and "Settings."
![An image showing the app bar for the Google Sheets app](https://developer.android.com/static/images/training/appbar/appbar_sheets_2x.png) **Figure 2.** The Google Sheets app, showing several buttons, including the action overflow button.

You can declare items for the options menu from your
`https://developer.android.com/reference/android/app/Activity`
subclass or a
`https://developer.android.com/reference/android/app/Fragment`
subclass. If both your activity and your fragments declare items for the
options menu, the items are combined in the UI. The activity's items appear
first, followed by those of each fragment, in the order in which the fragments
are added to the activity. If necessary, you can reorder the menu items with
the `android:orderInCategory` attribute in each
`<item>` you need to move.

To specify the options menu for an activity, override
`https://developer.android.com/reference/android/app/Activity#onCreateOptionsMenu(android.view.Menu)`.
Fragments provide their own
`https://developer.android.com/reference/android/app/Fragment#onCreateOptionsMenu(android.view.Menu, android.view.MenuInflater)`
callback. In this method, you can inflate your menu resource,
[defined in XML](https://developer.android.com/develop/ui/views/components/menus#xml), into the `Menu` provided in the
callback. This is shown in the following example:

### Kotlin

```kotlin
override fun onCreateOptionsMenu(menu: Menu): Boolean {
    val inflater: MenuInflater = menuInflater
    inflater.inflate(R.menu.game_menu, menu)
    return true
}
```

### Java

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    MenuInflater inflater = getMenuInflater();
    inflater.inflate(R.menu.game_menu, menu);
    return true;
}
```

You can also add menu items using
`https://developer.android.com/reference/android/view/Menu#add(int, int, int, int)`
and retrieve items with
`https://developer.android.com/reference/android/view/Menu#findItem(int)`
to revise their properties with `MenuItem` APIs.

### Handle click events

When the user selects an item from the options menu, including action items
in the app bar, the system calls your activity's
`https://developer.android.com/reference/android/app/Activity#onOptionsItemSelected(android.view.MenuItem)`
method. This method passes the `MenuItem` selected. You can identify
the item by calling
`https://developer.android.com/reference/android/view/MenuItem#getItemId()`,
which returns the unique ID for the menu item, defined by the
`android:id` attribute in the menu resource or with an integer given
to the `add()` method. You can match this ID against known menu
items to perform the appropriate action.

### Kotlin

```kotlin
override fun onOptionsItemSelected(item: MenuItem): Boolean {
    // Handle item selection.
    return when (item.itemId) {
        R.id.new_game -> {
            newGame()
            true
        }
        R.id.help -> {
            showHelp()
            true
        }
        else -> super.onOptionsItemSelected(item)
    }
}
```

### Java

```java
@Override
public boolean onOptionsItemSelected(MenuItem item) {
    // Handle item selection.
    switch (item.getItemId()) {
        case R.id.new_game:
            newGame();
            return true;
        case R.id.help:
            showHelp();
            return true;
        default:
            return super.onOptionsItemSelected(item);
    }
}
```

When you successfully handle a menu item, return `true`. If you
don't handle the menu item, call the superclass implementation of
`onOptionsItemSelected()`. The default implementation returns
false.

If your activity includes fragments, the system first calls
`onOptionsItemSelected()` for the activity, then for each fragment
in the order the fragments are added, until one returns `true` or
all fragments are called.
| **Tip:** If your app contains multiple activities and some of them provide the same options menu, consider creating an activity that implements only the `onCreateOptionsMenu()` and `onOptionsItemSelected()` methods. Then extend this class for each activity that shares the same options menu. This way, you can manage one set of code for handling menu actions, and each descendant class inherits the menu behaviors. If you want to add menu items to one of the descendant activities, override `>onCreateOptionsMenu()` in that activity. Call `super.onCreateOptionsMenu(menu)` so the original menu items are created, then add new menu items with `menu.add()`. You can also override the superclass's behavior for individual menu items.

### Change menu items at runtime

After the system calls `onCreateOptionsMenu()`, it retains an
instance of the `Menu` you populate and doesn't call
`onCreateOptionsMenu()` again unless the menu is invalidated.
However, use `onCreateOptionsMenu()` only to create the initial menu
state and not to make changes during the activity lifecycle.

If you want to modify the options menu based on events that occur during the
activity lifecycle, you can do so in the
`https://developer.android.com/reference/android/app/Activity#onPrepareOptionsMenu(android.view.Menu)`
method. This method passes you the `Menu` object as it currently
exists so you can modify it, such as by adding, removing, or disabling items.
Fragments also provide an
`https://developer.android.com/reference/android/app/Fragment#onPrepareOptionsMenu(android.view.Menu)`
callback.

The options menu is considered always open when menu items are presented in
the app bar. When an event occurs and you want to perform a menu update, call
`https://developer.android.com/reference/android/app/Activity#invalidateOptionsMenu()`
to request that the system call `onPrepareOptionsMenu()`.
| **Note:** Never change items in the options menu based on the `https://developer.android.com/reference/android/view/View` in focus. When in touch mode---when the user isn't using a trackball or D-pad---views can't take focus, so never use focus as the basis for modifying items in the options menu. If you want to provide menu items that are context-sensitive to a `View`, use a contextual menu as described in the following section.

## Create a contextual menu

![An image showing a floating context menu](https://developer.android.com/static/develop/ui/views/images/context_menu_no_icons.png) **Figure 3.** A floating context menu.

A contextual menu offers actions that affect a specific item or context
frame in the UI. You can provide a context menu for any view, but they are most
often used for items in a
`https://developer.android.com/develop/ui/views/layout/recyclerview` or
other view collections in which the user can perform direct actions on each
item.

There are two ways to provide contextual actions:

- In a [floating context menu](https://developer.android.com/develop/ui/views/components/menus#FloatingContextMenu). A menu appears as a floating list of menu items, similar to a dialog, when the user performs a touch \& hold on a view that declares support for a context menu. Users can perform a contextual action on one item at a time.
- In the [contextual action mode](https://developer.android.com/develop/ui/views/components/menus#CAB). This mode is a system implementation of `https://developer.android.com/reference/android/view/ActionMode` that displays a *contextual action bar*, or CAB, at the top of the screen with action items that affect the selected item(s). When this mode is active, users can perform an action on multiple items at once, if your app supports that.

**Note:** [Context menu](https://developer.android.com/reference/android/view/Menu) do not support item shortcuts and item icons.

### Create a floating context menu

To provide a floating context menu, do the following:

1. Register the `View` the context menu is associated with by calling `https://developer.android.com/reference/android/app/Activity#registerForContextMenu(android.view.View)` and passing it the `View`.

   If your activity uses a `RecyclerView` and you want each
   item to provide the same context menu, register all items for a context
   menu by passing the `RecyclerView` to
   `registerForContextMenu()`.
2. Implement the `https://developer.android.com/reference/android/view/View.OnCreateContextMenuListener#onCreateContextMenu(android.view.ContextMenu, android.view.View, android.view.ContextMenu.ContextMenuInfo)` method in your `Activity` or `Fragment`.

   When the registered view receives a touch \& hold event, the system calls
   your `onCreateContextMenu()` method. This is where you define
   the menu items, usually by inflating a menu resource, as in the following
   example:

   ### Kotlin

   ```kotlin
       override fun onCreateContextMenu(menu: ContextMenu, v: View,
                               menuInfo: ContextMenu.ContextMenuInfo) {
           super.onCreateContextMenu(menu, v, menuInfo)
           val inflater: MenuInflater = menuInflater
           inflater.inflate(R.menu.context_menu, menu)
       }
       
   ```

   ### Java

   ```java
       @Override
       public void onCreateContextMenu(ContextMenu menu, View v,
                                       ContextMenuInfo menuInfo) {
           super.onCreateContextMenu(menu, v, menuInfo);
           MenuInflater inflater = getMenuInflater();
           inflater.inflate(R.menu.context_menu, menu);
       }
       
   ```

   `https://developer.android.com/reference/android/view/MenuInflater`
   lets you inflate the context menu from a menu resource. The callback method
   parameters include the `View` that the user selects and a
   `https://developer.android.com/reference/android/view/ContextMenu.ContextMenuInfo`
   object that provides additional information about the item selected. If
   your activity has several views that each provide a different context menu,
   you might use these parameters to determine which context menu to
   inflate.
3. Implement
   `https://developer.android.com/reference/android/app/Activity#onContextItemSelected(android.view.MenuItem)`,
   as shown in the following example. When the user selects a menu item, the
   system calls this method so you can perform the appropriate action.

   ### Kotlin

   ```kotlin
       override fun onContextItemSelected(item: MenuItem): Boolean {
           val info = item.menuInfo as AdapterView.AdapterContextMenuInfo
           return when (item.itemId) {
               R.id.edit -> {
                   editNote(info.id)
                   true
               }
               R.id.delete -> {
                   deleteNote(info.id)
                   true
               }
               else -> super.onContextItemSelected(item)
           }
       }
       
   ```

   ### Java

   ```java
       @Override
       public boolean onContextItemSelected(MenuItem item) {
           AdapterContextMenuInfo info = (AdapterContextMenuInfo) item.getMenuInfo();
           switch (item.getItemId()) {
               case R.id.edit:
                   editNote(info.id);
                   return true;
               case R.id.delete:
                   deleteNote(info.id);
                   return true;
               default:
                   return super.onContextItemSelected(item);
           }
       }
       
   ```

   The `https://developer.android.com/reference/android/view/MenuItem#getItemId()`
   method queries the ID for the selected menu item, which you assign to each
   menu item in XML using the `android:id` attribute, as shown in
   [Define a menu in XML](https://developer.android.com/develop/ui/views/components/menus#xml).

   When you successfully handle a menu item, return `true`. If
   you don't handle the menu item, pass the menu item to the superclass
   implementation. If your activity includes fragments, the activity receives
   this callback first. By calling the superclass when unhandled, the system
   passes the event to the respective callback method in each fragment, one at
   a time, in the order each fragment is added, until `true` or
   `false` is returned. The default implementations for
   `Activity` and `android.app.Fragment` return
   `false`, so always call the superclass when unhandled.

### Use the contextual action mode

The contextual action mode is a system implementation of
`ActionMode` that focuses user interaction toward performing
contextual actions. When a user enables this mode by selecting an item, a
*contextual action bar* appears at the top of the screen to present
actions the user can perform on the selected items. While this mode is enabled,
the user can select multiple items, if your app supports that, and can deselect
items and continue to navigate within the activity. The action mode is disabled
and the contextual action bar disappears when the user deselects all items,
taps the Back button, or taps the **Done** action on the left side of the
bar.
| **Note:** The contextual action bar isn't necessarily associated with the app bar. They operate independently, although the contextual action bar visually overtakes the app bar position.

For views that provide contextual actions, you usually invoke the contextual
action mode when one or both of these two events occurs:

- The user performs a touch \& hold on the view.
- The user selects a checkbox or similar UI component within the view.

How your app invokes the contextual action mode and defines the
behavior for each action depends on your design. There are two designs:

- For contextual actions on individual, arbitrary views.
- For batch contextual actions on groups of items in a `RecyclerView`, letting the user select multiple items and perform an action on them all.

The following sections describe the setup required for the first scenario.

#### Enable the contextual action mode for individual views

If you want to invoke the contextual action mode only when the user selects
specific views, do the following:

1. Implement the `ActionMode.Callback` interface as shown in the following example. In its callback methods, you can specify the actions for the contextual action bar, respond to click events on action items, and handle other lifecycle events for the action mode.

   ### Kotlin

   ```kotlin
       private val actionModeCallback = object : ActionMode.Callback {
           // Called when the action mode is created. startActionMode() is called.
           override fun onCreateActionMode(mode: ActionMode, menu: Menu): Boolean {
               // Inflate a menu resource providing context menu items.
               val inflater: MenuInflater = mode.menuInflater
               inflater.inflate(R.menu.context_menu, menu)
               return true
           }

           // Called each time the action mode is shown. Always called after
           // onCreateActionMode, and might be called multiple times if the mode
           // is invalidated.
           override fun onPrepareActionMode(mode: ActionMode, menu: Menu): Boolean {
               return false // Return false if nothing is done
           }

           // Called when the user selects a contextual menu item.
           override fun onActionItemClicked(mode: ActionMode, item: MenuItem): Boolean {
               return when (item.itemId) {
                   R.id.menu_share -> {
                       shareCurrentItem()
                       mode.finish() // Action picked, so close the CAB.
                       true
                   }
                   else -> false
               }
           }

           // Called when the user exits the action mode.
           override fun onDestroyActionMode(mode: ActionMode) {
               actionMode = null
           }
       }
       
   ```

   ### Java

   ```java
       private ActionMode.Callback actionModeCallback = new ActionMode.Callback() {

           // Called when the action mode is created. startActionMode() is called.
           @Override
           public boolean onCreateActionMode(ActionMode mode, Menu menu) {
               // Inflate a menu resource providing context menu items.
               MenuInflater inflater = mode.getMenuInflater();
               inflater.inflate(R.menu.context_menu, menu);
               return true;
           }

           // Called each time the action mode is shown. Always called after
           // onCreateActionMode, and might be called multiple times if the mode
           // is invalidated.
           @Override
           public boolean onPrepareActionMode(ActionMode mode, Menu menu) {
               return false; // Return false if nothing is done.
           }

           // Called when the user selects a contextual menu item.
           @Override
           public boolean onActionItemClicked(ActionMode mode, MenuItem item) {
              switch (item.getItemId()) {
                   case R.id.menu_share:
                       shareCurrentItem();
                       mode.finish(); // Action picked, so close the CAB.
                       return true;
                   default:
                       return false;
               }
           }

           // Called when the user exits the action mode.
           @Override
           public void onDestroyActionMode(ActionMode mode) {
               actionMode = null;
           }
       };
       
   ```

   These event callbacks are almost exactly the same as the callbacks for
   the [options menu](https://developer.android.com/develop/ui/views/components/menus#options-menu), except that each of these
   also passes the `ActionMode` object associated with the event.
   You can use `ActionMode` APIs to make various changes to the
   CAB, such as revising the title and subtitle with
   `https://developer.android.com/reference/android/view/ActionMode#setTitle(int)`
   and
   `https://developer.android.com/reference/android/view/ActionMode#setSubtitle(int)`,
   which is useful to indicate how many items are selected.

   The preceding sample sets the `actionMode` variable to
   `null` when the action mode is destroyed. In the next step, see
   how it's initialized and how saving the member variable in your activity or
   fragment can be useful.
2. Call `https://developer.android.com/reference/android/app/Activity#startActionMode(android.view.ActionMode.Callback)` when you want to show the bar, such as when the user performs a touch \& hold on the view.

   ### Kotlin

   ```kotlin
       someView.setOnLongClickListener { view ->
           // Called when the user performs a touch & hold on someView.
           when (actionMode) {
               null -> {
                   // Start the CAB using the ActionMode.Callback defined earlier.
                   actionMode = activity?.startActionMode(actionModeCallback)
                   view.isSelected = true
                   true
               }
               else -> false
           }
       }
       
   ```

   ### Java

   ```java
       someView.setOnLongClickListener(new View.OnLongClickListener() {
           // Called when the user performs a touch & hold on someView.
           public boolean onLongClick(View view) {
               if (actionMode != null) {
                   return false;
               }

               // Start the CAB using the ActionMode.Callback defined earlier.
               actionMode = getActivity().startActionMode(actionModeCallback);
               view.setSelected(true);
               return true;
           }
       });
       
   ```

   When you call `startActionMode()`, the system returns the
   `ActionMode` created. By saving this in a member variable, you
   can make changes to the contextual action bar in response to other events.
   In the preceding sample, the `ActionMode` is used to ensure that
   the `ActionMode` instance isn't recreated if it's already
   active, by checking whether the member is null before starting the action
   mode.

## Create a popup menu

![An image showing a popup menu in the Gmail app, anchored to the overflow button at the top-right.](https://developer.android.com/static/images/ui/popupmenu.png) **Figure 4.** A popup menu in the Gmail app, anchored to the overflow button in the top-right corner.

A `https://developer.android.com/reference/android/widget/PopupMenu`
is a modal menu anchored to a `View`. It appears below the anchor
view if there is room, or above the view otherwise. It's useful for the
following:

- Providing an overflow-style menu for actions that *relate to* specific content, such as Gmail's email headers, shown in figure 4. **Note:** This isn't the same as a context menu, which is generally for actions that *affect* selected content. For actions that affect selected content, use the [contextual action mode](https://developer.android.com/develop/ui/views/components/menus#CAB) or [floating context menu](https://developer.android.com/develop/ui/views/components/menus#FloatingContextMenu).
- Providing a second part of a command sentence, such as a button marked **Add** that produces a popup menu with different **Add** options.
- Providing a menu similar to a `https://developer.android.com/reference/android/widget/Spinner` that doesn't retain a persistent selection.

If you [define your menu in XML](https://developer.android.com/develop/ui/views/components/menus#xml), here's how you can show
the popup menu:

1. Instantiate a `PopupMenu` with its constructor, which takes the current app `https://developer.android.com/reference/android/content/Context` and the `View` to which the menu is anchored.
2. Use `MenuInflater` to inflate your menu resource into the `Menu` object returned by `https://developer.android.com/reference/android/widget/PopupMenu#getMenu()`.
3. Call `https://developer.android.com/reference/android/widget/PopupMenu#show()`.

For example, here's a button that shows a popup menu:

```xml
<ImageButton
    android:id="@+id/dropdown_menu"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:contentDescription="@string/descr_overflow_button"
    android:src="@drawable/arrow_drop_down" />
```

The activity can then show the popup menu like this:

### Kotlin

```kotlin
findViewById<ImageButton>(R.id.dropdown_menu).setOnClickListener {
    val popup = PopupMenu(this, it)
    val inflater: MenuInflater = popup.menuInflater
    inflater.inflate(R.menu.actions, popup.menu)
    popup.show()
}
```

### Java

```java
findViewById(R.id.dropdown_menu).setOnClickListener(v -> {
    PopupMenu popup = new PopupMenu(this, v);
    popup.getMenuInflater().inflate(R.menu.actions, popup.getMenu());
    popup.show();
});
```

The menu is dismissed when the user selects an item or taps outside the menu
area. You can listen for the dismiss event using
`https://developer.android.com/reference/android/widget/PopupMenu.OnDismissListener`.

### Handle click events

To perform an action when the user selects a menu item, implement the
`https://developer.android.com/reference/android/widget/PopupMenu.OnMenuItemClickListener`
interface and register it with your `PopupMenu` by calling
`https://developer.android.com/reference/android/widget/PopupMenu#setOnMenuItemClickListener(android.widget.PopupMenu.OnMenuItemClickListener)`.
When the user selects an item, the system calls the
`https://developer.android.com/reference/android/widget/PopupMenu.OnMenuItemClickListener#onMenuItemClick(android.view.MenuItem)`
callback in your interface.

This is shown in the following example:

### Kotlin

```kotlin
fun showMenu(v: View) {
    PopupMenu(this, v).apply {
        // MainActivity implements OnMenuItemClickListener.
        setOnMenuItemClickListener(this@MainActivity)
        inflate(R.menu.actions)
        show()
    }
}

override fun onMenuItemClick(item: MenuItem): Boolean {
    return when (item.itemId) {
        R.id.archive -> {
            archive(item)
            true
        }
        R.id.delete -> {
            delete(item)
            true
        }
        else -> false
    }
}
```

### Java

```java
public void showMenu(View v) {
    PopupMenu popup = new PopupMenu(this, v);

    // This activity implements OnMenuItemClickListener.
    popup.setOnMenuItemClickListener(this);
    popup.inflate(R.menu.actions);
    popup.show();
}

@Override
public boolean onMenuItemClick(MenuItem item) {
    switch (item.getItemId()) {
        case R.id.archive:
            archive(item);
            return true;
        case R.id.delete:
            delete(item);
            return true;
        default:
            return false;
    }
}
```

## Create a menu group

A menu group is a collection of menu items that share certain traits. With a
group, you can do the following:

- Show or hide all items using `https://developer.android.com/reference/android/view/Menu#setGroupVisible(int, boolean)`.
- Enable or disable all items using `https://developer.android.com/reference/android/view/Menu#setGroupEnabled(int, boolean)`.
- Specify whether all items are checkable using `https://developer.android.com/reference/android/view/Menu#setGroupCheckable(int, boolean, boolean)`.

You can create a group by nesting `<item>` elements inside
a `<group>` element in your menu resource or by specifying a
group ID with the
`https://developer.android.com/reference/android/view/Menu#add(int, int, int, int)`
method.

Here's an example of a menu resource that includes a group:

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@+id/menu_save"
          android:icon="@drawable/menu_save"
          android:title="@string/menu_save" />
    <!-- menu group -->
    <group android:id="@+id/group_delete">
        <item android:id="@+id/menu_archive"
              android:title="@string/menu_archive" />
        <item android:id="@+id/menu_delete"
              android:title="@string/menu_delete" />
    </group>
</menu>
```

The items that are in the group appear at the same level as the first
item---all three items in the menu are siblings. However, you can modify
the traits of the two items in the group by referencing the group ID and using
the preceding methods. The system also never separates grouped items. For
example, if you declare `android:showAsAction="ifRoom"` for each
item, they both appear in the action bar or both appear in the action
overflow.

### Use checkable menu items

**Figure 5.** A submenu with checkable items.

A menu can be useful as an interface for turning options on and off, using a
checkbox for standalone options, or radio buttons for groups of mutually
exclusive options. Figure 5 shows a submenu with items that are checkable with
radio buttons.
| **Note:** Menu items in an options menu can't display a checkbox or radio button. If you make items in an options menu checkable, manually indicate the checked state by swapping the icon or text, or both, each time the state changes.

You can define the checkable behavior for individual menu items using the
`android:checkable` attribute in the `<item>`
element, or for an entire group with the `android:checkableBehavior`
attribute in the `<group>` element. For example, all items in
this menu group are checkable with a radio button:

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <group android:checkableBehavior="single">
        <item android:id="@+id/red"
              android:title="@string/red" />
        <item android:id="@+id/blue"
              android:title="@string/blue" />
    </group>
</menu>
```

The `android:checkableBehavior` attribute accepts one of the
following:

`single`
:   Only one item from the group can be checked, resulting in radio
    buttons.

`all`
:   All items can be checked, resulting in checkboxes.

`none`
:   No items are checkable.

You can apply a default checked state to an item using the
`android:checked` attribute in the `<item>` element
and change it in code with the
`https://developer.android.com/reference/android/view/MenuItem#setChecked(boolean)`
method.

When a checkable item is selected, the system calls your respective
item-selected callback method, such as `onOptionsItemSelected()`.
This is where you set the state of the checkbox, because a checkbox or radio
button doesn't change its state automatically. You can query the current state
of the item---as it was before the user selected it---with
`https://developer.android.com/reference/android/view/MenuItem#isChecked()`
and then set the checked state with `setChecked()`. This is shown in
the following example:

### Kotlin

```kotlin
override fun onOptionsItemSelected(item: MenuItem): Boolean {
    return when (item.itemId) {
        R.id.vibrate, R.id.dont_vibrate -> {
            item.isChecked = !item.isChecked
            true
        }
        else -> super.onOptionsItemSelected(item)
    }
}
```

### Java

```java
@Override
public boolean onOptionsItemSelected(MenuItem item) {
    switch (item.getItemId()) {
        case R.id.vibrate:
        case R.id.dont_vibrate:
            if (item.isChecked()) item.setChecked(false);
            else item.setChecked(true);
            return true;
        default:
            return super.onOptionsItemSelected(item);
    }
}
```

If you don't set the checked state this way, then the visible state of the
checkbox or radio button doesn't change when the user selects it. When you do
set the state, the activity preserves the checked state of the item so that
when the user opens the menu later, the checked state that you set is
visible.
| **Note:** Checkable menu items are intended to be used only on a per-session basis and not saved after the app is destroyed. If you have app settings that you want to save for the user, store the data using [shared storage](https://developer.android.com/guide/topics/data/data-storage).

## Add menu items based on an intent

Sometimes you want a menu item to launch an activity using an
`https://developer.android.com/reference/android/content/Intent`,
whether it's an activity in your app or another app. When you
know the intent you want to use and have a specific menu item that initiates
the intent, you can execute the intent with
`https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)`
during the appropriate on-item-selected callback method, such as the
`onOptionsItemSelected()` callback.

However, if you aren't certain that the user's device contains an app that
handles the intent, then adding a menu item that invokes it can result in a
non-functioning menu item, because the intent might not resolve to an activity.
To solve this, Android lets you dynamically add menu items to your menu when
Android finds activities on the device that handle your intent.

To add menu items based on available activities that accept an intent, do
the following:

1. Define an intent with the category `https://developer.android.com/reference/android/content/Intent#CATEGORY_ALTERNATIVE` or `https://developer.android.com/reference/android/content/Intent#CATEGORY_SELECTED_ALTERNATIVE`, or both, plus any other requirements.
2. Call `https://developer.android.com/reference/android/view/Menu#addIntentOptions(int, int, int, android.content.ComponentName, android.content.Intent[], android.content.Intent, int, android.view.MenuItem[])`. Android then searches for any apps that can perform the intent and adds them to your menu.

If there are no apps installed that satisfy the intent, then no menu
items are added.
| **Note:** `CATEGORY_SELECTED_ALTERNATIVE` is used to handle the selected element on the screen. Only use it when creating a menu in `https://developer.android.com/reference/android/app/Activity#onCreateContextMenu(android.view.ContextMenu, android.view.View, android.view.ContextMenu.ContextMenuInfo)`.

This is shown in the following example:

### Kotlin

```kotlin
override fun onCreateOptionsMenu(menu: Menu): Boolean {
    super.onCreateOptionsMenu(menu)

    // Create an Intent that describes the requirements to fulfill, to be
    // included in the menu. The offering app must include a category value
    // of Intent.CATEGORY_ALTERNATIVE.
    val intent = Intent(null, dataUri).apply {
        addCategory(Intent.CATEGORY_ALTERNATIVE)
    }

    // Search and populate the menu with acceptable offering apps.
    menu.addIntentOptions(
            R.id.intent_group,  // Menu group to which new items are added.
            0,                  // Unique item ID (none).
            0,                  // Order for the items (none).
            this.componentName, // The current activity name.
            null,               // Specific items to place first (none).
            intent,             // Intent created above that describes the requirements.
            0,                  // Additional flags to control items (none).
            null)               // Array of MenuItems that correlate to specific items (none).

    return true
}
```

### Java

```java
@Override
public boolean onCreateOptionsMenu(Menu menu){
    super.onCreateOptionsMenu(menu);

    // Create an Intent that describes the requirements to fulfill, to be
    // included in the menu. The offering app must include a category value
    // of Intent.CATEGORY_ALTERNATIVE.
    Intent intent = new Intent(null, dataUri);
    intent.addCategory(Intent.CATEGORY_ALTERNATIVE);

    // Search and populate the menu with acceptable offering apps.
    menu.addIntentOptions(
         R.id.intent_group,         // Menu group to which new items are added.
         0,                         // Unique item ID (none).
         0,                         // Order for the items (none).
         this.getComponentName(),   // The current activity name.
         null,                      // Specific items to place first (none).
         intent,                    // Intent created above that describes the requirements.
         0,                         // Additional flags to control items (none).
         null);                     // Array of MenuItems that correlate to specific items (none).

    return true;
}
```

For each activity found that provides an intent filter matching the intent
defined, a menu item is added, using the value in the intent filter's
`android:label` as the menu item title and the app icon as the menu
item icon. The `addIntentOptions()` method returns the number of
menu items added.
| **Note:** When you call `addIntentOptions()`, it overrides all menu items by the menu group specified in the first argument.

### Let your activity be added to other menus

You can offer the services of your activity to other apps so your app can be
included in the menu of others---reversing the roles described earlier.

To be included in other app menus, define an intent filter as usual,
but include the `CATEGORY_ALTERNATIVE` or
`CATEGORY_SELECTED_ALTERNATIVE` values, or both, for the intent
filter category. This is shown in the following example:

```xml
<intent-filter label="@string/resize_image">
    ...
    <category android:name="android.intent.category.ALTERNATIVE" />
    <category android:name="android.intent.category.SELECTED_ALTERNATIVE" />
    ...
</intent-filter>
```

Read more about writing intent filters in
[Intents and intent
filters](https://developer.android.com/guide/components/intents-filters).