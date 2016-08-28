#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle
from bottle import route, run, template, redirect, request
import sys
import datetime
import json
# from cgi import escape

from sql_commands import *
from authentication import *

userApp = Bottle()

@userApp.route('/user/new')
@userApp.post('/user/new')
def newUser():
	aaa.require(role="admin", fail_redirect='/login')
	return template('new-user')

@userApp.post('/user/new/save')
def saveNewUser():
	aaa.require(role="admin", fail_redirect='/login')
	username = request.forms.get('username');
	nome = request.forms.get('nome')
	telefone = request.forms.get('telefone')
	senha = request.forms.get('senha')
	role = request.forms.get('role')
	email_addr = request.get('email_addr')

	result = "success"
	try:
		aaa.create_user(username=username, role=role, password=senha, email_addr=email_addr)
		sql = "UPDATE USERS SET NOME = '%s', TELEFONE = '%s' WHERE USERNAME = '%s'" % (nome, telefone, username)
		executeSql(sql)
	except Exception, e:
		print e.message
		if(e.message == "User is already existing."):
			result = "Username não disponível."
		else:
			result = "Ocorreu um erro ao salvar usuário"
	return '{"result": "' + result + '"}'

@userApp.route('/user')
@userApp.post('/user')
def listUsers():
	aaa.require(role="admin", fail_redirect='/login')
	rows = fetchAll('SELECT * FROM USERS')
	return template('user-list',usuarios = rows[0])
	
@userApp.post('/user/update')
def updateUser():
	aaa.require(role="admin", fail_redirect='/login')
	username = request.forms.get('username')

	sql = "SELECT * FROM USERS WHERE USERNAME = '%s'" % username
	usuario = fetchOne(sql)

	return template('update-user', usuario = usuario[0])
	
@userApp.post('/user/update/save')
def saveUpdatedUser():
	aaa.require(role="admin", fail_redirect='/login')
	username = request.forms.get('username')
	nome = request.forms.get('nome')
	telefone = request.forms.get('telefone')
	role = request.forms.get('role')
	email_addr = request.forms.get('email_addr')
	id = request.forms.get('id')

	sql = "UPDATE USERS SET NOME = '%s', TELEFONE = '%s', EMAIL_ADDR = '%s', ROLE = '%s' WHERE USERNAME = '%s'" % (nome, telefone, email_addr, role, username)
	
	executeSql(sql)

@userApp.route('/user/delete')
@userApp.post('/user/delete')
def delete():
	aaa.require(role="admin", fail_redirect='/login')
	username = request.forms.get('username')
	aaa.delete_user(username)