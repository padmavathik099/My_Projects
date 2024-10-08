"""
WSGI config for diabetespredict project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'env', 'lib', 'site-packages'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetespredict.settings')

application = get_wsgi_application()

