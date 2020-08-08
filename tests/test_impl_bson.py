# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from anyser import *

data_1 = {
    'a': 1,
    'b': '2',
    'c': {
        'd': 'ddddd'
    }
}

def test_bson():
    b = dumpb(data_1, 'bson')
    assert isinstance(b, bytes)
    assert loadb(b, 'bson') == data_1

def test_bson_load_with_error():
    with pytest.raises(SerializeError):
        loadb(b'', 'bson')
    with pytest.raises(SerializeError):
        loadb(b'gfwjeio', 'bson')
