---
title: https://developer.android.com/develop/devices/assistant/assistant-sharing
url: https://developer.android.com/develop/devices/assistant/assistant-sharing
source: md.txt
---

# Assistant sharing

Users on Android phones can ask Google Assistant to share app content with another user using a voice command like*"Hey Google, send this to Jane."*Based on the first user's system options, Assistant can then incorporate text from the screen or a device screenshot in the shared content.
![The Assistant inserts a selected photo into a message when prompted.](https://developer.android.com/static/guide/app-actions/images/app-actions-assistant-sharing.gif)**Figure 1.**Assistant shares a photo with a contact.

This method of sharing is often sufficient, but users who receive content shared from your app might not re-enter the app to view content. You can provide Assistant with structured information about the current foreground content by implementing the[`onProvideAssistContent()`](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent))method.

This process helps maintain the structure of data as it's shared to another user. Users who receive shared app content can then be deep linked or receive content directly, instead of as text or as a screenshot.

Implement`onProvideAssistContent()`for any sharable[`entity`](https://developer.android.com/guide/app-actions/legacy/action-schema#entity)in your app.

## Provide content to Assistant

You only need to implement`onProvideAssistContent()`for the final app activity in the user's task flow after invoking the App Action. For example, in a`GET_ITEM_LIST`flow, implement the method in the final screen showing the item list; you don't need to implement it for any in-progress or preview screens.

Provide contextual information as a[JSON-LD](https://json-ld.org/)object[using schema.org vocabulary](https://schema.org/docs/documents.html)in the`structuredData`field of[`AssistContent`](https://developer.android.com/reference/android/app/assist/AssistContent). The following code snippet shows an example of logging contextual content:
Kotlin  

```kotlin
override fun onProvideAssistContent(outContent: AssistContent) {
    super.onProvideAssistContent(outContent)

    // JSON-LD object based on Schema.org structured data
    outContent.structuredData = JSONObject()
            .put("@type", "ItemList")
            .put("name", "My Work items")
            .put("url", "https://my-notes-and-lists.com/lists/12345a")
            .toString()
}
      
```
Java  

```java
@Override
public void onProvideAssistContent(AssistContent outContent) {
  super.onProvideAssistContent(outContent);

  // JSON-LD object based on Schema.org structured data
  outContent.structuredData = new JSONObject()
          .put("@type", "ItemList")
          .put("name", "My Work items")
          .put("url", "https://my-notes-and-lists.com/lists/12345a")
          .toString();
}
      
```

Provide as much data as possible about each`entity`. The following fields are required:

- `@type`
- `.name`
- `.url`(only required if the content is URL-addressable)

To learn more about using`onProvideAssistContent()`, see the[Optimizing Contextual Content for the Assistant](https://developer.android.com/training/articles/assistant)guide.