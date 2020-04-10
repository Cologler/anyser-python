# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

import xml.etree.ElementTree as et
from anyser import *

def test_xml_default():
    rot = et.Element('rot')
    rot.set('d', 'k')
    et.SubElement(rot, 'item').text = 'dsa'

    assert dumps(rot, 'xml') == '<rot d="k"><item>dsa</item></rot>'

def test_xml_serialize_error():
    with pytest.raises(SerializeError):
        loads('s', 'xml')
    with pytest.raises(SerializeError):
        dumps(object(), 'xml')
