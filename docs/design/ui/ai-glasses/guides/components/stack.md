---
title: Stack  |  AI Glasses  |  Android Developers
url: https://developer.android.com/design/ui/ai-glasses/guides/components/stack
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [AI Glasses](https://developer.android.com/design/ui/ai-glasses)
* [Guides](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles)

# Stack Stay organized with collections Save and categorize content based on your preferences.



A stack is a collapsed list that only displays one piece of content at a time,
in a stacked visual, such as a notification or card.

![Design elements should be anchored to the bottom of the
frame.](/static/images/design/ui/glasses/guides/glasses_components_stacks.png)

### Principles

Stack are a container component, so they share design principles with cards and
lists:

**Containment**: Stacks group related information and actions into a single,
digestible unit.

**Focused & Clarity**: They present content in a clear, focused manner.

**Versatility**: Stacks can display cards and notifications.

**Consistent Presentation**: Stacks follow a consistent visual structure.

## Usage & Placement

Stacks are a way to showcase to users that there are multiple elements collapsed
in a list while minimizing the visual elements within view. There are two
different variants of stacks:

**Card stacks**

**Notification stacks**

Stacks are a container component, both versions don't act or look differently.

Both should look and act nearly identical. The stack is a container for
these controls with built-in logic for pagination.

Users navigate by swiping or dragging along the touchpad forward and backward.
Scrolling the stack will move through only one item at a time.

![Design elements should be anchored to the bottom of the
frame.](/static/images/design/ui/glasses/guides/glasses_components_stack_use_depth.png)
**Use depth to indicate focus**

Lower stack items use a depth of 0 while the top most item uses a depth of +2.

![Anchor design elements to bottom of fram
e](/static/images/design/ui/glasses/guides/glasses_components_stack_use_traversal.png)

**Stacks can traversed one item at a time**

Upon touch input, stacks are able to present one item at a time by moving
vertically.

Upon touch input, stacks are able to become lists to show more than one element
at a time.  The list should use default containers and focus states.

## Anatomy

A stack is always collapsed as a pagination component. The top item is always
the primary focus, showing the stronger border depth, unless there is a nested
enabled button.

Bumpers help reinforce the end and beginning of a stack. A spring animation that
snaps the list back into place upon release.

![Design elements should be anchored to the bottom of the
frame.](/static/images/design/ui/glasses/guides/glasses_components_stack_anatomy.png)

## Customization

Stacks have built-in scrim, paging, and animations that can't be customized.
Rather the content within the stacks is customized.

[Previous

arrow\_back

Lists](/design/ui/ai-glasses/guides/components/lists)