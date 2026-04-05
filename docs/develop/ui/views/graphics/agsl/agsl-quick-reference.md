---
title: https://developer.android.com/develop/ui/views/graphics/agsl/agsl-quick-reference
url: https://developer.android.com/develop/ui/views/graphics/agsl/agsl-quick-reference
source: md.txt
---

AGSL is designed to be largely compatible with GLSL ES 1.0. For more information,
see the equivalent function in the
[OpenGL ES Shading Language documentation](https://www.khronos.org/files/opengles_shading_language.pdf).
When possible, this documentation attempts to call out differences between AGSL
and GLSL.

## Types

AGSL supports GLSL ES 1.0 types along with an additional way to represent vector
and matrix types. AGSL supports additional `short` and `half` types to represent
medium precision.

### Basic types

| Type | Description |
|---|---|
| **`void`** | No function return value or empty parameter list. *Unlike in GLSL, functions without a void return type must return a value.* |
| **`bool, bvec2, bvec3, bvec4`** **`(bool2, bool3, bool4)`**. | Boolean scalar/vector |
| **`int, ivec2, ivec3, ivec4`** **`(int2, int3, int4)`** | `highp` signed integer/vector |
| **`float, vec2, vec3, vec4`** **`(float2, float3, float4)`** | `highp` (single precision) floating point scalar/vector |
| **`short, short2, short3, short4`** | equivalent to `mediump int` signed integer/vector |
| **`half, half2, half3, half4`** | equivalent to `mediump float` scalar/vector |
| **`mat2, mat3, mat4`** **`(float2x2, float3x3, float4x4)`** | 2x2, 3x3, 4x4 `float` matrix |
| **`half2x2, half3x3, half4x4`** | Equivalent to `mediump float` matrix types |

### Precision and range minimums

These are the minimum guaranteed precision and range associated with each
modifier based upon the OpenGL ES 2.0 specification. Since most devices
support ES 3.0, they will have more guaranteed `highp` precision/range and
`int mediump` range. Precision modifiers can be applied to scalar, vector, and
matrix variables and parameters. Only the minimums listed below are guaranteed;
`lowp` is not necessarily actually lower precision than `mediump`, and `mediump`
is not necessarily lower precision than `highp`. AGSL currently converts `lowp`
to `mediump` in the final output.

| Modifier | 'float' range | 'float' magnitude range | 'float' precision | 'int' range |
|---|---|---|---|---|
| highp | \\(\\left\\{-2\^{62},2\^{62}\\right\\}\\) | \\(\\left\\{2\^{-62},2\^{62}\\right\\}\\) | Relative: \\(2\^{-16}\\) | \\(\\left\\{-2\^{16},2\^{16}\\right\\}\\) |
| mediump | \\(\\left\\{-2\^{14},2\^{14}\\right\\}\\) | \\(\\left\\{2\^{-14},2\^{14}\\right\\}\\) | Relative: \\(2\^{-10}\\) | \\(\\left\\{-2\^{10},2\^{10}\\right\\}\\) |
| lowp | \\(\\left\\{-2,2\\right\\}\\) | \\(\\left\\{2\^{-8},2\\right\\}\\) | Absolute: \\(2\^{-8}\\) | \\(\\left\\{-2\^{8},2\^{8}\\right\\}\\) |

In addition to array numeric subscript syntax ex: `var[num]`, names of vector
components for vectors of length 2 - 4 are denoted by a single letter. Components
can be swizzled and replicated. ex: `vect.yx`, `vect.yy`

**`vect.xyzw`** - Use when accessing vectors that represent points/normals

**`vect.rgba`** - Use when accessing vectors that represent colors

**`vect.LTRB`** - Use when the vector represents a rectangle (not in GLSL)

In AGSL, 0 and 1 can be used to produce a constant 0 or 1 in that channel.
Ex: `vect.rgb1 == vec4(vect.rgb,1)`

### Structures and arrays

Structures are declared with the same syntax as GLSL, but AGSL only supports
structures at global scope.

    struct type-name {
     members
    } struct-name; // optional variable declaration.

Only 1-dimensional arrays are supported with an explicit array size, using
either C-style or GLSL style syntax:

\<base type\>\[\<array size\>\] variable name - ex: `half[10] x;`

\<base type\> variable name\[\<array size\>\] - ex: `half x[10];`

Arrays cannot be returned from a function, copied, assigned or compared.
Array restrictions propagate out to structures containing arrays. Arrays can
only be indexed using a constant or a loop variable.

## Qualifiers

> [!NOTE]
> **Note:** `attribute`, `varying`, and `invariant` are not supported.

| Type | Description |
|---|---|
| **`const`** | Compile-time constant, or read-only function parameter. |
| **`uniform`** | Value does not change across the primitive being processed. Uniforms are passed from Android using [RuntimeShader](https://developer.android.com/reference/android/graphics/RuntimeShader) methods for `setColorUniform`, `setFloatUniform`, `setIntUniform`, `setInputBuffer`, and `setInputShader`. |
| **`in`** | For passed-in function parameters. This is the default. |
| **`out`** | For passed-out function parameters. Must use the same precision as the function definition. |
| **`inout`** | For parameters that are both passed in and out of a function. Must use the same precision as the function definition. |

## Variable declaration

Declarations must be in an explicit braced scope. The declaration of **`y`** in
the following sample is disallowed:

    if (condition)
        int y = 0;

## Matrix/structure/array basics

### Matrix constructor examples

When a matrix is constructed with a single value, all values along
the diagonal are given that value, while the rest are given zeros. `float2x2(1.0)` would
therefore create a 2x2 identity matrix.

When a matrix is constructed with multiple values, columns are filled first
(column-major order).

Note that, unlike GLSL, constructors that reduce the number of components of a
passed-in vector are not supported, but you can use swizzling to have the same
effect. To construct a `vec3` from a `vec4` in AGSL with the same behavior as
GLSL, specify `vec3 nv = quadVec.xyz`.

### Structure constructor example

    struct light { float intensity; float3 pos; };
    // literal integer constants auto-converted to floating point
    light lightVar = light(3, float3(1, 2, 3.0));

### Matrix components

Access components of a matrix with array subscripting syntax.

    float4x4 m; // represents a matrix
    m[1] = float4(2.0); // sets second column to all 2.0
    m[0][0] = 1.0; // sets upper left element to 1.0
    m[2][3] = 2.0; // sets 4th element of 3rd column to 2.0

### Structure fields

Select structure fields using the period **`.`** operator. Operators include:

| Operator | Description |
|---|---|
| **`.`** | field selector |
| **`==, !=`** | equality |
| **`=`** | assignment |

### Array elements

Array elements are accessed using the array subscript operator `[ ]`. For example:

    diffuseColor += lightIntensity[3] * NdotL;

## Operators

Numbered in order of precedence. The relational and equality
operators \> \< \<= \>= == != evaluate to a Boolean. To compare vectors
component-wise, use functions such as `lessThan()`, `equal()`, etc.

|   | Operator | Description | Associativity |
|---|---|---|---|
| 1 | **`()`** | parenthetical grouping | N/A |
| 2 | **`[] () . ++ --`** | array subscript function call \& constructor structure field or method selector, swizzle postfix increment and decrement | Left to Right |
| 3 | **`++ -- + - !`** | prefix increment and decrement unary | Right to Left |
| 4 | **`* /`** | multiply and divide | Left to Right |
| 5 | **`+ -`** | add and subtract | Left to Right |
| 7 | **`< > <= >=`** | relational | Left to Right |
| 8 | **`== !=`** | equality/inequality | Left to Right |
| 12 | **`&&`** | logical AND | Left to Right |
| 13 | **`^^`** | logical XOR | Left to Right |
| 14 | **`||`** | logical OR | Left to Right |
| 15 | **`?\:`** | selection (one entire operand) | Left to Right |
| 16 | **`= += -= *= /=`** | assignment arithmetic assignment arithmetic assignment | Left to Right |
| 17 | **`,`** | sequence | Left to Right |

### Matrix and vector operations

When applied to scalar values, the arithmetic operators result in a scalar. For
operators other than modulo, if one operand is a scalar and the other is a
vector or matrix, the operation is performed componentwise and results in the
same vector or matrix type. If both operations are vectors of the same size, the
operation is performed componentwise (and returns the same vector type).

| Operation | Description |
|---|---|
| `m = f * m` | Component-wise matrix multiplication by a scalar value |
| `v = f * v` | Component-wise vector multiplication by a scalar value |
| `v = v * v` | Component-wise vector multiplication by a vector value |
| `m = m + m` | Matrix component-wise addition |
| `m = m - m` | Matrix component-wise subtraction |
| `m = m * m` | Linear algebraic multiply |

If one operand is a vector matching the row or column size of our matrix, the
multiplication operator can be used to do algebraic row and column multiplication.

| Operation | Description |
|---|---|
| `m = v * m` | Row vector \* matrix linear algebraic multiply |
| `m = m * v` | Matrix \* column vector linear algebraic multiply |

Use the built-in functions for vector dot product, cross product, and
component-wise multiplication:

| Function | Description |
|---|---|
| `f = dot(v, v)` | Vector dot product |
| `v = cross(v, v)` | Vector cross product |
| `m = matrixCompMult(m, m)` | Component-wise multiply |

## Program control

| Function call | Call by value-return |
|---|---|
| Iteration | `for (<init>;<test>;<next>)` `{ break, continue }` |
| Selection | `if ( ) { }` `if ( ) { } else { }` `switch () { break, case }` - default case last |
| Jump | `break, continue, return` (discard is not allowed) |
| Entry | `half4 main(float2 fragCoord)` |

### For loop limitations

Similar to GLSL ES 1.0, 'for' loops are quite limited; the compiler must be able
to unroll the loop. This means that the initializer, the test condition, and the
`next` statement must use constants so that everything can be computed at compile
time. The `next` statement is further limited to using `++, --, +=, or -=`.

## Built-in functions

**`GT`** (generic type) is **`float`** , **`float2`** , **`float3`** , **`float4`** or
**`half`** , **`half2`** , **`half3`** , **`half4`**.

Most of these functions operate component-wise (the function is applied
per-component). It's noted when that is not the case.

### Angle \& trigonometric functions

Function parameters specified as an angle are assumed to be in units of radians.
In no case will any of these functions result in a divide by zero error. If the
divisor of a ratio is 0, then results will be undefined.

| Function | Description |
|---|---|
| **`GT radians(GT degrees)`** | Converts degrees to radians |
| **`GT degrees(GT radians)`** | Converts radians to degrees |
| **`GT sin(GT angle)`** | Standard sine |
| **`GT cos(GT angle)`** | Standard cosine |
| **`GT tan(GT angle)`** | Standard tangent |
| **`GT asin(GT x)`** | Returns an angle whose sine is x in the range of $ \\left\[-{\\pi\\over 2},{\\pi\\over 2}\\right\] $ |
| **`GT acos(GT x)`** | Returns an angle whose cosine is x in the range of $ \\left\[0,\\pi\\right\] $ |
| **`GT atan(GT y, GT x)`** | Returns an angle whose trigonometric arctangent is $ \\left\[{y\\over x}\\right\] $ in the range of $ \\left\[-\\pi,\\pi\\right\] $ |
| **`GT atan(GT y_over_x)`** | Returns an angle whose trigonometric arctangent is **`y_over_x`** in the range of $ \\left\[-{\\pi\\over 2},{\\pi\\over 2}\\right\] $ |

### Exponential functions

| Function | Description |
|---|---|
| **`GT pow(GT x, GT y)`** | Returns $ x\^y $ |
| **`GT exp(GT x)`** | Returns $ e\^x $ |
| **`GT log(GT x)`** | Returns $ ln(x) $ |
| **`GT exp2(GT x)`** | Returns $ 2\^x $ |
| **`GT log2(GT x)`** | Returns $ log_2(x) $ |
| **`GT sqrt(GT x)`** | Returns $ \\sqrt{x} $ |
| **`GT inversesqrt(GT x)`** | Returns $ 1\\over{\\sqrt{x}} $ |

### Common functions

| Function | Description |
|---|---|
| **`GT abs(GT x)`** | Absolute value |
| **`GT sign(GT x)`** | Returns -1.0, 0.0, or 1.0 based on sign of x |
| **`GT floor(GT x)`** | Nearest integer \<= x |
| **`GT ceil(GT x)`** | Nearest integer \>= x |
| **`GT fract(GT x)`** | Returns the fractional part of x |
| **`GT mod(GT x, GT y)`** | Returns value of x modulo y |
| **`GT mod(GT x, float y)`** | Returns value of x modulo y |
| **`GT min(GT x, GT y)`** | Returns minimum value of x or y |
| **`GT min(GT x, float y)`** | Returns minimum value of x or y |
| **`GT max(GT x, GT y)`** | Returns maximum value of x or y |
| **`GT max(GT x, float y)`** | Returns maximum value of x or y |
| **`GT clamp(GT x, GT`** **`minVal, GT maxVal)`** | Returns x clamped between minVal and maxVal. |
| **`GT clamp(GT x, float`** **`minVal, float maxVal)`** | Returns x clamped between minVal and maxVal |
| **`GT saturate(GT x)`** | Returns x clamped between 0.0 and 1.0 |
| **`GT mix(GT x, GT y,`** **`GT a)`** | Returns linear blend of x and y |
| **`GT mix(GT x, GT y,`** **`float a)`** | Returns linear blend of x and y |
| **`GT step(GT edge, GT x)`** | Returns 0.0 if x \< edge, else 1.0 |
| **`GT step(float edge,`** **`GT x)`** | Returns 0.0 if x \< edge, else 1.0 |
| **`GT smoothstep(GT edge0,`** **`GT edge1, GT x)`** | Performs Hermite interpolation between 0 and 1 when edge0 \< x \< edge1 |
| **`GT smoothstep(float`** **`edge0, float edge1,`** **`GT x)`** | Performs Hermite interpolation between 0 and 1 when edge0 \< x \< edge1 |

### Geometric functions

These functions operate on vectors as vectors, not component-wise. GT is float/half vectors in sizes 2-4.

| Function | Description |
|---|---|
| **`float/half length`** **`(GT x)`** | Returns length of vector |
| **`float/half distance(GT`** **`p0, GT p1)`** | Returns distance between points |
| **`float/half dot(GT x,`** **`GT y)`** | Returns dot product |
| **`float3/half3`** **`cross(float3/half3 x,`** **`float3/half3 y)`** | Returns cross product |
| **`GT normalize(GT x)`** | Normalize vector to length 1 |
| **`GT faceforward(GT N,`** **`GT I, GT Nref)`** | Returns N if dot(Nref, I) \< 0, else -N. |
| **`GT reflect(GT I, GT N)`** | Reflection direction I - 2 \* dot(N,I) \* N. |
| **`GT refract(GT I, GT N,`** **`float/half eta)`** | Returns [refraction vector](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/refract.xhtml) |

### Matrix functions

Type mat is any square matrix type.

| Function | Description |
|---|---|
| **`mat matrixCompMult(mat`** **`x, mat y)`** | Multiply x by y component-wise |
| **`mat inverse(mat m)`** | Returns the inverse of m |

### Vector relational functions

Compare x and y component-wise. Sizes of input and return vectors for a particular call must match. T is the union of integer and floating point vector types. BV is a boolean vector that matches the size of the input vectors.

| Function | Description |
|---|---|
| **`BV lessThan(T x, T y)`** | x \< y |
| **`BV lessThanEqual(T x,`** **`T y)`** | x \<= y |
| **`BV greaterThan(T x,`** **`T y)`** | x \> y |
| **`BV greaterThanEqual(T`** **`x, T y)`** | x \>= y |
| **`BV equal(T x, T y)`** | x == y |
| **`BV equal(BV x, BV y)`** | x == y |
| **`BV notEqual(T x, T y)`** | x != y |
| **`BV notEqual(BV x,`** **`BV y)`** | x != y |
| **`bool any(BV x)`** | `true` if any component of x is `true` |
| **`bool all(BV x)`** | `true` if all components of x are `true`. |
| **`BV not(BV x)`** | logical complement of x |

### Color functions

| Function | Description |
|---|---|
| **`vec4 unpremul(vec4`** **`color)`** | Converts color value to non-premultiplied alpha |
| **`half3 toLinearSrgb(half3`** **`color)`** | Color space transformation to linear SRGB |
| **`half3 fromLinearSrgb(half3`** **`color)`** | Color space transformation |

## Shader sampling (evaluation)

Sampler types aren't supported, but you can evaluate other shaders. If you need
to sample a texture, you can create a
[BitmapShader](https://developer.android.com/reference/android/graphics/BitmapShader) object, and add it as a
uniform. You can do this for any shader, which means you can directly evaluate
any Android Shader without turning it into a
[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap) first, including other
[RuntimeShader](https://developer.android.com/reference/android/graphics/RuntimeShader) objects. This allows
for a huge amount of flexibility, but complex shaders can be expensive to
evaluate, particularly in a loop.

    uniform shader image;

    image.eval(coord).a   // The alpha channel from the evaluated image shader

## Raw buffer sampling

Although most images contain colors that should be color-managed, some images
contain data that isn't actually colors, including images storing normals,
material properties (e.g., roughness), heightmaps, or any other purely
mathematical data that happens to be stored in an image. When using these kinds
of images in AGSL, you can use a BitmapShader as a generic raw buffer using
[RuntimeShader#setInputBuffer](https://developer.android.com/reference/android/graphics/RuntimeShader#setInputBuffer(java.lang.String,%20android.graphics.BitmapShader)).
This will avoid color space transformations and filtering.