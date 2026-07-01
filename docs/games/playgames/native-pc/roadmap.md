---
title: https://developer.android.com/games/playgames/native-pc/roadmap
url: https://developer.android.com/games/playgames/native-pc/roadmap
source: md.txt
---

This page outlines the roadmap for Google Play Games on PC (Native PC)
features, including what's available and what's planned for future
releases.

> [!NOTE]
> **Note:** Timelines provided on this page represent current planning and are subject to change or delay based on development and testing.

## 2026 June update

This section details the status of features and key releases for the 2026 June
update.

### Feature roadmap

We're continuously working to improve the developer and user experience on
Google Play Games on PC. Here's the status of key features:

| Feature Category | Feature | Status | Details |
|---|---|---|---|
| **Testing Capability** | PC app creation | Planned (Aug 2026) | Self-configured PC track in Play Console. |
|   | Country targeting | Planned (Aug 2026) | Target specific countries for PC releases. |
|   | Internal Testing Track | Planned (Aug 2026) | Support for internal testing track for PC builds. |
|   | App reviews \& appeals | Planned (Aug 2026) | Manage reviews, rejections, and appeals in Play Console. |
|   | Store listing management | Planned (Aug 2026) | Configure PC-specific store listings. |
|   | Windows Authenticode | Planned (Aug 2026) | Support for Authenticode submission. |
|   | Reporting \& Analytics | Planned (Aug 2026) | Visits, installs, engagement, and revenue reporting. |
| **Billing \& Payments** | Seamless Purchase Flow | **Available** | In-game checkout within the game client. |
|   | Client-side verification | **Available** | Client-side billing verification (requires [allowlisting](https://issuetracker.google.com/issues/new?component=175792)). |
|   | Purchase callbacks | **Available** | Callbacks for billing verification. |
|   | Extended status callbacks | Planned (Aug 2026) | Callbacks for pending, user cancellation, etc. |
| **Essential Features** | Unity Wrapper Plugin | **Available** | Plugin for Unity supporting Init, Integrity, and Billing. |
|   | Play Managed Installs | Planned (Aug 2026) | Simplified distribution, Google Play handles installation. |
|   | Play Managed EULA | Planned (Aug 2026) | Support for managed EULA. |
|   | Cloud Save \& Achievements | Planned (Aug 2026) | Cross-platform APIs for Android and PC. |
| **Support \& Tools** | Developer Tool | Planned (Aug 2026) | WAB validation and generation tool. |
| **Desktop Launcher** | gSession ID Passing | **Available** | Passing session ID to installer. |
|   | 3P Launcher Integration | Planned (Aug 2026) | Better install and launch flow for 3P launchers. |
|   | Thin GPG Client | Planned (Aug 2026) | Faster install with on-demand components. |
|   | Custom Install Folder | Planned (Aug 2026) | Allow users to choose installation location. |
|   | Lifecycle SDK | Planned (Aug 2026) | SDK for launcher handshake and metrics. |

### SDK integration architecture

It's important to distinguish between the **Lifecycle SDK** and the **PC Native
SDK**, also called the Play Games PC SDK:

- **PC Native SDK:** Integrated directly into the **game executable**. It provides access to Google Play services like Play Billing, Play Integrity, and Seamless Sign-in (Recall API).
- **Lifecycle SDK:** Integrated into the developer's **installer executable** or **third-party launcher executable**. It manages communication between the Google Play Games client and the launcher or installer, ensuring correct startup parameters and capturing metrics.

The following diagram and steps illustrate the relationship and execution flow
between the Google Play Games client, the developer's installer, the 3P
launcher, and the game:
![SDK integration architecture and execution flow](https://developer.android.com/static/games/playgames/native-pc/images/sdk_architecture.svg) SDK integration architecture and execution flow

1. **Launch/Update:** The **Google Play Games Client** initiates the process by launching or updating the developer's **Installer** (which uses the Lifecycle SDK).
2. **Launcher Startup:** The **Installer** installs the game components and then launches the developer's **3P Launcher** (also using the Lifecycle SDK).
3. **Game Launch:** The **3P Launcher** launches the final **Game Executable** , passing the GPG session token using the `--g_session_token=<TOKEN>` command-line argument.
4. **SDK Initialization:** The **Game Executable** starts up and initializes the **PC Native SDK** using the passed token. This establishes the authenticated session back to the **Google Play Games Client**.

### Key upcoming releases

The following sections highlight key upcoming releases for the platform.

### Unified Play Console for PC (Early Access in Aug 2026)

We are introducing a unified interface in the Play Console to manage
distribution across Android and Windows PC platforms.
![Unified Play Console Packaging Options](https://developer.android.com/static/games/playgames/native-pc/images/roadmap_packaging.png) Unified Play Console packaging options

This lets you:

- Manage PC app creation and publishing.
- Configure store listings and experiments.
- Access reporting for visits, installs, engagement, and revenue.

### Developer tool (August 2026)

We're developing a tool that helps you validate and generate GPG publishing
configurations to prevent common mistakes.
![Preview of the configuration interface for the developer tool](https://developer.android.com/static/games/playgames/native-pc/images/roadmap_developer_tool.png) Developer tool configuration preview

### Play managed installs (August 2026)

Google Play can automatically handle the complexities of installing and
updating your game, removing the need for you to write custom installers.

### Lifecycle SDK for Launchers (Aug 2026)

For developers with their own desktop launchers, the Lifecycle SDK ensures a
seamless game launching experience from GPG or your launcher. It handles a
direct handshake between the game and GPG, unlocking full Android-parity
metrics in the Play Console.

### Thin GPG client (August 2026)

We're working on a faster GPG client install that uses on-demand
installation of additional components. Early testing shows 3x faster
install time.
![Thin GPG Client Mock](https://developer.android.com/static/games/playgames/native-pc/images/roadmap_thin_client.png) Thin GPG client installation preview

### Custom install folder (August 2026)

Users can choose their preferred installation location,
which ensures optimal storage management across multiple drives.
![Custom Install Folder Mock](https://developer.android.com/static/games/playgames/native-pc/images/roadmap_custom_folder.png) Custom install folder configuration preview

## Additional resources

- [Launch checklist](https://developer.android.com/games/playgames/native-pc/checklist)
- [Frequently asked questions](https://developer.android.com/games/playgames/native-pc/faq)