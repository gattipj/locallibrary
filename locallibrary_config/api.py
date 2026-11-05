# locallibrary_config/api.py
from ninja import NinjaAPI
from ninja.security import django_auth

from chat.api import router as rooms_router
from profiles.api import router as me_router


api = NinjaAPI(auth=django_auth)

api.add_router("/rooms", rooms_router)
api.add_router("/me", me_router)