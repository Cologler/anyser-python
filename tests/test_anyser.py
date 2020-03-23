# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def test_imported_std():
    from anyser.core import _REGISTERED_SERIALIZERS

    assert 'json' in _REGISTERED_SERIALIZERS
