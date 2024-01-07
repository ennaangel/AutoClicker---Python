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
    def __init__(self, Sleeper: iSleeper, duration_secs: int):
        """Initiate Sleeper action by passing a Sleeper and the sleep duration
        """
        self.Sleeper: iClicker = Sleeper
        self.duration_secs: int = duration_secs

    def do(self):
        """Sleep for duration_secs
        """
        self.Sleeper.sleep(self.duration_secs)

class MultiAction(iAction):
    def __init__(self, actions: tuple) -> None:
        self.actions = actions

    def do(self):
        for action in self.actions:
            action.do()