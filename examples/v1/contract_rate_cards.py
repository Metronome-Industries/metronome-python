"""Examples for the Contract Rate Cards resource and sub-resources.

Covers rate card CRUD operations, plus managing product orders, rates, and named schedules.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/contract_rate_cards.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


# ============================================================================
# Rate Cards
# ============================================================================


def create_rate_card():
    """Create a new rate card."""
    response = client.v1.contracts.rate_cards.create(
        name="Standard Rate Card",
        # description="Default rate card for standard customers",
        # fiat_credit_type_id="2714e483-4ff1-48e4-9e25-ac732e8f24f2",
    )
    print(f"Created rate card: {response.data}")


def retrieve_rate_card():
    """Retrieve a specific rate card by ID."""
    response = client.v1.contracts.rate_cards.retrieve(
        id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    )
    print(f"Rate card: {response.data}")


def update_rate_card():
    """Update a rate card (e.g., change name or description)."""
    response = client.v1.contracts.rate_cards.update(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        # name="Updated Rate Card",
        # description="Updated description",
    )
    print(f"Updated rate card: {response.data}")


def list_rate_cards():
    """List all rate cards with auto-pagination."""
    for rate_card in client.v1.contracts.rate_cards.list():
        print(f"Rate card: {rate_card}")


def archive_rate_card():
    """Archive a rate card."""
    response = client.v1.contracts.rate_cards.archive(
        id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    )
    print(f"Archived: {response.data}")


def retrieve_rate_schedule():
    """Retrieve the rate schedule for a rate card."""
    response = client.v1.contracts.rate_cards.retrieve_rate_schedule(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        # ending_before=datetime.fromisoformat("2026-01-01T00:00:00"),
    )
    print(f"Rate schedule: {response.data}")


# ============================================================================
# Product Orders
# ============================================================================


def update_product_orders():
    """Move (reorder) products within a rate card."""
    response = client.v1.contracts.rate_cards.product_orders.update(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        product_moves=[
            {
                "product_id": "b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
                "position": 0,
            }
        ],
    )
    print(f"Updated product order: {response.data}")


def set_product_orders():
    """Set the complete product order for a rate card."""
    response = client.v1.contracts.rate_cards.product_orders.set(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        product_order=[
            "b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
            "c4d5e6f7-2a3b-4c5d-0e1f-2a3b4c5d6e7f",
        ],
    )
    print(f"Set product order: {response.data}")


# ============================================================================
# Rates
# ============================================================================


def list_rates():
    """List rates for a rate card at a specific point in time."""
    for rate in client.v1.contracts.rate_cards.rates.list(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        at=datetime.fromisoformat("2025-01-01T00:00:00"),
    ):
        print(f"Rate: {rate}")


def add_rate():
    """Add a single rate to a rate card."""
    response = client.v1.contracts.rate_cards.rates.add(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        product_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        entitled=True,
        rate_type="FLAT",
        # price=0.01,  # Price per unit
        # ending_before=datetime.fromisoformat("2026-01-01T00:00:00"),
    )
    print(f"Added rate: {response.data}")


def add_many_rates():
    """Add multiple rates to a rate card in a single request."""
    response = client.v1.contracts.rate_cards.rates.add_many(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        rates=[
            {
                "product_id": "b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
                "starting_at": "2025-01-01T00:00:00Z",
                "entitled": True,
                "rate_type": "FLAT",
                "price": 0.01,
            },
            {
                "product_id": "c4d5e6f7-2a3b-4c5d-0e1f-2a3b4c5d6e7f",
                "starting_at": "2025-01-01T00:00:00Z",
                "entitled": True,
                "rate_type": "FLAT",
                "price": 0.05,
            },
        ],
    )
    print(f"Added rates: {response.data}")


# ============================================================================
# Rate Card Named Schedules
# ============================================================================


def retrieve_rate_card_named_schedule():
    """Retrieve a named schedule for a rate card."""
    response = client.v1.contracts.rate_cards.named_schedules.retrieve(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        schedule_name="my-schedule",
    )
    print(f"Named schedule: {response.data}")


def update_rate_card_named_schedule():
    """Update a named schedule for a rate card."""
    client.v1.contracts.rate_cards.named_schedules.update(
        rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        schedule_name="my-schedule",
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        value={"discount_percentage": 15},
    )
    print("Rate card named schedule updated")


if __name__ == "__main__":
    # Uncomment the example you want to run:

    # Rate Cards
    # create_rate_card()
    # retrieve_rate_card()
    # update_rate_card()
    # list_rate_cards()
    # archive_rate_card()
    # retrieve_rate_schedule()

    # Product Orders
    # update_product_orders()
    # set_product_orders()

    # Rates
    # list_rates()
    # add_rate()
    # add_many_rates()

    # Named Schedules
    # retrieve_rate_card_named_schedule()
    # update_rate_card_named_schedule()
    pass
