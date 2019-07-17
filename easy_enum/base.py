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


class MetaEnum(type):
    """ MetaClass for Enum Type """

    def __new__(mcs, cls, bases, class_dict):
        new_cls = super().__new__(mcs, cls, bases, class_dict)
        new_cls._items_ = list()
        for name, value in class_dict.items():
            if name in set(dir(type(cls, (object,), {}))) or (name.startswith('_') and name.endswith('_')):
                continue
            if isinstance(value, tuple):
                if len(value) == 2:
                    new_cls._items_.append((name, value[0], value[1]))
                else:
                    new_cls._items_.append((value[1], value[0], value[2]))
                setattr(new_cls, name, value[0])
            else:
                new_cls._items_.append((name, value, ''))

        return new_cls

    def __getitem__(cls, key):
        if isinstance(key, str):
            for item in cls._items_:
                if key.upper() == item[0].upper():
                    return item[1]
            raise AttributeError("\'%s\' has no item with name \'%s\'" % (cls.__name__, key))
        elif isinstance(key, int):
            for item in cls._items_:
                if key == item[1]:
                    return item[0]
            raise ValueError("\'%s\' has no item with value \'%d\'" % (cls.__name__, key))
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
    """ Enum Type implementation in Python """

    @classmethod
    def desc(cls, key):
        if isinstance(key, str):
            for item in cls._items_:
                if key.upper() == item[0].upper():
                    return item[2]
            raise AttributeError("\'%s\' has no item with name \'%s\'" % (cls.__name__, key))
        elif isinstance(key, int):
            for item in cls._items_:
                if key == item[1]:
                    return item[2]
            raise ValueError("\'%s\' has no item with value \'%d\'" % (cls.__name__, key))
        else:
            raise TypeError("\'%s\' has no item with type \'%r\'" % (cls.__name__, type(key)))
