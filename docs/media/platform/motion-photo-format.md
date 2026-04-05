---
title: https://developer.android.com/media/platform/motion-photo-format
url: https://developer.android.com/media/platform/motion-photo-format
source: md.txt
---

# Motion Photo format 1.0

Motion Photos are single files that contain a still photographic image and a
short video, which includes audio recording. This type of media allows a user to
view a high resolution still image as well as the video and sound to capture the
sentiment and atmosphere where the image was taken.

## Dependencies

The following are normative references for this specification:

- [Key words for use in RFCs to Indicate Requirement Levels](https://www.ietf.org/rfc/rfc2119.txt)
- [T.81 (09/92) Digital compression and coding of continuous-tone still
  images](http://www.itu.int/rec/T-REC-T.81-199209-I/e) (JPEG)
- [ISO/IEC 23008-12:2022 High efficiency coding and media delivery in
  heterogeneous environments Part 12: Image File Format](https://www.iso.org/standard/83650.html) (HEIC)
- [AV1 Image File Format (AVIF)](https://aomediacodec.github.io/av1-avif/v1.1.0.html) (AVIF)
- [Ultra HDR Image Format v1.0 \| Android Developers](https://developer.android.com/guide/topics/media/platform/hdr-image-format) (Ultra HDR)
- [ISO 16684-1:2011(E) XMP Specification Part 1](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart1.pdf) (XMP)
- [Adobe XMP Specification Part 3 Storage in Files](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart3.pdf) (XMP)
- [ISO/IEC 14496-10:2022 Coding of audio-visual objects Part 10: Advanced
  video coding](https://www.iso.org/standard/83529.html) (AVC)
- [ISO/IEC 23008-2:2023 High efficiency coding and media delivery in
  heterogeneous environments Part 2: High efficiency video
  coding](https://www.iso.org/standard/85457.html) (HEVC)
- [AV1 Bitstream \& Decoding Process Specification](https://aomediacodec.github.io/av1-spec/av1-spec.pdf) (AV1)
- [ISO/IEC 14496-1:2010 Coding Of Audio-Visual Objects -
  Systems](https://www.iso.org/standard/55688.html)
- [ISO/IEC 14496-12:2015 ISO Box media file format](https://www.iso.org/standard/68960.html#:%7E:text=ISO%2FIEC%2014496%2D12%3A2015%20specifies%20the%20ISO%20base,such%20as%20audio%2Dvisual%20presentations.) (ISOBMFF)
- [ISO/IEC 14496-14:2020 Coding of audio-visual objects Part 14: MP4 file
  format](https://www.iso.org/standard/79110.html) (MP4)
- [Apple QuickTime File Format](https://developer.apple.com/documentation/quicktime-file-format) (MOV)

## Introduction

The use of "MUST", "MUST NOT", "REQUIRED", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" is per the IETF standard
defined in [RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

## Motion Photo Format

Motion Photo files consist of a primary still image file,
[JPEG](https://www.itu.int/rec/T-REC-T.81-199209-I/e), [HEIC](https://www.iso.org/standard/69668.html), or [AVIF](https://aomediacodec.github.io/av1-avif/v1.1.0.html), with a
secondary video file appended to it. The primary image contains Camera XMP
metadata describing how to display the still image file and video file contents,
and Container XMP metadata describing how to locate the video file contents.

The image file may have a gainmap, as is the case with [Ultra HDR JPEGs](https://developer.android.com/guide/topics/media/platform/hdr-image-format).

### Filename Pattern

Writers should use a filename matching the following regular expression:  

    ^([^\\s\\/\\\\][^\\/\\\\]*MP)\\.(JPG|jpg|JPEG|jpeg|HEIC|heic|AVIF|avif)

Readers may ignore the XMP metadata, the appended video file, or the video
contents if the pattern is not followed.

### Media Data Encoding

The primary image contains a Container Element [XMP](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart1.pdf)
metadata directory defining the order and properties of the subsequent media
file in the file container. Each file in the container has a corresponding media
item in the directory. The media item describes the location in the file
container and the basic properties of each concatenated file.

### XMP Attributes

Two sets of XMP metadata are used to define the extra semantic information for
the Motion Photo format. The metadata may appear in any order.

#### Camera Metadata

Camera metadata encodes information about how to present the primary image and
video portions of the Motion Photo.

- The namespace URI is `http://ns.google.com/photos/1.0/camera/`
- The default namespace prefix is `Camera`

The following attributes may appear in the still image file XMP metadata:

|-------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                                                                                                                    | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Camera:MicroVideo` `Camera:MicroVideoVersion` `Camera:MicroVideoOffset` `Camera:MicroVideoPresentation` ` TimestampUs` |           | These properties were part of the Microvideo V1 specification. They are deleted in this specification and must be ignored if present. In particular, the `MicroVideoOffset` attribute is replaced by the `GContainer:ItemLength` value for locating the video data in the file.                                                                                                                                                                                                                                                                                                                                                |
| `Camera:MotionPhoto`                                                                                                    | `Integer` | 0: Indicates that the file shouldn't be treated as a Motion Photo. 1: Indicates that the file should be treated as a Motion Photo. All other values are undefined and are treated equivalently to 0. If the value is zero or negative, then the file is always treated as a non-Motion Photo, even if a video is in fact appended to the file. Since XMP is carried over by most well behaved editors, still image files may still have a residual value of 1 for this field even though the appended video has been stripped. This field is therefore not definitive and readers must always confirm that a video is present. |
| `Camera:MotionPhotoVersion`                                                                                             | `Integer` | Indicates the file format version of the Motion Photo. This specification defines version "1".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Camera:MotionPhotoPresentationTimestampUs`                                                                             | `Long`    | Long value representing the presentation timestamp (in microseconds) of the video frame corresponding to the image still. Value can be -1 to denote unset/unspecified.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

##### Presentation behavior

If `Camera:MotionPhotoPresentationTimestampUs` is not present in the XMP packet,
readers should use a presentation timestamp immediately preceding the timestamp
closest to the middle of the video track, i.e., the duration of the video track
divided by 2.

If `Camera:MotionPhotoPresentationTimestampUs` is present in the XMP packet and
the `"application/motionphoto-image-meta"` is present in the video, the same
value must appear in the `primaryImageFrameScoreDescr` `presentationTimestampUs`
field of that track. If `Camera:MotionPhotoPresentationTimestampUs` is not
present in the XMP packet and the metadata track is present, then the value in
the metadata track must be -1.

#### Container element

The container element is encoded into the XMP metadata of the primary image and
defines the directory of media items in the container. Media items must be
located in the container file in the same order as the media item elements in
the directory and must be tightly packed.

- The namespace URI is `http://ns.google.com/photos/1.0/container/`
- The default namespace prefix is `Container`

The directory may contain only one primary image item and it must be the first
item in the directory.

|--------------|-----------------------------|-------------------------------------------------------------------------------------------------|
| Element Name | Type                        | Description                                                                                     |
| `Directory`  | Ordered Array of Structures | Ordered array of `Container:Item` structures defining the layout and contents of the container. |

#### Item element

Media item elements describe how each item should be used by the application.

- The namespace URI is `http://ns.google.com/photos/1.0/container/item/`
- The default namespace prefix is `Item`

The first media item must be the primary image. It must contain a `Mime`
attribute specifying one of the image MIME types listed in Item MIME Type
Values. The length of the primary item may be determined by parsing the primary
image based on its MIME type starting at the beginning of the file container.

The first media item may contain a `Padding` attribute specifying additional
padding between the end of the encoded primary image and the beginning of the
next media item. Only the first media item may contain a `Padding` attribute.

Each media item must contain a `Mime` attribute. The secondary media items must
also contain Length attributes.

Sequential media items may share resource data within the file container. The
first media item determines the location of the resource in the file container,
and subsequent shared media items have `Length` set to 0 in the case that the
resource data is itself a container.

The location of media item resources in the container is determined by summing
the `Length` values of the preceding secondary item resources to the length of
the primary image encoding plus `Padding` if specified.

|----------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attribute Name | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Mime`         | `String`  | Required. Simple string indicating the MIME type of the media item in the container.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `Semantic`     | `String`  | Required. Simple string indicating the application specific meaning of the media item. See Item Semantic Values section for definition.                                                                                                                                                                                                                                                                                                                                                                        |
| `Length`       | `Integer` | Required for secondary media items, including the video container. The positive integer length in bytes of the item. Media items are expected to be in their original form, with no encoding applied. The length value is the actual length of the bytes in the file. Length 0 in secondary media items indicates that the media item resource is shared with the previous media item. Length is expected to be 0 in a primary media item.                                                                     |
| `Padding`      | `Integer` | \[JPEG-based motion photos\] Optional for the primary media item. Simple string containing a positive integer length in bytes of additional padding between the end of encoded primary image and the beginning of the next media item. \[HEIC/AVIF-based motion photos\] Required for the primary media item. Must have a value equal to 8, the header length of [the Motion Photo Video Data ("mpvd") box](https://developer.android.com/media/platform/motion-photo-format#isobmff-image-specific-behavior). |

| **Non-normative:** The `Length` attribute for the secondary media item enables readers to quickly locate the video without reading the entire container file. Readers can start from the end of the file and move back `<Length>` bytes to find the start of the video.
|
| Writers don't have to determine the length of the primary still image file when writing the XMP within it since Length is an optional attribute for the primary item.

##### Item:Mime type values

The `Item:Mime` attribute defines the MIME type of each media item.

|-------------------|----------------------------------------------------------------------------------|
| Value             | Description                                                                      |
| `image/jpeg`      | [JPEG](http://www.itu.int/rec/T-REC-T.81-199209-I/e) image                       |
| `image/heic`      | [HEIC](http://ISO/IEC 23008-2:2017 High efficiency video coding) image           |
| `image/avif`      | [AVIF](https://aomediacodec.github.io/av1-avif/v1.1.0.html) image                |
| `video/mp4`       | [MP4](https://www.iso.org/standard/79110.html) container                         |
| `video/quicktime` | [MOV](https://developer.apple.com/documentation/quicktime-file-format) container |

##### Item:Semantic values

The `Item:Semantic` attribute defines the application specific meaning of each
media item in the container directory.

|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Value`       | Description                                                                                                                                                                                                                                                               |
| `Primary`     | Indicates that the media item is the primary display ready image in the container. A motion photo must include one, and only one, item with this semantic.                                                                                                                |
| `MotionPhoto` | Indicates that the media item is the video container. A motion photo must include one, and only one, item with this semantic. The location of this media item must be at the end of the file. No other bytes may be placed after this media item's bytes have terminated. |

###### Motion photos with a primary Ultra HDR image

As per the item semantic value rules defined in this specification and in
[the Ultra HDR image specification](https://developer.android.com/guide/topics/media/platform/hdr-image-format#GContainer_details),
motion photos with a primary Ultra HDR image must also include a media item with
an item semantic of `"GainMap"`. Also, writers encoding motion photos must place
the gainmap item element before the video item element.

### ISOBMFF-image-specific behavior

Motion Photos with
[ISOBMFF-based](https://www.iso.org/standard/68960.html#:%7E:text=ISO%2FIEC%2014496%2D12%3A2015%20specifies%20the%20ISO%20base,such%20as%20audio%2Dvisual%20presentations.)
images (e.g., HEIC and AVIF images) must have a structure such that the image
portion of the file terminates with a top-level "Motion Photo Video Data" box,
described using the semantics of the Syntactic Description Language defined in
ISO/IEC 14496-1:2010(E) clause 8:  

    // Box as defined in ISO/IEC 14496-12:2015: 4.2
    aligned(8) class MotionPhotoVideoData extends Box('mpvd') {
      bit(8) data[];
    }

where the "data" field contains all of the video bytes. The special value of "0"
is not allowed for the size of the Motion Photo Video Data Box. (Refer to
[ISO/IEC 14496-12:2015: 4.2](https://www.iso.org/standard/55688.html) for the definition of a size of class that
extends Box.)

The ISOBMFF image's XMP must also define the primary media item's Padding
attribute value as being equal to the size in bytes of the Motion Photo Video
Data Box header, that is the size and name headers.

Refer to Figure 1 illustrating this box structure for a sample HEIC-based motion
photo:

![Line diagram demonstrating the arrangement of elements in an HEIC motion file](https://developer.android.com/static/images/media/platform/motion-photo-heic.png)

**Figure 1.** Illustration of the top-level boxes of a sample HEIC image within
a single HEIC motion photo file. Note that the order of boxes is mostly for
illustration only (please refer to the relevant standards on how to construct
HEIF or video files); nevertheless, the "mpvd" box must come after all the HEIC
image file's boxes.

### Video container contents

The video container file that is appended to the primary image must include at
least one primary video track. This track is required and contains video encoded
in [AVC](https://www.iso.org/standard/83529.html),
[HEVC](https://www.iso.org/standard/85457.html), or
[AV1](https://aomediacodec.github.io/av1-spec/av1-spec.pdf). The
primary video frame resolution is undefined. The video color space, transfer
function, and bit-depth may vary. For example, SDR videos may have an 8-bit bit
depth, BT.709 color space, with an sRGB transfer function. Or, HDR videos may
have a 10-bit bit depth, BT.2100 color space, and an HLG or PQ transfer
function, along with HDR metadata and metadata tracks.

The video container file may contain one optional higher resolution secondary
video track. Readers should use its contents to display substitutions for the
primary still image encoded in the JPEG or HEIC image. This track may contain
lower frame rate video encoded in AVC, HEVC, or AV1. The secondary video frame
resolution is undefined.

It is expected that all of the frames in the secondary video track have
corresponding frames in the primary video track. Each pair of corresponding
frames in primary and secondary video tracks should have identical presentation
timestamps. If there is a secondary track frame without corresponding primary
track frame, viewers can try selecting a primary track frame with the closest
matching presentation timestamp as the representative thumbnail for that
secondary video track.

The video container file may contain one optional 16-bit mono or stereo audio
track at 44kHz, 48 kHz, or 96 kHz encoded in AAC. Readers should present this
audio track when the primary video track is displayed.

The secondary video track, if present, should always come *after* the primary
video track. There are no other ordering constraints regarding other tracks. The
primary video track must have a track index lower than that of any secondary
video track. That is, if the primary video track has a track number 2, then any
secondary video track must have a track number greater than or equal to 3.

### Video Metadata Track with Machine Intelligence Scoring

Writers may optionally add a metadata track to the video container file with a
type "meta". The metadata track should have exactly one sample that contains a
byte stream in [the format described in "Syntax"](https://developer.android.com/media/platform/motion-photo-format#metadata-syntax).

If the metadata track is present, the sample description table entry for the
track (i.e., the "stsd" box located at "mdia.minf.stbl.stsd" relative to the
"trak" box) must contain a single atom that indicates a text metadata sample
entry - (i.e, a "mett" box). The "mett" box must have a MIME type string equal
to "application/motionphoto-image-meta".

#### Syntax

If this metadata track is defined, its content must consist of a byte stream
conforming to this `MotionPhotoMetadataDescriptor` specification, described
here using the semantics of the Syntactic Description Language defined in
ISO/IEC 14496-1:2010(E) clause 8.  

    // BaseDescriptor as defined in ISO/IEC 14496-1:2010(E): 7.2.2.2
    abstract aligned(8) expandable((1<<28) - 1) class BaseDescriptor
        : bit(8) tag=0 {
      // Empty. To be filled by classes extending this class.
    }

    // Score data for a frame.
    class MotionPhotoFrameScoreDescriptor extends BaseDescriptor
        : bit(8) tag=MotionPhotoFrameScoreDescrTag {
      // The frame's score in the range [0, 1].
      float(32) score;

      // The frame's presentation timestamp in microseconds.
      int(64) presentationTimestampUs;
    }

    // Score data for a track.
    class MotionPhotoTrackScoreDescriptor extends BaseDescriptor
        : bit(8) tag=MotionPhotoTrackScoreDescrTag {
      // The number of scored frames in the track.
      unsigned int(32) numScoredFrames;

      // The track's frames' score data. They must be in ascending order with
      // respect to the presentation timestamp.
      MotionPhotoFrameScoreDescriptor trackFrameScoreDescr[numScoredHighResFrames];
    }

    // Score data for a motion photo.
    class MotionPhotoScoreDescriptor extends BaseDescriptor
        : bit(8) tag=MotionPhotoScoreDescrTag {

      // Machine-intelligence model version used to calculate the scores. Writers
      // using a scoring model should set this field to 1 or greater. Writers not
      // using any scoring model should set this field to 0.
      unsigned int(32) modelVersion;

      // The primary image's frame score data.
      MotionPhotoFrameScoreDescriptor primaryImageFrameScoreDescr;

      // The high-resolution motion photo frames' score data.
      MotionPhotoTrackScoreDescriptor highResTrackScoreDescr;
    }

    // Flag data for a track.
    class MotionPhotoTrackFlagsDescriptor extends BaseDescriptor
        : bit(8) tag=MotionPhotoTrackFlagDescrTag {
      // Set to true to indicate the video frames have been stabilized and don't
      // require readers of the track to apply any further stabilization.
      bit(1) isStabilized;
    }

    // Flags for a motion photo.
    class MotionPhotoFlagsDescriptor extends BaseDescriptor
            : bit(8) tag=MotionPhotoFlagDescrTag {
      // The low-resolution motion photo track's flag data.
      MotionPhotoTrackFlagDescriptor lowResTrackFlagsDescr;

      // The high-resolution motion photo track's flag data.
      MotionPhotoTrackFlagDescriptor highResTrackFlagsDescr;
    }

    // Container for motion photo metadata, like stabilization indicators and
    // quality scoring.
    class MotionPhotoMetadataDescriptor extends BaseDescriptor
        : bit(8) tag=MotionPhotoMetadataDescrTag {
      // Scoring data for the still and high-res frames.
      MotionPhotoScoreDescriptor motionPhotoScoreDescr;

      // Flags for the low-res and high-res frames.
      MotionPhotoFlagDescriptor motionPhotoFlagDescr;
    }

    // Class tags for MotionPhotoData using the "User Private" tag space 0xC0-0xFE
    // for descriptors defined in ISO/IEC 14496-1:2010(E): 7.2.2.1, Table 1.
    // 0xC0 MotionPhotoMetadataDescrTag
    // 0xC1 MotionPhotoScoreDescrTag
    // 0xC2 MotionPhotoTrackScoreDescrTag
    // 0xC3 MotionPhotoFrameScoreDescrTag
    // 0xC4 MotionPhotoFlagsDescrTag
    // 0xC5 MotionPhotoTrackFlagDescrTag