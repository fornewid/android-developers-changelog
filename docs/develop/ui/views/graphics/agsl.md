---
title: https://developer.android.com/develop/ui/views/graphics/agsl
url: https://developer.android.com/develop/ui/views/graphics/agsl
source: md.txt
---

# Android Graphics Shading Language (AGSL) is used by Android 13 and above to define the behavior of programmable[`RuntimeShader`](https://developer.android.com/reference/android/graphics/RuntimeShader)objects. AGSL shares much of its syntax with GLSL fragment shaders, but works within the Android graphics rendering system to both customize painting within`Canvas`and filter`View`content.

## Theory of operation

AGSL effects exist as part of the larger Android graphics pipeline. When Android issues a GPU accelerated drawing operation, it assembles a single GPU fragment shader to do the required work. This shader typically includes several pieces. For example, it might include:

- Evaluating whether a pixel falls inside or outside of the shape being drawn (or on the border, where it might apply anti-aliasing).
- Evaluating whether a pixel falls inside or outside of the clipping region (again, with possible anti-aliasing logic for border pixels).
- Logic for the[`Shader`](https://developer.android.com/reference/android/graphics/Shader)on the[`Paint`](https://developer.android.com/reference/android/graphics/Paint). The Shader can actually be a tree of objects (due to[`ComposeShader`](https://developer.android.com/reference/android/graphics/ComposeShader)and other features described below).
- Similar logic for the[`ColorFilter`](https://developer.android.com/reference/android/graphics/ColorFilter).
- Blending code (for certain types of[`BlendMode`](https://developer.android.com/reference/android/graphics/BlendMode)).
- Color space conversion code, as part of Android's color management.
- When the`Paint`has a complex tree of objects in the`Shader`,`ColorFilter`, or`BlendMode`fields, there is still only a single GPU fragment shader. Each node in that tree creates a single function. The clipping code and geometry code each create a function. The blending code might create a function. The overall fragment shader then calls all of these functions (which may call other functions, e.g. in the case of a shader tree).

Your AGSL effect contributes a function (or functions) to the GPU's fragment shader.

## Basic syntax

AGSL (and GLSL) are C-style domain specific languages. Types such as`bool`and`int`closely track their C equivalents; there are additional types to support vectors and matrices that support domain functionality.

Qualifiers can be applied to types for precision hints in a way that's unique to shading languages. Control structures such as`if-else`statements work much like they do in C; the language also provides support for`switch`statements and`for`loops with limitations. Some control structures require constant expressions that can be evaluated at compile time.

AGSL supports functions; every shader program begins with the`main`function. User defined functions are supported, without support for recursion of any kind. Functions use a "value-return" calling convention; values passed to functions are copied into parameters when the function is called, and outputs are copied back; this is determined by the`in`,`out`, and`inout`qualifiers.