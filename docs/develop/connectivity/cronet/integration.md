---
title: https://developer.android.com/develop/connectivity/cronet/integration
url: https://developer.android.com/develop/connectivity/cronet/integration
source: md.txt
---

Cronet is a powerful and flexible tool that can be used in combination with
other libraries, providing the best of utility, simplicity, and performance.

## ExoPlayer

ExoPlayer natively supports Cronet through its Cronet extension. Cronet is used
by some of the world's biggest streaming applications, including YouTube.

For more details, visit the [ExoPlayer site](https://exoplayer.dev/network-stacks.html#cronet).

## gRPC

Cronet can be used as the transport layer for gRPC on Android. This lets your
Android app make RPCs using the same networking stack as used in the Chrome
browser.

For more details, visit the [gRPC repository](https://android.googlesource.com/platform/external/grpc-grpc-java/+/refs/heads/master/cronet/).

## OkHttp

The Cronet team provides a library that enables
[OkHttp](https://square.github.io/okhttp/) users to use Cronet as their
transport layer, benefiting from features like QUIC/HTTP3 support or connection
migration. The library can also be used with other OkHttp-based libraries
such as [Retrofit](https://square.github.io/retrofit/),
[Coil](https://coil-kt.github.io/coil/),
and [others](https://square.github.io/okhttp/works_with_okhttp/).

For more details, visit the
[Cronet Transport for OkHttp repository](https://github.com/google/cronet-transport-for-okhttp).

## Glide

Cronet is a good default choice with Glide and will provide better performance
than Glide's default integration with the standard Android networking stack.

For more details, visit the [Glide site](https://bumptech.github.io/glide/int/cronet.html).

## Dart

Cronet can be used in Dart as a drop-in replacement for the `dart:io` package.

For more details, visit the
[Cronet Dart bindings repository](https://github.com/google/cronet.dart)
and [read a blogpost](https://unsuitable001.medium.com/package-cronet-an-http-dart-flutter-package-with-dart-ffi-84f9b69c8a24)
about how it came to existence!