# Python Autoclicker
Folder contains auto clickers and their related functions. Mainly used to automate some things in games.

# Clickers
 - **[click_image:](#click_image)** Automatically clicks on an image of it appears on the screen.
- **clicker:** Automatically click on the given location if it has the given colour. (No longer used)
## click_image
Clicks on the image supplied, for the number of times supplied. Has some randomizing in time and pixel to subvert bot checkers.
### How to use?
1. Place a .png image in the image folder. Only one image can be inside this folder(Move previous images to archive). 
2. Set variables:
    - clicks_to_stop: clicks till stopping the loop
    - clicker_positon_deviation: pixel deviatoin for clicking. Use this for dodging bot checkers. The clicker will click within this pixel distance of the centre of teh image.
    - image_folder: Only change if you want to change the folder location of the supplied image.
    - time_interval_seconds: Start duration in secodns of each loop. Loops will take longer due to random sleeps.
3. Execute script.
    - Make sure the screen to check and click on is on your main screen.
4. To stop:
    - Move to cursor to the top left corner of your screen.
    - Or wait till the clicker has reached *clicks_to_stop* count.
# Other
- **ClickerFunctions:** contains functions and class for clicking.
- **ImageFinder:** Functions for finding the location of images on the screen.
- **LoopManager:** Class for managing the iterator.
## ClickerFunctions
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