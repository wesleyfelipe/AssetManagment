#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run, template, redirect, request
import sqlite3
import sys
import datetime
import json
# from cgi import escape

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
			
#Criando tabelas no banco
ddl = open('ddl.sql', 'r')
for line in ddl:
	executeSql(line),

@route('/app/home')
def home():
	return template('home')
	
@route('/app/user/new')
def newUser():
	return template('new-user')

@route('/app/user/new/save')
def saveNewUser():
	nome = request.query.get('nome')
	telefone = request.query.get('telefone')
	senha = request.query.get('senha')
	role = request.query.get('role')
	
	sql = "INSERT INTO USUARIO(NOME, TELEFONE, SENHA, ROLE) VALUES('%s','%s','%s','%s')" % (nome, telefone, senha, role)
	
	executeSql(sql)
	redirect('/app/user')

@route('/app/user')
def listUsers():
	rows = fetchAll('SELECT * FROM USUARIO')
	return template('user-list',usuarios = rows[0])
	
@route('/app/user/update')
def updateUser():
	sql = "SELECT * FROM USUARIO WHERE ID = %s" % request.query.get('id')
	usuario = fetchOne(sql)
	return template('update-user', usuario = usuario[0])
	
@route('/app/user/update/save')
def saveUpdatedUser():
	nome = request.query.get('nome')
	telefone = request.query.get('telefone')
	senha = request.query.get('senha')
	role = request.query.get('role')
	id = request.query.get('id')
	
	sql = "UPDATE USUARIO SET NOME = '%s', TELEFONE = '%s', SENHA = '%s', ROLE = '%s' WHERE ID = %s" % (nome, telefone, senha, role, id)
	
	executeSql(sql)
	redirect('/app/user')

@route('/app/user/delete')
def delete():
	sql = "DELETE FROM USUARIO WHERE ID = %s" % request.query.get('id')
	executeSql(sql)
	redirect('/app/user')

run(host='localhost', port=8080)

