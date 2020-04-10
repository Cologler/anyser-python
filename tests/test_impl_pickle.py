# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from anyser import *

def test_pickle_default():
    data = {
        'a': 1,
        'b': '2',
        'c': {
            'd': 'ddddd'
        }
    }

    s = dumpb(data, 'pickle')
    assert loadb(s, 'pickle') == data

def test_pickle_serialize_error():
    with pytest.raises(SerializeError):
        loadb(b's', 'pickle')
