import sys
sys.path.append('./source')

from actions import Locators

def test_image_finder():
    ImFi = Locators.ImageFinder(image_file = 'testWindowLogo.png', folder = './Tests/TestData/')
    result = ImFi.locate()
    print(result)
    assert result == (29, 1056), "Wrong windows logo location"
    print("Passed image finder test")

def test_image_displace():
    ImFi = Locators.ImageFinder(image_file = 'testWindowLogo.png', folder = './Tests/TestData/', displace_pixels = (5,5))
    result = ImFi.locate()
    print(result)
    assert result == [34, 1061], "Window location wronly displaced"
    print("Passed image finder displace location test")

def test_locator_factory():
    parameter = {'type': 'imageFinder',
                 'image_file': 'testWindowLogo.png',
                 'folder': './Tests/TestData',
                 'confidence': 0.8}
    ImFiLoca = Locators.create_locator(parameters = parameter)
    result = ImFiLoca.locate()
    print(result)
    assert result == (29, 1055), "Wrong windows logo location"
    print("Passed locator Factory test")

def test_locator_factory_from_imagefolder():
    parameter = {'type': 'imageFinder',
                 'image_file': 'image.png',
                 'folder': "./source/actions/images",
                 'confidence': 0.8}
    ImFiLoca = Locators.create_locator(parameters = parameter)
    result = ImFiLoca.locate()
    print(result)

def main():
    test_image_finder()
    test_image_displace()
    test_locator_factory()
    test_locator_factory_from_imagefolder()

if __name__ == "__main__":
    main()
