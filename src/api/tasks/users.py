"""File contains the UsersTasks container"""
from api.schema.users import UsersSchema


class UsersTasks:
    """Tasks container for the UsersRouter"""

    @staticmethod
    async def do_after(entity: UsersSchema.Users):
        print(f"User.Name: {entity.name}")
