"""
Here is the main simulation.

1. Create a queue of print tasks. Each task will be
given a timestamp upon its arrival. The queue is
empty to start.
2. For each second (currentSecond):
    a.  Does a new print task get created? If so,
    add it to the queue with the currentSecond as
    the timestamp.
    b.  If the printer is not busy and if a task
    is waiting,
        i.  Remove the next task from the print queue
        and assign it to the printer.
        ii. Subtract the timestamp from the currentSecond
        to compute the waiting time for that task.
        iii.Append the waiting time for that task to a
        list for later processing.
        iv. Based on the number of pages in the print
        task, figure out how much time will be required.
    c.  The printer now does one second of printing if
    necessary. It also subtracts one second from the
    time required for that task.
    d.  If the task has been completed, in other words
    the time required has reached zero, the printer
    is no longer busy.
3. After the simulation is complete, compute the average
waiting time from the list of waiting times generated.
"""
import random


class Queue():

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def enqueue(self, items):
        self.items.insert(0, items)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


class Printer:

    def __init__(self, ppm):
        self.ppm = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def is_busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.ppm


class Task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, ppm):
    printer = Printer(ppm)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            # If there is new print task, create one
            task = Task(current_second)
            # And enqueue it
            print_queue.enqueue(task)

        if (not printer.is_busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remianing."\
          % (average_wait, len(print_queue)))


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)

"""
Reference:
https://runestone.academy/runestone/books/published/pythonds/BasicDS/SimulationPrintingTasks.html
"""
