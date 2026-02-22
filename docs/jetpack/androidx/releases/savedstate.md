---
title: https://developer.android.com/jetpack/androidx/releases/savedstate
url: https://developer.android.com/jetpack/androidx/releases/savedstate
source: md.txt
---

# Savedstate

# Savedstate

[User Guide](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate)[Codelab](https://codelabs.developers.google.com/codelabs/android-lifecycles/#6)  
API Reference  
[androidx.savedstate](https://developer.android.com/reference/kotlin/androidx/savedstate/package-summary)  
Write pluggable components that save the UI state when a process dies, and restore it when the process restarts.  

|  Latest Update   |                                  Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|------------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| November 5, 2025 | [1.4.0](https://developer.android.com/jetpack/androidx/releases/savedstate#1.4.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on SavedState, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Java language implementation
    implementation "androidx.savedstate:savedstate:1.4.0"

    // Kotlin
    implementation "androidx.savedstate:savedstate-ktx:1.4.0"
}
```

### Kotlin

```kotlin
dependencies {
    // Java language implementation
    implementation("androidx.savedstate:savedstate:1.4.0")

    // Kotlin
    implementation("androidx.savedstate:savedstate-ktx:1.4.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:878252+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=878252&template=1442003)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.4

### Version 1.4.0

November 05, 2025

`androidx.savedstate:savedstate-*:1.4.0`is released. Version 1.4.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a4c23caec259e53f8cfdc40b79e95c6f33136bec..56090e32a2b7028588a6dd0c73d706c6dd8dd1ee/savedstate).

### Version 1.4.0-rc01

October 22, 2025

`androidx.savedstate:savedstate-*:1.4.0-rc01`is released with no changes since 1.4.0-beta01. Version 1.4.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..84d7c340f8f124463fb6e81c405fd72106a4b81b/savedstate).

### Version 1.4.0-beta01

October 08, 2025

`androidx.savedstate:savedstate-*:1.4.0-beta01`is released with no notable changes since the last alpha. Version 1.4.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..4350deab5806bf95370a4d012d7eeaa70a10be44/savedstate).

### Version 1.4.0-alpha03

August 27, 2025

`androidx.savedstate:savedstate-*:1.4.0-alpha03`is released. Version 1.4.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/d1a3af87c572a19851d3436392c73f54a2d9e9a8..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/savedstate).

**API Changes**

