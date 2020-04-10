# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from anyser import *

def test_yaml_default():
    data = {
        'a': 1,
        'b': '2',
        'c': {
            'd': 'ddddd'
        }
    }

    s = dumps(data, 'yaml')
    assert loads(s, 'yaml') == data

def test_yaml_dumps_ensure_ascii():
    data = '👍'
    assert dumps(data, 'yaml', ensure_ascii=True) == '"\\U0001F44D"\n'
    assert dumps(data, 'yaml', ensure_ascii=False) == '👍\n...\n'

def test_yaml_dumps_indent():
    data = {'a': 1, 'b': {'c': 7}}
    assert dumps(data, 'yaml') ==           'a: 1\nb:\n  c: 7\n'
    assert dumps(data, 'yaml', indent=4) == 'a: 1\nb:\n    c: 7\n'

def test_yaml_serialize_error():
    with pytest.raises(SerializeError):
        loads('"', 'yaml')
