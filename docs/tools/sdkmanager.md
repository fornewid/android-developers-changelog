---
title: https://developer.android.com/tools/sdkmanager
url: https://developer.android.com/tools/sdkmanager
source: md.txt
---

The `sdkmanager` is a command-line tool that lets you view, install,
update, and uninstall packages for the Android SDK. If you're using Android
Studio, then you don't need to use this tool, and you can instead [manage your
SDK packages from the IDE](https://developer.android.com/studio/intro/update#sdk-manager).

The `sdkmanager` tool is provided in the
[Android SDK Command-Line Tools](https://developer.android.com/studio/command-line#tools-sdk) package.
To use the SDK Manager to install a version of the command-line tools,
follow these steps:

1. Download the latest [command line tools package](https://developer.android.com/studio#command-line-tools-only) from the [Android Studio](https://developer.android.com/studio) page and extract the package.
2. Move the unzipped `cmdline-tools` directory into a new directory of your choice, such as <var translate="no">android_sdk</var>. This new directory is your Android SDK directory.
3. In the unzipped `cmdline-tools` directory, create a sub-directory called `latest`.
4. Move the original `cmdline-tools` directory contents, including the `lib` directory, `bin` directory, `NOTICE.txt` file, and `source.properties` file, into the newly created `latest` directory. You can now use the command-line tools from this location.
5. (Optional) To install a previous version of the command-line tools, run
   the following command:

   ```
   android_sdk/cmdline-tools/latest/bin/sdkmanager --install "cmdline-tools;version"
   ```
   Substitute <var translate="no">version</var> with the version you want to install, for example `5.0`. **Note:** For local usage, you can use the `latest` packages. For scripts, choose a specific version instead to ensure stability.

## Usage

You can use the `sdkmanager` to list installed and available packages, install
packages, and update packages. For more details, see the following sections.

### List installed and available packages

To list installed and available packages, use the following syntax:  

```
sdkmanager --list [options] \
           [--channel=channel_id] // Channels: 0 (stable), 1 (beta), 2 (dev), or 3 (canary)
```

Use the `channel` option to include a package from a channel up to and
including `channel_id`. For example, specify the canary channel to list
packages from all channels.
| **Note:** To list only stable packages, use `--channel=0` or remove the `--channel` option entirely.

### Install packages

To install packages, use the following syntax:  

```
sdkmanager packages [options]
```

The <var translate="no">packages</var> argument is an SDK-style path, as shown with
the `--list` command, wrapped in quotes. For example,
`"build-tools;36.0.0"` or
`"platforms;android-36"`.

You can pass multiple package
paths, separated with a space, but they must each be wrapped in their own set of
quotes. For example, here's how to install the latest platform tools and
the SDK tools for API level 36:  

    sdkmanager "platform-tools" "platforms;android-36"

Alternatively, you can pass a text file that specifies all packages:  

```
sdkmanager --package_file=package_file [options]
```

The <var translate="no">package_file</var> argument is the location of a text file in which
each line is an SDK-style path of a package to install (without quotes).

To uninstall, add the `--uninstall` flag:  

```
sdkmanager --uninstall packages [options]
sdkmanager --uninstall --package_file=package_file [options]
```

To install CMake or the NDK, use the following syntax:  

```transact-sql
sdkmanager --install
           ["ndk;<var translate="no">major</var>.<var translate="no">minor</var>.<var translate="no">build</var>[<var translate="no">suffix</var>]" | "cmake;major.minor.micro.build"]
           [--channel=<var translate="no">channel_id</var>] // NDK channels: 0 (stable), 1 (beta), or 3 (canary)
```

For example, use the following command to install the specified NDK version
regardless of which channel it is currently on:  

```text
sdkmanager --install "ndk;21.3.6528147" --channel=3 // Install the NDK from the canary channel (or below)
sdkmanager --install "cmake;10.24988404" // Install a specific version of CMake
```

### Update all installed packages

To update all installed packages, use the following syntax:  

```
sdkmanager --update [options]
```

### Accept licenses

You are required to accept the necessary license for each package you have
installed. This step occurs during the installation flow when you install
packages from within Android Studio.

If you don't have Android Studio installed, or it is for a CI server
or other headless Linux device without a GUI installed, do the
following from the command-line:  

```text
sdkmanager --licenses
```

This prompts you to accept any licenses that haven't already been accepted.

## Options

The following table lists the available options for the commands listed in the preceding section:

| Option | Description |
|---|---|
| `--sdk_root=`**<var translate="no">path</var>** | Use the specified SDK path instead of the SDK containing this tool. |
| `--channel=`**<var translate="no">channel_id</var>** | Include packages in channels up to and including channel_id. Available channels are: `0` (Stable), `1` (Beta), `2` (Dev), and `3` (Canary). |
| `--include_obsolete` | Include obsolete packages in the package listing or package updates. For use with `--list` and `--update` only. |
| `--no_https` | Force all connections to use HTTP rather than HTTPS. |
| `--newer` | With `--list`, show only new or updatable packages. |
| `--verbose` | Verbose output mode. Errors, warnings and informational messages are printed. |
| `--proxy={http | socks}` | Connect via a proxy of the given type: either `http` for high level protocols such as HTTP or FTP, or `socks` for a SOCKS (V4 or V5) proxy. |
| `--proxy_host={`**<var translate="no">IP_address</var>**` | `**<var translate="no">DNS_address</var>**`}` | IP or DNS address of the proxy to use. |
| `--proxy_port=`**<var translate="no">port_number</var>** | Proxy port number to connect to. |

| **Note:** If you want to install packages for an operating system different from the current machine, set the [`REPO_OS_OVERRIDE`](https://developer.android.com/studio/command-line/variables#repo_os_override) environment variable to either `"windows"`, `"macosx"`, or `"linux"`.