"""File contains seeder for the 'users' table"""
from uuid import uuid4

from masoniteorm.seeds import Seeder

from databases.models import UsersModel


class UsersTableSeeder(Seeder):
    """Seeder for the 'users' table"""

    def run(self):
        """Run the database seeds."""
        UsersModel.create({"uid": uuid4(), "name": "John Doe"})
