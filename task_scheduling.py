#schedule a task

import time
import schedule

def job():
    print("this is a scheduled task")
    
schedule.every().day.at("12:18").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



