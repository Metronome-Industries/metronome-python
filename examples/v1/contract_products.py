"""Examples for the Contract Products resource.

Covers creating, retrieving, updating, listing, and archiving contract products.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/contract_products.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def create_product():
    """Create a new contract product."""
    response = client.v1.contracts.products.create(
        name="API Calls",
        type="USAGE",
        # type can be: USAGE, FIXED, COMPOSITE, SUBSCRIPTION, PROFESSIONAL_SERVICE, PRO_SERVICE
    )
    print(f"Created product: {response.data}")


def retrieve_product():
    """Retrieve a specific product by ID."""
    response = client.v1.contracts.products.retrieve(
        id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
    )
    print(f"Product: {response.data}")


def update_product():
    """Update a product (e.g., change name, add tags)."""
    response = client.v1.contracts.products.update(
        product_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
        starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        # name="Updated API Calls",
        # tags=["compute", "api"],
    )
    print(f"Updated product: {response.data}")


def list_products():
    """List all contract products with auto-pagination."""
    for product in client.v1.contracts.products.list():
        print(f"Product: {product}")


def archive_product():
    """Archive a contract product."""
    response = client.v1.contracts.products.archive(
        product_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
    )
    print(f"Archived: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # create_product()
    # retrieve_product()
    # update_product()
    # list_products()
    # archive_product()
    pass
