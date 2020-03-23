# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import xml.etree.ElementTree as et
from anyser import *

def test_xml_default():
    rot = et.Element('rot')
    rot.set('d', 'k')
    et.SubElement(rot, 'item').text = 'dsa'

    assert dumps(rot, 'xml') == '<rot d="k"><item>dsa</item></rot>'
