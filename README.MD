# Python Autoclicker
Folder contains auto clickers and their related functions. Mainly used to automate some things in games.
# How to use?
1. Open `main.py` source folder.
3. Define to amount of clicks to perform and time to wait in each iteration.
2. Define the action to perform.
4. Execute script
# Structure
All functiionality can be found in `source` and test for the different elements in `Tests`. Also has some utility code in `Utility`.
## actions
`actions` is the Package containing most of the functionality in the whole project.
- **Actions** These are the building blocks for the Auto clicker. Each action has only one fucntion called 'do()', which executes the action.
- **Factories** Factories to create the Actions
- **Clickers** Contains functiosn and classes for clicking. Each clikcer only has one fucntion 'click(position)', which click on the given pixel location.
- **Locators** Contains functions and classes for finding and returning locations on the screen.
- **Sleepers** Contains functions and classes for sleeping including randomization.
- **Interfaces** Includes most interfaces 

