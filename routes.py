#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
from bottle import route, run, template, redirect, request

from beaker.middleware import SessionMiddleware

from home import *
from usuarios import *
from ativos import *
from status import *
from login import *
from contratos import *
from authentication import *

app = Bottle()

app.merge(homeApp);
app.merge(userApp)
app.merge(ativoApp)
app.merge(statusApp)
app.merge(loginApp)
app.merge(contratosApp)

app = SessionMiddleware(app, session_opts)

bottle.run(app=app, quiet=False, reloader=True)