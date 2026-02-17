"""Examples for the Customer Plans resource.

Covers listing, adding, ending plans for customers, and viewing price adjustments.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customer_plans.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def list_plans():
    """List all plans for a customer."""
    for plan in client.v1.customers.plans.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    ):
        print(f"Plan: {plan}")


def add_plan():
    """Add a plan to a customer."""
    response = client.v1.customers.plans.add(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        starting_on=datetime.fromisoformat("2025-01-01T00:00:00"),
        # ending_before=datetime.fromisoformat("2026-01-01T00:00:00"),  # Optional end date
    )
    print(f"Added plan: {response.data}")


def end_plan():
    """End a customer's plan."""
    response = client.v1.customers.plans.end(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        customer_plan_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        # ending_before=datetime.fromisoformat("2025-06-01T00:00:00"),  # Specific end date
        # void_invoices=True,  # Void any pending invoices
    )
    print(f"Ended plan: {response.data}")


def list_price_adjustments():
    """List price adjustments for a customer's plan."""
    for adjustment in client.v1.customers.plans.list_price_adjustments(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        customer_plan_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    ):
        print(f"Price adjustment: {adjustment}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # list_plans()
    # add_plan()
    # end_plan()
    # list_price_adjustments()
    pass
