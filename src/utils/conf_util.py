#!/usr/bin/env python
# -*- coding:utf-8 -*-
import configparser
config = configparser.ConfigParser()


def get_conf(directory, key):
    return config[directory][key]