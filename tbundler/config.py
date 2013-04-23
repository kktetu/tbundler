# -*- encoding: utf-8 -*-

import sys

# python25 compatibility
if sys.version_info >= (2, 7):
    from termcolor import colored
else:
    def colored(message, color):
        return message


EXEC_NAME = 'tbundler'

# color and warning messages
COLOR_WARNING = 'red'
COLOR_INFO = 'cyan'
COLOR_INST = 'blue'

WARNING_NOT_FOUND = colored('NOT FOUND', COLOR_WARNING)
WARNING_VERSION_CONFLICT = colored('VERSION CONFLICT', COLOR_WARNING)

SELFUPDATE_DISTNAME = 'tbundler'
SELFUPDATE_SOURCE = ''
#"""
#SELFUPDATE_SOURCE = 'git+git@server:tbundler.git'
#"""
