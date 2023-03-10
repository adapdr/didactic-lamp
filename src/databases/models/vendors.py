"""File contains vendors model"""
from masoniteorm.models import Model
from masoniteorm.relationships import has_many
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin


class VendorsModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """Database ORM Model for 'vendors'"""

    # __connection__ = 'NAME'
    __table__ = "vendors"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    __hidden__ = ["created_at", "updated_at", "deleted_at"]

    @has_many("uuid", "webhook_id")
    def webhooks(self):
        from databases.models.webhooks import WebhooksModel

        return WebhooksModel

    @has_many("uuid", "campaign_id")
    def campaigns(self):
        from databases.models.campaigns import CampaignsModel

        return CampaignsModel
