"""Examples for the Audit Logs resource.

Covers listing audit log entries.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/audit_logs.py
"""

from metronome import Metronome

client = Metronome()


def list_audit_logs():
    """List audit log entries with auto-pagination."""
    for log in client.v1.audit_logs.list(
        # starting_on="2025-01-01T00:00:00Z",  # Filter by date range
        # ending_before="2025-02-01T00:00:00Z",
    ):
        print(f"Audit log: {log}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # list_audit_logs()
    pass
