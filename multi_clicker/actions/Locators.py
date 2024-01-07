import pyautogui
import os

class iLocator:
    def locate(self):
        pass

class ImageFinder(iLocator):
    def __init__(self, image_file: str, folder: str = "", confidence = 0.9, grayscale = False, displace_pixels: tuple = None) -> None:
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
        self.displace_pixels = displace_pixels

    def locate(self):
        """Returns centra location of the image, if not found return None"""
        try:
            location = pyautogui.locateOnScreen(self.path, confidence = self.confidence, grayscale = self.grayscale)
        except pyautogui.ImageNotFoundException:
            return None
        location = pyautogui.center(location)
        if self.displace_pixels != None:
            location = self.displace(location = location, displace_pixels = self.displace_pixels)
        return location
    
    def displace(self, location: tuple, displace_pixels: tuple)-> list:
        """Displaces given location with supplied displace tuple, returning the new location as a list
        Args:
            location (tuple): initial location as tuple or box type
            displace_pixels (tuple): displace
        Returns:
            list: _description_
        """
        location_list: list = [0,0]
        location_list[1] = location[1] + displace_pixels[1]
        location_list[0] = location[0] + displace_pixels[0]
        return location_list
