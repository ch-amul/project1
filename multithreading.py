# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:11:09 2018

@author: Cherukuri Amul

"""

'''******************************************************
python threading to sleep and awake a thread
******************************************************'''
#
#import time
#from threading import Thread
#
#def sleeper(i):
#    print ("\n thread %d sleeps for 5 seconds" % i)
#    time.sleep(1)
#    print ("\n thread %d woke up" % i)
#
#for i in range(5):
#    t = Thread(target=sleeper, args=(i,))
#    t.start()
#

'''******************************************************
#python threading to perform threading.active_count()
#******************************************************'''
#
#import time
#import threading
#from threading import Thread
#
#def sleepMe(i):
#    print("Thread %i going to sleep for 5 seconds." % i)
#    time.sleep(5)
#    print("Thread %i is awake now." % i)
#
#for i in range(5):
#    th = Thread(target=sleepMe, args=(i, ))
#    th.start()
#    print("\n Current Thread count: %i." % threading.active_count())


'''******************************************************
python threading to perform threading.current_thread()
******************************************************'''
'''This function returns the current thread in execution.
Using this method,we can perform particular actions
with the obtained thread.'''
#import time
#import threading
#from threading import Thread
# 
#def sleepMe(i):
#    print(i)
#    print(" \n Thread %s going to sleep for 5 seconds." % threading.current_thread())
#    time.sleep(5)
#    print("\n Thread %s is awake now.\n" % threading.current_thread())
#
##Creating only four threads for now
#for i in range(4):
#    th = Thread(target=sleepMe, args=(i, ))
#    th.start()

'''**************************************************
threading.timer
*************************************************'''
'''This function of threading module is used to create a new Thread and
letting it know that it should only start after a specified time.
Once it starts, it should call the specified function'''
import threading

def delayed():
    print("I am printed after 5 seconds!")

thread = threading.Timer(3, delayed)
thread.start()