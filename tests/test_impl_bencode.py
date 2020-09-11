# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from anyser import *
from io import BytesIO, StringIO

def test_bencode_dumpb():
    assert dumpb({'title': 'Example'}, 'bencode') == b'd5:title7:Examplee'
    assert dumpb(12, 'bencode') == b'i12e'

def test_bencode_load():
    assert load('d5:title7:Examplee', 'bencode') == {'title': 'Example'}
    assert load(b'd5:title7:Examplee', 'bencode') == {b'title': b'Example'}
    assert load('i12e', 'bencode') == 12

def test_bencode_loads():
    assert loads('d5:title7:Examplee', 'bencode') == {'title': 'Example'}
    assert loads('i12e', 'bencode') == 12

def test_bencode_loadb():
    assert loadb(b'd5:title7:Examplee', 'bencode') == {b'title': b'Example'}
    assert loadb(b'i12e', 'bencode') == 12
