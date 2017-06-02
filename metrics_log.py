import datetime
import json
from metrics_entry import MetricsEntry

class MetricsLog:
    """ A group of metrics that can be recorded regularly. """
    def __init__(self):
        self.entries = {}
        print "* Creating log file."
        self.file_name = datetime.datetime.utcnow().strftime("%y-%m-%d-%H-00") + '.log'
        print "* File stored at " + str(self.file_name)
        self.add_new_entry()

    def add_new_entry(self):
        """ MetricsEntry should be serializable in order to facilitate encapsulation. """
        self.newest_entry = MetricsEntry()
        print "* New entry created at " + str(self.newest_entry.get_timestamp())
        self.entries[self.newest_entry.get_timestamp()] = self.newest_entry.metrics
        self.write_log()

    def write_log(self):
        with open('logs/' + self.file_name, 'w') as log_file:
            formatted_metrics = json.dumps(self.entries, sort_keys=True, indent=4)
            print "* Writing log file."
            log_file.write(formatted_metrics)
