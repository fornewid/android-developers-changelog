---
title: https://developer.android.com/studio/inspect/database
url: https://developer.android.com/studio/inspect/database
source: md.txt
---

# Debug your database with the Database Inspector

The Database Inspector lets you inspect, query, and modify your app's databases while your app is running. This is especially useful for database debugging. The Database Inspector works with plain SQLite and with libraries built on top of SQLite, such as[Room](https://developer.android.com/training/data-storage/room).
| **Note:** The Database Inspector only works with the SQLite library included in the Android operating system on API level 26 and higher. It doesn't work with other SQLite libraries that you bundle with your app.

## Open the Database Inspector

To open a database in the Database Inspector, do the following:

1. [Run your app](https://developer.android.com/studio/run)on an emulator or connected device running API level 26 or higher.

   | **Note:** A known issue related to the Android 11 emulator causes apps to crash when connecting to the Database Inspector. To fix the issue,[follow these steps](https://developer.android.com/studio/known-issues#ki-android-11-db-inspector).
2. From the menu bar, select**View \> Tool Windows \> App Inspection**.

3. Select the**Database Inspector**tab.

4. Select the running app process from the menu.

5. The databases in the currently running app appear in the**Databases**pane. Expand the node for the database that you want to inspect.

## View and modify data

The**Databases**pane displays a list of the databases in your app and the tables that each database contains. Double-click a table name to display its data in the inspector window to the right, shown in figure 1. Click a column header to sort the data in the inspector window by that column.
![Screenshot of the Database Inspector window.](https://developer.android.com/static/studio/images/inspect/db-inspector-window.png)**Figure 1.**The Database Inspector window.

To modify data in a table, follow these steps:

1. Double-click a cell.
2. Type a new value.
3. Press<kbd>Enter</kbd>.

If your app uses Room and your UI observes the database, such as with`LiveData`or`Flow`, then any changes you make to the data are immediately visible in your running app. Otherwise, changes are only visible the next time your app reads the modified data from the database.

### See live database changes

If you want the Database Inspector to automatically update the data it presents as you interact with your running app, select the**Live updates**checkbox at the top of the inspector window. While live updates are enabled, the table in the inspector window is read-only and you can't modify its values.

Alternatively, to manually update the data, click the**Refresh table**button at the top of the inspector window.

## Query your databases

The Database Inspector can run queries against your app's database while the app is running. The tool can use DAO queries if your app uses Room, but it also supports custom SQL queries.

### Run DAO queries

If your app uses Room, Android Studio provides gutter actions that let you quickly run query methods that you have already defined in your[DAO classes](https://developer.android.com/training/data-storage/room/accessing-data). These actions are available while your app is running and the Database Inspector is open in the IDE.

To run any query method in a DAO, click the**Run SQLite statement in Database Inspector** ![](https://developer.android.com/static/studio/images/app-inspection/database_inspector_query.png)button next to its`@Query`annotation.
![Screenshot of DAO gutter actions.](https://developer.android.com/static/studio/images/inspect/db-inspector-dao-gutters.png)**Figure 2.**DAO query gutter actions.

If your app includes more than one database, Android Studio prompts you to select the database to query against from a list. If your query method includes named[bind parameters](https://developer.android.com/training/data-storage/room/accessing-data#simple-parameters), Android Studio requests values for each parameter before running the query. The query results are displayed in the inspector window.

### Run custom SQL queries

You can also use the Database Inspector to run custom SQL queries against your app's databases while your app is running.

To query a database, follow these steps:

1. Click**Open New Query tab** ![](https://developer.android.com/static/studio/images/app-inspection/database_inspector_query.png)at the top of the**Databases**pane to open a new tab in the inspector window.

   ![Screenshot indicating the new query tab button.](https://developer.android.com/static/studio/images/inspect/db-inspector-new-query.png)**Figure 3.** Open a**New Query**tab.
2. If your app includes more than one database, select the database to query from the list on the**New Query**tab.

3. At the top of the**New Query**tab, type your custom SQL query into the text field.

4. Click**Run**.

Alternatively, use the query history feature to run a query that you used previously:

1. Click the**Show query history** ![Show query history button](https://developer.android.com/static/studio/images/buttons/db-inspector-query-history.png)button to see a list of queries that you previously ran against the selected database.

   ![Screenshot showing the query history drop-down.](https://developer.android.com/static/studio/images/inspect/db-inspector-history.png)**Figure 4.**The query history menu.
2. Click a query in the list to see a preview of the full query in the editor, and press<kbd>Enter</kbd>to copy it to the editor.

3. Click**Run**to execute the statement.

The query results that are displayed in the**New Query** tab are read-only and can't be modified. However, you can use the custom SQL query field to run modifier statements such as`UPDATE`,`INSERT`, or`DELETE`.

If your app uses Room and your UI observes the database, such as with`LiveData`or`Flow`, then any changes you make to the data are immediately visible in your running app. Otherwise, changes are only visible the next time your app reads the modified data from the database.

## Offline mode

In Android Studio 4.2 and higher, you can continue to inspect your app's databases after a process disconnects. This makes it easier to debug your app after a crash.

When a disconnect occurs, the Database Inspector downloads your databases and makes them available to you in*offline mode*. When offline, you can still open tables and run queries.

When you reconnect to a live app process, the Database Inspector leaves offline mode and shows you only the data that is on the device. In other words, data shown in offline mode does not persist when you reconnect to an app process. Because of this limitation, the Database Inspector doesn't let you edit data or run modification SQL statements while in offline mode.

When you are viewing a database in offline mode, the process name includes`[DETACHED]`to indicate that the inspector is no longer attached to the process. Also, the database icon![Database offline](https://developer.android.com/static/studio/images/app-inspection/database-offline.png)indicates the offline state, shown in figure 5.
![Database inspector in offline mode](https://developer.android.com/static/studio/images/inspect/db-inspector-window-offline.png)**Figure 5.**Database Inspector in offline mode.

## Keep database connections open

The Database Inspector can modify a database only while your app maintains a live connection to that database. That means that if your app frequently connects to and disconnects from databases, it can be difficult to debug those databases. The**Databases** pane uses icons to identify open![](https://developer.android.com/static/studio/images/app-inspection/database_inspector-db_open.png)and closed![](https://developer.android.com/static/studio/images/app-inspection/database_inspector-db_closed.png)databases.

Additionally, to prevent database connections from closing, toggle**Keep database connections open** from off![](https://developer.android.com/static/studio/images/app-inspection/database_inspector_unlocked.png)to on![](https://developer.android.com/static/studio/images/app-inspection/database_inspector_locked.png)at the top of the**Databases**pane.

#### Export data from the Database Inspector

You can export databases, tables, and query results from the Database Inspector to save, share, or re-create locally. When you open up an app project in Android Studio and inspect the app for that project in the Database Inspector, you can start exporting data in one of the following ways:

- Select a database or table in the**Databases** panel and click**Export to file**near the top of the panel.
- Right-click a database or table in the**Databases** panel and select**Export to file**from the context menu.
- When inspecting a table or query results in a tab, click**Export to file**above the table or query results.

After selecting an export action, use the**Export Database**dialog to help you through the final steps, as shown in figure 6.

Depending on whether you are trying to export a database, table, or query results, you have the option of exporting the data in one or more of the following formats: DB, SQL, or CSV.

![Export Database dialog box](https://developer.android.com/static/studio/images/inspect/export-database-dialog-box.png)
**Figure 6.**The Export Database dialog.

<br />

## Additional resources

To learn more about the Database Inspector, see the following additional resources:

### Blog posts

- [Database Inspector: A live database tool we've been waiting for!](https://medium.com/androiddevelopers/database-inspector-9e91aa265316)

### Videos

- [Database Inspector](https://www.youtube.com/watch?v=UMc7Tu0nKYQ)