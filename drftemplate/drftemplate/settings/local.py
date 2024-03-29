from .base import *
from dotenv import load_dotenv
import os



load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': 'djangorest',
            'USER': 'HARSHA\Dell',
            'HOST': 'HARSHA\\SQLEXPRESS',
            'PASSWORD': '',
            'PORT': '',

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
                'extra_params': 'Trusted_Connection=yes',
            },
        },
    }