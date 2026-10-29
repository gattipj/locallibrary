from ninja import ModelSchema
from ninja import Schema
from chat.models import Room
from typing import Annotated

from ninja import FilterLookup, FilterSchema

from django.shortcuts import get_object_or_404

class RoomIn(ModelSchema):
    class Meta:
        model = Room
        fields = ["name", "topic"]


class RoomOut(ModelSchema):
    class Meta:
        model = Room
        fields = ["id", "name", "topic", "created_at"]

class Conflict(Schema):
    message: str
    existing_id: int

class RoomFilter(FilterSchema):
    search: Annotated[str | None, FilterLookup("name__icontains")] = None
    topic: Annotated[str | None, FilterLookup("topic__icontains")] = None
    recent: bool | None = None

class MessageIn(ModelSchema):
    class Meta:
        model = Message
        fields = ["content"]


class MessageOut(ModelSchema):
    room: RoomOut

    class Meta:
        model = Message
        fields = ["id", "author", "content", "created_at"]