---
title: https://developer.android.com/training/tv/accessibility/system-caption-settings
url: https://developer.android.com/training/tv/accessibility/system-caption-settings
source: md.txt
---

Android TV provides settings that let the user set caption preferences centrally
to create a cohesive experience across media apps.

These settings let users enable captions, select a preferred language, and
define a custom caption style based on their needs. Users can also specify
whether they prefer simplified captions at about a third-grade reading level,
known as "Easy Reader."

This guide shows how to get and apply system-provided caption settings to the
captions in your app.

Find the caption options, including a preview of the selected captions style,
under **Settings \> Accessibility \> Captions**:
![The captions settings menu on Android TV.](https://developer.android.com/static/training/tv/images/tv-caption-settings.png) Figure 1. Captions settings page.

## Get the CaptioningManager

From an activity, get the [`CaptioningManager`](https://developer.android.com/reference/android/view/accessibility/CaptioningManager) service from the `Context`:

    CaptioningManager captioningManager = (CaptioningManager) context.getSystemService(Context.CAPTIONING_SERVICE);

## Handle caption settings changes

Handle caption settings changes by implementing the
[`CaptioningChangeListener`](https://developer.android.com/reference/android/view/accessibility/CaptioningManager.CaptioningChangeListener) class:

    if (captioningManager != null) {
      // Define a class to store the CaptionStyle details.
      CurrentCaptionStyle currentCaptionStyle = new CurrentCaptionStyle();
      // Define the listeners.
      captioningManager.addCaptioningChangeListener(new CaptioningChangeListener() {

        @Override
        public void onEnabledChanged(boolean enabled) {
          super.onEnabledChanged(enabled);
          Log.d(TAG, "onEnabledChanged");
          currentCaptionStyle.isEnabled = enabled;
        }

        @Override
        public void onLocaleChanged(@Nullable Locale locale) {
          super.onLocaleChanged(locale);
          Log.d(TAG, "onLocaleChanged");
          currentCaptionStyle.locale = locale;
          if (locale == null) {
            currentCaptionStyle.isEasyReaderEnabled = false;
          } else {
            currentCaptionStyle.isEasyReaderEnabled = locale.getVariant().contains("simple");
          }
        }

        @Override
        public void onFontScaleChanged(float fontScale) {
          super.onFontScaleChanged(fontScale);
          Log.d(TAG, "onFontScaleChanged");
          currentCaptionStyle.fontScale = fontScale;
        }

        @Override
        public void onUserStyleChanged(@NonNull CaptionStyle userStyle) {
          super.onUserStyleChanged(userStyle);
          Log.d(TAG, "onUserStyleChanged");
          currentCaptionStyle.hasBackgroundColor = userStyle.hasBackgroundColor();
          currentCaptionStyle.backgroundColor = userStyle.backgroundColor;
          currentCaptionStyle.backgroundOpacity = userStyle.backgroundColor >>> 24;
          currentCaptionStyle.hasForegroundColor = userStyle.hasForegroundColor();
          currentCaptionStyle.foregroundColor = userStyle.foregroundColor;
          currentCaptionStyle.foregroundOpacity = userStyle.foregroundColor >>> 24;
          currentCaptionStyle.hasWindowColor = userStyle.hasWindowColor();
          currentCaptionStyle.windowColor = userStyle.windowColor;
          currentCaptionStyle.windowOpacity = userStyle.windowColor >>> 24;
          currentCaptionStyle.hasEdgeColor = userStyle.hasEdgeColor();
          currentCaptionStyle.edgeColor = userStyle.edgeColor;
          currentCaptionStyle.hasEdgeType = userStyle.hasEdgeType();
          currentCaptionStyle.edgeType = userStyle.edgeType;
          currentCaptionStyle.typeFace = userStyle.getTypeface();
        }

      });
    }

Alternatively, call the `getUserStyle` method directly:

    CaptionStyle systemCaptionStyle = captioningManager.getUserStyle();