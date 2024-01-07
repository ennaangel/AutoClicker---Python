## Actions
These are the building blocks for the Auto clicker. Each action has only one fucntion called 'do()', which executes the action.
### iAction
Interface for the Action class
### ClickAction
## Factories

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
