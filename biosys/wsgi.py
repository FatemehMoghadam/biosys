"""
WSGI config for biosys project.
It exposes the WSGI callable as a module-level variable named ``application``.
"""
from __future__ import absolute_import, unicode_literals, print_function, division

import os

import confy
from django.core.wsgi import get_wsgi_application

from pathlib import Path


d = Path(__file__).resolve().parents[1]
dot_env = os.path.join(str(d), '.env')
if os.path.exists(dot_env):
	confy.read_environment_file(dot_env)


from dj_static import Cling, MediaCling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biosys.settings")
application = Cling(MediaCling(get_wsgi_application()))
