# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import packets

#with open('README.rst') as f:
#    readme = f.read()
readme = "nothing to see here, move along"

with open('LICENSE') as f:
    license = f.read()

setup(
    name='packets',
    version=packets.__version__,
    description='UDP for Humans',
    long_description=readme,
    author=packets.__author__,
    author_email='medecau@gmail.com',
    url='http://medecau.github.com/packets',
    license=license,
    packages=find_packages(exclude=('test'))
)

