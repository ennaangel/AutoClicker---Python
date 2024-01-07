import pyautogui
import time
import random

class iClicker:
    def click(self,position: tuple):
        pass

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

def click_pixel_colour(position: tuple, hex_colour: tuple, Clicker: Clicker, delay_seconds: float = 0, random_delay_deviation_secs: float = 0):
    if hex_colour != pyautogui.pixel(position[0], position[1]):
        return False
    if delay_seconds != 0:
        delay_seconds = delay_seconds + random.random()*random_delay_deviation_secs
        print(f'Waiting {delay_seconds} seconds')
        time.sleep(delay_seconds)
    Clicker.click(position)
    return True


def fail_safe(x = 0, y = 0):
    """Abort program if mouse position is (x,y)"""
    pos: tuple = pyautogui.position()
    if pos == (x,y):
        message: str = f'Cancelled becaus of mouse position ({x},{y})'
        raise Exception(message)
    
def get_mouse_pos_info()-> dict:
    pos: tuple = pyautogui.position()
    print(f'- position:{pos}')
    hex_colour = pyautogui.pixel(pos[0], pos[1])
    print(f'- colour: {hex_colour}')
    return {'position': pos, 'hex_colour':hex_colour}