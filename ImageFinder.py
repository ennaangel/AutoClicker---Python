import pyautogui

def get_image_centre(path: str, confidence = 0.9, grayscale = True):
    """Returns centra location of the image, if not found return None"""
    try:
        location = pyautogui.locateOnScreen(path, confidence = confidence, grayscale = grayscale)
    except pyautogui.ImageNotFoundException:
        return None
    return pyautogui.center(location)

