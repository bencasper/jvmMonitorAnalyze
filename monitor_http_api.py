import urllib
import time
import logging

__author__ = 'ben'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()
threshold = 50  # threshold is 50ms


class APIMonitor:
    def __init__(self):
        self.urls = ['http://www.google.com/','http://www.youtube.com/']

    # noinspection PyBroadException
    def do_monitor(self):
        for url in self.urls:
            try:
                nf = urllib.urlopen(url)
                start = time.time()
                page = nf.read()
                end = time.time()
                nf.close()
                # logger.info("content of api is %s",page)
                response_time = (end - start) * 1000
                logger.info('response time for api %s is %d ms,start at %f end at %f', url, response_time, start, end)
                if response_time > threshold:
                    # trigger the analyze sript and send email
                    pass
            except:
                urllib.ContentTooShortError
                # trigger the analyze script and send email


APIMonitor().do_monitor()




