"""Async client examples for the Metronome Python SDK.

Demonstrates how to use the async client with both httpx and aiohttp backends.

Usage:
    export METRONOME_BEARER_TOKEN="your-api-token"
    python examples/async_usage.py
"""

import asyncio

from metronome import AsyncMetronome


async def basic_async():
    """Basic async client usage with httpx (default backend)."""
    client = AsyncMetronome()

    # All methods are the same as the sync client, but awaited
    customers = []
    async for customer in client.v1.customers.list():
        customers.append(customer)
    print(f"Fetched {len(customers)} customers")

    await client.close()


async def async_with_context_manager():
    """Use the async client as a context manager for automatic cleanup."""
    async with AsyncMetronome() as client:
        client.v1.usage.ingest(
            usage=[
                {
                    "transaction_id": "90e9401f-0f8c-4cd3-9a9f-d6beb56d8d72",
                    "customer_id": "team@example.com",
                    "event_type": "heartbeat",
                    "timestamp": "2025-01-01T00:00:00Z",
                    "properties": {"cpu_seconds": 60},
                }
            ],
        )
        print("Usage event ingested")


async def async_with_aiohttp():
    """Use the aiohttp backend for improved concurrency performance.

    Requires: pip install metronome-sdk[aiohttp]
    """
    from metronome import DefaultAioHttpClient

    async with AsyncMetronome(http_client=DefaultAioHttpClient()) as client:
        customers = []
        async for customer in client.v1.customers.list():
            customers.append(customer)
        print(f"Fetched {len(customers)} customers")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    # asyncio.run(basic_async())
    # asyncio.run(async_with_context_manager())
    # asyncio.run(async_with_aiohttp())
    pass
