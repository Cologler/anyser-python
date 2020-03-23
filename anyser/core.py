# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Optional, Any
from contextlib import contextmanager

from .err import *
from .abc import *

EXT2FORMAT_MAP = {
    '.json' : 'json',
    '.json5': 'json5',
    '.yaml' : 'yaml',
    '.yml' : 'yaml',
    '.toml' : 'toml',
}

NAME2FORMAT_MAP = {
    'pipfile' : 'pipfile'
}

_REGISTERED_SERIALIZERS = {}

def register_format(*keys):
    '''
    register a serializer class for load and dump.
    '''
    def decorator(cls):
        for k in keys:
            _REGISTERED_SERIALIZERS[k] = cls
        return cls
    return decorator


def find_serializer(format: str) -> Optional[ISerializer]:
    if not isinstance(format, str):
        raise TypeError

    cls = _REGISTERED_SERIALIZERS.get(format)
    if cls is not None:
        return cls()

@contextmanager
def capture_error():
    'catch serialize error in context'
    try:
        yield
    except (NotImplementedError, SerializeError) as e:
        raise
        raise e from None
    except Exception as e:
        raise SerializeError(e)

def loads(s: str, format: str, **options) -> Any:
    'load a obj from str.'
    if not isinstance(s, str):
        raise TypeError
    serializer = find_serializer(format)
    if not serializer:
        raise FormatNotFoundError(format)
    with capture_error():
        return serializer.loads(s, options)

def loadb(b: bytes, **options) -> Any:
    'load a obj from bytes.'
    if not isinstance(b, bytes):
        raise TypeError
    serializer = find_serializer(format)
    if not serializer:
        raise FormatNotFoundError(format)
    with capture_error():
        return serializer.loads(b, options)

def dumps(obj, format: str, **options) -> str:
    '''
    dump a obj to str.

    options:

    - `ensure_ascii` - `bool`
    - `indent` - `int?`
    '''
    serializer = find_serializer(format)
    if not serializer:
        raise FormatNotFoundError(format)
    with capture_error():
        return serializer.dumps(obj, options)

def dumpb(obj, format: str, **options) -> bytes:
    '''
    dump a obj to bytes.

    options:

    - `encoding` - `str`, default `utf-8`.
    - `ensure_ascii` - `bool`, default `True`.
    - `indent` - `int?`, default `None`.
    '''
    serializer = find_serializer(format)
    if not serializer:
        raise FormatNotFoundError(format)
    with capture_error():
        return serializer.dumpb(obj, options)
