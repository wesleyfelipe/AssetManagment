#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, redirect, request
import sqlite3
import sys
import datetime
import json
# from cgi import escape

CONNECTION_STRING = 'item.db'

@route('/')
def index():

	con = None

	try:
		con = sqlite3.connect(CONNECTION_STRING)
		
		con.row_factory = sqlite3.Row
		
		cur = con.cursor()
		
		cur.execute("CREATE TABLE IF NOT EXISTS Items(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR NOT NULL, description VARCHAR NOT NULL);")
	
		cur.execute("SELECT * FROM Items")

		rows = list(cur.fetchall())

		html = "<html><body>"
		html += "<div> <a href='/new'>Novo</a> </div>"
		html += "<table><tr><td>ID</td><td>Name</td><td>Description</td><td>Acao</td></tr>"

		for row in rows:
			html += """
<tr>
	<td>%s</td>
	<td>%s</td>
	<td>%s</td>
	<td><a href='#' onclick=\"javascript:document.location='/update?ItemId=%s'\">atualizar</a></td>
	<td><a href='#' onclick=\"javascript:document.location='/delete?ItemId=%s'\">excluir</a></td>
</tr>""" % (row['id'], row['name'], row['description'], row['id'], row['id'])

		html += "<table><body><html>"

		return html

	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()


@route('/submit')
def submit():

	action = request.query.get('action')
	print action
	if action == 'Novo':
		redirect('new')
	elif action == 'Atualizar':
		redirect('update?ItemId=%s' % request.query.get('ItemId'))
	elif action == 'Excluir':
		deleteItem(int(request.query.get('ItemId')))
		redirect('/')

@route('/new')
def new():

	html = """
<html>
	<body>
		<form action='save'>
			<div>
				Name: <input type='text' name='name'><br>
				Descricao: <input type='text' name='description'>
			</div>
			<div>
				<input type='submit' value='Salvar'>
			</div>
		<form>
	</body>
</html>
	"""
	return html
	

@route('/update')
def update():
	con = None

	try:
		con = sqlite3.connect(CONNECTION_STRING)
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		sqlCommand = "SELECT * FROM Items WHERE id=%s" % request.query.get('ItemId')
		cur.execute(sqlCommand)
		row = cur.fetchone()
		html = """
<html>
	<body>
		<form action='save'>
			<div>
				<input type='hidden' name='ItemId' value=%s>
				Name: <input type='text' name='name' value='%s'><br>
				Descricao: <input type='text' name='description' value='%s'>
			</div>
			<div>
				<input type='submit' value='Salvar'>
			</div>
		<form>
	</body>
</html>
		""" % (row['id'] or '', row['name'] or '', row['description'] or '')

		return html

	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()

@route('/save')
def save():
	ItemId = request.query.get('ItemId')
	name = request.query.get('name')
	description = request.query.get('description')

	if ItemId:
		saveItem({'name': name, 'description': description}, id=int(ItemId))
	else:
		saveItem({'name': name, 'description': description})

	redirect('/')

@route('/delete')
def delete():
	ItemId = request.query.get('ItemId')
	
	deleteItem(ItemId)

	redirect('/')



def saveItem(data, id=None):
	con = None
	try:
		con = sqlite3.connect(CONNECTION_STRING)
		cur = con.cursor()
		if id:
			# UPDATE
			# data['alteredIn'] = datetime.datetime.now()
			data['id'] = id
			sqlCommand = "UPDATE Items SET name='%s', description='%s' WHERE id=%s" % (data['name'], data['description'], data['id']) 
			cur.execute(sqlCommand)
		else:
			# INSERT
			# data['alteredIn'] = datetime.datetime.now()
			# data['createdIn'] = datetime.datetime.now()
			sqlCommand = "INSERT INTO Items (name, description) VALUES ('%s', '%s')" % (data['name'], data['description'])
			cur.execute(sqlCommand)
		con.commit()

	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()


def deleteItem(id):

	con = None

	try:
		con = sqlite3.connect(CONNECTION_STRING)
		cur = con.cursor()
		sqlCommand = "DELETE FROM Items WHERE id=%s" % id
		cur.execute(sqlCommand)
		con.commit()
	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if con:
			con.close()

run(host='localhost', port=8080)

