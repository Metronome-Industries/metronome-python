"""Examples for the Billable Metrics resource.

Covers creating, retrieving, listing, and archiving billable metrics.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/billable_metrics.py
"""

from metronome import Metronome

client = Metronome()


def create_billable_metric():
    """Create a new billable metric using aggregation."""
    response = client.v1.billable_metrics.create(
        name="CPU Seconds",
        aggregation_type="SUM",
        aggregation_key="cpu_seconds",
        event_type_filter={"in_values": ["heartbeat"]},
        # group_keys=[["region"]],  # Group usage by region
        # property_filters=[{"name": "cluster_id", "exists": True}],
    )
    print(f"Created billable metric: {response.data}")


def create_billable_metric_with_sql():
    """Create a billable metric using a SQL query."""
    response = client.v1.billable_metrics.create(
        name="Active Users",
        sql="SELECT COUNT(DISTINCT user_id) as value FROM events WHERE event_type = 'login'",
    )
    print(f"Created billable metric: {response.data}")


def retrieve_billable_metric():
    """Retrieve a specific billable metric by ID."""
    response = client.v1.billable_metrics.retrieve(
        billable_metric_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
    )
    print(f"Billable metric: {response.data}")


def list_billable_metrics():
    """List all billable metrics with auto-pagination."""
    for metric in client.v1.billable_metrics.list():
        print(f"Metric: {metric}")


def archive_billable_metric():
    """Archive a billable metric."""
    response = client.v1.billable_metrics.archive(
        id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
    )
    print(f"Archived: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_billable_metric()
    # create_billable_metric_with_sql()
    # retrieve_billable_metric()
    # list_billable_metrics()
    # archive_billable_metric()
    pass
