# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import (
    Payment,
    PaymentCancelResponse,
    PaymentAttemptResponse,
)
from metronome.pagination import SyncBodyCursorPage, AsyncBodyCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        payment = client.v1.payments.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )
        assert_matches_type(SyncBodyCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        payment = client.v1.payments.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            limit=1,
            next_page="next_page",
            statuses=["pending", "requires_intervention"],
        )
        assert_matches_type(SyncBodyCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.payments.with_raw_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncBodyCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.payments.with_streaming_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncBodyCursorPage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_attempt(self, client: Metronome) -> None:
        payment = client.v1.payments.attempt(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )
        assert_matches_type(PaymentAttemptResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_attempt(self, client: Metronome) -> None:
        response = client.v1.payments.with_raw_response.attempt(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentAttemptResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_attempt(self, client: Metronome) -> None:
        with client.v1.payments.with_streaming_response.attempt(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentAttemptResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Metronome) -> None:
        payment = client.v1.payments.cancel(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )
        assert_matches_type(PaymentCancelResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Metronome) -> None:
        response = client.v1.payments.with_raw_response.cancel(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCancelResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Metronome) -> None:
        with client.v1.payments.with_streaming_response.cancel(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCancelResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        payment = await async_client.v1.payments.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )
        assert_matches_type(AsyncBodyCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        payment = await async_client.v1.payments.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            limit=1,
            next_page="next_page",
            statuses=["pending", "requires_intervention"],
        )
        assert_matches_type(AsyncBodyCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.payments.with_raw_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(AsyncBodyCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.payments.with_streaming_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncBodyCursorPage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_attempt(self, async_client: AsyncMetronome) -> None:
        payment = await async_client.v1.payments.attempt(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )
        assert_matches_type(PaymentAttemptResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_attempt(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.payments.with_raw_response.attempt(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentAttemptResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_attempt(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.payments.with_streaming_response.attempt(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentAttemptResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncMetronome) -> None:
        payment = await async_client.v1.payments.cancel(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )
        assert_matches_type(PaymentCancelResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.payments.with_raw_response.cancel(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCancelResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.payments.with_streaming_response.cancel(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            invoice_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCancelResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
