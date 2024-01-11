import pyautogui
import time
import random
import json
from pathlib import Path

from actions.Interfaces import iClicker

class Clicker(iClicker):
    def __init__(self):
        print("Initialising: Base clicker")
    def click(self, position: tuple):
        """Clicks on given position on the screen.
        Args:
            position (tuple): x, y pixel location to click
        """
        pyautogui.click(position[0], position[1])

class ClickerWithDeviation(iClicker):
    def __init__(self, random_position_deviation_pixels = 0, random_sleep_deviation_secs = 0.5):
        self.random_position_deviation_pixels = random_position_deviation_pixels
        self.random_sleep_deviation_secs = random_sleep_deviation_secs
        print("Initialising: Clicker with deviation")
        print(f' - Random_position_deviation_pixels: {random_position_deviation_pixels}')
        print(f' - Random_sleep_deviation_secs: {random_sleep_deviation_secs}')

    def click(self, position: tuple):
        random_position = (position[0] + random.randrange(-self.random_position_deviation_pixels, self.random_position_deviation_pixels),
                       position[1] + random.randrange(-self.random_position_deviation_pixels, self.random_position_deviation_pixels))
        pyautogui.mouseDown(x = random_position[0], y = random_position[1]);
        random_sleep_sec = random.random()*self.random_sleep_deviation_secs
        time.sleep(random_sleep_sec)
        pyautogui.mouseUp(x = random_position[0], y = random_position[1])


def create_clicker(parameters: dict)-> iClicker:
    Factories = {'baseClicker': BaseClickerFactory(),
                'randomClicker': RandomClickerFactory(),
                'premadeClicker': PremadeClickerFactory()}
    Factory = Factories[parameters['type']]
    return Factory.create_clicker(parameters)

class iClickerFactory:
    def create_clicker(self, parameters: dict)-> iClicker:
        pass
    
class BaseClickerFactory(iClickerFactory):
    def create_clicker(self, parameters: dict):
        return Clicker()

class RandomClickerFactory(iClickerFactory):
    def create_clicker(self, parameters: dict):
        return ClickerWithDeviation(random_position_deviation_pixels = parameters['pixel_deviation'], 
                                    random_sleep_deviation_secs = parameters['second_deviation'])
    
class PremadeClickerFactory(iClickerFactory):
    def create_clicker(self, parameters: dict)-> iClicker:
        """Creates a premade clicker defined by jsons in the pramde clicker folder
        Args:
            parameters (dict): requires a "name": [name] combination. Where [name] is one 
            of the premades defined in the premade folder.
        Returns:
            iClicker: returns the premade clicker
        """
        name = parameters['name']
        path = Path(__file__).parent / f'./premade_clickers/{name}.json'
        print(f"Using premade clicker: {name}")
        with open(path, 'r') as j:
            config = json.loads(j.read())
        return create_clicker(parameters = config)