---
title: https://developer.android.com/training/wearables/wff/transform/content
url: https://developer.android.com/training/wearables/wff/transform/content
source: md.txt
---

While `Transform` lets you change the appearance of elements or groups of
elements, there might be occasions where you want to switch between a list of
behaviors based on some condition. This is analogous to a `switch` statement
or `if...else` statement in other languages.

For example, you might want to show a different background for early morning,
morning, lunch, afternoon, evening, and night.

`Condition` statements in Watch Face Format let you include different parts
of your watch face scene depending on the evaluation of [expressions](https://developer.android.com/training/wearables/wff/expressions), for
example:

<br />

```xml
<Condition>
    <Expressions>
        <Expression name="is_early_morning">
            <![CDATA[[HOUR_0_23] >= 6 && [HOUR_0_23] < 8]]
        </Expression>
        <Expression name="is_morning">
            <![CDATA[[HOUR_0_23] < 12]]
        </Expression>
        <!-- Further expressions -->
    </Expressions>
    <Compare expression="is_early_morning">
        <!-- Early morning content here -->
    </Compare>
    <Compare expression="is_morning">
        <!-- Morning content here -->
    </Compare>
    <!-- Further Compare elements -->
    <!-- The "else" case -->
    <Default>
        <!-- content -->
    </Default>
</Condition>https://github.com/android/snippets/blob/bbf4e1ff2570641546d50270b121493ef1965774/watchface/src/main/res/raw/watchface_dynamic_content.xml#L20-L55
```

<br />

A few things to note about conditions:

1. The first `Compare` element where the `expression` is `true` is used, and others are ignored.
2. Owing to the XML format, it can often be easiest to wrap the expression definition in a `CDATA` element as shown here, as this avoids the need for XML escaping using entity elements such as `&gt;` and `&amp;`.
3. `Condition` structures can be nested.