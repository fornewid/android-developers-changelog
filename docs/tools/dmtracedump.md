---
title: https://developer.android.com/tools/dmtracedump
url: https://developer.android.com/tools/dmtracedump
source: md.txt
---

# dmtracedump

`dmtracedump`is a tool that generates graphical call-stack diagrams from trace log files. The tool uses the Graphviz Dot utility to create the graphical output, so you need to install Graphviz before running`dmtracedump`. If you haven't yet generated trace logs and saved them from your connected device to your local machine, go to[Generate trace logs by instrumenting your app](https://developer.android.com/studio/profile/generate-trace-logs).

The`dmtracedump`tool generates the call stack data as a tree diagram, where each node represents a method call. It shows call flow (from parent node to child nodes) using arrows. The diagram below shows a sample output of`dmtracedump`.

The`dmtracedump`tool is provided in the Android SDK Tools package and is located in<var translate="no">android-sdk</var>`/platform-tools/`.

## Syntax

The usage for dmtracedump is:  

```
dmtracedump [-ho] [-s sortable] [-d trace-base-name] [-g outfile] trace-base-name
```

The tool then loads trace log data from<var translate="no">trace-base-name</var>`.data`and<var translate="no">trace-base-name</var>`.key`.

### Global options

| Global options |               Description                |
|----------------|------------------------------------------|
| `-h`           | Turn on HTML output                      |
| `-o`           | Dump the trace file instead of profiling |

### Commands and command options

|              Commands and options              |                                                                                      Description                                                                                      |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-d `<var translate="no">trace-base-name</var> | Diff with this trace name                                                                                                                                                             |
| `-g `<var translate="no">outfile</var>         | Generate output to<var translate="no">outfile</var>                                                                                                                                   |
| `-s `<var translate="no">sortable</var>        | URL base to the location of the sortable javascript file                                                                                                                              |
| `-t `<var translate="no">percent</var>         | Minimum threshold for including child nodes in the graph (child's inclusive time as a percentage of parent inclusive time). If this option is not used, the default threshold is 20%. |

## Output

![](https://developer.android.com/static/images/tracedump.png)

**Figure 1.**Screenshot of dmtracedump

<br />

For each node in the graph,`dmtracedump`shows the following information:  

```
ref callname (inc-ms, exc-ms,numcalls)
```

- <var translate="no">ref</var>--- Call reference number, as used in trace logs
- <var translate="no">inc-ms</var>--- Inclusive elapsed time (milliseconds spent in method, including all child methods)
- <var translate="no">exc-ms</var>--- Exclusive elapsed time (milliseconds spent in method, not including any child methods)
- <var translate="no">numcalls</var>--- Number of calls