#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

package_name = 'helloworld'
filename = package_name + '.py'

setup(
    name=package_name,
    version=0.1,
    author='warosaurus',
    author_email='',
    description='Test',
    url='',
    long_description="Test Hello World",
    py_modules=[package_name],
    entry_points={
        'console_scripts': [
            'helloworld=helloworld:main'
        ]
    },
)
