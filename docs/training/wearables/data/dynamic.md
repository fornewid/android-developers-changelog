---
title: https://developer.android.com/training/wearables/data/dynamic
url: https://developer.android.com/training/wearables/data/dynamic
source: md.txt
---

Wear OS supports dynamic updates to information that appears in your [tiles](https://developer.android.com/training/wearables/tiles)
and [complications](https://developer.android.com/training/wearables/tiles/complications).

Using dynamic expressions, you can bind data that appears on a surface of your
app--such as a tile or complication--to a particular data source. An example of
such a data source is heart rate data that the platform can read. After you've
established this binding, the system updates the data in your tiles and
complications automatically.

## Create dynamic data bindings

To create a dynamic data binding, define a variable that uses a
[dynamic data type](https://developer.android.com/training/wearables/data/dynamic#data-types). Associate this variable with the data stream that you
want to use.

For example, you can fetch values related to the system clock and health
information, as shown in the following code snippet.

> [!NOTE]
> **Note:** To access the data in [`PlatformHealthSources`](https://developer.android.com/reference/androidx/wear/protolayout/expression/PlatformHealthSources), you must [request a
> runtime permission](https://developer.android.com/training/permissions/requesting) in your app.

<br />

```kotlin
val systemTime = DynamicInstant.platformTimeWithSecondsPrecision()
val steps: DynamicInt32 = PlatformHealthSources.dailySteps()
```

<br />

You can also create dynamic values from constant expressions and perform
arithmetic operations on any dynamic value, as shown in the following snippet:

<br />

```kotlin
val dynamicAdditionResult = DynamicInt32.constant(1).plus(2)
```

<br />

### List of possible dynamic data types

Wear OS supports the following dynamic data types:

- [`DynamicBool`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicBool)
- [`DynamicColor`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicColor)
- [`DynamicDuration`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicDuration)
- [`DynamicFloat`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicFloat)
- [`DynamicInstant`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicInstant)
- [`DynamicInt32`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicInt32)
- [`DynamicString`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicString)

In addition, you can transform the data type using built-in capabilities, such
as the following:

- `DynamicInt32` supports conversion to a `DynamicString` using [`format()`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicBuilders.DynamicInt32#format()).
- `DynamicDuration` lets you extract specific parts, such as the seconds part of a duration, as `DynamicInt32` objects.

## Use a limited number of dynamic expressions on each screen

The system has a limit on the number of dynamic expressions that it can process
simultaneously on a particular screen. The system converts any additional
dynamic expressions to static values.

Wear OS considers constant expressions to be dynamic expressions, too. For
example, the following code snippet contains 4 dynamic expressions:

1. The `plus()` operation.
2. The `animate()` operation.
3. The `constant(1)` expression.
4. The `constant(2)` expression, which is implied by the value `2` in the `plus()` dynamic expression.

<br />

```kotlin
val animatedAdditionResult = DynamicInt32.constant(1).plus(2).animate()
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Migrate to ProtoLayout namespaces](https://developer.android.com/training/wearables/tiles/migrate-to-protolayout)
- [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)
- [AGSL Quick Reference](https://developer.android.com/develop/ui/views/graphics/agsl/agsl-quick-reference)