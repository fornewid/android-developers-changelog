---
title: https://developer.android.com/tools/agents/android-cli/commands/analyze
url: https://developer.android.com/tools/agents/android-cli/commands/analyze
source: md.txt
---

Analyzes the file(s) (AAB, APK, JAR, AAR) at the given location(s) and reports
back all available details.

## Usage

    android analyze [-h] [--analysis=PARAM] [--format=PARAM] <path>

## Options

- `--analysis=PARAM` - Analysis category to filter output (basic, optimization). Supports comma-separated values (default: all).
- `-f,--format=PARAM` - Output format: json, textproto. If omitted, output is formatted for human readability.
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<path>` - Path to the target file(s) to analyze (AAB, APK, JAR, AAR).

## Description

`android analyze` inspects one or more Android artifacts---such as application
packages (`.aab`, `.apk`) or library archives (`.aar`, `.jar`)---and reports
detailed build, structure, and performance metadata.

### Supported File Types

`android analyze` supports both application packages and library archives:

- **Android App Bundles (`.aab`) and APKs (`.apk`)**: Evaluates application-level metadata, compilation configurations, DEX characteristics, and optimization outputs.
- **Android Archives (`.aar`) and Java Archives (`.jar`)**: Evaluates library-level metadata, DEX compilation metrics, keep rule impact, and bundled native components.

### Analysis Categories (`--analysis`)

By default, all available analysis categories are performed. Use
`--analysis=<category>` to filter output to specific categories
(comma-separated).

- **`basic`**: Basic metadata such as package name and version for applications:
  Reports application identification details (e.g., package name, version name,
  and version code for applications).

- **`optimization`**: Compiler optimizations, DEX sizes, and code-shrinking
  metadata:

  - **For applications (`.aab`, `.apk`)**: Reports Android Gradle Plugin (AGP) version, uncompressed DEX size, R8 shrinking and optimization settings and percentages, R8 resource optimization status, and DEX marker metadata.
  - **For libraries (`.aar`, `.jar`)** : Reports D8 and R8 DEX sizes, keep ratio, item collection summaries (kept vs. total classes, methods, and fields), used and unused package-wide keep rules with impact radius, blocked consumer keep rules, packaged native libraries (`.so` files), and warnings for detected optimization antipatterns.

### Output Formatting (`-f, --format`)

- By default, output is printed in a human-readable summary format.
- `-f json, --format=json`: Emits machine-readable JSON, suitable for programmatic parsing by scripts and CI pipelines.
- `-f textproto, --format=textproto`: Emits Protobuf text format (`textproto`).

### Examples

Analyze an APK with all default categories:

    android analyze app-release.apk

Analyze multiple artifacts together:

    android analyze app-release.apk library.aar

Analyze an AAB and output the results as JSON:

    android analyze --format=json app-release.aab

Sample JSON output:

    {
      "results": [
        {
          "optimization": {
            "bundleAnalysisResult": {
              "agpVersion": "9.3.2",
              "r8Json": {
                "version": "9.3.16",
                "options": {
                  "isRepackageClassesEnabled": true,
                  "isProguardCompatibilityModeEnabled": false
                },
                "stats": {
                  "shrinkingRatio": 0.9606,
                  "optimizationRatio": 0.9551,
                  "obfuscationRatio": 0.9622
                },
                "resourceOptimizationStatus": "R8_RESOURCE_OPTIMIZATION_STATUS_DISABLED",
                "r8DexChecksumStatus": "EXACT_MATCH"
              },
              "r8DexMarkerMetadata": {
                "r8Enabled": true,
                "d8Enabled": false,
                "fullModeEnabled": true
              },
              "mappingObfuscationRatio": 0.97108626,
              "dexHeuristicObfuscationRatio": 0.97108626,
              "uncompressedDexSizeBytes": "6198152"
            }
          },
          "artifactPath": "app-release.aab",
          "basic": {
            "appInfo": {
              "packageName": "com.google.samples.apps.nowinandroid",
              "versionName": "1.0",
              "versionCode": "1"
            }
          }
        }
      ]
    }

Analyze a Java Archive (JAR) library with all default categories:

    android analyze library.jar

Analyze an Android Archive (AAR) library filtering for the `optimization`
category and outputting as JSON:

    android analyze --analysis=optimization -f json library.aar

Sample JSON output:

    {
      "results": [
        {
          "optimization": {
            "libraryAnalysisResult": {
              "dex": {
                "d8CompileResult": {
                  "dexSizeBytes": 2117400
                },
                "r8CompileResult": {
                  "dexSizeBytes": 1100,
                  "configuration": {
                    "keepRules": [
                      {
                        "source": "-keep class com.example.ExampleClass_* {\n  static *** builder();\n}",
                        "keptItemCount": 2
                      },
                      {
                        "source": "-keep class com.example.SomeClass {\n  public static *** SDK_ROOT_CLASS_NAME;\n}",
                        "keptItemCount": 2
                      }
                    ]
                  },
                  "classes": {
                    "itemCount": 3437,
                    "keptItemCount": 2,
                    "noObfuscationCount": 2,
                    "noOptimizationCount": 2,
                    "noShrinkingCount": 2
                  },
                  "fields": {
                    "itemCount": 9835,
                    "keptItemCount": 1,
                    "noObfuscationCount": 1,
                    "noOptimizationCount": 1,
                    "noShrinkingCount": 1
                  },
                  "methods": {
                    "itemCount": 16333,
                    "keptItemCount": 1,
                    "noObfuscationCount": 1,
                    "noOptimizationCount": 1,
                    "noShrinkingCount": 1
                  }
                },
                "validateConsumerKeepRulesResult": {}
              },
              "r8Version": "9.5.17-dev",
              "version": "kg=1_r8=9.5.17-dev"
            }
          },
          "artifactPath": "library.aar"
        }
      ]
    }