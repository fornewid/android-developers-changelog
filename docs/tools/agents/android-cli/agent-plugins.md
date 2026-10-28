---
title: https://developer.android.com/tools/agents/android-cli/agent-plugins
url: https://developer.android.com/tools/agents/android-cli/agent-plugins
source: md.txt
---

Android CLI is available to install as an official plugin for Antigravity,
Claude Code, and OpenAI's Codex. Each plugin adds the `android-cli` skill,
enabling your coding agent to create projects, manage virtual devices, inspect
live UI layouts, run Journeys, and search the official Android Knowledge Base.

In Antigravity, the Android CLI plugin comes with a deeper platform integration,
featuring interactive tools that appear right alongside your conversation:

- **Compose Previews:** See and interact with your Compose Previews as your
  agent iterates, so you can catch layout issues on different form factors
  before you ever run the app.

  **Figure 1.** Compose Previews in Antigravity.
- **Device Hub:** See and interact with virtual and physical devices from local
  or remote connections right in the agent window to validate how your app
  behaves on hardware.

  **Figure 2.** Device Hub in Antigravity.

## Install in Antigravity

To install the plugin from within an Antigravity CLI session, run:

    /plugin install android-cli-plugin@antigravity-plugins-official

Or run the following command from your terminal:

    agy plugin install android-cli-plugin@antigravity-plugins-official

In Antigravity, you can also open **Customizations \> Build with Google** and
install **Android CLI**.
![Android CLI plugin in Antigravity.](https://developer.android.com/static/tools/agents/images/agy-plugin-customizations.png) **Figure 3.** Android CLI plugin in Antigravity.

## Install in Claude

To add the marketplace and install the plugin from within a Claude Code session,
run:

    /plugin marketplace add android/android-cli-plugin
    /plugin install android-cli@android-cli-plugin

Or run the following commands from your terminal:

    claude plugin marketplace add android/android-cli-plugin
    claude plugin install android-cli@android-cli-plugin

![Android CLI plugin installed and enabled in Claude Code.](https://developer.android.com/static/tools/agents/images/claude-plugin.png) **Figure 4.** Android CLI plugin installed in Claude Code.

## Install in Codex

Run the following commands in your terminal to add the marketplace and install
the plugin in Codex:

    codex plugin marketplace add android/android-cli-plugin
    codex plugin add android-cli@android-cli-plugin

![Android CLI plugin installed in Codex.](https://developer.android.com/static/tools/agents/images/codex-plugin.png) **Figure 5.** Android CLI plugin installed in Codex.