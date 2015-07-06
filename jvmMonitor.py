#!/usr/bin/python
import os

from email_send import EmailSend
from exec_analyze_shell import exec_monitor_shell
from file_utils import get_log_file
from monitor_http_api import APIMonitor
from monitor_server_uptime import UptimeMonitor

__author__ = 'ben'

if __name__  == "__main__":
    os.system('truncate -s 0 ' + get_log_file())
    API_diagnosis = APIMonitor().do_monitor()
    Uptime_diagnosis = UptimeMonitor().do_monitor()
    if API_diagnosis or Uptime_diagnosis:
        exec_monitor_shell()
        EmailSend().write_email()

