---
title: https://developer.android.com/training/wearables/wff/text
url: https://developer.android.com/training/wearables/wff/text
source: md.txt
---

For digital clocks, you should aim to use `DigitalClock` where possible. For all
other text or clocks that cannot be represented using `DigitalClock`,
`PartText` is the container for text-based rendering.

Depending on whether you want to show circular or regular text, the `PartText`
should contain *either* a `Text` or a `TextCircular` element.

### Work with fonts and bitmap fonts

Using custom fonts allows your watch face to stand out with its own style.

There are two ways to use custom fonts, both within `TimeText` and `PartText`
containers.

1. Specify a custom font `family` in the `Font` element. [A range of common
   formats](https://developer.android.com/training/wearables/wff/group/part/text/font?version=1) are
   supported, which must be placed in `res/font`

   For example, using the Pacifico font from Google Fonts, and placing the
   asset as res/font/pacifico.ttf:

   <br />

   ```xml
   <PartText x="0" y="50" width="450" height="250">
       <Text align="CENTER">
           <Font family="pacifico" size="96">Hello!</Font>
       </Text>
   </PartText>
   ```

   <br />

2. Alternatively, define a `BitmapFont` supplying bitmap images in
   `res/drawable`:

   <br />

   ```xml
   <BitmapFonts>
       <BitmapFont name="myhandwriting">
           <Character name="1" resource="digit1" width="50" height="100" />
           <Character name="2" resource="digit2" width="50" height="100" />
           <Character name="3" resource="digit3" width="50" height="100" />
           <Character name="4" resource="digit4" width="50" height="100" />
           <!-- ... -->
           <!-- Treat "12" specially, instead of a 1 followed by a 2-->
           <Word name="12" resource="digit12" width="80" height="100" />
       </BitmapFont>
   </BitmapFonts>
   ```

   <br />

Note how sequences of characters can be given a special treatment. For example,
if "12" was to be represented with a joined 1 and 2, this could be achieved
using a `Word` element.

To use the defined font:

<br />

```xml
<DigitalClock x="125" y="120" width="200" height="50">
    <TimeText x="0" y="0" width="200" height="50" format="hh:mm">
        <BitmapFont family="myhandwriting" size="48" color="#FF00FF"/>
    </TimeText>
</DigitalClock>
```

<br />

### Text effects

Watch Face Format provides several text effects which can be applied, such as
[`OutGlow`](https://developer.android.com/training/wearables/wff/group/part/text/decoration/out-glow) and [`Shadow`](https://developer.android.com/training/wearables/wff/group/part/text/decoration/shadow). To use these, apply them as subelements of the
`Font` element:

<br />

```xml
<Font family="pacifico" size="96" color="#e2a0ff">
    <OutGlow color="#e8ffb7" radius="30">Hello!</OutGlow>
</Font>
```

<br />

### Work with templates

Instead of static text, you may need to construct your text from data sources or
expressions.

The `Template` element lets you do this:

<br />

```xml
<Font family="pacifico" size="60" weight="BOLD" color="#ffffff">
    <Template>Day: %s<Parameter expression="[DAY_OF_WEEK_S]" /></Template>
</Font>
```

<br />

### Work with resources

If your static text is instead defined in a resource, such as in
`res/values/strings.xml`, then it can be referenced as follows:

<br />

```xml
<!-- greeting defined in res/values/strings.xml -->
<Font family="pacifico" size="60" weight="BOLD" color="#ffffff">greeting</Font>
```

<br />

This also lets you localize your watch face using different [resource
qualifiers](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources).

### Handle spacing

Working with text spacing in XML can be challenging. Extra spacing around text
can cause formatting problems, such as incorrect centering, or prevent your app
from finding Android string resources.

To avoid these situations, wrap your `Font` contents in a `CDATA` element:

<br />

```xml
<Font family="pacifico" size="60" weight="BOLD" color="#ffffff">
    <![CDATA[Hello]]>
</Font>
```

<br />

### Multiline text

To create multiline text, use the `maxLines` attribute on `Text`:

<br />

```xml
<Text align="CENTER" maxLines="2">
    <Font family="pacifico" size="60" weight="BOLD" color="#ffffff">
        <![CDATA[Hello Wear OS world]]>
    </Font>
</Text>
```

<br />