#!/usr/bin/python
import os

from email_send import EmailSend
from monitor_http_api import APIMonitor
from monitor_server_uptime import UptimeMonitor

__author__ = 'ben'

if __name__  == "__main__":
    log_path = '/letv/logs/monitor'
    log_file = 'jvmdump.log'
    if os.path.isdir(log_path):
        pass
    else:
        os.mkdir(log_path)

    APIMonitor().do_monitor()
    UptimeMonitor().do_monitor()
    EmailSend().write_email()

