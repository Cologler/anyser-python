# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

class FormatNotFoundError(Exception):
    'raise when a format is not found.'
    pass

class SerializeError(Exception):
    'raise when serialize or deserialize from bad data.'
    pass

class NotSupportError(Exception):
    pass

class SizeOverflowError(Exception):
    pass
