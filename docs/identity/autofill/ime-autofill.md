---
title: https://developer.android.com/identity/autofill/ime-autofill
url: https://developer.android.com/identity/autofill/ime-autofill
source: md.txt
---

Beginning in Android 11, keyboards and other input-method editors
(*IMEs* ) can display autofill suggestions inline, in a suggestion strip, or
something similar instead of the system displaying suggestions in a menu. Since
these autofill suggestions can contain private data, such as passwords or
credit-card information, the suggestions are hidden from the IME until the user
selects one. Update IMEs and autofill services, such as password managers, to
make use of this feature. If an IME or an autofill service doesn't support
inline autofill, suggestions are shown in a menu, as in [versions earlier than
Android 11](https://developer.android.com/guide/topics/text/autofill#guides).

## Workflow

In this flow, *IME* means the current keyboard or other input editor, and
*suggestion provider* means the appropriate provider of the autofill suggestion.
Depending on the input field and the user's settings, the suggestion provider
might be the platform or an autofill service.

1. The user focuses on an input field that triggers autofill, like a password
   or credit-card input field.

2. The platform queries the current IME and the appropriate suggestion provider
   to see whether they support inline autofill. If either the IME or the
   suggestion provider doesn't support inline autofill, the suggestion is shown
   in a menu, as on Android 10 and lower.

3. The platform asks the IME to provide a *suggestion request* . This suggestion
   request specifies the maximum number of suggestions to be displayed and also
   provides *presentation specs* for each suggestion. The presentation specs
   specify things like maximum size, text size, colors, and font data, letting
   the suggestion provider match the look and feel of the IME.

4. The platform asks the suggestion provider to provide up to the requested
   number of suggestions. Each suggestion includes a callback to inflate a
   `View` containing the suggestion's UI.

5. The platform informs the IME that suggestions are ready. The IME displays
   the suggestions by calling the callback method to inflate each suggestion's
   `View`. To protect the user's private information, the IME does *not* see
   what the suggestions are at this stage.

6. If the user selects one of the suggestions, the IME is informed the same way
   as if the user picks a suggestion from a system menu.

The following sections describe how to configure your IME or autofill service to
support inline autofill.

## Configure IMEs to support inline autofill

This section describes how to configure your IME to support inline autofill. If
your IME doesn't support inline autofill, the platform defaults to showing
autofill suggestions in a menu.

Your IME must [set the `supportsInlinedSuggestions` attribute to `true`](https://developer.android.com/guide/topics/text/creating-input-method):  

    <input-method
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:supportsInlineSuggestions="true"/>

When the platform needs an autofill suggestion, it calls your IME's
[`InputMethodService.onCreateInlineSuggestionsRequest()`](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#onCreateInlineSuggestionsRequest(android.os.Bundle)) method. You must
implement this method. Return an [`InlineSuggestionsRequest`](https://developer.android.com/reference/android/view/inputmethod/InlineSuggestionsRequest) specifying the
following:

- **The number of suggestions** your IME wants.
- \*\*An [`InlinePresentationSpec`](https://developer.android.com/reference/android/widget/inline/InlinePresentationSpec) for each suggestion, which defines how
  the suggestion must be presented.

  | **Note:** If you provide fewer presentation specs than the number of suggestions requested, the last spec is used for all the excess suggestions. This means, for example, that if you provide only a single presentation spec, the suggestion provider uses that spec for all the suggestions.

When the platform has suggestions, it calls your IME's
[`onInlineSuggestionsResponse()`](https://developer.android.com/reference/android/inputmethodservice/InputMethodService#onInlineSuggestionsResponse(android.view.inputmethod.InlineSuggestionsResponse)) method, passing an
[`InlineSuggestionsResponse`](https://developer.android.com/reference/android/view/inputmethod/InlineSuggestionsResponse) containing the suggestions. You must implement
this method. In your implementation, call
[`InlineSuggestionsResponse.getInlineSuggestions()`](https://developer.android.com/reference/android/view/inputmethod/InlineSuggestionsResponse#getInlineSuggestions()) to get the list of
suggestions, then inflate each suggestion by calling its
[`InlineSuggestion.inflate()`](https://developer.android.com/reference/android/view/inputmethod/InlineSuggestion#inflate(android.content.Context,%20android.util.Size,%20java.util.concurrent.Executor,%20java.util.function.Consumer%3Candroid.widget.inline.InlineContentView%3E)) method.

## Configure autofill services to support inline autofill

This section describes how to configure your autofill service to support inline
autofill. If your app doesn't support inline autofill, the platform defaults to
showing its autofill suggestions in a menu.

Your autofill service must [set the `supportsInlinedSuggestions` attribute to
`true`](https://developer.android.com/guide/topics/text/autofill-services):  

    <autofill-service
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:supportsInlineSuggestions="true"/>

When the IME needs autofill suggestions, the platform calls your autofill
service's [`onFillRequest()`](https://developer.android.com/reference/android/service/autofill/AutofillService#onFillRequest(android.service.autofill.FillRequest,%20android.os.CancellationSignal,%20android.service.autofill.FillCallback)) method, just as it does in versions earlier
than Android 11. However, your service must call the passed
`FillRequest` object's [`getInlineSuggestionsRequest()`](https://developer.android.com/reference/android/service/autofill/FillRequest#getInlineSuggestionsRequest()) method. This
retrieves the `InlineSuggestionsRequest` created by the IME. The
`InlineSuggestionsRequest` specifies how many inline suggestions are needed and
how each one must be presented. If the IME doesn't support inline suggestions,
the method returns `null`.

Your autofill service creates [`InlinePresentation`](https://developer.android.com/reference/android/service/autofill/InlinePresentation) objects, up to the
maximum number requested in the `InlineSuggestionsRequest`. Your presentations
must obey the size constraints specified by the `InlineSuggestionsRequest`. To
return your suggestions to the IME, call [`Dataset.Builder.setValue()`](https://developer.android.com/reference/android/service/autofill/Dataset.Builder#setValue(android.view.autofill.AutofillId,%20android.view.autofill.AutofillValue,%20java.util.regex.Pattern,%20android.widget.RemoteViews,%20android.service.autofill.InlinePresentation)) once
for each suggestion. Android 11 provides versions of
`Dataset.Builder.setValue()` to support inline suggestions.
| **Note:** Although the IME is supposed to use the suggestions your service provides, this behavior isn't ensured.