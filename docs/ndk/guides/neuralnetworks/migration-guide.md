---
title: https://developer.android.com/ndk/guides/neuralnetworks/migration-guide
url: https://developer.android.com/ndk/guides/neuralnetworks/migration-guide
source: md.txt
---

# NNAPI Migration Guide

The Neural Networks API (NNAPI) is deprecated. It was[introduced in Android 8.1](https://developer.android.com/about/versions/oreo/android-8.1#nnapi)to provide a unified interface for hardware accelerated inference for on-device machine learning, and deprecated in Android 15.

After NNAPI's release, the field of on-device machine learning (ODML) advanced rapidly. Breakthroughs such as transformer and diffusion models, along with the high rate of innovation in the field meant that developers needed tools and infrastructure that update frequently.

To meet those needs, Google developed[TensorFlow Lite in Play Services](https://www.tensorflow.org/lite/android/play_services), providing an updatable TensorFlow runtime for custom on-device ML models, and[AICore](https://developer.android.com/ml/aicore), which provide GenAI foundation models like Gemini Nano directly on Android devices. To provide greater clarity on the recommended paths for production ML on Android, NNAPI (Neural Networks API) was deprecated.

To migrate from NNAPI, see the instructions for[TensorFlow Lite in Google Play Services](https://www.tensorflow.org/lite/android/play_services)and optionally[TFLite GPU delegate](https://www.tensorflow.org/lite/android/delegates/gpu)for hardware acceleration.