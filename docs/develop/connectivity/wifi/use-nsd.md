---
title: https://developer.android.com/develop/connectivity/wifi/use-nsd
url: https://developer.android.com/develop/connectivity/wifi/use-nsd
source: md.txt
---

Network service discovery (NSD) gives your app access to services that other
devices provide on a local network. Devices that support NSD include printers,
webcams, HTTPS servers, and other mobile devices.

NSD implements the DNS-based Service Discovery (DNS-SD) mechanism, which
allows your app to request services by specifying a type of service and the name
of a device instance that provides the desired type of service. DNS-SD is
supported both on Android and on other mobile platforms.

Adding NSD to your app allows your users to identify other devices on the
local network that support the services your app requests. This is useful for a
variety of peer-to-peer applications such as file sharing or multi-player
gaming. Android's NSD APIs simplify the effort required for you to implement
such features.

This lesson shows you how to build an application that can broadcast its
name and connection information to the local network and scan for information
from other applications doing the same. Finally, this lesson shows you how
to connect to the same application running on another device.

## Register your service on the network

**Note:** This step is optional. If
you don't care about broadcasting your app's services over the local network,
you can skip forward to the
next section, [Discover Services on the Network](https://developer.android.com/develop/connectivity/wifi/use-nsd#discover).

To register your service on the local network, first create a `https://developer.android.com/reference/android/net/nsd/NsdServiceInfo` object. This object provides the information
that other devices on the network use when they're deciding whether to connect to your
service.

### Kotlin

```kotlin
fun registerService(port: Int) {
    // Create the NsdServiceInfo object, and populate it.
    val serviceInfo = NsdServiceInfo().apply {
        // The name is subject to change based on conflicts
        // with other services advertised on the same network.
        serviceName = "NsdChat"
        serviceType = "_nsdchat._tcp"
        setPort(port)
        ...
    }
}
```

### Java

```java
public void registerService(int port) {
    // Create the NsdServiceInfo object, and populate it.
    NsdServiceInfo serviceInfo = new NsdServiceInfo();

    // The name is subject to change based on conflicts
    // with other services advertised on the same network.
    serviceInfo.setServiceName("NsdChat");
    serviceInfo.setServiceType("_nsdchat._tcp");
    serviceInfo.setPort(port);
    ...
}
```

This code snippet sets the service name to "NsdChat". The service name
is the instance name: it is the visible name to other devices on the network.
The name is visible to any device on the network that is using NSD to look for
local services. Keep in mind that the name must be unique for any service on the
network, and Android automatically handles conflict resolution. If
two devices on the network both have the NsdChat application installed, one of
them changes the service name automatically, to something like "NsdChat
(1)".

The second parameter sets the service type, specifies which protocol and transport
layer the application uses. The syntax is
"_\<protocol\>._\<transportlayer\>". In the
code snippet, the service uses HTTP protocol running over TCP. An application
offering a printer service (for instance, a network printer) would set the
service type to "_ipp._tcp".

**Note:** The International Assigned Numbers
Authority (IANA) manages a centralized,
authoritative list of service types used by service discovery protocols such as NSD and Bonjour.
You can download the list from [the
IANA list of service names and port numbers](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml).
If you intend to use a new service type, you should reserve it by filling out
the [IANA Ports and Service
registration form](http://www.iana.org/form/ports-services).

When setting the port for your service, avoid hardcoding it as this
conflicts with other applications. For instance, assuming
that your application always uses port 1337 puts it in potential conflict with
other installed applications that use the same port. Instead, use the device's
next available port. Because this information is provided to other apps by a
service broadcast, there's no need for the port your application uses to be
known by other applications at compile-time. Instead, the applications can get
this information from your service broadcast, right before connecting to your
service.

If you're working with sockets, here's how you can initialize a socket to any
available port simply by setting it to 0.

### Kotlin

```kotlin
fun initializeServerSocket() {
    // Initialize a server socket on the next available port.
    serverSocket = ServerSocket(0).also { socket ->
        // Store the chosen port.
        mLocalPort = socket.localPort
        ...
    }
}
```

### Java

```java
public void initializeServerSocket() {
    // Initialize a server socket on the next available port.
    serverSocket = new ServerSocket(0);

    // Store the chosen port.
    localPort = serverSocket.getLocalPort();
    ...
}
```

Now that you've defined the `https://developer.android.com/reference/android/net/nsd/NsdServiceInfo` object, you need to implement the `https://developer.android.com/reference/android/net/nsd/NsdManager.RegistrationListener` interface. This
interface contains callbacks used by Android to alert your application of the
success or failure of service registration and unregistration.

### Kotlin

```kotlin
private val registrationListener = object : NsdManager.RegistrationListener {

    override fun onServiceRegistered(NsdServiceInfo: NsdServiceInfo) {
        // Save the service name. Android may have changed it in order to
        // resolve a conflict, so update the name you initially requested
        // with the name Android actually used.
        mServiceName = NsdServiceInfo.serviceName
    }

    override fun onRegistrationFailed(serviceInfo: NsdServiceInfo, errorCode: Int) {
        // Registration failed! Put debugging code here to determine why.
    }

    override fun onServiceUnregistered(arg0: NsdServiceInfo) {
        // Service has been unregistered. This only happens when you call
        // NsdManager.unregisterService() and pass in this listener.
    }

    override fun onUnregistrationFailed(serviceInfo: NsdServiceInfo, errorCode: Int) {
        // Unregistration failed. Put debugging code here to determine why.
    }
}
```

### Java

```java
public void initializeRegistrationListener() {
    registrationListener = new NsdManager.RegistrationListener() {

        @Override
        public void onServiceRegistered(NsdServiceInfo NsdServiceInfo) {
            // Save the service name. Android may have changed it in order to
            // resolve a conflict, so update the name you initially requested
            // with the name Android actually used.
            serviceName = NsdServiceInfo.getServiceName();
        }

        @Override
        public void onRegistrationFailed(NsdServiceInfo serviceInfo, int errorCode) {
            // Registration failed! Put debugging code here to determine why.
        }

        @Override
        public void onServiceUnregistered(NsdServiceInfo arg0) {
            // Service has been unregistered. This only happens when you call
            // NsdManager.unregisterService() and pass in this listener.
        }

        @Override
        public void onUnregistrationFailed(NsdServiceInfo serviceInfo, int errorCode) {
            // Unregistration failed. Put debugging code here to determine why.
        }
    };
}
```

Now you have all the pieces to register your service. Call the method
`https://developer.android.com/reference/android/net/nsd/NsdManager#registerService(android.net.nsd.NsdServiceInfo, int, android.net.nsd.NsdManager.RegistrationListener)`.

Note that this method is asynchronous, so any code that needs to run
after the service has been registered must go in the `https://developer.android.com/reference/android/net/nsd/NsdManager.RegistrationListener#onServiceRegistered(android.net.nsd.NsdServiceInfo)` method.

### Kotlin

```kotlin
fun registerService(port: Int) {
    // Create the NsdServiceInfo object, and populate it.
    val serviceInfo = NsdServiceInfo().apply {
        // The name is subject to change based on conflicts
        // with other services advertised on the same network.
        serviceName = "NsdChat"
        serviceType = "_nsdchat._tcp"
        setPort(port)
    }

    nsdManager = (getSystemService(Context.NSD_SERVICE) as NsdManager).apply {
        registerService(serviceInfo, NsdManager.PROTOCOL_DNS_SD, registrationListener)
    }
}
```

### Java

```java
public void registerService(int port) {
    NsdServiceInfo serviceInfo = new NsdServiceInfo();
    serviceInfo.setServiceName("NsdChat");
    serviceInfo.setServiceType("_http._tcp.");
    serviceInfo.setPort(port);

    nsdManager = Context.getSystemService(Context.NSD_SERVICE);

    nsdManager.registerService(
            serviceInfo, NsdManager.PROTOCOL_DNS_SD, registrationListener);
}
```

## Discover services on the network

The network is teeming with life, from the beastly network printers to the
docile network webcams, to the brutal, fiery battles of nearby tic-tac-toe
players. The key to letting your application see this vibrant ecosystem of
functionality is service discovery. Your application needs to listen to service
broadcasts on the network to see what services are available, and filter out
anything the application can't work with.

Service discovery, like service registration, has two steps:
setting up a discovery listener with the relevant callbacks, and making a single asynchronous
API call to `https://developer.android.com/reference/android/net/nsd/NsdManager#discoverServices(java.lang.String, int, android.net.nsd.NsdManager.DiscoveryListener)`.

First, instantiate an anonymous class that implements `https://developer.android.com/reference/android/net/nsd/NsdManager.DiscoveryListener`. The following snippet shows a
simple example:

### Kotlin

```kotlin
// Instantiate a new DiscoveryListener
private val discoveryListener = object : NsdManager.DiscoveryListener {

    // Called as soon as service discovery begins.
    override fun onDiscoveryStarted(regType: String) {
        Log.d(TAG, "Service discovery started")
    }

    override fun onServiceFound(service: NsdServiceInfo) {
        // A service was found! Do something with it.
        Log.d(TAG, "Service discovery success$service")
        when {
            service.serviceType != SERVICE_TYPE -> // Service type is the string containing the protocol and
                // transport layer for this service.
                Log.d(TAG, "Unknown Service Type: ${service.serviceType}")
            service.serviceName == mServiceName -> // The name of the service tells the user what they'd be
                // connecting to. It could be "Bob's Chat App".
                Log.d(TAG, "Same machine: $mServiceName")
            service.serviceName.contains("NsdChat") -> nsdManager.resolveService(service, resolveListener)
        }
    }

    override fun onServiceLost(service: NsdServiceInfo) {
        // When the network service is no longer available.
        // Internal bookkeeping code goes here.
        Log.e(TAG, "service lost: $service")
    }

    override fun onDiscoveryStopped(serviceType: String) {
        Log.i(TAG, "Discovery stopped: $serviceType")
    }

    override fun onStartDiscoveryFailed(serviceType: String, errorCode: Int) {
        Log.e(TAG, "Discovery failed: Error code:$errorCode")
        nsdManager.stopServiceDiscovery(this)
    }

    override fun onStopDiscoveryFailed(serviceType: String, errorCode: Int) {
        Log.e(TAG, "Discovery failed: Error code:$errorCode")
        nsdManager.stopServiceDiscovery(this)
    }
}
```

### Java

```java
public void initializeDiscoveryListener() {

    // Instantiate a new DiscoveryListener
    discoveryListener = new NsdManager.DiscoveryListener() {

        // Called as soon as service discovery begins.
        @Override
        public void onDiscoveryStarted(String regType) {
            Log.d(TAG, "Service discovery started");
        }

        @Override
        public void onServiceFound(NsdServiceInfo service) {
            // A service was found! Do something with it.
            Log.d(TAG, "Service discovery success" + service);
            if (!service.getServiceType().equals(SERVICE_TYPE)) {
                // Service type is the string containing the protocol and
                // transport layer for this service.
                Log.d(TAG, "Unknown Service Type: " + service.getServiceType());
            } else if (service.getServiceName().equals(serviceName)) {
                // The name of the service tells the user what they'd be
                // connecting to. It could be "Bob's Chat App".
                Log.d(TAG, "Same machine: " + serviceName);
            } else if (service.getServiceName().contains("NsdChat")){
                nsdManager.resolveService(service, resolveListener);
            }
        }

        @Override
        public void onServiceLost(NsdServiceInfo service) {
            // When the network service is no longer available.
            // Internal bookkeeping code goes here.
            Log.e(TAG, "service lost: " + service);
        }

        @Override
        public void onDiscoveryStopped(String serviceType) {
            Log.i(TAG, "Discovery stopped: " + serviceType);
        }

        @Override
        public void onStartDiscoveryFailed(String serviceType, int errorCode) {
            Log.e(TAG, "Discovery failed: Error code:" + errorCode);
            nsdManager.stopServiceDiscovery(this);
        }

        @Override
        public void onStopDiscoveryFailed(String serviceType, int errorCode) {
            Log.e(TAG, "Discovery failed: Error code:" + errorCode);
            nsdManager.stopServiceDiscovery(this);
        }
    };
}
```

The NSD API uses the methods in this interface to inform your application when discovery
is started, when it fails, and when services are found and lost (lost means "is
no longer available"). Notice that this snippet does several checks
when a service is found.

1. The service name of the found service is compared to the service name of the local service to determine if the device just picked up its own broadcast (which is valid).
2. The service type is checked, to verify it's a type of service your application can connect to.
3. The service name is checked to verify connection to the correct application.

Checking the service name isn't always necessary, and is only relevant if you
want to connect to a specific application. For instance, the application might
only want to connect to instances of itself running on other devices. However, if the
application wants to connect to a network printer, it's enough to see that the service type
is "_ipp._tcp".

After setting up the listener, call `https://developer.android.com/reference/android/net/nsd/NsdManager#discoverServices(java.lang.String, int, android.net.nsd.NsdManager.DiscoveryListener)`, passing in the service type
your application should look for, the discovery protocol to use, and the
listener you just created.

### Kotlin

```kotlin
nsdManager.discoverServices(SERVICE_TYPE, NsdManager.PROTOCOL_DNS_SD, discoveryListener)
```

### Java

```java
nsdManager.discoverServices(
        SERVICE_TYPE, NsdManager.PROTOCOL_DNS_SD, discoveryListener);
```

## Connect to services on the network

When your application finds a service on the network to connect to, it
must first determine the connection information for that service, using the
`https://developer.android.com/reference/android/net/nsd/NsdManager#resolveService(android.net.nsd.NsdServiceInfo, android.net.nsd.NsdManager.ResolveListener)` method.
Implement a `https://developer.android.com/reference/android/net/nsd/NsdManager.ResolveListener` to pass into this
method, and use it to get a `https://developer.android.com/reference/android/net/nsd/NsdServiceInfo` containing
the connection information.

### Kotlin

```kotlin
private val resolveListener = object : NsdManager.ResolveListener {

    override fun onResolveFailed(serviceInfo: NsdServiceInfo, errorCode: Int) {
        // Called when the resolve fails. Use the error code to debug.
        Log.e(TAG, "Resolve failed: $errorCode")
    }

    override fun onServiceResolved(serviceInfo: NsdServiceInfo) {
        Log.e(TAG, "Resolve Succeeded. $serviceInfo")

        if (serviceInfo.serviceName == mServiceName) {
            Log.d(TAG, "Same IP.")
            return
        }
        mService = serviceInfo
        val port: Int = serviceInfo.port
        val host: InetAddress = serviceInfo.host
    }
}
```

### Java

```java
public void initializeResolveListener() {
    resolveListener = new NsdManager.ResolveListener() {

        @Override
        public void onResolveFailed(NsdServiceInfo serviceInfo, int errorCode) {
            // Called when the resolve fails. Use the error code to debug.
            Log.e(TAG, "Resolve failed: " + errorCode);
        }

        @Override
        public void onServiceResolved(NsdServiceInfo serviceInfo) {
            Log.e(TAG, "Resolve Succeeded. " + serviceInfo);

            if (serviceInfo.getServiceName().equals(serviceName)) {
                Log.d(TAG, "Same IP.");
                return;
            }
            mService = serviceInfo;
            int port = mService.getPort();
            InetAddress host = mService.getHost();
        }
    };
}
```

Once the service is resolved, your application receives detailed
service information including an IP address and port number. This is everything
you need to create your own network connection to the service.

## Unregister your service on application close

It's important to enable and disable NSD
functionality as appropriate during the application's
lifecycle. Unregistering your application when it closes down helps prevent
other applications from thinking it's still active and attempting to connect to
it. Also, service discovery is an expensive operation, and should be stopped
when the parent Activity is paused, and re-enabled when the Activity is
resumed. Override the lifecycle methods of your main Activity and insert code
to start and stop service broadcast and discovery as appropriate.

### Kotlin

```kotlin
    // In your application's Activity

    override fun onPause() {
        nsdHelper?.tearDown()
        super.onPause()
    }

    override fun onResume() {
        super.onResume()
        nsdHelper?.apply {
            registerService(connection.localPort)
            discoverServices()
        }
    }

    override fun onDestroy() {
        nsdHelper?.tearDown()
        connection.tearDown()
        super.onDestroy()
    }

    // NsdHelper's tearDown method
    fun tearDown() {
        nsdManager.apply {
            unregisterService(registrationListener)
            stopServiceDiscovery(discoveryListener)
        }
    }
```

### Java

```java
    // In your application's Activity

    @Override
    protected void onPause() {
        if (nsdHelper != null) {
            nsdHelper.tearDown();
        }
        super.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (nsdHelper != null) {
            nsdHelper.registerService(connection.getLocalPort());
            nsdHelper.discoverServices();
        }
    }

    @Override
    protected void onDestroy() {
        nsdHelper.tearDown();
        connection.tearDown();
        super.onDestroy();
    }

    // NsdHelper's tearDown method
    public void tearDown() {
        nsdManager.unregisterService(registrationListener);
        nsdManager.stopServiceDiscovery(discoveryListener);
    }
```