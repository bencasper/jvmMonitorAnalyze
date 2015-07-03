#!/usr/bin/python
import os

from email_send import EmailSend
from monitor_http_api import APIMonitor
from monitor_server_uptime import UptimeMonitor

__author__ = 'ben'

if __name__  == "__main__":
    pass
    APIMonitor().do_monitor()
    UptimeMonitor().do_monitor()
    EmailSend().write_email()

