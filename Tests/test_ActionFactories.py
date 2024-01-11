import sys
import time
sys.path.append('./source')

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

def test_SleepFactory_minduration():
    duration = 4
    min_duration = 3
    params = {'action': 'sleepAction',
              'action_parameters': {
                  'parameters': {'type': 'randomSleeper'}, 
                  'duration': duration,
                  "min_duration_secs": min_duration}
              }
    Sleep = Factories.create_action(params)
    i = 0
    while i <= 5:
        start_time = time.time()
        Sleep.do()
        sleep_duration = time.time()-start_time
        print(f"Sleep: actual={sleep_duration}, given={duration}")
        assert sleep_duration <= duration, "Sleep was longer than requested"
        assert sleep_duration >= min_duration, "Sleep was shorter than requested"
        print("Past min duration sleeper factory test")
        i+=1

def test_premade_click_windows_logo():
    ClickLogo = Factories.create_action({'action': 'premadeAction',
                                         'action_parameters':{'name': 'TestClickWindowsLogo'}})
    ClickLogo.do()



def main():
    test_ClickerFactory()
    test_SleepFactory()
    test_SleepFactory_minduration()
    #test_premade_click_windows_logo()

if __name__ == "__main__":
    main()