---
title: https://developer.android.com/develop/connectivity/nfc
url: https://developer.android.com/develop/connectivity/nfc
source: md.txt
---

Near Field Communication (NFC) is a set of short-range wireless technologies,
typically requiring a distance of 4 cm or less to initiate a connection. NFC
lets you share small payloads of data between an NFC tag and an
Android-powered device, or between two Android-powered devices.

Tags can range in complexity. Simple tags offer just read and write semantics,
sometimes with one-time-programmable areas to make the card read-only. More
complex tags offer math operations, and have cryptographic hardware to
authenticate access to a sector. The most sophisticated tags contain operating
environments, allowing complex interactions with code executing on the tag. The
data stored in the tag can also be written in a variety of formats, but many of
the Android framework APIs are based around a [NFC
Forum](http://www.nfc-forum.org/) standard called NDEF (NFC Data Exchange
Format).

Android-powered devices with NFC simultaneously support two main modes of
operation:

1. **Reader/writer mode**, allowing the NFC device to read and write passive NFC tags and stickers.
2. **Card emulation mode**, allowing the NFC device itself to act as an NFC card. The emulated NFC card can then be accessed by an external NFC reader, such as an NFC point-of-sale terminal.

**[NFC Basics](https://developer.android.com/develop/connectivity/nfc/nfc)**
:   This document describes how Android handles discovered NFC tags and how it
    notifies applications of data that is relevant to the application. It also
    goes over how to work with the NDEF data in your applications and gives an
    overview of the framework APIs that support the basic NFC feature set of
    Android.

**[Advanced NFC](https://developer.android.com/develop/connectivity/nfc/advanced-nfc)**
:   This document goes over the APIs that enable use of the various tag
    technologies that Android supports. When you are not working with NDEF data,
    or when you are working with NDEF data that Android cannot fully understand,
    you have to manually read or write to the tag in raw bytes using your own
    protocol stack. In these cases, Android provides support to detect certain
    tag technologies and to open communication with the tag using your own
    protocol stack.

**[Host-based Card Emulation](https://developer.android.com/develop/connectivity/nfc/hce)**
:   This document describes how Android devices can perform as NFC cards without
    using a secure element, allowing any Android application to emulate a card
    and talk directly to the NFC reader.