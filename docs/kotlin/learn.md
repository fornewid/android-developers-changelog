---
title: https://developer.android.com/kotlin/learn
url: https://developer.android.com/kotlin/learn
source: md.txt
---

# Learn the Kotlin programming language

[Kotlin](https://kotlinlang.org/)is a programming language widely used by Android developers everywhere. This topic serves as a Kotlin crash-course to get you up and running quickly.

## Variable declaration

Kotlin uses two different keywords to declare variables:`val`and`var`.

- Use`val`for a variable whose value never changes. You can't reassign a value to a variable that was declared using`val`.
- Use`var`for a variable whose value can change.

In the example below,`count`is a variable of type`Int`that is assigned an initial value of`10`:  

    var count: Int = 10

`Int`is a type that represents an integer, one of the many numerical types that can be represented in Kotlin. Similar to other languages, you can also use`Byte`,`Short`,`Long`,`Float`, and`Double`depending on your numerical data.

The`var`keyword means that you can reassign values to`count`as needed. For example, you can change the value of`count`from`10`to`15`:  

    var count: Int = 10
    count = 15

Some values are not meant to be changed, though. Consider a`String`called`languageName`. If you want to ensure that`languageName`always holds a value of "Kotlin", then you can declare`languageName`using the`val`keyword:  

    val languageName: String = "Kotlin"

These keywords allow you to be explicit about what can be changed. Use them to your advantage as needed. If a variable reference must be reassignable, then declare it as a`var`. Otherwise, use`val`.

### Type inference

Continuing the previous example, when you assign an initial value to`languageName`, the Kotlin compiler can infer the type based off of the type of the assigned value.

Since the value of`"Kotlin"`is of type`String`, the compiler infers that`languageName`is also a`String`. Note that Kotlin is a*statically-typed*language. This means that the type is resolved at compile time and never changes.

In the following example,`languageName`is inferred as a`String`, so you can't call any functions that aren't part of the`String`class:  

    val languageName = "Kotlin"
    val upperCaseName = languageName.toUpperCase()

    // Fails to compile
    languageName.inc()

`toUpperCase()`is a function that can only be called on variables of type`String`. Because the Kotlin compiler has inferred`languageName`as a`String`, you can safely call`toUpperCase()`.`inc()`, however, is an`Int`operator function, so it can't be called on a`String`. Kotlin's approach to type inference gives you both conciseness and type-safety.

### Null safety

In some languages, a reference type variable can be declared without providing an initial explicit value. In these cases, the variables usually contain a null value. Kotlin variables can't hold null values by default. This means that the following snippet is invalid:  

    // Fails to compile
    val languageName: String = null

For a variable to hold a null value, it must be of a*nullable* type. You can specify a variable as being nullable by suffixing its type with`?`, as shown in the following example:  

    val languageName: String? = null

With a`String?`type, you can assign either a`String`value or`null`to`languageName`.

You must handle nullable variables carefully or risk a dreaded`NullPointerException`. In Java, for example, if you attempt to invoke a method on a null value, your program crashes.

Kotlin provides a number of mechanisms for safely working with nullable variables. For more information, see[Common Kotlin patterns in Android: Nullability](https://developer.android.com/kotlin/common-patterns#nullability).

## Conditionals

Kotlin features several mechanisms for implementing conditional logic. The most common of these is an*if-else statement* . If an expression wrapped in parentheses next to an`if`keyword evaluates to`true`, then code within that branch (i.e. the immediately-following code that is wrapped in curly braces) is executed. Otherwise, the code within the`else`branch is executed.  

    if (count == 42) {
        println("I have the answer.")
    } else {
        println("The answer eludes me.")
    }

You can represent multiple conditions using`else if`. This lets you represent more granular, complex logic within a single conditional statement, as shown in the following example:  

    if (count == 42) {
        println("I have the answer.")
    } else if (count > 35) {
        println("The answer is close.")
    } else {
        println("The answer eludes me.")
    }

Conditional statements are useful for representing stateful logic, but you may find that you repeat yourself when writing them. In the example above, you simply print a`String`in each branch. To avoid this repetition, Kotlin offers*conditional expressions*. The last example can be rewritten as follows:  

    val answerString: String = if (count == 42) {
        "I have the answer."
    } else if (count > 35) {
        "The answer is close."
    } else {
        "The answer eludes me."
    }

    println(answerString)

Implicitly, each conditional branch returns the result of the expression on its final line, so you don't need to use a`return`keyword. Because the result of all three branches is of type`String`, the result of the if-else expression is also of type`String`. In this example,`answerString`is assigned an initial value from the result of the if-else expression. Type inference can be used to omit the explicit type declaration for`answerString`, but it's often a good idea to include it for clarity.
| **Note:** Kotlin does not include a traditional[ternary operator](https://en.wikipedia.org/wiki/%3F:), instead favoring the use of conditional expressions.

As the complexity of your conditional statement grows, you might consider replacing your if-else expression with a*when*expression, as shown in the following example:  

    val answerString = when {
        count == 42 -> "I have the answer."
        count > 35 -> "The answer is close."
        else -> "The answer eludes me."
    }

    println(answerString)

Each branch in a`when`expression is represented by a condition, an arrow (`->`), and a result. If the condition on the left-hand side of the arrow evaluates to true, then the result of the expression on the right-hand side is returned. Note that execution does not fall through from one branch to the next. The code in the`when`expression example is functionally-equivalent to that in the previous example but is arguably easier to read.

Kotlin's conditionals highlight one of its more powerful features,*smart casting*. Rather than using the safe-call operator or the not-null assertion operator to work with nullable values, you can instead check if a variable contains a reference to a null value using a conditional statement, as shown in the following example:  

    val languageName: String? = null
    if (languageName != null) {
        // No need to write languageName?.toUpperCase()
        println(languageName.toUpperCase())
    }

Within the conditional branch,`languageName`may be treated as non-nullable. Kotlin is smart enough to recognize that the condition for executing the branch is that`languageName`does not hold a null value, so you do not have to treat`languageName`as nullable within that branch. This smart casting works for null checks,[type checks](https://kotlinlang.org/docs/reference/typecasts.html#is-and-is-operators), or any condition that satisfies a[contract](https://kotlinlang.org/docs/reference/whatsnew13.html#contracts).

## Functions

You can group one or more expressions into a*function*. Rather than repeating the same series of expressions each time that you need a result, you can wrap the expressions in a function and call that function instead.

To declare a function, use the`fun`keyword followed by the function name. Next, define the types of inputs that your function takes, if any, and declare the type of output that it returns. A function's body is where you define expressions that are called when your function is invoked.

Building on previous examples, here's a complete Kotlin function:  

    fun generateAnswerString(): String {
        val answerString = if (count == 42) {
            "I have the answer."
        } else {
            "The answer eludes me"
        }

        return answerString
    }

The function in the example above has the name`generateAnswerString`. It doesn't take any input. It outputs a result of type`String`. To call a function, use its name, followed by the invocation operator (`()`). In the example below, the`answerString`variable is initialized with the result from`generateAnswerString()`.  

    val answerString = generateAnswerString()

Functions can take arguments as input, as shown in the following example:  

    fun generateAnswerString(countThreshold: Int): String {
        val answerString = if (count > countThreshold) {
            "I have the answer."
        } else {
            "The answer eludes me."
        }

        return answerString
    }

When declaring a function, you can specify any number of arguments and their types. In the example above,`generateAnswerString()`takes one argument named`countThreshold`of type`Int`. Within the function, you can refer to the argument by using its name.

When calling this function, you must include an argument within the function call's parentheses:  

    val answerString = generateAnswerString(42)

### Simplifying function declarations

`generateAnswerString()`is a fairly simple function. The function declares a variable and then immediately returns. When the result of a single expression is returned from a function, you can skip declaring a local variable by directly returning the result of the if-else expression contained in the function, as shown in the following example:  

    fun generateAnswerString(countThreshold: Int): String {
        return if (count > countThreshold) {
            "I have the answer."
        } else {
            "The answer eludes me."
        }
    }

You can also replace the return keyword with the assignment operator:  

    fun generateAnswerString(countThreshold: Int): String = if (count > countThreshold) {
            "I have the answer"
        } else {
            "The answer eludes me"
        }

### Anonymous functions

Not every function needs a name. Some functions are more directly identified by their inputs and outputs. These functions are called*anonymous functions*. You can keep a reference to an anonymous function, using this reference to call the anonymous function later. You can also pass the reference around your application, as with other reference types.  

    val stringLengthFunc: (String) -> Int = { input ->
        input.length
    }

Like named functions, anonymous functions can contain any number of expressions. The returned value of the function is the result of the final expression.

In the example above,`stringLengthFunc`contains a reference to an anonymous function that takes a`String`as input and returns the length of the input`String`as output of type`Int`. For that reason, the function's type is denoted as`(String) -> Int`. This code does not invoke the function, however. To retrieve the result of the function, you must invoke it with like you would a named function. You must supply a`String`when calling`stringLengthFunc`, as shown in the following example:  

    val stringLengthFunc: (String) -> Int = { input ->
        input.length
    }

    val stringLength: Int = stringLengthFunc("Android")

### Higher-order functions

A function can take another function as an argument. Functions that use other functions as arguments are called*higher-order functions*. This pattern is useful for communicating between components in the same way that you might use a callback interface in Java.

Here's an example of a higher-order function:  

    fun stringMapper(str: String, mapper: (String) -> Int): Int {
        // Invoke function
        return mapper(str)
    }

The`stringMapper()`function takes a`String`along with a function that derives an`Int`value from a`String`that you pass into it.

You can call`stringMapper()`by passing a`String`and a function that satisfies the other input parameter, namely a function that takes a`String`as input and outputs an`Int`, as shown in the following example:  

    stringMapper("Android", { input ->
        input.length
    })

If the anonymous function is the*last*parameter defined on a function, you can pass it outside of the parentheses used to invoke the function, as shown in the following example:  

    stringMapper("Android") { input ->
        input.length
    }

Anonymous functions can be found throughout the Kotlin standard library. For more information, see[Higher-Order Functions and Lambdas](https://kotlinlang.org/docs/reference/lambdas.html).

## Classes

All of the types mentioned so far are built into the Kotlin programming language. If you would like to add your own custom type, you can define a class using the`class`keyword, as shown in the following example:  

    class Car

### Properties

Classes represent state using properties. A[property](https://kotlinlang.org/docs/reference/properties.html)is a class-level variable that can include a getter, a setter, and a backing field. Since a car needs wheels to drive, you can add a list of`Wheel`objects as a property of`Car`, as shown in the following example:  

    class Car {
        val wheels = listOf<Wheel>()
    }

Note that`wheels`is a`public val`, meaning that`wheels`can be accessed from outside of the`Car`class, and it can't be reassigned. If you want to obtain an instance of`Car`, you must first call its constructor. From there, you can access any of its accessible properties.  

    val car = Car() // construct a Car
    val wheels = car.wheels // retrieve the wheels value from the Car

If you want to customize your wheels, you can define a custom constructor that specifies how your class properties are initialized:  

    class Car(val wheels: List<Wheel>)

In the example above, the class constructor takes a`List<Wheel>`as a constructor argument and uses that argument to initialize its`wheels`property.

### Class functions and encapsulation

Classes use functions to model behavior. Functions can modify state, helping you to expose only the data that you wish to expose. This access control is part of a larger object-oriented concept known as*encapsulation*.

In the following example, the`doorLock`property is kept private from anything outside of the`Car`class. To unlock the car, you must call the`unlockDoor()`function passing in a valid key, as shown in the following example:  

    class Car(val wheels: List<Wheel>) {

        private val doorLock: DoorLock = ...

        fun unlockDoor(key: Key): Boolean {
            // Return true if key is valid for door lock, false otherwise
        }
    }

If you would like to customize how a property is referenced, you can provide a custom getter and setter. For example, if you would like to expose a property's getter while restricting access to its setter, you can designate that setter as`private`:  

    class Car(val wheels: List<Wheel>) {

        private val doorLock: DoorLock = ...

        var gallonsOfFuelInTank: Int = 15
            private set

        fun unlockDoor(key: Key): Boolean {
            // Return true if key is valid for door lock, false otherwise
        }
    }

With a combination of properties and functions, you can create classes that model all types of objects.

## Interoperability

One of Kotlin's most important features is its fluid interoperability with Java. Because Kotlin code compiles down to JVM bytecode, your Kotlin code can call directly into Java code and vice-versa. This means that you can leverage existing Java libraries directly from Kotlin. Furthermore, the majority of Android APIs are written in Java, and you can call them directly from Kotlin.

## Next steps

Kotlin is a flexible, pragmatic language with growing support and momentum. We encourage you to give it a try if you haven't yet. For next steps, take a look at the[official Kotlin documentation](https://kotlinlang.org/)along with the guide on how to apply[common Kotlin patterns](https://developer.android.com/kotlin/common-patterns)in your Android apps.