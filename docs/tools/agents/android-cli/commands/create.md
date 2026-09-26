---
title: https://developer.android.com/tools/agents/android-cli/commands/create
url: https://developer.android.com/tools/agents/android-cli/commands/create
source: md.txt
---

Creates a new Android project from available templates. You can specify the project name, output directory, `minSdk` value, and dry-run execution.

## Usage

    android create [-h] [--application-id=PARAM] [--list] [--min-sdk=PARAM] [--name=PARAM] [--namespace=PARAM] [--output=PARAM] [<template-name>]

## Options

- `--application-id=PARAM` - The app ID for the app, for example `com.example.myapp`.
- `-h,--help` - Shows the help message for the specified command.
- `--list` - List all available templates.
- `--min-sdk=PARAM` - The `minSdk` value supported by the app (the default value is defined in the template).
- `--name=PARAM` - The name of the app, for example `My Application`.
- `--namespace=PARAM` - The namespace for resources and package name for Kotlin source files.
- `-o,--output=PARAM` - The destination project directory path (the default value is `.`).

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<template-name>` - The template name.

## Description

`android create` scaffolds a new Android project from an official project template.

By default, if `<template-name>` is omitted, the default empty Compose activity template is used. Pass `--list` to inspect all available project templates before creating a project.

### Configure project options

- `--name`: Required when creating a project. Sets the display name of the app (for example, `"My Application"`).
- `-o, --output`: Sets the destination directory where the project files are written. Defaults to the current directory (`.`).
- `--application-id`: Sets the unique app ID used for builds and Google Play publishing (for example, `com.example.myapp`).
- `--namespace`: Sets the namespace for generated Android resources (`R` class) and the default Kotlin package name.
- `--min-sdk`: Overrides the template's default minimum API level (`minSdk`).

### List templates (`--list`)

Run `android create --list` to print all available templates and their descriptions without creating a project.

### Examples

List all available project templates:

    android create --list

Create a new Android project in `./my-app` with a custom app name and app ID:

    android create --name="My Application" --application-id=com.example.myapp --output=./my-app

Create a project using a specific template and minimum SDK version:

    android create --name="Wear App" --min-sdk=30 --output=./wear-app empty-activity-compose