import sys, os
import threading

def create_thread(function):
   thread = threading.Thread(target=function)
   return thread.start()
