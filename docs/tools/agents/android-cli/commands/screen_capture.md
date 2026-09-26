---
title: https://developer.android.com/tools/agents/android-cli/commands/screen_capture
url: https://developer.android.com/tools/agents/android-cli/commands/screen_capture
source: md.txt
---

Outputs the device screen to a PNG.

## Usage

    android screen capture [-ah] [--debug] [--device=PARAM] [--distance=PARAM] [--edge-thresh-strong=PARAM] [--edge-thresh-weak=PARAM] [--features=PARAM] [--min-area=PARAM] [--min-nested-area=PARAM] [--min-rect=PARAM] [--min-round=PARAM] [--output=PARAM] [--threshold=PARAM]

## Options

- `-a,--annotate` - Detects and labels UI elements on the screenshot with numbered bounding boxes (`#1`, `#2`, and so on). This lets AI agents and scripts reference on-screen UI elements by label number instead of manually calculating pixel coordinates.
- `--debug` - Outputs intermediate feature detection steps for parameter tuning.
- `--device=PARAM` - The device serial number.
- `--distance=PARAM` - Used with `--annotate`. Distance metric for combining detected shapes into UI features (`MIN_EUCLIDEAN` or `MIN_ANISOTROPIC`). `MIN_ANISOTROPIC` weights vertical separation on the y-axis more heavily than horizontal separation on the x-axis (default: `MIN_EUCLIDEAN`).
- `--edge-thresh-strong=PARAM` - Used with `--annotate`. Strong threshold (`0` to `1`) for edge detection. Lower this value if barely detectable edges are being ignored, or raise it if detection is too noisy (default: `0.1`).
- `--edge-thresh-weak=PARAM` - Used with `--annotate`. Weak threshold (`0` to `1`) for edge detection. Lower this value if barely detectable edges are being ignored, or raise it if detection is too noisy (default: `0.05`).
- `--features=PARAM` - Used with `--annotate`. Algorithm used to group detected shapes into UI features (`GREEDY` or `FH`). `GREEDY` combines shapes closer than `--threshold` distance into a single feature. `FH` uses `--threshold` as the segmentation scale parameter, where higher values produce fewer, larger features and lower values produce more, smaller features (default: `FH`).
- `-h,--help` - Shows the help message for the specified command.
- `--min-area=PARAM` - Used with `--annotate`. Minimum shape area in `dp²` before feature detection. Shapes smaller than this threshold are ignored (default: `5.0`).
- `--min-nested-area=PARAM` - Used with `--annotate`. Minimum parent feature area in `dp²` required to keep nested child features. Raise this value if small details inside icons are being labeled as separate elements (default: `3600.0`).
- `--min-rect=PARAM` - Used with `--annotate`. Minimum ratio of a shape's area to its axis-aligned bounding box area. Shapes below both `--min-rect` and `--min-round` are ignored (default: `0.2`).
- `--min-round=PARAM` - Used with `--annotate`. Minimum shape roundness (`4 * PI * area / perimeter^2`, where `1.0` is a perfect circle). Shapes below both `--min-rect` and `--min-round` are ignored (default: `0.2`).
- `-o,--output=PARAM` - Writes the screenshot to the specified file or directory.
- `--threshold=PARAM` - Used with `--annotate`. Grouping threshold passed to the algorithm specified in `--features` (default: `15`).

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android screen capture` captures a PNG screenshot of the connected Android device or emulator.

If `-o, --output` is omitted, the raw PNG image bytes are written to standard output.

### Annotate UI elements (`-a, --annotate`)

Pass `-a, --annotate` to detect UI elements on the screen and overlay numbered bounding boxes (`#1`, `#2`, and so on) around each detected element. The output PNG also embeds bounding-box metadata so [`android screen resolve`](https://developer.android.com/tools/agents/android-cli/commands/screen_resolve) can translate `#N` labels into screen `(x, y)` coordinates.

You can fine-tune detection sensitivity using options such as `--edge-thresh-weak`, `--edge-thresh-strong`, `--min-area`, `--min-rect`, `--min-round`, `--min-nested-area`, `--distance`, `--features`, and `--threshold`.

### Examples

Save a screenshot of the connected device to `ui.png`:

    android screen capture --output=ui.png

Capture an annotated screenshot with labeled UI bounding boxes for visual targeting:

    android screen capture --annotate --output=ui_annotated.png