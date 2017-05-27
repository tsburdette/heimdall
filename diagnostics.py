import psutil
import json
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

class Diagnostics:
    """A group of metrics about a given machine"""
    diags = {'cpu': {},
            'memory': {},
            'disk': {}}
    def record_cpu_percent(self):
        self.diags['cpu']['percent'] = psutil.cpu_percent()
    def record_vm_usage(self):
        self.diags['memory']['virtual'] = psutil.virtual_memory()
    def record_swap_usage(self):
        self.diags['memory']['swap'] = psutil.swap_memory()
    def record_disk_usage(self):
        self.diags['disk']['usage'] = psutil.disk_usage('/')
    # some networking stuff here
    def record_all_metrics(self):
        self.record_cpu_percent()
        self.record_vm_usage()
        self.record_swap_usage()
        self.record_disk_usage()
        self.store_diags()
    def store_diags(self):
        with open('diags.json', 'w') as diags_json:
            formatted_diags = json.dumps(self.diags,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
            diags_json.write(to_unicode(formatted_diags))
