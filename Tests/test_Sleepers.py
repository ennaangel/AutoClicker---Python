import sys
import time

sys.path.append('source')
sys.path.append('')

from actions import Sleepers as Sleepers

def test_random_sleep():
    i = 0
    while i < 5:
        duration = 5
        min_duration = 2
        start_time = time.time()
        Sleepers.RandomSleeper().sleep(duration_secs = duration, min_duration_secs = min_duration)
        sleep_duration = time.time()-start_time
        print(f"Sleep: actual={sleep_duration}, given={duration}")
        assert sleep_duration <= duration, "Sleep was longer than requested"
        assert min_duration <= duration, "Sleep was shorter than requested"
        i += 1

def test_random_random_sleep():
    i = 0
    while i < 30:
        duration = 1
        start_time = time.time()
        Sleepers.RandomRandomSleeper(chance = 5).sleep(duration_secs = duration)
        sleep_duration = time.time()-start_time
        print(f"Sleep: actual={sleep_duration}, given={duration}")
        i += 1

def test_sleep_factory():
    params = {'type': 'randomRandomSleeper',
              'chance': 20}
    Sleepers.create_sleeper(params)

def main():
    test_random_sleep()
    test_random_random_sleep()
    test_sleep_factory()
    
if __name__ == "__main__":
    main()