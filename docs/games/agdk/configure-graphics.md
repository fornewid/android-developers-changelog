---
title: https://developer.android.com/games/agdk/configure-graphics
url: https://developer.android.com/games/agdk/configure-graphics
source: md.txt
---

# Configure graphics with OpenGL ES

To draw objects and sprites in your game, you will need to configure the display, surface and context variables, set up rendering in your game loop, and draw each scene and object.

There are two ways to draw images to the screen for a C or C++ game, namely with[OpenGL ES](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl), or[Vulkan](https://developer.android.com/ndk/guides/graphics/getting-started).

- [OpenGL ES](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl)is part of the[Open Graphics Library (OpenGL®)](https://www.khronos.org/opengles/)specification intended for mobile devices such as Android. Learn how to configure OpenGL ES for your game in this topic.

- If you use Vulkan for your game, read the[Getting started with Vulkan](https://developer.android.com/ndk/guides/graphics/getting-started)guide.

| **Note:** The code in this topic is based on the[Endless Tunnel](https://github.com/android/ndk-samples/tree/master/endless-tunnel)sample, where details may differ for your game. Understand and adapt these concepts for your specific use case.

## Before you get started

If you haven't already done so,[set up a GameActivity object](https://developer.android.com/games/agdk/game-activity)in your Android project.

## Set up OpenGL ES variables

1. You will need a[display](https://developer.android.com/reference/android/opengl/EGLDisplay),[surface](https://developer.android.com/reference/android/opengl/EGLSurface),[context](https://developer.android.com/reference/android/opengl/EGLContext), and[config](https://developer.android.com/reference/android/opengl/EGLConfig)to render your game. Add the following OpenGL ES variables to your game engine's header file:

       class NativeEngine {
        //...
        private:
         EGLDisplay mEglDisplay;
         EGLSurface mEglSurface;
         EGLContext mEglContext;
         EGLConfig mEglConfig;

         bool mHasFocus, mIsVisible, mHasWindow;
         bool mHasGLObjects;
         bool mIsFirstFrame;

         int mSurfWidth, mSurfHeight;
       }

2. In the constructor for your game engine, initialize the default values for the variables.

       NativeEngine::NativeEngine(struct android_app *app) {
         //...
         mEglDisplay = EGL_NO_DISPLAY;
         mEglSurface = EGL_NO_SURFACE;
         mEglContext = EGL_NO_CONTEXT;
         mEglConfig = 0;

         mHasFocus = mIsVisible = mHasWindow = false;
         mHasGLObjects = false;
         mIsFirstFrame = true;

         mSurfWidth = mSurfHeight = 0;
       }

3. Initialize the display to render.

       bool NativeEngine::InitDisplay() {
         if (mEglDisplay != EGL_NO_DISPLAY) {
           return true;
         }

         mEglDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);
         if (EGL_FALSE == eglInitialize(mEglDisplay, 0, 0)) {
           LOGE("NativeEngine: failed to init display, error %d", eglGetError());
           return false;
         }
         return true;
       }

4. The surface can be an off-screen buffer (pbuffer) allocated by EGL, or a window allocated by the Android OS. Initialize this surface:

       bool NativeEngine::InitSurface() {
         ASSERT(mEglDisplay != EGL_NO_DISPLAY);
         if (mEglSurface != EGL_NO_SURFACE) {
           return true;
         }

         EGLint numConfigs;
         const EGLint attribs[] = {
           EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT, // request OpenGL ES 2.0
           EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
           EGL_BLUE_SIZE, 8,
           EGL_GREEN_SIZE, 8,
           EGL_RED_SIZE, 8,
           EGL_DEPTH_SIZE, 16,
           EGL_NONE
         };

         // Pick the first EGLConfig that matches.
         eglChooseConfig(mEglDisplay, attribs, &mEglConfig, 1, &numConfigs);
         mEglSurface = eglCreateWindowSurface(mEglDisplay, mEglConfig, mApp->window,
                                              NULL);
         if (mEglSurface == EGL_NO_SURFACE) {
           LOGE("Failed to create EGL surface, EGL error %d", eglGetError());
           return false;
         }
         return true;
       }

5. Initialize the rendering context. This example creates an[OpenGL ES 2.0](https://developer.android.com/reference/android/opengl/GLES20)context:

       bool NativeEngine::InitContext() {
         ASSERT(mEglDisplay != EGL_NO_DISPLAY);
         if (mEglContext != EGL_NO_CONTEXT) {
           return true;
         }

         // OpenGL ES 2.0
         EGLint attribList[] = { EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE };
         mEglContext = eglCreateContext(mEglDisplay, mEglConfig, NULL, attribList);
         if (mEglContext == EGL_NO_CONTEXT) {
           LOGE("Failed to create EGL context, EGL error %d", eglGetError());
           return false;
         }
         return true;
       }

6. Configure your OpenGL ES settings before drawing. This example is executed at the beginning of every frame. It enables depth testing, sets the clear color to black, and clears the color and depth buffers.

       void NativeEngine::ConfigureOpenGL() {
         glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
         glEnable(GL_DEPTH_TEST);
         glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT);
       }

## Render with the game loop

1. The game loop renders a frame and repeats indefinitely until the user quits. Between frames, your game may:

   - [Process events](https://developer.android.com/games/agdk/game-activity/get-started#handle-events)such as input,[audio output](https://developer.android.com/games/sdk/oboe), and networking events.

   - Update the game logic and user interface.

   - Render a frame to the display.

   To render a frame to the display, the`DoFrame`method is called indefinitely in the game loop:  

       void NativeEngine::GameLoop() {
         // Loop indefinitely.
         while (1) {
           int events;
           struct android_poll_source* source;

           // If not animating, block until we get an event.
           while ((ALooper_pollAll(IsAnimating() ? 0 : -1, NULL, &events,
                                   (void **) &source)) >= 0) {
             // Process events.
             ...
           }

           // Render a frame.
           if (IsAnimating()) {
               DoFrame();
           }
         }
       }

2. In the`DoFrame`method, query the current surface dimensions, request`SceneManager`to render a frame, and swap the display buffers.

       void NativeEngine::DoFrame() {
         ...
         // Query the current surface dimension.
         int width, height;
         eglQuerySurface(mEglDisplay, mEglSurface, EGL_WIDTH, &width);
         eglQuerySurface(mEglDisplay, mEglSurface, EGL_HEIGHT, &height);

         // Handle dimension changes.
         SceneManager *mgr = SceneManager::GetInstance();
         if (width != mSurfWidth || height != mSurfHeight) {
           mSurfWidth = width;
           mSurfHeight = height;
           mgr->SetScreenSize(mSurfWidth, mSurfHeight);
           glViewport(0, 0, mSurfWidth, mSurfHeight);
         }
         ...
         // Render scenes and objects.
         mgr->DoFrame();

         // Swap buffers.
         if (EGL_FALSE == eglSwapBuffers(mEglDisplay, mEglSurface)) {
           HandleEglError(eglGetError());
         }
       }

## Render scenes and objects

1. The game loop processes a hierarchy of visible scenes and objects to render. In the Endless Tunnel example, a`SceneManager`keeps track of multiple scenes, with only one scene active at a time. In this example, the current scene is rendered:

       void SceneManager::DoFrame() {
         if (mSceneToInstall) {
           InstallScene(mSceneToInstall);
           mSceneToInstall = NULL;
         }

         if (mHasGraphics && mCurScene) {
           mCurScene->DoFrame();
         }
       }

2. Depending on your game, a scene may contain background, text, sprites and game objects. Render them in the order suitable for your game. This example renders the background, text, and widgets:

       void UiScene::DoFrame() {
         // clear screen
         glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
         glDisable(GL_DEPTH_TEST);

         RenderBackground();

         // Render the "Please Wait" sign and do nothing else
         if (mWaitScreen) {
           SceneManager *mgr = SceneManager::GetInstance();
           mTextRenderer->SetFontScale(WAIT_SIGN_SCALE);
           mTextRenderer->SetColor(1.0f, 1.0f, 1.0f);
           mTextRenderer->RenderText(S_PLEASE_WAIT, mgr->GetScreenAspect() * 0.5f,
                                     0.5f);
           glEnable(GL_DEPTH_TEST);
           return;
         }

         // Render all the widgets.
         for (int i = 0; i < mWidgetCount; ++i) {
           mWidgets[i]->Render(mTrivialShader, mTextRenderer, mShapeRenderer,
                 (mFocusWidget < 0) ? UiWidget::FOCUS_NOT_APPLICABLE :
                 (mFocusWidget == i) ? UiWidget::FOCUS_YES : UiWidget::FOCUS_NO,tf);
         }
         glEnable(GL_DEPTH_TEST);
       }

## Resources

Read the following for more information about OpenGL ES and Vulkan:

- [OpenGL ES](https://developer.android.com/develop/ui/views/graphics/opengl/about-opengl)- Images and graphics in Android.

- [OpenGL ES](https://source.android.com/devices/graphics/arch-egl-opengl)- Overview in Android Source.

- [Vulkan](https://developer.android.com/ndk/guides/graphics/getting-started)- Getting started in NDK.

- [Vulkan](https://source.android.com/devices/graphics/arch-vulkan)- Overview in Android Source.

- [Understand Android game loops](https://developer.android.com/games/develop/gameloops)- learn to pace frames, queue buffers, handle VSYNC callbacks, and manage threads.