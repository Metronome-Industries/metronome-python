"""Examples for the Customer Credits resource.

Covers creating, listing, and updating end dates for customer credits.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customer_credits.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def create_credit():
    """Create a credit for a customer."""
    response = client.v1.customers.credits.create(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        priority=100.0,
        product_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
        access_schedule={
            "schedule_items": [
                {
                    "amount": 5000.0,
                    "starting_at": "2025-01-01T00:00:00Z",
                    "ending_before": "2026-01-01T00:00:00Z",
                }
            ],
        },
        # name="Promotional Credit",
        # description="Credit for service disruption",
    )
    print(f"Created credit: {response.data}")


def list_credits():
    """List all credits for a customer."""
    for credit in client.v1.customers.credits.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    ):
        print(f"Credit: {credit}")


def update_end_date():
    """Update the end date of a customer's credit."""
    response = client.v1.customers.credits.update_end_date(
        credit_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        access_ending_before=datetime.fromisoformat("2025-12-31T00:00:00"),
    )
    print(f"Updated credit end date: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_credit()
    # list_credits()
    # update_end_date()
    pass
