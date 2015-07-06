import logging
from subprocess import Popen, PIPE
from re import split

from file_utils import mk_log_dir, get_log_file


__author__ = 'ben'
uploadThreshold = 30  # set linux upload threshold to 30
mk_log_dir()
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler(get_log_file())
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
        nearly_uptime = float(split(",", uptime)[0])
        logger.debug('nearly_uptime is %f',nearly_uptime)
        # print nearly_uptime
        if nearly_uptime > uploadThreshold:
            return True


if __name__ == "__main__":
    UptimeMonitor().do_monitor()

