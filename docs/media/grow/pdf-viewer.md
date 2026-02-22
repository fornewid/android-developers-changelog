---
title: https://developer.android.com/media/grow/pdf-viewer
url: https://developer.android.com/media/grow/pdf-viewer
source: md.txt
---

# Android PDF viewer

The Jetpack PDF viewer library, backed by framework APIs, offers a ready-made, performant solution for PDF document--related applications on Android.

The PDF viewer library ([androidx.pdf](https://developer.android.com/jetpack/androidx/releases/pdf)), provides an embeddable PDF viewer UI that enables users to do the following:

- Open and view PDF documents
- Search and select content
- Zoom and scroll
- Save document annotations
- Interact with PDFs using a stylus

You can create a full-featured PDF experience by integrating the Jetpack library APIs or using the framework APIs directly.

## Jetpack PDF library

The Jetpack PDF library provides the[`PdfViewerFragment`](https://developer.android.com/reference/kotlin/androidx/pdf/viewer/fragment/PdfViewerFragment)class which renders PDF documents, including paginated PDFs. Each page is rendered in its own view.`PdfViewerFragment`displays a floating action button for annotation support and typically includes a button or other UI control that opens a search menu.

To learn how to implement`PdfViewerFragment`, see[Implement a PDF viewer](https://developer.android.com/media/grow/implement-pdf-viewer).

## Framework APIs

The Jetpack library uses framework APIs to parse and load PDF documents.`PdfRenderer`provides the basic framework APIs related to PDF rendering.

Prior to Android V (API level 35), the[`PdfRenderer`](https://developer.android.com/reference/kotlin/android/graphics/pdf/PdfRenderer)and[`PdfRenderer.Page`](https://developer.android.com/reference/kotlin/android/graphics/pdf/PdfRenderer.Page)classes provided the APIs for PDF handling. The`PdfRenderer`and`PdfRenderer.Page`classes have been updated in Android V with advanced PDF capabilities.

### `PdfRenderer`

#### APIs prior to Android V

- `getPageCount()`--- Gets the number of pages in the document.
- `openPage(index: Int)`--- Opens a page for rendering.
- `shouldScaleForPrinting()`--- Gets whether the document should be scaled for printing. Take this information into account if the document is rendered for printing and the target media size differs from the page size.

#### APIs added in Android V

- `PdfRenderer(fileDescriptor: ParcelFileDescriptor, params: LoadParams)`--- Constructs a new instance. Supports loading password protected PDFs.
- `getDocumentLinearizedType()`--- Returns the linearized type of document for PDFs that are less than 1KB.
- `getPdfFormType()`--- Returns the form type of the loaded PDF.
- `write(destination: ParcelFileDescriptor, removePasswordProtection:
  Boolean)`--- Saves the state of the currently loaded document to the writable file descriptor passed as an argument.

### `PdfRenderer.Page`

The`PdfRenderer.Page`class represents a PDF document page for rendering.

#### APIs prior to Android V

- `RENDER_MODE_FOR_DISPLAY`--- Mode to render the content for display on a screen.
- `RENDER_MODE_FOR_PRINT`--- Mode to render the content for printing.
- `getIndex()`--- Gets the page index.
- `getWidth()`--- Gets the page width in points (1/72 of an inch).
- `getHeight()`--- Gets the page height in points (1/72 of an inch).
- `render(destination: Bitmap, destClip: Rect?, transform: Matrix?,
  renderMode: Int)`--- Renders a page to a bitmap.

#### APIs added in Android V

- `applyEdit(editRecord: FormEditRecord)`--- Applies a[`FormEditRecord`](https://developer.android.com/reference/kotlin/android/graphics/pdf/models/FormEditRecord)to the PDF.
- `getFormWidgetInfos()`--- Returns information about all form widgets on the page.
- `getFormWidgetInfos(types: IntArray)`--- Returns information about all form widgets of the specified types on the page.
- `getFormWidgetInfoAtIndex(widgetIndex: Int)`--- Returns information about the widget identified by the`widgetIndex`argument.
- `fun getFormWidgetInfoAtPosition(x: Int, y: Int)`--- Returns information about the widget at the given point.
- `getGotoLinks()`--- Gets bookmarks and goto links present on the page of a PDF document.
- `getImageContents()`--- Returns a list of[`PdfPageImageContent`](https://developer.android.com/reference/kotlin/android/graphics/pdf/content/PdfPageImageContent)found on the page.
- `getLinkContents()`--- Gets the bounds and URLs of all links on the page.
- `getTextContents()`--- Returns a list of[`PdfPageTextContent`](https://developer.android.com/reference/kotlin/android/graphics/pdf/content/PdfPageTextContent)on the page.
- `render(destination: Bitmap, destClip: Rect?, transform: Matrix?, params:
  RenderParams)`--- Renders a page to a bitmap.
- `searchText(query: String)`--- Searches the page for the given string and returns the bounds of all the matches.
- `selectContent(start: SelectionBoundary, stop: SelectionBoundary)`--- Returns a[`PageSelection`](https://developer.android.com/reference/kotlin/android/graphics/pdf/models/selection/PageSelection)which represents the content between the two boundaries.

## API usage

- The`PdfRenderer#write()`API writes a version of the loaded PDF to a[`ParcelFileDescriptor`](https://developer.android.com/reference/kotlin/android/os/ParcelFileDescriptor). Use cases include the following:

  - Saving a copy of the PDF document after removing the password security
  - Saving edits (annotations, form filling, etc.)
- The`PdfRenderer.Page#render()`APIs render a page or a portion of a page into a bitmap. In case of zoom, the API can also be used to render a portion of the page into a bitmap of a given size.

- The`PdfRenderer.Page`APIs`getImageContents()`,`getLinkContents()`, and`getTextContents()`return the contents available on the page. You can use the content for accessibility and TalkBack announcements or in AI-enabled features such as generating a summary of the page.

- The`PdfRenderer.Page#selectContent`API selects content available on a page. You can use the selected content for actions such as the following:

  - Call, if a phone number
  - Maps, if an address is selected
  - Copy
  - Share
  - Comments

## Compatibility

The[`PdfRendererPreV`](https://developer.android.com/reference/kotlin/android/graphics/pdf/PdfRendererPreV)class exposes the Android V APIs on Android R through U (API levels 30--34).

## Additional resources

See[Implement a PDF viewer](https://developer.android.com/media/grow/implement-pdf-viewer)to learn how to add a PDF viewer to your app.