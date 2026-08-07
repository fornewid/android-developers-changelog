---
title: https://developer.android.com/privacy-and-security/encrypted-client-hello
url: https://developer.android.com/privacy-and-security/encrypted-client-hello
source: md.txt
---

Encrypted Client Hello (ECH) is a TLS extension that encrypts the Server Name Indication (SNI) field in the client's handshake message. In Android 17 (API level 37) and higher, ECH is supported by default. ECH helps keep users' web traffic private by preventing network intermediaries from seeing the hostnames an app connects to.

## For App Developers

To adopt ECH in your application:

1. **Check your networking library for ECH support**: Ensure you are using a library version that supports ECH on Android. Support is coming soon in OkHttp and HttpEngine.
2. **Configure Network Security Config** : By default, ECH is enabled for all domains if your library supports it. If you need to disable or enforce ECH, configure the `domainEncryption` element in your [Network Security Config](https://developer.android.com/privacy-and-security/security-config#EncryptedClientHelloSummary).
3. **Update the target SDK level**: ECH is only available on Android 17 (API level 37) and higher.

## For Library Developers

If you're developing a custom HTTP networking library or extending an existing one, you should implement ECH support by interacting with the platform APIs.

### Check domain encryption policy

Before querying ECH configurations or initiating connections, check the app's [domain encryption policy](https://developer.android.com/privacy-and-security/security-config#EncryptedClientHelloSummary) by calling [`NetworkSecurityPolicy.getDomainEncryptionMode`](https://developer.android.com/reference/android/security/NetworkSecurityPolicy#getDomainEncryptionMode(java.lang.String)).

Depending on the returned mode, handle ECH as follows:

- **`DOMAIN_ENCRYPTION_MODE_DISABLED`** and **`DOMAIN_ENCRYPTION_MODE_UNKNOWN`**: Don't fetch ECH configurations or attempt ECH.
- **`DOMAIN_ENCRYPTION_MODE_ENABLED`** and **`DOMAIN_ENCRYPTION_MODE_OPPORTUNISTIC`**: Enforce ECH. Retrieve ECH configurations and use ECH if the server supports it. If the server doesn't support ECH, enable ECH GREASE.

> [!WARNING]
> **Deprecated:** Opportunistic mode is deprecated as of Android 17.1 (API level 37.1 ), and does not need to be explicitly handled past this API level.

> [!TIP]
> **Tip:** [ECH GREASE](https://www.rfc-editor.org/rfc/rfc9849.html#name-grease-psk) is automatically handled by the default platform SSL implementation (SSLSocketFactory) if your library uses this for TLS. Otherwise, it must be handled by the library itself.

### Retrieve ECH configurations

To connect with ECH, you must resolve the server's HTTPS DNS record containing the ECH configurations. When apps are using the system DNS, this data can be retrieved using one of two methods:

#### Method 1: Using the high-level `DnsResolver.query` API

If your library doesn't require custom DNS resolution mechanisms, you can use the platform's high-level [`DnsResolver.query`](https://developer.android.com/reference/android/net/DnsResolver#query(android.net.Network,%20java.lang.String,%20int,%20java.util.concurrent.Executor,%20int,%20android.os.CancellationSignal,%20android.net.DnsResolver.Callback%3Candroid.net.dns.HttpsEndpoint%3E)) API. This API makes parallel queries for the A/AAAA/HTTPS records and combines the results into an [`HttpsEndpoint`](https://developer.android.com/reference/android/net/dns/HttpsEndpoint).

### Kotlin

    val resolver = DnsResolver(context, looper)
    resolver.query(network, hostname, DnsResolver.TYPE_HTTPS, executor,
        DnsResolver.HTTPS_QUERY_WAIT_AUTO, cancellationSignal,
        object : DnsResolver.Callback<HttpsEndpoint> {
            override fun onAnswer(answer: HttpsEndpoint, rcode: Int) {
                val record = answer.httpsRecords.firstOrNull() ?: return
                val echConfigList = record.echConfigList ?: return
                establishEchConnection(echConfigList)
            }
            override fun onError(error: DnsResolver.DnsException) { /* Handle error */ }
        })

### Java

    DnsResolver resolver = new DnsResolver(context, looper);
    resolver.query(network, hostname, DnsResolver.TYPE_HTTPS, executor,
        DnsResolver.HTTPS_QUERY_WAIT_AUTO, cancellationSignal,
        new DnsResolver.Callback<HttpsEndpoint>() {
            @Override
            public void onAnswer(HttpsEndpoint answer, int rcode) {
                HttpsRecord record = answer.getHttpsRecords().stream().findFirst().orElse(null);
                if (record == null) return;
                EchConfigList echConfigList = record.getEchConfigList();
                if (echConfigList == null) return;
                establishEchConnection(echConfigList);
            }

            @Override
            public void onError(DnsResolver.DnsException error) { /* Handle error */ }
        });

#### Method 2: Using `getAllByName` and `DnsResolver.rawQuery`

For libraries that manage their own socket connections and DNS resolution pipelines, you may prefer to resolve IP addresses using standard APIs while fetching the HTTPS record separately:

1. Resolve A/AAAA records using [`InetAddress.getAllByName`](https://developer.android.com/reference/java/net/InetAddress#getAllByName(java.lang.String)) for the default network or [`Network.getAllByName`](https://developer.android.com/reference/android/net/Network#getAllByName(java.lang.String)).
2. Retrieve the raw HTTPS record in parallel using [`DnsResolver.rawQuery`](https://developer.android.com/reference/android/net/DnsResolver#rawQuery(android.net.Network,%20byte%5B%5D,%20int,%20java.util.concurrent.Executor,%20android.os.CancellationSignal,%20android.net.DnsResolver.Callback%3Cbyte%5B%5D%3E)). Specify [`DnsResolver.TYPE_HTTPS`](https://developer.android.com/reference/android/net/DnsResolver#TYPE_HTTPS) as the query type.

##### Developer responsibility and edge cases

If you choose Method 2, your library has additional responsibilities and edge cases to consider.

- **DNS Record Parsing** : You must parse the raw byte payload of the DNS response from `rawQuery` to extract the `EchConfigList`.
- **Handling Record Mismatches**: You must handle inconsistencies between the A/AAAA and HTTPS queries.
- **Race Conditions**: You must synchronize the results of the parallel DNS lookups. If one query resolves before the other or if the HTTPS query times out, you must fall back appropriately (for example, by attempting a standard TLS connection without ECH if the HTTPS query fails, or using ECH GREASE if it's enabled by policy).

### Configure TLS

Once the library has retrieved the ECH configuration list ([`EchConfigList`](https://developer.android.com/reference/android/net/ssl/EchConfigList)) from the `HttpsRecord`, pass this list in using either the [`SSLSockets`](https://developer.android.com/reference/android/net/ssl/SSLSockets#setEchConfigList(javax.net.ssl.SSLSocket,%20android.net.ssl.EchConfigList)) or [`SSLEngines`](https://developer.android.com/reference/android/net/ssl/SSLEngines#setEchConfigList(javax.net.ssl.SSLEngine,%20android.net.ssl.EchConfigList)) utility APIs before starting the TLS handshake.

### Kotlin

    fun establishEchConnection(echConfigList: EchConfigList) {
        val socket = sslSocketFactory.createSocket(ipAddress, port) as SSLSocket
        SSLSockets.setEchConfigList(socket, echConfigList)
        socket.startHandshake()
    }

### Java

    public void establishEchConnection(EchConfigList echConfigList)
        throws IOException {
        SSLSocket socket =
            (SSLSocket) sslSocketFactory.createSocket(ipAddress, port);
        SSLSockets.setEchConfigList(socket, echConfigList);
        socket.startHandshake();
    }

### Handle retry flow

If the server's ECH configurations have become out of sync, the handshake fails with an `EchConfigMismatchException` (a subclass of `javax.net.ssl.SSLException`). The server may include updated ECH configurations in its rejection, which should be used to establish a new connection. If a retry is not attempted despite the server providing valid retry configurations, the library must report an error to the calling application.

To handle ECH retries, catch the exception and perform these steps:

1. Call [`EchConfigMismatchException.getPublicHostname`](https://developer.android.com/reference/android/net/ssl/EchConfigMismatchException#getPublicHostname()) on the exception.
2. Verify the returned public hostname using your [`HostnameVerifier`](https://developer.android.com/reference/javax/net/ssl/HostnameVerifier). If it's `null`, abort the connection.
3. If hostname verification succeeds, check for updated configurations using [`EchConfigMismatchException.getRetryConfigList`](https://developer.android.com/reference/android/net/ssl/EchConfigMismatchException#getRetryConfigList()).
4. If updated configurations are available, retry the connection with the new [`EchConfigList`](https://developer.android.com/reference/android/net/ssl/EchConfigList).

### Kotlin

    try {
        socket.startHandshake()
    } catch (e: EchConfigMismatchException) {
        val publicName = e.publicHostname ?: throw e
        if (hostnameVerifier.verify(publicName, socket.session)) {
            val retryConfigList = e.retryConfigList
            if (retryConfigList != null) {
                retryConnection(retryConfigList)
            }
        } else {
            throw e // Hostname mismatch
        }
    }

### Java

    try {
        socket.startHandshake();
    } catch (EchConfigMismatchException e) {
        String publicName = e.getPublicHostname();
        if (publicName == null) {
            throw e;
        }
        if (hostnameVerifier.verify(publicName, socket.getSession())) {
            EchConfigList retryConfigList = e.getRetryConfigList();
            if (retryConfigList != null) {
                retryConnection(retryConfigList);
            }
        } else {
            throw e; // Hostname mismatch
        }
    }

See more details about the retry flow in [RFC 9849](https://www.rfc-editor.org/rfc/rfc9849.html#name-handshaking-with-clienthello), in particular [why it's necessary to authenticate for the public name](https://www.rfc-editor.org/rfc/rfc9849.html#name-authenticating-for-the-publ).