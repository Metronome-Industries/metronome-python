"""Examples for the Credit Grants resource.

Covers creating, listing, editing, voiding credit grants, and listing ledger entries.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/credit_grants.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def create_credit_grant():
    """Create a new credit grant for a customer."""
    response = client.v1.credit_grants.create(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        name="Promotional Credit",
        priority=100.0,
        expires_at=datetime.fromisoformat("2026-01-01T00:00:00"),
        grant_amount={
            "amount": 5000.0,
            "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        },
        paid_amount={
            "amount": 0.0,
            "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        },
        # reason="Sign-up bonus",
    )
    print(f"Created credit grant: {response.data}")


def list_credit_grants():
    """List all credit grants with auto-pagination."""
    for grant in client.v1.credit_grants.list(
        # customer_ids=["13117714-3f05-48e5-a6e9-a66093f13b4d"],  # Filter by customer
    ):
        print(f"Credit grant: {grant}")


def edit_credit_grant():
    """Edit an existing credit grant (e.g., change expiration)."""
    response = client.v1.credit_grants.edit(
        id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        # expires_at=datetime.fromisoformat("2026-06-01T00:00:00"),
        # name="Updated Credit Grant",
    )
    print(f"Edited credit grant: {response.data}")


def list_entries():
    """List credit ledger entries showing how credits were used."""
    for entry in client.v1.credit_grants.list_entries(
        # customer_ids=["13117714-3f05-48e5-a6e9-a66093f13b4d"],
    ):
        print(f"Ledger entry: {entry}")


def void_credit_grant():
    """Void a credit grant, removing any remaining balance."""
    response = client.v1.credit_grants.void(
        id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Voided credit grant: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_credit_grant()
    # list_credit_grants()
    # edit_credit_grant()
    # list_entries()
    # void_credit_grant()
    pass
