import time

class TimeKeeper:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0

    def start(self):
        """Start the timer."""
        if self.start_time is not None:
            print("Timer is already running!")
            return
        self.start_time = time.time()
        print("Timer started!")

    def stop(self):
        """Stop the timer and calculate elapsed time."""
        if self.start_time is None:
            print("Timer has not started yet!")
            return
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Timer stopped! Elapsed time: {self.elapsed_time:.2f} seconds.")

    def reset(self):
        """Reset the timer."""
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0
        print("Timer reset!")

    def get_elapsed_time(self):
        """Get the elapsed time without stopping the timer."""
        if self.start_time is None:
            print("Timer has not started yet!")
            return 0
        current_time = time.time()
        return current_time - self.start_time


time_keeper = TimeKeeper()

time_keeper.start()

time.sleep(5)

# Stop the timer and get the elapsed time
time_keeper.stop()

# Reset the timer
time_keeper.reset()
