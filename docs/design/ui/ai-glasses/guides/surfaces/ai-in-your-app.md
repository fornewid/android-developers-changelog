---
title: AI in your app  |  AI Glasses  |  Android Developers
url: https://developer.android.com/design/ui/ai-glasses/guides/surfaces/ai-in-your-app
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [AI Glasses](https://developer.android.com/design/ui/ai-glasses)
* [Guides](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles)

# AI in your app Stay organized with collections Save and categorize content based on your preferences.



The AI glasses form factor provides a first-person and muli-modal view of the
user interacting with their environment. Combined with voice input and hardware
sensors, it has the potential to provide an unprecedented level of contextual
information to your app. To utilize this context in your app, you can use an
in-app agent and route these multi-modal inputs to your LLM. Your app can take
advantage of the Gemini Live API or integrate a custom AI agent.

## Use AI Responsibly

Design for all aspects of user comfort, including Sensory, Cognitive, Social,
and Comfort with AI.

Design your apps for 'Consent First':

* Don't assume you can record because an app is open.
* Use explicit triggers like a physical gesture before activating sensors.
* Have your agent ask to turn on the camera if it deems it necessary for the
  activity.
* Collect the minimum amount of data necessary to deliver value, process it,
  and then discard it.

## Design considerations for your agent

For AI glasses, AI features provide an efficient manner to accomplish tasks like
text to speech and image recognition. AI allows for interaction through natural
language, instead of static trees.

AI can help make completing tasks between phone and glasses more natural with
natural audio cues and subtle visuals.

When integrating an agent within your app, consider:

* Voice and tone
* Contexts of the user in everyday life
* User safety
* Don't overwhelm the user
* Design for social comfort

For AI glasses, the AI agent should be concise and unobtrusive, following
conversational UX best practices and [AI patterns](/design/ui/ai-glasses/guides/interaction/ai-patterns)

[Previous

arrow\_back

App view](/design/ui/ai-glasses/guides/surfaces/app)

[Next

Inputs

arrow\_forward](/design/ui/ai-glasses/guides/interaction/inputs)