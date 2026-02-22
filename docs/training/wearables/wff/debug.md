---
title: https://developer.android.com/training/wearables/wff/debug
url: https://developer.android.com/training/wearables/wff/debug
source: md.txt
---

# Debug a watch face

This page describes how to debug a watch face built with the Watch Face Format. It also explains how to validate your watch face XML and identify runtime errors.

## Check for valid Watch Face Format documents

As the Watch Face Format requires well-structured XML that conforms to a published XSD, you can confirm whether your watch face is valid or not, and identify errors.

Use the[XML validation tool](https://github.com/google/watchface/tree/main/third_party/wff)to identify issues during the build process. This tool is integrated into the build process in the[sample watch faces](https://github.com/android/wear-os-samples/tree/main/WatchFaceFormat).

If you are building a tool for creating watch faces, be sure that the tool performs XML validation[using the XSD](https://github.com/google/watchface/tree/main/third_party/wff/specification/documents)in your tool.

An example of running the validation tool manually:  

    java -jar wff-validator.jar 2 ~/MyWatchface/res/raw/watchface.xml

If there is an error in your`watchface.xml`document, you'll see an error, such as in this case where`height`has been misspelled as`hight`:  

    INFO: DWF Validation Application Version 1.0. Maximum Supported Format Version #2
    SEVERE: [Line 41:Column 53]: cvc-complex-type.3.2.2: Attribute 'hight' is not allowed to appear in element 'PartDraw'.
    INFO: ❌  FAILED : watchface.xml is NOT valid against watch face format version #1

The validator identifies the location---line 41, column 53---of the element that needs to be corrected.

Learn how to[obtain the XML validator tool](https://github.com/google/watchface/blob/main/third_party/wff/README.md)and build it for use.

### Identify runtime errors

Ensuring the XML itself is valid is not enough to capture all potential issues.

For example, your XML might reference a font or drawable resource that does not exist, or an expression might be expected to produce a numeric value, but instead results in a string.

For these types of issues, using logcat, either in Android Studio or through ADB is a good way to get more detailed information.

Filter on "runtime" and you'll be able to see both fatal and nonfatal issues affecting the watch face. For example, here, when specifying a resource for`HourHand`which does not exist:  

    E  Invalid resource ID 0x00000000.
    E  FATAL EXCEPTION: main
    Process: com.google.wear.watchface.runtime, PID: 29115                                                                                                  android.content.res.Resources$NotFoundException: Resource ID #0x0

Or here, when trying to use a color theme with a typo in it:  

    W  color has wrong type of source:CONFIGURATION.myTheeeme.2[OBJECT:]
    E  Cannot parse theme color. Using theme color WHITE