---
title: https://developer.android.com/games/agdk/add-touch-support
url: https://developer.android.com/games/agdk/add-touch-support
source: md.txt
---

# Add touch support

To handle touch input events, read the array[`motionEvents`](https://developer.android.com/reference/android/view/MotionEvent)in your game loop. These contain events that have happened since the last time these arrays were cleared. The number of events contained is stored in`motionEventsCount`.
| **Note:** Prior to the addition of`GameActivity`, the`AInputQueue* inputQueue`field was used to handle input events. With`GameActivity`, this field has been removed from the`android_app`and no longer used for handling input events.

1. Iterate and handle each event in your game loop. In this example, the following code iterates`motionEvents`and handles them via`handle_event`:

       for(size_t i = 0; i < mApp->motionEventsCount; ++i) {
         GameActivityMotionEvent* motionEvent = mApp->motionEvents[i];

         int action = motionEvent->action;
         int actionMasked = action & AMOTION_EVENT_ACTION_MASK;
         int ptrIndex = (action & AMOTION_EVENT_ACTION_POINTER_INDEX_MASK) >>
           AMOTION_EVENT_ACTION_POINTER_INDEX_SHIFT;

         struct CookedEvent ev;
         memset(&ev, 0, sizeof(ev));

         if (actionMasked == AMOTION_EVENT_ACTION_DOWN ||
           actionMasked == AMOTION_EVENT_ACTION_POINTER_DOWN) {
             ev.type = COOKED_EVENT_TYPE_POINTER_DOWN;
         } else if (actionMasked == AMOTION_EVENT_ACTION_UP ||
           actionMasked == AMOTION_EVENT_ACTION_POINTER_UP) {
             ev.type = COOKED_EVENT_TYPE_POINTER_UP;
         } else {
             ev.type = COOKED_EVENT_TYPE_POINTER_MOVE;
         }

         ev.motionPointerId = motionEvent->pointers[ptrIndex].id;
         ev.motionIsOnScreen = motionEvent->source == AINPUT_SOURCE_TOUCHSCREEN;
         ev.motionX = GameActivityPointerInfo_getX(
           &motionEvent->pointers[ptrIndex]);
         ev.motionY = GameActivityPointerInfo_getY(
           &motionEvent->pointers[ptrIndex]);

         if (ev.motionIsOnScreen) {
           // Use screen size as the motion range.
           ev.motionMinX = 0.0f;
           ev.motionMaxX = SceneManager::GetInstance()->GetScreenWidth();
           ev.motionMinY = 0.0f;
           ev.motionMaxY = SceneManager::GetInstance()->GetScreenHeight();
         }

         handle_event(&ev);
       }

2. When you are done, remember to clear the queue of events that you have just handled:

       android_app_clear_motion_events(mApp);