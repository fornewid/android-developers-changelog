---
title: https://developer.android.com/training/wearables/wff/personalization/user-configurations
url: https://developer.android.com/training/wearables/wff/personalization/user-configurations
source: md.txt
---

`UserConfigurations` let you create options that the user can choose
between. You can adjust the appearance of watch face
elements based on the chosen values.

The user configuration options can be:

- `BooleanConfiguration`: typically used for where the user might have the option to show an element or not, or pick between two styles
- `ListConfiguration`: provides the user with a range of options. For example, if the watch face had four different background images to choose from
- `ColorConfiguration`: defines color themes, from which the user can select their preferred theme.

### Boolean options

Boolean options are perhaps the simplest of the user configurations. They can be
defined as follows:

<br />

```xml
<!-- Under WatchFace element -->
<UserConfigurations>
    <!-- show_date and show_date_label defined in res/values/strings.xml -->
    <BooleanConfiguration id="show_date"
        displayName="show_date_label"
        screenReaderText="show_date_label"
        defaultValue="TRUE"
        />
</UserConfigurations>
```

<br />

Boolean options can then be used in a two ways:

1. Using the `BooleanConfiguration` structure within the watch face `Scene`:

   <br />

   ```xml
   <!-- Within the main Scene of the watch face -->
   <BooleanConfiguration id="show_date">
       <BooleanOption id="TRUE">
           <!-- ...Content when date required -->
       </BooleanOption>
       <BooleanOption id="FALSE">
           <!-- ...Content when date not required -->
       </BooleanOption>
   </BooleanConfiguration>
   ```

   <br />

   Note that configuration options cannot be nested in their use.
