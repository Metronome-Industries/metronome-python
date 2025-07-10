# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import (
    InvoiceVoidResponse,
    InvoiceRegenerateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_regenerate(self, client: Metronome) -> None:
        invoice = client.v1.invoices.regenerate(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(InvoiceRegenerateResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_regenerate(self, client: Metronome) -> None:
        response = client.v1.invoices.with_raw_response.regenerate(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceRegenerateResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_regenerate(self, client: Metronome) -> None:
        with client.v1.invoices.with_streaming_response.regenerate(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceRegenerateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_void(self, client: Metronome) -> None:
        invoice = client.v1.invoices.void(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: Metronome) -> None:
        response = client.v1.invoices.with_raw_response.void(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: Metronome) -> None:
        with client.v1.invoices.with_streaming_response.void(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_regenerate(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.invoices.regenerate(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(InvoiceRegenerateResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_regenerate(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.invoices.with_raw_response.regenerate(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceRegenerateResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_regenerate(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.invoices.with_streaming_response.regenerate(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceRegenerateResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_void(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.invoices.void(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.invoices.with_raw_response.void(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.invoices.with_streaming_response.void(
            id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceVoidResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True
