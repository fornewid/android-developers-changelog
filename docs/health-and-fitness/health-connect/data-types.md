---
title: https://developer.android.com/health-and-fitness/health-connect/data-types
url: https://developer.android.com/health-and-fitness/health-connect/data-types
source: md.txt
---

<br />

Health Connect stores and structures both health and fitness data and medical
records data. It's important to understand first what data types and permissions
Health Connect offers so that you can plan your app's requirements.

After development, when you prepare to publish your app to the Play Store, you
must declare your app's data use as well as declare access to the Health Connect
data types that your app uses. Otherwise, users might be prompted with an error
message where your app can't access the Health Connect data types because they
require special approval.

See [Complete the health apps declaration in the Play Console](https://developer.android.com/health-and-fitness/guides/health-connect/publish/declare-access)
for more information.

## Data type categories

Health Connect supports data types that are used across most health and fitness
apps to provide as much variety as possible. Health Connect aims to offer a
comprehensive view and storage of health and fitness data. These data types fall
into the following categories:

<br />

| Category || Description |
|---|---|---|
| directions_run | **Activity** | This captures any activity that a user does. It can include health and fitness activities like running and swimming. |
| straighten | **Body Measurement** | This captures common data related to the body, such as a user's weight and their basal metabolic rate. |
| fertile | **Cycle Tracking** | This captures menstrual cycles and related data points, such as the binary result of an ovulation test. |
| grocery | **Nutrition** | This captures hydration and nutrition data types. The former represents how much water a user consume in a single drink. The latter includes optional fields such as calories, sugar, and magnesium. |
| sleep_auto | **Sleep** | This captures interval data related to a user's length and type of sleep. |
| vital_signs | **Vitals** | This captures essential information about the user's general health. It includes data such as body temperature, blood glucose, blood pressure, and blood oxygen saturation. |
| mindfulness | **Wellness** | This captures data related to a user's mental health and well-being. |
[*Table: Health Connect data type categories*]

<br />

## Health and fitness data types

Before requesting any permissions, your app must declare them in the manifest.
See the [Declare permissions](https://developer.android.com/health-and-fitness/guides/health-connect/develop/get-started#declare-permissions) section of the Quick start
guide for more information.

To read data while your app is in the background, or to read historical data, an
additional set of read permissions must be declared separately from data type
permissions:

<br />

| Additional read permission | Permission declaration |
|---|---|
| **Read data in background** <br /> [Background read example](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#background-read-example) guide | `android.permission.health.READ_HEALTH_DATA_IN_BACKGROUND` |
| **Read historical data** <br /> [Read data older than 30 days](https://developer.android.com/health-and-fitness/guides/health-connect/develop/read-data#read-older-data) guide | `android.permission.health.READ_HEALTH_DATA_HISTORY` |
[*Table: Additional read permissions for Health Connect data types*]

<br />

### 1. Select a Jetpack version

Permission declarations differ between Jetpack versions, make sure to the select
the Jetpack version range your app uses.

<button value="alpha10plus" default="">1.0.0-alpha10 and higher</button> <button value="alpha09">1.0.0-alpha09 and lower</button>

### 2. Filter the data types table

The following table contains the full list of data types, each with category,
feature flags and guides, and permission declarations.

| Data type Feature guides | Category | Record type Permission declarations Feature flag |
|---|---|---|
| **Active calories burned** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActiveCaloriesBurnedRecord` `android.permission.health.READ_ACTIVE_CALORIES_BURNED` `android.permission.health.WRITE_ACTIVE_CALORIES_BURNED` |
| **Activity intensity** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ActivityIntensityRecord` `android.permission.health.READ_ACTIVITY_INTENSITY` `android.permission.health.WRITE_ACTIVITY_INTENSITY` <br /> `FEATURE_ACTIVITY_INTENSITY` |
| **Basal body temperature** | Cycle Tracking | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BasalBodyTemperatureRecord` `android.permission.health.READ_BASAL_BODY_TEMPERATURE` `android.permission.health.WRITE_BASAL_BODY_TEMPERATURE` |
| **Basal metabolic rate** | Body Measurement | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BasalMetabolicRateRecord` `android.permission.health.READ_BASAL_METABOLIC_RATE` `android.permission.health.WRITE_BASAL_METABOLIC_RATE` |
| **Blood glucose** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodGlucoseRecord` `android.permission.health.READ_BLOOD_GLUCOSE` `android.permission.health.WRITE_BLOOD_GLUCOSE` |
| **Blood pressure** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BloodPressureRecord` `android.permission.health.READ_BLOOD_PRESSURE` `android.permission.health.WRITE_BLOOD_PRESSURE` |
| **Body fat** | Body Measurement | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BodyFatRecord` `android.permission.health.READ_BODY_FAT` `android.permission.health.WRITE_BODY_FAT` |
| **Body temperature** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BodyTemperatureRecord` `android.permission.health.READ_BODY_TEMPERATURE` `android.permission.health.WRITE_BODY_TEMPERATURE` |
| **Body water mass** | Body Measurement | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BodyWaterMassRecord` `android.permission.health.READ_BODY_WATER_MASS` `android.permission.health.WRITE_BODY_WATER_MASS` |
| **Bone mass** | Body Measurement | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/BoneMassRecord` `android.permission.health.READ_BONE_MASS` `android.permission.health.WRITE_BONE_MASS` |
| **Cervical mucus** | Cycle Tracking | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/CervicalMucusRecord` `android.permission.health.READ_CERVICAL_MUCUS` `android.permission.health.WRITE_CERVICAL_MUCUS` |
| **Cycling pedaling cadence** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/CyclingPedalingCadenceRecord` `android.permission.health.READ_EXERCISE` `android.permission.health.WRITE_EXERCISE` |
| **Distance** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/DistanceRecord` `android.permission.health.READ_DISTANCE` `android.permission.health.WRITE_DISTANCE` |
| **Elevation gained** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ElevationGainedRecord` `android.permission.health.READ_ELEVATION_GAINED` `android.permission.health.WRITE_ELEVATION_GAINED` |
| **Exercise** [Add exercise routes](https://developer.android.com/health-and-fitness/guides/health-connect/develop/exercise-routes) guide | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExerciseSessionRecord` `android.permission.health.READ_EXERCISE` `android.permission.health.READ_EXERCISE_ROUTE` `android.permission.health.WRITE_EXERCISE` `android.permission.health.WRITE_EXERCISE_ROUTE` #### Exercise types [View all exercise types](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/ExerciseSessionRecord#summary) `EXERCISE_TYPE_UNKNOWN` `EXERCISE_TYPE_BADMINTON` `EXERCISE_TYPE_BASEBALL` `EXERCISE_TYPE_BASKETBALL` `EXERCISE_TYPE_BIKING` `EXERCISE_TYPE_BIKING_STATIONARY` `EXERCISE_TYPE_BOOT_CAMP` `EXERCISE_TYPE_BOXING` `EXERCISE_TYPE_CALISTHENICS` `EXERCISE_TYPE_CRICKET` `EXERCISE_TYPE_DANCING` `EXERCISE_TYPE_ELLIPTICAL` `EXERCISE_TYPE_EXERCISE_CLASS` `EXERCISE_TYPE_FENCING` `EXERCISE_TYPE_FOOTBALL_AMERICAN` `EXERCISE_TYPE_FOOTBALL_AUSTRALIAN` `EXERCISE_TYPE_FRISBEE_DISC` `EXERCISE_TYPE_GOLF` `EXERCISE_TYPE_GUIDED_BREATHING` `EXERCISE_TYPE_GYMNASTICS` `EXERCISE_TYPE_HANDBALL` `EXERCISE_TYPE_HIGH_INTENSITY_INTERVAL_TRAINING` `EXERCISE_TYPE_HIKING` `EXERCISE_TYPE_ICE_HOCKEY` `EXERCISE_TYPE_ICE_SKATING` `EXERCISE_TYPE_MARTIAL_ARTS` `EXERCISE_TYPE_PADDLING` `EXERCISE_TYPE_PARAGLIDING` `EXERCISE_TYPE_PILATES` `EXERCISE_TYPE_RACQUETBALL` `EXERCISE_TYPE_ROCK_CLIMBING` `EXERCISE_TYPE_ROLLER_HOCKEY` `EXERCISE_TYPE_ROWING` `EXERCISE_TYPE_ROWING_MACHINE` `EXERCISE_TYPE_RUGBY` `EXERCISE_TYPE_RUNNING` `EXERCISE_TYPE_RUNNING_TREADMILL` `EXERCISE_TYPE_SAILING` `EXERCISE_TYPE_SCUBA_DIVING` `EXERCISE_TYPE_SKATING` `EXERCISE_TYPE_SKIING` `EXERCISE_TYPE_SNOWBOARDING` `EXERCISE_TYPE_SNOWSHOEING` `EXERCISE_TYPE_SOCCER` `EXERCISE_TYPE_SOFTBALL` `EXERCISE_TYPE_SQUASH` `EXERCISE_TYPE_STAIR_CLIMBING` `EXERCISE_TYPE_STAIR_CLIMBING_MACHINE` `EXERCISE_TYPE_STRENGTH_TRAINING` `EXERCISE_TYPE_STRETCHING` `EXERCISE_TYPE_SURFING` `EXERCISE_TYPE_SWIMMING_OPEN_WATER` `EXERCISE_TYPE_SWIMMING_POOL` `EXERCISE_TYPE_TABLE_TENNIS` `EXERCISE_TYPE_TENNIS` `EXERCISE_TYPE_VOLLEYBALL` `EXERCISE_TYPE_WALKING` `EXERCISE_TYPE_WATER_POLO` `EXERCISE_TYPE_WEIGHTLIFTING` `EXERCISE_TYPE_WHEELCHAIR` `EXERCISE_TYPE_OTHER_WORKOUT` `EXERCISE_TYPE_YOGA` |
| **Floors climbed** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/FloorsClimbedRecord` `android.permission.health.READ_FLOORS_CLIMBED` `android.permission.health.WRITE_FLOORS_CLIMBED` |
| **Heart rate** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateRecord` `android.permission.health.READ_HEART_RATE` `android.permission.health.WRITE_HEART_RATE` |
| **Heart rate variability** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeartRateVariabilityRmssdRecord` `android.permission.health.READ_HEART_RATE_VARIABILITY` `android.permission.health.WRITE_HEART_RATE_VARIABILITY` |
| **Height** | Body Measurement | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HeightRecord` `android.permission.health.READ_HEIGHT` `android.permission.health.WRITE_HEIGHT` |
| **Hydration** | Nutrition | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/HydrationRecord` `android.permission.health.READ_HYDRATION` `android.permission.health.WRITE_HYDRATION` |
| **Intermenstrual bleeding** | Cycle Tracking | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/IntermenstrualBleedingRecord` `android.permission.health.READ_INTERMENSTRUAL_BLEEDING` `android.permission.health.WRITE_INTERMENSTRUAL_BLEEDING` |
| **Lean body mass** | Body Measurement | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/LeanBodyMassRecord` `android.permission.health.READ_LEAN_BODY_MASS` `android.permission.health.WRITE_LEAN_BODY_MASS` |
| **Menstruation** | Cycle Tracking | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MenstruationFlowRecord` `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MenstruationPeriodRecord` `android.permission.health.READ_MENSTRUATION` `android.permission.health.WRITE_MENSTRUATION` |
| **Mindfulness** [Track mindfulness](https://developer.android.com/health-and-fitness/guides/health-connect/develop/mindfulness) guide | Wellness | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MindfulnessSessionRecord` `android.permission.health.READ_MINDFULNESS` `android.permission.health.WRITE_MINDFULNESS` <br /> `FEATURE_MINDFULNESS_SESSION` |
| **Nutrition** | Nutrition | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/NutritionRecord` `android.permission.health.READ_NUTRITION` `android.permission.health.WRITE_NUTRITION` |
| **Ovulation test** | Cycle Tracking | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/OvulationTestRecord` `android.permission.health.READ_OVULATION_TEST` `android.permission.health.WRITE_OVULATION_TEST` |
| **Oxygen saturation** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/OxygenSaturationRecord` `android.permission.health.READ_OXYGEN_SATURATION` `android.permission.health.WRITE_OXYGEN_SATURATION` |
| **Planned exercise** [Training plans](https://developer.android.com/health-and-fitness/guides/health-connect/develop/training-plans) guide | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PlannedExerciseSessionRecord` `android.permission.health.READ_PLANNED_EXERCISE` `android.permission.health.WRITE_PLANNED_EXERCISE` <br /> `FEATURE_PLANNED_EXERCISE` |
| **Power** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/PowerRecord` `android.permission.health.READ_POWER` `android.permission.health.WRITE_POWER` |
| **Respiratory rate** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RespiratoryRateRecord` `android.permission.health.READ_RESPIRATORY_RATE` `android.permission.health.WRITE_RESPIRATORY_RATE` |
| **Resting heart rate** | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/RestingHeartRateRecord` `android.permission.health.READ_RESTING_HEART_RATE` `android.permission.health.WRITE_RESTING_HEART_RATE` |
| **Sexual activity** | Cycle Tracking | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SexualActivityRecord` `android.permission.health.READ_SEXUAL_ACTIVITY` `android.permission.health.WRITE_SEXUAL_ACTIVITY` |
| **Skin temperature** [Measure skin temperature](https://developer.android.com/health-and-fitness/guides/health-connect/develop/skin-temperature) guide | Vitals | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SkinTemperatureRecord` `android.permission.health.READ_SKIN_TEMPERATURE` `android.permission.health.WRITE_SKIN_TEMPERATURE` <br /> `FEATURE_SKIN_TEMPERATURE` |
| **Sleep session** [Track sleep sessions](https://developer.android.com/health-and-fitness/guides/health-connect/develop/sleep-sessions) guide | Sleep | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SleepSessionRecord` `android.permission.health.READ_SLEEP` `android.permission.health.WRITE_SLEEP` |
| **Speed** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/SpeedRecord` `android.permission.health.READ_SPEED` `android.permission.health.WRITE_SPEED` |
| **Steps** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsRecord` `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/StepsCadenceRecord` `android.permission.health.READ_STEPS` `android.permission.health.WRITE_STEPS` |
| **Total calories burned** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/TotalCaloriesBurnedRecord` `android.permission.health.READ_TOTAL_CALORIES_BURNED` `android.permission.health.WRITE_TOTAL_CALORIES_BURNED` |
| **VO2 max** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/Vo2MaxRecord` `android.permission.health.READ_VO2_MAX` `android.permission.health.WRITE_VO2_MAX` |
| **Weight** | Body Measurement | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WeightRecord` `android.permission.health.READ_WEIGHT` `android.permission.health.WRITE_WEIGHT` |
| **Wheelchair pushes** | Activity | `https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/WheelchairPushesRecord` `android.permission.health.READ_WHEELCHAIR_PUSHES` `android.permission.health.WRITE_WHEELCHAIR_PUSHES` |
[*Table: Health Connect data types*]