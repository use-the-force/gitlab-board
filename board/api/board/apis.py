from ninja import NinjaAPI

from apps.authentication.apis import router as auth_router
from apps.teams.apis import router as teams_router
from apps.users.apis import router as users_router

api = NinjaAPI(version='1', csrf=True)

api.add_router('auth/', auth_router)
api.add_router('users/', users_router)
api.add_router('teams/', teams_router)
