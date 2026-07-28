---
title: https://developer.android.com/distribute/aep/aep-integration-planner
url: https://developer.android.com/distribute/aep/aep-integration-planner
source: md.txt
---

Use this questionnaire to begin identifying your app's Apps Experience Program (AEP) requirements and potential. Select your app's capabilities and use cases in the questionnaire to generate a preliminary requirements report.
**Note:** This tool is designed to help you identify which guidelines and exemptions are relevant to your app. The output does not represent an official or final determination. It's your responsibility to identify all applicable requirements and exemptions for your app. For authoritative details, refer to the [AEP guideline documentation](https://developer.android.com/distribute/aep/aep-guidelines-overview).

## Guideline Questionnaire

Question 1 Select any of the following capabilities or content experiences supported within your app:

Select all that apply.
Video playback and streaming (including short-form video, DramaShorts, and linear/live streaming. Does not include video calling.) Streaming music, podcasts, live radio, or audiobooks Video calling or video chat Video editing Creating assets, editing photos, and building creative workflows (excluding video editing) Video capture Image capture Calling over VoIP Mapping, navigation, and finding points of interest Selecting photos or videos from the user's media library, such as for photo sharing or organization Weather tracking and reporting Note-taking, calendaring, and task management On-device actions, remote hardware management (locking doors, finding devices, checking battery or fuel levels) External content sharing (sharing app text, links, or media out to third-party apps) My app doesn't have any of these capabilities or use cases Question 2 Does the app serve content related to any of the following verticals?

Select all that apply.
Social media (excluding live-streams, chat apps, avatar generators, and dating apps) Health and fitness (fitness classes, meditations, trails, meal planning) Travel and events Shopping Food and drink (food or alcohol ordering / delivery, restaurant discovery and reservations, meal subscription boxes, reviews for restaurants, food, or drinks) Books and comics (including Manga, Webtoons, long-form UGC content, and longform blogs) Education Dating My app doesn't fall into any of these verticals or use cases Question 3 Is the app primarily intended for instant messaging?

The primary purpose is text-based communication between users who have manually shared contact information, rather than communicating to facilitate another app user journey (e.g. transactions, gaming, matching, business workflows).
Yes No Question 4 Does the app meet the Play Premium growth tools eligibility criteria?

