"""CreateBehavioursTable Migration."""

from masoniteorm.migrations import Migration


class CreateBehavioursTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("behaviours") as table:
            table.uuid("uuid").primary()
            table.text("name", nullable=True)
            table.text("address")

            table.uuid("user_id").foreign("user_id").references("uuid").on(
                "users"
            ).on_delete("cascade")

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("behaviours")
