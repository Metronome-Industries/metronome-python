"""Examples for the Dashboards resource.

Covers generating embeddable dashboard URLs for customer-facing analytics.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/v1/dashboards.py
"""

from metronome import Metronome

client = Metronome()


def get_embeddable_url():
    """Generate an embeddable URL for a customer dashboard."""
    response = client.v1.dashboards.get_embeddable_url(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        dashboard="usage",
        # dashboard options: "invoices", "usage", "credits", "commits_and_credits"
        # color_overrides=[  # Customize dashboard colors
        #     {"name": "Primary_medium", "value": "#1a73e8"},
        # ],
    )
    print(f"Embeddable URL: {response.data}")


def get_invoice_dashboard_url():
    """Generate an embeddable URL for the invoices dashboard."""
    response = client.v1.dashboards.get_embeddable_url(
        customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        dashboard="invoices",
    )
    print(f"Invoice dashboard URL: {response.data}")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # get_embeddable_url()
    # get_invoice_dashboard_url()
    pass
