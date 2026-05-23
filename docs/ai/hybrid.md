---
title: https://developer.android.com/ai/hybrid
url: https://developer.android.com/ai/hybrid
source: md.txt
---

Google provides an extensive selection of industry-leading AI models and APIs
for both cloud-based and on-device inference. Hybrid inference lets you to seamlessly balance AI workloads between the local device and the cloud, optimizing performance, cost, and availability.

Hybrid inference provides two primary advantages for your Android app:

- **Maximize reach**: Cloud models serve as a critical fallback when on-device models, such as Gemini Nano, are unavailable due to device hardware or OS constraints. This helps ensure that your AI features remain functional across the widest possible range of user devices.
- **Cost and offline capabilities**: On-device models help ensure that your AI features work seamlessly when the user is offline. Additionally, offloading routine tasks to the local device helps reduce cloud inference costs.

![Diagram showing the rationale for on-device inference versus cloud inference.](https://developer.android.com/static/ai/assets/images/hybrid_matrix.png) **Figure 1**: The respective benefits of on-device inference and cloud inference.

## Implementation options

You can implement hybrid inference using the following approaches:

### Firebase AI Logic Hybrid API

The [Firebase AI Logic Hybrid API](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started?api=dev) provides a single, unified interface for
splitting inference between cloud and on-device environments.

It includes a `onDeviceConfig` parameter providing simple controls to define the
[inference mode](https://firebase.google.com/docs/ai-logic/hybrid/android/configuration-options?api=dev#inference-modes) and manage the routing:

- `PREFER_ON_DEVICE`: attempt to use the on-device model, automatically falling back to the cloud-hosted model if the on-device model is unavailable or unsupported for the request.
- `PREFER_IN_CLOUD`: attempts to use the cloud-hosted model when the device is online and the model is available, falling back to the on-device model only if the device is offline.
- `ONLY_ON_DEVICE`: attempts to use the on-device model, but throws an exception if it is unavailable or unsupported for the request.
- `ONLY_IN_CLOUD`: attempts to use the cloud-hosted model when the device is online and the model is available, throwing an exception in all other cases.

    val model = Firebase.ai(backend = GenerativeBackend.googleAI())
        .generativeModel(
            modelName = "gemini-2.5-flash",
            onDeviceConfig = OnDeviceConfig(mode = InferenceMode.PREFER_ON_DEVICE)
        )


    val response = model.generateContent("Write a story about a green robot.")
    print(response.text)

For implementation details, review the [Firebase documentation](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started?api=dev) and explore
the [Hybrid AI sample in the AI catalog](https://github.com/android/ai-samples/tree/main/samples/gemini-hybrid).

### Custom routing

If your app has specific business or UX requirements, you can also implement
custom routing logic. This lets you dynamically determine the inference path
based on real-time factors, such as:

- Network latency
- Device system health (for example battery levels and processor load)
- User query complexity

This custom hybrid inference approach is used by leading apps that implemented
their own custom routing to deliver reliable AI experiences, including:

- [**GBoard**](https://blog.google/products-and-platforms/platforms/android/new-android-features-september-2025/):
  Gboard uses custom hybrid inference to power the writing tools such as
  proofread and rewrite.

- [**Kakao Mobility**](https://developer.android.com/blog/posts/kakao-mobility-uses-gemini-nano-on-device-to-reduce-costs-and-boost-call-conversion-by-45):
  Kakao Mobility built an Entity Extraction tool using custom hybrid inference
  for their parcel delivery service that automatically extracts recipient names,
  addresses, and phone numbers from natural language messages to streamline
  order forms.