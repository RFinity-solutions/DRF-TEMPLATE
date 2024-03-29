from .base import *


from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': os.environ.get("DB_NAME"),
            'USER': os.environ.get("DB_USER"),
            'HOST': os.environ.get("DB_HOST"),
            'PASSWORD': os.environ.get("DB_PASSWORD"),
            'PORT': os.environ.get("DB_PORT"),

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
                'extra_params': 'Trusted_Connection=yes',
            },
        },
    }


ALLOWED_HOSTS = ['*']
