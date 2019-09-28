#!/usr/bin/env python

# Copyright 2019 Martin Olejar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from setuptools import setup
from easy_enum import __version__, __license__, __author__, __contact__


def long_description():
    try:
        import pypandoc

        readme_path = path.join(path.dirname(__file__), 'README.md')
        return pypandoc.convert(readme_path, 'rst').replace('\r', '')
    except (IOError, ImportError):
        return (
            "More on: https://github.com/molejar/pyEnum"
        )


setup(
    name='easy_enum',
    version=__version__,
    license=__license__,
    author=__author__,
    author_email=__contact__,
    url='https://github.com/molejar/pyEnum',
    description='User friendly implementation of Enum in Python',
    long_description=long_description(),
    py_modules=['easy_enum'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ]
)