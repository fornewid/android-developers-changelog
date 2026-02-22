---
title: https://developer.android.com/topic/performance/benchmarking/microbenchmark-and-hilt
url: https://developer.android.com/topic/performance/benchmarking/microbenchmark-and-hilt
source: md.txt
---

Many apps use Hilt to inject different behaviors to different build variants.
This can be particularly useful when Microbenchmarking your app because it lets
you switch out a component that can skew the results. For example, the following
code snippet shows a repository that fetches and sorts a list of names:  

### Kotlin

```kotlin
class PeopleRepository @Inject constructor(
    @Kotlin private val dataSource: NetworkDataSource,
    @Dispatcher(DispatcherEnum.IO) private val dispatcher: CoroutineDispatcher
) {
    private val _peopleLiveData = MutableLiveData<List<Person>>()

    val peopleLiveData: LiveData<List<Person>>
        get() = _peopleLiveData

    suspend fun update() {
        withContext(dispatcher) {
            _peopleLiveData.postValue(
                dataSource.getPeople()
                    .sortedWith(compareBy({ it.lastName }, { it.firstName }))
            )
        }
    }
}}
```

### Java

```java
public class PeopleRepository {

    private final MutableLiveData<List<Person>> peopleLiveData = new MutableLiveData<>();

    private final NetworkDataSource dataSource;

    public LiveData<List<Person>> getPeopleLiveData() {
        return peopleLiveData;
    }

    @Inject
    public PeopleRepository(NetworkDataSource dataSource) {
        this.dataSource = dataSource;
    }

    private final Comparator<Person> comparator = Comparator.comparing(Person::getLastName)
            .thenComparing(Person::getFirstName);

    public void update() {
        Runnable task = new Runnable() {

            @Override
            public void run() {
                peopleLiveData.postValue(
                        dataSource.getPeople()
                                .stream()
                                .sorted(comparator)
                                .collect(Collectors.toList())
                );
            }
        };
        new Thread(task).start();
    }
}
```

If you include a network call when benchmarking, implement a fake network call
to get a more accurate result.

Including a real network call when benchmarking makes it harder to interpret
benchmark results. Network calls can be affected by many external factors, and
their duration can vary between iterations of running the benchmark. The
duration of network calls can take longer than the sorting.

## Implement a fake network call using Hilt

The call to `dataSource.getPeople()`, as shown in the preceding example,
contains a network call. However, the `NetworkDataSource` instance is injected
by Hilt, and you can replace it with the following fake implementation for
benchmarking:  

### Kotlin

```kotlin
class FakeNetworkDataSource @Inject constructor(
    private val people: List<Person>
) : NetworkDataSource {
    override fun getPeople(): List<Person> = people
}
```

### Java

```java
public class FakeNetworkDataSource implements NetworkDataSource{

    private List<Person> people;

    @Inject
    public FakeNetworkDataSource(List<Person> people) {
        this.people = people;
    }

    @Override
    public List<Person> getPeople() {
        return people;
    }
}
```

This fake network call is designed to run as quickly as possible when you call
the `getPeople()` method. For Hilt to be able to inject this, the following
provider is used:  

### Kotlin

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object FakekNetworkModule {

    @Provides
    @Kotlin
    fun provideNetworkDataSource(@ApplicationContext context: Context): NetworkDataSource {
        val data = context.assets.open("fakedata.json").use { inputStream ->
            val bytes = ByteArray(inputStream.available())
            inputStream.read(bytes)

            val gson = Gson()
            val type: Type = object : TypeToken<List<Person>>() {}.type
            gson.fromJson<List<Person>>(String(bytes), type)
        }
        return FakeNetworkDataSource(data)
    }
}
```

### Java

```java
@Module
@InstallIn(SingletonComponent.class)
public class FakeNetworkModule {

