---
title: https://developer.android.com/blog/posts/inside-android-skills-built-for-deprecation
url: https://developer.android.com/blog/posts/inside-android-skills-built-for-deprecation
source: md.txt
---

[Community](https://developer.android.com/blog/categories/community)

# Inside Android Skills - Built for deprecation

4 min read ![](https://developer.android.com/static/blog/assets/Inside_Android_Skills_Built_for_deprecation_Strapi_V01_8f34b79673_MYo9i.webp) 06 Aug 2026 [![View Jose Alcérreca's profile](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp)](https://developer.android.com/blog/authors/jose-alcerreca) [Jose Alcérreca](https://developer.android.com/blog/authors/jose-alcerreca) Developer Relations Engineer We released the official [Android Skills](https://github.com/android/skills)in April, and the response surpassed all our expectations. In this blog post, I'll address some of the feedback we received, explaining the philosophy and methodology behind the project. Hopefully, this will also help you understand what happens behind the scenes when you install and use skills, allowing you to make better use of tokens and your own time.

## Why are there so few official skills?

Currently, we only consider new skills when there's a verifiable knowledge gap in state-of-the-art (SOTA) models. Put simply: you don't need to teach the model what it already knows. (Though there are a few exceptions---read on!)

We've released around 20 official skills so far, and they intentionally target highly specific, fast-moving areas that standard models aren't fully grounded on yet---things like AGP 9, Navigation 3, advanced Camera APIs, and Perfetto SQL.

What about core, more general, skills? Every installed skill injects 100--200 tokens into the baseline context of every task you start. If that skill actually activates, that count can quickly jump into the thousands. In most cases, hoarding basic skills is both counterproductive and expensive. Before installing a skill for writing basic Kotlin or Compose, consider if your LLM of choice really needs it, or if it knows those topics well enough already.

## Evaluating skills

Before their release, each skill is tested against a comprehensive set of evals that prove that the skill delivers clear value. These evals should pass when the skill is active, and fail otherwise. Evals are to skills what integration tests are to code.

```
timeout_s: 1200
repository:
  url: [redacted - internal git repo]
  working_dir: wear_compose_m3_empty_app
category_ids:
  - wear
prompt: |-
  Add a horizontal pager to MainActivity.kt. Have three pages in the pager. Each page should contain
  the text "Page 1", "Page 2", and "Page 3" respectively in the center of the screen.
commands:
  build:
    - ./gradlew assembleDebug
acceptance_criteria:
  project_builds: true
  llm_diff_judge:
    - Must use `HorizontalPagerScaffold`.
    - Each page should use `AnimatedPage` to wrap a `ScreenScaffold`.
```

*Example eval that checks the correct implementation of a horizontal pager on a wear app*

At a minimum, we test the skill in Android Studio using the latest Gemini Flash model. Depending on the skill, we also ensure compatibility with other models such as Gemini Pro and other agents such as Antigravity, and third-party systems.

All of the evals run with access to the [Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources#android-knowledge-base), so if the information is in the documentation, and models decide to search for it, we don't publish a skill for it.

## Using the Android Knowledge Base (Android Studio or Android CLI)

If you develop Android apps, you should always use the Android Knowledge Base to have access to the official documentation. If you use the agent in Android Studio, it's already available as a tool, but if you use another agent, [install Android CLI](https://developer.android.com/tools/agents). Among other things, it contains the docs command, which gives your agent access to the official Android documentation. Having a single tool is much more efficient than installing hundreds of skills.

If your model is acting overconfident, and you want it to consult the documentation more often, a very common way to motivate it is to add "Always consult the official Android documentation when dealing with Android APIs" to your AGENTS.md file or equivalent. Of course, you can also force this by asking the agent to check the documentation directly in your prompts.

## Why are pull requests disabled?

Because our evaluation framework depends on internal infrastructure that cannot be open-sourced, we are unable to accept direct pull requests for new skills---without this infrastructure, we would have no way to re-evaluate incoming PR changes. However, we actively monitor community feedback. If you want to report a bug, suggest an optimization, or request a new official skill, please file an [issue](https://github.com/android/skills/issues)!

## When do core or basic skills make sense?

While SOTA models generally don't need basic skills, there are some scenarios where enabling core or community-built skills adds real value. For example:

- **You're using vague prompts**: Skills amplify your intent. If you give a loose prompt like "add animations to this screen," a specific Compose animation skill can inspire the model, pushing it toward modern APIs or screenshot testing patterns it might not have otherwise considered.
- **You want to use smaller, cheaper models**: Frontier LLMs are expensive. If you are offloading routine tasks to smaller open-weight models like Gemma 4, enabling basic skills fills the knowledge gaps that smaller parameters miss.
- **You're refactoring or reviewing legacy code:** Models excel at generating code that works, but when editing old codebases, they often prioritize staying consistent with the surrounding legacy patterns over rewriting things with modern accuracy. A specialized reviewer agent equipped with core skills can help break that habit.
- **You deviate from the norm**: LLMs love the standard "Google way" of architecting Android apps. If your team uses a highly customized view-layer architecture, the model will struggle to stay aligned. A custom skill explicitly describing your architecture goes a long way.

## Where can I find core skills?

The Android community has your back. Chris Banes has [a comprehensive collection of skills for Compose and Kotlin](https://github.com/chrisbanes/skills), Ivan Morguillo published [a skill that audits Compose projects](https://github.com/hamen/compose_skill), and Jaewoong Eum created two on [testing](https://github.com/skydoves/compose-performance-skills) and [performance](https://github.com/skydoves/compose-performance-skills).

Always download skills from reputable sources! I personally wouldn't trust repositories containing dozens or hundreds of Android skills as they're probably AI-generated and untested, and they could even contain malicious or biased instructions. Also, don't install general software engineering skills blindly; a lot of them are tailored for web development.

## Goal: deprecation

Loosely paraphrasing Karpathy: *Skills of today will be in the models of tomorrow*. As SOTA models keep improving, we expect skills to be obsolete, especially those built around new APIs. To figure out when to retire them, we run our evals when new models drop. If they pass, we'll keep them around for a few months until most users have transitioned over.
- [#AI-assisted coding](https://developer.android.com/blog/topics/ai-assisted-coding)
- [#Android Skills](https://developer.android.com/blog/topics/android-skills)
Written by:

-

  ## [Jose Alcérreca](https://developer.android.com/blog/authors/jose-alcerreca)

  ###### Developer Relations Engineer

  [read_more View profile](https://developer.android.com/blog/authors/jose-alcerreca) ![View Jose Alcérreca's profile](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp) ![View Jose Alcérreca's profile](https://developer.android.com/static/blog/assets/jose_21a476d0ec_23cCms.webp)
Continue reading
- [![View Steph Pio's profile](https://developer.android.com/static/blog/assets/security_pass_photo_b9ab37d5bf_1fkXBh.webp)](https://developer.android.com/blog/authors/steph-pio) 06 Jul 2026 06 Jul 2026 ![](https://developer.android.com/static/blog/assets/IG_Fund26_Strapi_Header_716b75cbab_1E2Dt5.webp) [Community](https://developer.android.com/blog/categories/community)

  ## [Google Play launches the first Indie Games Fund in Africa](https://developer.android.com/blog/posts/google-play-launches-the-first-indie-games-fund-in-africa)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-launches-the-first-indie-games-fund-in-africa) Google Play is launching the first Indie Games Fund in Africa, investing $1 million to empower 10 indie game studios across Sub-Saharan Africa.
  [Steph Pio](https://developer.android.com/blog/authors/steph-pio) • 1 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play)
- [![View Robbie McLachlan's profile](https://developer.android.com/static/blog/assets/Robbie_280bd4586c_2wmcrw.webp)](https://developer.android.com/blog/authors/robbie-mclachlan) 25 Mar 2026 25 Mar 2026 ![](https://developer.android.com/static/blog/assets/Meet_The_Class_2_bb4f1ec5bd_Z1MklPk.webp) [Community](https://developer.android.com/blog/categories/community)

  ## [Meet the class of 2026 for the Google Play Apps Accelerator](https://developer.android.com/blog/posts/meet-the-class-of-2026-for-the-google-play-apps-accelerator)

  [arrow_forward](https://developer.android.com/blog/posts/meet-the-class-of-2026-for-the-google-play-apps-accelerator) The wait is over! We are incredibly excited to share the Google Play Apps Accelerator class of 2026.
  [Robbie McLachlan](https://developer.android.com/blog/authors/robbie-mclachlan) • 1 min read
- [![View Robbie McLachlan's profile](https://developer.android.com/static/blog/assets/Robbie_280bd4586c_2wmcrw.webp)](https://developer.android.com/blog/authors/robbie-mclachlan) 11 Dec 2025 11 Dec 2025 ![](https://developer.android.com/static/blog/assets/Android_Devs_Google_Devs_Blog_Header_1200x600_79350b0b52_1w8gkH.webp) [Community](https://developer.android.com/blog/categories/community)

  ## [#WeArePlay: How Matraquina helps non-verbal kids communicate](https://developer.android.com/blog/posts/we-are-play-how-matraquina-helps-non-verbal-kids-communicate)

  [arrow_forward](https://developer.android.com/blog/posts/we-are-play-how-matraquina-helps-non-verbal-kids-communicate) In our latest #WeArePlay film, we meet Adriano, Wagner and Grazyelle. The trio are behind Matraquinha, an app helping thousands of non-verbal children in more than 80 countries communicate.
  [Robbie McLachlan](https://developer.android.com/blog/authors/robbie-mclachlan) • 2 min read
Stay in the loop

Get the latest Android development insights delivered to your inbox weekly.
[mail Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)