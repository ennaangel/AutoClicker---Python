    sys.path.append('./multi_clicker')


    from actions import Locators

    def test_image_finder():
        ImFi = Locators.ImageFinder(image_file = 'testVsCLogo.png', folder = './Tests/TestData/')
        print(ImFi.locate())

    def main():
        test_image_finder()


    if __name__ == "__main__":
        main()
