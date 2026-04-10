---
title: https://developer.android.com/media/platform/mp4-at-file-format
url: https://developer.android.com/media/platform/mp4-at-file-format
source: md.txt
---

# MP4 With Auxiliary Tracks Extension (MP4-AT) File Format 0.9

The**MP4-AT**file format supports storing auxiliary tracks that are useful for post-capture editing and composition (for example, a depth map video track) alongside playable media data in an ISOBMFF/MP4 structure.

The goal of the format is to store auxiliary tracks such that the tracks are hidden from clients not implementing this spec. This prevents clients from interpreting auxiliary tracks as playable data.

## Dependencies

The following are normative references for this specification:

- [Key words for use in RFCs to Indicate Requirement Levels](https://www.ietf.org/rfc/rfc2119.txt)
- [ISO/IEC 14496-12:2022 ISO Box media file format](https://www.iso.org/standard/83102.html)(ISOBMFF/MP4)
- [ISO/IEC 14496-10:2022 Coding of audio-visual objects Part 10: Advanced video coding](https://www.iso.org/standard/83529.html)(AVC)
- [ISO/IEC 23008-2:2023 High efficiency coding and media delivery in heterogeneous environments Part 2: High efficiency video coding](https://www.iso.org/standard/85457.html)(HEVC)
- [VP9 Video Codecs](https://www.webmproject.org/vp9/)(VP9)
- [AV1 Bitstream \& Decoding Process Specification](https://aomediacodec.github.io/av1-spec/av1-spec.pdf)(AV1)
- [Dynamic depth 1.0 spec](https://developer.android.com/static/media/camera/camera2/Dynamic-depth-v1.0.pdf)

## Introduction

The use of "MUST", "MUST NOT", "REQUIRED", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" is per the IETF standard defined in[RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

## MP4-AT file format

The**MP4-AT** file format consists of primary tracks and auxiliary tracks to enable various editing operations. The primary tracks (for example, a video track that has had a bokeh effect applied to it) are written in the MP4 file as usual, whereas the auxiliary tracks are written in an**Auxiliary Tracks MP4** . The**Auxiliary Tracks MP4** is another MP4 compliant container, and is placed inside the`axte`**(Auxiliary Tracks Extension)** box. The`axte`box is recommended to be the last box in the file, which makes it convenient to remove auxiliary data by truncating the file.

This format is backward compatible: players that don't support the rest of this format will read and play the primary video tracks when loading the file.

![Line diagram demonstrating the arrangement of elements in an MP4-AT file](https://developer.android.com/static/images/media/platform/mp4-at-structure.svg)

The file has a`moov.meta`box with`mdta`handler that contains the following metadata. The metadata may appear in any order.

|---------------------------|-----------------------------------------|--------------------------------------------|
| **Metadata key**          | **Type indicator**                      | **Value**                                  |
| `auxiliary.tracks.offset` | 78 (big endian 64-bit unsigned integer) | The file offset (in bytes) of the`axte`box |
| `auxiliary.tracks.length` | 78 (big endian 64-bit unsigned integer) | The length (in bytes) of the`axte`box      |

| **Note:** Since metadata is carried over by most well-behaved editors, the MP4 file may still have this residual metadata even though the axte box has been stripped. These metadata therefore are not definitive and readers must always confirm that the axte box is present.

### Auxiliary tracks extension (axte) box

#### Syntax

The`axte`box is described using the semantics of the box defined in[ISO/IEC 14496-12:2022: 4.2](https://www.iso.org/standard/83102.html)  

    aligned(8) class AuxiliaryTracksExtensionBox extends Box('axte') {
      bit(8) data[];
    }

where the data field contains the**Auxiliary Tracks MP4**.

#### Payload

The`axte`box's payload is an**Auxiliary Tracks MP4** . The**Auxiliary Tracks MP4**has the usual MP4 structure.

![Line diagram demonstrating the arrangement of elements in the Auxiliary Tracks MP4](https://developer.android.com/static/images/media/platform/auxiliary-tracks-mp4-structure.svg)

The**Auxiliary Tracks MP4** contains sample metadata for all auxiliary tracks. All auxiliary track sample payloads must be stored either in the**Auxiliary Tracks MP4** 's`mdat`box, or in the outer MP4's`mdat`box (but not both).

In the former case,`auxiliary.tracks.interleaved`must be set to 0 ([see "Static Metadata" below](https://developer.android.com/media/platform/mp4-at-file-format#static-metadata)) and the sample offsets in the`axte.moov`box are relative to the start of the**Auxiliary Tracks MP4** . This makes the**Auxiliary Tracks MP4** self contained, which means the**Auxiliary Tracks MP4**can be read standalone without any references to the outer MP4.

In the latter case,`auxiliary.tracks.interleaved`must be set to 1 ([see "Static Metadata" below](https://developer.android.com/media/platform/mp4-at-file-format#static-metadata)) and the sample offsets in the`axte.moov`box are relative to the start of the file and the sample payloads of the primary and auxiliary tracks may be interleaved. The`axte.mdat`box can be absent in this case.

##### Static metadata

The**Auxiliary Tracks MP4** contains a`moov.meta`box with`mdta`handler that contains the following metadata. The metadata may appear in any order.

|------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Metadata key**                         | **Type indicator**          | **Value**                                                                                                                                                                                                                                                                                          |
| (Optional)`auxiliary.tracks.interleaved` | 75 (8-bit Unsigned Integer) | 0: Indicates samples are not interleaved and are in the`axte.mdat`box 1: Indicates samples are interleaved in the primary video track's`mdat`box All other values are reserved and must not be used. Absence of this metadata indicates default value 0.                                           |
| `auxiliary.tracks.map`                   | 0 (reserved)                | Binary format: - 1 byte version = 1 - 1 byte track count = n - n bytes track types from following set - 0 = Sharp video - 1 = Depth video (linear) - 2 = Depth video (inverse) - 3 = Timed depth metadata - 4 = Translucent video - 5-127 = Reserved for future use - 128-255 = Custom track types |

The order of track types in the`auxiliary.tracks.map`indicates their order in the**Auxiliary Tracks MP4**'s payload.

##### Auxiliary track types

The**Auxiliary Tracks MP4**may contain following video and metadata tracks useful for editing.
| **Note:** Timestamps of the access units should match between all the timed tracks. Clients may not support interpolation, so they may drop frames if timestamps are not aligned (for example, if the frame rates of the**depth** and**sharp video tracks**are different).

###### Sharp video track

A video at full resolution without editable effects applied. The video track may be stored at a different resolution than the primary video track. The**sharp video track**may use any common video codec, and may be in standard or high dynamic range.

###### Depth video track

The**depth video track** provides the depth information encoded as a standard grayscale video. This is to allow decoding and encoding depth tracks on devices that don't have any special decoding or encoding support for depth. The**depth video track** may use[H.264/AVC](https://www.iso.org/standard/83529.html),[H.265/HEVC](https://www.iso.org/standard/85457.html),[VP9](https://www.webmproject.org/vp9/),[AV1](https://aomediacodec.github.io/av1-spec/av1-spec.pdf)or any other common video codec. The**depth video track** can be 8-bit or 10-bit and linear- or inverse-encoded (refer to the[Dynamic depth 1.0 spec](https://developer.android.com/static/media/camera/camera2/Dynamic-depth-v1.0.pdf)).

###### Timed depth metadata track

The**timed depth metadata track**contains normalizing values to calculate depth, and a focal table that can be used to calculate the blur radius for a bokeh effect.

|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sample mime type** | `application/x-depth-metadata`                                                                                                                                                                                                |
| **Sample syntax**    | Binary format (all ints little endian): - Near distance (16-bit float) - Far distance (16-bit float) - Focal table entry count (16-bit int) - Focal table entry - Entry distance (16-bit float) - Entry radius (16-bit float) |

###### Translucent video track

A video track storing the alpha value (transparency) for each pixel in the corresponding frame. A minimum value indicates fully transparent, while the maximum value indicates full opacity. Values in between represent varying levels of translucency on a linear scale, and compositing uses the normal blending mode with non-pre-multiplied color values. Similar to the[depth video track](https://developer.android.com/media/platform/mp4-at-file-format#depth-video-track), this track should also be encoded as a standard grayscale video.

## Example use cases

- Storing a playable rendered bokeh video in a primary track, with auxiliary video tracks for the original (pre-blurring) sharp color data and a depth map, and an auxiliary timed metadata track with depth metadata reflecting the focus point at each frame. The auxiliary tracks can then be used in a video editor to modify the focus subject and re-render a high quality bokeh video track.

- Storing a pre-rendered translucent 'sticker' video, for example, an animated emoji video on a white background in a primary video track, with an auxiliary video track containing an alpha map. The auxiliary track can then be used by a compositor to blend the sticker with a background using translucency information from the auxiliary track.