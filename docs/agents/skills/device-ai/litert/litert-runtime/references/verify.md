---
title: https://developer.android.com/agents/skills/device-ai/litert/litert-runtime/references/verify
url: https://developer.android.com/agents/skills/device-ai/litert/litert-runtime/references/verify
source: md.txt
---

## Reference first

Keep the output of one fixed input from the source model in its own framework,
or from the same `.tflite` file on the workstation using the Python package
`ai-edge-litert` (using the same `CompiledModel` API:
`CompiledModel.from_file(path)`, then write, run, and read). The `qwen3_tts`
recipe in `litert-samples` ships such source-model dumps as `dump_*_ref.py`.
This output serves as the ground truth for every run on a device that runs
Android.

## Device CPU, then the GPU

Run the fixed input with `Accelerator.CPU` first and compare with the reference;
a difference here is in the model file or preprocessing, not in the device.

Next, run `Accelerator.GPU`. First check that the model runs on the GPU: after
the CPU fallback of Step 3, `UiState.accelerator` is `CPU` (the button reads
`Run (CPU)`), and the following comparison would compare the CPU with itself.
Logcat names the delegate that took the model's operators: `Replacing <n> out of
<n> node(s) with delegate (LITERT_CL)` for the GPU, `(TfLiteXNNPackDelegate)`
for the CPU. On the Google Play services runtime, `Error loading LiteRT GPU
accelerator module` means that Google Play services doesn't have its GPU module
on the device yet, and the model runs on the CPU. Then compare in two ways:

1. **Numbers**: Compute maximum absolute difference and Pearson correlation against the reference dump.
2. **Task result**: Check task-level agreement (top-1 argmax, segmentation mask, or output text). Because the GPU computes in FP16, the least significant digits move slightly, whereas the task result shouldn't change.

When the `Accelerator.CPU` run differs and the app builds the input from a
picture, compare the array the app writes with the input that produced the
reference. Check its length against the input element count (`writeFloat` writes
a shorter array without an error, Step
2 of the skill),
the bitmap's config (by default `ImageDecoder` returns `HARDWARE` bitmaps, which
`getPixels` can't read; copy to `ARGB_8888` first, Step
4 of the skill),
then the input dimensions, mean, standard deviation, channel order, and tensor
layout.

## Diagnostic indicators

- **First inference slow**: GPU shader compilation runs during the first execution. The helper constructor's warm-up call absorbs this cost; never include the first run in timing metrics.
- **Timing GPU execution** : On the GPU, measure `model.run` and `readFloat` together, because the output buffer readback is where the app waits for the GPU to finish.

## Device-only failures

- **`CompiledModel.create` with `Accelerator.GPU` throws `Failed to compile
  model`** : Caused by an operator the GPU doesn't support (Logcat logs `Following operations are not supported by GPU delegate`). Run the model on `Accelerator.CPU`, or re-export the model without that operator.
- **`NaN` or corrupted values appear only on `Accelerator.GPU`** : Caused by an FP16 range overflow in the model. Run the model on `Accelerator.CPU`, or re-export it with an FP16-safe graph rewrite.
- **Process terminates while loading an unquantized FP32 model exceeding 100
  MB**: Insufficient device RAM. Quantize or split the model before loading.

## Record

Record the device model, LiteRT version, accelerator, maximum absolute
difference, and task result (one row per device in the app's `README`). When the
`Accelerator.CPU` run differs from the reference output, inspect the model
itself (such as the converted or quantized model accuracy, GPU operator
residency, or device-only failures such as FP16 range overflows).