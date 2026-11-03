"""Examples for the Usage resource.

Covers ingesting usage events and querying aggregated usage data.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/usage.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def ingest_usage():
    """Send usage events to Metronome."""
    client.v1.usage.ingest(
        usage=[
            {
                "transaction_id": "90e9401f-0f8c-4cd3-9a9f-d6beb56d8d72",
                "customer_id": "team@example.com",
                "event_type": "heartbeat",
                "timestamp": "2025-01-01T00:00:00Z",
                "properties": {
                    "cluster_id": "42",
                    "cpu_seconds": 60,
                    "region": "Europe",
                },
            }
        ],
    )
    print("Usage event ingested successfully")


def ingest_multiple_events():
    """Send multiple usage events in a single batch."""
    client.v1.usage.ingest(
        usage=[
            {
                "transaction_id": "event-001",
                "customer_id": "team@example.com",
                "event_type": "api_call",
                "timestamp": "2025-01-01T00:00:00Z",
                "properties": {"endpoint": "/v1/data", "response_ms": 120},
            },
            {
                "transaction_id": "event-002",
                "customer_id": "team@example.com",
                "event_type": "api_call",
                "timestamp": "2025-01-01T00:01:00Z",
                "properties": {"endpoint": "/v1/query", "response_ms": 250},
            },
        ],
    )
    print("Batch of usage events ingested successfully")


def list_usage():
    """Query aggregated usage data for a time period."""
    for usage in client.v1.usage.list(
        starting_on=datetime.fromisoformat("2025-01-01T00:00:00"),
        ending_before=datetime.fromisoformat("2025-02-01T00:00:00"),
        window_size="DAY",
        # customer_ids=["13117714-3f05-48e5-a6e9-a66093f13b4d"],  # Filter by customer
    ):
        print(usage)


def list_usage_with_groups():
    """Query usage data grouped by a specific property."""
    for usage in client.v1.usage.list_with_groups(
        billable_metric_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        window_size="DAY",
        # starting_on="2025-01-01T00:00:00Z",
        # ending_before="2025-02-01T00:00:00Z",
        # group_by={"key": "region"},  # Group results by region property
    ):
        print(usage)


def search_events():
    """Search for specific usage events by transaction ID."""
    response = client.v1.usage.search(
        transaction_ids=[
            "90e9401f-0f8c-4cd3-9a9f-d6beb56d8d72",
            "event-001",
        ],
    )
    print(response)


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # ingest_usage()
    # ingest_multiple_events()
    # list_usage()
    # list_usage_with_groups()
    # search_events()
    pass
