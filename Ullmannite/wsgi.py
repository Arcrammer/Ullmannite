"""
WSGI config for Ullmannite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/var/www/Ullmannite")
sys.path.append("/var/www/Ullmannite/Ullmannite")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ullmannite.settings_production")

application = get_wsgi_application()
