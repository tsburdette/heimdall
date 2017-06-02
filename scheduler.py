from apscheduler.schedulers.background import BackgroundScheduler
from metrics_log import MetricsLog

class Scheduler:

    def __init__(self):
        self.create_new_log()
        self.scheduler = BackgroundScheduler()
        print "* Adding new log job hourly."
        self.scheduler.add_job(self.create_new_log, 'interval', hours=1)
        print "* Adding record metrics minutely."
        self.scheduler.add_job(self.log.add_new_entry, 'interval', minutes=1)
        print "* Starting scheduler."
        self.scheduler.start()

    def create_new_log(self):
        print "* Creating log data."
        self.log = MetricsLog()
