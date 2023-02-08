# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-osaoh-wy*f02d*#8der$v#6xp!$la)(6d@xq9xf-z1rey+nqp3'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
