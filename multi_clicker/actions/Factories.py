import random
import time
import json
from pathlib import Path

from actions.Interfaces import *

import actions.Clickers as Clickers
import actions.Sleepers as Sleepers
import actions.Actions as Actions

def create_action(parameters)-> iAction:
    factories = {'premadeAction': PremadeActionFactory(),
                     'clickAction': ClickActionFactory(),
                     'sleepAction': SleepActionFactory(),
                     'multiAction': MultiActionFactory()}
    Factory = factories[parameters['action']]
    return Factory.create_action(parameters['action_parameters'])


class ClickActionFactory(iActionFactory):
    def create_action(self, parameters: dict) -> Actions.ClickAction:
        """_summary_
        Args:       parameters (dict): {''}
        Returns:    ClickAction: An action that clicks using the clicker on the given position
        """
        Clicker = Clickers.create_clicker(parameters['parameters'])
        return Actions.ClickAction(Clicker = Clicker, position = parameters['position'])
    
class SleepActionFactory(iActionFactory):
    def create_action(self, parameters: dict) -> Actions.SleepAction:
        Sleeper = Sleepers.create_sleeper(parameters['parameters'])
        min_duration_secs = parameters.get('duration', 0) # Set min duration to 0 if not givrn
        return Actions.SleepAction(Sleeper = Sleeper, duration_secs = parameters['duration'], min_duration_secs = min_duration_secs)
    
class MultiActionFactory(iActionFactory):
    def create_action(self, parameters: dict) -> Actions.MultiAction:
        actions = [create_action(action) for action in parameters['actions']]
        return Actions.MultiAction(actions = actions)
    
class PremadeActionFactory(iActionFactory):
    def create_action(self, parameters: dict) -> iAction:
        name = parameters['name']
        path = Path(__file__).parent / f'./premade_actions/{name}.json'
        print(f"Using premade clicker: {name}")
        with open(path, 'r') as j:
            config = json.loads(j.read())
        return create_action(parameters = config)