- Add support for nullable types in`encodeToSavedState`and`decodeFromSavedState`. ([I79062](https://android-review.googlesource.com/#/q/I7906231207e2b25c64111123c0c9f22802c87139),[b/439527454](https://issuetracker.google.com/issues/439527454))
- Update Compose to 1.9.0. ([I2b9de](https://android-review.googlesource.com/#/q/I2b9de4c8a0f1efb5e6e7e328a52152b89d79aa90))

### Version 1.4.0-alpha02

August 13, 2025

`androidx.savedstate:savedstate-*:1.4.0-alpha02`is released. Version 1.4.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/90f45005ac103f49af0dfc59047d2aab9752b957..c359e97fece91f3767a7d017e9def23c7caf1f53/savedstate).

### Version 1.4.0-alpha01

July 30, 2025

`androidx.savedstate:savedstate-*:1.4.0-alpha01`is released. Version 1.4.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/db5028d6e08062647d9b1955154b39179732d595..90f45005ac103f49af0dfc59047d2aab9752b957/savedstate).

**API Changes**

- Add native support for nullable types in`SavedStateRegistryOwner.saved`, simplifying saving and restoring nullable properties. ([Ia632](https://android-review.googlesource.com/#/q/Ia632f9f5d19896f7d0e59eed439d75b55c1b1cb6),[b/421325690](https://issuetracker.google.com/issues/421325690))

## Version 1.3

### Version 1.3.3

September 17, 2025

`androidx.savedstate:savedstate-*:1.3.3`is released. Version 1.3.3 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f24bdb90711ef452dd28d14ea3a6537b3bbfc0c..a4c23caec259e53f8cfdc40b79e95c6f33136bec/savedstate).

**Bug Fixes**

- Fixed an error with the Compose Compiler plugin not being applied that caused`SavedState`KMP artifacts to be broken. ([Id2290](https://android-review.googlesource.com/#/q/Id2290d74b2db521eb4cd00999bda3e8b116ae48d),[b/443965665](https://issuetracker.google.com/443965665))

### Version 1.3.2

August 27, 2025

`androidx.savedstate:savedstate-*:1.3.2`is released. Version 1.3.2 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/db5028d6e08062647d9b1955154b39179732d595..1f24bdb90711ef452dd28d14ea3a6537b3bbfc0c/savedstate).

**New Features**

- Add new Kotlin Multiplatform (KMP) targets to SavedState`*-compose`artifact. Lifecycle now supports the following platforms in total: JVM (Android and Desktop), Native (Linux, iOS, watchOS, macOS, MinGW), and Web (JavaScript, WasmJS). ([/Idcf26](https://android-review.googlesource.com/#/q/Idcf2618b6b648bed4c29a04bc8e83589bd1bdd65))

### Version 1.3.1

July 16, 2025

`androidx.savedstate:savedstate-*:1.3.1`is released. Version 1.3.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/db5028d6e08062647d9b1955154b39179732d595/savedstate).

**Bug Fixes**

- Add all KMP targets supported by annotations to`SavedState`artifacts.
- Added new Kotlin Multiplatform (KMP) targets to`SavedState`artifacts.`SavedState`now supports the following platforms in total: JVM (Android and Desktop), Native (Linux, iOS, watchOS, macOS, MinGW), and Web (JavaScript, WasmJS). Note that no new KMP targets have been added to the`*-compose`artifacts, as this depends on the stable release of Compose 1.9. ([I062f4](https://android-review.googlesource.com/#/q/I062f43ad0e5ddb9140a136658f4beb3ab56543df)).

### Version 1.3.0

May 7, 2025

`androidx.savedstate:savedstate-*:1.3.0`is released. Version 1.3.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/0b329ce8820d3a97f3b21d1efabef074e12072f8..5b67d17950276ae45c2b89c55904a019de4b2041/savedstate).

**Important changes since 1.2.0**

- `LocalSavedStateRegistryOwner`has been moved from Compose UI to the new`savedstate-compose`module so that its Compose-based helper APIs can be used outside of Compose UI. This should always be used when using[Compose UI`1.9.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.9.0-alpha02)and higher, but is backward compatible such that it can be used with all versions of Compose.
- The`savedstate-ktx`kotlin extensions have now been moved to the base savedstate module.
- `SavedStateRegistryOwner`instances retrieved via`findViewTreeSavedStateRegistryOwner`can now be resolved through disjoint parents of a view, such as a`ViewOverlay`. See the release notes of core or the documentation in`ViewTree.setViewTreeDisjointParent`for more information on disjoint view parents.

**Kotlin Multiplatform**

- The`SavedState`module is now KMP compatible. Supported platforms now include Android, iOS, Linux, Mac, and JVM desktop environments.
- Introduce`SavedState`opaque type as an abstraction to provide a consistent way to save and restore application state in KMP. It includes a`SavedStateReader`and`SavedStateWriter`for modifying the state to be saved. On Android,`SavedState`is a type alias for`Bundle`, ensuring binary compatibility and facilitating the migration of existing APIs to a common source set. On other platforms,`SavedState`is a`Map<String, Any>`instance.

        // Create a new SavedState object using the savedState DSL:
        val savedState = savedState {
          putInt("currentPage", 1)
          putString("filter", "favorites")
        }

        // Read from a SavedState object
        val currentPage = savedState.read { getInt("currentPage") }

        // Edit an existing SavedState object
        savedState.write {
          remove("currentPage")
        }

**KotlinX Serialization Support**

- `SavedState`now includes KotlinX Serialization support. You can convert a class annotated with`@Serializable`to a`SavedState`using the methods`encodeToSavedState`and`decodeFromSavedState`. The returned`SavedState`is a regular`Bundle`on Android and can be used by any API that accepts a`Bundle`.

      @Serializable
      data class Person(val firstName: String, val lastName: String)

      fun main() {
          val person = Person("John", "Doe")
          val encoded: SavedState = encodeToSavedState(person)
          val decoded: Person = decodeFromSavedState(encoded)
      }

- While most types (such as primitive types) are directly supported without any configuration needed, additional serializers that can be used with`@Serializable(with = ___:class)`can be found in the[`androidx.savedstate.serialization.serializers`package](https://developer.android.com/reference/kotlin/androidx/savedstate/serialization/serializers/package-summary)in the`savedstate`module and the[`androidx.savedstate.compose.serialization.serializers`package](https://developer.android.com/reference/kotlin/androidx/savedstate/compose/serialization/serializers/package-summary)in the`savedstate-compose`module.

- We also have included`saved`, a lazy property delegate, to make it easy to store`@Serializable`classes in a`SavedStateRegistryOwner`(e.g.,`ComponentActivity`,`Fragment`, etc.) and have those classes automatically be restored across process death and recreation. Please note the`saved`delegate is lazy and will not call the`init`lambda or save anything into the`SavedStateRegistry`until it is accessed.

      @Serializable
      data class Person(val firstName: String, val lastName: String)

      class MyActivity : ComponentActivity() {
          var person by saved { Person("John", "Doe") }

          override fun onCreate(savedInstanceState: Bundle?) {
              super.onCreate(savedInstanceState)
              this.person = Person("Jane", "Doe")
          }
      }

- There is a similar`saved`property delegate for`SavedStateHandle`added in[Lifecycle`2.9.0`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.9.0).

### Version 1.3.0-rc01

April 23, 2025

`androidx.savedstate:savedstate-*:1.3.0-rc01`is released. Version 1.3.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/64e37c2d3d42028c9ab14070feedcab6b5a9e982..0b329ce8820d3a97f3b21d1efabef074e12072f8/savedstate).

### Version 1.3.0-beta01

April 9, 2025

`androidx.savedstate:savedstate-*:1.3.0-beta01`is released. Version 1.3.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..64e37c2d3d42028c9ab14070feedcab6b5a9e982/savedstate).

**Dependency Updates**

- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.3.0-alpha11

March 26, 2025

`androidx.savedstate:savedstate-*:1.3.0-alpha11`is released with no notable public changes. Version 1.3.0-alpha11 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..78132378b67c86698d1ade3dc368c9f15d738a71/savedstate).

### Version 1.3.0-alpha10

March 12, 2025

`androidx.savedstate:savedstate-*:1.3.0-alpha10`is released. Version 1.3.0-alpha10 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..7a145e052ae61e272e91ffe285e9451b8ab71870/savedstate).

**New Features**

- Add non-reified method variants for`get`collections in`SavedStateReader`. ([I0b641](https://android-review.googlesource.com/#/q/I0b641cba421761ee41bb8dc386cbc5db7cb67066),[b/399820614](https://issuetracker.google.com/issues/399820614))
- Add`encodeDefaults`to`SavedStateConfiguration`, allowing customizing whether properties with default values should be encoded. ([I893cc](https://android-review.googlesource.com/#/q/I893cc44c323c972d388476bb7593259d595517af),[b/395104517](https://issuetracker.google.com/issues/395104517))
- Add`SnapshotStateMapSerializer`to support`mutableStateMapOf`. ([Ie6f19](https://android-review.googlesource.com/#/q/Ie6f1905cb2004c75efc4e962a6a6275773259af8),[b/378895074](https://issuetracker.google.com/issues/378895074))
- Add`SnapshotStateListSerializer`to support`mutableStateListOf`. ([I4d888](https://android-review.googlesource.com/#/q/I4d888f709797a1b2f87490af0758baa4da78660d),[b/378895074](https://issuetracker.google.com/issues/378895074))
- Add`getOrNull`alternative methods for`SavedStateReader.get`variants. These methods will auto-box primitive values. ([I6228c](https://android-review.googlesource.com/#/q/I6228c173c45e6137de7d4885550285de5e50ae15),[b/399820614](https://issuetracker.google.com/issues/399820614))

**API Changes**

- Remove`getOrElse`from`SavedStateReader`in favor of`getOrNull() ?: else()`. ([I87317](https://android-review.googlesource.com/#/q/I87317b0eaa0f6d0fad334cc3f81bfcc8a90e6313),[b/399820614](https://issuetracker.google.com/issues/399820614))
- Remove`inline`modifier from`SavedStateReader`and`SavedStateWriter`methods. ([If2a02](https://android-review.googlesource.com/#/q/If2a0264a865f5d1d0a1298903c83fa02cbd6a99e),[b/399820614](https://issuetracker.google.com/issues/399820614))
- Remove built-in Android-specific List and Array serializers out of public API ([Ida293](https://android-review.googlesource.com/#/q/Ida2938fa2ad727ddfc985ff11d13b8840a383618))
- Replace`SparseParcelableArraySerializer`with`SparseArraySerializer`([I91de8](https://android-review.googlesource.com/#/q/I91de872ff549b0262418cdb9c1e4d682c69f84ee))
- Make all`SavedStateReader.get`behave consistently by throwing when value type doesn't match return type ([I78c4a](https://android-review.googlesource.com/#/q/I78c4adedf59bc93ae8851ef105b7ef362bd37a64),[b/399317598](https://issuetracker.google.com/issues/399317598))
- Rename`SavedState*Delegates`to`SavedState*Delegate`. ([I8589b](https://android-review.googlesource.com/#/q/I8589b62294646cb4529869228ea0185dac6087e6),[b/399629301](https://issuetracker.google.com/issues/399629301))
- Rename`SavedStateConfig`to`SavedStateConfiguration`. ([I043a5](https://android-review.googlesource.com/#/q/I043a5be95276ef617588559f5e3fcdb15905b793),[b/399629301](https://issuetracker.google.com/issues/399629301))

### Version 1.3.0-alpha09

February 26, 2025

`androidx.savedstate:savedstate-*:1.3.0-alpha09`is released. Version 1.3.0-alpha09 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a25ff290e492e331a1de2799475965f8c1ad8ca0..fd7408b73d9aac0f18431c22580d9ab612278b1e/savedstate).

**New Features**

- Add fallback for built-in types, ensuring that all types supported by`Bundle`can be used with`encodeAsSavedState`/`decodeFromSavedState`by default or, for properties in`@Serializable`classes, via the`@Contextual`annotation. ([Ic01d2](https://android-review.googlesource.com/#/q/Ic01d267d1f3a18e7a23ec0866076bbd2c940e5e6))
- Include support for`classDiscriminator`and`classDiscriminatorMode`on`SavedStateConfig`. ([I69b66](https://android-review.googlesource.com/#/q/I69b66678ccae14507e0a6d1b8d7d11c5b564ba9f),[b/395104517](https://issuetracker.google.com/issues/395104517))

**API Changes**

- Add`SavedStateConfig`parameter to`saved()`delegates ([I39b3a](https://android-review.googlesource.com/#/q/I39b3a73d139c1d4c2a5fd01151679252dab67ad0))
- Makes built-in serializers singleton objects ([Ifeee4](https://android-review.googlesource.com/#/q/Ifeee4e8598b390ec32c9ed32c34e3664314ffb73))
- `SavedStateConfig`properties are now public, enabling other modules to use these configurations. ([Ie5f49](https://android-review.googlesource.com/#/q/Ie5f4997bc61932de390da3699339e01b2e91b514),[b/378897438](https://issuetracker.google.com/issues/378897438))
- Support`@Serializer(with = ...)`for`MutableStateFlowSerializer`and`MutableStateSerializer`([I90953](https://android-review.googlesource.com/#/q/I909533ef1e3eb472677519d3a5590fc20ad1b839))
- Add`contentDeepToString`to`SavedStateReader`([I14d10](https://android-review.googlesource.com/#/q/I14d10bb8f695b786e48c0761f4ff5f1b308635a9))

### Version 1.3.0-alpha08

February 12, 2025

`androidx.savedstate:savedstate-*:1.3.0-alpha08`is released. Version 1.3.0-alpha08 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3671eefdf920941dd90f135e8dd0caf9fd4cb14c..a25ff290e492e331a1de2799475965f8c1ad8ca0/savedstate).

**New Features**

- Move`MutableStateSerializer`to`savedstate-compose`from`lifecycle-viewmodel-compose`, allowing you to use the SavedState Serialization APIs with Compose's`MutableState`. ([I4f690](https://android-review.googlesource.com/#/q/I4f690e41dc5619d185784409170943abeb0f0550),[b/378895074](https://issuetracker.google.com/issues/378895074))

**API Changes**

- Add a factory function to create`SavedState`from an existing`SavedState`. ([I39f9a](https://android-review.googlesource.com/#/q/I39f9acb8a02946e150ccfe0a394e4f5dbf8f8ac6))
- Adds support for`Array<SavedState>`and`List<SavedState>`in`androidx.savedstate`. ([Idd8a5](https://android-review.googlesource.com/#/q/Idd8a5075c7151fd97153a00c413a4015325a3be3))
- Add`SavedStateConfig`optional parameter to SavedState encoding/decoding ([I6c4c0](https://android-review.googlesource.com/#/q/I6c4c06f6090e0ebb6233e590a263a150d83aed6d))

### Version 1.3.0-alpha07

January 29, 2025

`androidx.savedstate:savedstate-*:1.3.0-alpha07`is released. Version 1.3.0-alpha07 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9b7c30efa4b23edcbca29da0d87ef33be7f0e6e2..3671eefdf920941dd90f135e8dd0caf9fd4cb14c/savedstate).

**New Features**

- Add`MutableStateFlowSerializer`for serializing`kotlinx.coroutines.flow.MutableStateFlow`. ([I6a892](https://android-review.googlesource.com/#/q/I6a8925772d2f124d2db4a83bff0062c1db0eb0fb),[b/378895070](https://issuetracker.google.com/issues/378895070))

**API Changes**

- Replace overloaded`SavedStateRegistryOwner.saved()`delegate functions with default parameters ([Icd1c1](https://android-review.googlesource.com/#/q/Icd1c1e64c3df58fc7505bef99494ef168a0268bb))
- Make`JavaSerializableSerializer`and`ParcelableSerializer`abstract ([I268f6](https://android-review.googlesource.com/#/q/I268f62533803b846f158b51a65da091285f90dd3))
- Remove generic`T : CharSequence`from`CharSequenceSerializer`([Ib40bd](https://android-review.googlesource.com/#/q/Ib40bd2dcf522ceb14f03efacffc18ce6ad188844))

### Version 1.3.0-alpha06

December 11, 2024

`androidx.savedstate:savedstate-*:1.3.0-alpha06`is released. Version 1.3.0-alpha06 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9f3e1b6fc190040f287dcfe745fbc438cbed93f9..9b7c30efa4b23edcbca29da0d87ef33be7f0e6e2/savedstate).

**New Features**

- `SavedState`KMP now supports:`IBinder`,`Size`,`SizeF`,`Array<Parcelable>`,`SparseArray<Parcelable>`and Serializable (Android). ([I1ba94](https://android-review.googlesource.com/#/q/I1ba9446ed4dad6e018cbf17feaef1f5fcdeb6c3f),[b/334076622](https://issuetracker.google.com/issues/334076622))
- Add`KSerializer`instances that can be used to encode/decode Java and Android types supported by Bundle by marking the relevant field in your class with`@Serializable(with = ParcelableSerializer::class)`. ([I8c10f](https://android-review.googlesource.com/#/q/I8c10fdae09e9e10f7699838439d3f3145af32b36),[I28caf](https://android-review.googlesource.com/#/q/I28caf279b53cb69311c861e415390da7efd90c40),[b/376026712](https://issuetracker.google.com/issues/376026712))
- `SavedStateRegistryOwner`instances retrieved via`findViewTreeSavedStateRegistryOwner`can now be resolved through disjoint parents of a view, such as a`ViewOverlay`. See the release notes of core or the documentation in`ViewTree.setViewTreeDisjointParent`for more information on disjoint view parents. ([Iccb33](https://android-review.googlesource.com/#/q/Iccb332b0306c15259ce223ee70255b04af36c427))

**API Changes**

- Make the namings and package organization more consistent with`SavedStateRegistryOwnerDelegate`([I8c135](https://android-review.googlesource.com/#/q/I8c1353eedd7299f885ce45b7d85deb4a24c557e4),[b/376026744](https://issuetracker.google.com/issues/376026744))

### Version 1.3.0-alpha05

November 13, 2024

`androidx.savedstate:savedstate-*:1.3.0-alpha05`is released. Version 1.3.0-alpha05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..0aac1878823c58d5a7b1eee060cc79d1b38b4996/savedstate).

**KotlinX Serialization Support**

- `SavedState`now includes KotlinX Serialization support. You can convert a class annotated with`@Serializable`to a`SavedState`using the methods`encodeToSavedState`and`decodeFromSavedState`. The returned`SavedState`is a regular`Bundle`on Android and can be used by any API that accepts a`Bundle`. ([I6f59f](https://android-review.googlesource.com/#/q/I6f59faffaa3777bf56132a67f41b867d7a9663e5),[b/374102924](https://issuetracker.google.com/issues/374102924))

      @Serializable
      data class Person(val firstName: String, val lastName: String)

      fun main() {
          val person = Person("John", "Doe")
          val encoded: SavedState = encodeToSavedState(person)
          val decoded: Person = decodeFromSavedState(encoded)
      }

- We also have included`saved`, a lazy property delegate, to make it easy to store`@Serializable`classes in a`SavedStateRegistryOwner`(e.g.,`ComponentActivity`,`Fragment`, etc.) and have those classes automatically be restored across process death and recreation. Please note the`saved`delegate is lazy and will not call the`init`lambda or save anything into the`SavedStateRegistry`until it is accessed. ([I66739](https://android-review.googlesource.com/#/q/I667391f94de531e5535435b3b05bdef8bde5f61f),[b/376027806](https://issuetracker.google.com/issues/376027806))

      @Serializable
      data class Person(val firstName: String, val lastName: String)

      class MyActivity : ComponentActivity() {
          var person by saved { Person("John", "Doe") }

          override fun onCreate(savedInstanceState: Bundle?) {
              super.onCreate(savedInstanceState)
              this.person = Person("Jane", "Doe")
          }
      }

- There is a similar`saved`property delegate for`SavedStateHandle`added in[Lifecycle`2.9.0-alpha07`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.9.0-alpha07).

**API Changes**

- Add`toMap`to`SavedState`, allowing any`SavedState`to be converted to a regular`Map`(shallow copy). ([I487b9](https://android-review.googlesource.com/#/q/I487b901051ad68a3e27f9a5550fd7336734abbb1),[b/334076622](https://issuetracker.google.com/issues/334076622))
- `SavedState`KMP now supports arrays. ([Ic0552](https://android-review.googlesource.com/#/q/Ic0552cac5744d8422524d8219438a6571f70c476),[b/334076622](https://issuetracker.google.com/issues/334076622))

### Version 1.3.0-alpha04

October 30, 2024

`androidx.savedstate:savedstate-*:1.3.0-alpha04`is released. Version 1.3.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/savedstate).

**API Changes**

- SavedState KMP now supports Char. ([I9ac2f](https://android-review.googlesource.com/#/q/I9ac2ff6589371bd4bc79b1910334ce24710cd176),[b/334076622](https://issuetracker.google.com/issues/334076622))
- Add`putNull`and`isNull`to SavedState KMP. ([Iea71d](https://android-review.googlesource.com/#/q/Iea71d9d8652c9cbd45e701d5b4785579acd73969),[b/334076622](https://issuetracker.google.com/issues/334076622))
- Add additional`savedState`factory parameters supporting an initial`Map<String, Any>`([I9b37d](https://android-review.googlesource.com/#/q/I9b37da20978bc549e1ab5c354985aa4ca450f6be),[b/334076622](https://issuetracker.google.com/issues/334076622))
- SavedState KMP now supports`contentDeepEquals`comparison. ([Ia515c](https://android-review.googlesource.com/#/q/Ia515c97b16e17bcb8a20dafbc043cf2d971c4405),[b/334076622](https://issuetracker.google.com/issues/334076622))
- SavedState KMP now supports Long. ([I4c180](https://android-review.googlesource.com/#/q/I4c180e12c8259436628e5b6b62a0dfa38f003be6),[b/334076622](https://issuetracker.google.com/issues/334076622))

### Version 1.3.0-alpha03

October 16, 2024

`androidx.savedstate:savedstate-*:1.3.0-alpha03`is released with no notable changes. Version 1.3.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/savedstate).

### Version 1.3.0-alpha02

October 2, 2024

`androidx.savedstate:savedstate-*:1.3.0-alpha02`is released. Version 1.3.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/savedstate).

**Kotlin Multiplatform**

- The`SavedState`module is now KMP compatible. Supported platforms now include Android, iOS, Linux, Mac, and JVM desktop environments. ([I26305](https://android-review.googlesource.com/#/q/I26305abd31dcbbf1c686e0bcfa9871b23cdd8545),[b/334076622](https://issuetracker.google.com/issues/334076622))

**New Features**

- Introduce`SavedState`opaque type as an abstraction to provide a consistent way to save and restore application state in KMP. It includes a`SavedStateReader`and`SavedStateWriter`for modifying the state to be saved. On Android,`SavedState`is a type alias for`Bundle`, ensuring binary compatibility and facilitating the migration of existing APIs to a common source set. On other platforms,`SavedState`is a`Map<String, Any>`instance. ([I18575](https://android-review.googlesource.com/#/q/I185754bb2e7e04c32ccc89209a4d4e765334e547),[b/334076622](https://issuetracker.google.com/issues/334076622))

      // Create a new SavedState object using the savedState DSL:
      val savedState = savedState {
        putInt("currentPage", 1)
        putString("filter", "favorites")
      }

      // Read from a SavedState object
      val currentPage = savedState.read { getInt("currentPage") }

      // Edit an existing SavedState object
      savedState.write {
        remove("currentPage")
      }

**API Changes**

- `SavedStateRegistry`and`SavedStateRegistryController`are now KMP compatible. ([Id7bb8](https://android-review.googlesource.com/#/q/Id7bb8064cc8bf19faade95636dd1436943056ce6),[b/334076622](https://issuetracker.google.com/issues/334076622))
- `SavedState`,`SavedStateWriter`and`SavedStateReader`are now KMP compatible. ([I26305](https://android-review.googlesource.com/#/q/I26305abd31dcbbf1c686e0bcfa9871b23cdd8545),[b/334076622](https://issuetracker.google.com/issues/334076622))

### Version 1.3.0-alpha01

August 7, 2024

`androidx.savedstate:savedstate:1.3.0-alpha01`and`androidx.savedstate:savedstate-ktx:1.3.0-alpha01`are released. Version 1.3.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9adc92b66f549bb8c730a8710cc44189673e8dfc..9130b719318a69f2f3eaf82c32b131232fd721cb/savedstate).

**API Changes**

- The`savedstate-ktx`kotlin extensions have now been moved to the base savedstate module. ([I1cc18](https://android-review.googlesource.com/#/q/I1cc18c7e02f8aa1744d59552e20c41381e469df6),[b/274803094](https://issuetracker.google.com/issues/274803094))

**Note**

- Update`compileSdk`to 35 ([5dc41be](https://android.googlesource.com/platform/frameworks/support/+/5dc41be792a8fa6b2488df3e780da1c0805b202f))

## Version 1.2.1

### Version 1.2.1

March 22, 2023

`androidx.savedstate:savedstate:1.2.1`and`androidx.savedstate:savedstate-ktx:1.2.1`are released.[Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3329ffac761570981343cb9fb84e087782d3403e..800c80137427602e8e003b8aad0e3051436bdd17/savedstate)

**Dependency Updates**

- `SavedState`now depends on[Lifecycle`2.6.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.1). ([c1f621](https://android.googlesource.com/platform/frameworks/support/+/c1f62187db7f83e7db1bc1c1fb0b122d7ed34ee8))

## Version 1.2.0

### Version 1.2.0

June 29, 2022

`androidx.savedstate:savedstate:1.2.0`and`androidx.savedstate:savedstate-ktx:1.2.0`are released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/441d1e30254495bca43af4b5d3b13906babd74c7..3329ffac761570981343cb9fb84e087782d3403e/savedstate)

**Important changes since 1.1.0**

- `SavedStateRegistryController`now allows early attachment of the`SavedStateRegistry`via`performAttach()`.
- You can now retrieve a previously registered`SavedStateProvider`from a`SavedStateRegistry`via`getSavedStateProvider()`.
- The`SavedState`library has been rewritten in Kotlin.
  - For`SavedStateRegistryOwner`, this is a**source incompatible change** for those classes written in Kotlin - you must now override the`savedStateRegistry`property rather than implement the previous`getSavedStateRegistry()`function.
  - For`ViewTreeSavedStateRegistryOwner`, this is a**source incompatible change** for those classes written in Kotlin - you must now directly import and use the Kotlin extension methods on`View`of`androidx.savedstate.setViewTreeSavedStateRegistryOwner`and`androidx.savedstate.findViewTreeSavedStateRegistryOwner`to set and find a previously set owner. This replaces the`savedstate-ktx`API of`findViewTreeSavedStateRegistryOwner`.

**Behavior Changes**

- `SavedStateRegistry`no longer saves an empty Bundle if there is no state to save.

### Version 1.2.0-rc01

May 11, 2022

`androidx.savedstate:savedstate:1.2.0-rc01`and`androidx.savedstate:savedstate-ktx:1.2.0-rc01`are released.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..441d1e30254495bca43af4b5d3b13906babd74c7/savedstate)

**Documentation Changes**

- The`SavedStateRegistryOwner`Kdocs have been updated to clarify the responsibilities and contract that the owner has on how it should implement the interface or when they should call the methods on`SavedStateRegistryController`. ([Iefc95](https://android-review.googlesource.com/#/q/Iefc9519241d9d6844868e6833b33081aa6908b7f),[b/228887344](https://issuetracker.google.com/228887344))

### Version 1.2.0-beta01

April 20, 2022

`androidx.savedstate:savedstate:1.2.0-beta01`and`androidx.savedstate:savedstate-ktx:1.2.0-beta01`are released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/savedstate)

**API Changes**

- The`SavedStateRegistry`and`ViewTreeSavedStateRegistryOwner`classes have been rewritten in Kotlin. For`ViewTreeSavedStateRegistryOwner`, this is a**source incompatible change** for those classes written in Kotlin - you must now directly import and use the Kotlin extension methods on`View`of`androidx.savedstate.setViewTreeSavedStateRegistryOwner`and`androidx.savedstate.findViewTreeSavedStateRegistryOwner`to set and find a previously set owner. This replaces the`savedstate-ktx`API of`findViewTreeSavedStateRegistryOwner`. This is binary compatible and remains source compatible for implementations written in the Java programming language. ([b/220191285](https://issuetracker.google.com/issues/220191285))

### Version 1.2.0-alpha02

April 6, 2022

`androidx.savedstate:savedstate:1.2.0-alpha02`and`androidx.savedstate:savedstate-ktx:1.2.0-alpha02`are released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/savedstate)

**New Features**

- You can now retrieve a previously registered`SavedStateProvider`from a`SavedStateRegistry`via`getSavedStateProvider()`. ([I7ea47](https://android-review.googlesource.com/#/q/I7ea470c1af0385b8bc9d8ca653c84cc8d224e6cf),[b/215406268](https://issuetracker.google.com/215406268))

**API Changes**

- The`SavedStateRegistryOwner`,`SavedStateRegistryController`, and`Recreator`classes have been rewritten in Kotlin. For`SavedStateRegistryOwner`, this is a**source incompatible change** for those classes written in Kotlin - you must now override the`savedStateRegistry`property rather than implement the previous`getSavedStateRegistry()`function. This is binary compatible and source compatible for implementations written in the Java programming language. ([b/220191285](https://issuetracker.google.com/issues/220191285))

### Version 1.2.0-alpha01

January 26, 2022

`androidx.savedstate:savedstate:1.2.0-alpha01`and`androidx.savedstate:savedstate-ktx:1.2.0-alpha01`are released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2591e18c04b1293252380dce8256c33faea59b9d..9dceceb54300ed028a7e8fc7a3454f270337ffde/savedstate)

**New Features**

- `SavedStateRegistryController`now allows early attachment of the`SavedStateRegistry`via`performAttach()`. ([Ice4bf](https://android-review.googlesource.com/#/q/Ice4bf56901f54a425c61e7a224df7507ec776645))

**Behavior Changes**

- `SavedStateRegistry`no longer saves an empty Bundle if there is no state to save. ([aosp/1896865](https://android-review.googlesource.com/c/platform/frameworks/support/+/1896865),[b/203457956](https://issuetracker.google.com/203457956))

## Version 1.1.0

### Version 1.1.0

February 10, 2021

`androidx.savedstate:savedstate:1.1.0`and`androidx.savedstate:savedstate-ktx:1.1.0`are released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e55e4062ce898295bd26770eee5d355eb7f0f738..2591e18c04b1293252380dce8256c33faea59b9d/savedstate)

**Major changes since 1.0.0**

- **`ViewTreeSavedStateRegistryOwner`API** : A new`ViewTreeSavedStateRegistryOwner.get(View)`API allows you to retrieve the containing`SavedStateRegistry`given a`View`instance. You must upgrade to[Activity`1.2.0`](https://developer.android.com/jetpack/androidx/releases/jetpack/androidx/releases/activity#1.2.0),[Fragment`1.3.0`](https://developer.android.com/jetpack/androidx/releases/jetpack/androidx/releases/fragment#1.3.0), and[AppCompat`1.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/jetpack/androidx/releases/appcompat#1.3.0-alpha01)or higher to populate this correctly.
- **`savedstate-ktx`artifact** : The new`savedstate-ktx`artifact has been added with a`findViewTreeSavedStateRegistryOwner()`Kotlin extension for working with`ViewTreeSavedStateRegistryOwner`.

### Version 1.1.0-rc01

December 16, 2020

`androidx.savedstate:savedstate:1.1.0-rc01`and`androidx.savedstate:savedstate-ktx:1.1.0-rc01`are released with no changes since`1.1.0-beta01`.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..e55e4062ce898295bd26770eee5d355eb7f0f738/savedstate)

### Version 1.1.0-beta01

October 1, 2020

`androidx.savedstate:savedstate:1.1.0-beta01`and`androidx.savedstate:savedstate-ktx:1.1.0-beta01`are released with no changes since`1.1.0-alpha01`.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/savedstate)

### Version 1.1.0-alpha01

May 20, 2020

`androidx.savedstate:savedstate:1.1.0-alpha01`and`androidx.savedstate:savedstate-ktx:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb/savedstate)

**New Features**

- A new`ViewTreeSavedStateRegistryOwner.get(View)`API allows you to retrieve the containing`SavedStateRegistry`given a`View`instance. You must upgrade to[Activity`1.2.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha05),[Fragment`1.3.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha05), and[AppCompat`1.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.3.0-alpha01)to populate this correctly. ([aosp/1298679](https://android-review.googlesource.com/1298679))
- The new`savedstate-ktx`artifact has been added with a`findViewTreeSavedStateRegistryOwner()`Kotlin extension for working with`ViewTreeSavedStateRegistryOwner`. ([aosp/1299434](https://android-review.googlesource.com/1299434))

## Version 1.0.0

### Version 1.0.0

September 5, 2019

`androidx.savedstate:savedstate:1.0.0`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/31e072b23ddd65615efc5f3fbece2276b6b5cae4..e498cc0e42f55ccda2c1af1aa9475fe18814ee4a/savedstate).

**Major features of SavedState 1.0.0**

`androidx.savedstate`graduated to a stable release. This is a set of APIs that allow developers to plugin components into the restore / saveInstanceState process. The main entry point of the API is`SavedStateRegistry`, which provides a way to retrieve previously saved states using`consumeRestoredStateForKey`and register a callback to`registerSavedStateProvider`to provide a saved state once system requests it.

### Version 1.0.0-rc01

July 2, 2019

`androidx.savedstate:savedstate:1.0.0-rc01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311..31e072b23ddd65615efc5f3fbece2276b6b5cae4/savedstate).

**Bug fixes**

- Fixed incorrect proguard rule ([b/132655499](https://issuetracker.google.com/issues/132655499))

### Version 1.0.0-beta01

May 7, 2019

`androidx.savedstate:savedstate:1.0.0-beta01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/b22fd6c3be270f4c9fd632c55593568ff21637e0..fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311/savedstate).

### Version 1.0.0-alpha02

March 13, 2019

`androidx.savedstate:savedstate:1.0.0-alpha02`is released.`androidx.savedstate:savedstate`combines artifacts`androidx.savedstate:savedstate-bundle`and`androidx.savedstate:savedstate-common`into one artifact, because it was decided to simplify savedstate infrastructure and remove generics from`SavedStateRegistry`. Thus, there is no need for separate modules.

The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/86267e31251cdaf875674004b9937ff3da0c3f24..b22fd6c3be270f4c9fd632c55593568ff21637e0/savedstate).

**New features**

- `SavedStateRegistry.runOnNextRecreaction(Class<? extends AutoRecreated> clazz )`was added. The given class will be instantiated and the method`AutoRecreated.onRecreated`will be run when the owning component restarted.

**API changes**

- Generics removed from`SavedStateRegistry<T>`
- AbstractSavedStateRegistry \& BundlableSavedStateRegistry are removed, use simple`SavedStateRegistry`instead
- `BundleSavedStateRegistryOwner`is renamed to`SavedStateRegistryOwner`

### Version 1.0.0-alpha01

December 17, 2018

This is the first release of`SavedState`.

**New features**

`androidx.savedstate`is a new set of alpha APIs that allow developers to plugin components to the restore / saveInstanceState process. The main entry point of the API is`SavedStateRegistry<T>`, which provides a way to retrieve previously savedstate via`consumeRestoredStateForKey`and register a callback to`registerSavedStateProvider`to provide a savedstate once system requests it.