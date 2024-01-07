import pyautogui
import os

class iLocator:
    def locate(self):
        pass

class ImageFinder(iLocator):
    def __init__(self, image_file: str, folder: str = "", confidence = 0.9, grayscale = False) -> None:
        self.path = os.path.join(folder, image_file)
        self.confidence = confidence 
        self.grayscale = grayscale

    def locate(self):
        """Returns centra location of the image, if not found return None"""
        try:
            location = pyautogui.locateOnScreen(self.path, confidence = self.confidence, grayscale = self.grayscale)
        except pyautogui.ImageNotFoundException:
            return None
        return pyautogui.center(location) 
