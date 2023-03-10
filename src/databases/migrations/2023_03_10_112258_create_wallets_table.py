"""CreateWalletsTable Migration."""

from masoniteorm.migrations import Migration


class CreateWalletsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("wallets") as table:
            table.uuid("uuid").primary()
            table.text("name", length=32, nullable=True)
            table.text("address", length=64)

            table.uuid("user_id").foreign("user_id").references("uuid").on(
                "users"
            ).on_delete("cascade")

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("wallets")
