#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient


class MongoDB:
    def __init__(self, hostname, port, database, user, password):
        self.client = MongoClient(hostname, port)
        self.db = self.client[database]
