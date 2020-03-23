# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from anyser import *

def test_json_equals():
    data = {
        'a': 1,
        'b': '2',
        'c': {
            'd': 'ddddd'
        }
    }

    s = dumps(data, 'json')
    assert loads(s, 'json') == data

def test_json_dumps_ensure_ascii():
    data = '👍'
    assert dumps(data, 'json', ensure_ascii=False) == "\"👍\""

def test_json_dumps_indent():
    data = {'a': 1, 'b': {}}
    assert dumps(data, 'json', indent=2) == '{\n  "a": 1,\n  "b": {}\n}'
