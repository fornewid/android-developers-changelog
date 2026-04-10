---
title: https://developer.android.com/design/ui/ai-glasses/guides/components/buttons
url: https://developer.android.com/design/ui/ai-glasses/guides/components/buttons
source: md.txt
---

Buttons are the primary visual indicator for a user's actions.

![Design elements should be anchored to the bottom of the
frame.](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons.png)

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

## Usage \& Placement

A button should be placed closely to its relevant content. They can be placed
alone or with other components, like cards and lists.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons_use_do.png)

### Do

Use progressive disclosure to reveal less relevant actions. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons_use_dont.png)

### Don't

Overwhelm the user's view with too many buttons. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons_action_do.png)

### Do

Use buttons to prompt an action. Or use a title chip for a static element. ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons_action_dont.png)

### Don't

use a button as a static decorative element.

## Anatomy

### Default


![Default buttons](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons_default.png)
**1.** Enabled: Default state.
**2.** Hover
**3.** Tap

### Large

![Large button style](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons_large.png)
**1.** Enabled: Default state.
**2.** Hover
**3.** Tap

## Customization

Buttons contain a default and large variation, along with default, focused, and
pressed states for each. Icons can be used to give greater emphasis,
clarification, and recognition to the button. Button size can help emphasize
importance.

### Default


| Properties | Customization | Defaults |
|---|---|---|
| Shape | Yes | Large, Circle |
| Padding | Yes | 16 dp, 8 dp |
| Border | Yes | 2 dp, #606460 |
| Text | Yes | Body Small |
| Leading icon | Yes | 40 dp |
| Trailing icon | Yes | 40 dp |
| Size | Yes | 56 dp min height |
| Depth | Yes | 0 |

<br />

### Large


| Properties | Customization | Defaults |
|---|---|---|
| Shape | Yes | Large, Circle |
| Padding | Yes | 20 dp, 8 dp |
| Border | Yes | 2 dp, #606460 |
| Text | Yes | Body Small |
| Leading icon | Yes | 56 dp |
| Trailing icon | Yes | 56 dp |
| Size | Yes | 72 dp min height |
| Depth | Yes | 0 |
| Surface | No |   |

<br />