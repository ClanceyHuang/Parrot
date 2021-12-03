#!/usr/bin/env python
# encoding: utf-8
"""
:file      :   getConfig.py
:author    :   ClanceyHuang 
:name      :   getConfig.py
:refer     :   unknown
:desc      :   提取ini配置文件中的配置信息
:version   :   Python3.x
:contact   :   ClanceyHuang@outlook.com
:copyright :   © 2017 by ClanceyHuang(Kirk).
:license   :   MIT, see LICENSE for more details.
"""

# here put the import lib

from configparser import SafeConfigParser


def get_config(config_file="config.ini"):
    parser = SafeConfigParser()
    parser.read(config_file, "utf-8")
    # get the ints, floats and strings
    _conf_ints = [(key, int(value)) for key, value in parser.items("ints")]
    # _conf_floats = [ (key, float(value)) for key,value in parser.items('floats') ]
    _conf_strings = [(key, str(value))
                     for key, value in parser.items("strings")]
    return dict(_conf_ints + _conf_strings)
