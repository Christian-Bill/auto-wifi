import os
import time
import schedule
import urllib.request
from pynotifier import Notification


def check_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def on_off_connection():
    if check_connection():
        os.system("nmcli radio wifi off")
    else:
        os.system("nmcli radio wifi on")

def notify():
    Notification(
        title='title',                          # Title of the Notification Tray
        description='Wifi Connection Disabled', # Description of the Notification Tray
        icon_path='path/assets/sleep.ico',      # Icon path
        duration=5,                                 
        urgency='normal'
    ).send()
    on_off_connection()

def job():
    notify()


if __name__ == "__main__":

    os.system("nmcli radio wifi on")
    schedule.every().day.at("00:00").do(job) # 24 Hour time format

    while True:
        schedule.run_pending()
        time.sleep(1)

