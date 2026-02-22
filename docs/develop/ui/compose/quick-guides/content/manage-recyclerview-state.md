---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/manage-recyclerview-state
url: https://developer.android.com/develop/ui/compose/quick-guides/content/manage-recyclerview-state
source: md.txt
---

<br />

[`RecyclerView`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView) can display large amounts of data using minimal graphical
resources. As users scroll through the items in a `RecyclerView`, `View`
instances of items that have scrolled off screen are reused to create new items
as they scroll on screen. But configuration changes, such as device rotation,
can reset the state of a `RecyclerView`, forcing users to again scroll to their
previous position in the list of items.

`RecyclerView` should maintain its state---in particular, scroll
position---and the state of its list elements during all configuration
changes.

## Results

Your `RecyclerView` is able to restore its scroll position and the state of
every item in the `RecyclerView` list.

## Version compatibility

This implementation is compatible with all API levels.

### Dependencies

None.

## Maintain state

Set the state restoration policy of the `RecyclerView.Adapter` to save the
`RecyclerView` scroll position. Save the state of `RecyclerView` list items. Add
the state of the list items to the `RecyclerView` adapter, and restore the state
of list items when they're bound to a `ViewHolder`.

### 1. Enable `Adapter` state restoration policy

Enable the state restoration policy of the `RecyclerView` adapter so that the
scrolling position of the `RecyclerView` is maintained across configuration
changes. Add the policy specification to the adapter constructor:  

### Kotlin

    class MyAdapter() : RecyclerView.Adapter<RecyclerView.ViewHolder>() {
        init {
            stateRestorationPolicy = StateRestorationPolicy.PREVENT_WHEN_EMPTY
        }
        ...
    }

### Java

    class MyAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

        public Adapter() {
            setStateRestorationPolicy(StateRestorationPolicy.PREVENT_WHEN_EMPTY);
        }
        ...
    }

### 2. Save the state of stateful list items

Save the state of complex `RecyclerView` list items, such as items that contain
`EditText` elements. For example, to save the state of an `EditText`, add a
callback similar to an `onClick` handler to capture text changes. Within the
callback, define what data to save:  

### Kotlin

    input.addTextChangedListener(
        afterTextChanged = { text ->
            text?.let {
                // Save state here.
            }
        }
    )

### Java

    input.addTextChangedListener(new TextWatcher() {

        ...

        @Override
        public void afterTextChanged(Editable s) {
            // Save state here.
        }
    });

Declare the callback in your `Activity` or `Fragment`. Use a `ViewModel` to
store the state.

### 3. Add list item state to the `Adapter`

Add the state of list items to your `RecyclerView.Adapter`. Pass the item state
to the adapter constructor when your host `Activity` or `Fragment` is created:  

### Kotlin

    val adapter = MyAdapter(items, viewModel.retrieveState())

### Java

    MyAdapter adapter = new MyAdapter(items, viewModel.retrieveState());

### 4. Recover list item state in the adapter's `ViewHolder`

In the `RecyclerView.Adapter`, when you bind a [`ViewHolder`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.ViewHolder) to an item,
restore the item's state:  

### Kotlin

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        ...
        val item = items[position]
        val state = states.firstOrNull { it.item == item }

        if (state != null) {
            holder.restore(state)
        }
    }

### Java

    @Override
    public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
        ...
        Item item = items[position];
        Arrays.stream(states).filter(state -> state.item == item)
            .findFirst()
            .ifPresent(state -> holder.restore(state));
    }

## Key points

- [`RecyclerView.Adapter#setStateRestorationPolicy()`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView.Adapter.StateRestorationPolicy): Specifies how a `RecyclerView.Adapter` restores its state after a configuration change.
- [`ViewModel`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel): Holds state for an activity or fragment.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover broader
Android development goals:  
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png)  
![](https://developer.android.com/static/images/picto-icons/collection.svg)  

### Optimize for large screens

Enable your app to support an optimized user experience on tablets, foldables, and ChromeOS devices.  
[Quick guide collection](https://developer.android.com/quick-guides/collections/optimize-for-large-screens)
![](https://developer.android.com/static/images/picto-icons/help.svg)  

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.  
[Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)