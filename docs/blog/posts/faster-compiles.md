---
title: https://developer.android.com/blog/posts/faster-compiles
url: https://developer.android.com/blog/posts/faster-compiles
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# 18% Faster Compiles, 0% Compromises

###### 8-min read

![](https://developer.android.com/static/blog/assets/Android_Compile_Speed_d1a7744c0f_ZJfSB.webp) 15 Dec 2025 [![](https://developer.android.com/static/blog/assets/Santiago_Aboy_Solanes_a5f0203d61_1YKhxs.webp)](https://developer.android.com/blog/authors/santiago-solanes)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/vladimir-marko)

##### [Santiago Aboy Solanes](https://developer.android.com/blog/authors/santiago-solanes)
\&
[Vladimír Marko](https://developer.android.com/blog/authors/vladimir-marko)

The [Android Runtime (ART)](https://source.android.com/docs/core/runtime) team has reduced compile time by 18% without compromising the compiled code or any peak memory regressions. This improvement was part of our 2025 initiative to improve compile time without sacrificing memory usage or the quality of the compiled code.

Optimizing compile-time speed is crucial for ART. For example, when just-in-time (JIT) compiling it directly impacts the efficiency of applications and overall device performance. Faster compilations reduce the time before the optimizations kick in, leading to a smoother and more responsive user experience. Furthermore, for both JIT and ahead-of-time (AOT), improvements in compile-time speed translate to reduced resource consumption during the compilation process, benefiting battery life and device thermals, especially on lower-end devices.

Some of these compile-time speed improvements launched in the June 2025 Android release, and the rest will be available in the end-of-year release of Android. Furthermore, all Android users on versions 12 and above are eligible to receive these improvements through [mainline updates](https://source.android.com/docs/core/ota/modular-system).

## Optimizing the optimizing compiler

Optimizing a compiler is always a game of trade-offs. You can't just get speed for free; you have to give something up. We set a very clear and challenging goal for ourselves: make the compiler faster, but do it without introducing memory regressions and, crucially, without degrading the quality of the code it produces. If the compiler is faster but the apps run slower, we've failed.

The one resource we were willing to spend was our own development time to dig deep, investigate, and find clever solutions that met these strict criteria. Let's take a closer look at how we work to find areas to improve, as well as finding the right solutions to the various problems.

## Finding worthwhile possible optimizations

Before you can begin to optimize a metric, you have to be able to measure it. Otherwise, you can't ever be sure if you improved it or not. Luckily for us, compile time speed is fairly consistent as long as you take some precautions like using the same device you use for measuring before and after a change, and making sure you don't thermal throttle your device. On top of that, we also have deterministic measurements like compiler statistics that help us understand what's going on under the hood.

Since the resource we were sacrificing for these improvements was our development time, we wanted to be able to iterate as fast as we could. This meant that we grabbed a handful of representative apps (a mix of first-party apps, third-party apps, and the Android operating system itself) to prototype solutions. Later, we verified that the final implementation was worth it with both manual and automated testing in a widespread manner.

With that set of hand-picked apks we would trigger a manual compile locally, get a profile of the compilation, and use [pprof](https://github.com/google/pprof) to visualize where we are spending our time.
![image.png](https://developer.android.com/static/blog/assets/image_dd9a9ee49a_ZTEwkN.webp)

*Example of a profile's flame graph in pprof*

The pprof tool is very powerful and allows us to slice, filter, and sort the data to see, for example, which compiler phases or methods are taking most of the time. We will not go into detail about pprof itself; just know that if the bar is bigger then it means it took more time of the compilation.

One of these views is the "bottom up" one where you can see which methods are taking most of the time. In the image below we can see a method called Kill, accounting for over a 1% of the compile time. Some of the other top methods will also be discussed later in the blog post.
![image.png](https://developer.android.com/static/blog/assets/image_b1d0d17b7f_ZXFa8t.webp)

*Bottom up view of a profile*

In our optimizing compiler, there's a phase called Global Value Numbering (GVN). You don't have to worry about what it does as a whole, but the relevant part is to know that it has a method called \`Kill\` that it will delete some nodes according to a filter. This is time consuming as it has to iterate through all the nodes and check one by one. We noticed that there are some cases in which we know in advance that the check will be false, no matter the nodes we have alive at that point. In these cases, we can [skip iterating altogether](http://r.android.com/3469228), bringing it from 1.023% down to \~0.3% and improving GVN's runtime by \~15%.

## Implementing worthwhile optimizations

We covered how to measure and how to detect where the time is being spent, but this is only the beginning. The next step is how to optimize the time being spent compiling.

Usually, in a case like the \`Kill\` one above we would take a look at how we iterate through the nodes and do it faster by, for example, doing things in parallel or improving the algorithm itself. In fact, that's what we tried at first and only when we couldn't find anything to do we had a "Wait a minute..." moment and saw that the solution was to (in some cases) not iterate at all! When doing these kinds of optimizations, it is easy to miss the forest for the trees.

In other cases, we used a handful of different techniques including:

- using heuristics to decide whether an optimization will fail to produce worthwhile results and therefore can be skipped
- using extra data structures to cache computed data
- changing the current data structures to get a speed boost
- lazily computing results to avoid cycles in some cases
- use the right abstraction - unnecessary features can slow down the code
- avoid chasing a frequently used pointer through many loads

## How do we know if the optimizations are worth pursuing?

That's the neat part, you don't. After detecting that an area is consuming a lot of compile time and after devoting development time to try to improve it, sometimes you can't just find a solution. Maybe there's nothing to do, it will take too long to implement, it will regress another metric significantly, increase code base complexity, etc. For every successful optimization that you can see in this blog post, know that there are countless others that just didn't come to fruition.

If you are in a similar situation, try to estimate how much you are going to improve the metric by doing as little work as you can. This means, in order:

1. Estimating with a metrics you have already collected, or just a gut feeling
2. Estimating with a quick and dirty prototype
3. Implement a solution.

Don't forget to consider estimating the drawbacks of your solution. For example, if you are going to rely on extra data structures, how much memory are you willing to use?

## Diving deeper

Without further ado, let's look at some of the changes we implemented.

We implemented a [change to optimize](http://r.android.com/3473498) a method called FindReferenceInfoOf. This method was doing a linear search of a vector to find an entry. We updated that data structure to be indexed by the instruction's id so that FindReferenceInfoOf would be O(1) instead of O(n). Also, we pre-allocated the vector to avoid resizing. We slightly increased memory as we had to add an extra field which counted how many entries we inserted in the vector, but it was a small sacrifice to make as the peak memory didn't increase. This sped up our LoadStoreAnalysis phase by 34-66% which in turns gives \~0.5-1.8% compile time improvement.

We have a custom implementation of HashSet that we use in several places. Creating this data structure was taking a considerable amount of time and we found out why. Many years ago, this data structure was used in only a few places that were using very big HashSets and it was tweaked to be optimized for that. However, nowadays it was used in the opposite direction with only a few entries and with a short lifespan. This meant that we were wasting cycles by creating this huge HashSet but we only used it for a few entries before discarding it. With [this change](http://r.android.com/3480514), we improved \~1.3-2% of compile time. As an added bonus, memory usage decreased by \~0.5-1% since we weren't using as big data structures as before.

We improved \~0.5-1% of compile time by [passing data structures by reference](https://android.googlesource.com/platform/art/+/43f2b628ffc82f91af20d44bd3d50c79a00b2189%5E%21/#F0) to the lambda to avoid copying them around. This was something that was missed in the original review and sat in our codebase for years. It was thanks to taking a look at the profiles in pprof that we noticed that these methods were creating and destroying a lot of data structures, which led us to investigate and optimize them.

We sped up the phase that writes the compiled output by [caching computed values](https://android.googlesource.com/platform/art/+/42086fbafefaf8305fff3f7e40c6c68539e8505c%5E%21/#F0), which translated to \~1.3-2.8% of total compile time improvement. Sadly, the extra bookkeeping was too much and our automated testing alerted us of the memory regression. Later, we took a second look at the same code and implemented a [new version](https://android.googlesource.com/platform/art/+/9c6e669bc718429e15632c7ecf08d19a43248e33%5E%21/#F0) which not only took care of the memory regression but also improved the compile time a further \~0.5-1.8%! In this second change we had to refactor and reimagine how this phase should work, in order to get rid of one of the two data structures.

We have a phase in our optimizing compiler which inlines function calls in order to get better performance. To choose which methods to inline we use both heuristics before we do any computation, and final checks after doing work but right before we finalize the inlining. If any of those detect that the inlining is not worth it (for example, too many new instructions would be added), then we don't inline the method call.

We moved two checks from the "final checks" category to the "heuristic" category to estimate whether an inlining will succeed or not before we do any time-expensive computation. Since this is an estimate it is not perfect, but we verified that our new heuristics cover 99.9% of what was inlined before without affecting performance. One of these new heuristics was about the [needed DEX registers](http://r.android.com/3513632) (\~0.2-1.3% improvement), and the other one about [number of instructions](https://android.googlesource.com/platform/art/+/b77c09612f67ee057eab8b9fa1fc461751d38e8d%5E%21/#F0) (\~2% improvement).

We have a custom implementation of a BitVector that we use in several places. We replaced the resizable BitVector class with a simpler BitVectorView for certain fixed-size bit vectors. This eliminates some indirections and run-time range checks and speeds up the construction of the bit vector objects.

Furthermore, the BitVectorView class was templatized on the underlying storage type (instead of always using uint32_t as the old BitVector). This allows some operations, for example Union(), to process twice as many bits together on 64-bit platforms. The samples of the affected functions were reduced by more than 1% in total when compiling the Android OS. This was done across several changes \[[1](https://r.android.com/3500455), [2](https://r.android.com/3500395), [3](https://r.android.com/3501792), [4](https://r.android.com/3501794), [5](https://r.android.com/3505691), [6](https://r.android.com/3506110)\]

If we talked in detail about all the optimizations we would be here all day! If you are interested in some more optimizations, take a look at some other changes we implemented:

- [Add bookkeeping](http://r.android.com/3469440) to improve compilation times by \~0.6-1.6%.
- [Lazily compute data](http://r.android.com/3492151) to avoid cycles, if possible.
- [Refactor our code](https://android.googlesource.com/platform/art/+/bd15b243cda3f9c5038b76099e703e050890f280%5E%21/#F0) to skip precomputing work when it will not be used.
- [Avoid some dependent load chains](http://r.android.com/3497214) when the allocator can be readily obtained from other places.
- Another case of [adding a check to avoid unnecessary work](http://r.android.com/3553643).
- [Avoid frequent branching](https://android.googlesource.com/platform/art/+/bf625ebd279484bc5b0214e1659797dac2f27c8d%5E%21/#F0) on register type (core/FP) in register allocator.
- [Make sure some arrays are initialized](http://r.android.com/3802063) at compile time. Don't rely on clang to do it.
- [Clean up some loops](https://android.googlesource.com/platform/art/+/77a5d1e6464a03460fad1daa6f357f3a9e5d8f19%5E%21/#F0). Use range loops that clang can optimize better because it does not need to reload the internal pointers of the container due to loop side effects. Avoid calling the virtual function \`HInstruction::GetInputRecords()\` in the loop via the inlined \`InputAt(.)\` for each input.
- [Avoid Accept() functions](https://android.googlesource.com/platform/art/+/85f6b01b978b0543e964fa65d9d66adfedfd90cb%5E%21/#F0) for the visitor pattern by exploiting a compiler optimization.

## Conclusion

Our dedication to improving ART's compile-time speed has yielded significant improvements, making Android more fluid and efficient while also contributing to better battery life and device thermals. By diligently identifying and implementing optimizations, we've demonstrated that substantial compile-time gains are possible without compromising memory usage or code quality.

Our journey involved profiling with tools like pprof, a willingness to iterate, and sometimes even abandon less fruitful avenues. The collective efforts of the ART team have not only reduced compile time by a noteworthy percentage, but have also laid the groundwork for future advancements.

All of these improvements are available in the 2025 end-of-year Android update, and for Android 12 and above through mainline updates. We hope this deep dive into our optimization process provides valuable insights into the complexities and rewards of compiler engineering!

###### Written by:

-

  ## [Santiago Aboy Solanes](https://developer.android.com/blog/authors/santiago-solanes)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/santiago-solanes) ![](https://developer.android.com/static/blog/assets/Santiago_Aboy_Solanes_a5f0203d61_1YKhxs.webp) ![](https://developer.android.com/static/blog/assets/Santiago_Aboy_Solanes_a5f0203d61_1YKhxs.webp)
-

  ## [Vladimír Marko](https://developer.android.com/blog/authors/vladimir-marko)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/vladimir-marko) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Fourth Beta of Android 17](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17) Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability.

  ###### [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)