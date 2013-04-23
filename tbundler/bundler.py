# -*- coding: utf-8 -*-

import os
import pip

from pkg_resources import get_distribution
from pkg_resources import VersionConflict, DistributionNotFound

from tbundler.config import colored, COLOR_WARNING, COLOR_INFO, COLOR_INST, WARNING_NOT_FOUND, WARNING_VERSION_CONFLICT, SELFUPDATE_SOURCE, SELFUPDATE_DISTNAME


def pkg(distname, version=None, source=None):
    """
    Specify package info

    Example:
        import tbundler

        pkg('django', '==1.4')
        pkg('PyYAML', '>=3.10')

        So then, tbundler check the packages are resolved with version string
    """
    Bundler.resolve(distname, version, source)


def inspect(pyfile):
    """
    Inspection

    Use with your own script:
        import tbundler
        tbundler.inspect('path/to/pyfile')

        # your code here

    The script may be terminated if dependencies are not resolved
    """
    Bundler.load(pyfile)
    execfile(pyfile)
    if Bundler.terminate:
        print colored("""
Your programm is terminated
Before run the program, make sure resolve all the dependencies on $PYTHONPATH
""", COLOR_WARNING)
        exit(1)


class Bundler():
    """
    =======
    Bundler
    =======

    Dependency resolver
    """

    LOCK_FILE = "PyFile"
    INSTALL_OPT = "-q"
    INSTALL_GIT = "-e"

    dependencies = {}
    unresolved = {}
    terminate = False

    @classmethod
    def show(cls):
        """
        Display resolved packages
        """
        if len(cls.dependencies.keys()) > 0:
            print "\nResolved:"

        for distname in cls.dependencies.keys():
            version = cls.dependencies[distname][0] or 'any'
            print "  %s(%s)" % (distname, version)

        print "%s %s" % (colored(len(cls.dependencies), COLOR_INFO), colored('package(s)', COLOR_INFO))

    @classmethod
    def resolve(cls, distname, version, source=None):
        """
        Check a dependent package

        Parameters:
            - distname: package name
            - version
        Return:
            True if the dependency resolved
        """
        try:
            version = version or ''
            get_distribution(distname + version)
            cls.dependencies[distname] = (version, source)
        except VersionConflict:
            version = version or 'any'
            print "%s: %s(%s)" % (WARNING_VERSION_CONFLICT, colored(distname, COLOR_INFO), colored(version, COLOR_INFO))
            cls.terminate = True
            cls.unresolved[distname] = (version, source)
            return False
        except DistributionNotFound:
            version = version or 'any'
            print "%s: %s(%s)" % (WARNING_NOT_FOUND, colored(distname, COLOR_INFO), colored(version, COLOR_INFO))
            cls.terminate = True
            cls.unresolved[distname] = (version, source)
            return False

        return True

    @classmethod
    def install(cls):
        """
        Install all dependencies
        """
        if len(cls.unresolved.keys()) > 0:
            print colored("\nStart resolving...", COLOR_INST)
        else:
            print "No unresolved package"
            return

        for distname in cls.unresolved.keys():
            version = cls.unresolved[distname][0]
            source = cls.unresolved[distname][1]
            print "%s %s(%s)..." % (colored('installing', COLOR_INST), distname, version)
            if 'any' == version:
                version = ''
            cls._run_pip_(distname, version, source)

    @classmethod
    def load(cls, pyfile=LOCK_FILE):
        if os.path.isfile(pyfile):
            execfile(cls.LOCK_FILE)
        else:
            print colored('No PyFile exists', COLOR_WARNING)
            exit(1)  # fail

    @classmethod
    def execute(cls, target):
        # TODO: unstable & not well tested
        if os.path.isfile(target):
            execfile(target)
        else:
            print colored('Not executable file', COLOR_WARNING)
            exit(1)  # fail

    @classmethod
    def upgrade(cls, filter=None):
        # TODO: If filter is None, slowly...
        for distname, (version, source) in cls.dependencies.iteritems():
            if filter and not distname == filter:
                continue
            print "%s %s(%s)..." % (colored('installing', COLOR_INST), distname, version)
            if 'any' == version:
                version = ''
            cls._run_pip_(distname, version, source=source, options=['--upgrade'])

    @classmethod
    def selfupdate(cls):
        cls._run_pip_(SELFUPDATE_DISTNAME, None, source=SELFUPDATE_SOURCE, options=['--upgrade'])

    @classmethod
    def _run_pip_(cls, distname, version, source=None, options=None):
        source = source or ''
        options = options or []
        if 'git' in source:
            return pip.main(initial_args=['install', cls.INSTALL_OPT, cls.INSTALL_GIT, source + '#egg=' + distname] + options)
        elif 'svn' in source:
            return pip.main(initial_args=['install', cls.INSTALL_OPT, cls.INSTALL_GIT, source + '#egg=' + distname] + options)
        else:
            return pip.main(initial_args=['install', cls.INSTALL_OPT, distname + version] + options)
