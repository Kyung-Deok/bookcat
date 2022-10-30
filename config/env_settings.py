import pymysql

SECRET_KEY = 'django-insecure-^p2o*qw674)&*tf9qh53g*t^$6qehh8bupne&9qlw8p1_l&7p3'

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root',
        'PASSWORD': '9941',
        'HOST': '127.0.0.1',
        'PORT': '3307',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

CERT_KEY = '9B5ECDD9AF5A32F5973EAC757CB6F1256C686473954F652396AEBF9E1AEDB253'

ALGORITHM = 'HS256'