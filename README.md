# LibrePCB API

The API is implemented with Django REST Framework on Python 3.

## Setup

Create a virtualenv:

    python3 -m venv VIRTUAL

Export some environment variables:

    echo 'export DJANGO_DEBUG=true' >> VIRTUAL/bin/activate
    echo 'export DATABASE_URL=postgres:///librepcb-api' >> VIRTUAL/bin/activate

Enable virtualenv:

    source VIRTUAL/bin/activate

Install dependencies:

    pip install -r requirements.txt

Create a database:

    createdb librepcb-api

Initialize database:

    src/manage.py migrate

Create a superuser:

    src/manage.py createsuperuser

Start the development server:

    src/manage.py runserver

The server is now running on `http://localhost:8000/`.

## License

GPLv3, see `LICENSE` file.
