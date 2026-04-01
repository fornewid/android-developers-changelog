---
title: https://developer.android.com/design/ui/mobile/guides/components/material-overview
url: https://developer.android.com/design/ui/mobile/guides/components/material-overview
source: md.txt
---

# Material Components

![Banner for Material Components](https://developer.android.com/static/images/design/ui/mobile/material-components-hero.png)

A design system is a collection of reusable design decisions expressed as guidance, components, and patterns. The system can be broken down into smallest design primitives: things like color, type, or shape which build into larger complex component pieces. For example, an icon and text label make up a button component, while multiple buttons and a surface make up a card. Design systems also come with a set of guidance composed of these existing design decisions around the components and patterns.

Material Design is an open-source design system developed by Google to help you build beautiful user-focused products. Material 3 is the latest iteration of Material Design.

## Material Design Components

Material Design provides an array of code-backed[components](https://m3.material.io/components)that are interactive building blocks for creating a user interface. These components can be organized into five categories based on their purpose: action, containment, navigation, selection, and text input.

### Action components

Action components help people achieve an aim.

Material has multiple types of[buttons](https://m3.material.io/components/buttons/overview)to help define priority of actions and interaction in different contexts. From[FABs](https://m3.material.io/components/floating-action-button/overview)or[extended FABs](https://m3.material.io/components/extended-fab/overview)for primary actions to supporting[icon buttons](https://m3.material.io/components/icon-buttons/overview)to selecting options with[segmented buttons](https://m3.material.io/components/segmented-buttons/overview).
![](https://developer.android.com/static/images/design/ui/mobile/material-components-action-components.png)**Figure 1:**Action Components

### Communication components

Communication components provide helpful information, by alerting users with[badges](https://m3.material.io/components/badges), informing of status through[progress indicators](https://m3.material.io/components/progress-indicators), and providing brief process messages with[snackbars](https://m3.material.io/components/snackbar).
![](https://developer.android.com/static/images/design/ui/mobile/material-components-communication.png)**Figure 2:**Communication

### Containment components

Containment components hold information and actions -- including other components like buttons, menus, or chips. Most Material components use explicit containment, grouping together related content and actions with visual objects:[cards](https://m3.material.io/components/cards),[dialogs](https://m3.material.io/components/dialogs),[bottom sheets](https://m3.material.io/components/bottom-sheets),[side sheets](https://m3.material.io/components/side-sheets),[carousels](https://m3.material.io/components/carousel), and[tooltips](https://m3.material.io/components/tooltips).[Lists](https://m3.material.io/components/lists)can be provided with implicit containment or explicit by showing visible[dividers](https://m3.material.io/components/divider). These components provide common patterns for displaying groups of content.
![](https://developer.android.com/static/images/design/ui/mobile/material-components-containment.png)**Figure 3:**Containment

### Navigation components

Navigation components help people move through the UI. For mobile, the[navigation bar](https://m3.material.io/components/navigation-bar)or[navigation drawer](https://m3.material.io/components/navigation-drawer)contain your primary navigation destinations.[Tabs](https://m3.material.io/components/tabs),[the bottom app bar](https://m3.material.io/components/bottom-app-bar), and[the top app bar](https://m3.material.io/components/top-app-bar)provide different ways to navigate supporting information and actions. Read more about how to work with navigation within your[layouts](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-basics).
![](https://developer.android.com/static/images/design/ui/mobile/material-components-navigation.png)**Figure 4:**Navigation

### Selection components

Selection components let people specify choices. Whether building out a form with[checkboxes](https://m3.material.io/components/checkbox)and[radio buttons](https://m3.material.io/components/radio-button), filtering using[chips](https://m3.material.io/components/chips), or toggling settings with[switches](https://m3.material.io/components/switch)and[sliders](https://m3.material.io/components/sliders), selection components allow users to control and input their decisions.
![](https://developer.android.com/static/images/design/ui/mobile/material-components-selection.png)**Figure 5:**Selection

### Text input components

Text input components let people enter and edit text.[Text fields](https://m3.material.io/components/text-fields)allow users to enter text into a UI.
![](https://developer.android.com/static/images/design/ui/mobile/material-components-text-input.png)**Figure 6:**Text Input

## Design systems for Compose

Read[Design systems in Compose](https://developer.android.com/jetpack/compose/designsystems)for details about how to use Compose to more smoothly implement a design system and give your app a consistent look and feel with theming, components, and other aspects of the design system.