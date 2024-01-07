import pyautogui
import os

class iLocator:
    def locate(self):
        pass

class ImageFinder(iLocator):
    def __init__(self, image_file: str, folder: str = "", confidence = 0.9, grayscale = False) -> None:
            """Find centre of image

        Args:
            image_file (str): file name of image
            folder (str, optional): Folder path of image. Defaults to "".
            confidence (float, optional): Confidence level of found image, 1 is 100% sure. Defaults to 0.9.
            grayscale (bool, optional): Enable Grayscale. Defaults to False.
        """
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
