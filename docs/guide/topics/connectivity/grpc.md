---
title: https://developer.android.com/guide/topics/connectivity/grpc
url: https://developer.android.com/guide/topics/connectivity/grpc
source: md.txt
---

# Build client-server applications with gRPC

gRPC is a modern, open-source, high-performance RPC framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health-checking, and authentication. It is also applicable in the last mile of distributed computing to connect devices, mobile applications, and browsers to backend services. You can find documentation on gRPC's official website and get support from open source communities. This guide points you to solutions for building Android apps using gRPC.

[grpc.io](https://grpc.io)is the official website for the gRPC project. To learn more about how gRPC works, see[What is gRPC?](https://grpc.io/docs/guides/)and[gRPC Concepts](https://grpc.io/docs/guides/concepts/). To learn how to use gRPC in an Android app, see the Hello World example in[gRPC Android Java Quickstart](https://grpc.io/docs/quickstart/android/). You can also find several other gRPC Android examples[on GitHub](https://github.com/grpc/grpc-java/tree/v1.24.0/examples/android).

## Features

**Procedure call makes it simple**
:   Because it's RPC, the programming model is procedure calls: the networking aspect of the technology is abstracted away from application code, making it look almost as if it was a normal in-process function call. Your client-server interaction will not be constrained by the semantics of HTTP resource methods (such as GET, PUT, POST, and DELETE). Compared to REST APIs, your implementation looks more natural, without the need for handling HTTP protocol metadata.

**Efficient network transmission with HTTP/2**
:   Transmitting data from mobile devices to a backend server can be a very resource-intensive process. Using the standard HTTP/1.1 protocol, frequent connections from a mobile device to a cloud service can drain the battery, increase latency, and block other apps from connecting. By default, gRPC runs on top of HTTP/2, which introduces bi-directional streaming, flow control, header compression, and the ability to multiplex requests over a single TCP/IP connection. The result is that gRPC can reduce resource usage, resulting in lower response times between your app and services running in the cloud, reduced network usage, and longer battery life for client running on mobile devices.

Built-in streaming data exchange support
:   gRPC was designed with HTTP/2's support for full-duplex bidirectional streaming in mind from the outset. Streaming allows a request and response to have an arbitrarily large size, such as operations that require uploading or downloading a large amount of information. With streaming, client and server can read and write messages simultaneously and subscribe to each other without tracking resource IDs. This makes your app implementation more flexible.

**Seamless integration with Protocol Buffer**
:   gRPC uses Protocol Buffers (Protobuf) as its serialization/deserialization method with optimized-for-Android codegen plugin ([Protobuf Java Lite](https://github.com/protocolbuffers/protobuf/blob/v3.9.0/java/lite.md)). Compared to text-based format (such as JSON), Protobuf offers more efficient data exchanging in terms of marshaling speed and code size, which makes it more suitable to be used in mobile environments. Also Protobuf's concise message/service definition syntax makes it much easier to define data model and application protocols for your app.

## Usage overview

Following the[gRPC Basics - Android Java](https://grpc.io/docs/tutorials/basic/android/)tutorial, using gRPC for Android apps involves four steps:

- Define RPC services with protocol buffers and generate the gRPC client interfaces.
- Build a Channel that serves as the medium for RPC calls between client and server.
- Create a client Stub as the entry point for initiating RPC calls from client side.
- Make RPC calls to remote server as you would when performing local procedure calls.

For demonstration purposes, bytes are transmitted in plain text in the provided example. However, your app should always encrypt network data in production. gRPC provides SSL/TLS encryption support as well as OAuth token exchanging (OAuth2 with Google services) for authentication. For more details, see[TLS on Android](https://github.com/grpc/grpc-java/blob/v1.24.0/SECURITY.md#tls-on-android)and[Using OAuth2](https://github.com/grpc/grpc-java/blob/v1.24.0/SECURITY.md#using-oauth2).
| **Note:** If you are using Gradle as the build tool for your app, the Protobuf Gradle plugin is a handy tool for automating the process of generating and building gRPC Java code into your app. For more information, see[Protobuf Plugin for Gradle](https://github.com/google/protobuf-gradle-plugin#protobuf-plugin-for-gradle-).

## Transport

gRPC provides two choices of Transport implementations for Android clients: OkHttp and Cronet.
| **Note:** Creating channels with transport-specific channel builders (such as[`OkHttpChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/okhttp/src/main/java/io/grpc/okhttp/OkHttpChannelBuilder.java#L57)or[`CronetChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/cronet/src/main/java/io/grpc/cronet/CronetChannelBuilder.java#L49)) is for more advanced usage. If you build the channel with[`ManagedChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/api/src/main/java/io/grpc/ManagedChannelBuilder.java#L31), the class loader will load the plain[`OkHttpChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/okhttp/src/main/java/io/grpc/okhttp/OkHttpChannelBuilder.java#L57)as the default implementation at runtime. Starting from gRPC's 1.24 release, we recommend using[`AndroidChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/android/src/main/java/io/grpc/android/AndroidChannelBuilder.java#L54), which is similar, but with some Android-specific optimizations.

**Choose a transport (advanced)**

-

  OkHttp
  :   OkHttp is a light-weight networking stack designed for use on mobile. It is gRPC's default transport for running in Android environment. To use OkHttp as gRPC transport for your app, construct the channel with[`AndroidChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/android/src/main/java/io/grpc/android/AndroidChannelBuilder.java#L54), which wraps[`OkHttpChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/okhttp/src/main/java/io/grpc/okhttp/OkHttpChannelBuilder.java#L57)and will register a network monitor with the Android OS to quickly respond to network changes. An example usage can be found in[gRPC-Java AndroidChannelBuilder](https://github.com/grpc/grpc-java/blob/v1.24.0/documentation/android-channel-builder.md#example-usage).
-

  Cronet (experimental)
  :   Cronet is Chromium's Networking stack packaged as a library for mobile. It offers robust networking support with state-of-the-art QUIC protocol, which can be especially effective in unreliable network environments. To learn more details about Cronet, see[Perform network operations using Cronet](https://developer.android.com/guide/topics/connectivity/cronet). To use Cronet as gRPC transport for your app, construct the channel with[`CronetChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/cronet/src/main/java/io/grpc/cronet/CronetChannelBuilder.java#L49). An example usage is provided in[gRPC-Java Cronet Transport](https://github.com/grpc/grpc-java/tree/v1.24.0/cronet#grpc-cronet-transport).

| **Note:** Cronet's bidirectional streaming feature is still experimental. Therefore,[`CronetChannelBuilder`](https://github.com/grpc/grpc-java/blob/v1.24.0/cronet/src/main/java/io/grpc/cronet/CronetChannelBuilder.java#L49)is marked as an experimental API.

Generally speaking, we recommend apps targeting recent SDK versions use Cronet as it offers a more-powerful network stack. The downside of using Cronet is the APK size increase, as adding the binary Cronet dependency will add \>1MB to the app size, versus \~100KB for OkHttp. Starting with GMSCore v.10, an up-to-date copy of Cronet can be loaded from Google Play Services. The APK size may no longer be a concern, although devices without the latest GMSCore installed may still prefer using OkHttp.
| **Note:** When loading Cronet from Google Play services, call[`CronetProviderInstaller.installProvider(Context)`](https://developers.google.com/android/reference/com/google/android/gms/net/CronetProviderInstaller)before creating[`CronetEngine/ExperimentalCronetEngine`](https://developer.android.com/guide/topics/connectivity/cronet/reference/org/chromium/net/CronetEngine)objects to prevent unexpected exceptions from being thrown due to errors like devices requiring an updated version of Google Play services.