"""Examples for the Customer Named Schedules resource.

Covers retrieving and updating named schedules for customers.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customer_named_schedules.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def retrieve_named_schedule():
    """Retrieve a named schedule for a customer."""
    response = client.v1.customers.named_schedules.retrieve(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        schedule_name="my-schedule",
    )
    print(f"Named schedule: {response.data}")


def update_named_schedule():
    """Update a named schedule for a customer."""
    client.v1.customers.named_schedules.update(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        schedule_name="my-schedule",
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        value={"discount_percentage": 10},
        # ending_before=datetime.fromisoformat("2026-01-01T00:00:00"),
    )
    print("Named schedule updated")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # retrieve_named_schedule()
    # update_named_schedule()
    pass
