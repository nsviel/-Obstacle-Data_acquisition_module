#---------------------------------------------
from src.utils import terminal

import threading
import time


class Daemon:
    def start_daemon(self):
        self.run_thread = True
        self.thread = threading.Thread(target = self.thread_loop)
        self.thread.start()
        terminal.addDaemon("#", "ON", self.name)

    def stop_daemon(self):
        self.run_thread = False
        terminal.addDaemon("#", "OFF", self.name)

    def restart_daemon(self):
        terminal.addDaemon("#", "restart", self.name)
        self.run_thread = False
        time.sleep(1)
        self.run_thread = True
        self.thread.join()
        self.thread = threading.Thread(target = self.thread_loop)
        self.thread.start()

    def thread_loop(self):
        self.thread_init()
        while self.run_thread:
            self.thread_function()
            time.sleep(self.run_sleep)
        self.thread_end()

    def thread_init(self):
        pass

    def thread_function(self):
        pass

    def thread_end(self):
        pass

    thread = None
    run_thread = False;
    run_sleep = 1;
    name = "default";
