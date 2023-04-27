gitlab-board
=============

Extended kanban board application for GitLab Community Edition. It provides kanban board by assignee, grouped by teams.

.. image:: demo.gif

Requirements
-------------------

The application requires three scoped labels:

- Status::{name} - status labels
- Priority::{name} - priority labels
- Task::{name} - task type

Installation
-------------------

1. Configure environments
^^^^^^^^^^^^^^^^^^^

Copy `.env.example` and name it `.env`. Most environment variables are already set, but some still need to be filled in.

::

    SECRET_KEY=[generate your own]
    JWT_SECRET=[generate your own]
    DATABASE_PASSWORD=[generate your own]
    POSTGRES_PASSWORD==[same as DATABASE_PASSWORD]
    VITE_GITLAB_API_URL=[gitlab api url]
    VITE_GITLAB_API_TOKEN=[gitlab api token]


2. Build images
^^^^^^^^^^^^^^^^^^^

Run next command

::

    docker-compose build

.. note::
   You will need to push images for production usage.

3. Configure Nginx
^^^^^^^^^^^^^^^^^^^

Nginx is used as reverse proxy. Copy `nginx/board.conf` to `/etc/nginx/conf.d`.

Board will be available at http://localhost:8000.

.. warning::
   DO NOT use it in your production! `nginx/board.conf` is minimal configuration for development.

4. Deploying via docker-compose
^^^^^^^^^^^^^^^^^^^

Run next command

::

    docker-compose up -d

Advanced
-------------------
Customization
^^^^^^^^^^^^^^^^^^^

Custom Logo

The default logo can be changed. Add an `VITE_LOGO_URL` environment variable with image path.

Configuration
^^^^^^^^^^^^^^^^^^^

Frontend environment variables
`````````````

VITE_BOARD_API_URL
'''''''''''''
Required

GitLab Board API URL.

VITE_GITLAB_API_URL
'''''''''''''
Required

GitLab API URL.

VITE_GITLAB_API_TOKEN
'''''''''''''
Required

GitLab API Token.

VITE_LOGO_URL
'''''''''''''
Optional

Logo URL. If not specified, the default logo is taken.

API environment variables
`````````````

DEPLOYMENT_ENVIRONMENT
'''''''''''''
Required

Deployment environment. Can be `PROD` or `LOCAL`.

By default `PROD`.

SECRET_KEY
'''''''''''''
Required

A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

See https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key.

JWT_SECRET
'''''''''''''
Required

This is the secret key used to sign the JWT. Make sure this is safe and not shared or public.

CSRF_TRUSTED_ORIGINS
'''''''''''''
Required

A list of trusted origins for unsafe requests (e.g. POST).

See https://docs.djangoproject.com/en/4.1/ref/settings/#csrf-trusted-origins.

CORS_ALLOWED_ORIGINS
'''''''''''''
Required

A list of origins that are authorized to make cross-site HTTP requests.

DATABASE_HOST
'''''''''''''
Required

Database host.

DATABASE_PORT
'''''''''''''
Required

Database port.

DATABASE_NAME
'''''''''''''
Required

Database name.

DATABASE_USER
'''''''''''''
Required

Database user.

DATABASE_PASSWORD
'''''''''''''
Required

Database password.

TIME_ZONE
'''''''''''''
Required

Time zone database name. (e.g `Europe/Berlin`).

LANGUAGE_CODE
'''''''''''''
Optional

ISO 639-1 standard language codes (e.g `ja`). By default `en-us`.
