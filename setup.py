#!/usr/bin/env python

from distutils.core import setup

setup(name='yahooapi',
      version='1.0.0',
      description='Python Distribution Utilities',
      author='Rocky Xu',
      author_email='percyxu@hotmail.com',
      url='finaius.com',
      packages=['yahooapi'],
            install_requires=[
            'pandas'
      ]
     )