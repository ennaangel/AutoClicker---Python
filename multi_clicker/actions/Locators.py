import pyautogui

class iLocator:
    def locate(self):
        pass

class ImageFinder(iLocator):
    def __init__(self, image_file: str, folder: str = "") -> None:
        self.path

    def locate(self):
        """Returns centra location of the image, if not found return None"""
        try:
            location = pyautogui.locateOnScreen(path, confidence = confidence, grayscale = grayscale)
        except pyautogui.ImageNotFoundException:
            return None
        return pyautogui.center(location) 
