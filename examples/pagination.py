"""Pagination examples for the Metronome Python SDK.

Demonstrates auto-pagination and manual page control for list endpoints.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/pagination.py
"""

from metronome import Metronome

client = Metronome()


def auto_paginate():
    """Automatically iterate through all pages of results."""
    all_customers = []
    for customer in client.v1.customers.list():
        all_customers.append(customer)
    print(f"Fetched {len(all_customers)} customers")


def auto_paginate_with_limit():
    """Iterate through results with a maximum limit per page."""
    for plan in client.v1.plans.list(limit=10):
        print(f"Plan: {plan.id}")


def manual_page_control():
    """Manually control pagination using page objects."""
    first_page = client.v1.contracts.products.list()

    print(f"Items on first page: {len(first_page.data)}")

    if first_page.has_next_page():
        print(f"Next page info: {first_page.next_page_info()}")
        next_page = first_page.get_next_page()
        print(f"Items on second page: {len(next_page.data)}")


def collect_all_items():
    """Collect all items from a paginated endpoint into a list."""
    all_products = []
    for product in client.v1.contracts.products.list():
        all_products.append(product)
    print(f"Total products: {len(all_products)}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # auto_paginate()
    # auto_paginate_with_limit()
    # manual_page_control()
    # collect_all_items()
    pass
