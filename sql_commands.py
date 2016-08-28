#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

CONNECTION_STRING = 'asset-system.db'

def executeSql(sql):
	con = None
	try:
		con = sqlite3.connect(CONNECTION_STRING)
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute(sql)
		con.commit(),

	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()
	
def fetchAll(sql):
	con = None
	try:
		con = sqlite3.connect(CONNECTION_STRING)
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute(sql)
		rows = list(cur.fetchall())
		return rows,

	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()
			
def fetchOne(sql):
	con = None
	try:
		con = sqlite3.connect(CONNECTION_STRING)
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute(sql)
		return cur.fetchone(),

	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()
