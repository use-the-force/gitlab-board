FROM python:3.10.10-alpine3.16 as build

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.2.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

ADD ./board/api/pyproject.toml .
ADD ./board/api/poetry.lock .

RUN apk add --no-cache --virtual build-base g++ gcc libffi-dev python3-dev \
    && pip install --no-cache-dir poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.create false \
    && poetry install --without dev

FROM build

WORKDIR /usr/src/app

COPY ./board/api .
COPY ./docker/api/entrypoint.sh .
COPY ./.env.example .

ENV SECRET_KEY=build
ENV JWT_SECRET=build
ENV TIME_ZONE=Europe/Moscow
ENV CORS_ALLOWED_ORIGINS=*
ENV CSRF_TRUSTED_ORIGINS=*

RUN set -ex \
    && chmod +x /usr/src/app/entrypoint.sh \
    && /usr/src/app/manage.py collectstatic --noinput --clear \
    && mkdir /srv/www/htdocs/media

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
