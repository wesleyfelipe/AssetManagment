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

loginApp = Bottle()

@loginApp.route('/')
@loginApp.post('/')
@loginApp.route('/login')
@loginApp.post('/login')
def login():
	return template('login')

@loginApp.post('/login/confirm')
def loginConfirm():
	username = request.forms.get('username')
	password = request.forms.get('senha')
	success = aaa.login(username, password)
	if(success):
		return '{"authenticated":"true"}'
	return '{"authenticated":"false"}'

@loginApp.route('/logout')
@loginApp.post('/logout')
def logout():
    aaa.logout(success_redirect='/login')