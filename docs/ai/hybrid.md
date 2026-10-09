---
title: https://developer.android.com/ai/hybrid
url: https://developer.android.com/ai/hybrid
source: md.txt
---

Google provides an extensive selection of industry-leading AI models and APIs
for both cloud-based and on-device inference. Hybrid inference lets you
seamlessly balance AI workloads between the local device and the cloud,
optimizing performance, cost, and availability.

Hybrid inference provides two primary advantages for your Android app:

- **Maximize reach**: Cloud models serve as a critical fallback when on-device models, such as Gemini Nano, are unavailable due to device hardware or OS constraints. This helps ensure that your AI features remain functional across the widest possible range of user devices.
- **Cost and offline capabilities**: On-device models help ensure that your AI features work seamlessly when the user is offline. Additionally, offloading routine tasks to the local device helps reduce cloud inference costs.

Here are the benefits of on-device inference and cloud inference, respectively:

| On-device inference | Cloud inference |
|---|---|
| **Available offline** | **Compatible with any device** |
| **No inference cost** | **Advanced model capabilities** |

## Implementation options

You can implement hybrid inference using the following approaches:

- [Firebase AI Logic Hybrid API](https://developer.android.com/ai/hybrid#firebase-hybrid)
- [Custom routing](https://developer.android.com/ai/hybrid#custom-routing)

### Firebase AI Logic Hybrid API

The [Firebase AI Logic Hybrid API](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started) provides a single, unified interface for
routing inference between cloud and on-device models.

- **Automatic switching**: You can configure your app to run AI tasks on-device whenever possible. This means your app's feature works offline, has enhanced privacy, and incurs no cloud inference cost. If the on-device model isn't available, the SDK can automatically route the request to the cloud-hosted Gemini model.
- **Protection against abuse** : Directly calling cloud APIs from a mobile app can risk exposing credentials and leading to unwanted charges. However, when you use Firebase AI Logic, you also enforce [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check) which can help prevent abuse by verifying that only your genuine, untampered app can access the cloud Gemini API.
- **Spending limits** : When routing requests to cloud-hosted models, you can configure [spend caps](https://firebase.google.com/docs/projects/billing/spend-caps) to help you protect your cloud budget and avoid unexpected charges.

In your app, you define the `onDeviceConfig` parameter to control the
[inference mode](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options#inference-modes) and manage the routing:

- `PREFER_ON_DEVICE`: Attempts to use the on-device model; automatically falls
  back to the cloud-hosted model if the on-device model is unavailable or
  unsupported for the request.

- `PREFER_IN_CLOUD`: Attempts to use the cloud-hosted model when the device is
  online and the model is available; falls back to the on-device model only if
  the device is offline.

- `ONLY_ON_DEVICE`: Attempts to use the on-device model; throws an exception if
  the on-device model is unavailable or unsupported for the request.

- `ONLY_IN_CLOUD`: Attempts to use the cloud-hosted model when the device is
  online and the model is available; throws an exception in all other cases.


```kotlin
val model = Firebase.ai(backend = GenerativeBackend.Companion.googleAI())
    .generativeModel(
        modelName = "gemini-3.5-flash",
        onDeviceConfig = OnDeviceConfig(mode = InferenceMode.Companion.PREFER_ON_DEVICE)
    )

val response = model.generateContent("Write a story about a green robot.")
print(response.text)
```

<br />

For implementation details, review the [Firebase documentation](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started) and explore
the [Hybrid AI sample in the AI catalog](https://github.com/android/ai-samples/tree/main/samples/gemini-hybrid).

Transitioning workloads to the cloud can expose cloud API endpoints. When you
use Firebase AI Logic, you can securely access cloud-based Gemini models
directly from your client-side apps by enforcing [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check), which
helps protect cloud-based inference from unauthorized access and billing abuse.
This helps keep your hybrid fallback mechanism both available and secure.

### Custom routing

If your app has specific business or UX requirements, you can also implement
custom routing logic. This lets you dynamically determine the inference path
based on real-time factors, such as:

- Network latency
- Device system health (for example battery levels and processor load)
- User query complexity

This custom hybrid inference approach is used by leading apps that implemented
their own custom routing to deliver reliable AI experiences, including:

- [GBoard](https://blog.google/products-and-platforms/platforms/android/new-android-features-september-2025/):
  Gboard uses custom hybrid inference to power the writing tools such as
  proofread and rewrite.

- [Kakao Mobility](https://developer.android.com/blog/posts/kakao-mobility-uses-gemini-nano-on-device-to-reduce-costs-and-boost-call-conversion-by-45):
  Kakao Mobility built an Entity Extraction tool using custom hybrid inference
  for their parcel delivery service that automatically extracts recipient names,
  addresses, and phone numbers from natural language messages to streamline
  order forms.