---
title: https://developer.android.com/android-performance-analyzer/agentic
url: https://developer.android.com/android-performance-analyzer/agentic
source: md.txt
---

Android Performance Analyzer includes agentic capabilities that let your agent interact directly
with the [trace view](https://developer.android.com/android-performance-analyzer/view.md.txt) and query the data it contains.
![](https://developer.android.com/static/android-performance-analyzer/images/agent-panel-hero.png) **Figure 1**: The agent panel alongside a trace view.

> [!NOTE]
> **Note:** The agentic capabilities in Android Performance Analyzer only work with the System Profiler.

## Agent tools

The tool support in Android Performance Analyzer gives agents the following capabilities:

- **Read the trace view.** The agent can see exactly what you see in the trace view pane: visible time range, selected slices, pinned tracks, visible tracks, bookmarks, and highlights.
- **Query the trace.** The agent has full access to all of the data collected in the trace and the ability to run whatever queries are needed.
- **Update the trace view.** The agent can pan and zoom the trace view, pin or unpin tracks, select slices and time ranges, and place bookmarks according to your instructions.

## Open the agent panel

To open the agent panel, do one of the following:

- Click the ![](https://developer.android.com/static/studio/images/agent-icon.png) **Agent** button from the sidebar.
- Select **View \> Tool Windows \> Agent** from the menu bar.
- Click the ![](https://developer.android.com/static/images/picto-icons/gemini.svg) **Ask
  AI** button from your trace view.

The agent panel works the same as the [agent panel in Android Studio](https://developer.android.com/studio/gemini/agent-mode.md.txt).

## Bring your own agent

In addition to Google Antigravity, Android Performance Analyzer also supports Bring Your Own
Agent (BYOA). Select an agent from the **Agents** menu, or select **Configure
Agents** to see the Agent Marketplace.
![](https://developer.android.com/static/android-performance-analyzer/images/agent-select.webp) **Figure 2** : The **Agents** menu in the agent panel.

When you've selected an agent, follow the instructions to authenticate and
connect your account.

## Agentic performance analysis

The agentic integrations give you powerful, flexible tools to interact with your
traces using natural language. Here are some examples to demonstrate a few of
the ways your agent can streamline your analysis.

### Find and pin threads

**Prompt:** Pin the app's main thread.

The agent queries the trace, locates the thread designated as the main thread,
and pins it directly in the trace view.
![](https://developer.android.com/static/android-performance-analyzer/images/agent-ex-pinthreads.png) **Figure 3**: The agent's ability to find and pin threads.

### Apply highlights and bookmarks

**Prompt:** Highlight the time range of the `bindApplication` slice, then put
bookmarks at the start and end of that slice.

The agent queries the trace to find the requested slice, highlights and selects
its time range, and places bookmarks as requested.
![](https://developer.android.com/static/android-performance-analyzer/images/agent-ex-bookmarks.png) **Figure 4**: The agent's ability to identify slices and place bookmarks.

### Find long-rendering frames

**Prompt:** Find the frame with the longest render time.

The agent queries the trace to identify the frame with the longest render time.
It then produces a breakdown of the time spent on the frame, and it centers and
selects the corresponding `Choreographer#doFrame` slice for easier inspection.
![](https://developer.android.com/static/android-performance-analyzer/images/agent-ex-longframe.png) **Figure 5**: The agent's ability to find long-rendering frames.