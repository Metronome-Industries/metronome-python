"""Examples for the Invoices resource (top-level).

Covers regenerating and voiding invoices.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/invoices.py
"""

from metronome import Metronome

client = Metronome()


def regenerate_invoice():
    """Regenerate an invoice (e.g., after updating contract terms)."""
    response = client.v1.invoices.regenerate(
        id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Regenerated invoice: {response.data}")


def void_invoice():
    """Void an invoice."""
    response = client.v1.invoices.void(
        id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Voided invoice: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # regenerate_invoice()
    # void_invoice()
    pass
