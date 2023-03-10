"""CreateWebhooksTable Migration."""

from masoniteorm.migrations import Migration


class CreateWebhooksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("webhooks") as table:
            table.uuid("uuid").primary()
            table.uuid("vendor_id").foreign("vendor_id").references("uuid").on(
                "vendors"
            ).on_delete("cascade")

            table.text("name", length=128, nullable=True)
            table.text("hook_url")
            table.json("meta", nullable=True)

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("webhooks")
