---
title: https://developer.android.com/kotlin/common-patterns
url: https://developer.android.com/kotlin/common-patterns
source: md.txt
---

# Use common Kotlin patterns with Android

This topic focuses on some of the most useful aspects of the Kotlin language when developing for Android.

## Work with fragments

The following sections use`Fragment`examples to highlight some of Kotlin's best features.

### Inheritance

You can declare a class in Kotlin with the`class`keyword. In the following example,`LoginFragment`is a subclass of`Fragment`. You can indicate inheritance by using the`:`operator between the subclass and its parent:  

    class LoginFragment : Fragment()

In this class declaration,`LoginFragment`is responsible for calling the constructor of its superclass,`Fragment`.

Within`LoginFragment`, you can override a number of lifecycle callbacks to respond to state changes in your`Fragment`. To override a function, use the`override`keyword, as shown in the following example:  

    override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.login_fragment, container, false)
    }

To reference a function in the parent class, use the`super`keyword, as shown in the following example:  

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
    }

### Nullability and initialization

In the previous examples, some of the parameters in the overridden methods have types suffixed with a question mark`?`. This indicates that the arguments passed for these parameters can be null. Be sure to[handle their nullability safely](https://kotlinlang.org/docs/reference/null-safety.html).

In Kotlin, you must initialize an object's properties when declaring the object. This implies that when you obtain an instance of a class, you can immediately reference any of its accessible properties. The`View`objects in a`Fragment`, however, aren't ready to be inflated until calling`Fragment#onCreateView`, so you need a way to defer property initialization for a`View`.

The`lateinit`lets you defer property initialization. When using`lateinit`, you should initialize your property as soon as possible.

The following example demonstrates using`lateinit`to assign`View`objects in`onViewCreated`:  

    class LoginFragment : Fragment() {

        private lateinit var usernameEditText: EditText
        private lateinit var passwordEditText: EditText
        private lateinit var loginButton: Button
        private lateinit var statusTextView: TextView

        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            super.onViewCreated(view, savedInstanceState)

            usernameEditText = view.findViewById(R.id.username_edit_text)
            passwordEditText = view.findViewById(R.id.password_edit_text)
            loginButton = view.findViewById(R.id.login_button)
            statusTextView = view.findViewById(R.id.status_text_view)
        }

        ...
    }

| **Note:** If you access a property before it is initialized, Kotlin throws an`UninitializedPropertyAccessException`.

### SAM conversion

You can listen for click events in Android by implementing the`OnClickListener`interface.`Button`objects contain a`setOnClickListener()`function that takes in an implementation of`OnClickListener`.

