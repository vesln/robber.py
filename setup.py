#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='robber',
    version='0.0.4',
    description='BDD / TDD assertion library for Python',
    author='Veselin Todorov',
    author_email='hi@vesln.com',
    url='https://github.com/vesln/robber.py',
    packages=[
        'robber',
        'robber.matchers',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing'
    ],
)
