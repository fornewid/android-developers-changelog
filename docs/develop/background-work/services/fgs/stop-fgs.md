---
title: https://developer.android.com/develop/background-work/services/fgs/stop-fgs
url: https://developer.android.com/develop/background-work/services/fgs/stop-fgs
source: md.txt
---

> Documentation index: https://developer.android.com/develop/background-work/services/fgs/llms.txt

If you want a foreground service to stop running in the foreground, you have
two options. You can stop the service, or you can leave the service
running but remove it from the foreground.

You can stop a foreground service
[the same way you would stop any service](https://developer.android.com/develop/background-work/services.md.txt#Stopping). The service can
call its own [`stopSelf()`](https://developer.android.com/reference/android/app/Service.md.txt#stopSelf()) method, or another component can stop it
by calling [`stopService()`](https://developer.android.com/reference/android/content/Context.md.txt#stopService(android.content.Intent)). If you stop the service while it runs
in the foreground, its notification is removed.

To remove a service from the foreground, call
[`stopForeground(int)`](https://developer.android.com/reference/android/app/Service.md.txt#stopForeground(int)) from inside the service. This method
takes a boolean, which indicates whether to remove the status bar notification
as well. The service continues to run, but it's no longer a foreground service.