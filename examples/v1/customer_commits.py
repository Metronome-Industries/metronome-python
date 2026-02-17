"""Examples for the Customer Commits resource.

Covers creating, listing, and updating end dates for customer commits.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customer_commits.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def create_commit():
    """Create a prepaid commit for a customer."""
    response = client.v1.customers.commits.create(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        type="PREPAID",
        priority=100.0,
        product_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
        access_schedule={
            "schedule_items": [
                {
                    "amount": 10000.0,
                    "starting_at": "2025-01-01T00:00:00Z",
                    "ending_before": "2026-01-01T00:00:00Z",
                }
            ],
        },
        # invoice_schedule={  # Optional invoice schedule
        #     "schedule_items": [
        #         {
        #             "timestamp": "2025-01-01T00:00:00Z",
        #             "amount": 10000.0,
        #         }
        #     ],
        # },
        # name="Annual Prepaid Commit",
        # description="Annual prepaid commitment for API usage",
    )
    print(f"Created commit: {response.data}")


def list_commits():
    """List all commits for a customer."""
    for commit in client.v1.customers.commits.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    ):
        print(f"Commit: {commit}")


def update_end_date():
    """Update the end date of a customer's commit."""
    response = client.v1.customers.commits.update_end_date(
        commit_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        # access_ending_before=datetime.fromisoformat("2025-12-31T00:00:00"),
        # invoices_ending_before=datetime.fromisoformat("2025-12-31T00:00:00"),
    )
    print(f"Updated commit end date: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_commit()
    # list_commits()
    # update_end_date()
    pass
