---
title: https://developer.android.com/develop/background-work/background-tasks/asynchronous
url: https://developer.android.com/develop/background-work/background-tasks/asynchronous
source: md.txt
---

# Asynchronous background processing

Asynchronous work is the second component of background work, alongside persistent work. While both persistent and asynchronous work take place in the background, they are ultimately quite different.

Asynchronous work is that which:

- Takes place in the moment.
- Does not need to persist across app restarts or device reboots.
- Occurs off the main thread, or blocks the main thread.

This is in contrast to persistent work, which you may schedule for future execution and which remains scheduled through app restarts and device reboots. An example of asynchronous work may be sending an HTTP request off the main thread, returning its result only when it arrives.

## Java and Kotlin

The way you handle asynchronous work depends on the overall app architecture you follow. If you are working with a Java Programming Language app, your needs are different than if you are working with Kotlin.

|                 |                                                     Kotlin                                                     |                                                           Java                                                            |
|    Solution     |                                                  Coroutines.                                                   |                                                       Java threads.                                                       |
| Further reading | For a full overview of Coroutines, see the[Coroutines guide](https://developer.android.com/kotlin/coroutines). | See the[Java Threads](https://developer.android.com/guide/background/asynchronous/java-threads)page for more information. |
|-----------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|

## Further reading

For more information on persistent work, see the[persistent work overview](https://developer.android.com/guide/background/persistent).