import urllib
import time
import logging

from file_utils import parse_conf, mk_log_dir, get_log_file


__author__ = 'ben'
mk_log_dir()

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler(get_log_file())
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
threshold = 50  # threshold is 50ms


class APIMonitor:
    def __init__(self):
        self.urls = []
        conf_json = parse_conf()
        api_json = conf_json['api_list']
        for k,v in api_json.iteritems():
            logger.info('%s,%s',k,v)
            self.urls.append(v)

        # self.urls = ['http://www.google.com/','http://www.youtube.com/']

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
                    return True

            except:
                urllib.ContentTooShortError
                return True


if __name__ == "__main__":
    APIMonitor().do_monitor()




