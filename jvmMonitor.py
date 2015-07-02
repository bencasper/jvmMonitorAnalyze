from email_send import EmailSend
from monitor_http_api import APIMonitor
from monitor_server_uptime import UptimeMonitor

__author__ = 'ben'

APIMonitor().do_monitor()
UptimeMonitor().do_monitor()
EmailSend.write_email()
