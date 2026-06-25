---
title: https://developer.android.com/distribute/aep/aep-req-engage-sdk
url: https://developer.android.com/distribute/aep/aep-req-engage-sdk
source: md.txt
---

Integrate Engage SDK to deliver personalized recommendations and continuation
content directly to users across multiple on-device surfaces, like Collections,
Entertainment Space, and the Play Store. This integration allows users to
discover your personalized content before they launch your app, driving higher
user re-engagement by surfacing relevant content outside the app boundaries.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Pass baseline technical criteria, including support for all required metadata fields and broadcast support for service availability.
- Publish at least one personalized recommendation cluster for logged-in users.
- Publish a continuation cluster, such as "Resume Watching", for logged-in users with at least one in-progress item.
- Update the continuation cluster within 10 minutes (ideally instantly) after a user takes an action that triggers a continuation experience and exits the app.
- Refresh recommendations at least once every 3 days to ensure content remains relevant and fresh for the user.
- Maintain content safety by filtering inappropriate content and ensure data privacy by immediately deleting content upon user logout or account deletion.

## Guideline applicability

This guideline applies to:

- Apps that have the following use cases:
  - Streaming video (Movies, TV, video clips, live sports, live news, transactional video, Drama Shorts, and educational videos)
  - Streaming audio (Music, Podcasts, Live Radio, Audiobooks)
  - Social media (excluding live-streams, chat apps, and avatar generators)
  - Health and Fitness classes, meditations, trails, or meal planning
  - Travel and Event discovery, booking, and planning
  - Shopping
  - Food and Drink (food or alcohol ordering / delivery, restaurant discovery and reservations, meal subscription boxes, reviews for restaurants, food, or drinks)
  - Books and Comics (including Manga, Webtoons, long-form UGC content, and longform Blogs)
  - Education (videos and lessons)
- Phone and tablet form factors.

## Exemptions

The following exemptions apply to this guideline:

- Apps that don't meet the [Engage SDK](https://developer.android.com/guide/playcore/engage/preview#eligibility) eligibility criteria.
- Apps whose main content type can quickly become stale: live-streams, ephemeral recommendations (such as limited shopping inventory), and chat apps.
- Apps that don't provide a signed-in experience.
- Apps that don't provide native recommendations are exempt from publishing recommendations.
- Apps that don't provide native personalized recommendations can provide non-personalized recommendations, consistent with what they provide in their own app.
- Apps without native continuation journeys are exempt from continuation content.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Engage SDK**. These resources are for your reference only and don't
contain additional program requirements.

- [Engage SDK Guide](https://developer.android.com/guide/playcore/engage)