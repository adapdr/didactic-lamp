"""CreateVendorsTable Migration."""

from masoniteorm.migrations import Migration


class CreateVendorsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("vendors") as table:
            table.uuid("uuid").primary()
            table.text("name", length=128)

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("vendors")
