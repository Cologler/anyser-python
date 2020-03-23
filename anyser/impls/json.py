# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import json

from ..abc import *
from ..core import register_format

@register_format('json', '.json')
class JsonSerializer(ISerializer):
    format_name = 'json'

    def loads(self, s: str, options: dict):
        kwargs = {}
        self.check_options(options)
        return json.loads(s, **kwargs)

    def dumps(self, obj, options: dict) -> str:
        kwargs = {
            'ensure_ascii': options.pop('ensure_ascii', True),
            'indent': options.pop('indent', None),
        }
        self.check_options(options)
        return json.dumps(obj, **kwargs)
