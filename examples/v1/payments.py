"""Examples for the Payments resource.

Covers listing, attempting, and canceling payments.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/payments.py
"""

from metronome import Metronome

client = Metronome()


def list_payments():
    """List payments for a customer's invoice."""
    for payment in client.v1.payments.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        invoice_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    ):
        print(f"Payment: {payment}")


def attempt_payment():
    """Attempt to process a payment for a customer's invoice."""
    response = client.v1.payments.attempt(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        invoice_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Payment attempt: {response}")


def cancel_payment():
    """Cancel a pending payment for a customer's invoice."""
    response = client.v1.payments.cancel(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        invoice_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Payment canceled: {response}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # list_payments()
    # attempt_payment()
    # cancel_payment()
    pass
