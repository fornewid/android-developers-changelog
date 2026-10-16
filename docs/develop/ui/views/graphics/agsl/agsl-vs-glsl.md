---
title: https://developer.android.com/develop/ui/views/graphics/agsl/agsl-vs-glsl
url: https://developer.android.com/develop/ui/views/graphics/agsl/agsl-vs-glsl
source: md.txt
---

AGSL and GLSL are very similar in syntax, allowing many GLSL fragment shader
effects to be brought over to Android with minimal changes. AGSL fixes its GLSL
feature set at GLSL ES 1.0 (the shading language used by OpenGL ES 2.0) to
provide for maximum device reach.

A GLSL fragment shader controls the entire behavior of the GPU between the
rasterizer and the blending hardware. That shader does all the work to compute a
color, and the color it generates is exactly what is fed to the blending stage
of the pipeline. When you write a shader in AGSL, you are programming a stage of
the Android graphics pipeline. Many of the language differences stem from this.

## Shader execution

Just like in a GLSL shader, an AGSL shader begins execution in a main function.
Unlike GLSL, the function takes the shader position in "local" coordinates as a
parameter. This is similar to `gl_FragCoord`, but rather than framebuffer
coordinates, these coordinates may have been translated prior to calling your
shader. Your shader then returns the pixel color as a `vec4` in medium or
high precision (similar to `out vec4 color` or `gl_FragColor` in GLSL).

    mediump vec4 main(in vec2 fragCoord)

## Coordinate space

![GLSL vs AGSL coordinate spaces](https://developer.android.com/static/images/guide/topics/graphics/agsl/agsl-coordinate-glsl-vs-agsl.png)

*Shader drawn using GLSL vs [Near identical shader drawn using AGSL](https://shaders.skia.org/?id=9dc5c7170e82d49c47a3ee20d679ad5bef45b5ca7e23c4327dd93b8d3101256f)*

AGSL and GLSL use different coordinate spaces by default. In GLSL, the fragment
coordinate (fragCoord) is relative to the lower left. AGSL matches the screen
coordinate system of [Canvas](https://developer.android.com/reference/android/graphics/Canvas),
which means that the Y axis begins from the upper left corner. If needed, you
can convert between these two spaces by passing in the resolution as a uniform
and using `resolution.y - fragCoord.y` for the Y axis value. Alternatively, you
can apply a local transformation matrix to your shader.

    // AGSL to GLSL coordinate space transformation matrix
    val localMatrix = Matrix()
    localMatrix.postScale(1.0f, -1.0f)
    localMatrix.postTranslate(0.0f, viewHeight)
    gridShader.setLocalMatrix(localMatrix)

## Precision and types

GLSL compatible precision modifiers are supported, but AGSL introduces
`half` and `short` types which also represent medium precision.

Vector types can be declared as named \<base type\>\<columns\>. You can use
`float2` instead of `vec2` and `bool4` instead of `bvec4`.
Matrix types can be declared as named \<base type\>\<columns\>x\<rows\>, so
`float3x3` instead of `mat3`. AGSL also allows GLSL-style declarations
for `mat` and `vec` and these types are mapped to their float
equivalents.

## Preprocessor

AGSL doesn't support GLSL style
[preprocessor](https://www.khronos.org/opengl/wiki/Core_Language_(GLSL)#Preprocessor_directives)
directives. Convert #define statements to const variables. AGSL's compiler
supports constant folding and branch elimination for const variables, so these
will be efficient.

## Color spaces

Android Applications are color managed. The color space of a Canvas determines
the working color space for drawing. Source content (like shaders, including
[BitmapShader](https://developer.android.com/reference/android/graphics/BitmapShader))
also have color spaces.

For certain effects, such as physically accurate lighting, math should be done
in a linear color space. To help with this, AGSL provides these intrinsic
functions:

    half3 toLinearSrgb(half3 color)
    half3 fromLinearSrgb(half3 color)

These convert colors between the working color space and Android's
[`LINEAR_EXTENDED_SRGB`](https://developer.android.com/reference/android/graphics/ColorSpace.Named#LINEAR_EXTENDED_SRGB)
color space. That space uses the sRGB color primaries (gamut), and a linear
transfer function. It represents values outside of the sRGB gamut using extended
range values (below 0.0 and above 1.0).

### Uniforms

Since AGSL doesn't know if uniforms contain colors, it won't automatically apply
a color conversion to them. You can label `half4`/`float4`/`vec4` with
`layout(color)`, which lets Android know that the uniform will be used as a
color, allowing Android to transform the uniform value to the working color
space.

In AGSL, declare the uniform like this:

    layout(color) uniform half4 iColor;  // Input color
    uniform float2 iResolution;          // Viewport resolution (pixels)

In Android code, you can then set the uniform like this:

    shader.setColorUniform("iColor", Color.GREEN)
    shader.setFloatUniform("iResolution", canvas.width.toFloat(), canvas.height.toFloat())