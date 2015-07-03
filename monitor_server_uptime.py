import os
from subprocess import Popen, PIPE
from re import split

__author__ = 'ben'
uploadThreshold = 10  # set linux upload threshold to 10


class UptimeMonitor:
    def __init__(self):
        self.command = 'uptime'

    def do_monitor(self):
        sub_proc = Popen([self.command], shell=False, stdout=PIPE)
        line = sub_proc.stdout.readline()
        # The separator for splitting is 'variable number of spaces'
        print line
        proc_info = split("load averages:", line)
        uptime = proc_info[1]
        nearly_uptime = split(" ", uptime)[1]
        print nearly_uptime
        if nearly_uptime > uploadThreshold:
            """ do analyze """
            os.system('shell/findhighestcpucomsumethread.sh')
            os.system('shell/findhighestcpucomsumethread.sh')


UptimeMonitor().do_monitor()

