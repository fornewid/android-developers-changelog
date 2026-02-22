---
title: https://developer.android.com/training/tv/accessibility/system-caption-settings
url: https://developer.android.com/training/tv/accessibility/system-caption-settings
source: md.txt
---

# Adopt system caption settings

On Android TV, settings are provided for users to define their own caption style. This guide demonstrates how an app can obtain and apply the system-provided caption style.

The caption options can be found under**Settings \> System \> Accessibility \> Caption**:

![ATV_Caption_Settings](https://developer.android.com/training/tv/images/tv-caption-settings.png)

## Obtain the CaptioningManager

From an activity, you can get the caption service from its`Context`using[`CaptioningManager`](https://developer.android.com/reference/android/view/accessibility/CaptioningManager):  

    CaptioningManager captioningManager = (CaptioningManager)context.getSystemService(Context.CAPTIONING_SERVICE);

## Handle caption style changes

You can then handle caption style changes by implementing[`CaptioningChangeListener`](https://developer.android.com/reference/android/view/accessibility/CaptioningManager.CaptioningChangeListener):  

    if (captioningManager != null) {
      // Define a class to store the CaptionStyle details.
      CurrentCaptionStyle currentCaptionStyle = new CurrentCaptionStyle;
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
          currentCaptionStyle.backgroundOpcity = userStyle.backgroundColor >>> 24;
          currentCaptionStyle.hasForegroundColor = userStyle.hasForegroundColor();
          currentCaptionStyle.foregroundColor = userStyle.foregroundColor;
          currentCaptionStyle.foregroundOpacity = userStyle.foregroundColor >>> 24;
          currentCaptionStyle.hasWindowColor = userStyle.hasWindowColor();
          currentCaptionStyle.windowColor = userStyle.windowColor;
          currentCaptionStyle.windowOpcity = userStyle.windowColor >>> 24;
          currentCaptionStyle.hasEdgeColor = userStyle.hasEdgeColor();
          currentCaptionStyle.edgeColor = userStyle.edgeColor;
          currentCaptionStyle.hasEdgeType = userStyle.hasEdgeType();
          currentCaptionStyle.edgeType = userStyle.edgeType;
          currentCaptionStyle.typeFace = userStyle.getTypeface();
        }

      });

To obtain the system`CaptionStyle`, you can call`getUserStyle()`directly:  

    CaptionStyle systemCaptionStyle = captioningManager.getUserStyle();