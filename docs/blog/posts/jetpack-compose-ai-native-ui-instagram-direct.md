---
title: https://developer.android.com/blog/posts/jetpack-compose-ai-native-ui-instagram-direct
url: https://developer.android.com/blog/posts/jetpack-compose-ai-native-ui-instagram-direct
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# How Instagram Direct engineers built AI-native UI architecture with Jetpack Compose and reduced token cost per agent session by 33%

11 min read ![](https://developer.android.com/static/blog/assets/Compose_Carousel_Strapi_3_ca1ff69fce_Z1u412n.webp) 30 Sep 2026 [![View Pavlo Stavytskyi's profile](https://developer.android.com/static/blog/assets/pavlo_a4e2ec12e9_v4xs2.webp)](https://developer.android.com/blog/authors/pavlo-stavytskyi)[![View Rebecca Franks's profile](https://developer.android.com/static/blog/assets/unnamed_12_b05cc1bf55_Z1XnKqa.webp)](https://developer.android.com/blog/authors/rebecca-franks) [Pavlo Stavytskyi](https://developer.android.com/blog/authors/pavlo-stavytskyi) \& [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks) *This blog post is written in collaboration with the Meta team*

[Instagram Direct](https://about.instagram.com/features/direct) is one of the core surfaces on Instagram, handling billions of user messages every single day. Over years of iteration, the team squeezed every micro-optimization possible out of the legacy Android View system. However, maintaining and expanding a heavily optimized legacy surface creates significant technical debt and engineering overhead, especially as teams increasingly adopt declarative UI and AI coding assistants.

Adopting [Jetpack Compose](https://developer.android.com/compose) for Instagram Direct went beyond a typical UI modernization. The team built an AI-native UI codebase that is **50% smaller** than the original implementation, while achieving a **35% reduction in AI agent execution time** , **32% fewer engineer-agent exchanges** , and a **33% reduction in token cost** . In close partnership with Google, the team adopted Jetpack Compose while maintaining a high performance bar. **Through the performance optimizations, Meta and Google improved Compose not only for Instagram, but for the broader Android developer ecosystem too.**

## **Modernizing the codebase at massive scale**

AI has rapidly become a daily companion for engineers in the industry, and applying it to a large-scale codebase like Instagram already yields real productivity gains. The Instagram Direct team set a more ambitious goal. Rather than simply pointing AI tools at the existing code, the team redesigned the codebase and its architecture to be AI-native by design, multiplying the impact of AI far beyond what retrofitting alone can deliver.

The Instagram Direct team chose Jetpack Compose as a key component for building an AI-native UI architecture. Its declarative nature ensures code is concise, predictable, and structurally easier for AI models to reason about, with fewer side effects, less implicit state, and clearer component boundaries.

The migration to Jetpack Compose required careful planning. Hundreds of millions of people send messages on Instagram every day, so the migration had to be gradual, smooth, with zero disruption to the experience while the team re-architected the foundation underneath it. To illustrate the scale of the challenge: Individual UI components can render in **over 160 distinct state permutations** , and a single conversation screen alone handles **more than 200 distinct message types**.
![Product Design 1.png](https://developer.android.com/static/blog/assets/Product_Design_1_918f61a91b_ZUSy3F.webp)

When migrating a codebase of this size to Compose, it's tempting to take the easy way out and embed Compose UI components inside the existing View hierarchy. As an incremental step during a gradual migration, that's perfectly valid. Over the long run, though, integrating Compose inside a View-based codebase poses a challenge. AI tools often take the path of least resistance. If you mix declarative and imperative UI code, AI is likely to blend them incorrectly, introducing subtle bugs, tech debt and performance regressions.

## **Building an AI-native UI architecture**

At the scale of Instagram, a degree of architectural abstraction is unavoidable, and it is what keeps the app maintainable as it grows. Consider a common pattern, where every `RecyclerViewitem` item type is modeled as a descendant of a custom `RecyclerViewItem` base class that exposes usual lifecycle hooks such as `onBind`.

**Example 1**

```kotlin
class ChatItem(
  val features: FeatureFlagProvider
) : RecyclerViewItem<ComposeViewHolder, ChatUiState> {

  // Imperative context:
  // AI could often take the path of least resistance and generate a mutable
  // state here, dispatched outside the ChatUiState. This class survives
  // re-bindings and is shared across multiple items, ultimately leading to
  // unexpected, hard-to-reproduce bugs.
  var isPinned: Boolean = false

  override fun onBind(holder: ComposeViewHolder, uiState: ChatUiState) {
      // Imperative context
      val isPinnedChatsEnabled = features.isEnabled("pinned_chats_feature")

      // Declarative context
      holder.composeView.setContent {

        // Blending imperative and declarative contexts
        if (isPinnedChatsEnabled) {
          Button(onClick = { isPinned = !isPinned }) {
            Text(if (isPinned) "Unpin" else "Pin")
          }
        }
        
        ...
      }
  }
}
```

<br />

In the snippet above, two problems creep in. First, the `isPinnedChatsEnabled` flag is read in imperative code and then captured inside a Compose lambda, a subtle coupling across paradigms. Second, `isPinned` lives as a mutable field on the item itself rather than in `ChatUiState`, so it survives `RecyclerView` re-binding and recycling across rows, leaking and producing bugs that are painful to reproduce.

Even when the code is cleaned up by giving the item a dedicated `@Composable` function, the same problems remain.

**Example 2**

```kotlin
class ChatItem(
  val features: FeatureFlagProvider
) : ComposeRecyclerViewItem<ChatUiState> {

  // Imperative context
  val isPinnedChatsEnabled = features.isEnabled("pinned_chats_feature")
  var isPinned: Boolean = false

  // Declarative context
  @Composable
  override fun Content(uiState: ChatUiState) {

 
    // Blending imperative and declarative contexts
    if (isPinnedChatsEnabled) {
      Button(onClick = { isPinned = !isPinned }) {
        Text(if (isPinned) "Unpin" else "Pin")
      }
    }

    ...
  }
}
```

This is deliberately a simple example, but it illustrates a broader issue--- the fewer boundaries AI is given, the lower the quality of the code it produces over time. Guardrails and skills help, but they are not enough on their own, because when AI hits friction it will often route around them to unblock itself.

To make the codebase AI-friendly, it needs to follow two practical rules:

- **Minimize dependency on custom context.** The more bespoke, codebase-specific knowledge an AI agent needs to make a correct change, the lower the quality of its output. The closer the codebase is to known best practices, the better the AI results.
- **An AI-first codebase must enforce its own boundaries.** Patching design gaps with AI skills doesn't scale, since every skill loaded into context costs tokens and can degrade the agent's performance. Instead, the architecture itself should carry that weight. AI agents naturally take the path of least resistance, so the design should make that path lead to correct, high-quality code, while making poor design decisions hard and expensive to express.

A list item can still be represented by its own abstraction, but in this case all the Compose code lives in the constructor, so it has no access to class members or state, and its only source of arguments is the constructor. This makes it equivalent to a plain `@Composable` function, while conforming to the existing architecture.

**Example 3**

```kotlin
class ChatItem(
  val features: FeatureFlagProvider,
  val onPin: (Boolean) -> Unit,
) : ComposeItem<ChatUiState>(

 
    // Compose UI
   content = { uiState: ChatUiState ->
    val isPinnedChatsEnabled = features.isEnabled("pinned_chats_feature")

    if (isPinnedChatsEnabled) {
      Button(onClick = { onPin(!uiState.isPinned) }) {
        Text(if (uiState.isPinned) "Unpin" else "Pin")
      }
    }
    
    ...
  },
)
```

Migrating a codebase of this size is a massive undertaking. For a long time, the hundreds of UI components that make up the majority of Direct UI had to coexist with their legacy counterparts, with both maintained in parallel. AI workflows helped make this parallel migration possible by speeding up the process of writing massive amounts of code. That approach is what let the Direct team perform the migration in record time, all without disrupting the rest of the team, who kept shipping the features that improve the experience of millions of people every day.

Multiple engineers ran their own AI agents against a shared knowledge base of reusable skills and conventions built during the migration. That kept workflows and best practices in sync across the team, rather than having each engineer rediscover them. Within each surface, the team performed the migration in the following stages:

- Write all the Compose code with AI.
- Polish it, handling edge cases and closing performance gaps, until the UI was rolled out to real users in a public test.

Splitting the work into two stages per screen lets one engineer move quickly through the entire surface, settling the architecture and the tricky edge cases up front. With that groundwork in place, others can focus on getting the UI production-ready without stopping to make those technical decisions themselves, keeping the overall migration fast.

The results of the migration validated the approach. For migrated Instagram Direct surfaces, Jetpack Compose allowed the team to **reduce the total amount of UI code by 50%**. Less code for AI to generate is associated with higher-quality output and lower token cost per task.
![Quote-Pavlo-New.jpg](https://developer.android.com/static/blog/assets/Quote_Pavlo_New_2c09049407_1B5C42.webp)

An internal data analysis of the Android codebase for Instagram Direct compared AI agent sessions working on Compose UI against the same tasks using Android Views. The efficiency gains were clear across two dimensions:

- **Per character of landed code:** Compose required **32% fewer engineer-agent exchanges** and **35% less agent execution time**(the elapsed time from when an agent starts working on an engineer's request until it returns a response).
- **Per agent session:** The overall **token cost dropped by 33%**with Compose in comparison to Views.

*We report both output efficiency and typical session numbers because they are independently useful outcomes. The engineer-agent exchanges and execution time figures compare resource use per unit of landed output, while the token figure compares total cost for a typical agent session.*

The data also revealed a consistent difference in how the two frameworks handle complex or fragile code. Meta tracks this using a risk score of code changes, which evaluates overall code quality and the likelihood of a change causing production incidents. The analysis measured an agent's **resource efficiency** using a composite of token consumption, agent's execution time and the engineer to agent interactions. As files accumulate a higher risk score, AI agent sessions naturally become less **resource efficient**.

**When a file's accumulated risk score doubles** , the UI implemented with **Android Views reduces agent resource efficiency by 30%** (per landed character). In the same circumstances, the reduction by**Jetpack Compose UI is only 9%**

Through partnership between Google and Meta, the Instagram Direct team brought a fresh perspective to Compose adoption --- approaching it through the lens of the codebase's AI-readiness, not just a UI rewrite. This work revealed Compose's strength in serving as a foundation for building AI-first codebases and architectures, especially when applied at the scale of apps like Instagram.

## **Performance optimizations**

Instagram Direct is one of the most integral surfaces of the app, and people expect it to feel fast and responsive at all times. Adopting Jetpack Compose effectively meant a substantial UI rewrite, and the number-one goal was to preserve the **high-quality experience with no regressions**.

Years of iteration had already pushed the legacy View-based implementation on Instagram to an exceptionally high performance bar, and the team needed to meet that same standard while moving to an entirely new UI framework.

Instagram measures hundreds, if not thousands, of performance metrics. For Compose adoption, the following three were the most important:

- **Time to interact** - the amount of time between opening the screen to being able to use it.
- **Time to fully load**- the amount of time between opening the screen to when all the content is fully loaded (i.e. images).
- **Scroll performance** - how smoothly the screen scrolls, without dropped frames.

These metrics are tracked at runtime in production, making it possible to run A/B tests comparing the migrated Compose UI against the legacy UI and evaluate the performance impact of this effort.

A common way to approach a migration like this is to start small, moving over a handful of UI components, gathering data, and studying how they behave. While helpful, these early results only paint a partial picture, providing false negatives against Compose adoption because:

- **Not representative** --- one migrated UI component can provide useful data about its overall performance on a particular screen. However, different components behave differently for reasons that don't generalize, so you can't always extrapolate from it.
- **Interop cost** --- a small Compose piece inside a big View codebase pays an unpredictable bridging cost between the two systems. That overhead distorts the measurement, so early small-scale results don't reflect what full migration would actually look like.

The result is that small migrations, while useful, don't always reflect the full impact of Compose.**The more of a surface is migrated end-to-end without bridging interruptions, the clearer and better the picture becomes performance-wise.**

The core screens in Instagram Direct are built around long lists of varied item types, originally implemented with `RecyclerView`. The architecture relies on custom abstractions for scalability, but it remains bound to the lifecycle of the View-based system.
![Diagram 1.png](https://developer.android.com/static/blog/assets/Diagram_1_e63ae5110e_1dDwj7.webp)

The team's primary undertaking was a gradual migration of several hundred individual list items to Compose within the existing `RecyclerView`-based architecture, rolling them out in production in small independent groups under A/B tests --- all of it without visible changes to the user's messaging experience.

The biggest downside of such a setup is a significant dependency on the legacy View system through a core `RecyclerView` architecture, even after the full migration of every list item to Compose. As a natural next step, the team decided to invest in replacing the `RecyclerView`-based core architecture with the Compose-native alternative --- `LazyColumn`.

This means Compose UI components should be abstracted away from the framework they are enclosed in while still being compatible with both `RecyclerView` and `LazyColumn` at the same time. Equally important is the ability to switch between the two at runtime via feature flags, to enable A/B testing.
![Diagram 2.png](https://developer.android.com/static/blog/assets/Diagram_2_a9c5775b7c_qwken.webp)

While the new Compose items are natively compatible with `LazyColumn` and can be plugged into an uninterrupted composition tree, an interop API was created to slot them into a `RecyclerView` as well. This made it possible to roll out the `LazyColumn` setup under an A/B test side-by-side with `RecyclerView` --- reusing the same Compose items and polishing performance, without disrupting the rest of the team building and refining features.

The scale, complexity and sensitivity of Instagram to even the smallest regressions posed a unique challenge for Jetpack Compose. Addressing these required an **iterative** , **hands-on partnership** . Working closely together, Google and Meta engineers analysed metrics to pinpoint and design new Compose capabilities to meet or exceed the View-based benchmarks. As a result of this partnership, the following additions to Jetpack Compose stand out: Pausable composition with `LazyLayoutCacheWindows` and visibility tracking.

## Pausable composition with LazyLayoutCacheWindows

Pausable composition (enabled by default in [Compose 1.10](https://android-developers.googleblog.com/2025/12/whats-new-in-jetpack-compose-december.html)) allows expensive lazy-list items to be composed incrementally across frames to prevent jank. When paired with [**LazyLayoutCacheWindow**](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/layout/LazyLayoutCacheWindow) (added in [Compose 1.9](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-december-release)), the combination significantly improves scroll smoothness. In recent internal testing at Meta, combining Pausable composition with a one-viewport `LazyLayoutCacheWindow` reduced large frame drops per minute (LFDs/m) by about 13% compared with vanilla Compose. Cache Window on its own reduced it by about 8% against the same baseline. LFDs/m is an internal metric Meta uses to track noticeable stutters while scrolling.
![Quote-Fabio.jpg](https://developer.android.com/static/blog/assets/Quote_Fabio_a38b8669d9_12HbdB.webp)

<br />

Using a [`LazyLayoutCacheWindow`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/layout/LazyLayoutCacheWindow) in your app prepares and retains off-screen items within a pixel-based band around the viewport to enable fast flings. To take advantage of `LazyLayoutCacheWindows` in your app, you can use the latest Compose 1.13.0-alpha03 and set it up as shown in the example below:

```kotlin
val cacheWindow = LazyLayoutCacheWindow(ahead = 150.dp, behind = 100.dp)
// OR
val cacheWindow = LazyLayoutCacheWindow(aheadFraction = 0.5f, behindFraction = 0.3f)

LazyColumn(state = state, cacheWindow = cacheWindow) {
    ...
}
```

There are two ways to configure the cache window. Both describe the same thing: how much off-screen content to keep composed, but in different units.

- **Dp** : fixed absolute length. `ahead = 150.dp` keeps 150dp of content composed past the visible edge regardless of device.
- **Float** : fraction of the viewport. `aheadFraction = 0.5f` keeps half a screen composed ahead, so the absolute amount scales with screen height supporting various form factors: more on a tablet or unfolded foldable, less on a compact phone.

The Instagram team fine-tuned the cache window's **float fractions** specifically for Direct's content structure and item sizes. Since the ideal values vary depending on the specific UI parameters, finding the right balance requires some experimentation.

## Impression logging with onVisibilityChanged

<br />

The[`onVisibilityChanged`](https://developer.android.com/develop/ui/compose/layouts/visibility-modifiers)(added in Compose 1.9.0) API was another key result of the technical partnership between Google and Meta. It gives large-scale Jetpack Compose surfaces a consistent way to know when a composable is actually visible on screen, replacing custom, hand-rolled implementations used in the past. Within Instagram Direct alone, these visibility signals are used across hundreds of files to support product quality metrics that depend on whether UI elements were actually shown to people.

## Startup performance

The adoption of Jetpack Compose for Instagram Direct led to unexpected performance improvements across other surfaces of the app. The Jetpack Compose runtime carries a warmup cost you pay only once, and because messaging is a high-traffic surface often visited early in a user session, other surfaces across Instagram that rely on Compose saw noticeable performance improvements.

The startup performance of Compose UI inside Instagram Direct itself was optimized through using [Baseline Profiles](https://engineering.fb.com/2025/10/01/android/accelerating-our-android-apps-with-baseline-profiles/), which pre-compile hot code paths at install time so Compose renders quickly from the very first launch.

## Lessons from the Instagram Direct migration to Jetpack Compose

- **Jetpack Compose has an immediate return on investment:** You do not need to be using advanced AI workflows to benefit from Compose. With the \~50% reduction in code, it means less code to maintain, and reduced surface area for bugs.
- **Designing an AI-native architecture led to significant wins**, including a 35% reduction in AI agent execution time, 32% fewer engineer-agent exchanges, and a 33% reduction in token cost.
- Although there are plenty of interop APIs and support for combining Views and Compose together, **aim to migrate bigger surfaces over individual small components**. This keeps the UI within a single, uninterrupted composition hierarchy and unlocks all the best Compose-native performance optimizations.
- **Pair Pausable composition with LazyLayoutCacheWindow**: Pairing these two together yields better results than cache windows alone. With only the cache window, a heavy item could still try to compose in a single pass, potentially overrunning the frame budget.
- **Contribute to Compose itself!** Meta has partnered with the Jetpack Compose team to bring their feedback and ideas to life within Compose. Working on an open-source toolkit means we all benefit when bugs and performance improvements are made centrally. So, make your [feedback](https://issuetracker.google.com/issues/new?component=612128&template=1253476) known!

Adopting Jetpack Compose unlocked significant gains in AI-assisted development while simplifying day-to-day UI engineering at Instagram. The declarative approach reduces boilerplate, makes state easier to reason about, and improves overall developer productivity. The Instagram engineering team is looking forward to bringing Compose to more surfaces across the app, and the continued collaboration between Google and Meta to bring more improvements to Instagram and Jetpack Compose users alike.

If you haven't yet tried out [Compose](https://developer.android.com/compose), now with AI-assistance, migrating to Jetpack Compose is easier than ever.

*Acknowledgements. Thank you to Michal Zielinski and Matthew Du from Meta, and Andrei Shikov and George Mount from Google, for their work bringing performance improvements to Compose through the collaboration between Meta and Google! Thank you also to Gary Ye from Meta for helping bring Compose to Instagram Direct, and to Gopal Juneja from Meta for supporting this effort through data science!*
- [#Compose-first](https://developer.android.com/blog/topics/compose-first)
- [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Written by:

-

  ## [Pavlo Stavytskyi](https://developer.android.com/blog/authors/pavlo-stavytskyi)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/pavlo-stavytskyi) ![View Pavlo Stavytskyi's profile](https://developer.android.com/static/blog/assets/pavlo_a4e2ec12e9_v4xs2.webp) ![View Pavlo Stavytskyi's profile](https://developer.android.com/static/blog/assets/pavlo_a4e2ec12e9_v4xs2.webp)
-

  ## [Rebecca Franks](https://developer.android.com/blog/authors/rebecca-franks)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/rebecca-franks) ![View Rebecca Franks's profile](https://developer.android.com/static/blog/assets/unnamed_12_b05cc1bf55_Z1XnKqa.webp) ![View Rebecca Franks's profile](https://developer.android.com/static/blog/assets/unnamed_12_b05cc1bf55_Z1XnKqa.webp)
Continue reading
- 3 Authors 27 Aug 2026 27 Aug 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_Passkeys_Strapi_2fc9df18a8_Z28fFzY.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How WhatsApp Upgraded to Secure, Seamless Sign-In for 1 Billion Users with Passkeys](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys)

  [arrow_forward](https://developer.android.com/blog/posts/how-whats-app-upgraded-to-secure-seamless-sign-in-for-1-billion-users-with-passkeys) WhatsApp is the world's largest messaging platform, serving billions of users globally. It is the default communication tool for people across diverse regions, connecting users through private, reliable, and secure messaging.
  [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang), [Mayank Jain](https://developer.android.com/blog/authors/blog-author) • 8 min read
  - [#Passkeys](https://developer.android.com/blog/topics/passkeys)
- 3 Authors 18 Aug 2026 18 Aug 2026 ![](https://developer.android.com/static/blog/assets/Copy_of_ANDDM_TINDER_Strapi_d8536aec8a_1WnFNT.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Tinder cuts app cold starts by 47% with new R8 Configuration Analyzer](https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer)

  [arrow_forward](https://developer.android.com/blog/posts/tinder-cuts-app-cold-starts-by-47-with-new-r8-configuration-analyzer) Tinder is on a mission to power and inspire real connections by making meeting easy and fun for every new generation of singles.
  [Ajesh Pai](https://developer.android.com/blog/authors/ajesh-pai), [Ulises Uriel Verduzco Díaz](https://developer.android.com/blog/authors/ulises-uriel-verduzco-diaz), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
- [![View Jonathan Starup's profile](https://developer.android.com/static/blog/assets/unnamed_10_16ef5ad5c7_Z2tS3U3.webp)](https://developer.android.com/blog/authors/jonathan-starup)[![View Andrei Shikov's profile](https://developer.android.com/static/blog/assets/unnamed_9_1eaaffc6a9_27dNln.webp)](https://developer.android.com/blog/authors/andrei-shikov) 27 Jul 2026 27 Jul 2026 ![](https://developer.android.com/static/blog/assets/0707_Faster_Kotlin_coroutines_on_Android_with_R8_Strapi_5b162a2623_wPRs6.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How R8 made Kotlin Coroutines on Android 2x faster](https://developer.android.com/blog/posts/how-r8-made-kotlin-coroutines-on-android-2x-faster)

  [arrow_forward](https://developer.android.com/blog/posts/how-r8-made-kotlin-coroutines-on-android-2x-faster) With the majority of Android apps adopting Kotlin as their main language of choice, kotlinx.coroutines has become a de-facto standard for asynchronous programming. The library offers a well-designed and structured way of managing concurrent flows that is native to Kotlin.
  [Jonathan Starup](https://developer.android.com/blog/authors/jonathan-starup), [Andrei Shikov](https://developer.android.com/blog/authors/andrei-shikov) • 7 min read
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - [#R8](https://developer.android.com/blog/topics/r8)
  - [#coroutines](https://developer.android.com/blog/topics/coroutines)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)