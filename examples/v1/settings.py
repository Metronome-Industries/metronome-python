"""Examples for the Settings resource and Billing Providers sub-resource.

Covers managing Avalara credentials and billing provider configurations.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/settings.py
"""

from metronome import Metronome

client = Metronome()


# ============================================================================
# Settings
# ============================================================================


def upsert_avalara_credentials():
    """Create or update Avalara tax provider credentials."""
    response = client.v1.settings.upsert_avalara_credentials(
        avalara_environment="production",
        avalara_password="your-avalara-password",
        avalara_username="your-avalara-username",
        delivery_method_ids=["a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d"],
    )
    print(f"Avalara credentials: {response}")


# ============================================================================
# Billing Providers
# ============================================================================


def create_billing_provider():
    """Set up a billing provider configuration."""
    response = client.v1.settings.billing_providers.create(
        billing_provider="stripe",
        delivery_method="direct_to_billing_provider",
        configuration={
            "stripe_api_key": "sk_live_...",
        },
    )
    print(f"Created billing provider: {response}")


def list_billing_providers():
    """List all configured billing providers."""
    response = client.v1.settings.billing_providers.list()
    print(f"Billing providers: {response}")


if __name__ == "__main__":
    # Uncomment the example you want to run:

    # Settings
    # upsert_avalara_credentials()

    # Billing Providers
    # create_billing_provider()
    # list_billing_providers()
    pass
