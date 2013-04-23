# -*- coding: utf-8 -*-

import sys

from tbundler.config import colored, EXEC_NAME, COLOR_WARNING
from tbundler.bundler import Bundler


def usage():
    print """
　　　　　　　　　　　　　　　　　______,,,,,,,,,,,,,,,,______
　　　　　　　　　　　　　    ,,::::::::::::::::::::::::::::::::ﾞ,,
　　　　　　　　　　　　　..::::::::::ﾞﾞﾞﾞﾞ ､-‐‐-､::::::-‐‐-､ﾞﾞﾞﾞ:::,,
　　　　　　　　　　　 .::"::::::::/　　　  ヽ /　　　 ヽ::::::::::":::,
　　　　　　　　　　 .::"::::::::::l　　　　     　　　　l::::::::::::":,,
　　　　　　　　　／.::::::::::::;;l　　　　 ●|●　　　　 l;;;;::::::::::::＼
　　　　　　　　／::::::::::: ''" 　ヽ.　 ,.---‐-､　　ノ　　"'' :::::::::::＼
　　　　　　　/::::::::／　 ｰ-､,,,_　 ￣´l::::::::::l￣ 　_,,,､-‐　＼:::::::ヽ
　　　　　　 i':::,､-‐-､.　　　　 ｀'''‐-　`‐-‐'　-‐'''´　　　　      -‐-､::::
　　　　 　 i':::/　　　　 　──-----　　       |　　       -----── 　     ヽ::.
　　　　　 i'::::{. 　 　 　 -----‐‐‐‐‐　      │　     ‐‐‐‐‐-----　　　    }:::
　　　　　.|:::i ヽ.,　　　　　　  _____,,,,,,,|,,,,,,,_____　　　　　    ノ:::
　　　　　.|:::|　　 ｀'t‐----‐'''''´　　　　　　　　　｀'''''‐---‐t''´´´ |::::
　　　　　 i:::i　　　　/ 　　　　　　　　　　　　　　　　　　　　　|　　　i::'
　　　　　 .'i::i　　　i 　　　　　　　　　　　　　　　　　　　　 .:　　　 i:'
　　, -‐‐- ､::i,　　　 ヽ. 　　　　　 　　　　　　　　　　　　　/　　　/::i:'
　/　　　　　ヽi,　　　　ヽ　　　／ﾞﾞﾞﾞﾞﾞﾞ"'‐--‐'"ﾞﾞﾞﾞﾞ＼　　／ 　　 /:i':
　{　　　　　　} ヽ　　　　 ＼ /　　　　　　　　　　　　 i／ 　　　./'´   |Package Control|
　ヽ 　　　　ノ:::::＼　　　　 `''‐-､,,,,,,,,,_______,,,,,,,､-‐'´　　 ＼  |===============|
　　｀''''''''"::::::::::::＼,,,,__　 　　　　　　　　　　　　　__,,,,＼....../`````````}
　　　　 　 ＼::::::::::::::/;,,,,,,,,''''''''''''ゝ‐-､''''''''''',,,,,,,,,,,,ヽ､_____ノ
　　　　　　　　 ､'''ﾞﾞ￣￣ﾞﾞヽ／　　　`ｰﾞ‐"　　　 ＼::::::::::|::::::::::.
　　　　　　　 /　　　　　　　 ヽ　　　　　　　　　　　 ヽ:::::::|‐‐--ヽ
　　　　　　　/　　　　　　　　　|─--､､､,,,,,______　　 |:::::::|
　　　　　　　| 　　　　　　　　　|　　　　　　　　　|　　 }:::::::l
　　　　　 　 |　　　　　　　　　 |　　　　　　　　 /　　./:::::/
　　　　　　　ヽ. 　　　　　　　 /ヽ､,,,________,,／　 ／:::::/
　　　　　　　　＼ 　　　　　／ｰ---------‐‐''´:::::::/:::|
　　　　　　　　　 ｀'ー--‐''ﾞ　　　　　｀ﾞヽ::::::::::::::::::::/
　　　　　　　　　　　　　　　　　　　　　／ヽ;;＿＿;;／､:::::::ヽ....
　　　　　　　 　 :::::::::::::::::::::::::::::::::::{, 　　　　　　  }
　　　　　　 ::::::::::::::::::::::::::::::::::::::::::::`ー-------‐""

                            Time Wasting Dependency Resolver
"""
    print "Usage: %s subcmd [file]" % EXEC_NAME
    print "       %s help" % EXEC_NAME
    print """
subcmd:

   show:                   Show dependencies
   help:                   Display this message
   install:                Resolve dependencies automatically
   upgrade [all|package]:  Force upgrade package or dependency
   exec [file]:            Execute file
   selfupdate:             Update tbundler
"""
    exit(0)


def run():
    """
    console_scripts
    """
    if not len(sys.argv) > 1:
        option = 'help'
    else:
        option = sys.argv[1]

    if option in ['help', '-h', '--help']:
        usage()

    elif option == 'show':
        Bundler.load()
        Bundler.show()
    elif option == 'install':
        Bundler.load()
        Bundler.install()
    elif option == 'upgrade':
        if len(sys.argv) > 2:
            filter = None if sys.argv[2] == 'all' else sys.argv[2]
        else:
            filter = None
        Bundler.load()
        Bundler.upgrade(filter=filter)
    elif option == 'selfupdate':
        Bundler.selfupdate()
    elif option == 'exec':
        if 3 > len(sys.argv):
            print colored('file is not given', COLOR_WARNING)
            exit(1)
        Bundler.load()
        Bundler.execute(sys.argv[2])
    else:
        usage()
