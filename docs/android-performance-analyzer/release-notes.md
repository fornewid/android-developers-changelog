---
title: https://developer.android.com/android-performance-analyzer/release-notes
url: https://developer.android.com/android-performance-analyzer/release-notes
source: md.txt
---

This page contains release notes for current and previous Stable and Canary
releases of Android Performance Analyzer.


## Stable

## 1.0.0-Stable (November 2026)

This release builds AI Agent into the app, lets you run SQL queries from the
search bar, refreshes the trace viewer, and fixes many bugs.

### New features and improvements

- **AI Agent is built in:** Use the ACP integration to use Claude, Antigravity, or Codex inside Android Performance Analyzer. Or, you can sign in with your Google Account and use the built-in agent. Use **Ask AI** to analyze a trace, and use **Generate
  Query** to have AI Agent write SQL for you.
- **AI Agent can see and control your open trace view:** It can see what you're looking at and answer your questions by querying the trace. You can also control the trace viewer directly with natural language. Tell the AI Agent what you want to see. For example: "Zoom to the longest frame on the main thread," "Pin the app's RenderThread," or "Bookmark where startup ends." Based on your commands, it drives the view for you by zooming, panning, selecting slices, pinning tracks, and adding bookmarks.
- **Android-profiler skill is built in:** The AI Agent can use the built-in profiling skill to understand System Profiler (Perfetto) traces and perform deep performance analyses.
- **SQL in the search bar:** Type `:` to run a Perfetto SQL query. Results open in tabs below the timeline, and slice IDs link straight to the slice.
- **More trace data:** A new Long wakelocks track, plus counter tracks that were missing before, such as thermal, network, disk I/O, memory, and battery.
- **Easier navigation:** Area selection with `Shift+drag`, smooth animated jumps to slices, filtering tracks by several terms at once, and `Esc` to clear highlights.
- **Richer selection details:** A two-column layout, wrapped values, table cells you can copy, and callstacks for track events such as Jetpack Compose state reads.
- **Visual refresh:** Colors that match the Perfetto UI, clearer slice labels and selection outlines, and a trace view that scales with the IDE zoom level.
- **Smoother recording:** Faster device setup and recording start, the app's default activity selected for you, a searchable package list, and clearer error messages.
- **Open traces from Finder on macOS:** Android Performance Analyzer can now be your default app to open trace files on macOS. You can open the trace file directly in Android Performance Analyzer from Finder or using the `open` command in Terminal.

### Bug fixes

- Fixed system traces for some devices losing CPU scheduling data after the first second.
- Fixed GPU render stages no longer being recorded on devices with recent Android updates.
- Fixed the timeline wobbling, jittering, and freezing when zoomed in very deeply.
- Fixed device setup getting stuck, hiding installation errors, or not recovering when you click Retry.
- Fixed Android Performance Analyzer staying in the macOS Dock after you quit it.
- Fixed some traces failing to load, and FPS and Frame Time tracks being wrong during idle periods.
- Fixed undo and redo in the SQL editor.

### Other changes

- Trace Processor is updated to v58.2.
- Help buttons now open the Android Performance Analyzer documentation.

## 0.9.0-Stable (July 2026)

This release brings various usability improvements such as slice search and
property copy/paste. It also contains various bug fixes for loading and
displaying traces.

### New features and enhancements

- Support searching for slices and navigating to next or previous with Enter or Shift+Enter.
- Accelerated data load times on zoom by 2.5x for large traces.
- Add 'm' keyboard shortcut to toggle timeline measurement.
- Support selecting and copying text from the properties panel.
- Support regular expressions in slice search and track filter.
- Improved precision and visualization of timestamps in timeline ruler.
- Label the process or thread the pinned track is rooted in.
- Add checkbox to enable or disable vsync highlights.

### Fixes

- Fix: Core titles remains hidden after clearing search.
- Fix: No GPU Counters displayed for Exynos devices.
- Fix: A horizontal blue row appears and disappears when navigating trace.
- Fix: Landscape screenshot previews are squished.
- Fix: VSync highlights masked by new background color in light mode.
- Fix: Wobbly zoom on Mac trackpad when using Cmd+Scroll.

### Other

- Updated Trace Processor to v56.
- Support overriding Android SDK Location using Settings.

## 0.8.1 (June 2026)

This point release fixes a critical trace loading issue, improves light mode
visibility, and delivers smoother navigation and visual polish.

### Fixes

- Fixed an issue where traces were failing to parse or load by updating the Trace Processor to v55.3.
- Fixed an issue where VSYNC highlights were not showing up properly when using light mode.
- Fixed the wobbly zoom behavior on Mac trackpads when using Cmd + Scroll.
- Resolved a layout overlap bug in the toolbar.
- Restored the missing divider line next to expanded track groups.
- Ensured landscape screenshots are correctly oriented before being scaled down.

## 0.8.0 (May 2026)

Android Performance Analyzer is publicly released.

## Canary

## 0.10.0-Canary 6 (5th November 2026)

- Improved trace selection and visuals: Selecting and viewing trace data is now easier. Using `Shift+drag` selects across entire tracks, selected items stand out with a high-contrast outline, and a 1-pixel gap ensures tiny trace slices are no longer hidden.
- Better visibility for thread activity: Trace rows for processes without CPU data no longer appear completely empty; they now display the activity of up to 8 of their busiest threads.
- Faster loading and UI fixes: Frame Profiler captures now load faster in Canary builds, and several bugs have been fixed, including issues with lost selections and forgotten recording settings.

## 0.10.0-Canary 1 (1st September 2026)

This release brings the experimental rollout of the Frame Profiler component.