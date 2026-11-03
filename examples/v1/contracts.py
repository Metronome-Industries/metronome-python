"""Examples for the Contracts resource.

Covers creating, retrieving, listing, amending, and managing contracts.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/contracts.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def create_contract():
    """Create a new contract for a customer."""
    response = client.v1.contracts.create(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        # ending_before=datetime.fromisoformat("2026-01-01T00:00:00"),  # Optional end date
        # rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        # billing_provider_configuration={
        #     "billing_provider": "stripe",
        #     "delivery_method": "direct_to_billing_provider",
        # },
    )
    print(f"Created contract: {response.data}")


def retrieve_contract():
    """Retrieve a specific contract."""
    response = client.v1.contracts.retrieve(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Contract: {response.data}")


def list_contracts():
    """List all contracts for a customer."""
    response = client.v1.contracts.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Contracts: {response.data}")


def amend_contract():
    """Amend an existing contract (e.g., add commits, overrides, or change terms)."""
    response = client.v1.contracts.amend(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        starting_at=datetime.fromisoformat("2025-06-01T00:00:00"),
    )
    print(f"Amendment: {response.data}")


def archive_contract():
    """Archive a contract."""
    response = client.v1.contracts.archive(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        void_invoices=True,
    )
    print(f"Archived: {response.data}")


def add_manual_balance_entry():
    """Add a manual balance entry to a contract's commit or credit ledger."""
    client.v1.contracts.add_manual_balance_entry(
        id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        amount=1000.0,
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        reason="Manual credit adjustment for overage",
        segment_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print("Manual balance entry added")


def create_historical_invoices():
    """Create historical invoices for a contract."""
    response = client.v1.contracts.create_historical_invoices(
        invoices=[
            {
                "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "exclusive_end_date": datetime.fromisoformat("2025-02-01T00:00:00"),
                "inclusive_start_date": datetime.fromisoformat("2025-01-01T00:00:00"),
                "issue_date": datetime.fromisoformat("2025-02-01T00:00:00"),
            }
        ],
        preview=False,
    )
    print(f"Historical invoices: {response.data}")


def get_net_balance():
    """Get the net balance for a customer's commits and credits."""
    response = client.v1.contracts.get_net_balance(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        # id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  # Specific commit/credit ID
    )
    print(f"Net balance: {response}")


def list_balances():
    """List commit and credit balances for a customer."""
    for balance in client.v1.contracts.list_balances(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        # include_balance=True,  # Include the current balance (may be slower)
        # include_ledgers=True,  # Include ledger entries
    ):
        print(f"Balance: {balance}")


def retrieve_rate_schedule():
    """Retrieve the rate schedule for a contract."""
    response = client.v1.contracts.retrieve_rate_schedule(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        # at=datetime.fromisoformat("2025-06-01T00:00:00"),  # Rates at a specific time
    )
    print(f"Rate schedule: {response.data}")


def retrieve_subscription_quantity_history():
    """Retrieve the quantity history for a subscription on a contract."""
    response = client.v1.contracts.retrieve_subscription_quantity_history(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        subscription_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Subscription quantity history: {response.data}")


def schedule_pro_services_invoice():
    """Schedule a professional services invoice."""
    response = client.v1.contracts.schedule_pro_services_invoice(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        issued_at=datetime.fromisoformat("2025-02-01T00:00:00"),
        line_items=[
            {
                "professional_service_id": "a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
                "amount": 5000.0,
            }
        ],
    )
    print(f"Pro services invoice: {response.data}")


def set_usage_filter():
    """Set a usage filter on a contract to control which events are billable."""
    client.v1.contracts.set_usage_filter(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        group_key="region",
        group_values=["us-east-1", "us-west-2"],
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
    )
    print("Usage filter set")


def update_end_date():
    """Update the end date of a contract."""
    response = client.v1.contracts.update_end_date(
        contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ending_before=datetime.fromisoformat("2025-12-31T00:00:00"),
    )
    print(f"Updated contract end date: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_contract()
    # retrieve_contract()
    # list_contracts()
    # amend_contract()
    # archive_contract()
    # add_manual_balance_entry()
    # create_historical_invoices()
    # get_net_balance()
    # list_balances()
    # retrieve_rate_schedule()
    # retrieve_subscription_quantity_history()
    # schedule_pro_services_invoice()
    # set_usage_filter()
    # update_end_date()
    pass
