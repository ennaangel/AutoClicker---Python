
import time
import pyautogui

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


for i in range(50):
    time.sleep(0.5)
    fail_safe(x = 0, y = 0)
    get_mouse_pos_info()
    