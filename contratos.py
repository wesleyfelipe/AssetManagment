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

contratosApp = Bottle()

@contratosApp.route('/contratos')
@contratosApp.post('/contratos')
def listUsers():
	aaa.require(role="admin", fail_redirect='/login')
	rows = fetchAll('SELECT * FROM contrato')
	return template('contratos-list',contratosList = rows[0])
	

@contratosApp.route('/contratos/new')
@contratosApp.post('/contratos/new')
def newcontratos():
	aaa.require(role="admin", fail_redirect='/login')
	return template('contratos-new')

@contratosApp.post('/contratos/new/save')
def saveNewUser():
	aaa.require(role="admin", fail_redirect='/login')
	descricao = request.forms.get('descricao')
	
	sql = "INSERT INTO contrato(DESCRICAO) VALUES('%s')" % (descricao)
	
	executeSql(sql)

@contratosApp.post('/contratos/update')
def updatecontratos():
	aaa.require(role="admin", fail_redirect='/login')
	id = request.forms.get('id')

	sql = "SELECT * FROM contrato WHERE ID = '%s'" % id
	contratos = fetchOne(sql)

	return template('contratos-update', ctr = contratos[0])

@contratosApp.post('/contratos/update/save')
def saveUpdatedcontratos():
	aaa.require(role="admin", fail_redirect='/login')
	descricao = request.forms.get('descricao')
	id = request.forms.get('id')

	sql = "UPDATE contrato SET DESCRICAO = '%s' WHERE ID = %s" % (descricao, id)
	
	executeSql(sql)

@contratosApp.route('/contratos/delete')
@contratosApp.post('/contratos/delete')
def delete():
	aaa.require(role="admin", fail_redirect='/login')
	id = request.forms.get('id')

	sql = "DELETE FROM contrato WHERE ID = '%s'" % id
	executeSql(sql)