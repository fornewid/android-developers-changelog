---
title: https://developer.android.com/studio/debug/universal-problems-panel
url: https://developer.android.com/studio/debug/universal-problems-panel
source: md.txt
---

# View issues for your design tools in the Problems panel

The**Problems** panel in Android Studio is a centralized and shared issue panel for all design tools, such as Compose Preview, Layout Editor, and Layout Validation. To view the tool window, navigate to**View** \>**Tool Windows** \>**Problems**.

![Panel UI](https://developer.android.com/static/studio/images/debug/upp.png)**Figure 1.**You can view all the issues for your design tools in a shared issue panel.

From the**Problems** toolbar, you can see the**View Options** , such as Severity Filter and Order, the**Editor Preview** , and suggestions for**Quick Fix**.

![View Options list](https://developer.android.com/static/studio/images/debug/upp-view-optns.png)**Figure 2.** The**Problems**panel has the following view options that you can sort by either severity or name: Show Warning, Show Weak Warning, Show Server Problem, Show Typo, Show Visual Lint.

Individual issue details are displayed in the**Issue Details** pane in the**Editor Preview**. Each issue can be displayed in the built-in editor so that you can preview the code.

## View issues with visual lint

Android Studio automatically checks for visual lint issues for your layouts that are written in Views. When you open[**Layout Validation**](https://developer.android.com/studio/debug/layout-inspector#layout-validation), you can see all your layouts render in multiple device sizes. All visual issues, including background visual linting, appear in the**Problems**panel.

Visual linting rules look not only at the current file, but also at the versions of the same layout with different qualifiers--for example,`landscape`or`sw600`, if they exist when performing the analysis.

![Layout Validation UI](https://developer.android.com/static/studio/images/visual-linting.png)**Figure 3.** Visual lint issues are displayed in the**Problems**panel.