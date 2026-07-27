---
title: https://developer.android.com/games/engines/unreal/unreal-mcp-antigravity
url: https://developer.android.com/games/engines/unreal/unreal-mcp-antigravity
source: md.txt
---

[Model Context Protocol (MCP)](https://antigravity.google/docs/mcp) is an open standard that lets
developers build secure, two-way connections between AI assistants and data
sources or tools.

Starting with Unreal Engine 5.8, integrating Unreal's MCP server with
Google's Antigravity allows an AI agent in the IDE to interact directly with
the Unreal Editor. This integration lets the agent seamlessly execute editor
operations to streamline your game development workflow.

## Set up Unreal MCP for Antigravity IDE

1. Open the Unreal Editor, go to **Edit \> Plugins** , and enable the
   **Unreal MCP** and **All Toolsets** plugins. Depending on your
   workflow, you can activate additional plugins.

   ![Unreal Editor Plugins window showing the Unreal MCP plugin enabled.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-plugins1.png) **Figure 1.** Enabling Unreal MCP plugin. ![Unreal Editor Plugins window showing the All Toolsets plugin enabled.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-plugins2.png) **Figure 2.** Applying All Toolsets plugin.
2. Go to **Edit \> Editor Preferences** , locate the
   **General - Model Context Protocol** settings, and enable
   **Auto Start Server**.

   ![Unreal Editor Preferences window showing the Auto Start Server option enabled.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-preferences.png) **Figure 3.** Activating Auto Start Server.
3. To start the MCP server, restart the Unreal Editor, or in the editor
   console, enter the `ModelContextProtocol.StartServer` command.

4. Install [Antigravity IDE](https://antigravity.google/download), and sign in with your
   Google Account.

5. In the Antigravity IDE, open the **Agent** window, click
   **Additional Options** (the three-dot menu), and select
   **MCP Servers \> Manage MCP Servers \> View raw config**.

   ![Antigravity IDE Agent window with the three-dot options menu expanded, showing 'MCP Servers' as one of the menu items.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-mcp1.png) **Figure 4.** Navigating to MCP Servers. ![Antigravity IDE menu showing the path to Manage MCP Servers.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-mcp2.png) **Figure 5.** Selecting Manage MCP Servers. ![Antigravity IDE Manage MCP Servers window showing the View raw config button.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-mcp3.png) **Figure 6.** Clicking View raw config button.
6. Add this configuration to `mcp_config.json`, replacing `[YOUR_PORT]` with
   your Unreal Editor port:

       {
         "mcpServers":{
           "unreal-mcp":{
             "serverUrl":"http://127.0.0.1:[YOUR_PORT]/mcp"
           }
         }
       }

   ![Antigravity IDE text editor showing the JSON configuration for the Unreal MCP server.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-mcp4.png) **Figure 7.** Configuring the Unreal MCP server.

## Verify setup with an example

Here's an example of using Gemini within the Antigravity IDE to add a 3D
sphere to the scene.

1. In the Antigravity IDE, open the **Agent** window and enter a prompt to add
   a 3D sphere to your scene.

   ![Antigravity IDE Agent window with a user prompt to add a 3D sphere.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-example1.png) **Figure 8.** Prompting the AI agent to add a sphere.
2. In the Unreal Editor, confirm that the sphere is in the scene.

   ![Unreal Editor showing a 3D sphere successfully added to the scene.](https://developer.android.com/static/images/games/engines/unreal/unreal-mpc-antigravity-example2.png) **Figure 9.** Sphere added to the Unreal Editor scene.