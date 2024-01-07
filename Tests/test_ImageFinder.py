import sys

sys.path.append('')
import ImageFinder

def get_image_location():
    print(ImageFinder.get_image_centre('./Tests/TestData/testVsCLogo.png'))
    return

def main():
    get_image_location()

if __name__ == '__main__':
    main()