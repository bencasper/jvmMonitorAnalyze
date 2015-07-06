import os

__author__ = 'ben'


def exec_monitor_shell():
    """ do analyze """
    os.system('shell/findhighestcpucomsumethread.sh')
    os.system('shell/findhighestramcomsumethread.sh')
