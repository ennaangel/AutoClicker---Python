import sys
sys.path.append('./multi_clicker')


from actions import Actions
from actions.Interfaces import iClicker, iSleeper

class TestSleeper(iSleeper):
    def sleep(self, duration_secs):
        print(f'Sleeping for {duration_secs}')

class TestClicker(iClicker):
    def click(self, position):
        print(f"Click at position: {position}")

def test_multi_action():
    MultiAction = Actions.MultiAction(
        [Actions.SleepAction(TestSleeper(), 5),
         Actions.ClickAction(TestClicker(), (1,2))]
    )
    MultiAction.do()


def main():
    test_multi_action()

if __name__ == "__main__":
    main()