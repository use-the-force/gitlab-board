FROM node:16-alpine3.15

WORKDIR /usr/src/app

COPY ./board/frontend .
COPY ./docker/frontend ./docker
COPY ./.env.example .

RUN set -eux \
    && chmod +x /usr/src/app/docker/entrypoint.sh \
    && npm i \
    && npm run build

ENTRYPOINT ["/usr/src/app/docker/entrypoint.sh"]
