from inspect import getsourcefile
import json
import logging
import os
from os.path import join, split

__author__ = 'ben'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()


def parse_conf():
    sourcefile = getsourcefile(lambda:0)
    logger.info('source file is %s;',sourcefile)
    fd = split(sourcefile)[0]
    logger.info('source file path is %s;',fd)
    # read from file to get mail info
    conf_file = join(fd, 'conf', 'monitor_configure.conf')
    logger.info('conf_file is %s', conf_file)
    with open(conf_file, 'r') as conf:
        conf_json = json.load(conf, 'utf-8')
        return conf_json


def mk_log_dir():
    log_path = '/letv/logs/monitor'
    if os.path.isdir(log_path):
        pass
    else:
        os.mkdir(log_path)


def get_log_file():
    log_path = '/letv/logs/monitor'
    log_file = 'jvmdump'
    log_file_abs = "{0}/{1}.log".format(log_path, log_file)
    logger.info('abs of log file is %s',log_file_abs)
    return log_file_abs

if __name__ == "__main__":
    parse_conf()