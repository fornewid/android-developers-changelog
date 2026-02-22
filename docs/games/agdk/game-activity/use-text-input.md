---
title: https://developer.android.com/games/agdk/game-activity/use-text-input
url: https://developer.android.com/games/agdk/game-activity/use-text-input
source: md.txt
---

# TextInput in GameActivityPart of[Android Game Development Kit](https://developer.android.com/games/agdk/overview).

[GameActivity](https://developer.android.com/reference/games/game-activity)integrates[GameTextInput](https://developer.android.com/reference/games/game-text-input)by:

- providing a wrapper
- creating a flag for new text input event availability
- directly using GameTextInput's state buffer for the text content

As shown in the following diagram, applications use different internal logical components for user text input purpose:

![alt_text](https://developer.android.com/static/games/agdk/game-activity/images/GameActivityTextInput.png "TextInput paths")
| **Note:** Bypassing GameActivity and directly creating a`GameTextInput`instance is out of the scope of this document. For more information about that usage, refer to the[GameTextInput documentation](https://developer.android.com/games/agdk/add-support-for-text-input).

There are three broad steps to using the built-in`GameTextInput`library:

- Controlling the soft keyboard on UI
- Knowing when new text is available
- Retrieving the user input text and its states

The rest of this document describes them in detail. For an example of`GameTextInput`with`GameActivity`in action, see the[games-samples repository](https://github.com/android/games-samples).

## Control the soft keyboard on UI

`GameActivity`provides two functions to control the soft keyboard on the UI:

- [`GameActivity_showSoftInput()`](https://developer.android.com/reference/games/game-activity/group/game-activity#gameactivity_showsoftinput)displays the soft keyboard.
- [`GameActivity_hideSoftInput()`](https://developer.android.com/reference/games/game-activity/group/game-activity#gameactivity_hidesoftinput)hides the soft keyboard.

Refer to the API reference docs for their definitions. After the keyboard is displayed, the application's UI may look similar to the following:

![alt_text](https://developer.android.com/static/games/agdk/game-activity/images/GameActivityTextInputUI.png "TextInput UI")

## Check for text availability

Soft keyboard events get passed from`GameTextInput`on the Java side to the C/C++ side through the JNI, then travel up to GameActivity's wrapper, finally reflecting in the[`android_app::textInputState`](https://developer.android.com/reference/games/game-activity/structandroid/app#textinputstate)flag implemented in[`native_app_glue`](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue). Applications should poll this flag periodically to perform the intended processing:

- GameActivity only sets the`android_app::textInputState`flag.
- Applications poll the flag and handle the new`GameTextInput`events, such as the new text added to the input buffer.
- Applications clear the`android_app::textInputState`.

Note that`android_app::textInputState`does not differentiate between single and multiple text input events.

For a simple example, the following code polls the`textInputState`flag after handling app cycle commands, touch events, and key events:  

    while (true) {
       // Read all pending events.
       int events;
       struct android_poll_source* source;

       while ((ALooper_pollOnce(engine.animating ? 0 : -1, nullptr, &events,
                                     (void**)&source)) >= 0) {
           // Process this event, etc.
           ...
           // Check if we are exiting.
           if (app->destroyRequested != 0) {
               engine_term_display(&engine);
               return;
           }
       }
       engine_handle_input(app);

       // Process text input events if there is any outstanding.
       if (app->textInputState) {
           // process TextInput events.
              ...
           //reset the textInputState flag
           app->textInputState = 0;
       }
       if (engine.animating) {
             // draw frames.
       }
    }

## Retrieve the user input text

The input texts and other states are accumulated in GameTextInput's internal buffer,[`GameTextInput::currentState_`](https://developer.android.com/reference/games/game-text-input/struct/game-text-input-state). Applications can use one of the following ways to retrieve its content:

- GameActivity's wrapper API (recommended)
- GameTextInput API

### Get TextInput state with GameActivity API

Applications acquire the current text input with the typical callback mechanism:

- Implement a callback function of type[`GameTextInputGetStateCallback`](https://developer.android.com/reference/games/game-text-input/group/game-text-input#gametextinputgetstatecallback)to process text input events.
- Call`GameActivity_getInputState()`when there is one or multiple outstanding events.
- Clear the[`android_app::textInputState`](https://developer.android.com/reference/games/game-activity/structandroid/app#textinputstate)after the events are processed.

Continuing with the snippet in the previous section, the following code acquires a reference to the text input buffer, processes it (not shown), and resets the event flag:  

    extern "C" void GameTextInputGetStateCB(void *ctx, const struct GameTextInputState *state) {
        auto* engine = (struct engine*)ctx;
        if (!engine || !state) return;

        // Process the text event(s).
        LOGI("UserInputText: %s", state->text_UTF8);

        // Clear the text input flag.
        engine->app->textInputState = 0;
    }

In the game loop shown in the previous section, check and process text with the above text input handler:  

    if (state->textInputState) {
        GameActivity_getTextInputState(
            app->activity,
            GameTextInputGetStateCB,  // App's event handler shown above.
            &engine // Context to the GameTextInputGetStateCB function.
        );
    }

Applications can optionally initialize the`GameTextInputState`content with[`GameActivity_setTextInputState()`](https://developer.android.com/reference/games/game-activity/group/game-activity#gameactivity_settextinputstate).

### Get TextInput state with GameTextInput API

Applications can also directly use`GameTextInput`API to retrieve the current`GameTextInputState`:

- Use[`GameActivity_getTextInput()`](https://developer.android.com/reference/games/game-activity/group/game-activity#gameactivity_gettextinput)to get GameActivity's internal`GameTextInput`instance.
- With the`GameTextInput`instance in hand, call[`GameTextInput_getState()`](https://developer.android.com/reference/games/game-text-input/group/game-text-input#gametextinput_getstate)to get the same`GameTextInputState`content.

Again, note that applications should not initialize`GameTextInput`directly;`GameActivity`already does that during its initialization process.

The callback mechanism is the same as that used by the GameActivity's`GameActivity_getTextInputState()`function.

## References

Developers might find the following resources helpful when creating`GameActivity`applications:

- [GameActivity get started](https://developer.android.com/games/agdk/game-activity/get-started)
- [GameTextInput user documentation](https://developer.android.com/games/agdk/add-support-for-text-input)
- [agdkTunnel sample](https://github.com/android/games-samples/tree/main/agdk/agdktunnel)
- [Jetpack reference documentation for GameActivity](https://developer.android.com/reference/games/game-activity)
- [Jetpack reference documentation for GameTextInput](https://developer.android.com/reference/games/game-text-input)
- [AGDK source code](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/refs/heads/master/game-activity/)

## Feedback

GameActivity and GameTextInput are both part of Jetpack games library. For any issues and questions, create[a bug on the Google IssueTracker](https://issuetracker.google.com/issues/new?component=897320&pli=1&template=1456805).