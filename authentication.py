#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cork import Cork
from cork.backends import SQLiteBackend

def populate_backend():
    b = SQLiteBackend('asset-system.db', initialize=False)
    return b

b = populate_backend()
aaa = Cork(backend=b)

session_opts = {
    'session.cookie_expires': True,
    'session.encrypt_key': 'please use a random key and keep it secret!',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
}

