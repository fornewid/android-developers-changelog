---
title: https://developer.android.com/studio/test/monkeyrunner/MonkeyImage
url: https://developer.android.com/studio/test/monkeyrunner/MonkeyImage
source: md.txt
---

# MonkeyImage

A monkeyrunner class to hold an image of the device or emulator's screen. The image is copied from the screen buffer during a screenshot. This object's methods allow you to convert the image into various storage formats, write the image to a file, copy parts of the image, and compare this object to other`MonkeyImage`objects.

You do not need to create new instances of`MonkeyImage`. Instead, use[MonkeyDevice.takeSnapshot()](https://developer.android.com/tools/help/MonkeyDevice#takeSnapshot)to create a new instance from a screenshot. For example, use:  

```
newimage = MonkeyDevice.takeSnapshot()
```

## Summary

|                                                                                                                                                                                                                                        Methods                                                                                                                                                                                                                                         ||||||||||||
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|---|---|---|---|---|---|---|---|
| *string*                                                                  | [convertToBytes](https://developer.android.com/studio/test/monkeyrunner/MonkeyImage#convertToBytes)(*string*format) Converts the current image to a particular format and returns it as a*string* that you can then access as an*iterable*of binary bytes.                                                                                                                    |
| *tuple*                                                                   | [getRawPixel](https://developer.android.com/studio/test/monkeyrunner/MonkeyImage#getRawPixel)(*integer* x,*integer*y) Returns the single pixel at the image location (x,y), as an a*tuple* of*integer*, in the form (a,r,g,b).                                                                                                                                                |
| *integer*                                                                 | [getRawPixelInt](https://developer.android.com/studio/test/monkeyrunner/MonkeyImage#getRawPixelInt)(*integer* x,*integer*y) Returns the single pixel at the image location (x,y), as a 32-bit*integer*.                                                                                                                                                                       |
| ` `[MonkeyImage](https://developer.android.com/tools/help/MonkeyImage)` ` | [getSubImage](https://developer.android.com/studio/test/monkeyrunner/MonkeyImage#getSubImage)(*tuple*rect) Creates a new`MonkeyImage`object from a rectangular selection of the current image.                                                                                                                                                                                |
| *boolean*                                                                 | [sameAs](https://developer.android.com/studio/test/monkeyrunner/MonkeyImage#sameAs)([MonkeyImage](https://developer.android.com/tools/help/MonkeyImage)other,*float*percent) Compares this`MonkeyImage`object to another and returns the result of the comparison. The`percent`argument specifies the percentage difference that is allowed for the two images to be "equal". |
| *void*                                                                    | [writeToFile](https://developer.android.com/studio/test/monkeyrunner/MonkeyImage#writeToFile)(*string* path,*string*format) Writes the current image to the file specified by`filename`, in the format specified by`format`.                                                                                                                                                  |

## Public methods

#### *string*convertToBytes(*string*format)

Converts the current image to a particular format and returns it as a*string* that you can then access as an*iterable*of binary bytes.  

##### Arguments

| format | The desired output format. All of the common raster output formats are supported. The default value is "png" (Portable Network Graphics). |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------|

#### *tuple*getRawPixel(*integer* x,*integer*y)

Returns the single pixel at the image location (x,y), as an a*tuple* of*integer*, in the form (a,r,g,b).  

##### Arguments

| x | The horizontal position of the pixel, starting with 0 at the left of the screen in the orientation it had when the screenshot was taken. |
| y |  The vertical position of the pixel, starting with 0 at the top of the screen in the orientation it had when the screenshot was taken.   |
|---|------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A tuple of integers representing the pixel, in the form (a,r,g,b) where a is the alpha channel value, and r, g, and b are the red, green, and blue values, respectively.  

#### *tuple*getRawPixelInt(*integer* x,*integer*y)

Returns the single pixel at the image location (x,y), as an an*integer*. Use this method to economize on memory.  

##### Arguments

| x | The horizontal position of the pixel, starting with 0 at the left of the screen in the orientation it had when the screenshot was taken. |
| y |  The vertical position of the pixel, starting with 0 at the top of the screen in the orientation it had when the screenshot was taken.   |
|---|------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- The a,r,g, and b values of the pixel as 8-bit values combined into a 32-bit integer, with a as the leftmost 8 bits, r the next rightmost, and so forth.  

#### `
`[MonkeyImage](https://developer.android.com/tools/help/MonkeyImage)`
`getSubImage(*tuple*rect)

Creates a new`MonkeyImage`object from a rectangular selection of the current image.  

##### Arguments

| rect | A tuple (x, y, w, h) specifying the selection. x and y specify the 0-based pixel position of the upper left-hand corner of the selection. w specifies the width of the region, and h specifies its height, both in units of pixels. The image's orientation is the same as the screen orientation at the time the screenshot was made. |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A new`MonkeyImage`object containing the selection.  

#### *boolean*sameAs(`
`[MonkeyImage](https://developer.android.com/tools/help/MonkeyImage)`
`otherImage,*float*percent )

Compares this`MonkeyImage`object to another and returns the result of the comparison. The`percent`argument specifies the percentage difference that is allowed for the two images to be "equal".  

##### Arguments

|  other  |                                                                           Another`MonkeyImage`object to compare to this one.                                                                            |
| percent | A float in the range 0.0 to 1.0, inclusive, indicating the percentage of pixels that need to be the same for the method to return`true`. The default is 1.0, indicating that all the pixels must match. |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- Boolean`true`if the images match, or boolean`false`otherwise.  

#### voidwriteToFile(*string* filename,*string*format)

Writes the current image to the file specified by`filename`, in the format specified by`format`.  

##### Arguments

|  path  |                                                                                                     The fully-qualified filename and extension of the output file.                                                                                                      |
| format | The output format to use for the file. If no format is provided, then the method tries to guess the format from the filename's extension. If no extension is provided and no format is specified, then the default format of "png" (Portable Network Graphics) is used. |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|