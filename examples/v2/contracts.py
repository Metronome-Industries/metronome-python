"""Examples for the V2 Contracts resource.

Covers retrieving, listing, editing contracts, and editing commits and credits using the V2 API.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v2/contracts.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def retrieve_contract():
    """Retrieve a specific contract using the V2 API."""
    response = client.v2.contracts.retrieve(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Contract: {response.data}")


def list_contracts():
    """List all contracts for a customer using the V2 API."""
    response = client.v2.contracts.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Contracts: {response.data}")


def edit_contract():
    """Edit a contract (e.g., add commits, update subscriptions, change end date)."""
    response = client.v2.contracts.edit(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        # ending_before=datetime.fromisoformat("2026-01-01T00:00:00"),  # Update end date
        # add_commits=[...],  # Add new commits
        # update_commits=[...],  # Update existing commits
        # add_credits=[...],  # Add new credits
    )
    print(f"Edited contract: {response.data}")


def edit_commit():
    """Edit a specific commit on a contract."""
    response = client.v2.contracts.edit_commit(
        commit_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        # name="Updated Commit Name",
        # description="Updated description",
        # access_schedule={  # Modify the access schedule
        #     "add_schedule_items": [
        #         {
        #             "amount": 5000.0,
        #             "starting_at": "2025-07-01T00:00:00Z",
        #             "ending_before": "2026-01-01T00:00:00Z",
        #         }
        #     ],
        # },
    )
    print(f"Edited commit: {response.data}")


def edit_credit():
    """Edit a specific credit on a contract."""
    response = client.v2.contracts.edit_credit(
        credit_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        # name="Updated Credit Name",
        # description="Updated description",
        # access_schedule={  # Modify the access schedule
        #     "add_schedule_items": [
        #         {
        #             "amount": 2000.0,
        #             "starting_at": "2025-07-01T00:00:00Z",
        #             "ending_before": "2026-01-01T00:00:00Z",
        #         }
        #     ],
        # },
    )
    print(f"Edited credit: {response.data}")


def get_edit_history():
    """Get the edit history for a contract."""
    response = client.v2.contracts.get_edit_history(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Edit history: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # retrieve_contract()
    # list_contracts()
    # edit_contract()
    # edit_commit()
    # edit_credit()
    # get_edit_history()
    pass
