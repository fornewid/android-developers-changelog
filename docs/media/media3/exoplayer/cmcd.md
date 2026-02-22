---
title: https://developer.android.com/media/media3/exoplayer/cmcd
url: https://developer.android.com/media/media3/exoplayer/cmcd
source: md.txt
---

Media player clients can transmit valuable information to Content Delivery
Networks (CDNs) with each object request. Transmitting that data can improve QoS
monitoring, adaptive traffic optimization, and delivery performance, ultimately
enhancing the consumer experience.

The implementation in ExoPlayer is based on the specification defined in
[CTA-5004](https://cdn.cta.tech/cta/media/media/resources/standards/pdfs/cta-5004-final.pdf).

## CMCD support in Exoplayer

CMCD support in ExoPlayer can only be enabled for adaptive streaming formats,
such as [DASH](https://developer.android.com/guide/topics/media/exoplayer/dash), [HLS](https://developer.android.com/guide/topics/media/exoplayer/hls), and [SmoothStreaming](https://developer.android.com/guide/topics/media/exoplayer/smoothstreaming).

## CMCD data keys

CMCD data keys are classified into four distinct types:

- **CMCD-Request**: keys whose values vary with each request.
- **CMCD-Object**: keys whose values vary with the object being requested.
- **CMCD-Status**: keys whose values don't vary with every request or object.
- **CMCD-Session**: keys whose values are expected to be invariant over the life of the session.

## Modes of transmitting data

CMCD data can be transmitted using one of two methods:

- As a custom HTTP request header, which is the **default** behaviour.
- As a HTTP query argument.

## Enable CMCD

To enable CMCD, you need to create an instance of `CmcdConfiguration.Factory`
and pass this to the `MediaSource.Factory` which is [used when building the
player](https://developer.android.com/guide/topics/media/exoplayer/media-sources#customizing-media-source-creation). You can either use the default `CmcdConfiguration.Factory` or provide
your own custom factory which is called each time an adaptive media source is
created for the given media item.

### Enable CMCD with default configuration factory

### Kotlin

```kotlin
// Create media source factory and set default cmcdConfigurationFactory.
val mediaSourceFactory =
  DefaultMediaSourceFactory(context)
    .setCmcdConfigurationFactory(CmcdConfiguration.Factory.DEFAULT)
```

### Java

```java
// Create media source factory and set default cmcdConfigurationFactory.
MediaSource.Factory mediaSourceFactory =
    new DefaultMediaSourceFactory(context)
        .setCmcdConfigurationFactory(CmcdConfiguration.Factory.DEFAULT);
```

> [!NOTE]
> **Note:** When using the default configuration, data is transmitted as custom HTTP request headers.

### Enable CMCD with custom configuration factory

### Kotlin

```kotlin
val cmcdConfigurationFactory =
  object : CmcdConfiguration.Factory {
    override fun createCmcdConfiguration(mediaItem: MediaItem): CmcdConfiguration {
      val cmcdRequestConfig =
        object : CmcdConfiguration.RequestConfig {
          override fun isKeyAllowed(key: String): Boolean {
            return key == "br" || key == "bl"
          }

          override fun getCustomData():
            ImmutableListMultimap<@CmcdConfiguration.HeaderKey String, String> {
            return ImmutableListMultimap.of(
              CmcdConfiguration.KEY_CMCD_OBJECT,
              "key1=stringValue",
            )
          }

          override fun getRequestedMaximumThroughputKbps(throughputKbps: Int): Int {
            return 5 * throughputKbps
          }
        }

      val sessionId = UUID.randomUUID().toString()
      val contentId = UUID.randomUUID().toString()

      return CmcdConfiguration(sessionId, contentId, cmcdRequestConfig, MODE_QUERY_PARAMETER)
    }
  }

// Create media source factory and set your custom cmcdConfigurationFactory.
val mediaSourceFactory =
  DefaultMediaSourceFactory(context).setCmcdConfigurationFactory(cmcdConfigurationFactory)
```

### Java

```java
CmcdConfiguration.Factory cmcdConfigurationFactory =
    mediaItem -> {
      CmcdConfiguration.RequestConfig cmcdRequestConfig =
          new CmcdConfiguration.RequestConfig() {
            @Override
            public boolean isKeyAllowed(String key) {
              return key.equals("br") || key.equals("bl");
            }

            @Override
            public ImmutableListMultimap<@HeaderKey String, String> getCustomData() {
              return ImmutableListMultimap.of(
                  CmcdConfiguration.KEY_CMCD_OBJECT, "key1=stringValue");
            }

            @Override
            public int getRequestedMaximumThroughputKbps(int throughputKbps) {
              return 5 * throughputKbps;
            }
          };

      String sessionId = UUID.randomUUID().toString();
      String contentId = UUID.randomUUID().toString();

      return new CmcdConfiguration(
          sessionId, contentId, cmcdRequestConfig, MODE_QUERY_PARAMETER);
    };

// Create media source factory and set your custom cmcdConfigurationFactory.
MediaSource.Factory mediaSourceFactory =
    new DefaultMediaSourceFactory(context)
        .setCmcdConfigurationFactory(cmcdConfigurationFactory);
```

> [!NOTE]
> **Note:** When utilising a custom configuration, you have the option to transmit data as custom request headers (`MODE_REQUEST_HEADER`) or as query parameters (`MODE_QUERY_PARAMETER`).

## CMCD data examples

These examples illustrate valid data combinations of data sent when fetching
media chunks:

- As custom HTTP request headers

         CMCD-Session:sid="6e2fb550-c457-11e9-bb97-0800200c9a66"

         CMCD-Request:mtp=25400 CMCD-Object:br=3200,d=4004,ot=v,tb=6000
         CMCD-Status:bs,rtp=15000
         CMCD-Session:sid="6e2fb550-c457-11e9-bb97-0800200c9a66"

- As HTTP query arguments

         ?CMCD=sid%3D%226e2fb550-c457-11e9-bb97-0800200c9a66%22

         ?CMCD=br%3D3200%2Cbs%2Cd%3D4004%2Cmtp%3D25400%2Cot%3Dv%2Crtp
         %3D15000%2Csid%3D%226e2fb550-c457-11e9-bb97-
         0800200c9a66%22%2Ctb%3D6000