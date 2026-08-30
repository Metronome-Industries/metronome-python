"""Examples for the Services resource.

Covers listing available services.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/services.py
"""

from metronome import Metronome

client = Metronome()


def list_services():
    """List all available services."""
    response = client.v1.services.list()
    print(f"Services: {response}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # list_services()
    pass
