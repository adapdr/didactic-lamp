"""File contains the UsersService class."""
from typing import List

from api.schema.users import Users, UsersList
from databases.models import Models


class UsersService:
    """Service class for the UsersRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Users):
        """Creates a `Users` Entity from data"""
        result = Models.users.create(data.with_secrets()).fresh()
        return Users.from_orm(result)

    def retrieve(self, uuid: str) -> Users:
        """Retrieves a `Users` Entity by uuid"""
        result = Models.users.find(uuid)
        return Users.from_orm(result)

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Users]:
        """Retrieves a `Users` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.users.where(query).simple_paginate(limit, page_nr)
        return UsersList(**result.serialize()).data

    def update(self, uuid: str, data: Users) -> Users:
        """Updates a `Users` Entity by uuid with data"""
        result = Models.users.where({"uuid": uuid}).update(data.dict()).get()
        return Users.from_orm(result)

    def replace(self, uuid: str, data: Users) -> Users:
        """Replaces a `Users` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Users:
        """Delete a `Users` Entity by uuid"""
        result = Models.users.delete(uuid)
        return Users.from_orm(result)

    def deleted(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Users]:
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        query.update({"deleted_at": None})
        result = (
            Models.users.where(query).with_trashed().simple_paginate(limit, page_nr)
        )
        return UsersList(**result.serialize()).data
