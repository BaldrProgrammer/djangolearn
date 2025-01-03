if __name__ == '__main__':
    import os
    import django
    from django.conf import settings

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')  # Путь к вашему settings.py

    settings.configure(
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'products',
        ],
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
    )

    django.setup()  # Инициализация приложений
