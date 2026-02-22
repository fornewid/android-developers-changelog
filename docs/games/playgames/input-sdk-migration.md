---
title: https://developer.android.com/games/playgames/input-sdk-migration
url: https://developer.android.com/games/playgames/input-sdk-migration
source: md.txt
---

This guide describes how to migrate your game to use the latest
Input SDK. The 1.0.0-beta SDK has substantial improvements over the
previous 0.0.4 preview. You should migrate from the earlier previews as soon as
possible. The 0.0.4 SDK will continue function through March 2023.

## Update the dependency

Delete the 0.0.4 library from your `libs` directory since the library is now
available on maven. Then Find this line in your module-level `build.grade`
file:

    implementation files('libs/inputmapping-0.0.4.aar')

Replace it with the following code:

    implementation 'com.google.android.libraries.play.games:inputmapping:1.0.0-beta'

## Implement the new InputMappingProvider interface

The former abstract class `InputMappingProvider` turned into an interface in
version `1.0.0-beta`. The method `onProvideInputMap()` is still part of the
interface.

<br />

### Kotlin

<br />

Remove `()` from the class definition since there's no constructor to invoke in
`InputMappingProvider`.

Locate your `InputMappingProvider` implementation:

    class MyInputMapProvider : InputMappingProvider() {
        override fun onProvideInputMap(): InputMap {
            TODO("Not yet implemented")
        }
    }

And update it to this:

    class MyInputMapProvider : InputMappingProvider {
        override fun onProvideInputMap(): InputMap {
            TODO("Not yet implemented")
        }
    }

<br />

### Java

<br />

Replace `extends` with `implements` to indicate that your implementing an
interface rather than extending a class.

Locate where you extend `InputMappingProvider`:

    public class MyInputMapProvider extends InputMappingProvider {
        @NonNull
        @Override
        public InputMap onProvideInputMap() {
            // TODO: return an InputMap
        }
    }

And change it to implement `InputMappingProvider`:

    public class MyInputMapProvider implements InputMappingProvider {
        @NonNull
        @Override
        public InputMap onProvideInputMap() {
            // TODO: return an InputMap
        }
    }

<br />

<br />

## Use the new InputClient

`registerInputMappingProvider` and `unregisterInputMappingProvider` have been
replaced with `setInputMappingProvider` and `clearInputMappingProvider`.
Further, `clearInputMappingProvider` no longer takes an argument so you no
longer need to keep a reference to your provider to unregister it later.

<br />

### Kotlin

To register your input map provider, locate your call to `registerInputMappingProvider`:

<br />

    private val myInputMapProvider by lazy {
        MyInputMapProvider()
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val inputMappingClient = Input.getInputMappingClient(this)
        inputMappingClient.registerInputMappingProvider(myInputMapProvider)
    }

And replace it with `setInputMappingProvider`:

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val inputMappingClient = Input.getInputMappingClient(this)
        inputMappingClient.setInputMappingProvider(MyInputMapProvider())
    }

To clear your input map, locate your call to `unregisterInputMappingProvider`:

    override fun onDestroy() {
        val inputMappingClient = Input.getInputMappingClient(this)
        inputMappingClient.unregisterInputMappingProvider(myInputMapProvider)

        super.onDestroy()
    }

And replace it with `clearInputMappingprovider`:

    override fun onDestroy() {
        val inputMappingClient = Input.getInputMappingClient(this)
        inputMappingClient.clearInputMappingProvider()

        super.onDestroy()
    }

<br />

### Java

<br />

To register your input map provider, locate your call to
`registerInputMappingProvider`:

    private final MyInputMapProvider myInputMapProvider = new MyInputMapProvider();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        InputMappingClient inputMappingClient = Input.getInputMappingClient(this);
        inputMappingClient.registerInputMappingProvider(myInputMapProvider);
    }

And replace it with `setInputMappingProvider`:

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        InputMappingClient inputMappingClient = Input.getInputMappingClient(this);
        inputMappingClient.setInputMappingProvider(new MyInputMapProvider());
    }

To clear your input mapping provider, locate your call to
`unregisterInputMappingProvider`:

    @Override
    protected void onDestroy() {
        InputMappingClient inputMappingClient = Input.getInputMappingClient(this);
        inputMappingClient.unregisterInputMappingProvider(myInputMapProvider);

        super.onDestroy();
    }

And replace it with `clearInputMappingProvider`:

    @Override
    protected void onDestroy() {
        InputMappingClient inputMappingClient = Input.getInputMappingClient(this);
        inputMappingClient.clearInputMappingProvider();

        super.onDestroy();
    }

<br />

<br />