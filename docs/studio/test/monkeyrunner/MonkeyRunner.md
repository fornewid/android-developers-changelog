---
title: https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner
url: https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner
source: md.txt
---

# MonkeyRunner

A monkeyrunner class that contains static utility methods.

## Summary

|                                                                                                                                                                            Methods                                                                                                                                                                             ||||||||||||
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|---|---|---|---|---|---|---|---|
| void                                                                        | [alert](https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner#alert) (*string* message, *string* title, *string* okTitle) Displays an alert dialog to the process running the current program.                                        |
| *integer*                                                                   | [choice](https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner#choice) (*string* message, *iterable* choices, *string* title) Displays a dialog with a list of choices to the process running the current program.                    |
| void                                                                        | [help](https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner#help) (*string* format) Displays the monkeyrunner API reference in a style similar to that of Python's `pydoc` tool, using the specified format.                         |
| *string*                                                                    | [input](https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner#input) (*string* message, *string* initialValue, *string* title, *string* okTitle, *string* cancelTitle) Displays a dialog that accepts input.                          |
| void                                                                        | [sleep](https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner#sleep) (*float* seconds) Pauses the current program for the specified number of seconds.                                                                                |
| ` `[MonkeyDevice](https://developer.android.com/tools/help/MonkeyDevice)` ` | [waitForConnection](https://developer.android.com/studio/test/monkeyrunner/MonkeyRunner#waitForConnection) (*float* timeout, *string* deviceId) Tries to make a connection between the `monkeyrunner` backend and the specified device or emulator. |

## Public methods

#### *string*
alert
( *string* message, *string* title, *string* okTitle)


Displays an alert dialog to the process running the current
program. The dialog is modal, so the program pauses until the user clicks the dialog's
button.  

##### Arguments

| message |                The message to display in the dialog.                |
|  title  |          The dialog's title. The default value is "Alert".          |
| okTitle | The text displayed in the dialog button. The default value is "OK". |
|---------|---------------------------------------------------------------------|

#### *integer*
choice
(*string* message, *iterable* choices, *string* title)


Displays a dialog with a list of choices to the process running the current program. The
dialog is modal, so the program pauses until the user clicks one of the dialog's
buttons.  

##### Arguments

| message |                                         The prompt message displayed in the dialog.                                          |
| choices | A Python iterable containing one or more objects that are displayed as strings. The recommended form is an array of strings. |
|  title  |                                         The dialog's title. The default is "Input".                                          |
|---------|------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- If the user makes a selection and clicks the "OK" button, the method returns the 0-based index of the selection within the iterable. If the user clicks the "Cancel" button, the method returns -1.  

#### void
help
(*string* format)


Displays the monkeyrunner API reference in a style similar to that of Python's
`pydoc` tool, using the specified format.  

##### Arguments

| format | The markup format to use in the output. The possible values are "text" for plain text or "html" for HTML. |
|--------|-----------------------------------------------------------------------------------------------------------|

#### *string*
input
(*string* message *string* initialValue, *string* title, *string* okTitle, *string* cancelTitle)


Displays a dialog that accepts input and returns it to the program. The dialog is
modal, so the program pauses until the user clicks one of the dialog's buttons.


The dialog contains two buttons, one of which displays the okTitle value
and the other the cancelTitle value. If the user clicks the okTitle button,
the current value of the input box is returned. If the user clicks the cancelTitle
button, an empty string is returned.  

##### Arguments

|   message    |                 The prompt message displayed in the dialog.                 |
| initialValue | The initial value to display in the dialog. The default is an empty string. |
|    title     |                 The dialog's title. The default is "Input".                 |
|   okTitle    |       The text displayed in the okTitle button. The default is "OK".        |
| cancelTitle  |   The text displayed in the cancelTitle button. The default is "Cancel".    |
|--------------|-----------------------------------------------------------------------------|

##### Returns

- If the user clicks the okTitle button, then the method returns the current value of the dialog's input box. If the user clicks the cancelTitle button, the method returns an empty string.  

#### void
sleep
( *float* seconds )


Pauses the current program for the specified number of seconds.  

##### Arguments

| seconds | The number of seconds to pause. |
|---------|---------------------------------|

#### `
`[MonkeyDevice](https://developer.android.com/tools/help/MonkeyDevice)`
`
waitForConnection
(*float* timeout, *string* deviceId)


Tries to make a connection between the `monkeyrunner` backend and the
specified device or emulator.  

##### Arguments

| timeout  |                                                                       The number of seconds to wait for a connection. The default is to wait forever.                                                                        |
| deviceId | A regular expression that specifies the serial number of the device or emulator. See the topic [Android Debug Bridge](https://developer.android.com/tools/help/adb) for a description of device and emulator serial numbers. |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [MonkeyDevice](https://developer.android.com/tools/help/MonkeyDevice) instance for the device or emulator. Use this object to control and communicate with the device or emulator.