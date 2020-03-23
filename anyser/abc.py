# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import Any

def str2bytes(s: str, options: dict) -> bytes:
    return s.encode(options.pop('encoding', 'utf-8'))

def bytes2str(b: bytes, options: dict) -> str:
    return b.decode(options.pop('encoding', 'utf-8'))

class ISerializer:
    format_name: str

    def is_overrided(self, name: str):
        return getattr(type(self), name, None) is not getattr(ISerializer, name, None)

    def check_options(self, options: dict):
        if options:
            raise TypeError(f'unexpected options: {options}')

    def loads(self, s: str, options: dict) -> Any:
        'load a obj from str.'

        if self.is_overrided('loadb'):
            return self.loadb(str2bytes(s, options), options)

        raise NotImplementedError

    def loadb(self, b: bytes, options: dict) -> Any:
        'load a obj from bytes.'

        if self.is_overrided('loads'):
            return self.loads(bytes2str(b, options), options)

        raise NotImplementedError

    def dumps(self, obj, options: dict) -> str:
        'dump a obj to str.'

        if self.is_overrided('dumpb'):
            return bytes2str(self.dumpb(obj, options), options)

        raise NotImplementedError

    def dumpb(self, obj, options: dict) -> bytes:
        'dump a obj to bytes.'

        if self.is_overrided('dumps'):
            return str2bytes(self.dumps(obj, options), options)

        raise NotImplementedError
