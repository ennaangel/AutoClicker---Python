import os
import time
import random
import sys

sys.path.append('')
import ImageFinder
import ClickerFunctions
import LoopManagerV1

clicks_to_stop = 94
clicker_positon_deviation = 7
image_folder = './click_image/image/'
time_interval_seconds = 3

RandClicker = ClickerFunctions.ClickerWithDeviation(random_position_deviation_pixels = clicker_positon_deviation)
LM = LoopManagerV1.LoopManager(clicks_to_stop = clicks_to_stop, loop_duration = time_interval_seconds)

def get_image_path(folder: str, extension = '.png')-> str:
    """Get path of the image located in the folder, only the irst image is used"""
    files = os.listdir(folder)
    image_path = [file for file in files if file.endswith(extension)]
    return os.path.join(folder, image_path[0])

def random_sleep(time_secs = 2):
    """Sleeps for a random interval between 0 and time seconds"""
    time.sleep(time_secs*random.random())

def random_random_sleep(chance, time_secs):
    """Sleeps for a random interval between 0 and time seconds at random moments
    with 1/chance chance"""
    if random.randint(0,chance) == 0:
        sleep_time_sec = time_secs*random.random()
        time.sleep(sleep_time_sec)
    

def main():
    LM.show_clicks_to_stop()
    image = get_image_path(folder = image_folder)
    while LM.clicks != LM.clicks_to_stop:
        LM.sleep()
        ClickerFunctions.fail_safe(x = 0, y = 0)
        random_random_sleep(chance = 3, time_secs = 4)
        location = ImageFinder.get_image_centre(image)
        if location != None:
            time.sleep(5)
            random_sleep(time_secs = 4)
            RandClicker.click(location)
            LM.add_clicks()
            LM.get_clicks_to_go()
            LM.get_loop_time()

    LM.get_run_time()
    
if __name__ == "__main__":
    main()