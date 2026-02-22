---
title: https://developer.android.com/studio/gemini/add-mcp-server
url: https://developer.android.com/studio/gemini/add-mcp-server
source: md.txt
---

**Preview:** The ability to connect to remote MCP servers is available starting with Android Studio Otter 1 Canary 3.[See the preview release note](https://developer.android.com/studio/preview/features#remote-mcp).  

Gemini in Android Studio's agent can interact with external tools using the[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction). This feature provides a standardized way for Agent mode to use tools and extend knowledge and capabilities with the external environment.

There are many tools you can connect to the MCP Host in Android Studio. For example, you can integrate with the[GitHub MCP Server](https://github.com/github/github-mcp-server)to create pull requests directly from Android Studio or with the[Figma remote MCP server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)to provide design information without downloading the desktop app. For more ideas, see the[MCP example servers](https://modelcontextprotocol.io/examples).

To add an MCP server, follow these steps:

1. Go to the MCP server settings by clicking**File** (**Android Studio** on macOS)**\> Settings \> Tools \> Gemini \> MCP Servers**.
2. Select**Enable MCP Servers**.
3. Add the MCP configuration in the field provided. The configuration is saved in an`mcp.json`file in the[configuration directory](https://developer.android.com/studio/troubleshoot#directories)of Android Studio.
4. Click**OK**.

The following example shows an`mcp.json`file with several server configurations:  

    {
      "mcpServers": {
        "figma": {
          "httpUrl": "https://mcp.figma.com/mcp"
        },
        "github": {
          "httpUrl": "https://api.githubcopilot.com/mcp/",
          "headers": {
            "Authorization": "Bearer <YOUR_PERSONAL_ACCESS_TOKEN>"
          }
        },
        "gitlab": {
          "httpUrl": "https://gitlab.com/api/v4/mcp"
        },
        "canva": {
          "httpUrl": "https://mcp.canva.com/mcp"
        },
        "notion": {
          "httpUrl": "https://mcp.notion.com/mcp"
        },
        "linear": {
          "httpUrl": "https://mcp.linear.app/mcp"
        }
      }
    }

For the precise configuration values to list in this file, see the documentation for the MCP server that you're integrating with.

## Authentication

After clicking**OK**, you will either see a notification saying "Successfully connected to MCP server..." or a notification describing an error. Most remote MCP Servers require authentication and therefore return "Error connecting to transport: Authorization Exception" when authorization fails.

Click**Start Login**to initiate the authentication process for that server. You will be asked to sign in to that server's login page in your browser. After you log in, the connection is attempted again and, if successful, you will see the "Successfully connected to MCP server..." notification.

## Use MCP tools

To see which tools are available to Gemini in Android Studio, type`/mcp`in the chat.

You can then reference the tools in the chat, for example, "list my repositories on GitHub".

## Configurations

This section describes all the MCP server configuration options.

### HTTP MCP server

The following table lists the configuration options for connecting to an MCP server through a streamable HTTP transport.
| **Note:** Some MCP servers provide an HTTP Server-Sent Events (SSE) endpoint, which is usually indicated by`/sse`in the URL. If you're connecting to an SSE endpoint instead of a streamable HTTP endpoint, use`url`instead of`httpUrl`to specify the URL.

|   Name    |         Type          |                                                         Description                                                          |
|-----------|-----------------------|------------------------------------------------------------------------------------------------------------------------------|
| `httpUrl` | String                | Required. The full URL of the streamable HTTP endpoint (for example,`https://example.com/mcp`or`http://localhost:1234/mcp`). |
| `headers` | Map\<String, String\> | A map of custom HTTP headers to include in the connection request. Defaults to`{}`(an empty map).                            |
| `timeout` | Long                  | Connection timeout in milliseconds. -1 indicates no timeout. Defaults to -1.                                                 |
| `enabled` | Boolean               | Whether this server configuration is active. Defaults to`true`.                                                              |

## Limitations

Android Studio's MCP integration doesn't support the following features:

- Connection to MCP servers through`stdio`transport
- MCP resources
- Prompt templates
- OAuth login with some MCP servers, such as GitHub