pyEnum
======

[![Build Status](https://travis-ci.org/molejar/pyEnum.svg?branch=master)](https://travis-ci.org/molejar/pyEnum)
[![Coverage Status](https://coveralls.io/repos/github/molejar/pyEnum/badge.svg?branch=master)](https://coveralls.io/github/molejar/pyEnum?branch=master)
[![PyPI Status](https://img.shields.io/pypi/v/easy-enum.svg)](https://pypi.python.org/pypi/easy-enum)
[![Python Version](https://img.shields.io/pypi/pyversions/easy-enum.svg)](https://www.python.org)

User friendly implementation of documented `Enum` type for Python language.

Installation
------------

``` bash
    $ pip install easy_enum
```

To install the latest version from master branch execute in shell following commands:

``` bash
    $ pip install -U https://github.com/molejar/pyEnum/archive/master.zip
```

In case of development, install pyEnum from sources:

``` bash
    $ git clone https://github.com/molejar/pyEnum.git
    $ cd pyEnum
    $ pip install -U -e .
```

You may run into a permissions issues running these commands. Here are a few options how to fix it:

1. Run with `sudo` to install pyEnum and dependencies globally
2. Specify the `--user` option to install locally into your home directory (export "~/.local/bin" into PATH variable if haven't).
3. Run the command in a [virtualenv](https://virtualenv.pypa.io/en/latest/) local to a specific project working set.

Usage
-----

Example for basic Enum (Enum):

``` Python
    from easy_enum import Enum

    class TestEnum(Enum):

        # attribute with no description, the name will be 'FIRST_ITEM' and empty string as description
        FIRST_ITEM  = 1

        # attribute with description
        SECOND_ITEM = (2, 'Description for second item')

        # attribute with description and custom string name
        THIRD_ITEM  = (3, 'third', 'Description for third item')

        # attribute with custom string name (the description must be specified as empty string)
        FOURTH_ITEM = (4, 'fourth', '')


    # Read attributes value and name
    print(TestEnum.SECOND_ITEM)    # 2
    print(TestEnum['FIRST_ITEM'])  # 1
    print(TestEnum[1])             # 'FIRST_ITEM'
    print(TestEnum[3])             # 'third'
    print(TestEnum['third'])       # 3

    # Get count of all attributes
    print(len(TestEnum))           # 4

    # Get list with all attributes name
    names = [item[0] for item in TestEnum]
    print(names)

    # Get list with all attributes value
    values = [item[1] for item in TestEnum]
    print(values)

    # Read all items
    for name, value, desc in TestEnum:
        print('{} = {} ({})'.format(name, value, desc))
```

Example for extended Enum (EEnum):

``` Python
    from easy_enum import EEnum as Enum

    class TestEnum(Enum):

        # attribute with no description, the name will be 'FIRST_ITEM' and empty string as description
        FIRST_ITEM  = 1

        # attribute with description
        SECOND_ITEM = (2, 'Description for second item')

        # attribute with description and custom string name
        THIRD_ITEM  = (3, 'third', 'Description for third item')

        # attribute with custom string name (the description must be specified as empty string)
        FOURTH_ITEM = (4, 'fourth', '')

    # Check if exist attribute with specific value
    print(TestEnum.is_valid(1))       # True
    print(TestEnum.is_valid(8))       # False

    # Check if exist attribute with specific name
    print(TestEnum.is_valid('first')) # False
    print(TestEnum.is_valid('third')) # True

    # Get attribute description (as parameter use attribute name or value)
    print(TestEnum.desc(1))           # ''
    print(TestEnum.desc(2))           # 'Description for second item'
    print(TestEnum.desc('third'))     # 'Description for third item'

```
