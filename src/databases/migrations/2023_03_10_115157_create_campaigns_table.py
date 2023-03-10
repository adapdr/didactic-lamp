"""CreateCampaignsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCampaignsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("campaigns") as table:
            table.uuid("uuid").primary()
            table.text("name", length=128)
            table.uuid("vendor_id").foreign("vendor_id").references("uuid").on(
                "vendors"
            ).on_delete("cascade")
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("campaigns")
