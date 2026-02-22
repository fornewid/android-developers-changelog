---
title: https://developer.android.com/ndk/guides/graphics/shader-compilers
url: https://developer.android.com/ndk/guides/graphics/shader-compilers
source: md.txt
---

# Vulkan shader compilers on Android

A Vulkan app must manage shaders differently from the way an OpenGL ES app does: In OpenGL ES, you provide a shader as a set of strings forming the source text of a GLSL shader program. By contrast, the Vulkan API requires you to provide a shader in the form of an entry point in a[SPIR-V](https://www.khronos.org/spir)module.

The[NDK Release 12 and later](https://github.com/android-ndk/ndk/wiki)includes a runtime library for compiling GLSL into SPIR-V. The runtime library is the same as the one in the[Shaderc](https://github.com/google/shaderc)open source project, and uses the same[Glslang GLSL](https://github.com/KhronosGroup/glslang)reference compiler as its back end. By default, the Shaderc version of the compiler assumes you are compiling for Vulkan. After checking whether your code is valid for Vulkan, the compiler automatically enables the`KHR_vulkan_glsl`extension. The Shaderc version of the compiler also generates Vulkan-compliant SPIR-V code.

You can choose to compile SPIR-V modules into your Vulkan app during development, a practice called*ahead-of-time* , or*AOT* , compilation. Alternatively, you can have your app compile them from shipped or procedurally generated shader source when needed during runtime. This practice is called*runtime compiling*. Android Studio has integrated support to build Vulkan shaders.

The rest of this page provides more detail about each practice, and then explains how to integrate shader compilation into your Vulkan app.

## AOT compilation

There are two ways to achieve shader AOT compilation, described in the following sections.

### Use Android Studio

Putting shaders into`app/src/main/shaders/`, Android Studio recognizes shaders by[their file extensions](https://github.com/google/shaderc/tree/main/glslc), and will complete the following actions:

- Compile all shader files recursively under that directory.
- Append the .spv suffix to the compiled SPIR-V shader files.
- Pack SPIRV-shaders into the APK's`assets/shaders/`directory.

The application would load the compiled shaders from the corresponding`assets/shaders/`location at run time; the compiled spv shader file structure is the same as the application's GLSL shader file structure under`app/src/main/shaders/`:  

```c++
AAsset* file = AAssetManager_open(assetManager,
                     "shaders/tri.vert.spv", AASSET_MODE_BUFFER);
size_t fileLength = AAsset_getLength(file);
char* fileContent = new char[fileLength];
AAsset_read(file, fileContent, fileLength);
```

Shaderc compile flags could be configured inside the gradle DSL`shaders`block, as shown in the following example:  

### Groovy

```groovy
android {
  defaultConfig {
    shaders {
      glslcArgs.addAll(['-c', '-g'])
      scopedArgs.create('lights') {
        glslcArgs.addAll(['-DLIGHT1=1', '-DLIGHT2=0'])
      }
    }
  }
}
```

### Kotlin

```kotlin
android {
  defaultConfig {
    shaders {
        glslcArgs += listOf("-c", "-g")
        glslcScopedArgs("lights", "-DLIGHT1=1", "-DLIGHT2=0")
    }
  }
}
```

`glslcArgs`apply to all shader compilations;`scopedArgs`only apply when compiling for that scope. The above example creates a scope argument`lights`, which will only apply to GLSL shaders under the`app/src/main/shaders/lights/`directory. Refer to[glslc](https://github.com/google/shaderc/tree/main/glslc)for the complete list of available compilation flags. Note that Shaderc inside NDK is a snapshot from that github repo at the NDK release time; you can get the exact supported flags for that version with the command`glslc --help`, as decribed in the next section.

### Offline command-line compilation

GLSL Shaders can be compiled to SPIR-V independent of the main application using the*glslc* command-line compiler. NDK release 12 and later packs a version of pre-built*glslc* and related tools in the`<android-ndk-dir>/shader-tools/`directory to support this usage model.

The compiler is also available from the[Shaderc](https://github.com/google/shaderc)project; follow the instructions there to build a binary version.

*glslc* provides a rich set of[command-line options](https://github.com/google/shaderc/tree/main/glslc)for shader compilation to meet various requirements for an application.

The glslc tool compiles a single-source file to a SPIR-V module with a single shader entry point. By default, the output file has the same name as that of the source file, but with the`.spv`extension appended.

You use filename extensions to tell the glslc tool which graphics shader stage to compile, or whether a compute shader is being compiled. For information on how to use these filename extensions, and options you can use with the tool, see[Shader stage specification](https://github.com/google/shaderc/tree/main/glslc#user-content-shader-stage-specification)in the[glslc](https://github.com/google/shaderc/tree/main/glslc)manual.

## Runtime compilation

For JIT compilation of shaders during runtime, the NDK provides the libshaderc library, which has both C and C++ APIs.

C++ applications should use the C++ API. We recommend that apps in other languages use the C API, because the C ABI is lower level, and likely to provide better stability.

The following example shows how to use the C++ API:  

```c++
#include <iostream>
#include <string>
#include <vector>
#include <shaderc/shaderc.hpp>

std::vector<uint32_t> compile_file(const std::string& name,
                                   shaderc_shader_kind kind,
                                   const std::string& data) {
  shaderc::Compiler compiler;
  shaderc::CompileOptions options;

  // Like -DMY_DEFINE=1
  options.AddMacroDefinition("MY_DEFINE", "1");

  shaderc::SpvCompilationResult module = compiler.CompileGlslToSpv(
      data.c_str(), data.size(), kind, name.c_str(), options);

  if (module.GetCompilationStatus() !=
      shaderc_compilation_status_success) {
    std::cerr << module.GetErrorMessage();
  }

  std::vector<uint32_t> result(module.cbegin(), module.cend());
  return result;
}
```

## Integrate into your projects

You can integrate the Vulkan shader compiler into your app using either the project's`Android.mk`file or Gradle.

### Android.mk

Perform the following steps to use your project's`Android.mk`file to integrate the shader compiler.

1. Include the following lines in your Android.mk file:  

   ```
   include $(CLEAR_VARS)
        ...
   LOCAL_STATIC_LIBRARIES := shaderc
        ...
   include $(BUILD_SHARED_LIBRARY)

   $(call import-module, third_party/shaderc)
   ```
2. Set APP_STL to one of`c++_static`,`c++_shared`,`gnustl_static`, or`gnustl_shared`in app's Application.mk

### Gradle's CMake integration

1. In a terminal window, navigate to`ndk_root/sources/third_party/shaderc/`.
2. Run the following command to build NDK's Shaderc. You only need to run this command once on each NDK version that you use:  

   ```
   $ ../../../ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk \
   APP_STL:=<stl_version> APP_ABI=all libshaderc_combined
   ```

   This command places two folders in \<ndk_root\>/sources/third_party/shaderc/. The directory structure is as follows:  

   ```
   include/
     shaderc/
       shaderc.h
       shaderc.hpp
   libs/
     <stl_version>/
       {all of the abis}
          libshaderc.a
   ```
3. Add the generated includes and libs using[`target_include_directories`](https://cmake.org/cmake/help/v3.12/command/target_include_directories.html?highlight=target_include_directories)and[`target_link_libraries`](https://cmake.org/cmake/help/v3.12/command/target_link_libraries.html?highlight=target_link_lib#target-link-libraries), as you normally do for similar[external libraries](https://github.com/android/ndk-samples/blob/master/hello-libs/app/src/main/cpp/CMakeLists.txt). Your app's STL type must match one of the`stl`types specified in`stl_version`. The NDK recommends using`c++_shared`or`c++_static`, although`gnustl_static`and`gnustl_shared`are also supported.

## Get the latest Shaderc

Shaderc in NDK comes from[Android Source tree](https://android.googlesource.com/platform/external/shaderc), which is a snapshot of[the upstream Shaderc repo](https://github.com/google/shaderc). If you need the latest Shaderc, refer to[build instruction for details](https://github.com/google/shaderc/blob/master/README.md). The high-level steps are as follows:

1. Download the latest Shaderc:  

   ```
   git clone https://github.com/google/shaderc.git
   ```
2. Update dependencies:  

   ```
   ./utils/git-sync-deps
   ```
3. Build Shaderc:  

   ```
   <ndk_dir>/ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk \
       APP_STL:=c++_static APP_ABI=all libshaderc_combined -j16
   ```
4. Configure your project to use your own Shaderc build in your build script file.

<br />