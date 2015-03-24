#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# To Upload to PyPI by executing:  python3 setup.py sdist upload -r pypi


"""Setup.py for Python, as Generic as possible."""


import os

from setuptools import setup


MODULE_PATH = os.path.join(os.getcwd(), "octopussh")


def find_this(search, filename=MODULE_PATH):
    """Take a string and a filename path string and return the found value."""
    if not search:
        return
    for line in open(str(filename)).readlines():
        if search.lower() in line.lower():
            line = line.split("=")[1].strip()
            if "'" in line or '"' in line or '"""' in line:
                line = line.replace("'", "").replace('"', '').replace('"""', '')
            return line


setup(

    name="octopussh",
    description="SSH Launcher from .sh Bash Scripts",

    version=find_this("__version__"),

    url=find_this("__url__"),
    license=find_this("__licence__"),

    author=find_this("__author__"),
    author_email=find_this("__email__"),
    maintainer=find_this("__author__"),
    maintainer_email=find_this("__email__"),


    include_package_data=True,
    zip_safe=True,
    install_requires=['pip'],
    requires=['pip'],


    scripts=['octopussh'],


    keywords=['SSH', 'Bash', 'SysAdmin', 'DevOps', 'Administration', 'Server'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',

        'Natural Language :: English',

        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',

        'Programming Language :: Python :: Implementation :: CPython',

        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)
