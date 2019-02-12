#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb


class MySQL:
    def __init__(self, hostname, port, database, user, password):
        connection = MySQLdb.connect(
            host=hostname, port=port, user=user, passwd=password, db=database, charset='utf8')
        self.cursor = connection.cursor()