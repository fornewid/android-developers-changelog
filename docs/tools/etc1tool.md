---
title: https://developer.android.com/tools/etc1tool
url: https://developer.android.com/tools/etc1tool
source: md.txt
---

# etc1tool

`etc1tool`is a command line utility that lets you encode PNG images to the[ETC1](https://registry.khronos.org/OpenGL/extensions/OES/OES_compressed_ETC1_RGB8_texture.txt)compression standard and decode ETC1 compressed images back to PNG.

The usage for`etc1tool`is:  

```
etc1tool infile [--help | --encode | --encodeNoHeader | --decode] [--showDifference
diff-file] [-o outfile]
```

This table lists the command options:

|             Option             |                                                                              Description                                                                               |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `infile`                       | The input file to compress.                                                                                                                                            |
| `--help`                       | Print usage information.                                                                                                                                               |
| `--encode`                     | Create an ETC1 file from a PNG file. This is the default mode for the tool if nothing is specified.                                                                    |
| `--encodeNoHeader`             | Create a raw ETC1 data file without a header from a PNG file.                                                                                                          |
| `--decode`                     | Create a PNG file from an ETC1 file.                                                                                                                                   |
| `--showDifference `*diff-file* | Write the difference between the original and encoded image to*diff-file*. This option is only valid when encoding.                                                    |
| `-o `*outfile*                 | Specify the name of the output file. If*outfile*is not specified, the output file is constructed from the input filename with the appropriate suffix (`.pkm`or`.png`). |