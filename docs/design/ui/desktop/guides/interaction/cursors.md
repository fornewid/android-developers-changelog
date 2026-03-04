---
title: https://developer.android.com/design/ui/desktop/guides/interaction/cursors
url: https://developer.android.com/design/ui/desktop/guides/interaction/cursors
source: md.txt
---

When using a pointer device, users rely on the cursor to track where they are
pointing, infer what kind of actions they can perform, and get feedback during
certain interactions.

## Cursor icons

Cursor icons provide specific visual cues that indicate to users which elements
are interactive and what actions they can perform.

The system provides a set of cursor icons, such as the following:

### General


| Icon | Type | Description |
|---|---|---|
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_default.webp) | Pointer | Indicates where the mouse is pointing on the screen. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_hand.webp) | Hand pointer | Indicates that an object can be clicked or interacted with. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_all.webp) | All scroll | Indicates that the user can scroll in any direction. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_grab.webp) | Grab | Indicates that the user can drag an object. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_grabbing.webp) | Grabbing | Indicates that the element is being dragged. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_copy.webp) | Copy | Indicates that the user can copy text or other content by clicking and dragging. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_nodrop.webp) | No drop | Indicates that the user can't drop the item that they are dragging. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_text.webp) | Text | Indicates that the user can insert, edit, or copy text. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_verticaltext.webp) | Text vertical | Indicates that the user can insert, edit, or copy vertical text. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_alias.webp) | Alias | Indicates that the user can create an alias for a file or directory. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_wait.webp) | Process spinner | Indicates that a process is underway and the user can't interact with the UI until the process is finished. |

<br />

### Services


| Icon | Type | Description |
|---|---|---|
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_help.webp) | Help | Indicates that help is available as a help window for the current context. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_context.webp) | Context menu | Indicates that the user can right-click to open a context menu. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_crosshair.webp) | Crosshair | Indicates that the user can precisely select an object or location. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_cell.webp) | Cell | Shows the active cell in a spreadsheet. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_zoomout.webp) | Zoom out | Indicates that the user can zoom out on an object or area of the screen. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_zoomin.webp) | Zoom in | Indicates that the user can zoom in on an object or area of the screen. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_spothover.webp) | Spot hover | Indicates that the mouse is hovering, similar to the default pointer. Used mostly for testing and screen recording. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_spottouch.webp) | Spot touch | Indicates that the cursor has tapped. |

<br />

### Resize


| Icon | Type | Description |
|---|---|---|
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_resizedirections.webp) | Resize arrows | Indicates that the element can be resized in the direction shown. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_noresizedirections.webp) | No resize directional arrows | Indicates that the user can't resize the object in the shown direction. |
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_noresize.webp) | No resize all directions | Indicates that the user can't resize an object in any direction. |

<br />

### Stylus


| Icon | Type | Description |
|---|---|---|
| ![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_cursor_stylus.webp) | Scribe hover | With a stylus, indicates that the input field is writable. |

<br />

## Use cursor icons

Use and set the system cursors to communicate interaction to users.
For example, use a magnifying glass when hovering over zoomable content.
![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_target_hover.webp) Zoom in cursor set to indicate images can be zoomed in on.

Create a custom cursor icon for more specialized actions that are not provided
by Android.
![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_custom-cursor.webp) App with a custom cursor for a unique interaction.

<br />

For design guidance, [cursor icons](https://m3.material.io/foundations/interaction/inputs#64b60907-0946-462c-adbf-99c96c3bf16c). For implementation details and how to
set different cursor types, [custom cursors](https://developer.android.com/guide/topics/large-screens/custom-cursors).