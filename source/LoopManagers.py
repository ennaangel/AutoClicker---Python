import time

class iLoopManager:
    def show_initiation_info(self):
        pass
    def sleep(self):
        pass
    def print_loop_info(self):
        pass
    def update(self):
        pass
    def get_run_time(self):
        pass
    def loop_requirement(self):
        pass

class ClickLoopManager(iLoopManager):
    def __init__(self, clicks_to_stop, loop_duration = 0):
        self.clicks = 0
        self.start_time = self.get_cur_time()
        self.cur_click_time = self.get_cur_time()
        self.last_click_time = self.get_cur_time()
        self.clicks_to_stop = clicks_to_stop
        self.loop_duration = loop_duration

        print('Loop Manager initialised')
        print(f' - Start time: {time.ctime()}')
        print(f' - Loop duration: {loop_duration}')

    def sleep(self):
        time.sleep(self.loop_duration)

    def print_loop_info(self):
        """Show loop info"""
        self._get_clicks_to_go()
        self.get_loop_time()

    def update(self):
        """Updates loop info, adding a click to click counter and updating loop time"""
        self._add_clicks(n = 1)
        self.update_loop_time()

    def _add_clicks(self, n = 1):
        """Add n clicks to click counter"""
        self.clicks += n

    def update_loop_time(self):
        self.last_click_time = self.cur_click_time
        self.cur_click_time = self.get_cur_time()

    def loop_requirement(self):
        """Keep looping if the number of clicks is lower than clicks to stop"""
        return self.clicks < self.clicks_to_stop
    
    def show_initiation_info(self):
        self._show_clicks_to_stop()

    def get_cur_time(self):
        return time.time()
    
    def get_loop_time(self):
        """Prints and returns the duration of current loop"""
        loop_time = self.get_cur_time() - self.cur_click_time
        print(f" - Current loop duration: {loop_time}")
        return loop_time

    def get_run_time(self):
        self.end_time = self.get_cur_time()
        run_time = self.end_time - self.start_time
        print(f'Run time: {run_time}')
        return run_time
        
    def _show_clicks_to_stop(self):
        print(f'Running for: {self.clicks_to_stop} clicks')
        
    def _get_clicks_to_go(self):
        print(f'Clicks: {self.clicks}/{self.clicks_to_stop}')


