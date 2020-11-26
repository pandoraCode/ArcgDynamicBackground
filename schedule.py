from apscheduler.schedulers.blocking import BlockingScheduler
from fetchbg import bg

def run():
   bg()

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', hours=4)
scheduler.start()