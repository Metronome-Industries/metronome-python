"""Examples for the Plans resource.

Covers listing plans, getting plan details, and listing plan charges and customers.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/plans.py
"""

from metronome import Metronome

client = Metronome()


def list_plans():
    """List all plans with auto-pagination."""
    for plan in client.v1.plans.list():
        print(f"Plan: {plan}")


def get_plan_details():
    """Get detailed information about a specific plan."""
    response = client.v1.plans.get_details(
        plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    )
    print(f"Plan details: {response.data}")


def list_plan_charges():
    """List all charges associated with a plan."""
    for charge in client.v1.plans.list_charges(
        plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    ):
        print(f"Charge: {charge}")


def list_plan_customers():
    """List all customers on a specific plan."""
    for customer in client.v1.plans.list_customers(
        plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    ):
        print(f"Customer: {customer}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # list_plans()
    # get_plan_details()
    # list_plan_charges()
    # list_plan_customers()
    pass
