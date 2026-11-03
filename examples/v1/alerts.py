"""Examples for the Alerts resource.

Covers creating and archiving threshold alerts.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/alerts.py
"""

from metronome import Metronome

client = Metronome()


def create_alert():
    """Create a threshold alert that fires when a condition is met."""
    response = client.v1.alerts.create(
        alert_type="spend_threshold_reached",
        name="High Spend Alert",
        threshold=10000.0,
        # customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",  # Specific customer (omit for all)
        # evaluate_on_create=True,  # Evaluate immediately for existing customers
    )
    print(f"Created alert: {response.data}")


def create_usage_alert():
    """Create an alert that fires when usage reaches a threshold."""
    response = client.v1.alerts.create(
        alert_type="usage_threshold_reached",
        name="API Usage Alert",
        threshold=1000000.0,
        billable_metric_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
    )
    print(f"Created usage alert: {response.data}")


def create_low_credit_alert():
    """Create an alert that fires when credit balance drops below a threshold."""
    response = client.v1.alerts.create(
        alert_type="low_credit_balance_reached",
        name="Low Credit Balance",
        threshold=500.0,
    )
    print(f"Created credit alert: {response.data}")


def archive_alert():
    """Archive an alert."""
    response = client.v1.alerts.archive(
        id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Archived alert: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_alert()
    # create_usage_alert()
    # create_low_credit_alert()
    # archive_alert()
    pass
