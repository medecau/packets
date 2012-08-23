# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='packets',
    version='0.0.6',
    description='UDP for Humans',
    author='Pedro Rodrigues',
    author_email='medecau@gmail.com',
    url='http://medecau.github.com/packets',
    license=license,
    pu_modules=['travis'],
    packages=find_packages(exclude=('test')),
    #install_requires=['clint',],
)

