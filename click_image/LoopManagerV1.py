import time

class LoopManager:
    def __init__(self, clicks_to_stop, loop_duration):
        self.clicks = 0
        self.start_time = self.set_cur_time()
        self.cur_click_time = self.set_cur_time()
        self.last_click_time = self.set_cur_time()
        self.clicks_to_stop = clicks_to_stop
        self.loop_duration = loop_duration

        print('Loop Manager initialised')
        print(f' - Start time: {time.ctime()}')
        print(f' - Loop duration: {loop_duration}')

    def set_cur_time(self):
        return time.time()
    
    def get_loop_time(self):
        self.cur_click_time = self.set_cur_time()
        self.loop_time = self.cur_click_time - self.last_click_time
        print(f" - Loop duration: {self.loop_time}")
        self.last_click_time = self.cur_click_time
        return self.loop_time

    def get_run_time(self):
        self.end_time = self.set_cur_time()
        self.run_time = self.end_time - self.start_time
        print(f'Run time: {self.run_time}')
        return self.run_time

    def add_clicks(self, n = 1):
        self.clicks += n
        
    def show_clicks_to_stop(self):
        print(f'Running for: {self.clicks_to_stop} clicks')
        
    def get_clicks_to_go(self):
        print(f'Clicks: {self.clicks}/{self.clicks_to_stop}')

    def sleep(self):
        time.sleep(self.loop_duration)

    def print_loop_info(self):
        self.get_clicks_to_go()
        self.get_loop_time()

    def update(self):
        self.add_clicks(n = 1)

    def loop_requirement(self):
        return self.clicks != self.clicks_to_stop
    
    def show_initiation_info(self):
        self.show_clicks_to_stop()
