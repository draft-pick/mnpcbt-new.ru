# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1235053/data/www/mnpcbt-new.ru/mnpcbtProjectNew')
sys.path.insert(1, '/var/www/u1235053/data/mnpcbtPrvenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mnpcbtProjectNew.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()