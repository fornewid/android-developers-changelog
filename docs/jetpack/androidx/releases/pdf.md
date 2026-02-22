---
title: https://developer.android.com/jetpack/androidx/releases/pdf
url: https://developer.android.com/jetpack/androidx/releases/pdf
source: md.txt
---

# pdf

API Reference  
[androidx.pdf.viewer.fragment](https://developer.android.com/reference/kotlin/androidx/pdf/viewer/fragment/package-summary)  
A library to add pdf viewing capabilities inside apps.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | - | - | - | [1.0.0-alpha13](https://developer.android.com/jetpack/androidx/releases/pdf#1.0.0-alpha13) |

## Declaring dependencies

To add a dependency on pdf, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.pdf:pdf-viewer-fragment:1.0.0-alpha13"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.pdf:pdf-viewer-fragment:1.0.0-alpha13")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1630469+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1630469&template=2029937)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Version 1.0

### Version 1.0.0-alpha13

February 11, 2026

`androidx.pdf:pdf-*:1.0.0-alpha13` is released. Version 1.0.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0902224f8b42bb10455664301705339a04b0b84c..7a88bc76ceeb1bab5f6dc6f0c8a314230e5dde3b/pdf).

**New Features**

- Introduced `EditablePdfViewerFragment`, which extends the standard `PdfViewerFragment` to provide PDF editing capabilities, including annotations and form-filling.
- Annotations: Leverages the `androidx.ink` library to provide comprehensive PDF annotation support. A dedicated toolbar, triggered by the edit `FloatingActionButton`, grants access to specialized tools including:
  - Pen: Enables freehand writing and drawing directly on the document. Users can customize the pen stroke with adjustable thickness and a broad color palette.
  - Highlighter: Supports both free-form and snap-to-text highlighting, available in multiple colors.
  - Eraser: Precisely removes specific annotations.
  - Undo and Redo: Provides built-in capabilities to seamlessly undo or redo most recent changes.
- Form Filling: Support for clicking on and modifying form fields such as text inputs, drop-downs, checkboxes and radio buttons.
  - The `EditablePdfViewerFragment` supports inline form-filling capabilities providing a seamless user experience. This feature is controlled via the `isFormFillingEnabled` API in `PdfView`.
  - `EditablePdfDocument`: A new interface extending `PdfDocument` for managing and applying form data edits.
  - The `PdfViewer` composable supports interaction with form fields, controllable via the `isFormFillingEnabled` parameter.
- Saving Changes: `PdfWriteHandle` allows for committing edited content to a specified file.
- Image Selection: Added support for selecting images on long-press within PDF documents. This feature is enabled via the `isImageSelectionEnabled` property in both `PdfView` and the `PdfViewer` composable. Resulting data is exposed through the `ImageSelection` model in `OnSelectionChangedListener`.
- Two-Page Layout: Added a side-by-side layout mode for large-screen devices, configurable using the `pagesPerRow` property in `PdfView` and the `PdfViewer` composable.

**API Changes**

