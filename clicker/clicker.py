import pyautogui
import time
import sys
import json

sys.path.append('')
import ClickerFunctions
import clicker.InfoManager as InfoManager


# Set configs
with open('./clickerConfigs.json', 'r') as j:
     config = json.loads(j.read())

time_interval_seconds = config['time_interval_seconds']
clicks_to_stop = config['total_clicks']
click_position = config['click_position']
click_hex_colour = tuple(config['click_hex_colour'])
click_delay_seconds = config['click_delay_seconds']
click_delay_deviation_secs = config['click_delay_deviation_seconds']

clicker_positon_deviation = config['clicker']['positon_deviation']
clicker_sleep_devivation = config['clicker']['sleep_devivation']


RandClicker = ClickerFunctions.ClickerWithDeviation(random_position_deviation_pixels = clicker_positon_deviation, 
                                                    random_sleep_deviation_secs = clicker_sleep_devivation)
IM = InfoManager.InfoManager(clicks_to_stop = clicks_to_stop)

def main():
    IM.show_clicks_to_stop()
    while IM.clicks != IM.clicks_to_stop:
        time.sleep(time_interval_seconds)
        ClickerFunctions.fail_safe(x = 0, y = 0)
        if ClickerFunctions.click_pixel_colour(position = click_position,  
                                            hex_colour = click_hex_colour,
                                            Clicker = RandClicker,
                                            delay_seconds = click_delay_seconds,
                                            random_delay_deviation_secs = click_delay_deviation_secs):
            IM.add_clicks()
            IM.get_clicks_to_go()
            IM.get_loop_time()

    IM.get_run_time()
    
if __name__ == "__main__":
    main()


        
    