import sys
sys.path.append('./multi_clicker')

from actions import Factories

def test_ClickerFactory():
    params = {'action': 'clickAction',
              'action_parameters': {'parameters': {
                  'type': 'premadeClicker',
                  'name': 'QuickRandomClick'
                  },
                  'position': (100,100)}
    }
    Factories.create_action(params)

def test_SleepFactory():
    params = {'action': 'sleepAction',
              'action_parameters': {
                  'parameters': {'type': 'randomRandomSleeper', 'chance': 20}, 
                  'duration': 2}
              }
    Factories.create_action(params)

def test_premade_click_windows_logo():
    ClickLogo = Factories.create_action({'action': 'premadeAction',
                                         'action_parameters':{'name': 'TestClickWindowsLogo'}})
    ClickLogo.do()


def main():
    test_ClickerFactory()
    test_SleepFactory()
    test_premade_click_windows_logo()

if __name__ == "__main__":
    main()