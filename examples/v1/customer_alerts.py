"""Examples for the Customer Alerts resource.

Covers retrieving, listing, and resetting customer-specific alerts.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customer_alerts.py
"""

from metronome import Metronome

client = Metronome()


def retrieve_alert():
    """Retrieve a specific alert for a customer."""
    response = client.v1.customers.alerts.retrieve(
        alert_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print(f"Alert: {response.data}")


def list_alerts():
    """List all alerts for a customer."""
    for alert in client.v1.customers.alerts.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    ):
        print(f"Alert: {alert}")


def reset_alert():
    """Reset an alert for a customer, re-evaluating the alert condition."""
    client.v1.customers.alerts.reset(
        alert_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    )
    print("Alert reset successfully")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # retrieve_alert()
    # list_alerts()
    # reset_alert()
    pass
