"""Examples for the Contract Named Schedules resource.

Covers retrieving and updating named schedules on contracts.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/contract_named_schedules.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def retrieve_named_schedule():
    """Retrieve a named schedule for a contract."""
    response = client.v1.contracts.named_schedules.retrieve(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        schedule_name="my-schedule",
    )
    print(f"Named schedule: {response.data}")


def update_named_schedule():
    """Update a named schedule on a contract."""
    client.v1.contracts.named_schedules.update(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        schedule_name="my-schedule",
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        value={"custom_field": "custom_value"},
        # ending_before=datetime.fromisoformat("2026-01-01T00:00:00"),
    )
    print("Contract named schedule updated")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # retrieve_named_schedule()
    # update_named_schedule()
    pass
