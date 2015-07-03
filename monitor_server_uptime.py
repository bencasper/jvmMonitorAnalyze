import logging
import os
from subprocess import Popen, PIPE
from re import split

__author__ = 'ben'
uploadThreshold = 10  # set linux upload threshold to 10
logPath = '/letv/logs/monitor'
fileName = 'jvmdump'
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler) #a bug?


class UptimeMonitor:
    def __init__(self):
        self.command = 'uptime'

    def do_monitor(self):
        sub_proc = Popen([self.command], shell=False, stdout=PIPE)
        line = sub_proc.stdout.readline()
        # The separator for splitting is 'variable number of spaces'
        logger.info('uptime is :\n %s',line)
        # average on linux  and averages on osx
        proc_info = split("load average:", line)
        uptime = proc_info[1]
        # commas on linux and blank on osx
        nearly_uptime = split(",", uptime)[1]
        # print nearly_uptime
        if nearly_uptime > uploadThreshold:
            """ do analyze """
            os.system('shell/findhighestcpucomsumethread.sh')
            os.system('shell/findhighestramcomsumethread.sh')


UptimeMonitor().do_monitor()

