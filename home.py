#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle
from bottle import route, run, template, redirect, request, static_file
import sys
import datetime
import json

from authentication import *

homeApp = Bottle()

@homeApp.route('/css/<filename>')
def static_css(filename):
	return static_file(filename, root='views/css')

@homeApp.route('/js/<filename>')
def static_css(filename):
	return static_file(filename, root='views/js')

@homeApp.route('/home')
@homeApp.post('/home')
def home():
	aaa.require(fail_redirect='/login')
	return template('home', role=aaa.current_user.role)