[Read more about Play Premium growth tools eligibility criteria](https://play.google.com/console/about/guides/premium-growth-tools/)
Yes No Question 5 Does the app support a signed-in experience?

Select Yes if the app supports an account sign-in. Select No if the app is entirely anonymous without accounts.
Yes No Question 6 Does the app have high-security needs (e.g. operate or access financial, medical, or other highly sensitive user data) or regulatory compliance requirements that restrict credential restoration?

Examples include banking, fintech, healthcare, authenticators, and government apps, or apps with short-lived sessions (e.g., auto-logout within 1 hour of inactivity).
Yes No warning **Manual verification required:** High-security status must be justified during enrollment. The Play review team will verify this status. Question 7 Has the app already implemented the Block Store API? Yes No Question 8 Select all video content categories that the app provides: Streaming long-form video (movies, TV, video clips, live sports, live news, transactional video. Does not include Drama Shorts and short-form content.) Live streaming Drama shorts Short-form UGC video content (social feed) Other warning This may trigger additional requirements or exemption cases. Please review the vertical-specific guidelines for your app's use case. Question 9 Does the app include continuous or sequential prerecorded video playback where the next video is predicted?

For example, short-form video (SFV), linear playlists, or auto-playing lists.
Yes No Question 10 Does the app support bulk operations on photos (e.g., applying actions to multiple photos simultaneously)?

This does not include simple multi-select functionality.
Yes No Question 11 Does the app only access proprietary photos from its own private storage? Yes No Question 12 Does the app provide a browsable feed of media, social updates, products, or services that can be ordered or consumed digitally? Yes No Question 13 Is the app's main content strictly ephemeral with a functional lifespan under 24 hours?

For example, localized real-time inventory, live streams, or peer-to-peer chat.
Yes No Generate report Please complete all highlighted questions above to generate your report.

## Preliminary Requirements Report

edit Edit Answers <button type="reset" class="aep-reset-btn" style="padding-block: 8px; padding-inline: 16px; border: var(--tenant-primary-border); border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 500; color: var(--aep-color-text-medium); display: inline-flex; align-items: center; gap: 4px;"> restart_alt Reset All </button> To view your preliminary requirements and potential program exemptions, you must first complete all required questions in the questionnaire above and click **Generate report**. Important Notice: Preliminary Assessment Only

This report is generated based on your self-reported questionnaire answers. It does **not** constitute an official or final determination of your program requirements or exemption eligibility.

- **Developer Accuracy:** You are responsible for ensuring all questionnaire answers are complete and accurate. Incorrect inputs will yield incorrect requirements.
- **Dynamic Requirements:** Your app's requirements are subject to change if the app's functionality or target form factors change before enrollment.
- **Exemption Process:** Exemption eligibility is preliminary and subject to verification. To request an exemption, submit supporting evidence on the [AEP Get Support page](https://developer.android.com/distribute/aep/aep-get-support). This report lists common exemption scenarios, but is not exhaustive. It is the developer's responsibility to review the official program documentation to identify all exemptions for which your app may qualify.

| Requirement / Guideline | Why it applies | Potential exemptions |
|---|---|---|
| Consistent user experiences |||
| [**Cross-platform design systems**](https://developer.android.com/distribute/aep/aep-req-material-ux) (material ux, system emoji, dark theme, themed app icons, physics based motion, share sheet) | Applies to all apps | Share Sheet: App does not support sharing (Q1) |
| [**Feature Availability**](https://developer.android.com/distribute/aep/aep-req-feature-availability) | Applies to all apps |   |
| [**Title Availability**](https://developer.android.com/distribute/aep/aep-req-new-title-availability) | Applies to all apps |   |
| [**Phishing-Resistant Authentication**](https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth) | Applies to all apps | App is entirely anonymous without accounts (Q5: No) |
| [**Restore Credentials API**](https://developer.android.com/distribute/aep/aep-req-restore-credentials) | Applies to all apps | Block Store API is already implemented (Q7: Yes) App has high security constraints (Q6: Yes) App is entirely anonymous without accounts (Q5: No) |
| [**Play Content Integration**](https://developer.android.com/distribute/aep/aep-req-play-content) | Applies to all apps | App does not meet Play Premium eligibility (Q4: No) App primarily supports Video Calling (Q1) App supports VoIP Calling (Q1) App supports Mapping/Navigation (Q1) App supports Weather Tracking (Q1) App supports Instant Messaging (Q3: Yes) App supports Note-taking/Productivity (Q1) App supports IoT/Remote actions (Q1) App primarily supports live-streams (Q8: Live streaming) |
| [**Engage SDK Integration**](https://developer.android.com/distribute/aep/aep-req-engage-sdk) | Triggered by app vertical and content capabilities | App is entirely anonymous without accounts (Q5: No) App does not provide a browsable feed of content App content is strictly ephemeral with lifespan \< 24h (Q13: Yes) App vertical is Dating (Q2) |
| Reach across form factors |||
| [**Phones, Tablets, and Foldables**](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | Applies to all apps |   |
| [**XR**](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | Applies to all apps |   |
| [**Googlebook Form Factor**](https://developer.android.com/distribute/aep/aep-req-form-factor-support) Deferred (Mar 1, 2027) | Applies to all apps |   |
| [**TV**](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | Triggered by streaming video |   |
| [**Wear**](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | Triggered by audio playback, mapping/navigation, weather, or messaging |   |
| [**Auto (driving)**](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | Triggered by audio playback, mapping/navigation, or weather tracking |   |
| [**Auto (non-driving)**](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | Triggered by streaming long-form video |   |
| Stable and modern experiences |||
| [**Stability**](https://developer.android.com/distribute/aep/aep-req-stability) | Applies to all apps |   |
| [**Memory Usage Requirements**](https://developer.android.com/distribute/aep/aep-req-stability) Criteria to be shared in the coming months | Applies to all apps |   |
| [**Jetpack Compose**](https://developer.android.com/distribute/aep/aep-req-jetpack-compose) | Applies to all apps |   |
| [**Edge-to-Edge Drawing**](https://developer.android.com/distribute/aep/aep-req-edge-to-edge) | Applies to all apps |   |
| [**Predictive Back Navigation**](https://developer.android.com/distribute/aep/aep-req-predictive-background) | Applies to all apps |   |
| [**Media3 API Integration**](https://developer.android.com/distribute/aep/aep-req-media-3) | Triggered by audio playback, video playback, or video editing |   |
| [**Google Cast Support**](https://developer.android.com/distribute/aep/aep-req-cast-support) | Triggered by audio playback or streaming video | App supports Video Calling (Q1) |
| [**Android MCP**](https://developer.android.com/distribute/aep/aep-req-android-mcp) Deferred (Mar 1, 2027) | Triggered by app vertical or capabilities |   |
| [**Telecom API Integration**](https://developer.android.com/distribute/aep/aep-req-telecom-api) | Triggered by VoIP calling |   |
| [**Preload Caching Support**](https://developer.android.com/distribute/aep/aep-req-preload-caching) | Triggered by continuous or sequential video playback | App primarily supports live-streams (Q8: Live streaming) |
| [**Picture-in-Picture (PiP) Support**](https://developer.android.com/distribute/aep/aep-req-picture-in-picture) | Triggered by video playback, video calling, or navigation |   |
| [**Photo Picker Integration**](https://developer.android.com/distribute/aep/aep-req-photo-picker) | Triggered by photo/video selection | App supports bulk photo operations (Q10: Yes) App only accesses proprietary photos (Q11: Yes) |
| [**CameraX API Adoption**](https://developer.android.com/distribute/aep/aep-req-camera-x) | Triggered by image or video capture |   |
| [**Night Mode Capture Support**](https://developer.android.com/distribute/aep/aep-req-night-mode) | Triggered by image capture |   |

Your preliminary results include requirements and potential exemptions.

#### App Capabilities

- Video playback
- Audio playback
- Video calling
- Video editing
- Photo creation/editing
- Video capture
- Image capture
- VoIP calling
- Mapping \& Navigation
- Selecting photos or videos
- Weather updates
- Note-taking / Productivity
- IoT actions
- External sharing
- My app doesn't have any of these capabilities or use cases

#### App Verticals

- My app doesn't fall into any of these verticals or use cases
- Social Media
- Health \& Fitness
- Travel \& Events
- Shopping
- Food \& Drink
- Books \& Comics
- Education

#### Is the app primarily intended for instant messaging?

Yes No

#### Does the app meet the Play Premium growth tools eligibility criteria?

Yes No

#### Does the app support a signed-in experience?

Yes No

#### Does the app have high-security needs?

Yes No

#### Has the app already implemented the Block Store API?

Yes No

#### Video Content Types

- Streaming video
- Live Streaming
- Drama Shorts
- SFV Portrait
- Other

#### Does the app include continuous or sequential prerecorded video playback?

Yes No

#### Does the app support bulk photo operations?

Yes No

#### Does the app only access proprietary photos from private storage?

Yes No

#### Does the app provide a browsable feed of content?

Yes No

#### Is the app's main content strictly ephemeral with a functional lifespan under 24 hours?

Yes No Your Preliminary Requirements Your Questionnaire Answers