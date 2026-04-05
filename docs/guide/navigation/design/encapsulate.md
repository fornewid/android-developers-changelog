---
title: https://developer.android.com/guide/navigation/design/encapsulate
url: https://developer.android.com/guide/navigation/design/encapsulate
source: md.txt
---

# Encapsulate your navigation code

When using the Kotlin DSL to construct your graph, keeping destinations and navigation events in a single file can be difficult to maintain. This is especially true if you have multiple independent features.

## Extract destinations

You should move your destinations into[`NavGraphBuilder`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder)extension functions. They should live close to the routes which define them, and the screens that they display. For example, consider the following app-level code that creates a destination which shows a list of contacts:  

    // MyApp.kt

    @Serializable
    object Contacts

    @Composable
    fun MyApp() {
      ...
      NavHost(navController, startDestination = Contacts) {
        composable<Contacts> { ContactsScreen( /* ... */ ) }
      }
    }

You should move the navigation-specific code into a separate file:  

    // ContactsNavigation.kt

    @Serializable
    object Contacts

    fun NavGraphBuilder.contactsDestination() {
        composable<Contacts> { ContactsScreen( /* ... */ ) }
    }

    // MyApp.kt

    @Composable
    fun MyApp() {
      ...
      NavHost(navController, startDestination = Contacts) {
         contactsDestination()
      }
    }

The routes and destination definitions are now separate from the main app and you can update them independently. The main app is only dependent on a single extension function. In this case, that is`NavGraphBuilder.contactsDestination()`.

The`NavGraphBuilder`extension function forms the bridge between a stateless screen-level composable function and Navigation-specific logic. This layer can also define where the state comes from and how you handle events.
| **Note:** This is essentially the same approach as when you move screens to different composable functions instead of defining them in one monolithic composable function.

## Example

The following snippet introduces a new destination to display a contact's details, and updates the existing contact list destination to[expose a navigation event](https://developer.android.com/guide/navigation/use-graph/navigate#nav-from-composable)to display the contact's details.

Here's a typical set of screens that can be`internal`to their own module, so that other modules cannot access them:  

    // ContactScreens.kt

    // Displays a list of contacts
    @Composable
    internal fun ContactsScreen(
      uiState: ContactsUiState,
      onNavigateToContactDetails: (contactId: String) -> Unit
    ) { ... }

    // Displays the details for an individual contact
    @Composable
    internal fun ContactDetailsScreen(contact: ContactDetails) { ... }

### Create destinations

The following[`NavGraphBuilder`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder)extension function creates a destination which shows the`ContactsScreen`composable. In addition, it now connects the screen with a`ViewModel`that provides the screen UI state and handles the screen-related business logic.

Navigation events, such as navigating to the contact details destination, are exposed to the caller rather than being handled by the`ViewModel`.  

    // ContactsNavigation.kt

    @Serializable
    object Contacts

    // Adds contacts destination to `this` NavGraphBuilder
    fun NavGraphBuilder.contactsDestination(
      // Navigation events are exposed to the caller to be handled at a higher level
      onNavigateToContactDetails: (contactId: String) -> Unit
    ) {
      composable<Contacts> {
        // The ViewModel as a screen level state holder produces the screen
        // UI state and handles business logic for the ConversationScreen
        val viewModel: ContactsViewModel = hiltViewModel()
        val uiState = viewModel.uiState.collectAsStateWithLifecycle()
        ContactsScreen(
          uiState,
          onNavigateToContactDetails
        )
      }
    }

You can use the same approach to create a destination which displays the`ContactDetailsScreen`. In this case, instead of obtaining the UI state from a view model, you can obtain it directly from the`NavBackStackEntry`.  

    // ContactsNavigation.kt

    @Serializable
    internal data class ContactDetails(val id: String)

    fun NavGraphBuilder.contactDetailsScreen() {
      composable<ContactDetails> { navBackStackEntry ->
        ContactDetailsScreen(contact = navBackStackEntry.toRoute())
      }
    }

### Encapsulate navigation events

In the same way that you encapsulate destinations, you can encapsulate navigation events to avoid exposing route types unnecessarily. Do this by creating extension functions on`NavController`.  

    // ContactsNavigation.kt

    fun NavController.navigateToContactDetails(id: String) {
      navigate(route = ContactDetails(id = id))
    }

### Bring it together

The navigation code for displaying contacts is now cleanly separated from the app's navigation graph. The app needs to:

- Call`NavGraphBuilder`extension functions to create destinations
- Connect those destinations by calling`NavController`extension functions for navigation events

    // MyApp.kt

    @Composable
    fun MyApp() {
      ...
      NavHost(navController, startDestination = Contacts) {
         contactsDestination(onNavigateToContactDetails = { contactId ->
            navController.navigateToContactDetails(id = contactId)
         })
         contactDetailsDestination()
      }
    }

## In summary

- Encapsulate your navigation code for a related set of screens by placing it in a separate file
- Expose destinations by creating extension functions on`NavGraphBuilder`
- Expose navigation events by creating extension functions on`NavController`
- Use`internal`to keep screens and route types private