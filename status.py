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

statusApp = Bottle()

@statusApp.route('/status')
@statusApp.post('/status')
def listUsers():
	aaa.require(role="admin", fail_redirect='/login')
	rows = fetchAll('SELECT * FROM STATUS')
	return template('status-list',statusList = rows[0])
	

@statusApp.route('/status/new')
@statusApp.post('/status/new')
def newStatus():
	aaa.require(role="admin", fail_redirect='/login')
	return template('status-new')

@statusApp.post('/status/new/save')
def saveNewUser():
	aaa.require(role="admin", fail_redirect='/login')
	descricao = request.forms.get('descricao')
	
	sql = "INSERT INTO STATUS(DESCRICAO) VALUES('%s')" % (descricao)
	
	executeSql(sql)

@statusApp.post('/status/update')
def updateStatus():
	aaa.require(role="admin", fail_redirect='/login')
	id = request.forms.get('id')

	sql = "SELECT * FROM STATUS WHERE ID = '%s'" % id
	status = fetchOne(sql)

	return template('status-update', sts = status[0])

@statusApp.post('/status/update/save')
def saveUpdatedStatus():
	aaa.require(role="admin", fail_redirect='/login')
	descricao = request.forms.get('descricao')
	id = request.forms.get('id')

	sql = "UPDATE STATUS SET DESCRICAO = '%s' WHERE ID = %s" % (descricao, id)
	
	executeSql(sql)

@statusApp.route('/status/delete')
@statusApp.post('/status/delete')
def delete():
	aaa.require(role="admin", fail_redirect='/login')
	id = request.forms.get('id')

	sql = "DELETE FROM STATUS WHERE ID = '%s'" % id
	executeSql(sql)