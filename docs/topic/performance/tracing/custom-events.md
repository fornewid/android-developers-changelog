---
title: https://developer.android.com/topic/performance/tracing/custom-events
url: https://developer.android.com/topic/performance/tracing/custom-events
source: md.txt
---

# Define custom events

System tracing shows you information about processes only at the system level, so it's sometimes difficult to know which of your app or game's methods are executing at a given time relative to system events.

Jetpack provides a tracing API that you can use to label a particular section of code. This information is then reported in traces captured on the device.[Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)captures traces with custom trace points automatically.

When using the systrace command line tool to capture traces, the`-a`option is required. Without this option, your app's methods don't appear in a system trace report.  

### Kotlin

```kotlin
class MyAdapter : RecyclerView.Adapter<MyViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup,
            viewType: Int): MyViewHolder {
        trace("MyAdapter.onCreateViewHolder") {
            MyViewHolder.newInstance(parent)
        }
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        trace("MyAdapter.onBindViewHolder") {
            trace("MyAdapter.queryDatabase")
                val rowItem = queryDatabase(position)
                dataset.add(rowItem)
            }
            holder.bind(dataset[position])
        }
    }
}
```

### Java

```java
public class MyAdapter extends RecyclerView.Adapter<MyViewHolder> {
    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return TraceKt.trace(
            "MyAdapter.onCreateViewHolder",
            () -> MyViewHolder.newInstance(parent)
        );
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        TraceKt.trace(
            "MyAdapter.onBindViewHolder",
            () -> {
                TraceKt.trace(
                    "MyAdapter.queryDatabase",
                    () -> {
                        Item rowItem = queryDatabase(position);
                        dataset.add(rowItem);
                    }
                );
            }
        );
    }
}
```

We recommend using the Kotlin extension function, even in Java code, as it automatically ends the trace when the lambda completes. This removes the risk of forgetting to end the tracing.

You can also use an NDK API for custom trace events. To learn about using this API for your native code, see[Custom trace events in native code](https://developer.android.com/topic/performance/tracing/custom-events-native).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [App startup time](https://developer.android.com/topic/performance/vitals/launch-time)
- [Slow rendering](https://developer.android.com/topic/performance/vitals/render)