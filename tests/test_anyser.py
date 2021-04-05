# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import io

import pytest

from anyser import *
from anyser.err import FormatNotFoundError, SizeOverflowError

def test_imported_std():
    from anyser.core import _REGISTERED_SERIALIZERS

    assert 'json' in _REGISTERED_SERIALIZERS

def test_use_unknown_format():
    with pytest.raises(FormatNotFoundError):
        loadb(b'', 'ssssss')
    with pytest.raises(FormatNotFoundError):
        dumpb(b'', 'ssssss')
    with pytest.raises(FormatNotFoundError):
        loads('', 'ssssss')
    with pytest.raises(FormatNotFoundError):
        dumps('', 'ssssss')

def test_get_available_formats():
    assert set(get_available_formats()) == {
        'json', '.json',
        'pickle',
        'json5', '.json5',
        'toml',  '.toml',
        'xml', '.xml',
        'yaml', '.yaml', '.yml',
        'bson', '.bson',
        'bencode', '.torrent',
    }

def test_options_strict():
    loadb(b'{}', 'json', encoding='utf-8')
    loadf(io.BytesIO(b'{}'), 'json', encoding='utf-8')

    with pytest.raises(ValueError):
        loads('{}', 'json', encoding='utf-8')

    with pytest.raises(ValueError):
        loadf(io.StringIO('{}'), 'json', encoding='utf-8')

def test_options_not_strict():
    loads('{}', 'json', encoding='utf-8', strict=False)
    loadf(io.StringIO('{}'), 'json', encoding='utf-8', strict=False)

def test_options_size_limit():
    with pytest.raises(TypeError):
        loadf(io.StringIO('{}'), 'json', size_limit=1.1)

    with pytest.raises(ValueError):
        loadf(io.StringIO('{}'), 'json', size_limit=0)

    with pytest.raises(SizeOverflowError):
        loadf(io.StringIO('{}'), 'json', size_limit=1)

    loadf(io.StringIO('{}'), 'json', size_limit=2)
    loadf(io.StringIO('{}'), 'json', size_limit=3)
