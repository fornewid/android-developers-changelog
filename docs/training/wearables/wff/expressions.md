---
title: https://developer.android.com/training/wearables/wff/expressions
url: https://developer.android.com/training/wearables/wff/expressions
source: md.txt
---

WFF uses an expression language to enable:

- Transforming the appearance using `Transform` or `Gyro`
- Conditional behavior through `Condition` statements
- String formatting in `Template` elements

The expression language is a scripting language which contains your
typical operators and a range of functions that can be used.

Expressions can use [data sources](https://developer.android.com/training/wearables/wff/common/attributes/source-type)---represented using square brackets---to
let you react to external inputs such as the current date and time, health
and fitness metrics, or even the weather.

When using expressions, the primary difference between `Transform`, `Template`,
and `Condition` usage is that `Transform` and `Template` require the expression
to result in a *value* (for example, the new position of the enclosing element)
while `Condition` requires the expression to result in a *boolean*.

When used in a `Condition` element, specify the expression as a text
element. Wrap the expression in a `CDATA` element to avoid the need to
use entity references, such as `&quot;` and `&amp;`.

<br />

```xml
<![CDATA[[DAY_OF_WEEK] == 6 || [DAY_OF_WEEK] == 7]]>
```

<br />

This evaluates to a boolean and determines whether it is a weekend or not,
using the `DAY_OF_WEEK` data source.

[Functions](https://developer.android.com/training/wearables/wff/common/attributes/arithmetic-expression#functions) are also supported---for example, an expression for rotating a
value up to 5 degrees in either direction---based on the `x-value` of the Wear OS
device's accelerometer:

<br />

```xml
(5.0/90.0)*clamp([ACCELEROMETER_ANGLE_X],0,90) +
(-5.0/90.0)*clamp([ACCELEROMETER_ANGLE_X],-90,0)
```

<br />

The `clamp()` function constrains a value within two bounds.

### Expression re-evaluation

The frequency with which expressions are re-evaluated depends on the data
sources used in them. For example, the
`[DAY_OF_WEEK] == 6 || [DAY_OF_WEEK] == 7`
expression only re-evaluates when a new day starts. However, an expression
that uses the `[SECOND]` data source re-evaluates every second.

Re-evaluation may result in scene recalculations and re-rendering, based on the
change in the result of the expression. Therefore it is important to always use
data sources that re-evaluate as infrequently as possible. For example, to
determine whether it is afternoon:

<br />

```xml
<!-- BAD: Re-evaluates every second -->
[SECONDS_IN_DAY] > 43200
```

<br />

<br />

```xml
<!-- Good: Minimizes re-evaluation (1 = PM, 0 = AM) -->
[AMPM_STATE] == 1
```

<br />

### Configuration values in expressions

In addition to functions and data sources, configuration values can be used. For
example, if in the [UserConfigurations](https://developer.android.com/training/wearables/wff/user-configuration/user-configurations) a `BooleanConfiguration` named
`showBackgroundInAfternoon` has been defined, this can be used in an expression:

<br />

```xml
<![CDATA[[CONFIGURATION.showBackgroundInAfternoon] == "TRUE" && [AMPM_STATE] == 1]]>
```

<br />