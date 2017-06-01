import psutil
import datetime

class MetricsEntry:
    """A group of metrics for a given machine.
    
    Options for extending functionality:
        Recording metrics per CPU

    All metric calls using psutil should return dictionary objects for consistency.
    """
    def __init__(self):
        self.metrics = {'timestamp': str(datetime.datetime.utcnow()),
                        'cpu': self.get_cpu_metrics(),
                        'memory': self.get_memory_metrics(),
                        'disk': self.get_disk_metrics()}

    def get_cpu_metrics(self):
        """ psutil.cpu_percent() with no interval parameter compares since
        last call or module import but is non-blocking. First result will
        always be 0.0.
        """
        return {'cpu percent': psutil.cpu_percent()}

    def get_memory_metrics(self):
        virtual = psutil.virtual_memory()
        swap = psutil.swap_memory()
        return {'virtual': {'total': virtual.total,
                            'available': virtual.available},
                'swap': {'total': swap.total,
                         'used': swap.used,
                         'free': swap.free,
                         'percent': swap.percent}}

    def get_disk_metrics(self):
        """ psutil can see all disk partitions, so we make usage available
        per partition.
        """
        total_usage = {}
        for disk_part in psutil.disk_partitions():
            part_usage = psutil.disk_usage(disk_part.mountpoint)
            total_usage[disk_part.mountpoint] = {'total': part_usage.total,
                                                 'used': part_usage.used,
                                                 'free': part_usage.free,
                                                 'percent': part_usage.percent}
        return total_usage
