import os
import time
import random
import sys

sys.path.append('')
import source.LoopManagers as LoopManagers
from actions import Factories

clicks_to_stop = 1200
time_interval_seconds = 0.3

LM = LoopManagers.ClickLoopManager(clicks_to_stop = clicks_to_stop, 
                                   loop_duration = time_interval_seconds)

Action = Factories.create_action(parameters = {'action':'premadeAction',
                                     'action_parameters':{'name': 'PostOffice'}})

def main():
    LM.show_initiation_info()
    while LM.loop_requirement():
        LM.sleep()
        Action.do()
        LM.print_loop_info()
        LM.update()
        
    LM.get_run_time()
    
if __name__ == "__main__":
    main()