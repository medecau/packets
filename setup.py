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
    version=samplemod.__version__,
    description='Sample package for me',
    long_description=readme,
    author=samplemod.__author__,
    author_email='medecau@gmail.com',
    url='http://medecau.github.com/samplemod',
    license=license,
    packages=find_packages(exclude=('tests'))
)

