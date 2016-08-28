#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle
from bottle import route, run, template, redirect, request
import sys
import datetime
import json

from sql_commands import *
from authentication import *

ativoApp = Bottle()

@ativoApp.route('/ativo')
@ativoApp.post('/ativo')
def listAtivo():
	aaa.require(fail_redirect='/login')
	rows = fetchAll('SELECT * FROM ATIVO')

	stts = fetchAll('SELECT * FROM STATUS')
	ctrs = fetchAll('SELECT * FROM CONTRATO')	

	return template('ativo-list',ativos = rows[0], status = stts[0], contratos = ctrs[0])

@ativoApp.post('/ativo/busca')
def buscaAtivo():
	aaa.require(fail_redirect='/login')
	busca = request.forms.get('busca')
	f_busca = request.forms.get('filtro_busca')
	
	if f_busca == "status":
		sql = 'SELECT * FROM STATUS WHERE DESCRICAO LIKE "%%%s%%"' % (busca)
		stt = fetchOne(sql)[0]
		sql = 'SELECT * FROM ATIVO WHERE ID_STATUS = %s' % (stt['id'])
	elif f_busca == "id":
		sql = 'SELECT * FROM ATIVO WHERE %s = %s ' % (f_busca, busca)
	elif f_busca == "descricao":
		sql = 'SELECT * FROM ATIVO WHERE %s LIKE "%%%s%%" ' % (f_busca, busca)
	elif f_busca == "data_compra":
		sql = 'SELECT * FROM ATIVO WHERE %s = "%s" ' % (f_busca, busca)

	rows = fetchAll(sql)

	stts = fetchAll('SELECT * FROM STATUS')
	ctrs = fetchAll('SELECT * FROM CONTRATO')	

	return template('ativo-linhas',ativos = rows[0], status = stts[0], contratos = ctrs[0])

@ativoApp.route('/ativo/new')
@ativoApp.post('/ativo/new')
def newAtivo():
	aaa.require(fail_redirect='/login')
	stts = fetchAll('SELECT * FROM STATUS')
	ctrs = fetchAll('SELECT * FROM CONTRATO')
	return template('ativo-criar', status = stts[0], contratos = ctrs[0])


@ativoApp.post('/ativo/new/save')
def saveNewAtivo():
	aaa.require(fail_redirect='/login')
	descricao = request.forms.get('desc')
	valor = request.forms.get('valor')
	data_compra = request.forms.get('dt_compra')
	depreciacao = request.forms.get('depreciacao')
	status = request.forms.get('status')
	contrato = request.forms.get('contrato')
	
	sql = "INSERT INTO ATIVO(DESCRICAO, VALOR, DATA_COMPRA, DEPRECIACAO, ID_STATUS, ID_CONTRATO) VALUES('%s','%s','%s','%s','%s','%s')" % (descricao, valor, data_compra, depreciacao, status, contrato)
	
	executeSql(sql)
	
@ativoApp.post('/ativo/update')
def updateAtivo():
	aaa.require(fail_redirect='/login')
	id = request.forms.get('id')

	sql = "SELECT * FROM ATIVO WHERE ID = '%s'" % id
	ativo = fetchOne(sql)

	stts = fetchAll('SELECT * FROM STATUS')
	ctrs = fetchAll('SELECT * FROM CONTRATO')

	return template('ativo-detalhe', ativo = ativo[0], status = stts[0],  contratos = ctrs[0])
	
@ativoApp.post('/ativo/update/save')
def saveUpdatedAtivo():
	aaa.require(fail_redirect='/login')
	id = request.forms.get('id')
	descricao = request.forms.get('desc')
	valor = request.forms.get('valor')
	data_compra = request.forms.get('dt_compra')
	depreciacao = request.forms.get('depreciacao')
	status = request.forms.get('status')
	contrato = request.forms.get('contrato')	

	sql = "UPDATE ATIVO SET DESCRICAO = '%s', VALOR = '%s', DATA_COMPRA = '%s', DEPRECIACAO = '%s', ID_STATUS = '%s', ID_CONTRATO = '%s' WHERE ID = %s" % (descricao, valor, data_compra, depreciacao, status, contrato, id)
	
	executeSql(sql)

@ativoApp.route('/ativo/delete')
@ativoApp.post('/ativo/delete')
def deleteAtivo():
	aaa.require(fail_redirect='/login')
	id = request.forms.get('id')

	sql = "DELETE FROM ATIVO WHERE ID = '%s'" % id
	executeSql(sql)