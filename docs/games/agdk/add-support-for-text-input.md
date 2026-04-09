---
title: https://developer.android.com/games/agdk/add-support-for-text-input
url: https://developer.android.com/games/agdk/add-support-for-text-input
source: md.txt
---

# GameTextInputPart of[Android Game Development Kit](https://developer.android.com/games/agdk/overview).

Using the[`GameTextInput`](https://developer.android.com/reference/games/game-text-input)library is a simpler alternative to writing a full-screen Android app that uses the soft keyboard for text input.

`GameTextInput`provides a straightforward API to show or hide the soft keyboard, set or get the currently-edited text, and receive notifications when the text is changed. This is not meant for fully-fledged text editor apps, but still provides selection and composing region support for typical uses cases in games. Also, this library supports advanced[input method editor (IME)](https://developer.android.com/guide/topics/text/creating-input-method)features such as spell- checking, completions, and multi-key characters.

Internally,`GameTextInput`accumulates the input text (together with the relevant states) to the internal buffer[`GameTextInput::currentState_`](https://developer.android.com/games/agdk/reference/games/game-text-input/struct/game-text-input-state)and notifies the app of any changes in it. The app then performs text processing in its registered callback function.

## Availability

`GameTextInput`can be used in the following ways:

- Together with GameActivity: GameActivity integrates GameTextInput. Applications that use GameActivity can only use the integrated GameTextInput. Usage instructions are fully documented on[the GameActivity page](https://developer.android.com/games/agdk/game-activity/use-text-input). For a sample of GameActivity and GameTextInput integration, see the[games-samples repository](https://github.com/android/games-samples). This usage model is not within the scope of this guide.

- As a standalone library: the rest of the guide describes the usage steps.

Note that the above two methods are mutually exclusive.

Formal`GameTextInput`releases are available in the Jetpack games library release in[Google Maven](https://maven.google.com/web/index.html?q=game#androidx.games:games-text-input).

## Set up your build

`GameTextInput`is distributed as an[Android Archive (AAR)](https://developer.android.com/studio/projects/android-library). This AAR contains the Java classes and the C source code, which implements the native features of`GameTextInput`. You need to include these source files as part of your build process via[`Prefab`](https://developer.android.com/studio/build/dependencies#using-native-dependencies), which exposes native libraries and source code to your[CMake project](https://developer.android.com/ndk/guides/cmake)or[NDK build](https://developer.android.com/ndk/guides).

1. Follow the instructions on the[Jetpack Android Games](https://developer.android.com/jetpack/androidx/releases/games)page to add the`GameTextInput`library dependency to your game's`build.gradle`file. Note that if your applications are using GameActivity, they*cannot* use the standalone`GameTextInput`library.

2. Make sure`gradle.properties`contains the following lines:

       # Tell Android Studio we are using AndroidX.
       android.useAndroidX=true
       # Use Prefab 1.1.2 or higher, which contains a fix for "header only" libs.
       android.prefabVersion=1.1.2
       # Required only if you're using Android Studio 4.0 (4.1 is recommended).
       # android.enablePrefab=true

3. Import the`game-text-input`package and add it to your target in your project's`CMakeLists.txt`file:

       find_package(game-text-input REQUIRED CONFIG)
       ...
       target_link_libraries(... game-text-input::game-text-input)

4. In one of the`.cpp`files in your game, add the following line to include the`GameTextInput`implementation:

       #include <game-text-input/gametextinput.cpp>

5. In the source files that use the`GameTextInput`C API, include the header file:

       #include <game-text-input/gametextinput.h>

6. Compile and run the app. If you have CMake errors, verify the AAR and the`build.gradle`files are properly set up. If the`#include`file is not found, verify your`CMakeLists.txt`configuration file.

## Integrate your build

1. From your C thread that is already attached to the JVM, or the app main thread, call[`GameTextInput_init`](https://developer.android.com/games/agdk/reference/games/game-text-input/group/game-text-input#gametextinput_init)with a[`JNIEnv`](https://developer.android.com/training/articles/perf-jni#javavm-and-jnienv)pointer.

       static GameTextInput* gameTextInput = nullptr;

       extern "C"
       JNIEXPORT void JNICALL
       Java_com_gametextinput_testbed_MainActivity_onCreated(JNIEnv* env,
         jobject this) {
       {
           if(!gameTextInput)
             gameTextInput = GameTextInput_init(env);
           ...
       }

2. Create a`InputEnabledTextView`Java class with access to[`InputConnection`](https://developer.android.com/reference/android/view/inputmethod/InputConnection).

       public class InputEnabledTextView extends View implements Listener {
         public InputConnection mInputConnection;
         public InputEnabledTextView(Context context, AttributeSet attrs) {
           super(context, attrs);
         }

         public InputEnabledTextView(Context context) {
           super(context);
         }
         public void createInputConnection(int inputType) {
           EditorInfo editorInfo = new EditorInfo();
           editorInfo.inputType = inputType;
           editorInfo.actionId = IME_ACTION_NONE;
           editorInfo.imeOptions = IME_FLAG_NO_FULLSCREEN;
           mInputConnection = new InputConnection(this.getContext(), this,
                   new Settings(editorInfo, true)
           ).setListener(this);
         }

         @Override
         public InputConnection onCreateInputConnection(EditorInfo outAttrs) {
           if (outAttrs != null) {
               GameTextInput.copyEditorInfo(mInputConnection.getEditorInfo(), outAttrs);
           }
           return mInputConnection;
         }

         // Called when the IME input changes.
         @Override
         public void stateChanged(State newState, boolean dismissed) {
           onTextInputEventNative(newState);
         }
         @Override
         public void onImeInsetsChanged(Insets insets) {
           // handle Inset changes here
         }

         private native void onTextInputEventNative(State softKeyboardEvent);
       }

3. Add the created`InputEnabledTextView`to UI layout. For example, the following code in`activity_main.xml`can position it at the bottom of the screen:

       <com.android.example.gametextinputjava.InputEnabledTextView
           android:id="@+id/input_enabled_text_view"
           android:layout_width="wrap_content"
           android:layout_height="wrap_content"
           app:layout_constraintBottom_toBottomOf="parent"
           app:layout_constraintEnd_toEndOf="parent"
           app:layout_constraintStart_toStartOf="parent" />

4. Retrieve this new`InputEnabledTextView`class to your Java activity. This is relative simple when you use[View Binding](https://developer.android.com/topic/libraries/view-binding):

       public class MainActivity extends AppCompatActivity {
         ...
         private ActivityMainBinding binding;
         private InputEnabledTextView inputEnabledTextView;

         private native void setInputConnectionNative(InputConnection c);

         @Override
         protected void onCreate(Bundle savedInstanceState) {
           ...
           binding = ActivityMainBinding.inflate(getLayoutInflater());
           inputEnabledTextView = binding.inputEnabledTextView;
           inputEnabledTextView.createInputConnection(InputType.TYPE_CLASS_TEXT);
           setInputConnectionNative(inputEnabledTextView.mInputConnection);
         }

5. In your C library, pass`inputConnection`into[`GameTextInput_setInputConnection`](https://developer.android.com/reference/games/game-text-input/group/game-text-input#gametextinput_setinputconnection). Pass a callback in[`GameTextInput_setEventCallback`](https://developer.android.com/reference/games/game-text-input/group/game-text-input#gametext-input_seteventcallback)to be notified of events as C state struct[`GameTextInputState`](https://developer.android.com/reference/games/game-text-input/struct/game-text-input-state).

       extern "C"JNIEXPORT void JNICALL
       Java_com_gametextinput_testbed_MainActivity_setInputConnectionNative(
         JNIEnv *env, jobject this, jobject inputConnection) {
         GameTextInput_setInputConnection(gameTextInput, inputConnection);
         GameTextInput_setEventCallback(gameTextInput,[](void *ctx, const GameTexgtInputState *state) {
           if (!env || !state) return;
           // process the newly arrived text input from user.
           __android_log_print(ANDROID_LOG_INFO, "TheGreateGameTextInput", state->text_UTF8);
         }, env);
       }

6. In your C library, call[`GameTextInput_processEvent`](https://developer.android.com/reference/games/game-text-input/group/game-text-input#gametextinput_processevent), which internally calls your callback registered in the previous step, for your app to handle events when the state changes.

       extern "C"
       JNIEXPORT void JNICALL
       Java_com_gametextinput_testbed_InputEnabledTextView_onTextInputEventNative(
         JNIEnv* env, jobject this, jobject soft_keyboard_event) {
         GameTextInput_processEvent(gameTextInput, soft_keyboard_event);
       }

## Utility functions

The`GameTextInput`library includes utility functions that lets you convert between Java state objects and C state structs. Access functionality for showing and hiding the IME through the[`GameTextInput_showIme`](https://developer.android.com/reference/games/game-text-input/group/game-text-input#gametextinput_showime)and[`GameTextInput_hideIme`](https://developer.android.com/reference/games/game-text-input/group/game-text-input#gametextinput_hideime)functions.

## References

Developers may find the following helpful when creating apps with`GameTextInput`:

- [GameTextInput test app](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/refs/heads/master/samples/game_text_input/game_text_input_testbed)
- [Use GameTextInput with GameActivity](https://developer.android.com/games/agdk/game-activity/use-text-input)
- [GameTextInput Reference doc](https://developer.android.com/reference/games/game-text-input)
- [GameTextInput source code](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/refs/heads/master/GameTextInput/)

## Feedback

For any issues and questions for`GameTextInput`, create[a bug on the Google IssueTracker](https://issuetracker.google.com/issues/new?component=897320&pli=1&template=1456805).