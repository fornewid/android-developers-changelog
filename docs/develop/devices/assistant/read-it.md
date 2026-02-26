---
title: https://developer.android.com/develop/devices/assistant/read-it
url: https://developer.android.com/develop/devices/assistant/read-it
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

Read It is a Google Assistant feature available on Android devices that offers
another way for users to read long-form web content like news articles and
blog posts. Users can say something like *"Hey Google, read it"* to have an app
read web-based content out loud, highlight the words being read, and auto-scroll
the page. To learn more about this feature, you can also read the
[Read It product update post](https://www.blog.google/products/assistant/easier-access-web-pages-let-assistant-read-it-aloud/).
![When prompted, an app reads web content on the screen out loud with
the help of the Google Assistant.](https://developer.android.com/static/guide/app-actions/images/read-it-blog-post.gif) **Figure 1.** Listening to an app read web content out loud.

Android apps with web-based content can support Read It by providing information
to Assistant using the [`onProvideAssistContent()`](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent)) method.

This process helps maintain the structure of data as it's shared with
Assistant. Users who receive shared app content can then be deep linked or
receive content directly, instead of as text or a screenshot.

Implement `onProvideAssistContent()` for any web-based content
and any sharable [`entity`](https://developer.android.com/guide/app-actions/legacy/action-schema#entity) in your app.

## Provide content to Assistant

For Read It to access your content, your app must provide Assistant with
information about the content, like its web URI and some basic context.
Assistant can then retrieve your content to be read out loud to the user.

For
Android apps that already implement [web-based content](https://developer.android.com/guide/webapps) using WebViews or
Chrome Custom Tabs, use the same web URIs for Read It as a
starting point.

When combining Read It functionality with built-in intents, you only need to
implement `onProvideAssistContent()` for the final app activity in the user's
task flow after invoking the App Action.

For example, if your app displays
news articles, implement `onProvideAssistContent()` in the final screen
showing the article; you don't need to implement it for any in-progress or
preview screens.

Provide a web URI for your content in the `uri` field of [`AssistContent`](https://developer.android.com/reference/android/app/assist/AssistContent).
Provide contextual information as a [JSON-LD](https://json-ld.org/) object
[using schema.org vocabulary](https://schema.org/docs/documents.html) in the
`structuredData` field.

> [!NOTE]
> **Note:** Read It functionality is not available for content that requires authentication, such as articles locked for users without a subscription.

The following code snippet shows an example of providing content to Assistant:

### Kotlin

```kotlin
override fun onProvideAssistContent(outContent: AssistContent) {
    super.onProvideAssistContent(outContent)

    // Set the web URI for content to be read from a
    // WebView, Chrome Custom Tab, or other source
    val urlString = url.toString()
    outContent.setWebUri(Uri.parse(urlString))

    // Create JSON-LD object based on schema.org structured data
    val structuredData = JSONObject()
        .put("@type", "Article")
        .put("name", "ExampleName of blog post")
        .put("url", outContent.getWebUri())
        .toString()
    outContent.setStructuredData(structuredData)
}
```

### Java

```java
@Override
public void onProvideAssistContent(AssistContent outContent) {

  // Set the web URI for content to be read from a
  // WebView, Chrome Custom Tab, or other source
  String urlString = url.toString();
  outContent.setWebUri(Uri.parse(urlString));

  try {
      // Create JSON-LD object based on schema.org structured data
      String structuredData = new JSONObject()
          .put("@type", "Article")
          .put("name", "ExampleName of blog post")
          .put("url", outContent.getWebUri())
          .toString();
      outContent.setStructuredData(structuredData);
  } catch (JSONException ex) {
      // Handle exception
      Log.e(TAG, ex.getMessage());
  }

  super.onProvideAssistContent(outContent);
}
```

When implementing `onProvideAssistContent()`, provide as much
data as possible about each `entity`. The following
fields are required:

- `@type`
- `.name`
- `.url` (only required if the content is URL-addressable)

To learn more about using [`onProvideAssistContent()`](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent)), see the
[Optimizing Contextual Content for the Assistant](https://developer.android.com/training/articles/assistant) guide in
the Android developer documentation.