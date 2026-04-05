---
title: https://developer.android.com/tools/zipalign
url: https://developer.android.com/tools/zipalign
source: md.txt
---

# zipalign

`zipalign`is a zip archive alignment tool that helps ensure that all uncompressed files in the archive are aligned relative to the start of the file. This lets the files be accessed directly via[mmap(2)](https://man7.org/linux/man-pages/man2/mmap.2.html)`
`, removing the need to copy this data in RAM and reducing your app's memory usage.

Use`zipalign`to optimize your APK file before distributing it to end users. If you build using Android Studio, which uses the Android Gradle plugin (AGP), this is done automatically. In this case, you should still use`zipalign`to verify that the APK is aligned, but you don't need to align it. This documentation is mainly for maintainers of custom build systems.  
**Caution:** You must use`zipalign`at a specific point in the build process. That point depends on which app-signing tool you use:

- If you use[apksigner](https://developer.android.com/studio/command-line/apksigner),`zipalign`must be used**before** the APK file has been signed. If you sign your APK using`apksigner`and make further changes to the APK, its signature is invalidated.
- If you use[jarsigner](https://docs.oracle.com/javase/tutorial/deployment/jar/signing.html)(not recommended),`zipalign`must be used**after**the APK file has been signed.

To achieve alignment,`zipalign`alters the size of the`"extra"`field in the zip**Local File Header** sections. This process can also alter existing data in the`"extra"`fields.

## Usage

If your APK contains shared libraries (`.so`files), use`-P 16`to ensure that they're aligned to a 16KiB page boundary suitable for`mmap(2)`in both 16KiB and 4KiB devices. For other files, whose alignment is determined by the mandatory alignment argument to`zipalign`, should be aligned to 4 bytes on both 32-bit and 64-bit systems.

To align`infile.apk`and save it as`outfile.apk`:  

```
zipalign -P 16 -f -v 4 infile.apk outfile.apk
```

To confirm the alignment of`existing.apk`, use the following command.  

```
zipalign -c -P 16 -v 4 existing.apk
```

### Options

The following table lists the available`zipalign`options:

|       Option       |                                                     Description                                                     |
|--------------------|---------------------------------------------------------------------------------------------------------------------|
| -c                 | Checks alignment only (does not modify file).                                                                       |
| -f                 | Overwrites existing output file.                                                                                    |
| -h                 | Displays tool help.                                                                                                 |
| -P \<pagesize_kb\> | aligns uncompressed`.so`files to the specified page size in KiB. Valid options for`<pagesize_kb>`are 4, 16, and 64. |
| -p                 | 4KiB page-aligns uncompressed`.so`files. It is recommended to use`-P 16`instead, as`-p`is deprecated.               |
| -v                 | Verbose output.                                                                                                     |
| -z                 | Recompresses using Zopfli.                                                                                          |