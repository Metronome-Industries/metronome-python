"""Examples for the Customer Invoices resource.

Covers retrieving, listing, adding charges, listing breakdowns, and downloading PDFs.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/customer_invoices.py
"""

from datetime import datetime

from metronome import Metronome

client = Metronome()


def retrieve_invoice():
    """Retrieve a specific invoice for a customer."""
    response = client.v1.customers.invoices.retrieve(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        invoice_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    print(f"Invoice: {response.data}")


def list_invoices():
    """List all invoices for a customer."""
    for invoice in client.v1.customers.invoices.list(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
    ):
        print(f"Invoice: {invoice.id}")


def add_charge():
    """Add a one-time charge to a customer's next invoice."""
    response = client.v1.customers.invoices.add_charge(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        charge_id="b3f3e5a4-1b2c-4d5e-9f0a-1b2c3d4e5f6a",
        customer_plan_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        description="One-time setup fee",
        invoice_start_timestamp=datetime.fromisoformat("2025-01-01T00:00:00"),
        price=500.00,
        quantity=1.0,
    )
    print(f"Added charge: {response}")


def list_breakdowns():
    """List invoice breakdowns showing line-item details."""
    for breakdown in client.v1.customers.invoices.list_breakdowns(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        starting_on=datetime.fromisoformat("2025-01-01T00:00:00"),
        ending_before=datetime.fromisoformat("2025-02-01T00:00:00"),
    ):
        print(f"Breakdown: {breakdown}")


def retrieve_pdf():
    """Download an invoice as a PDF file."""
    response = client.v1.customers.invoices.retrieve_pdf(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        invoice_id="a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    )
    # Write the PDF binary content to a file
    with open("invoice.pdf", "wb") as f:
        f.write(response.content)
    print("Invoice PDF saved to invoice.pdf")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # retrieve_invoice()
    # list_invoices()
    # add_charge()
    # list_breakdowns()
    # retrieve_pdf()
    pass
