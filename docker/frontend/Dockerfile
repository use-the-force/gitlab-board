FROM node:16-alpine3.15

WORKDIR /usr/src/app

COPY ./board/frontend /usr/src/app
COPY ./docker/frontend/entrypoint.sh .
COPY ./.env.example .

RUN set -eux \
    && chmod +x /usr/src/app/entrypoint.sh \
    && npm i \
    && npm run build

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
