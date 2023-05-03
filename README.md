[![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Github CI](https://github.com/use-the-force/gitlab-board/actions/workflows/ci.yml/badge.svg?branch=main)
![Read the Docs](https://img.shields.io/readthedocs/gitlab-board)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# gitlab-board

Extended kanban board application for GitLab Community Edition. It provides kanban board by assignee, grouped by teams.

See the docs at [readthedocs.io](https://gitlab-board.readthedocs.io/en/latest).

![Demo](docs/source/demo.gif)

## Requirements

The application requires three scoped labels:

- Status::{name} - status labels
- Priority::{name} - priority labels
- Type::{name} - task type

## Installation

### 1. Configure environments

Copy `.env.example` and name it `.env`. Most environment variables are already set, but some still need to be filled in.

```
SECRET_KEY=[generate your own]
JWT_SECRET=[generate your own]
DATABASE_PASSWORD=[generate your own]
POSTGRES_PASSWORD==[same as DATABASE_PASSWORD]
VITE_GITLAB_API_URL=[gitlab api url]
VITE_GITLAB_API_TOKEN=[gitlab api token]
```


### 2. Build images

Run next command

```
docker-compose build
```

> **_Note:_**  You will need to push images for production usage.

### 3. Configure Nginx

Nginx is used as reverse proxy. Copy `nginx/board.conf` to `/etc/nginx/conf.d`.

Board will be available at http://localhost:8000.

> **_Warning:_** DO NOT use it in your production! `nginx/board.conf` is minimal configuration for development.

### 4. Deploying via docker-compose

Run next command

```
docker-compose up -d
```
