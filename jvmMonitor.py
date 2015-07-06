#!/usr/bin/python
import logging
import os

from email_send import EmailSend
from exec_analyze_shell import exec_monitor_shell
from file_utils import get_log_file, mk_log_dir
from monitor_http_api import APIMonitor
from monitor_server_uptime import UptimeMonitor

__author__ = 'ben'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()

if __name__  == "__main__":
    mk_log_dir()
    os.system('truncate -s 0 ' + get_log_file())
    os.system('rm -rf /letv/logs/monitor/[0-9]*.log')  # delete old jstack dump file
    API_diagnosis = APIMonitor().do_monitor()
    Uptime_diagnosis = UptimeMonitor().do_monitor()
    if API_diagnosis or Uptime_diagnosis:
        logger.info('to start execute shell ...')
        exec_monitor_shell()
        logger.info('executing shell ended...')
        EmailSend().write_email()

