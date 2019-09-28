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

__author__  = "Martin Olejar"
__contact__ = "martin.olejar@gmail.com"
__version__ = "0.3.0"
__license__ = "Apache 2.0"
__status__  = "Production"
__all__     = ['Enum']


class MetaEnum(type):
    """ Meta Class for Enum Type """

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        cls._items_ = list()
        for attr, value in attrs.items():
            if attr in set(dir(type(name, (object,), {}))) or (attr.startswith('_') and attr.endswith('_')):
                continue
            if isinstance(value, classmethod):
                continue
            if isinstance(value, tuple):
                if len(value) == 2:
                    cls._items_.append((attr, value[0], value[1]))
                else:
                    cls._items_.append((value[1], value[0], value[2]))
                setattr(cls, attr, value[0])
            else:
                cls._items_.append((attr, value, ''))
        return cls

    def __getitem__(cls, key):
        if isinstance(key, str):
            for name, value, _ in cls._items_:
                if key.upper() == name.upper():
                    return value
            raise KeyError("\'%s\' has no item with name \'%s\'" % (cls.__name__, key))

        elif isinstance(key, int):
            for name, value, _ in cls._items_:
                if key == value:
                    return name
            raise KeyError("\'%s\' has no item with value \'%d\'" % (cls.__name__, key))

        else:
            raise TypeError("\'%s\' has no item with type \'%r\'" % (cls.__name__, type(key)))

    def __iter__(cls):
        return (item for item in cls._items_)

    def __contains__(cls, item):
        if isinstance(item, str) and item in (item[0] for item in cls._items_):
            return True
        if isinstance(item, int) and item in (item[1] for item in cls._items_):
            return True
        return False

    def __len__(cls):
        return len(cls._items_)


class Enum(metaclass=MetaEnum):
    """ Enum Type Class """

    @classmethod
    def get(cls, key, default=None):
        try:
            return cls[key]
        except KeyError:
            return default

    @classmethod
    def desc(cls, key, default=''):
        if isinstance(key, str):
            for name, _, desc in cls._items_:
                if key.upper() == name.upper():
                    return desc
            return default

        elif isinstance(key, int):
            for _, value, desc in cls._items_:
                if key == value:
                    return desc
            return default

        else:
            raise TypeError("\'%s\' has no item with type \'%r\'" % (cls.__name__, type(key)))
