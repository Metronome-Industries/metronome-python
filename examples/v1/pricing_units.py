"""Examples for the Pricing Units resource.

Covers listing available pricing units (credit types / currencies).

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/pricing_units.py
"""

from metronome import Metronome

client = Metronome()


def list_pricing_units():
    """List all available pricing units (credit types)."""
    for unit in client.v1.pricing_units.list():
        print(f"Pricing unit: {unit}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # list_pricing_units()
    pass
