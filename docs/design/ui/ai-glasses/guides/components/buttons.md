---
title: Buttons  |  AI Glasses  |  Android Developers
url: https://developer.android.com/design/ui/ai-glasses/guides/components/buttons
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [AI Glasses](https://developer.android.com/design/ui/ai-glasses)
* [Guides](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles)

# Buttons Stay organized with collections Save and categorize content based on your preferences.





Buttons are the primary visual indicator for a user's actions.

![Design elements should be anchored to the bottom of the
frame.](/static/images/design/ui/glasses/guides/glasses_components_buttons.png)

### Principles

**Action-Oriented**: Buttons should clearly communicate that they trigger an
action.

**Clear Feedback**: The button's appearance must change distinctly across
different interaction states (hover, press, focus) to provide immediate
feedback.

**Consistent**: All buttons should share a core visual language to be instantly
recognizable.

**Flexible**: The button component should accommodate common variations, such as
including icons and different sizes, without sacrificing consistency.

## Usage & Placement

A button should be placed closely to its relevant content. They can be placed
alone or with other components, like cards and lists.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_use_do.png)

check\_circle

### Do

Use progressive disclosure to reveal less relevant actions.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_use_dont.png)

cancel

### Don't

Overwhelm the user's view with too many buttons. Use a button group instead.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_action_do.png)

check\_circle

### Do

Use buttons to prompt an action. Or use a title chip for a static element.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_action_dont.png)

cancel

### Don't

Use a button as a static decorative element.

### Icon buttons

Icon buttons are available to reduce content density. Use icon buttons when the
icon clearly illustrates an action, otherwise include a button label.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_icon_do.png)

check\_circle

### Do

Use an icon button for common highly recognizable actions.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_icon_dont.png)

cancel

### Don't

Use an icon button for very obscure actions.

### Toggable

For actions with boolean states, like favorite, a toggle variant is available
for each button type. Swapping icons in between toggle states makes the
interaction glanceable and responsive.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_toggle_do.png)

check\_circle

### Do

Use a toggle button if there are boolean options for an action. Like start/stop.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons_toggle_dont.png)

cancel

### Don't

Use a toggle button for non binary actions.

## Anatomy

Buttons are composed of a label and optional icon leading or trailing icon.

![Default buttons
](/static/images/design/ui/glasses/guides/glasses_components_buttons_anatomy.png)

Icon buttons are composed of only a recognizable icon.

Both have a togglable variant.

### Default

![Default buttons
](/static/images/design/ui/glasses/guides/glasses_components_buttons_anatomy_default.png)
**1.** Rest  
**2.** Focused  
**3.** Pressed  
**4.** Disabled  
**5.** Disabled & focused

### Large

![Large button style
](/static/images/design/ui/glasses/guides/glasses_components_buttons_large.png)
**1.** Rest  
**2.** Focused  
**3.** Pressed  
**4.** Disabled  
**5.** Disabled & focused

### Icon

![Icon buttons
](/static/images/design/ui/glasses/guides/glasses_components_buttons_anatomy_icon.png)
**1.** Rest  
**2.** Focused  
**3.** Pressed  
**4.** Disabled  
**5.** Disabled & focused

### Icon

![Icon buttons
](/static/images/design/ui/glasses/guides/glasses_components_buttons_anatomy_toggle.png)
**1.** Rest  
**2.** Focused  
**3.** Pressed  
**4.** Disabled  
**5.** Disabled & focused

## Customization

Buttons contain a default and large style. Large size can help emphasize
importance.

Icons can be used to give greater emphasis, clarification, and recognition to
the button in a trailing or leading position.

### Default

| Properties | Customization | Defaults |
| --- | --- | --- |
| Shape | Yes | Large, Circle |
| Padding | Yes | 16 dp, 8 dp |
| Border | Yes | Default, 2 dp, #606460 |
| Text | Yes | Body Small |
| Leading icon | Yes | 32 dp |
| Trailing icon | Yes | 32 dp |
| Size | Yes | 48 dp min height |
| Depth | Yes | 0 |
| Gap | Yes | Between label and icon: Extra small |

### Large

| Properties | Customization | Defaults |
| --- | --- | --- |
| Shape | Yes | Large, Circle |
| Padding | Yes | 16 dp, 16 dp |
| Border | Yes | 2 dp, #606460 |
| Text | Yes | Body Small |
| Leading icon | Yes | 32 dp |
| Trailing icon | Yes | 32 dp |
| Size | Yes | 72 dp min height |
| Depth | Yes | 0 |
| Gap | Yes | Between label and icon: Extra small |

### Icon

| Properties | Customization | Defaults |
| --- | --- | --- |
| Shape | Yes | Large, Circle |
| Padding | Yes | Small, Small |
| Border | Yes | Default |
| Icon | Yes | Default = 32 dp, On Surface |
| Size | Yes | 48 dp min height |
| Depth | Yes | 0 |

### Toggable

| Properties | Customization | Defaults |
| --- | --- | --- |
| Selected | Yes | Boolean |
| Default corners | Yes | 16 dp, 8 dp |
| Selected corners | Yes | Default focus |
| Selected Surface color | Yes | Outline |
| All other properties | Yes | Same as buttons |

### Toggable icon

| Properties | Customization | Defaults |
| --- | --- | --- |
| Selected | Yes | Boolean |
| Default corners | Yes | 100 dp |
| Selected corners | Yes | 20 dp |
| Selected Surface color | Yes | Outline |
| All other properties | Yes | Same as buttons |

[Previous

arrow\_back

Icons](/design/ui/ai-glasses/guides/styles/icons)

[Next

Button groups

arrow\_forward](/design/ui/ai-glasses/guides/components/button-group)