import sys

sys.path.append("./source")
from actions import Clickers

def test_factory():
    params = {'type': 'baseClicker'}
    Clickers.create_clicker(params)
    params = {'type': 'randomClicker',
              'pixel_deviation': 6,
              'second_deviation': 7}
    Clickers.create_clicker(params)
    params = {'type': 'premadeClicker',
              'name': 'QuickRandomClick'}
    Clickers.create_clicker(params)
    return 

def main():
    test_factory()

if __name__ == "__main__":
    main()