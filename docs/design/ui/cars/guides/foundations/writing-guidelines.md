---
title: https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines
url: https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines
source: md.txt
---

# Writing principles

Text on the car screen must be glanceable, consistent, clear, and oriented towards the driver's situation.

This section describes how you can:

- [Make content glanceable](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#glanceable)
- [Use consistent language](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#consistent)
- [Write with situational awareness](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#situational)
- [Follow best practices for writing component text](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#best-practices)

## Make content glanceable

Simple, glanceable content makes sure that the driver's attention returns quickly to the road.

You should:

- [Use scannable content patterns](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#scannable)
- [Use simpler, direct language](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#simple-language)
- [Limit text to 120 characters](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#limit-text)

### Use scannable content patterns

While both driving and parked, the goal is to reduce the driver's cognitive load. People don't read what's on the screen; instead they scan the text in an F-shaped pattern.

Front-load important information, clearly and concisely describing the action the user needs to perform. Use clear hierarchy to convey information at a glance. For example, use bullet points to organize content.

|                                                                Do                                                                |                                                                                      Don't                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Connect your phone to start** To get started, do one of the following: - Tap the notification on your phone - Scan the QR Code | **Connect your phone to start** Tap the on the notification on your phone or scan the QR Code to get started. You will then be guided to your car's app to complete next steps. |

### Use direct language

Avoid using jargon or complex words. They confuse the user and delay task completion.

|           Do            |           Don't           |
|-------------------------|---------------------------|
| Sign in to your account | Authenticate your account |

### Limit text to 120 characters

Limiting the amount of text the driver has to read before taking action reduces cognitive load and increases comprehension. Based on guidance from National Highway Traffic Safety Administration (NHTSA) and Japan Automobile Manufacturers Association (JAMA):

- A single message or chunk of text in English shouldn't exceed 120 characters or 24 words
- A single message or chunk of text in Japanese shouldn't exceed 30 characters
- The text in 1 line shouldn't exceed 80 characters
- A sentence or paragraph shouldn't span more than 3 lines of text

This guidance doesn't apply to legal or privacy text.

|                                                                       Do                                                                       |                                                                                                 Don't                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android Auto doesn't work with your phone** Android Auto isn't part of your phone's operating system, so it won't work with this car. **OK** | **Android Auto was not pre installed on this device** Android Auto must be bundled with your operating system to work correctly. Please contact your phone manufacturer for assistance. **Try Again** |

## Use consistent language

Consistent language helps minimize cognitive load for drivers.

You should:

- [Be consistent in your writing style](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#consistent-writing)
- [Unify terminology](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#terminology)

### Be consistent in your writing style

Consistency creates a cohesive and recognizable voice for your brand. It helps drivers navigate the text seamlessly and builds trust and loyalty over time.

Based on your brand's style choices, ensure consistency in choice of words, sentence structure, capitalization, punctuation, and overall voice and tone.

|                                                                                  Do                                                                                  |                                                             Don't                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ***Make buttons sentence case or title case consistently*** Cancel setup Connect another phone                                                                       | ***Mix capitalization across buttons*** Cancel Setup Connect another device                                                   |
| ***Punctuate the end of standalone sentences consistently: period or no period*** "Your phone is now connected to the car" and "You lost connection with your phone" | ***Mix use of periods across sentences*** "Your phone is now connected to the car." and "You lost connection with your phone" |

### Unify terminology

Using different words to mean the same thing confuses users. Use consistent terminology across your product to remove ambiguity during user journeys, enhance user comprehension, and increase user trust.

|                                   Do                                   |                                     Don't                                      |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **First reference**: Phone **Second reference**: Connect another phone | **First reference**: Mobile device **Second reference**: Connect another phone |

## Write with situational awareness

Ensure that the language on the UI is relevant to the user's needs and situation, including whether they are driving, parked, or experiencing an emergency.

You should:

- [Balance brevity with clarity](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#brevity-clarity)
- [Lead with benefit to the user](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#lead-with-benefits)
- [Use reassuring tone of voice, except in emergency](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#tone)

### Balance brevity with clarity

The text shown during driving should be brief and clear. However, it's OK to use longer explanations for complex situations --- such as privacy consents, permissions, and data sharing --- when the driver is parked. In those instances, break up longer text using lists and hierarchy to keep text readable.

|                                                                                                                              Do                                                                                                                               |                                                                                   Don't                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Chromecast built-in** To use Chromecast built-in, you'll need to agree to Google's Terms of Service and Google's Privacy Policy. Your device data ensures Chromecast built-in works as expected, and won't be used to identify you. \[I agree\] \[Not now\] | **Chromecast Terms of Service** You must agree to Google's Terms of Service and Google's Privacy Policy. Your device data won't be used to identify you. \[OK\] \[Cancel\] |

### Lead with benefit to the user

By starting with the value a feature offers, you can prioritize the importance of the user's needs, reduce cognitive load, and help them make a decision to move forward in a short span of time.

|                    Do                    |                Don't                |
|------------------------------------------|-------------------------------------|
| To connect your phone, turn on Bluetooth | Use Bluetooth to connect your phone |
| To sign in faster, scan the QR Code      | Scan the QR Code to connect faster  |

### Use reassuring tone of voice, except in emergency

When the car is in motion, use a reassuring tone of voice to avoid distracting the driver and causing needless anxiety.

However, exceptions should be made when the driver is in physical danger and needs to take immediate action. In those cases, use direct instruction and exclamation marks to convey urgency.

|                      Do                      |                               Don't                                |
|----------------------------------------------|--------------------------------------------------------------------|
| (Non emergency) New conversations are paused | (Non emergency) For your safety, all new conversations are paused! |
| (Non emergency) Android Auto lost connection | (Non emergency) Lost connection!                                   |
| (Emergency) Brake now!                       | (Emergency) Take control of your steering wheel to stop collision  |

## Follow best practices for writing component text

These best practices are always relevant but especially so for car screens.

You should:

- [Make button text brief and actionable](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#button-text)
- [Provide confirmation messages](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#confirmation)
- [Provide recovery from errors](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#error-recovery)
- [Front-load critical information in notifications](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#critical-info)

### Make button text brief and actionable

Button labels, also known as CTAs (calls to action), should always start with a verb and ideally contain no more than 3 words.

|      Do       |     Don't      |
|---------------|----------------|
| Connect phone | Phone is ready |
| Download app  | App listing    |

### Provide confirmation messages

Provide a confirmation message to reassure users when tasks they initiated have been completed.

|                         Do                         |            Don't            |
|----------------------------------------------------|-----------------------------|
| Dave's phone is now connected to the car's hotspot | \<No confirmation message\> |

### Provide recovery from errors

Error messages should state the problem clearly and offer a way out of the situation. If there's no recovery path, the message should be transparent about it with the user.

|                                                          Do                                                          |                                            Don't                                             |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Turn on Wi-Fi to connect** Android Auto needs 5 GHz Wi-Fi support to connect \[Turn on Wi-Fi\] \[Not now\]         | **Android Auto is not connected** Your Wi-Fi is turned off \[OK\]                            |
| **Try a new USB cable** Your phone keeps disconnecting from the car. Using a different USB cable or port could help. | **Damaged USB cable detected** Android Auto has noticed an unusual number of disconnections. |

### Front-load critical information in notifications

Notifications should succinctly front-load critical information.[Avoid causing alarm to the driver in any way](https://developer.android.com/design/ui/cars/guides/foundations/writing-guidelines#tone).

|                                        Do                                        |                                            Don't                                             |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Focus on driving** Some new notifications are saved in the Notification Center | **Notifications aren't being shown** Go to the Notification Center to see your notifications |