- Introduce Image Selection API in Jetpack PDF Library ([Iee0b9](https://android-review.googlesource.com/#/q/Iee0b963fb44f14a7280480629643d389fd637d52), [b/470897750](https://issuetracker.google.com/issues/470897750))
- Make Form filling processing layer APIs public. ([Iec39c](https://android-review.googlesource.com/#/q/Iec39c614dc4347cd94d99b0552010af756bbe603), [b/474260451](https://issuetracker.google.com/issues/474260451))
- Add `renderParams` parameter to `openDocument` API in `SandboxedPdfLoader` ([If9344](https://android-review.googlesource.com/#/q/If9344e1f233b06065d5040ee1108b59ccbb72762), [b/438269273](https://issuetracker.google.com/issues/438269273))
- Add form filling presentation layer APIs ([I829c5](https://android-review.googlesource.com/#/q/I829c58ccd8624180f6fa8dabdf4630d5fd6c6ae0), [b/449869703](https://issuetracker.google.com/issues/449869703))
- Added `@MainThread` annotation on the callback methods of `OnFirstContentLoadListener` and `OnSelectionChangedListener` ([I4cf10](https://android-review.googlesource.com/#/q/I4cf101fbb608626ebb17d5146910847502c1db15), [b/466965940](https://issuetracker.google.com/issues/466965940))
- Marked `ApplyInProgressException` constructor internal, preventing external instantiation ([I5cc66](https://android-review.googlesource.com/#/q/I5cc662e848cc34016971b0850654ec2ef4cd41b4), [b/465414484](https://issuetracker.google.com/issues/465414484))
- Added `@MainThread` annotation on the callback methods of listeners in `PdfView` ([Ie7201](https://android-review.googlesource.com/#/q/Ie72015d5943bdd624b1866edae21918c8e1e6e8e), [b/429407597](https://issuetracker.google.com/issues/429407597))
- Add APIs for native editing capabilities through `EditablePdfViewerFragment`. ([Ifae6c](https://android-review.googlesource.com/#/q/Ifae6c791afaa9a850d7bb540d707282203fe2a01), [b/462049364](https://issuetracker.google.com/issues/462049364))
- Add `FirstContentLoad` API to `PdfView` and `PdfViewer` ([Icf63d](https://android-review.googlesource.com/#/q/Icf63d7146ff2172a92d7bd8ace9efe738d2d8acd), [b/461666545](https://issuetracker.google.com/issues/461666545))
- \[2Page\] Add Two-Page Layout API to `PdfViewer` Library ([I8d7f1](https://android-review.googlesource.com/#/q/I8d7f153a4d4c750ef46b8e35f111494f1540e859), [b/452517650](https://issuetracker.google.com/issues/452517650))

**Bug Fixes**

- Fix for exception due to Page already closed before fetching bitmap ([b/475255729](https://issuetracker.google.com/issues/475255729))

### Version 1.0.0-alpha12

December 03, 2025

`androidx.pdf:pdf-*:1.0.0-alpha12` is released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..0902224f8b42bb10455664301705339a04b0b84c/pdf).

**API Changes**

- Remove `textAsString` function from `TextSelection` into androidx-main
- Rename `clearSelection` to `clearCurrentSelection` ([I3a318](https://android-review.googlesource.com/#/q/I3a318e7f8b08f4614708a59b2e5363f2ebd3128c), [b/429407597](https://issuetracker.google.com/issues/429407597))
- Remove `textAsString` function from `TextSelection` ([I1305d](https://android-review.googlesource.com/#/q/I1305dfd2b6d1c5dbb3d69fee91e36d20d8e6230f), [b/429407798](https://issuetracker.google.com/issues/429407798))

**Bug Fixes**

- Fixed an issue where the fast scroller in `PdfView` was not visible by default. ([I7fb0e](https://android-review.googlesource.com/#/q/I7fb0e803f6c13ff1f5886e07ca63c9c8962b8dff))
- Fix crash in `TextSelectionMenuProvider` for selection with null text. ([I855df](https://android-review.googlesource.com/#/q/I855df18f1cef0419b7af816434908a3de9ea477a))

### Version 1.0.0-alpha11

October 22, 2025

`androidx.pdf:pdf-*:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c87a48a9ee2d6fbb166a58dfe61264062da0e6a4..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/pdf).

**New Features**

- Enabling Smart Menu Items on pdf content selection.
- Enabling hyperlink selection and GoTo link selection in pdf.
- Exposing selection menu api `fromPdfView` and `PdfViewer` Composable, which allows developers to add selection menu items.
- Adding page alignment api in PdfView and PdfViewer Composable which allows developers to choose the page alignment when the content height \< viewport height.

**API Changes**

- Made `contentDesc` nullable and removed default value. ([I86f8c](https://android-review.googlesource.com/#/q/I86f8c8cb5e67ba5654b55b5fbdd63ebe9c3166c9), [b/441973880](https://issuetracker.google.com/issues/441973880))
- Expose `PdfSelectionMenuKeys` for Link Selection Menu Items ([Ic9b05](https://android-review.googlesource.com/#/q/Ic9b05c000a346a61c695bbf2b0a4a7a318994a00), [b/447079082](https://issuetracker.google.com/issues/447079082))
- Add `PageAlignment` API to `PdfView` and `PdfViewer` into androidx-main
- Change angle-related API to use degrees and include unit in names, be clear about units in Angle conversion utilities and support both degrees and radians, change `StockBrushes` API to take stock brush version as a factory function parameter and expose self-overlap behavior control for highlighter brushes, rename `MutableAffineTransform.populateFromTranslate` to `populateFromTranslation`, remove `InProgressStrokesView.setRenderFactory/getRenderFactory`. ([Id9eab](https://android-review.googlesource.com/#/q/Id9eab6301d2ca1803452cd8a1eb2dcf0a3cd357d), [b/436656418](https://issuetracker.google.com/issues/436656418))
- Add `PageAlignment` API to `PdfView` and `PdfViewer` ([I9c9a5](https://android-review.googlesource.com/#/q/I9c9a55df56046dcfadd51efbf658d3ba69e563a0), [b/438065228](https://issuetracker.google.com/issues/438065228))
- Expose Selection Menu API from `PdfViewer` Composable ([Id9b0f](https://android-review.googlesource.com/#/q/Id9b0f795a4071a8e6a2bb8197b0d3326ec7a521e), [b/407663999](https://issuetracker.google.com/issues/407663999))
- Make `PdfView` a `ViewGroup`. No support for arbitrary children. ([Ib51d8](https://android-review.googlesource.com/#/q/Ib51d899b17b1867dd32566fbbf4e33d5a64313cb), [b/410008792](https://issuetracker.google.com/issues/410008792))
- Expose `HyperLinkSelection` and `GoToLinkSelection` from `PdfView` ([I378c4](https://android-review.googlesource.com/#/q/I378c4a8aff7fefc00bf4eac31438f69ea19db9ee), [b/441280002](https://issuetracker.google.com/issues/441280002))
- Refactor `PdfPageContent` to support generic selections ([I28f16](https://android-review.googlesource.com/#/q/I28f167f9501ff9b78e883794d0e33fc9ac26a655), [b/437845185](https://issuetracker.google.com/issues/437845185))
- Expose Selection Menu API from `PdfView` ([Idd547](https://android-review.googlesource.com/#/q/Idd547773529c416ef20d1d8adf9a20ec57b24d20), [b/407663737](https://issuetracker.google.com/issues/407663737))
- Move selection-related classes to a dedicated package ([I953cb](https://android-review.googlesource.com/#/q/I953cbda59914fcfe9a172b68677e2c9141d4d138), [b/436157691](https://issuetracker.google.com/issues/436157691))
- Introduce experimental `onPdfViewCreated` for PdfView access in `PdfViewerFragment`. ([I86715](https://android-review.googlesource.com/#/q/I86715dcaef62f0eb8e32dc172814c6db7eda43d5), [b/422620454](https://issuetracker.google.com/issues/422620454))
- Adds `FileDescriptor` API to `PdfLoader` ([I60b8d](https://android-review.googlesource.com/#/q/I60b8dfa37b4c3800392f2d14992375b9d2581f05))

**Bug Fixes**

- Improve input modeling to make strokes more accurately reflect input ([I93097](https://android-review.googlesource.com/#/q/I9309760022de0c30a0bc5e960da4c2467f663e9f))

**External Contribution**

- Expose `PdfSelectionMenuKeys` for Link Selection Menu Items
- Expose Selection Menu API from `PdfViewer` Composable
- Expose Selection Menu API from `PdfView`

### Version 1.0.0-alpha10

July 16, 2025

`androidx.pdf:pdf-*:1.0.0-alpha10` is released. Version 1.0.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314..c87a48a9ee2d6fbb166a58dfe61264062da0e6a4/pdf).

**New Features**

- Enhanced selection that allows users to select text across multiple pages by dragging selection handles beyond page boundaries.
- Applications can now intercept and customize the handling of hyperlink clicks within PDF documents.

**API Changes**

- Exposes a Composable for presenting PDF content ([I8e7ee](https://android-review.googlesource.com/#/q/I8e7ee4f232f9a3f64f34a19e9c4d58bca8a42c79))
- Moving `PdfPoint` and `PdfRect` to `androidx.pdf.models` package ([I26cf4](https://android-review.googlesource.com/#/q/I26cf46db246cfa2c0955f0c48a48876754b7adac))
- Exposes a View component for presenting PDF content ([I9fe27](https://android-review.googlesource.com/#/q/I9fe275e860f750975e2fa1c2541c6a13b06e1cae))
- Exposes API to initialize pdf resources ahead of time and bring down cold-start latency ([a18fa89](https://android.googlesource.com/platform/frameworks/support/+/a18fa89e7dd627fe71060b2b1e57363b707921f8))
- Exposes API to override hyperlink click handling on Pdf content([6330a8b](https://android.googlesource.com/platform/frameworks/support/+/6330a8b9f18cd953f006ee3abc3b549378749136))
- Exposes a new artifact pdf-document-service and the corresponding APIs - `PdfLoader`, `PdfDocument` and `SandboxedPdfLoader`. The interfaces can be used to implement the parsing and processing component of the PDF document ([Ide70d](https://android.googlesource.com/platform/frameworks/support/+/11a11a163e54f428660c33450ebd96621644c3ea))
- Exposes an API to set `PdfDocument` on `PdfView` to initialize rendering of the document ([If8738](https://android.googlesource.com/platform/frameworks/support/+/5a906b9fc156d20dba11e67cfba08c1a2b0205b7))

### Version 1.0.0-alpha09

May 7, 2025

`androidx.pdf:pdf-*:1.0.0-alpha09` is released. Version 1.0.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/af3ab4a50a3fbaf02943120e34efdc4b84eb481d..a99266d9ab8e4a0b6b8d4c11d8fc79524f59c314/pdf).

**Major Changes**

- The codebase has undergone a major refactoring and is now fully written in Kotlin, utilizing Coroutines and `ViewModel`. This includes a reimplementation of the `PdfViewerFragment`. This release does not include any new APIs or features.

**Known Issues:**

- The fast scroller and page indicator are missing shadow effects.
- Single-page PDF documents might not always be centered and scaled to the view's width.

**API Changes**

- Annotate `containerStyleResId` with `@StyleRes`. ([I88d85](https://android-review.googlesource.com/#/q/I88d8535bccfe9ce7f9d23f513fd3cbed762d534c))

### Version 1.0.0-alpha08

March 12, 2025

`androidx.pdf:pdf-document-service:1.0.0-alpha08`, `androidx.pdf:pdf-viewer:1.0.0-alpha08`, and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha08` are released. Version 1.0.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..af3ab4a50a3fbaf02943120e34efdc4b84eb481d/pdf).

**Bug Fixes**

- Resolved inconsistent selection menu placement between different Android devices due to scaling differences. Selection menu placement is now consistent across devices.
- Aligned fast scroller and page indicator position on fragment recreation in scenarios like config change, etc.

### Version 1.0.0-alpha07

February 26, 2025

`androidx.pdf:pdf-document-service:1.0.0-alpha07`, `androidx.pdf:pdf-viewer:1.0.0-alpha07`, and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha07` are released. Version 1.0.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3d32c4baa01dcb977da6a86a7434e0167288d750..fd7408b73d9aac0f18431c22580d9ab612278b1e/pdf).

**New Features**

- The `PdfViewerFragment` now supports `StylingOptions` (a set of style resource ids) enabling custom styling via `newInstance` or XML (`FragmentContainerView`). Subclasses can utilize the protected constructor for similar functionality.
- `StylingOptions` currently takes in `containerStyle` which provides:
  - Custom drawable support for the fast scroll handle and page indicator.
  - `marginEnd` attribute for precise positioning of the fast scroll handle and page indicator.

**API Changes**

- Added public attrs from `PdfView` ([I30fc5](https://android-review.googlesource.com/#/q/I30fc544c356784b2be74c0d66d8c040cb1b38338))
- Added new APIs `StylingOptions` for pdf view. ([Id2993](https://android-review.googlesource.com/#/q/Id299338b7220c7a447d7356b8ccca92a9dab70b0))

**Bug Fixes**

- Fixed synchronization discrepancy between the fast scroll handle and page indicator visibility state.

### Version 1.0.0-alpha06

January 29, 2025

`androidx.pdf:pdf-document-service:1.0.0-alpha06`, `androidx.pdf:pdf-viewer:1.0.0-alpha06`, and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha06` are released. Version 1.0.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8963abd77b9ce2c2f8a165926e4019318329b298..3d32c4baa01dcb977da6a86a7434e0167288d750/pdf).

**Bug Fixes**

- Fix: Crash caused by `IllegalArgumentException` when unbinding a service that's not registered ([eb4e85](https://android-review.googlesource.com/q/commit:eb4e858871b8ced47400f62ee97513d3d2056b2a))
- Fix: Crash `IllegalArgumentException` due to difference in `mMaxPages` and `numPages`. ([75d763](https://android-review.googlesource.com/q/commit:75d7635d81d1fcb18706c3295ca3094db7aa8a75))

### Version 1.0.0-alpha05

December 11, 2024

`androidx.pdf:pdf-document-service:1.0.0-alpha05`, `androidx.pdf:pdf-viewer:1.0.0-alpha05`, and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha05` are released. Version 1.0.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02fa00d7c09d100730c54cf194e22ba51ffc2ec9..8963abd77b9ce2c2f8a165926e4019318329b298/pdf).

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([I38301](https://android-review.googlesource.com/#/q/I38301fa68aaeb50a61c5929d8e784ebd6515cefd), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Fixed previously opened page being displayed after rotation in Android 13. ([Ib03dd](https://android-review.googlesource.com/#/q/Ib03dd03e34b38c0a429b178f66de00d62aa37bfc))
- Fixed Toolbox disappearing on Rotation. ([01148f](https://android-review.googlesource.com/#/q/01148f9d13f0895cb4b46015e440467dd39c66c2))

### Version 1.0.0-alpha04

November 13, 2024

`androidx.pdf:pdf-viewer:1.0.0-alpha04` and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha04` are released. Version 1.0.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..02fa00d7c09d100730c54cf194e22ba51ffc2ec9/pdf).

**Expanded Compatibility**

- The `PDFViewer` library now supports Android versions S, T, U, and V. This enhanced compatibility is linked to the SDK extension 13 update.

**API Changes**

- Added minimum `SdkExtension` constraint to `PdfViewerFragment`. ([I922af](https://android-review.googlesource.com/#/q/I922afd62cd92eb55465d7108f19a7da1f55384c3))
- Exposing new apis for PDF Viewer library. ([I0af57](https://android-review.googlesource.com/#/q/I0af5789d96f0ce53338e160da464dd3cd1f1b7fb))

**Bug Fixes**

- Crash fix for process death issue.
- UI fixes related to the password dialog.
- Accessibility fixes for `findInFileView` and `FastscrollView`.

**Ongoing Development**

- We are actively working on incorporating Jetpack Compose into the library.

### Version 1.0.0-alpha03

September 18, 2024

`androidx.pdf:pdf-viewer:1.0.0-alpha03` and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha03` are released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f6ddb4b44762d7b8edb8d4258798e2f68c23246b..0431b84980e97d6bafdfda7c9038bc4d9529564f/pdf).

**Bug Fixes**

- Keyboard not coming up when search is opened for the first time is resolved
- UI fixes related to the font of FindInFile view.
- UI fixes for text selection and drag handle.

**Known Issues**

- 3D images in PDF documents are not rendered in the viewer.
- `PdfViewerFragment` has some performance issues on very large PDF documents (\> 250 MB)

### Version 1.0.0-alpha02

September 4, 2024

`androidx.pdf:pdf-viewer:1.0.0-alpha02` and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha02` are released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/675667ff3320d18a27d98255c55c56775bf0a3e6..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/pdf).

**Bug Fixes**

- The blurry PDF image issue when rotating from portrait to landscape and the app going to sleep has been resolved.
- The find in file menu now maintains the result count even when the configuration changes.
- The `FloatingActionButton` icon is now available for single-page PDFs.
- Overlapping issues between the Find in file bar and the `FloatingActionButton` have been fixed.
- Text and highlight annotations can now be rendered in the viewer.
- Accessibility improvements have been made to the Find in file bar.
- UI fixes have been implemented for rotation, including preserving the find count, addressing the disappearing text selection menu, and resolving the FAB overlapping issue.
- The find in file menu hiding behind the keyboard in landscape mode has been fixed.

**Known Issues**

- 3D images in PDF documents are not rendered in the viewer.
- `PdfViewerFragment` has some performance issues on very large PDF documents (\> 250 MB)

### Version 1.0.0-alpha01

August 7, 2024

`androidx.pdf:pdf-viewer:1.0.0-alpha01` and `androidx.pdf:pdf-viewer-fragment:1.0.0-alpha01` are released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/79adf4553982866e6de98b7c68615fe53ad85c6d/pdf).

**New Features**

The initial alpha release of `PDFViewer` includes early preview implementations that enable core PDF reading scenarios. Please note that the `PdfViewerFragment` is currently supported only on Android V (SDK 35) versions. Support for older Android versions will be added in upcoming releases.

- Introduced `PdfViewerFragment` which your app can use to render a PDF document. `PdfViewerFragment` simplifies integrating a PDF viewer in your Activity and lets the users interact in the following ways:
  - Zooming: Pinch in and out to adjust zoom levels for a comfortable reading experience as well as double tap for a quick zoom in/out to the default state.
  - Navigation: Scroll in the default/zoomed state. `PdfViewerFragment` provides a quick scrubber for fast scrolling between pages.
  - Text actions: Long tapping on text selects it, allowing users to use options like Copy and Select all on the current page.
  - Password-protected documents: `PdfViewerFragment` provides a dialog box for the user to enter the password and open the document.
  - Navigable hyperlinks: Users can navigate to Web URLs or bookmarks by tapping on hyperlinks within the PDF.
  - Shortcut to annotations mode: Edit mode is not yet supported in `PdfViewerFragment`. Instead, `PdfViewerFragment` displays a `FloatingActionButton` that fires an implicit `android.intent.action.ANNOTATE` intent with the document URI.

**API Changes**

- Added `PdfViewerFragment.documentUri` property to set a file or content URI for the document and initiate the document loading. `PdfViewerFragment` displays a loading spinner when the URI is set indicating the background processing of the document.
- Added `PdfViewerFragment.isTextSearchActive` to toggle the visibility of the find in file menu. `PdfViewerFragment` handles the entire flow - allowing input, displaying total number of matches, enabling navigation between results and exiting it.
- Added `onDocumentLoadSuccess` and `onDocumentLoadError` callbacks which are invoked after successful rendering of the document or after an error is thrown before the rendering.

**Known Issues**

- Find in file bar overlaps with the `FloatingActionButton` in some cases.
- `FloatingActionButton` icon isn't visible for single page PDFs.
- Result count is not preserved on configuration change in the find in file menu.
- Flickering is observed while closing the find in file menu
- 3D images in PDF documents are not rendered in the viewer.
- Accessibility features will be enabled in the following releases.
- PDF image gets blurry on rotating from portrait to landscape.
- No support for text/highlight annotation.
- `PdfViewerFragment` has some performance issues on very large PDF documents (\> 250 MB)

**Note**

- Update `compileSdk` to 35 [5dc41be](https://android.googlesource.com/platform/frameworks/support/+/5dc41be792a8fa6b2488df3e780da1c0805b202f)