---
title: https://developer.android.com/develop/devices/assistant/grow-overview
url: https://developer.android.com/develop/devices/assistant/grow-overview
source: md.txt
---

Project: /develop/devices/assistant/_project.yaml
Book: /develop/devices/assistant/_book.yaml

Extending your app to Assistant with App Actions lets users quickly engage
with the key features of your app by talking to Google Assistant. Once you
implement App Actions, you can use it to drive user retention and engagement
for your app with the following features:

- **System shortcut suggestions**. The Google Shortcuts Integration library
  lets Google Assistant suggest your dynamic shortcuts to users. This
  capability makes it simple for users to discover and replay shortcuts to your
  app's key features.

- **In-app shortcut suggestions** . The [In-App Promo SDK](https://developer.android.com/guide/app-actions/in-app-promo-sdk) lets you
  easily suggest Assistant shortcuts to users in your app. Users can launch
  these shortcuts using their voice with Assistant and see them suggested on
  Google surfaces.

## Enable system shortcut suggestions

To add the Google Shortcuts Integration library to your Android project and
push dynamic shortcuts to Assistant, follow the instructions at [Push dynamic
shortcuts to Assistant](https://developer.android.com/guide/app-actions/dynamic-shortcuts).

These best practices maximize user exposure to your App Actions bound shortcuts:

- Push a shortcut whenever a user completes a relevant action to help Google
  surfaces, like Assistant, suggest the shortcut to the user. You can push an
  unlimited number of shortcuts with the Google Shortcuts Integration library.

- Define static shortcuts in `shortcuts.xml` for Assistant to suggest
  proactively to users. These shortcuts can only update by releasing
  a new version of your app to Google Play Console, so they are best for
  suggesting shortcuts that apply to all users, for example, "Send an email."

  Static shortcuts are useful for helping Assistant suggest app shortcuts to
  new users who have not yet taken actions in your app that have dynamic
  shortcuts.

## Create in-app shortcut suggestions

The In-App Promo SDK lets you suggest Assistant shortcuts in your app.
For example, if a user performs a search for "heavy metal workout" in your music
app, you might suggest an Assistant shortcut directly to those search results
in the future. The user can then launch the shortcut by asking Assistant, *"Hey
Google, Example App heavy metal workout."*

Consider suggesting shortcuts during user onboarding or when a user performs an
action you want them to quickly replay in the future with Assistant.

For more information about building suggestions for your app, see
[Implement suggestions](https://developer.android.com/guide/app-actions/in-app-promo-sdk#implement_suggestions).