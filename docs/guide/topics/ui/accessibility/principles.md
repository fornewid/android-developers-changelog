---
title: https://developer.android.com/guide/topics/ui/accessibility/principles
url: https://developer.android.com/guide/topics/ui/accessibility/principles
source: md.txt
---

# Principles for improving app accessibility

To assist users with accessibility needs, the Android framework lets you create an accessibility service that can present content from apps to users and also operate apps on their behalf.

Android provides several system accessibility services, including the following:

- **[TalkBack](https://support.google.com/accessibility/android/answer/6283677)**: helps people who have low vision or are blind. It announces content through a synthesized voice and performs actions on an app in response to user gestures.
- **[Switch Access](https://support.google.com/accessibility/android/answer/6122836)**: helps people who have motor disabilities. It highlights interactive elements and performs actions in response to the user pressing a button. It allows for controlling the device using only one or two buttons.

To help people with accessibility needs use your app successfully, your app must follow the best practices described on this page, which build on the guidelines described in[Make apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps).

Each of these best practices, described in the sections that follow, can further improve your app's accessibility:

[Label elements](https://developer.android.com/guide/topics/ui/accessibility/principles#label-elements)
:   Users must be able to understand the content and purpose of each interactive and meaningful UI element within your app.

[Add accessibility actions](https://developer.android.com/guide/topics/ui/accessibility/principles#accessibility-actions)
:   By adding accessibility actions, you can enable users of accessibility services to complete critical user flows within your app.

[Extend system widgets](https://developer.android.com/guide/topics/ui/accessibility/principles#system-widgets)
:   Build on the view elements that the framework includes, rather than creating your own custom views. The framework's view and widget classes already provide most of the accessibility capabilities that your app needs.

[Use cues other than color](https://developer.android.com/guide/topics/ui/accessibility/principles#cues-other-than-color)
:   Users must be able to clearly distinguish between categories of elements in a UI. To do so, use patterns and position, along with color, to express these differences.

[Make media content more accessible](https://developer.android.com/guide/topics/ui/accessibility/principles#media-content)
:   Add descriptions to your app's video or audio content so that users who consume this content don't need to rely on entirely visual or aural cues.

## Label elements

It's important to provide users with useful and descriptive labels for each interactive UI element in your app. Each label must explain the meaning and purpose of a particular element. Screen readers such as TalkBack can announce these labels to users.

In most cases, you specify a UI element's description in the layout resource file that contains the element. Usually, you add labels using the`contentDescription`attribute, as explained in the guide to[making apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps#describe-ui-element). There are several other labeling techniques described in the following sections.

### Editable elements

When labeling editable elements, such as[`EditText`](https://developer.android.com/reference/android/widget/EditText)objects, it's helpful to show text that gives an example of valid input in the element itself, in addition to making this example text available to screen readers. In these situations, you can use the`android:hint`attribute, as shown in the following snippet:  

```xml
<!-- The hint text for en-US locale would be
     "Apartment, suite, or building". -->
<EditText
   android:id="@+id/addressLine2"
   android:hint="@string/aptSuiteBuilding" ... />
```

In this situation, the`View`object must have its`android:labelFor`attribute set to the ID of the`EditText`element. For more details, see the following section.

#### Pairs of elements where one describes the other

It's common for an`EditText`element to have a corresponding[`View`](https://developer.android.com/reference/android/view/View)object that describes what users must enter in the`EditText`element. You can indicate this relationship by setting the`View`object's`android:labelFor`attribute.

An example of labeling such element pairs appears in the following snippet:  

```xml
<!-- Label text for en-US locale would be "Username:" -->
<TextView
   android:id="@+id/usernameLabel" ...
   android:text="@string/username"
   android:labelFor="@+id/usernameEntry" />

<EditText
   android:id="@+id/usernameEntry" ... />

<!-- Label text for en-US locale would be "Password:" -->
<TextView
   android:id="@+id/passwordLabel" ...
   android:text="@string/password
   android:labelFor="@+id/passwordEntry" />

<EditText
   android:id="@+id/passwordEntry"
   android:inputType="textPassword" ... />
```

### Elements in a collection

When adding labels to the elements of a collection, each label must be unique. This way, the system's accessibility services can refer to exactly one on-screen element when announcing a label. This correspondence lets users know when they cycle through the UI or when they move focus to an element that they already discovered.

In particular, include additional text or contextual information in elements within reused layouts---such as[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)objects---so that each child element is uniquely identified.

To do so, set the content description as part of your adapter implementation, as shown in the following code snippet:  

### Kotlin

```kotlin
data class MovieRating(val title: String, val starRating: Integer)

class MyMovieRatingsAdapter(private val myData: Array<MovieRating>):
        RecyclerView.Adapter<MyMovieRatingsAdapter.MyRatingViewHolder>() {

    class MyRatingViewHolder(val ratingView: ImageView) :
            RecyclerView.ViewHolder(ratingView)

    override fun onBindViewHolder(holder: MyRatingViewHolder, position: Int) {
        val ratingData = myData[position]
        holder.ratingView.contentDescription = "Movie ${position}: " +
                "${ratingData.title}, ${ratingData.starRating} stars"
    }
}
```

### Java

```java
public class MovieRating {
    private String title;
    private int starRating;
    // ...
    public String getTitle() { return title; }
    public int getStarRating() { return starRating; }
}

public class MyMovieRatingsAdapter
        extends RecyclerView.Adapter<MyAdapter.MyRatingViewHolder> {
    private MovieRating[] myData;


    public static class MyRatingViewHolder extends RecyclerView.ViewHolder {
        public ImageView ratingView;
        public MyRatingViewHolder(ImageView iv) {
            super(iv);
            ratingView = iv;
        }
    }

    @Override
    public void onBindViewHolder(MyRatingViewHolder holder, int position) {
        MovieRating ratingData = myData[position];
        holder.ratingView.setContentDescription("Movie " + position + ": " +
                ratingData.getTitle() + ", " + ratingData.getStarRating() +
                " stars")
    }
}
```

### Groups of related content

If your app displays several UI elements that form a natural group, such as details of a song or attributes of a message, arrange these elements within a container, which is usually a subclass of`ViewGroup`. Set the container object's[`android:screenReaderFocusable`](https://developer.android.com/reference/android/view/View#attr_android:screenReaderFocusable)attribute to`true`, and each inner object's[`android:focusable`](https://developer.android.com/reference/android/view/View#attr_android:focusable)attribute to`false`. This way, accessibility services can present the inner elements' content descriptions, one after the other, in a single announcement. This consolidation of related elements helps users of assistive technology discover the information on the screen more efficiently.
| **Note:** On Android 4.4 (API level 19) and lower, the`android:screenReaderFocusable`attribute isn't available, so set the container's`android:focusable`attribute instead.

The following snippet contains pieces of content that relate to one another, so the container element, an instance of`ConstraintLayout`, has its`android:screenReaderFocusable`attribute set to`true`and the inner`TextView`elements each have their`android:focusable`attribute set to`false`:  

```xml
<!-- In response to a single user interaction, accessibility services announce
     both the title and the artist of the song. -->
<ConstraintLayout
    android:id="@+id/song_data_container" ...
    android:screenReaderFocusable="true">

    <TextView
        android:id="@+id/song_title" ...
        android:focusable="false"
        android:text="@string/<var translate="no">my_song_title</var>" />
    <TextView
        android:id="@+id/song_artist"
        android:focusable="false"
        android:text="@string/<var translate="no">my_songwriter</var>" />
</ConstraintLayout>
```

Because accessibility services announce the inner elements' descriptions in a single utterance, it's important to keep each description as short as possible while still conveying the element's meaning.  
**Note:**In general, you should avoid creating a content description for a group by aggregating the text of its children. Doing so makes the group's description brittle, and when the text of a child changes, the group's description may no longer match the visible text.

In a list or a grid context, a screenreader may consolidate the text of a list or grid element's child text nodes. It is best to avoid modifying this announcement.

#### Nested groups

If your app's interface presents multidimensional information, such as a day-by-day list of festival events, use the`android:screenReaderFocusable`attribute on the inner group containers. This labeling scheme provides a good balance between the number of announcements needed to discover the screen's content and the length of each announcement.

The following code snippet shows one method of labeling groups inside of larger groups:  

```xml
<!-- In response to a single user interaction, accessibility services
     announce the events for a single stage only. -->
<ConstraintLayout
    android:id="@+id/festival_event_table" ... >
    <ConstraintLayout
        android:id="@+id/stage_a_event_column"
        android:screenReaderFocusable="true">

        <!-- UI elements that describe the events on Stage A. -->

    </ConstraintLayout>
    <ConstraintLayout
        android:id="@+id/stage_b_event_column"
        android:screenReaderFocusable="true">

        <!-- UI elements that describe the events on Stage B. -->

    </ConstraintLayout>
</ConstraintLayout>
```

### Headings within text

Some apps use*headings* to summarize groups of text that appear on screen. If a particular`View`element represents a heading, you can indicate its purpose for accessibility services by setting the element's[`android:accessibilityHeading`](https://developer.android.com/reference/android/view/View#attr_android:accessibilityHeading)attribute to`true`.

Users of accessibility services can choose to navigate between headings instead of between paragraphs or between words. This flexibility improves the text navigation experience.

### Accessibility pane titles

In Android 9 (API level 28) and higher, you can provide accessibility-friendly titles for a screen's*panes*. For accessibility purposes, a pane is a visually distinct portion of a window, such as the contents of a fragment. For accessibility services to understand a pane's window-like behavior, give descriptive titles to your app's panes. Accessibility services can then provide more granular information to users when a pane's appearance or content changes.

To specify the title of a pane, use the[`android:accessibilityPaneTitle`](https://developer.android.com/reference/android/R.attr#accessibilityPaneTitle)attribute, as shown in the following snippet:  

```xml
<!-- Accessibility services receive announcements about content changes
     that are scoped to either the "shopping cart view" section (top) or
     "browse items" section (bottom) -->
<MyShoppingCartView
     android:id="@+id/shoppingCartContainer"
     android:accessibilityPaneTitle="@string/shoppingCart" ... />

<MyShoppingBrowseView
     android:id="@+id/browseItemsContainer"
     android:accessibilityPaneTitle="@string/browseProducts" ... />
```

### Decorative elements

If an element in your UI exists only for visual spacing or visual appearance purposes, set its[`android:importantForAccessibility`](https://developer.android.com/reference/android/view/View#attr_android:importantForAccessibility)attribute to`"no"`.

## Add accessibility actions

It's important to allow users of accessibility services to easily perform all user flows within your app. For example, if a user can swipe on an item in a list, this action can also be exposed to accessibility services so users have an alternate way to complete the same user flow.

### Make all actions accessible

A user of TalkBack,[Voice Access](https://support.google.com/accessibility/android/answer/6151848), or Switch Access might need alternate ways to complete certain user flows within the app. For actions associated with gestures such as drag-and-drop or swipes, your app can expose the actions in a way that is accessible to users of accessibility services.

Using[accessibility actions](https://developer.android.com/reference/kotlin/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.AccessibilityActionCompat), the app can provide alternative ways for users to complete an action.

For example, if your app allows users to swipe on an item, you can also expose the functionality through a custom accessibility action, like this:  

### Kotlin

```kotlin
ViewCompat.addAccessibilityAction(
    // View to add accessibility action
    itemView,
    // Label surfaced to user by an accessibility service
    getText(R.id.archive)
) { _, _ ->
    // Same method executed when swiping on itemView
    archiveItem()
    true
}
```

### Java

```java
ViewCompat.addAccessibilityAction(
    // View to add accessibility action
    itemView,
    // Label surfaced to user by an accessibility service
    getText(R.id.archive),
    (view, arguments) -> {
        // Same method executed when swiping on itemView
        archiveItem();
        return true;
    }
);
```

Withthecustomaccessibilityactionimplemented,userscanaccesstheactionthroughtheactionsmenu.

### Makeavailableactionsunderstandable

Whenaviewsupportsactionssuchastouch\&hold,anaccessibilityservicesuchasTalkBackannouncesitas"Double tap and hold to long press."

Thisgenericannouncementdoesn'tgivetheuseranycontextaboutwhatatouch\&holdactiondoes.

Tomakethisannouncementmoredescriptive,youcanreplacetheaccessibilityaction'sannouncementlikeso:  

### Kotlin

```kotlin
ViewCompat.replaceAccessibilityAction(
    // View that contains touch & hold action
    itemView,
    AccessibilityNodeInfoCompat.AccessibilityActionCompat.ACTION_LONG_CLICK,
    // Announcement read by TalkBack to surface this action
    getText(R.string.favorite),
    null
)
```

### Java

```java
ViewCompat.replaceAccessibilityAction(
    // View that contains touch & hold action
    itemView,
    AccessibilityNodeInfoCompat.AccessibilityActionCompat.ACTION_LONG_CLICK,
    // Announcement read by TalkBack to surface this action
    getText(R.string.favorite),
    null
);
```

ThisresultsinTalkBackannouncing"Double tap and hold to favorite,"helpingusersunderstandthepurposeoftheaction.

## Extendsystemwidgets

**Note:** Whenyoudesignyourapp'sUI,useorextendsystem-providedwidgetsthatareasfardownAndroid'sclasshierarchyaspossible.System-providedwidgetsthatarefardownthehierarchyalreadyhavemostoftheaccessibilitycapabilitiesyourappneeds.It'seasiertoextendthesesystem-providedwidgetsthantocreateyourownfromthemoregeneric[View](https://developer.android.com/reference/kotlin/android/view/View),[ViewCompat](https://developer.android.com/reference/kotlin/androidx/core/view/ViewCompat),[Canvas](https://developer.android.com/reference/kotlin/android/graphics/Canvas),and[CanvasCompat](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/canvas/CanvasCompat.java)classes.

IfyoumustextendVieworCanvasdirectly,whichmightbenecessaryforahighlycustomizedexperienceoragamelevel,see[Makecustomviewsmoreaccessible](https://developer.android.com/guide/topics/ui/accessibility/custom-views).

Thissectionusestheexampleofimplementingaspecialtypeof[Switch](https://developer.android.com/reference/android/widget/Switch)calledTriSwitchwhilefollowingbestpracticesaroundextendingsystemwidgets.ATriSwitchobjectworkssimilarlytoaSwitchobject,exceptthateachinstanceofTriSwitchallowstheusertotoggleamongthreepossiblestates.

### Extendfromfardowntheclasshierarchy

TheSwitchobjectinheritsfromseveralframeworkUIclassesinitshierarchy:

```
View
↳ TextView
  ↳ Button
    ↳ CompoundButton
      ↳ Switch
```

It's best for the new`TriSwitch`class to extend directly from the`Switch`class. This way, the[Android accessibility framework](https://developer.android.com/reference/kotlin/android/view/accessibility/package-summary)provides most of the accessibility capabilities the`TriSwitch`class needs:

- **Accessibility actions:** information for the system about how accessibility services can emulate each possible user input that's performed on a`TriSwitch`object. (Inherited from`View`.)
- **Accessibility events:** information for accessibility services about every possible way that a`TriSwitch`object's appearance can change when the screen refreshes or updates. (Inherited from`View`.)
- **Characteristics:** details about each`TriSwitch`object, such as the contents of any text that it displays. (Inherited from`TextView`.)
- **State information:** description of a`TriSwitch`object's current state, such as "checked" or "unchecked." (Inherited from`CompoundButton`.)
- **Text description of state:** text-based explanation of what each state represents. (Inherited from`Switch`.)

This behavior from`Switch`and its superclasses is almost the same behavior for`TriSwitch`objects. Therefore, your implementation can focus on expanding the number of possible states from two to three.

### Define custom events

When you extend a system widget, you likely change an aspect of how users interact with that widget. It's important to define these interaction changes so that accessibility services can update your app's widget as if the user interacts with the widget directly.

A general guideline is that for every view-based callback you override, you also need to redefine the corresponding accessibility action by overriding[`ViewCompat.replaceAccessibilityAction()`](https://developer.android.com/reference/androidx/core/view/ViewCompat#replaceAccessibilityAction(android.view.View,%20androidx.core.view.accessibility.AccessibilityNodeInfoCompat.AccessibilityActionCompat,%20java.lang.CharSequence,%20androidx.core.view.accessibility.AccessibilityViewCommand)). In your app's tests, you can validate the behavior of these redefined actions by calling[`ViewCompat.performAccessibilityAction()`](https://developer.android.com/reference/androidx/core/view/ViewCompat#performAccessibilityAction(android.view.View,%20int,%20android.os.Bundle)).

#### How this principle can work for TriSwitch objects

Unlike an ordinary`Switch`object, tapping a`TriSwitch`object cycles through three possible states. Therefore, the corresponding`ACTION_CLICK`accessibility action needs to be updated:  

### Kotlin

```kotlin
class TriSwitch(context: Context) : Switch(context) {
    // 0, 1, or 2
    var currentState: Int = 0
        private set

    init {
        updateAccessibilityActions()
    }

    private fun updateAccessibilityActions() {
        ViewCompat.replaceAccessibilityAction(this, ACTION_CLICK,
            <var translate="no"><span class="devsite-syntax-n">action</span><span class="devsite-syntax-o">-</span><span class="devsite-syntax-n">label</span></var>) {
            view, args -> moveToNextState()
        })
    }

    private fun moveToNextState() {
        currentState = (currentState + 1) % 3
    }
}
```

### Java

```java
public class TriSwitch extends Switch {
    // 0, 1, or 2
    private int currentState;

    public int getCurrentState() {
        return currentState;
    }

    public TriSwitch() {
        updateAccessibilityActions();
    }

    private void updateAccessibilityActions() {
        ViewCompat.replaceAccessibilityAction(this, ACTION_CLICK,
            <var translate="no"><span class="devsite-syntax-n">action</span><span class="devsite-syntax-o">-</span><span class="devsite-syntax-n">label</span></var>, (view, args) -> moveToNextState());
    }

    private void moveToNextState() {
        currentState = (currentState + 1) % 3;
    }
}
```

## Use cues other than color

To assist users with color vision deficiencies, use cues other than color to distinguish UI elements within your app's screens. These techniques can include using different shapes or sizes, providing text or visual patterns, or adding audio- or touch-based (haptic) feedback to mark the elements' differences.

Figure 1 shows two versions of an activity. One version uses only color to distinguish between two possible actions in a workflow. The other version uses the best practice of including shapes and text in addition to color to highlight the differences between the two options:
![](https://developer.android.com/static/images/guide/topics/ui/accessibility/cues-other-than-color.svg)**Figure 1.**Examples of creating UI elements using color only (left) and using color, shapes, and text (right).

## Make media content more accessible

If you're developing an app that includes media content, such as a video clip or an audio recording, try to support users with different types of accessibility needs in understanding this material. In particular, we encourage you to do the following:

- Include controls that allow users to pause or stop the media, change the volume, and toggle subtitles (captions).
- If a video presents information that is vital to completing a workflow, provide the same content in an alternate format, such as a transcript.

## Additional resources

To learn more about making your app more accessible, see the following additional resources:

### Codelabs

- [Starting Android accessibility](https://codelabs.developers.google.com/codelabs/basic-android-accessibility/)

### Blog posts

- [Accessibility: Are You Serving All Your Users?](https://android-developers.googleblog.com/2012/04/accessibility-are-you-serving-all-your.html)