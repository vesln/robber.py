#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

long_description = 'BDD / TDD assertion library for Python',
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='robber',
    version='1.1.2',
    description='BDD / TDD assertion library for Python',
    long_description=long_description,
    author='Tao Liang',
    author_email='tao@synapse-ai.com',
    url='https://github.com/vesln/robber.py',
    packages=[
        'robber',
        'robber.matchers',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=[
        'mock',
        'termcolor'
    ],
    tests_require=[
        'nose'
    ],
)
