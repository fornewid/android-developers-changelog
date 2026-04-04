---
title: https://developer.android.com/games/guides/basics
url: https://developer.android.com/games/guides/basics
source: md.txt
---

There are three basic components of your development environment that you
must decide on before you start developing an Android game.
These include:

- Game engines
- Integrated development environments (IDEs)
- Graphics APIs

## Develop with game engines

A *game engine* is a software framework that includes a set of libraries and
tools for game development. Using a game engine lets you focus on game
content and optimization, while easily implementing things like:

- Graphics
- Animation
- Sound
- Game loops
- Input device support

Game engines usually include an IDE and other tools for configuring features,
designing, developing, compiling, and exporting your game to Android and other
platforms.

To work with a game engine, you can choose from the following approaches:

- Use an unmodified game engine (recommended)
- Customize an existing game engine
- Develop a new game engine

### Use an unmodified game engine (recommended)

Working with an unmodified game engine is the simplest approach to developing
Android games. To do so, you must choose a game engine that meets Android
development requirements.

#### Game engines you can use without modification

Here are some existing game engines that support Android development:

- **Unity**: commercial; uses the C# programming language.
- **Godot**: open source; supports multiple programming languages including GDScript, C#, and C++.
- **Defold**: open source; uses the Lua programming language.
- **Unreal**: commercial; uses the Blueprint visual scripting system and C++. (Specializes in high-end 3D graphics)

For information about setting up and working with these engines, see
[Using a game engine on Android](https://developer.android.com/games/engines/engines-overview).

## Develop with IDEs

The IDE you use to develop Android games depends on the game engine you use and
your workflow. The most common game engines include a game editor for design and
code editing, which game developers typically use along with Android Studio.

### Game editors

A *game editor* often tightly integrates game design features with code editing.
In some cases these editors help designers complete development tasks
without writing code.

If you are developing your first Android game, the simplest and best option is
to use a game editor along with Android Studio, because game editors:

- Provide UI and a toolset focused on game design.
- Integrate asset design and code editing tasks.
- Focus on the supported programming language.
- Include modeling and rendering tools.

### Android Studio

Android Studio is the official IDE for developing Android apps. You should
install it along with any other IDEs that you plan to use. With Android Studio,
you can:

- Debug code written in C/C++, Java, or Kotlin.
- Manage the Android SDK, which you must use to build Android games.
- Build, test, profile, and optimize games.
- Edit C/C++ code using the [Android NDK](https://developer.android.com/ndk).
- Configure app packages and Google Play settings.

For more information, see [Android Studio](https://developer.android.com/studio).

### Visual Studio

If you're developing your game on Windows using Visual Studio, you can add
Android as a target using the Android Game Development Extension (AGDE) for
Visual Studio. This option for advanced game developers targets games that are
already in development using a Visual C++ project. You can use AGDE to do the
following:

- Use an existing Visual C++ project to create an Android game.
- Debug and profile your game using Visual Studio.
- Use distributed build systems such as Incredibuild or SN-DBS.

For more information, see [AGDE](https://developer.android.com/games/agde).

## Develop with Google Play Games Services

To add social features to your game, view gameplay statistics, and provide
cross-platform gameplay across multiple devices, you can use Google Play Games Services.
You can set up and manage Play Games Services in the Google Play Console. You
can then add features using the Play Games Services APIs for Android, C, and
Unity.
For more information, see [Play Games Services overview](https://developer.android.com/games/pgs/overview).

## Develop with Graphics APIs

To achieve the best 2D and 3D graphics performance, your Android game must use a
low-level graphics API to communicate with a GPU. The most widely supported
options for Android game development are:

- OpenGL ES
- Vulkan

OpenGL ES or Vulkan are required to use the Android Games Development Kit (AGDK)
to develop a game in C or C++. They are the only two graphics APIs
supported by the Android GPU Inspector (AGI) graphics profiling tool.

For information about the Android GPU Inspector, see
[AGI](https://developer.android.com/agi).