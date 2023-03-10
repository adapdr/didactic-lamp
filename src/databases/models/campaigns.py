"""File contains campaigns model"""
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin


class CampaignsModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """Database ORM Model for 'campaigns'"""

    # __connection__ = 'NAME'
    __table__ = "campaigns"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    __hidden__ = ["created_at", "updated_at", "deleted_at"]

    @belongs_to("vendor_id", "uuid")
    def vendor(self):
        from databases.models.vendors import VendorsModel

        return VendorsModel
