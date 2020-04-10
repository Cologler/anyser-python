# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from anyser import *
from io import BytesIO, StringIO

data_1 = {
    'a': 1,
    'b': '2',
    'c': {
        'd': 'ddddd'
    }
}

def test_json_dumps():
    s = dumps(data_1, 'json')
    assert isinstance(s, str)

def test_json_dumpb():
    b = dumpb(data_1, 'json')
    assert isinstance(b, bytes)

def test_json_dumpf_str():
    fp = StringIO()
    dumpf(data_1, fp, 'json')
    assert fp.getvalue() == '{"a": 1, "b": "2", "c": {"d": "ddddd"}}'

def test_json_dumpf_bytes():
    fp = BytesIO()
    dumpf(data_1, fp, 'json')
    assert fp.getvalue() == b'{"a": 1, "b": "2", "c": {"d": "ddddd"}}'

def test_json_load():
    assert data_1 == load(dumps(data_1, 'json'), 'json')
    assert data_1 == load(dumpb(data_1, 'json'), 'json')

def test_json_loads():
    assert data_1 == loads(dumps(data_1, 'json'), 'json')

def test_json_loadb():
    assert data_1 == loadb(dumpb(data_1, 'json'), 'json')

def test_json_dumps_ensure_ascii():
    data = '👍'
    assert dumps(data, 'json', ensure_ascii=False) == "\"👍\""

def test_json_dumps_indent():
    data = {'a': 1, 'b': {}}
    assert dumps(data, 'json', indent=2) == '{\n  "a": 1,\n  "b": {}\n}'

def test_json_serialize_error():
    with pytest.raises(SerializeError):
        loads('s', 'json')
    with pytest.raises(SerializeError):
        dumps(object(), 'json')
