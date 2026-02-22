---
title: https://developer.android.com/training/data-storage/room/referencing-data
url: https://developer.android.com/training/data-storage/room/referencing-data
source: md.txt
---

# Referencing complex data using Room

Room provides functionality for converting between primitive and boxed types but doesn't allow for object references between entities. This document explains how to use type converters and why Room doesn't support object references.

## Use type converters

Sometimes, you need your app to store a custom data type in a single database column. You support custom types by providing*type converters* , which are methods that tell Room how to convert custom types to and from known types that Room can persist. You identify type converters by using the[`@TypeConverter`](https://developer.android.com/reference/androidx/room/TypeConverter)annotation.
| **Note:** Room 2.3 and higher includes a default type converter for persisting enums. Existing type converters take precedence over the default, but if you have not already defined a type converter for enums then you don't need to define one.

Suppose you need to persist instances of[`Date`](https://developer.android.com/reference/java/util/Date)in your Room database. Room doesn't know how to persist`Date`objects, so you need to define type converters:  

### Kotlin

```kotlin
class Converters {
  @TypeConverter
  fun fromTimestamp(value: Long?): Date? {
    return value?.let { Date(it) }
  }

  @TypeConverter
  fun dateToTimestamp(date: Date?): Long? {
    return date?.time?.toLong()
  }
}
```

### Java

```java
public class Converters {
  @TypeConverter
  public static Date fromTimestamp(Long value) {
    return value == null ? null : new Date(value);
  }

  @TypeConverter
  public static Long dateToTimestamp(Date date) {
    return date == null ? null : date.getTime();
  }
}
```

This example defines two type converter methods: one that converts a`Date`object to a`Long`object, and one that performs the inverse conversion from`Long`to`Date`. Because Room knows how to persist`Long`objects, it can use these converters to persist`Date`objects.

Next, you add the[`@TypeConverters`](https://developer.android.com/reference/androidx/room/TypeConverters)annotation to the`AppDatabase`class so that Room knows about the converter class that you have defined:  

### Kotlin

```kotlin
@Database(entities = [User::class], version = 1)
@TypeConverters(Converters::class)
abstract class AppDatabase : RoomDatabase() {
  abstract fun userDao(): UserDao
}
```

### Java

```java
@Database(entities = {User.class}, version = 1)
@TypeConverters({Converters.class})
public abstract class AppDatabase extends RoomDatabase {
  public abstract UserDao userDao();
}
```

With these type converters defined, you can use your custom type in your entities and DAOs just as you would use primitive types:  

### Kotlin

```kotlin
@Entity
data class User(private val birthday: Date?)

@Dao
interface UserDao {
  @Query("SELECT * FROM user WHERE birthday = :targetDate")
  fun findUsersBornOnDate(targetDate: Date): List<User>
}
```

### Java

```java
@Entity
public class User {
  private Date birthday;
}

@Dao
public interface UserDao {
  @Query("SELECT * FROM user WHERE birthday = :targetDate")
  List<User> findUsersBornOnDate(Date targetDate);
}
```

In this example, Room can use the defined type converter everywhere because you annotated`AppDatabase`with`@TypeConverters`. However, you can also scope type converters to specific entities or DAOs by annotating your`@Entity`or`@Dao`classes with`@TypeConverters`.

### Control type converter initialization

Ordinarily, Room handles instantiation of type converters for you. However, sometimes you might need to pass additional dependencies to your type converter classes, which means that you need your app to directly control initialization of your type converters. In that case, annotate your converter class with[`@ProvidedTypeConverter`](https://developer.android.com/reference/androidx/room/ProvidedTypeConverter):  

### Kotlin

```kotlin
@ProvidedTypeConverter
class ExampleConverter {
  @TypeConverter
  fun StringToExample(string: String?): ExampleType? {
    ...
  }

  @TypeConverter
  fun ExampleToString(example: ExampleType?): String? {
    ...
  }
}
```

### Java

```java
@ProvidedTypeConverter
public class ExampleConverter {
  @TypeConverter
  public Example StringToExample(String string) {
    ...
  }

  @TypeConverter
  public String ExampleToString(Example example) {
    ...
  }
}
```

Then, in addition to declaring your converter class in`@TypeConverters`, use the[`RoomDatabase.Builder.addTypeConverter()`](https://developer.android.com/reference/androidx/room/RoomDatabase.Builder#addTypeConverter(java.lang.Object))method to pass an instance of your converter class to the`RoomDatabase`builder:  

### Kotlin

```kotlin
val db = Room.databaseBuilder(...)
  .addTypeConverter(exampleConverterInstance)
  .build()
```

### Java

```java
AppDatabase db = Room.databaseBuilder(...)
  .addTypeConverter(exampleConverterInstance)
  .build();
```

## Understand why Room doesn't allow object references

**Key takeaway:**Room disallows object references between entity classes. Instead, you must explicitly request the data that your app needs.

Mapping relationships from a database to the respective object model is a common practice and works very well on the server side. Even when the program loads fields as they're accessed, the server still performs well.

However, on the client side, this type of lazy loading isn't feasible because it usually occurs on the UI thread, and querying information on disk in the UI thread creates significant performance problems. The UI thread typically has about 16 ms to calculate and draw an activity's updated layout, so even if a query takes only 5 ms, it's still likely that your app will run out of time to draw the frame, causing noticeable visual glitches. The query could take even more time to complete if there's a separate transaction running in parallel, or if the device is running other disk-intensive tasks. If you don't use lazy loading, however, your app fetches more data than it needs, creating memory consumption problems.

Object-relational mappings usually leave this decision to developers so that they can do whatever is best for their app's use cases. Developers usually decide to share the model between their app and the UI. This solution doesn't scale well, however, because as the UI changes over time, the shared model creates problems that are difficult for developers to anticipate and debug.

For example, consider a UI that loads a list of`Book`objects, with each book having an`Author`object. You might initially design your queries to use lazy loading to have instances of`Book`retrieve the author. The first retrieval of the`author`field queries the database. Some time later, you realize that you need to display the author name in your app's UI, as well. You can access this name easily enough, as shown in the following code snippet:  

### Kotlin

```kotlin
authorNameTextView.text = book.author.name
```

### Java

```java
authorNameTextView.setText(book.getAuthor().getName());
```

However, this seemingly innocent change causes the`Author`table to be queried on the main thread.

If you query author information ahead of time, it becomes difficult to change how data is loaded if you no longer need that data. For example, if your app's UI no longer needs to display`Author`information, your app effectively loads data that it no longer displays, wasting valuable memory space. Your app's efficiency degrades even further if the`Author`class references another table, such as`Books`.

To reference multiple entities at the same time using Room, you instead create a POJO that contains each entity, then write a query that joins the corresponding tables. This well-structured model, combined with Room's robust query validation capabilities, allows your app to consume fewer resources when loading data, improving your app's performance and user experience.