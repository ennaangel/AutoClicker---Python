import sys
sys.path.append('')

import source.LoopManagers as LoopManagers

def test_click_manager():
    LM = LoopManagers.ClickLoopManager(
        clicks_to_stop = 2
    )
    assert LM.loop_requirement() == True, "Failed loop requirement test"
    LM.update()
    LM.update()
    LM.print_loop_info()
    assert LM.loop_requirement() == False, "Failed loop requirement test"
    print("Succeded loop requirement test")

def test_show_loop_info():
    LM = LoopManagers.ClickLoopManager(
        clicks_to_stop = 5, loop_duration = 5)
    LM.print_loop_info()
    LM.sleep()
    LM.update()
    LM.print_loop_info()
    LM.update()
    LM.print_loop_info()
    

def main():
    test_click_manager()
    test_show_loop_info()

if __name__ == "__main__":
    main()