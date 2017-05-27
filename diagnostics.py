import psutil
import json
import io
import datetime
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

class Diagnostics:
    """A group of metrics about a given machine"""
    diags = {'timestamp': str(datetime.datetime.utcnow()),
             'cpu': {},
             'memory': {},
             'disk': {}}
    def record_cpu_percent(self):
        self.diags['cpu']['percent'] = psutil.cpu_percent()
        with open('logs/cpu/percent.log', 'w') as cpu_per_log:
            cpu_per_log.write(self.diags['timestamp'] + ': ' + str(self.diags['cpu']['percent']) + '\n')
    def record_vm_usage(self):
        self.diags['memory']['virtual'] = psutil.virtual_memory()
        with open('logs/memory/virtual.log', 'w') as cpu_per_log:
            cpu_per_log.write(self.diags['timestamp'] + ': ' + str(self.diags['memory']['virtual']) + '\n')
    def record_swap_usage(self):
        self.diags['memory']['swap'] = psutil.swap_memory()
        with open('logs/memory/swap.log', 'w') as cpu_per_log:
            cpu_per_log.write(self.diags['timestamp'] + ': ' + str(self.diags['memory']['swap']) + '\n')
    def record_disk_usage(self):
        self.diags['disk']['usage'] = psutil.disk_usage('/')
        with open('logs/disk/usage.log', 'w') as cpu_per_log:
            cpu_per_log.write(self.diags['timestamp'] + ': ' + str(self.diags['disk']['usage']) + '\n')
    # some networking stuff here
    def record_all_metrics(self):
        self.record_cpu_percent()
        self.record_vm_usage()
        self.record_swap_usage()
        self.record_disk_usage()
        self.store_diags()
    def store_diags(self):
        """Stores immediate diagnostics via RESTful JSON"""
        with open('diags.json', 'w') as diags_json:
            formatted_diags = json.dumps(self.diags,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
            diags_json.write(to_unicode(formatted_diags))

if __name__ == '__main__':
    diags = Diagnostics()
    diags.record_all_metrics()
