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
    def __init__(self, Sleeper: iSleeper, duration_secs: int, min_duration_sec: int = 0):
        """Initiate Sleeper action by passing a Sleeper and the sleep duration
        """
        self.Sleeper: iClicker = Sleeper
        self.duration_secs: int = duration_secs
        self.min_duration_sec: int = min_duration_sec

    def do(self):
        """Sleep for duration_secs
        """
        self.Sleeper.sleep(self.duration_secs, self.min_duration_sec)

class MultiAction(iAction):
    def __init__(self, actions: tuple) -> None:
        self.actions = actions

    def do(self):
        for action in self.actions:
            action.do()

class LocatorClickerAction(iClicker):
    def __init__(self, Locator: iLocator, Clicker: iClicker, SleeperAction: SleepAction = None) -> None:
        self.Clicker = Clicker
        self.Locator = Locator
        self.SleeperAction = SleeperAction
        self.delay_secs = delay_secs
        self.min_duration_secs

    def do(self):
        location = self.Locator.locate()
        if self.Sl != None:
            self.SleeperAction.do()
        self.Clicker.click(location)