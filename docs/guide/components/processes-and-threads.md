---
title: https://developer.android.com/guide/components/processes-and-threads
url: https://developer.android.com/guide/components/processes-and-threads
source: md.txt
---

# Processes and threads overview

When an application component starts and the application doesn't have any other components running, the Android system starts a new Linux process for the application with a single thread of execution. By default, all components of the same application run in the same process and thread, called the*main*thread.

If an application component starts and there is already a process for that application, because another component from the application already started, then the component starts within that process and uses the same thread of execution. However, you can arrange for different components in your application to run in separate processes, and you can create additional threads for any process.

This document discusses how processes and threads work in an Android application.

## Processes

By default, all of an application's components run in the same process, and most applications don't change this. However, if you find that you need to control which process a certain component belongs to, you can do so in the manifest file.

The manifest entry for each type of component element---[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element),[`<service>`](https://developer.android.com/guide/topics/manifest/service-element),[`<receiver>`](https://developer.android.com/guide/topics/manifest/receiver-element), and[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element)---supports an`android:process`attribute that can specify a process the component runs in. You can set this attribute so that each component runs in its own process or so that some components share a process while others don't.

You can also set`android:process`so that components of different applications run in the same process, provided that the applications share the same Linux user ID and are signed with the same certificates.

The[`<application>`](https://developer.android.com/guide/topics/manifest/application-element)element also supports an`android:process`attribute, which you can use to set a default value that applies to all components.

Android might decide to shut down a process at some point, when resources are required by other processes that are more immediately serving the user. Application components running in the process that's shut down are consequently destroyed. A process is started again for those components when there's work for them to do.

When deciding which processes to shut down, the Android system weighs their relative importance to the user. For example, it more readily shuts down a process hosting activities that are no longer visible on screen, compared to a process hosting visible activities. The decision of whether to terminate a process, therefore, depends on the state of the components running in that process.

The details of the process lifecycle and its relationship to application states are discussed in[Processes and app lifecycle](https://developer.android.com/guide/topics/processes/process-lifecycle).

## Threads

When an application is launched, the system creates a thread of execution for the application, called the*main thread* . This thread is very important, because it is in charge of dispatching events to the appropriate user interface widgets, including drawing events. It is also almost always the thread in which your application interacts with components from the Android UI toolkit's[android.widget](https://developer.android.com/reference/android/widget/package-summary)and[android.view](https://developer.android.com/reference/android/view/package-summary)packages. For this reason, the main thread is sometimes called the*UI thread* . However, under special circumstances, an app's main thread might not be its UI thread. For more information, see[Thread annotations](https://developer.android.com/studio/write/annotations#thread-annotations).

The system does*not* create a separate thread for each instance of a component. All components that run in the same process are instantiated in the UI thread, and system calls to each component are dispatched from that thread. Consequently, methods that respond to system callbacks---such as[onKeyDown()](https://developer.android.com/reference/android/view/View#onKeyDown(int, android.view.KeyEvent))to report user actions, or a lifecycle callback method---always run in the UI thread of the process.

For instance, when the user touches a button on the screen, your app's UI thread dispatches the touch event to the widget, which in turn sets its pressed state and posts an invalidate request to the event queue. The UI thread dequeues the request and notifies the widget to redraw itself.

Unless you implement your application properly, this single-thread model can yield poor performance when your app performs intensive work in response to user interaction. Performing long operations in the UI thread, such as network access or database queries, blocks the whole UI. When the thread is blocked, no events can be dispatched, including drawing events.

From the user's perspective, the application appears to hang. Even worse, if the UI thread is blocked for more than a few seconds, the user is presented with the "[application not responding](https://developer.android.com/guide/practices/responsiveness.html)" (ANR) dialog. The user might then decide to quit your application or even uninstall it.

Bear in mind that the Android UI toolkit is*not*thread-safe. So, don't manipulate your UI from a worker thread. Do all manipulation to your user interface from the UI thread. There are two rules to Android's single-thread model:

1. Don't block the UI thread.
2. Don't access the Android UI toolkit from outside the UI thread.

### Worker threads

Because of this single-thread model, it's vital to the responsiveness of your application's UI that you don't block the UI thread. If you have operations to perform that aren't instantaneous, make sure to do them in separate*background* or*worker*threads. Just remember that you can't update the UI from any thread other than the UI, or main, thread.

To help you follow these rules, Android offers several ways to access the UI thread from other threads. Here is a list of methods that can help:

- [Activity.runOnUiThread(Runnable)](https://developer.android.com/reference/android/app/Activity#runOnUiThread(java.lang.Runnable))
- [View.post(Runnable)](https://developer.android.com/reference/android/view/View#post(java.lang.Runnable))
- [View.postDelayed(Runnable,
  long)](https://developer.android.com/reference/android/view/View#postDelayed(java.lang.Runnable, long))

The following example uses`View.post(Runnable)`:  

### Kotlin

```kotlin
fun onClick(v: View) {
    Thread(Runnable {
        // A potentially time consuming task.
        val bitmap = processBitMap("image.png")
        imageView.post {
            imageView.setImageBitmap(bitmap)
        }
    }).start()
}
```

### Java

```java
public void onClick(View v) {
    new Thread(new Runnable() {
        public void run() {
            // A potentially time consuming task.
            final Bitmap bitmap =
                    processBitMap("image.png");
            imageView.post(new Runnable() {
                public void run() {
                    imageView.setImageBitmap(bitmap);
                }
            });
        }
    }).start();
}
```

This implementation is thread-safe, because the background operation is done from a separate thread while the[ImageView](https://developer.android.com/reference/android/widget/ImageView)is always manipulated from the UI thread.

However, as the complexity of the operation grows, this kind of code can get complicated and difficult to maintain. To handle more complex interactions with a worker thread, you might consider using a[Handler](https://developer.android.com/reference/android/os/Handler)in your worker thread to process messages delivered from the UI thread. For a full explanation of how to schedule work on background threads and communicate back to the UI thread, see[Background Work Overview](https://developer.android.com/training/multiple-threads).

### Thread-safe methods

In some situations, the methods you implement are called from more than one thread, and therefore must be written to be thread-safe.

This is primarily true for methods that can be called remotely, such as methods in a[bound service](https://developer.android.com/guide/components/bound-services). When a call on a method implemented in an[IBinder](https://developer.android.com/reference/android/os/IBinder)originates in the same process in which the`IBinder`is running, the method is executed in the caller's thread. However, when the call originates in another process, the method executes in a thread chosen from a pool of threads that the system maintains in the same process as the`IBinder`. It's not executed in the UI thread of the process.

For example, whereas a service's[onBind()](https://developer.android.com/reference/android/app/Service#onBind(android.content.Intent))method is called from the UI thread of the service's process, methods implemented in the object that`onBind()`returns, such as a subclass that implements remote procedure call (RPC) methods, are called from threads in the pool. Because a service can have more than one client, more than one pool thread can engage the same`IBinder`method at the same time, so`IBinder`methods must be implemented to be thread-safe.

Similarly, a content provider can receive data requests that originate in other processes. The[ContentResolver](https://developer.android.com/reference/android/content/ContentResolver)and[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider)classes hide the details of how the interprocess communication (IPC) is managed, but the`ContentProvider`methods that respond to those requests---the methods[query()](https://developer.android.com/reference/android/content/ContentProvider#query(android.net.Uri, java.lang.String[], android.os.Bundle, android.os.CancellationSignal)),[insert()](https://developer.android.com/reference/android/content/ContentProvider#insert(android.net.Uri, android.content.ContentValues)),[delete()](https://developer.android.com/reference/android/content/ContentProvider#delete(android.net.Uri, java.lang.String, java.lang.String[])),[update()](https://developer.android.com/reference/android/content/ContentProvider#update(android.net.Uri, android.content.ContentValues, java.lang.String, java.lang.String[])), and[getType()](https://developer.android.com/reference/android/content/ContentProvider#getType(android.net.Uri))---are called from a pool of threads in the content provider's process, not the UI thread for the process. Because these methods might be called from any number of threads at the same time, they too must be implemented to be thread-safe.

## Interprocess communication

Android offers a mechanism for IPC using RPCs, in which a method is called by an activity or other application component but executed remotely in another process, with any result returned back to the caller. This entails decomposing a method call and its data to a level the operating system can understand, transmitting it from the local process and address space to the remote process and address space, and then reassembling and reenacting the call there.

Return values are then transmitted in the opposite direction. Android provides all the code to perform these IPC transactions, so you can focus on defining and implementing the RPC programming interface.

To perform IPC, your application must bind to a service using[bindService()](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent, android.content.ServiceConnection, int)). For more information, see the[Services overview](https://developer.android.com/guide/components/services).