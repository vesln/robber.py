#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='robber',
    version='1.0.1',
    description='BDD / TDD assertion library for Python',
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
)
