import sys
sys.path.append('./multi_clicker')

from actions import Locators

def test_image_finder():
    ImFi = Locators.ImageFinder(image_file = 'testWindowLogo.png', folder = './Tests/TestData/')
    result = ImFi.locate()
    print(result)
    assert result == (29, 1056), "Wrong windows logo location"

def test_image_displace():
    ImFi = Locators.ImageFinder(image_file = 'testWindowLogo.png', folder = './Tests/TestData/', displace_pixels = (5,5))
    result = ImFi.locate()
    print(result)
    assert result == [34, 1061], "Window location wronly displaced"

def main():
    test_image_finder()
    test_image_displace()

if __name__ == "__main__":
    main()
