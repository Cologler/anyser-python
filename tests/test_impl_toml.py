# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------
import pytest

from anyser import *

def test_toml_default():
    data = {
        'a': 1,
        'b': '2',
        'c': {
            'd': 'ddddd'
        }
    }

    s = dumps(data, 'toml')
    assert loads(s, 'toml') == data

def test_toml_serialize_error():
    with pytest.raises(SerializeError):
        loads('\0\"', 'toml')
    with pytest.raises(SerializeError):
        dumps(object(), 'toml')
