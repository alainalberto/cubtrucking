# -*- coding: utf-8 -*-
from __future__ import unicode_literals

chdir = "/home/ubuntu/workshop-deploying-django/main"
bind = "unix:/home/ubuntu/main.sock"
env = 'DJANGO_SETTINGS_MODULE="main.settings.production"'
workers = 2
