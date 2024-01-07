
import time
import ClickerFunctions



for i in range(50):
    time.sleep(0.5)
    ClickerFunctions.fail_safe(x = 0, y = 0)
    ClickerFunctions.get_mouse_pos_info()
    