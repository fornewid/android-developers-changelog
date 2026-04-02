---
title: Stop a foreground service  |  Background work  |  Android Developers
url: https://developer.android.com/develop/background-work/services/fgs/stop-fgs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Background work](https://developer.android.com/develop/background-work)
* [Guides](https://developer.android.com/develop/background-work/background-tasks)

# Stop a foreground service Stay organized with collections Save and categorize content based on your preferences.



If you want a foreground service to stop running in the foreground, you have
two options. You can stop the service, or you can leave the service
running but remove it from the foreground.

You can stop a foreground service
[the same way you would stop any service](/develop/background-work/services#Stopping). The service can
call its own [`stopSelf()`](/reference/android/app/Service#stopSelf()) method, or another component can stop it
by calling [`stopService()`](/reference/android/content/Context#stopService(android.content.Intent)). If you stop the service while it runs
in the foreground, its notification is removed.

To remove a service from the foreground, call
[`stopForeground(int)`](/reference/android/app/Service#stopForeground(int))
from inside the service. This method takes a boolean, which indicates whether to
remove the status bar notification as well. The service continues to run, but
it is no longer a foreground service.