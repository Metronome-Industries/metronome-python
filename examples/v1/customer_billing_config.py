"""Examples for the Customer Billing Config resource.

Covers creating, retrieving, and deleting billing provider configurations for customers.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customer_billing_config.py
"""

from metronome import Metronome

client = Metronome()


def create_billing_config():
    """Create a billing configuration for a customer."""
    client.v1.customers.billing_config.create(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        billing_provider_type="stripe",
        billing_provider_customer_id="cus_abc123",
    )
    print("Billing config created")


def retrieve_billing_config():
    """Retrieve a customer's billing configuration for a specific provider."""
    response = client.v1.customers.billing_config.retrieve(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        billing_provider_type="stripe",
    )
    print(f"Billing config: {response.data}")


def delete_billing_config():
    """Delete a customer's billing configuration for a specific provider."""
    client.v1.customers.billing_config.delete(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        billing_provider_type="stripe",
    )
    print("Billing config deleted")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_billing_config()
    # retrieve_billing_config()
    # delete_billing_config()
    pass