    @Provides
    @Java
    NetworkDataSource provideNetworkDataSource(
            @ApplicationContext Context context
    ) {
        List<Person> data = new ArrayList<>();
        try (InputStream inputStream = context.getAssets().open("fakedata.json")) {
            int size = inputStream.available();
            byte[] bytes = new byte[size];
            if (inputStream.read(bytes) == size) {
                Gson gson = new Gson();
                Type type = new TypeToken<ArrayList<Person>>() {
                }.getType();
                data = gson.fromJson(new String(bytes), type);

            }
        } catch (IOException e) {
            // Do something
        }
        return new FakeNetworkDataSource(data);
    }
}
```

The data is loaded from assets using a potentially variable length I/O call.
However, this is done during initialization and won't cause any irregularities
when `getPeople()` is called during benchmarking.

Some apps already use fakes on debug builds to remove any backend dependencies.
However, you need to benchmark on a build as close to the release build as
possible. The rest of this document uses a multi-module, multi-variant structure
as described in [Full project setup](https://developer.android.com/topic/performance/benchmarking/microbenchmark-write#full-setup).

There are three modules:

- `benchmarkable`: contains the code to benchmark.
- `benchmark`: contains the benchmark code.
- `app`: contains the remaining app code.

Each of the preceding modules has a build variant named `benchmark` along with
the usual `debug` and `release` variants.

## Configure the benchmark module

The code for the fake network call is in the `debug` source set of the
`benchmarkable` module, and the full network implementation is in the `release`
source set of the same module. The asset file containing the data returned by
the fake implementation is in the `debug` source set to avoid any APK bloat in
the `release` build. The `benchmark` variant needs to be based on `release` and
use the `debug` source set. The build configuration for the `benchmark` variant
of the `benchmarkable` module containing the fake implementation is as follows:  

### Kotlin

```kotlin
android {
    ...
    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
        create("benchmark") {
            initWith(getByName("release"))
        }
    }
    ...
    sourceSets {
        getByName("benchmark") {
            java.setSrcDirs(listOf("src/debug/java"))
            assets.setSrcDirs(listOf("src/debug/assets"))
        }
    }
}
```

### Groovy

```groovy
android {
    ...
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'),
                'proguard-rules.pro'
            )
        }
        benchmark {
            initWith release
        }
    }
    ...
    sourceSets {
        benchmark {
            java.setSrcDirs ['src/debug/java']
            assets.setSrcDirs(listOf ['src/debug/assets']
        }
    }
}
```

In the `benchmark` module add a custom test runner that creates an `Application`
for the tests to run in that supports Hilt as follows:  

### Kotlin

```kotlin
class HiltBenchmarkRunner : AndroidBenchmarkRunner() {

    override fun newApplication(
        cl: ClassLoader?,
        className: String?,
        context: Context?
    ): Application {
        return super.newApplication(cl, HiltTestApplication::class.java.name, context)
    }
}
```

### Java

```java
public class JavaHiltBenchmarkRunner extends AndroidBenchmarkRunner {

    @Override
    public Application newApplication(
            ClassLoader cl,
            String className,
            Context context
    ) throws InstantiationException, IllegalAccessException, ClassNotFoundException {
        return super.newApplication(cl, HiltTestApplication.class.getName(), context);
    }
}
```

This makes the `Application` object in which the tests are run extend the
[`HiltTestApplication`](https://dagger.dev/api/latest/dagger/hilt/android/testing/HiltTestApplication.html) class. Make the following changes to the build
configuration:  

### Kotlin

```kotlin
plugins {
    alias(libs.plugins.android.library)
    alias(libs.plugins.benchmark)
    alias(libs.plugins.jetbrains.kotlin.android)
    alias(libs.plugins.kapt)
    alias(libs.plugins.hilt)
}

android {
    namespace = "com.example.hiltmicrobenchmark.benchmark"
    compileSdk = 34

    defaultConfig {
        minSdk = 24

        testInstrumentationRunner = "com.example.hiltbenchmark.HiltBenchmarkRunner"
    }

    testBuildType = "benchmark"
    buildTypes {
        debug {
            // Since isDebuggable can't be modified by Gradle for library modules,
            // it must be done in a manifest. See src/androidTest/AndroidManifest.xml.
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "benchmark-proguard-rules.pro"
            )
        }
        create("benchmark") {
            initWith(getByName("debug"))
        }
    }
}

dependencies {
    androidTestImplementation(libs.bundles.hilt)
    androidTestImplementation(project(":benchmarkable"))
    implementation(libs.androidx.runner)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.junit)
    implementation(libs.androidx.benchmark)
    implementation(libs.google.dagger.hiltTesting)
    kaptAndroidTest(libs.google.dagger.hiltCompiler)
    androidTestAnnotationProcessor(libs.google.dagger.hiltCompiler)
}
```

### Groovy

```groovy
plugins {
    alias libs.plugins.android.library
    alias libs.plugins.benchmark
    alias libs.plugins.jetbrains.kotlin.android
    alias libs.plugins.kapt
    alias libs.plugins.hilt
}

android {
    namespace = 'com.example.hiltmicrobenchmark.benchmark'
    compileSdk = 34

    defaultConfig {
        minSdk = 24

        testInstrumentationRunner 'com.example.hiltbenchmark.HiltBenchmarkRunner'
    }

    testBuildType "benchmark"
    buildTypes {
        debug {
            // Since isDebuggable can't be modified by Gradle for library modules,
            // it must be done in a manifest. See src/androidTest/AndroidManifest.xml.
            minifyEnabled true
            proguardFiles(
                getDefaultProguardFile('proguard-android-optimize.txt'),
                'benchmark-proguard-rules.pro'
            )
        }
        benchmark {
            initWith debug"
        }
    }
}

