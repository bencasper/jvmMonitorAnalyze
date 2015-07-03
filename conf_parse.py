import json
import logging
import os
from os.path import join

__author__ = 'ben'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()


def parse_conf():
    # read from file to get mail info
    conf_file = join(os.getcwd(), 'conf', 'monitor_configure.conf')
    logger.info('conf_file is %s', conf_file)
    with open(conf_file, 'r') as conf:
        conf_json = json.load(conf, 'utf-8')
        return conf_json


def mk_log_dir():
    log_path = '/letv/logs/monitor'
    log_file = 'jvmdump.log'
    if os.path.isdir(log_path):
        pass
    else:
        os.mkdir(log_path)