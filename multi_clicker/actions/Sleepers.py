import time
import random

from actions.Interfaces import iSleeper

class Sleeper(iSleeper):
    def sleep(self, duration_secs: int):
        time.sleep(duration_secs)

class RandomSleeper(iSleeper):
    def sleep(self, duration_secs: int):
        """Sleeps for a random duration between 0 and duration secs"""
        time.sleep(duration_secs*random.random())

class RandomRandomSleeper(iSleeper):
    def __init__(self, chance: int) -> None:
        self.chance = chance
        print(f"Initiated random random sleeper with chance 1/{chance}")

    def sleep(self, duration_secs: int):
        """Sleeps for a random interval between 0 and time seconds at random moments
        with 1/chance chance"""
        if random.randint(0, self.chance) == 0:
            sleep_time_sec = duration_secs*random.random()
            time.sleep(sleep_time_sec)

def create_sleeper(parameters) -> iSleeper:
    factories = {'baseSleeper': BaseSleeperFactory(),
                'randomSleeper': RandomSleeperFactory(),
                'randomRandomSleeper': RandomRandomSleeperFactory()}
    Factory = factories[parameters['type']]
    return Factory.create_sleeper(parameters)
    
class iSleeperFactory():
    def create_sleeper(self, parameters)-> iSleeper:
        pass
    
class BaseSleeperFactory(iSleeperFactory):
    def create_sleeper(self, parameters) -> Sleeper:
        return Sleeper()

class RandomSleeperFactory(iSleeperFactory):
    def create_sleeper(self, parameters) -> Sleeper:
        return RandomSleeper()
    
class RandomRandomSleeperFactory(iSleeperFactory):
    def create_sleeper(self, parameters) -> Sleeper:
        return RandomRandomSleeper(chance = parameters['chance'])