dependencies {
    androidTestImplementation libs.bundles.hilt
    androidTestImplementation project(':benchmarkable')
    implementation libs.androidx.runner
    androidTestImplementation libs.androidx.junit
    androidTestImplementation libs.junit
    implementation libs.androidx.benchmark
    implementation libs.google.dagger.hiltTesting
    kaptAndroidTest libs.google.dagger.hiltCompiler
    androidTestAnnotationProcessor libs.google.dagger.hiltCompiler
}
```

The preceding example does the following:

- Applies the necessary gradle plugins to the build.
- Specifies that the custom test runner is used to run the tests.
- Specifies that the `benchmark` variant is the test type for this module.
- Adds the `benchmark` variant.
- Adds the required dependencies.

You need to change the `testBuildType` to ensure that Gradle creates the
`connectedBenchmarkAndroidTest` task, which performs the benchmarking.

## Create the microbenchmark

The benchmark is implemented as follows:  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
@HiltAndroidTest
class PeopleRepositoryBenchmark {

    @get:Rule
    val benchmarkRule = BenchmarkRule()

    @get:Rule
    val hiltRule = HiltAndroidRule(this)

    private val latch = CountdownLatch(1)

    @Inject
    lateinit var peopleRepository: PeopleRepository

    @Before
    fun setup() {
        hiltRule.inject()
    }

    @Test
    fun benchmarkSort() {
        benchmarkRule.measureRepeated {
            runBlocking {
                benchmarkRule.getStart().pauseTiming()
                withContext(Dispatchers.Main.immediate) {
                    peopleRepository.peopleLiveData.observeForever(observer)
                }
                benchmarkRule.getStart().resumeTiming()
                peopleRepository.update()
                latch.await()
                assert(peopleRepository.peopleLiveData.value?.isNotEmpty() ?: false)
           }
        }
    }

    private val observer: Observer<List<Person>> = object : Observer<List<Person>> {
        override fun onChanged(people: List<Person>?) {
            peopleRepository.peopleLiveData.removeObserver(this)
            latch.countDown()
        }
    }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
@HiltAndroidTest
public class PeopleRepositoryBenchmark {
    @Rule
    public BenchmarkRule benchmarkRule = new BenchmarkRule();

    @Rule
    public HiltAndroidRule hiltRule = new HiltAndroidRule(this);

    private CountdownLatch latch = new CountdownLatch(1);

    @Inject
    JavaPeopleRepository peopleRepository;

    @Before
    public void setup() {
        hiltRule.inject();
    }

    @Test
    public void benchmarkSort() {
        BenchmarkRuleKt.measureRepeated(benchmarkRule, (Function1<BenchmarkRule.Scope, Unit>) scope -> {
            benchmarkRule.getState().pauseTiming();
            new Handler(Looper.getMainLooper()).post(() -> {
                awaitValue(peopleRepository.getPeopleLiveData());
            });
            benchmarkRule.getState().resumeTiming();
            peopleRepository.update();
            try {
                latch.await();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            assert (!peopleRepository.getPeopleLiveData().getValue().isEmpty());
            return Unit.INSTANCE;
        });
    }

    private <T> void awaitValue(LiveData<T> liveData) {
        Observer<T> observer = new Observer<T>() {
            @Override
            public void onChanged(T t) {
                liveData.removeObserver(this);
                latch.countDown();
            }
        };
        liveData.observeForever(observer);
        return;
    }
}
```

The preceding example creates rules for both the benchmark and Hilt.
`benchmarkRule` performs the timing of the benchmark. `hiltRule` performs the
dependency injection on the benchmark test class. You must invoke the
[`inject()`](https://dagger.dev/api/latest/dagger/hilt/android/testing/HiltAndroidRule.html#inject()) method of the Hilt rule in a `@Before` function to perform the
injection before running any individual tests.

The benchmark itself pauses timing while the [`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata) observer is
registered. Then it uses a latch to wait until the `LiveData` is updated before
finishing. As the sorting is run in the time between when
`peopleRepository.update()` is called and when `LiveData` receives an update,
the duration of the sorting is included in the benchmark timing.

## Run the microbenchmark

Run the benchmark with `./gradlew :benchmark:connectedBenchmarkAndroidTest`
to perform the benchmark over many iterations and to print the timing data to
[Logcat](https://developer.android.com/studio/debug/logcat):  

    PeopleRepositoryBenchmark.log[Metric (timeNs) results: median 613408.3952380952, min 451949.30476190476, max 1412143.5142857144, standardDeviation: 273221.2328680522...

The preceding example shows the benchmark result between 0.6ms and 1.4ms to run
the sorting algorithm on a list of 1,000 items. However, if you include the
network call in the benchmark, then the variance between iterations is greater
than the time that the sort itself is taking to run, hence the need to isolate
the sorting from the network call.

You can always refactor code to make it easier to run the sorting in
isolation, but if you're already using Hilt, you can use it to inject fakes for
benchmarking instead.