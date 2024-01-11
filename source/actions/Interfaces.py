class iClicker:
    def click(self,position: tuple):
        pass

class iSleeper:
    def sleep(self, duration_secs: int):
        pass

class iAction:
    def do(self):
        """Performs action"""
        pass

class iActionFactory:
    def create_action(self, parameters: dict)-> iAction:
        pass

class iLocator:
    def locate(self):
        pass