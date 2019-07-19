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

import pytest
from easy_enum import Enum


class TestEnum(Enum):
    FIRST_ITEM  = 1
    SECOND_ITEM = (2, 'Description for second item')
    THIRD_ITEM  = (3, 'third', '')
    FOURTH_ITEM = (4, 'fourth', 'Description for fourth item')


def test_values():
    assert TestEnum.FIRST_ITEM == 1
    assert TestEnum['FIRST_ITEM'] == 1
    assert TestEnum['third'] == 3


def test_names():
    assert TestEnum[1] == 'FIRST_ITEM'
    assert TestEnum[3] == 'third'


def test_contains():
    assert 3 in TestEnum
    assert 0 not in TestEnum
    assert 'third' in TestEnum
    assert 'zero' not in TestEnum


def test_internals():
    assert len(TestEnum) == 4
    for item in TestEnum:
        assert len(item) == 3
        assert isinstance(item[0], str)
        assert isinstance(item[1], int)
        assert isinstance(item[2], str)


def test_description():
    assert TestEnum.desc(1) == ''
    assert TestEnum.desc(4) == 'Description for fourth item'
    assert TestEnum.desc('third') == ''


def test_basic_exceptions():
    with pytest.raises(AttributeError):
        _ = TestEnum['second']
    with pytest.raises(ValueError):
        _ = TestEnum[10]
    with pytest.raises(TypeError):
        _ = TestEnum[(1, 2)]


def test_desc_exceptions():
    with pytest.raises(AttributeError):
        _ = TestEnum.desc('second')
    with pytest.raises(ValueError):
        _ = TestEnum.desc(10)
    with pytest.raises(TypeError):
        _ = TestEnum.desc((1, 2))
