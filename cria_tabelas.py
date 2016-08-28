#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

from sql_commands import *

#Criando tabelas no banco
ddl = open('ddl.sql', 'r')
for line in ddl:
	executeSql(line),