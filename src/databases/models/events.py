"""File contains events model"""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin


class EventsModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """Database ORM Model for 'events'"""

    # __connection__ = 'NAME'
    __table__ = "events"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    __hidden__ = ["created_at", "updated_at", "deleted_at"]
