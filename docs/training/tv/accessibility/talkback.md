---
title: https://developer.android.com/training/tv/accessibility/talkback
url: https://developer.android.com/training/tv/accessibility/talkback
source: md.txt
---

# TalkBack evaluation examples for TV apps

This guide lists steps to evaluate your TV app to improve a screen reader user's experience. Perform these steps to understand how users experience your app when TalkBack, the Android screen reader, is enabled.

## Evaluation examples

Start your evaluation by[enabling TalkBack](https://support.google.com/googletv/answer/10070337)and opening your app. We recommend that the first time you conduct this evaluation, you do so without looking at the TV screen.

### First-time use

Explore the landing page and log into an account, trying every possible login path:

- Use the remote control to enter the account credentials.
- If available, log in with a code.
- If available, opt into a trial.

Confirm the following:

- Are all key elements on the page reachable and clickable? That is, can you select all key elements when navigating with the remote?
- Are elements, such as "Login," meaningfully labeled and announced when TalkBack is enabled? Watch out for unlabeled elements or sequences of numbers, such as "unlabeled" or "item 08328492qw."
- When TalkBack is enabled, is all the text that appears on screen announced?
- Do interactions yield expected results? For example, does clicking the**Sign in**button actually bring users to a sign-in page?
- Is navigation smooth, or do issues occur? For example, does the selection jump to the wrong element in the UI at any point?
- Confirm the following login-specific issues:
  - Can you move from character to character on the screen keyboard when using the remote to type?
  - When using a login code that displays on the TV to be entered on a secondary device, can you navigate from character to character?

### Navigate the user interface with a remote

Navigate through the interface, testing the following behaviors for all pages and menus:

- Navigate all the way to the end of the page and back.
- Navigate all the way to the end of a row and back.
- Click row elements, including content cards and buttons, to confirm that all actions yield expected results.

Confirm the following:

- Are all key elements on the page reachable and clickable? That is, can you select all key elements when navigating with the remote?
- If an element has focus, is it meaningfully labeled and announced? Watch out for unlabeled elements or sequences of numbers, such as "unlabeled" or "item 08328492qw."
- If an element with text has focus, is all the text that appears on screen announced by TalkBack?
- Do interactions yield expected results? Is navigation smooth, or do issues occur? For example, does the selection jump to the wrong element in the UI at any point?
- When opening a page, does clicking the**Back**button bring the user to where they were before opening the page?
- Confirm the following row-specific issues:
  - If a row heading has focus, is it announced by TalkBack?
  - If a row has focus, are all items within the row announced by TalkBack? For example, if it's a movie row, are all movie titles announced by TalkBack?
- Avoid instances of automatic playback. Check the following:
  - Does content start playing only when the user has initiated an interaction?
  - If not, can autoplaying content be paused or stopped by the user?

**Note:** Automatic playback of content, such as trailer autoplay, can be disruptive for users with vision impairments. The ability to pause or stop autoplay content is recommended by the[Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/).

### Explore information pages for media content

If your app contains media content with detail pages, such as an information page about a movie or show, open the detail page for two or more media titles and do the following:

- Navigate through all the information available for a title.
- Test all available actions, such as play, rent, and add to favorites.

Confirm the following:

- Are all key elements on the page reachable and clickable? That is, can you select all key elements when navigating with the remote?
- If an element has focus, is it meaningfully labeled and announced? Watch out for unlabeled elements or sequences of numbers, such as "unlabeled" or "item 08328492qw."
- If an element has focus, is all the text announced by TalkBack?
- Do interactions yield expected results? Is navigation smooth, or do issues occur? For example, does the selection jump to the wrong element in the UI at any point?
- When opening a page, does clicking the**Back**button bring the user to where they were before opening the page?
- Confirm the following detail-page specific issues:
  - Is the title announced by TalkBack when the user lands on the page?
  - Is metadata, such as ratings and genre, announced by TalkBack?
  - If there are additional rows, are all row headings announced by TalkBack?
- Watch out for instances of automatic playback. Check the following:
  - Does content start playing only when the user has initiated an interaction?
  - If not, can autoplaying content be paused or stopped by the user?

### Play media content

If available, play one or more media titles and test the following interactions:

- Play and pause.
- Rewind and fast-forward.
- Activate audio descriptions, if available.
- Change audio language.
- Enable and change subtitles or captions, if available, including changing any associated settings.
- Test any additional playback controls that are available.

Confirm the following:

- If media controls have focus, are they appropriately labeled and announced by TalkBack? This includes additional options such as subtitle options or audio descriptions.
- If media controls have focus, do all media controls work in the expected manner when TalkBack is enabled?
- When pausing and resuming media playback, do TalkBack announcements occur concurrently over the movie or show's audio?
- When rewinding or fast-forwarding, does TalkBack provide information about timestamps or about rewinding and fast-forwarding speed?
- Change settings and check the following:
  - Are actions confirmed by TalkBack?
  - Are toggles and toggle actions appropriately labeled? For example, is*current state* +*action*announced?

### Watch live content with an Electronic Programming Guide

If your app has live TV content, do the following:

- Browse the Electronic Programming Guide (EPG).
- Browse through different channels.
- Browse forward in time.
- Click to play live content.
- Test any additional controls that are available, such as marking channels as favorites and reordering rows.

Confirm the following:

- Are all key elements on the page reachable and clickable? That is, can you select all key elements when navigating with the remote?
- If an element has focus, is it meaningfully labeled and announced? Watch out for unlabeled elements or sequences of numbers, such as "unlabeled" or "item 08328492qw."
- If an element has focus, is all the text that appears on screen announced by TalkBack?
- Do interactions yield expected results? Is navigation smooth, or do issues occur? For example, does the selection jump to the wrong element in the UI at any point?
- When opening a page, does clicking the**Back**button bring the user to where they were before opening the page?

### Voice support

If your app has any embedded form of voice search, use it to do the following:

- Spell, if available.
- Search for content.

Confirm the following:

- Can users revise what they have spelled?
- Are there any interferences between searching or spelling with voice and TalkBack? For example, when TalkBack announces something, is the announcement picked up as a voice query?

Examine the search results page like any other page. For guidance, see the[Navigate the user interface with a remote](https://developer.android.com/training/tv/accessibility/talkback#navigate-with-remote)section.

### Explore app settings

Navigate through settings, including the following:

- Navigate through every menu and submenu.
- Modify settings.

Confirm the following:

- Are all key elements on the page reachable and clickable? That is, can you select all key elements when navigating with the remote?
- If an element has focus, is it meaningfully labeled and announced? Watch out for unlabeled elements or sequences of numbers, such as "unlabeled" or "item 08328492qw."
- If a setting has focus, is all the text that appears on screen announced by TalkBack?
- Do interactions yield expected results? Is navigation smooth, or do issues occur? For example, does the selection jump to the wrong element in the UI at any point?
- When opening a page, does clicking the**Back**button bring the user to where they were before opening the page?
- Change settings and check the following:
  - Are selections confirmed by TalkBack?
  - Are toggles and toggle actions appropriately labeled? For example, is*current state* +*action*announced?

### Make changes to global TalkBack settings

Open the global TalkBack settings on the TV device and do the following:

- Modify each TalkBack setting, such as speech rate and verbosity, one by one.
- After modifying each setting, return to the app you are evaluating and confirm that the changes you made to TalkBack settings successfully carry into the app.

## Learn more

To learn more, see our[accessibility development resources](https://developer.android.com/guide/topics/ui/accessibility).