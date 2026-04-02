---
title: Shader pane  |  Android Developers
url: https://developer.android.com/agi/frame-trace-gui/shader-pane
source: html-scrape
---

Join us for ⁠the [Google for Games Developer Summit](https://gamedevsummit.withgoogle.com/) on March 15!

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Guides](https://developer.android.com/games/guides)

# Shader pane Stay organized with collections Save and categorize content based on your preferences.



The **Shader** pane allows you to see individual shaders used in the trace.

To use this pane, select a shader in the list. This creates a new tab that shows
the shader's source as well as static analysis statistics.

To see the specific shader bound to a specific stage in the pipeline, view that
stage in the [**Pipeline** view](/games/agi/refdocs/pipeline-view-pane).

![Shader pane](/static/images/games/agi/pane-shader.png)


**Figure 1.** **Shader** pane

## Select shader code

You can select either **SPIR-V** or, if possible, **GLSL**. Note:

* If the SPIR-V code provides the original GLSL code in its OpSource
  instruction, the **GLSL** tab simply shows the same code. If not, AGI attempts
  to decompile the SPIR-V into GLSL using SPIRV-Cross.
* If an error occurs in the decompilation, the option to show GLSL source code
  isn't available.

## Static analysis

AGI provides statistics from a static analysis of the SPIR-V shader. Here are
the statistics supported:

| Statistic | Description |
| --- | --- |
| ALU Instructions | Number of instructions in the shader that uses the ALU. |
| Texture Instructions | Number of texture fetches in the shader. |
| Branch Instructions | Number of branching instructions in the shader. |
| Peak Temporary Register Pressure | The highest number of concurrently live temporary registers. A temporary value's lifetime starts at its defition and ends at its last use in the shader. The statistic adds *p* the number of registers each live value uses (for example, a 4D float would be 4 registers). |