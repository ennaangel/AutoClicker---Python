## Actions
These are the building blocks for the Auto clicker. Each action has only one fucntion called `do()`, which executes the action.
### iAction
Interface for the Action class.
### ClickAction

## Factories
### create_action(parameters)
A factory method to create the action. Each action has it's own factory class.

The function takes a dictionary as input with the following general format:

```json
{"action": action_name,
"action_parameters": {
        "parameters": action_specefic_parameters,
        action_specefic_variables: action_specefic_variables_values}
}
```
- **action_name**: the name of the action type. See below for possible action types.
    - **[premadeAction](#PremadeActionFactory)**: Creates a premade action defined in the premade_actions folder
    - **[clickAction](#ClickActionFactory)**: Creates a click action.
    - **[sleepAction](#SleepActionFactory)**: Creates a sleep action.
    - **[multiAction](MultiActionFactory)**: Creates a multi action from a list of multiple actions.
    - **[clickLocation](#LocatorClickerActionFactory)**: Creates a action to click on a location.
- **action_specefic_parameters**: Parameter dictionary for the specefic action. Each ation needs it's own parameters.
- **action_specefic_variables**: Variables used in the actions.

### PremadeActionFactory

```json
{"action": "premadeAction",
"action_parameters":{"name": premade_json_file_name}}
```
- **premade_json_file_name**: the file name of the predefined action, without the .json extension. For example: `'TestClickWindowsLogo'`
### SleepActionFactory

```json
{"action": "sleepAction",
"action_parameters": {
    "parameters": {
        "type": sleeper_type,
        sleep_specefic_parameters: sleeper_parameters_values},
    "duration": sleep_duration,
    "min_duration_secs": minimal_sleep_duration}
}
```
- **sleeper_type**: Indicate the type of sleeper to use.
- **sleep_duration**: Duration  for the sleeper to sleep.
- **sleep_specefic_parameters:** If the sleeper object reuired parameters, they are indicated here.
- **"min_duration_secs": minimal_sleep_duration**: Optional argument for random sleep functions. Indicating the minal sleepign time.
### LocatorClickerActionFactory
```json
{"action": "clickLocation",
"action_parameters": {
    "parameters": {
        "clicker": clicker_action_parameters,
        "sleeper": sleeper_action_parameters,
        "locator": {
            "type": locator_type,
            locator_specefic_parameters: locator_parameters_values}
}}}
```
- **clicker**: Pass clicker action parameters for the kind of clicker to be used.
- **locator_type**: Type of locator to use.
- **locator_specefic_parameters**: Locator specefic parameters.
- **sleeper**: (Optional)Pass sleeper action parameters for the kind of clicker to be used.

### MultiActionFactory
```json
{"action": "multiAction",
"action_parameters": {"actions": [list_of_actions]}
}
```
### ClickActionFactory
Creates a click action.
```json
{"action": "clickAction",
"action_parameters": {
    "parameters": {
        "type": clicker_type,
        clicker_specefic_parameters: clicker_parameters_values},
    "position": position}
}
```
- **clicker_type**: Indicate the type of clicker to use.
- **position**: Pixel location for the click to happen.
## Clickers
Contains functiosn and classes for clicking.
### iClicker
Interface for clicker classes. Each clicker needs only a click method with a single paramete ie a position tuple.
### Clicker
Clicks on the location supplied as an (x,y) tuple.
### ClickerWithDeviation
Clicks on the location supplied by an (x,y) tuple, but with a ceratin deviation in location and pressing time. Used for game with bot checks.

Needs to be initialised with the following parameters:
- **random_position_deviation_pixels:** Click location deviaiton in pxiels.
- **random_sleep_deviation_secs:** Button press time deviation in seconds.