2. Alternatively, the configuration option can be used in
   [expressions](https://developer.android.com/training/wearables/wff/expressions):

   <br />

   ```xml
       <Expressions>
           <Expression name="my_expression">
               <!-- Use show_date as part of a more complex evaluation -->
               <![CDATA[[CONFIGURATION.show_date] == "TRUE" && [HOUR_0_23] < 15]]
           </Expression>
       </Expressions>
       <Compare expression="my_expression">
           <!-- Content goes here -->
       </Compare>
   </Condition>https://github.com/android/snippets/blob/bf60b1e59478ef481b1a2936dd14e2c41b9a26e2/watchface/src/main/res/raw/watchface_boolean_configuration.xml#L59-L75
   ```

   <br />

### List options

List options work in a very similar manner to boolean options. For example, to
provide a list of background images for the user to choose from:

<br />

```xml
<!-- Under WatchFace element -->
<UserConfigurations>
    <ListConfiguration id="background_image" displayName="background_image_label"
        icon="background_option_icon"
        screenReaderText="background_image_label" defaultValue="0">
        <ListOption id="0" displayName="background0_image_label"
            screenReaderText="background0_image_label" icon="background0_icon" />
        <ListOption id="1" displayName="background1_image_label"
            screenReaderText="background1_image_label" icon="background1_icon" />
        ...
    </ListConfiguration>
</UserConfigurations>
```

<br />

Similar to boolean options, there are again two ways to use this:

1. Using the `ListConfiguration` element in `Scene`:

   <br />

   ```xml
   <!-- Within the main Scene of the watch face -->
   <ListConfiguration id="background_image">
       <ListOption id="0">
           <!-- ...Content for option 0 -->
       </ListOption>
       <ListOption id="1">
           <!-- ...Content for option 1 -->
       </ListOption>
   </ListConfiguration>
   ```

   <br />

2. Alternatively, the configuration option can be used in more complex
   expressions:

   <br />

   ```xml
       <Expressions>
           <Expression name="background_zero_and_something_else">
               <!-- Use as part of a more complex evaluation -->
               <![CDATA[[CONFIGURATION.background_image] == "0" && [HOUR_0_23] < 15]]
           </Expression>
       </Expressions>
       <Compare expression="background_zero_and_something_else">
           <!-- Content goes here -->
       </Compare>
   </Condition>https://github.com/android/snippets/blob/bf60b1e59478ef481b1a2936dd14e2c41b9a26e2/watchface/src/main/res/raw/watchface_list_configuration.xml#L58-L74
   ```

   <br />

### Color themes

Watch Face Format lets you define color themes through `ColorConfiguration`.
Users can select the theme of their choice from the watch face editor, and the
colors from this theme can appear throughout your watch face definition.

For example, to define a theme with two entries and three colors in the theme,
define a `ColorConfiguration` as follows:

<br />

```xml
<!-- Under WatchFace element -->
<UserConfigurations>
    <ColorConfiguration id="myThemeColor" displayName="theme_label" defaultValue="0">
        <ColorOption id="0" displayName="relaxed_label" colors="#3083dc #f8ffe5 #7dde92" />
        <ColorOption id="1" displayName="urban_label" colors="#f4b393 #fc60a8 #7a28cb" />
    </ColorConfiguration>
</UserConfigurations>
```

<br />

These can then be used as data sources instead of hexadecimal color values. Note
how the index value is specified to select the first, second, or third element
of the theme:

<br />

```xml
<AnalogClock x="0" y="0" width="450" height="450">
    <HourHand resource="hour" x="220" y="55" width="20" height="190"
        pivotX="0.5" pivotY="0.9210"
        tintColor="[CONFIGURATION.myThemeColor.0]"/>
    <MinuteHand resource="minute" x="222" y="30" width="16" height="220"
        pivotX="0.5" pivotY="0.9"
        tintColor="[CONFIGURATION.myThemeColor.1]"/>
    <SecondHand resource="second" x="226" y="20" width="8" height="245"
        pivotX="0.5" pivotY="0.8571"
        tintColor="[CONFIGURATION.myThemeColor.2]"/>
</AnalogClock>
```

<br />

In the specific case where each `ColorOption` only has one color defined, it is
also possible to reference it as `CONFIGURATION.myThemeColor`, without the
index. The user can then select the theme entry of their choice in the watch
face editor.

## Flavors

**Note**: Flavors are supported on version 2 and higher of Watch Face Format.

`UserConfigurations` provide the user with a lot of flexibility, but as you
increase the number of configuration elements you define, the number of
combinations can grow overwhelmingly.

`Flavors` lets you define *presets* for the `UserConfigurations` that you
think are worth highlighting.

The user can then select from these preset flavors within the companion app,
or continue to choose each configuration value individually.

For example, consider a watch face where you define three settings:

1. A color theme configuration, allowing the user to select which color theme to apply. You've defined two themes, one colorful and one monochrome.
2. A list of backgrounds. You've defined two choices the user can select from.
3. A choice of whether to show the user's heart rate on the watch face.

Furthermore, you have a `ComplicationSlot` on the watch face.

You decide that there are two `Flavors` that you want to highlight to the user.
There are many more possible combinations of all these settings, but these are
the ones you think work best:

1. **A sporty flavor** : This will consist of:
   1. The bright color theme, to energize you and get you active (ID: 0)
   2. The first background image (ID: 0)
   3. Heart rate showing on the watch face for reference
   4. The complication slot showing step count
2. **A sophisticated flavor** : This will consist of:
   1. The monochrome color theme, to match any outfit (ID: 1)
   2. The second background image (ID: 1)
   3. No heart rate showing on the watch face
   4. The complication slot not enabled

Flavors require enabling in `watch_face_info.xml`, so the `FlavorsSupported`
element in the `watch_face_info.xml` file should be set with `value="true"`.

Each Flavor is defined within `UserConfigurations` as follows:

<br />

```xml
<!-- Under UserConfigurations -->
<Flavors defaultValue="sporty_flavor">
    <Flavor id="sporty_flavor"
        displayName="flavor_sporty_label" screenReaderText="flavor_sporty_label">
        <Configuration id="theme_color" optionId="0"/>
        <Configuration id="background_image" optionId="0"/>
        <Configuration id="show_hr" optionId="TRUE"/>
        <ComplicationSlot slotId="0">
            <DefaultProviderPolicy
                defaultSystemProvider="STEP_COUNT"
                defaultSystemProviderType="SHORT_TEXT"/>
        </ComplicationSlot>
    </Flavor>
    <Flavor id="sophisticated_flavor"
        displayName="flavor_sophisticated_label" screenReaderText="flavor_sophisticated_label">
        <Configuration id="theme_color" optionId="1"/>
        <Configuration id="background_image" optionId="1"/>
        <Configuration id="show_hr" optionId="FALSE"/>
        <ComplicationSlot slotId="0">
            <!--
              Type here is set to empty to demonstrate how to hide a complication
              slot in Flavors.
            -->
            <DefaultProviderPolicy
                defaultSystemProvider="SUNRISE_SUNSET"
                defaultSystemProviderType="EMPTY"/>
        </ComplicationSlot>
    </Flavor>
</Flavors>
```

<br />