"""Examples for the Custom Fields resource.

Covers adding keys, setting values, listing keys, deleting values, and removing keys.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/custom_fields.py
"""

from metronome import Metronome

client = Metronome()


def add_key():
    """Add a custom field key to an entity type."""
    client.v1.custom_fields.add_key(
        enforce_uniqueness=True,
        entity="customer",
        key="salesforce_id",
    )
    print("Custom field key added")


def set_values():
    """Set custom field values on a specific entity."""
    client.v1.custom_fields.set_values(
        custom_fields={"salesforce_id": "SF-12345", "industry": "Technology"},
        entity="customer",
        entity_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print("Custom field values set")


def list_keys():
    """List all custom field keys."""
    for key in client.v1.custom_fields.list_keys(
        # entity="customer",  # Filter by entity type
    ):
        print(f"Custom field key: {key}")


def delete_values():
    """Delete custom field values from an entity."""
    client.v1.custom_fields.delete_values(
        entity="customer",
        entity_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        keys=["salesforce_id"],
    )
    print("Custom field values deleted")


def remove_key():
    """Remove a custom field key from an entity type."""
    client.v1.custom_fields.remove_key(
        entity="customer",
        key="salesforce_id",
    )
    print("Custom field key removed")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # add_key()
    # set_values()
    # list_keys()
    # delete_values()
    # remove_key()
    pass
