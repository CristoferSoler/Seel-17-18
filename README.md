# Systementwicklung für ein Entwicklungsland

### SETUP SOFTWARE PROJECT TO USE REMOTE DB
##### to use remote DB, first install psycopg2
    sudo apt-get build-dep python-psycopg2
##### then go into your virtual environment and run
    pip install psycopg2

##### make configuration in settings.py (for 'DATABASES'):
    DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fordjango',
            'USER': 'django',
            'PASSWORD': 'django',
            'HOST': 'localhost',
            'PORT': '1234',
        }
    }
##### then use a ssh tunneling to connect
    ssh -N -L 1234:localhost:5432 ec2-user@18.194.158.20
##### now you can run your webserver locally with the remote DB

