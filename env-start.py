#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys
import datetime

CONNECTION_STRING = 'item.db'

def create_tables():

	print 'create_tables'
	
	con = None

	try:
		con = sqlite3.connect(CONNECTION_STRING)
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS Items")
		cur.execute("CREATE TABLE Items(id INTEGER PRIMARY KEY, name TEXT, description TEXT, createdIn date, alteredIn date)")
	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()


def init_data():
	data = [{
		'name':'Aula 01',
		'description':u'Introdução'
	}, {
		'name':'Aula 02',
		'description':'Shell Script'
	}, {
		'name':'Aula 03',
		'description':u'Python'
	}]

	for d in data:
		save(d)

def save(data, id=None):

	con = None

	try:
		con = sqlite3.connect(CONNECTION_STRING)
		cur = con.cursor()
		
		if id:
			# UPDATE

			data['alteredIn'] = datetime.datetime.now()
			data['id'] = id
			cur.execute("UPDATE Items SET name=:name, description=:description, alteredIn=:alteredIn WHERE id=:id", data)
		else:
			# INSERT
			data['alteredIn'] = datetime.datetime.now()
			data['createdIn'] = datetime.datetime.now()
			cur.execute("INSERT INTO Items (name, description, createdIn, alteredIn) VALUES (:name, :description, :createdIn, :alteredIn);", data)
		con.commit()

	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()

if __name__ == '__main__':

	create_tables()
	init_data()