"""
Threading Module is used for Making Threads.
"""

import threading
import time


# Topic: Threading
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name + "\n")


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" % (threadName, time.ctime(time.time()), counter) + "\n")
        counter -= 1


# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1.5)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")


# Topic: Working with Different Threads (Payment,Email,Loading page)
class myThread(threading.Thread):
    def __init__(self, threadid, name, count34):
        threading.Thread.__init__(self)
        self.threadId = threadid
        self.name = name
        self.count = count34

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        print_timing(self.name, 1, self.count)
        threadLock.release()
        print("Exiting: " + self.name + "\n")


class myThread2(threading.Thread):
    def __init__(self, threadids, name, count45):
        threading.Thread.__init__(self)
        self.threadId = threadids
        self.name = name
        self.count = count45

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        threadLock.release()
        print_timing(self.name, 1, self.count)
        print("Exiting: " + self.name + "\n")


def print_timing(name, delay, counting):
    while counting:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), counting) + "\n")
        counting -= 1


threadLock = threading.Lock()
thread1 = myThread(1, "Payment", 5)
thread2 = myThread2(2, "Sending Email", 10)
thread3 = myThread2(3, "Loading Page", 3)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("Done main thread")


# Topic: Locking and Synchronizing 1 Thread
class myThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()
        print("Exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


threadLock = threading.Lock()

thread1 = myThread(1, "Thread 1", 5)
thread2 = myThread(2, "Thread 2", 5)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Done main thread")


# Topic: Locking and Synchronizing 2 Threads (Payment,Email,Loading page)
class myThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()
        print("Exiting: " + self.name + "\n")


class myThread2(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1, self.count)
        print("Exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


threadLock = threading.Lock()

thread1 = myThread(1, "Payment", 5)
thread2 = myThread2(2, "Sending Email", 10)
thread3 = myThread2(3, "Loading Page", 3)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("Done main thread")
