#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='criclive',
    version='0.1.1',
    description='Live Cricket Scores in Command Line.',
    author='Amit Kumar',
    license='MIT',
    keywords="Cricket score espn scores cli",
    author_email='dtu.amit@gmail.com',
    url='https://github.com/aktech/criclive',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "beautifulsoup4==4.9.0",
        "requests",
        "lxml==4.5.0",
        "tabulate==0.8.7",
    ],
    entry_points={
        'console_scripts': [
            'criclive = criclive.main:main'
        ],
    }
)
