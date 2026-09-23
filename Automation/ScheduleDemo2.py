import schedule
import time
import datetime

def display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation script started")

    schedule.every(1).minute.do(display)
    # ISSUE

if __name__ == "__main__":
    main()