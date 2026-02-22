---
title: https://developer.android.com/games/playgames/native-pc/setup
url: https://developer.android.com/games/playgames/native-pc/setup
source: md.txt
---

With the Play Games PC SDK you can access Google Play services to build and
monetize your game on PCs. Sell digital content using Play Billing, seamlessly
sign-in using Play Games, and verify your users have a valid entitlement to your
application with Play Integrity.

Ready to get started?

## Prerequisites

- Create an app entry inside of the Play Console and claim a Play package name.

- Download and install
  [Google Play Games for PC](https://play.google.com/googleplaygames) and sign in with
  your Google Account.

## **Step 1**: Add the SDK to your project

> [!NOTE]
> **Note:** This page contains instructions for both Native C++ games and Unity C# games. All steps must be completed but watch out for unique steps that apply to only Native C++ project or Unity C# project and follow the steps that are relevant to the language you are using.

### C++

- Download the [Play Games PC C++ SDK](https://developer.android.com/games/playgames/native-pc/downloads/cpp).

- Copy the API headers folder `includes/` into your application's codebase.

- Copy the redistributable files from `imports/` directory into your
  application's project, depending on your target architecture:

- **For 64-bit (x64):** Copy the files from `imports/x64/`.

- **For 32-bit (x86):** Copy the files from `imports/x86/`.

- Link your project against `play_pc_sdk.lib` allowing access to the contents
  of the `play_pc_sdk.dll`.

### C#

- Download the [Play Games PC Unity SDK](https://dl.google.com/play/games/native/sdk/unity/play_pc_sdk_unity_26.2.121.0.tgz) as a tarball (.tgz) file.

- The SDK is distributed as a tarball (.tgz) compatible with the **Unity Package Manager (UPM)** . To import the package, see [Install a UPM package from a local tar file](https://docs.unity3d.com/6000.3/Documentation/Manual/upm-ui-tarball.html)

- For detailed documentation, setup instructions, and additional guidance, please refer to the [Play PC Unity Package](https://developer.android.com/games/playgames/native-pc/unity) page.

## **Step 2**: Add a manifest file

Before you can use the SDK from within your game you will need to
associate your game executable with the Play package name that you claimed
inside of the Play Console. This done by adding a `manifest.xml` file in the
same directory as your game's executable.

> [!CAUTION]
> **Caution:** Please note that while there's a Manifest version, you will need to implement a self-update mechanism for your game executable or launcher. In the future, update functionality will be offered under a new Play-Managed-Installs feature.

Example `manifest.xml` contents:

    <?xml version="1.0" encoding="utf-8"?>
    <Manifest version="1">
        <Application>
            <PackageName>com.example.package</PackageName>
        </Application>
    </Manifest>

Example `manifest.xml` placement:

    C:\Program Files
    └───Example Game
        ├───Game.exe
        └───manifest.xml

## **Step 3**: Digitally sign your game

> [!TIP]
> **Tip:** Developers can skip this step during local development by enabling [developer mode](https://developer.android.com/games/playgames/native-pc/setup/developer_mode).

Before your game can use the SDK, the game's executable must be digitally signed
using an
[Authenticode Digital Signature](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode).
For instructions on how to sign an executable see the
[documentation on the SignTool](https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool) .

When you have completed the process for digitally signing your game, send the
certificate information to your Google representative for configuration.

> [!WARNING]
> **Warning:** Safeguard your certificate properly. You must sign all updates to your game using the same certificate.

## **Step 4**: Initialize the SDK

Initialize the SDK during the startup sequence of your game. This should be done
automatically without requiring any user interaction and it is recommended to
verify a successful initialization before rendering your game window.
This provides the best user experience by surfacing and resolving errors as soon
as possible and avoids your game window briefly appearing in cases where your
game process needs to exit.

Start using the SDK by calling
[`GooglePlayInitialize`](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/initialization) (C++) /
[`GooglePlayInitialization.InitializeAsync`](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/initialization) (C#)
to initialize the API. This will setup global state, connect with the SDK
runtime, and verify the application was started correctly. This **MUST** be
called and have the continuation callback complete with `InitializeResult::ok()`
(C++) / `Result.IsOk` (C#) equal to `true` before any other API may be used.

### C++

      // Initialize the SDK as part of the startup sequence of your application.
      auto promise = std::make_shared<std::promise<InitializeResult>>();
      GooglePlayInitialize(
        [promise](InitializeResult result) {
          promise->set_value(std::move(result));
        });

      auto initialize_result = promise->get_future().get();
      if (initialize_result.ok()) {
        // The SDK succeeded with initialization. Continue with the startup sequence
        // of the game.
        // ...
      } else if (initialize_result.code() == InitializationError::kActionRequiredShutdownClientProcess) {
        // The SDK failed to initialize and has requested that your game process exit
        // as soon as possible.
        exit(1);
      } else {
        // The SDK failed to initialize for an alternative reason. It is still
        // generally recommended that you exit the game process as soon as possible,
        // because it won't be possible to access any APIs in the SDK. Critical
        // operations such as verifying the user owns a valid license to your game
        // won't be possible.
        // ...
      }

### C#

      // SDK Clients
      private BillingClient _billingClient;
      private IntegrityClient _integrityClient;

      // Stored product information
      private string _offerToken;

      private async void InitializeSDK()
      {
          // The factory provides the necessary handler for initialization.
          var initializationHandler = PlayPcSdkFactory.InitializationHandler;
          var result = await GooglePlayInitialization.InitializeAsync(initializationHandler);

          if (result.IsOk)
          {
              // Use the factory to get Unity-compatible instances of the clients
              _billingClient = PlayPcSdkFactory.CreateBillingClient();
              _integrityClient = PlayPcSdkFactory.CreateIntegrityClient();

              // SDK is ready for use
          }
          else
          {
              // Handle specific, actionable errors
              if (result.Code == InitializationError.ActionRequiredShutdownClientProcess)
              {
                  Log("This game must be launched through the Google Play Games client. Please exit all game processes immediately, GPG will relaunch the game safely.");
                  Application.Quit();
              }
          }
      }

If the initialization fails with the code `kActionRequiredShutdownClientProcess`
(C++) / `InitializationError.ActionRequiredShutdownClientProcess` (C#), **exit
the game process as soon as possible**. The SDK's runtime will attempt to assist
the user with no additional action required by your game. For example if the
user does not own a valid license to the game, Google Play Games will prompt the
user to purchase a copy. For other errors, you should also exit the game process
because you won't be able to use the SDK to perform critical operations, such as
verifying the user owns a valid license to your game.

A non-successful response may indicate one of the following conditions:

- The SDK runtime is not installed, is not running on the device or is
  an older version not compatible with the SDK integrated into your game.

- The SDK runtime was unable to verify the application identity of the
  game. This could be due to an invalid `manifest.xml` or using the SDK
  without enabling [developer mode](https://developer.android.com/games/playgames/native-pc/setup/developer_mode)
  when developing. Without this your game's executable is required to be
  digitally signed with the digital certificate registered to your Play package
  name.

- The game executable was not launched through the Google Play games client.

- The active user in Google Play Games does not own a license for the
  application.

## **Step 5**: (Optional) Supporting multiple game-processes

Complete these additional integration steps if your game uses multiple
processes, and the Play Games PC SDK is used by a different process than the one
that is launched by Google Play Games on PC. For example, if Google Play Games
on PC launches your game's launcher, and then your launcher starts the game
process that will interact with the SDK.

1. The process directly launched by Google Play Games for PC must
   verify a successful [initialization of the Play Games PC SDK](https://developer.android.com/games/playgames/native-pc/setup#step-4).

   This provides the best user experience by surfacing errors as soon as
   possible. Note that child-process using the SDK must also perform
   initialization in addition to the directly launched process.
2. To use the Play Games PC SDK in a child-process forward the command line
   parameters to the spawned child-process.

   Example command line parameter forwarding:

       Processes hierarchy tree:

       GooglePlayGames.exe
       └───YourGameLauncher.exe --gpg_args=abc --your_args=123
           └───YourGame.exe --gpg_args=abc --your_args=123

   In this example we see a process hierarchy where Google Play Games for PC
   (`GooglePlayGames.exe`) launches the game (`YourGameLauncher.exe`) with some
   example parameters (`--gpg_args=abc --your_args=123`). The game then spawns a
   child-process (`YourGame.exe`) which uses the Play Games PC SDK. To allow this
   the game process launched by Google Play Games for PC forwards the command
   line parameters it was given to the child-process.

   > [!WARNING]
   > **Warning:** You must pass all command-line arguments received from `GooglePlayGames.exe` to all your child processes that are using Play Games PC SDK, such as `YourGame.exe`. Otherwise, all SDK functions fail.

3. Exit all processes when the game stops running.

   When a user closes your game or the game exits due to a SDK initialization
   failure, such as `kActionRequiredShutdownClientProcess`, close all processes
   your game has spawned. This makes certain that the next time your game is
   launched by the Google Play Games for PC client, new changes such as switching
   to a different active account will take effect.

## Next steps

Use the SDK while developing in your IDE:

- Enable [developer mode](https://developer.android.com/games/playgames/native-pc/setup/developer_mode)

Add Google Play PC features to your app:

- Sell digital goods with [Play Billing](https://developer.android.com/games/playgames/native-pc/billing)
- Measure your marketing with [Play Install Referrer](https://developer.android.com/games/playgames/native-pc/install_referrer)
- Protect your game with [Play Integrity for PC](https://developer.android.com/games/playgames/native-pc/trust)