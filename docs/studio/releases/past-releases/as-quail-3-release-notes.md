---
title: https://developer.android.com/studio/releases/past-releases/as-quail-3-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-quail-3-release-notes
source: md.txt
---

The following are the release notes for Android Studio Quail 3.

## Patch releases

The following is a list of patch releases for Android Studio Quail 3.

### Android Studio Quail 3 \| 2026.1.3 Patch 1 (August 2026)

This minor updates includes [these bug
fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2026.1.3#android-studio-quail-3-%7C-2026.1.3-patch-1).

The following are new features in Android Studio Quail 3.

## Improvements to Planning Mode

[Planning Mode](https://developer.android.com/studio/releases/past-releases/as-panda-4-release-notes#planning-mode)
facilitates a multi-stage reasoning process, giving the agent more space
to evaluate its own proposed logic for potential issues before presenting it
to you. This is especially useful for complex and long-running tasks which
demand a high degree of precision.

### How to use Planning Mode

You can explicitly kick off Planning Mode by including the **`/plan`** command
in your prompt, or by asking the agent to generate a plan before it starts
implementing code.
![Ask the agent to come up with a plan or use /plan explicitly.](https://developer.android.com/static/studio/images/planning-mode-prompt.png) Ask the agent to come up with a plan or use `/plan` explicitly.

Once the agent examines your request and generates an implementation plan,
you can review it. You can iterate on the plan with the agent, going back
and forth to fix mistakes or clarify which approaches to use---all before
the agent has spent any time or tokens executing actions.
![Open and review the plan.](https://developer.android.com/static/studio/images/planning-mode-review-plan.png) Open and review the plan.

Add your feedback directly to the plan and send it to the agent by clicking
**Submit comments**. The agent will use your comments to revise the proposed
implementation.
![Add comments and submit them. The agent regenerates the plan incorporating the new feedback.](https://developer.android.com/static/studio/images/planning-mode-submit-comments.png) Add comments and submit them. The agent regenerates the plan incorporating the new feedback.

When you are completely satisfied with the plan, click **Proceed** to
implement the plan.
![Click on Proceed to approve the plan and kick off the implementation.](https://developer.android.com/static/studio/images/planning-mode-proceed.png) Click on **Proceed** to approve the plan and kick off the implementation.

After the work is done, the agent produces a summary of exactly what has been
changed, so you can review the updates.
![Get a summary of changes once implementation is complete.](https://developer.android.com/static/studio/images/planning-mode-summary.png) Get a summary of changes once implementation is complete.

## MCP Marketplace

Starting in Quail 3, we're making it easier for you to find and add MCP servers.
Navigate to **Settings \> Tools \> AI \> MCP Servers** to browse for a server and
install it.
![](https://developer.android.com/static/studio/releases/assistant/2026.1.3/mcp-marketplace.png)

The **Marketplace** tab lists all the servers available on
[ModelContextProtocol.io](http://modelcontextprotocol.io/). Click the gear icon to switch to a custom
registry or to filter by MCP server type (such as **NPX** , **Docker** , or
**Python**).
![](https://developer.android.com/static/studio/releases/assistant/2026.1.3/mcp-servers.png)

## Merge Conflicts action

Quail 3 introduces a new
![](https://developer.android.com/static/studio/releases/assistant/2026.1.3/resolve-conflicts-icon.svg)
**Merge Conflicts with Agent** button into the **Commit** tool window that
instructs the agent to automatically merge conflicts. When there are one or more
conflicting files in the repositories, you can click this button to launch a new
agent session targeting those files.