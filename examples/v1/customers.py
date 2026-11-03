"""Examples for the Customers resource.

Covers creating, retrieving, listing, and managing customer configurations.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customers.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def create_customer():
    """Create a new customer."""
    response = client.v1.customers.create(
        name="Acme Corp",
        # ingest_aliases=["acme-corp", "acme"],  # Aliases for usage events
        # custom_fields={"industry": "SaaS", "tier": "enterprise"},
    )
    print(f"Created customer: {response.data}")


def create_customer_with_billing():
    """Create a customer with billing provider configuration."""
    response = client.v1.customers.create(
        name="Acme Corp",
        billing_config={
            "billing_provider_type": "stripe",
            "billing_provider_customer_id": "cus_abc123",
            "stripe_collection_method": "charge_automatically",
        },
    )
    print(f"Created customer: {response.data}")


def retrieve_customer():
    """Retrieve a single customer by ID."""
    response = client.v1.customers.retrieve(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Customer: {response.data}")


def list_customers():
    """List all customers with auto-pagination."""
    for customer in client.v1.customers.list():
        print(f"Customer: {customer.id} - {customer.name}")


def archive_customer():
    """Archive (soft-delete) a customer."""
    response = client.v1.customers.archive(
        id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Archived customer: {response.data}")


def list_billable_metrics():
    """List billable metrics associated with a customer."""
    for metric in client.v1.customers.list_billable_metrics(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    ):
        print(f"Metric: {metric}")


def list_costs():
    """List costs for a customer over a time period."""
    for cost in client.v1.customers.list_costs(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        starting_on=datetime.fromisoformat("2025-01-01T00:00:00"),
        ending_before=datetime.fromisoformat("2025-02-01T00:00:00"),
    ):
        print(f"Cost: {cost}")


def preview_events():
    """Preview how events would be processed for a customer."""
    response = client.v1.customers.preview_events(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        events=[
            {
                "event_type": "heartbeat",
                "timestamp": "2025-01-01T00:00:00Z",
                "transaction_id": "preview-001",
                "properties": {"cpu_seconds": 60},
            }
        ],
    )
    print(response)


def retrieve_billing_configurations():
    """Retrieve billing provider configurations for a customer."""
    response = client.v1.customers.retrieve_billing_configurations(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(response)


def set_billing_configurations():
    """Set billing provider configurations for a customer."""
    response = client.v1.customers.set_billing_configurations(
        data=[
            {
                "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                "billing_provider": "stripe",
                "delivery_method": "direct_to_billing_provider",
                # configuration={"stripe_customer_id": "cus_abc123"},
            }
        ],
    )
    print(response)


def set_ingest_aliases():
    """Set ingest aliases that can be used to refer to a customer in usage events."""
    client.v1.customers.set_ingest_aliases(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ingest_aliases=["acme-corp", "acme"],
    )
    print("Ingest aliases set successfully")


def set_name():
    """Update the name of a customer."""
    response = client.v1.customers.set_name(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        name="Acme Corporation",
    )
    print(f"Updated customer: {response.data}")


def update_config():
    """Update customer configuration settings."""
    client.v1.customers.update_config(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        leave_stripe_invoices_in_draft=True,
        # salesforce_account_id="001abc123",
    )
    print("Customer config updated")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_customer()
    # create_customer_with_billing()
    # retrieve_customer()
    # list_customers()
    # archive_customer()
    # list_billable_metrics()
    # list_costs()
    # preview_events()
    # retrieve_billing_configurations()
    # set_billing_configurations()
    # set_ingest_aliases()
    # set_name()
    # update_config()
    pass
