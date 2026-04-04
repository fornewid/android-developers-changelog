---
title: Printing photos  |  App data and files  |  Android Developers
url: https://developer.android.com/training/printing/photos
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [App data and files](https://developer.android.com/training/data-storage)

# Printing photos Stay organized with collections Save and categorize content based on your preferences.




Taking and sharing photos is one of the most popular uses for mobile devices. If your application
takes photos, displays them, or allows users to share images, you should consider enabling printing
of those images in your application. The [Android Support Library](/tools/support-library) provides a convenient function for enabling image printing using a
minimal amount of code and simple set of print layout options.

This lesson shows you how to print an image using the v4 support library `PrintHelper` class.

## Print an image

The Android Support Library `PrintHelper` class provides
a simple way to print images. The class has a single layout option, `setScaleMode()`,
which allows you to print with one of two options:

* `SCALE_MODE_FIT` - This
  option sizes the image so that the whole image is shown within the printable area of the page.
* `SCALE_MODE_FILL` - This
  option scales the image so that it fills the entire printable area of the page. Choosing this
  setting means that some portion of the top and bottom, or left and right edges of the image is
  not printed. This option is the default value if you do not set a scale mode.

Both scaling options for `setScaleMode()` keep the existing aspect ratio of the image intact. The following code example
shows how to create an instance of the `PrintHelper` class, set the
scaling option, and start the printing process:

### Kotlin

```
private fun doPhotoPrint() {
    activity?.also { context ->
        PrintHelper(context).apply {
            scaleMode = PrintHelper.SCALE_MODE_FIT
        }.also { printHelper ->
            val bitmap = BitmapFactory.decodeResource(resources, R.drawable.droids)
            printHelper.printBitmap("droids.jpg - test print", bitmap)
        }
    }
}
```

### Java

```
private void doPhotoPrint() {
    PrintHelper photoPrinter = new PrintHelper(getActivity());
    photoPrinter.setScaleMode(PrintHelper.SCALE_MODE_FIT);
    Bitmap bitmap = BitmapFactory.decodeResource(getResources(),
            R.drawable.droids);
    photoPrinter.printBitmap("droids.jpg - test print", bitmap);
}
```

This method can be called as the action for a menu item. Note that menu items for actions that are
not always supported (such as printing) should be placed in the overflow menu. For more
information, see the [Action Bar](/design/patterns/actionbar) design
guide.

After the `printBitmap()` method is
called, no further action from your application is required. The Android print user interface
appears, allowing the user to select a printer and printing options. The user can then print the
image or cancel the action. If the user chooses to print the image, a print job is created and a
printing notification appears in the system bar.

If you want to include additional content in your printouts beyond just an image, you must
construct a print document. For information on creating documents for printing, see the
[Printing an HTML document](/training/printing/html-docs) or
[Printing a custom document](/training/printing/custom-docs)
lessons.

[Next

Printing HTML documents

arrow\_forward](/training/printing/html-docs)