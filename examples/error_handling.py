"""Error handling examples for the Metronome Python SDK.

Demonstrates how to handle API errors, configure retries, and set timeouts.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/error_handling.py
"""

from datetime import datetime

import metronome
from metronome import Metronome


def basic_error_handling():
    """Handle common API errors with specific exception types."""
    client = Metronome()

    try:
        client.v1.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=datetime.fromisoformat("2025-01-01T00:00:00"),
        )
    except metronome.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)  # an underlying Exception, likely raised within httpx.
    except metronome.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
    except metronome.BadRequestError as e:
        print(f"Bad request (400): {e.message}")
    except metronome.AuthenticationError as e:
        print(f"Authentication failed (401): {e.message}")
    except metronome.NotFoundError as e:
        print(f"Resource not found (404): {e.message}")
    except metronome.APIStatusError as e:
        print(f"API error (status {e.status_code}): {e.message}")
        print(f"Response body: {e.response}")


def configure_retries():
    """Configure automatic retry behavior."""
    # Disable retries entirely
    client = Metronome(max_retries=0)

    # Or increase retries (default is 2)
    client = Metronome(max_retries=5)

    # Override retries for a specific request
    client.with_options(max_retries=5).v1.customers.list()


def configure_timeouts():
    """Configure request timeouts."""
    import httpx

    # Set a global timeout (in seconds, default is 60)
    client = Metronome(timeout=20.0)

    # Fine-grained timeout control
    client = Metronome(
        timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
    )

    # Override timeout for a specific request
    client.with_options(timeout=5.0).v1.customers.list()


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # basic_error_handling()
    # configure_retries()
    # configure_timeouts()
    pass
