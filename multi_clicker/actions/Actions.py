from actions.Interfaces import *

class ClickAction(iAction):
    def __init__(self, Clicker: iClicker, position: tuple):
        """Initiate Clicker action, will click on given position using the given clicker
            Clicker (iClicker): Clicker type to perform clicks
            position (Tuple): (x,y) coordinates of click
        """
        self.Clicker: iClicker = Clicker
        self.position: tuple = position

    def do(self):
        """Click on position
        """
        self.Clicker.click(self.position)

class SleepAction(iAction):
    def __init__(self, Sleeper: iSleeper, duration_secs: int, min_duration_secs: int = 0):
        """Initiate Sleeper action by passing a Sleeper and the sleep duration
        """
        self.Sleeper: iClicker = Sleeper
        self.duration_secs: int = duration_secs
        self.min_duration_secs: int = min_duration_secs

    def do(self):
        """Sleep for duration_secs
        """
        self.Sleeper.sleep(self.duration_secs, self.min_duration_secs)

class MultiAction(iAction):
    def __init__(self, actions: tuple) -> None:
        self.actions = actions

    def do(self):
        for action in self.actions:
            action.do()

class LocatorClickerAction(iClicker):
    def __init__(self, Locator: iLocator, Clicker: iClicker, SleeperAction: SleepAction = None) -> None:
        """Finds location using locator and clicks on it. If no location, returns nothing"""
        self.Clicker = Clicker
        self.Locator = Locator
        self.SleeperAction = SleeperAction

    def do(self):
        location = self.Locator.locate()
        if location == None:
            return
        if self.SleeperAction != None:
            self.SleeperAction.do()
        self.Clicker.click(location)

class WaitTillLocationAndClickAction(iClicker):
    def __init__(self, Locator: iLocator, Clicker: iClicker, WaitSleeperAction: SleepAction = None, IterationSleeperAction: SleepAction = None) -> None:
        """Waits till location returns a location and clicks it. """
        self.Clicker = Clicker
        self.Locator = Locator
        self.WaitSleeperAction = WaitSleeperAction
        self.IterationSleeperAction = IterationSleeperAction

    def do(self):
        location = None 
        while location = None:
            if self.IterationSleeperAction != None:
                self.IterationSleeperAction.do()
            location = self.Locator.locate()
        if self.WaitSleeperAction != None:
            self.WaitSleeperAction.do()
        self.Clicker.click(location)