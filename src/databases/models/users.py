"""File contains users model"""
from masoniteorm.models import Model
from masoniteorm.relationships import has_one, has_many
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin

from databases.observers.users import UsersObserver


class UsersModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """Database ORM Model for 'users'"""

    # __connection__ = 'NAME'
    __table__ = "users"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    __hidden__ = ["uuid", "created_at", "updated_at", "deleted_at"]

    @has_many("uuid", "user_id")
    def wallets(self):
        from databases.models.wallets import WalletsModel

        return WalletsModel

    @has_many("uuid", "user_id")
    def traits(self):
        from databases.models.traits import TraitsModel

        return TraitsModel

    @has_one("uuid", "user_id")
    def behaviours(self):
        from databases.models.behaviours import BehavioursModel

        return BehavioursModel

    @has_one("uuid", "user_id")
    def preferences(self):
        from databases.models.preferences import PreferencesModel

        return PreferencesModel


UsersModel.observe(UsersObserver())
