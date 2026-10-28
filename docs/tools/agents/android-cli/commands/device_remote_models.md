---
title: android device remote models  |  Android Studio  |  Android Developers
url: https://developer.android.com/tools/agents/android-cli/commands/device_remote_models
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Agent tools and resources](https://developer.android.com/tools/agents)

# android device remote models Stay organized with collections Save and categorize content based on your preferences.





Lists available remote device models.

## Usage

```
android device remote models [-h]
```

## Options

* `-h,--help` - Shows the help message for the specified command.

`remote` options:

* `--project=PARAM` - The Google Cloud project ID.

`android` options:

* `--sdk=PARAM` - Path to the Android SDK.
* `-v,--verbose` - Enable verbose output for troubleshooting.
* `-V,--version` - Print version information and exit.

## Description

`android device remote models` lists the physical devices that you can reserve,
grouped by manufacturer and model. Each model shows the builds that are
available as `<codename>/<api>`, which is the value that you pass to
`android device remote create`.

`--project` is optional. When it's set, the list shows the devices available to
that project.

### Examples

List the available devices:

```
android device remote models
```

List the devices available to the `my-project` project:

```
android device remote models --project=my-project
```