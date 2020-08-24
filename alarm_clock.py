import pygame
from threading import Thread
import datetime
from termcolor import colored

def set_alarm(snooze = False):
    
    """
        INPUT : Takes the user input for the timestamp to set the alarm and an internal snooze switcher
        
        OUTPUT : Sets the alarm and play beeps when the time is up! An additional snooze option is provided
        
        FUTURE UPGRADES : Can set different Alarm Tones
    
    """
    
    from pygame import mixer
    
    global snooze_time
    
    if not snooze:        
        
        days = int(input("Enter how many days later to set the alarm : "))
        hours = int(input("Enter how many hours later to set the alarm : "))
        minutes = int(input("Enter how many minutes later to set the alarm : "))
        #seconds = 0
        seconds = int(input("Enter how many seconds later to set the alarm : "))
        
        snooze_time = 10
        ch = input("\nSnooze time has been set to 10 minutes. Do you wish to change it (Y/N)? ")
        if ch in ['Y','y','N','n']:
            while True:
                if ch == 'Y' or ch == 'y':
                    snooze_time = input("Enter snooze time in minutes : ")
                    try :
                        snooze_time = abs(int(snooze_time))
                        break
                    except Exception:
                        print(f"Snooze time should be a natural number, not {snooze_time}")
                        continue
                break
        else:
            raise ValueError(f"\nChoice type should be either Y or N, not {ch}")
        
        alarm_time = datetime.datetime.now() + datetime.timedelta(days, seconds, hours = hours, minutes = minutes)    
        
        ones = []
        suffixes = ['days','hours','minutes','seconds']
        for i,el in enumerate([days,hours,minutes,seconds]):
            if el == 1:
                suffixes[i] = suffixes[i][:-1]
        
        if days:
            print(f"\n"+colored(f"Alarm set for {days} {suffixes[0]}, {hours} {suffixes[1]},{minutes} {suffixes[2]}, {seconds} {suffixes[3]} from now!",'green'))
        elif hours:
            print(f"\n"+colored(f"Alarm set for {hours} {suffixes[1]},{minutes} {suffixes[2]}, {seconds} {suffixes[3]} from now!","green"))
        elif minutes:
            print(f"\n"+colored(f"Alarm set for {minutes} {suffixes[2]}, {seconds} {suffixes[3]} from now!","green"))
        elif seconds:
            print(f"\n"+colored(f"Alarm set for {seconds} {suffixes[3]} from now!",'green'))
        else:
            raise AssertionError(colored("Alarm NOT Set!",'red'))
        
    elif snooze:
        mixer.music.stop()
        if snooze_time == 1:
            print(f"\n"+colored(f"Alarm Snoozed for {snooze_time} minute!",'green'))
        else:
            print(f"\n"+colored(f"Alarm Snoozed for {snooze_time} minutes!",'green'))
        alarm_time = datetime.datetime.now() + datetime.timedelta(minutes = snooze_time)
    else:
        raise AssertionError("The code never reaches here normally!")
    
    class ThreadWithReturnValue(Thread):
        def __init__(self, group=None, target=None, name=None,
                     args=(), kwargs={}, Verbose=None):
            Thread.__init__(self, group, target, name, args, kwargs)
            self._return = None
        def run(self):
            if self._target is not None:
                self._return = self._target(*self._args,
                                                    **self._kwargs)
        def join(self, *args):
            Thread.join(self, *args)
            return self._return
    
    def play_music():
            print(colored("\nTime to wake up sleepyhead!\n",'red'))
            mixer.init()
            mixer.music.load('/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga')
            mixer.music.play(loops=-1)
    
    def stop_or_snooze():
        ch = input("Please enter S to stop and P to snooze : ")
        if ch == 'S':
            return False
        elif ch == 'P' : 
            return True
        else:
            print(f"ch should be either S or P, not {ch}")
            while True: 
                ret = stop_or_snooze()
                if ret is not None:
                    break
    
    flag = False
    
    while True:
        if(alarm_time-datetime.datetime.now()) == datetime.timedelta(0):
            t1 = ThreadWithReturnValue(target=play_music)
            t2 = ThreadWithReturnValue(target=stop_or_snooze) 

            t1.start()
            t2.start()
        
            snooze = t2.join()
            t1.join()
            
            if snooze:
                set_alarm(snooze = True)
                break
            else:
                mixer.music.stop()
                flag = True
        
        elif flag: break
        else: continue 

if __name__ == "__main__":
    set_alarm()