`OnClickListener`has a single abstract method,`onClick()`, that you must implement. Because`setOnClickListener()`always takes an`OnClickListener`as an argument, and because`OnClickListener`always has the same single abstract method, this implementation can be represented using an anonymous function in Kotlin. This process is known as[Single Abstract Method conversion](https://kotlinlang.org/docs/reference/java-interop.html#sam-conversions), or*SAM conversion*.

SAM conversion can make your code considerably cleaner. The following example shows how to use SAM conversion to implement an`OnClickListener`for a`Button`:  

    loginButton.setOnClickListener {
        val authSuccessful: Boolean = viewModel.authenticate(
                usernameEditText.text.toString(),
                passwordEditText.text.toString()
        )
        if (authSuccessful) {
            // Navigate to next screen
        } else {
            statusTextView.text = requireContext().getString(R.string.auth_failed)
        }
    }

The code within the anonymous function passed to`setOnClickListener()`executes when a user clicks`loginButton`.

### Companion objects

[Companion objects](https://kotlinlang.org/docs/tutorials/kotlin-for-py/objects-and-companion-objects.html#companion-objects)provide a mechanism for defining variables or functions that are linked conceptually to a type but are not tied to a particular object. Companion objects are similar to using Java's`static`keyword for variables and methods.

In the following example,`TAG`is a`String`constant. You don't need a unique instance of the`String`for each instance of`LoginFragment`, so you should define it in a companion object:  

    class LoginFragment : Fragment() {

        ...

        companion object {
            private const val TAG = "LoginFragment"
        }
    }

You could define`TAG`at the top level of the file, but the file might also have a large number of variables, functions, and classes that are also defined at the top level. Companion objects help to connect variables, functions, and the class definition without referring to any particular instance of that class.

### Property delegation

When initializing properties, you might repeat some of Android's more common patterns, such as accessing a`ViewModel`within a`Fragment`. To avoid excess duplicate code, you can use Kotlin's*property delegation*syntax.  

    private val viewModel: LoginViewModel by viewModels()

Property delegation provides a common implementation that you can reuse throughout your app. Android KTX provides some property delegates for you.`viewModels`, for example, retrieves a`ViewModel`that is scoped to the current`Fragment`.

Property delegation uses reflection, which adds some performance overhead. The tradeoff is a concise syntax that saves development time.

## Nullability

Kotlin provides strict nullability rules that maintain type-safety throughout your app. In Kotlin, references to objects cannot contain null values by default. To assign a null value to a variable, you must declare a*nullable* variable type by adding`?`to the end of the base type.

As an example, the following expression is illegal in Kotlin.`name`is of type`String`and isn't nullable:  

    val name: String = null

To allow a null value, you must use a nullable`String`type,`String?`, as shown in the following example:  

    val name: String? = null

### Interoperability

Kotlin's strict rules make your code safer and more concise. These rules lower the chances of having a`NullPointerException`that would cause your app to crash. Moreover, they reduce the number of null checks you need to make in your code.

Often, you must also call into non-Kotlin code when writing an Android app, as most Android APIs are written in the Java programming language.

Nullability is a key area where Java and Kotlin differ in behavior. Java is less strict with nullability syntax.

As an example, the`Account`class has a few properties, including a`String`property called`name`. Java does not have Kotlin's rules around nullability, instead relying on optional*nullability annotations*to explicitly declare whether you can assign a null value.

Because the Android framework is written primarily in Java, you might run into this scenario when calling into APIs without nullability annotations.

#### Platform types

If you use Kotlin to reference a unannotated`name`member that is defined in a Java`Account`class, the compiler doesn't know whether the`String`maps to a`String`or a`String?`in Kotlin. This ambiguity is represented via a*platform type* ,`String!`.

`String!`has no special meaning to the Kotlin compiler.`String!`can represent either a`String`or a`String?`, and the compiler lets you assign a value of either type. Note that you risk throwing a`NullPointerException`if you represent the type as a`String`and assign a null value.

To address this issue, you should use nullability annotations whenever you write code in Java. These annotations help both Java and Kotlin developers.

For example, here's the`Account`class as it's defined in Java:  

    public class Account implements Parcelable {
        public final String name;
        public final String type;
        private final @Nullable String accessId;

        ...
    }

One of the member variables,`accessId`, is annotated with`@Nullable`, indicating that it can hold a null value. Kotlin would then treat`accessId`as a`String?`.

To indicate that a variable can never be null, use the`@NonNull`annotation:  

    public class Account implements Parcelable {
        public final @NonNull String name;
        ...
    }

In this scenario,`name`is considered a non-nullable`String`in Kotlin.

Nullability annotations are included in all new Android APIs and many existing Android APIs. Many Java libraries have added nullability annotations to better support both Kotlin and Java developers.

#### Handling nullability

If you are unsure about a Java type, you should consider it to be nullable. As an example, the`name`member of the`Account`class is not annotated, so you should assume it to be a nullable`String?`.

If you want to trim`name`so that its value does not include leading or trailing whitespace, you can use Kotlin's`trim`function. You can safely trim a`String?`in a few different ways. One of these ways is to use the*not-null assertion operator* ,`!!`, as shown in the following example:  

    val account = Account("name", "type")
    val accountName = account.name!!.trim()

The`!!`operator treats everything on its left-hand side as non-null, so in this case, you are treating`name`as a non-null`String`. If the result of the expression to its left is null, then your app throws a`NullPointerException`. This operator is quick and easy, but it should be used sparingly, as it can reintroduce instances of`NullPointerException`into your code.

A safer choice is to use the*safe-call operator* ,`?.`, as shown in the following example:  

    val account = Account("name", "type")
    val accountName = account.name?.trim()

Using the safe-call operator, if`name`is non-null, then the result of`name?.trim()`is a name value without leading or trailing whitespace. If`name`is null, then the result of`name?.trim()`is`null`. This means that your app can never throw a`NullPointerException`when executing this statement.

While the safe-call operator saves you from a potential`NullPointerException`, it does pass a null value to the next statement. You can instead handle null cases immediately by using an*Elvis operator* (`?:`), as shown in the following example:  

    val account = Account("name", "type")
    val accountName = account.name?.trim() ?: "Default name"

If the result of the expression on the left-hand side of the Elvis operator is null, then the value on the right-hand side is assigned to`accountName`. This technique is useful for providing a default value that would otherwise be null.

You can also use the Elvis operator to return from a function early, as shown in the following example:  

    fun validateAccount(account: Account?) {
        val accountName = account?.name?.trim() ?: "Default name"

        // account cannot be null beyond this point
        account ?: return

        ...
    }

#### Android API changes

Android APIs are becoming increasingly Kotlin-friendly. Many of Android's most-common APIs, including`AppCompatActivity`and`Fragment`, contain nullability annotations, and certain calls like`Fragment#getContext`have more Kotlin-friendly alternatives.

For example, accessing the`Context`of a`Fragment`is almost always non-null, since most of the calls that you make in a`Fragment`occur while the`Fragment`is attached to an`Activity`(a subclass of`Context`). That said,`Fragment#getContext`does not always return a non-null value, as there are scenarios where a`Fragment`is not attached to an`Activity`. Thus, the return type of`Fragment#getContext`is nullable.

Since the`Context`returned from`Fragment#getContext`is nullable (and is annotated as @Nullable), you must treat it as a`Context?`in your Kotlin code. This means applying one of the previously-mentioned operators to address nullability before accessing its properties and functions. For some of these scenarios, Android contains alternative APIs that provide this convenience.`Fragment#requireContext`, for example, returns a non-null`Context`and throws an`IllegalStateException`if called when a`Context`would be null. This way, you can treat the resulting`Context`as non-null without the need for safe-call operators or workarounds.

### Property initialization

Properties in Kotlin are not initialized by default. They must be initialized when their enclosing class is initialized.

You can initialize properties in a few different ways. The following example shows how to initialize an`index`variable by assigning a value to it in the class declaration:  

    class LoginFragment : Fragment() {
        val index: Int = 12
    }

This initialization can also be defined in an initializer block:  

    class LoginFragment : Fragment() {
        val index: Int

        init {
            index = 12
        }
    }

In the examples above,`index`is initialized when a`LoginFragment`is constructed.

However, you might have some properties that can't be initialized during object construction. For example, you might want to reference a`View`from within a`Fragment`, which means that the layout must be inflated first. Inflation does not occur when a`Fragment`is constructed. Instead, it's inflated when calling`Fragment#onCreateView`.

One way to address this scenario is to declare the view as nullable and initialize it as soon as possible, as shown in the following example:  

    class LoginFragment : Fragment() {
        private var statusTextView: TextView? = null

        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
                super.onViewCreated(view, savedInstanceState)

                statusTextView = view.findViewById(R.id.status_text_view)
                statusTextView?.setText(R.string.auth_failed)
        }
    }

While this works as expected, you must now manage the nullability of the`View`whenever you reference it. A better solution is to use`lateinit`for`View`initialization, as shown in the following example:  

    class LoginFragment : Fragment() {
        private lateinit var statusTextView: TextView

        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
                super.onViewCreated(view, savedInstanceState)

                statusTextView = view.findViewById(R.id.status_text_view)
                statusTextView.setText(R.string.auth_failed)
        }
    }

The`lateinit`keyword allows you to avoid initializing a property when an object is constructed. If your property is referenced before being initialized, Kotlin throws an`UninitializedPropertyAccessException`, so be sure to initialize your property as soon as possible.
| **Note:** View binding solutions like[Data Binding](https://developer.android.com/topic/libraries/data-binding)that remove manual calls to`findViewById`can help reduce the number of null-safety issues you need to consider.