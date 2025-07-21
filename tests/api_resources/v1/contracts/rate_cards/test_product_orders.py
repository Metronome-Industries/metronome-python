# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1.contracts.rate_cards import (
    ProductOrderSetResponse,
    ProductOrderUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProductOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Metronome) -> None:
        product_order = client.v1.contracts.rate_cards.product_orders.update(
            product_moves=[
                {
                    "position": 0,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                },
                {
                    "position": 1,
                    "product_id": "b086f2f4-9851-4466-9ca0-30d53e6a42ac",
                },
            ],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(ProductOrderUpdateResponse, product_order, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.product_orders.with_raw_response.update(
            product_moves=[
                {
                    "position": 0,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                },
                {
                    "position": 1,
                    "product_id": "b086f2f4-9851-4466-9ca0-30d53e6a42ac",
                },
            ],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_order = response.parse()
        assert_matches_type(ProductOrderUpdateResponse, product_order, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.product_orders.with_streaming_response.update(
            product_moves=[
                {
                    "position": 0,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                },
                {
                    "position": 1,
                    "product_id": "b086f2f4-9851-4466-9ca0-30d53e6a42ac",
                },
            ],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_order = response.parse()
            assert_matches_type(ProductOrderUpdateResponse, product_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set(self, client: Metronome) -> None:
        product_order = client.v1.contracts.rate_cards.product_orders.set(
            product_order=["13117714-3f05-48e5-a6e9-a66093f13b4d", "b086f2f4-9851-4466-9ca0-30d53e6a42ac"],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(ProductOrderSetResponse, product_order, path=["response"])

    @parametrize
    def test_raw_response_set(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.product_orders.with_raw_response.set(
            product_order=["13117714-3f05-48e5-a6e9-a66093f13b4d", "b086f2f4-9851-4466-9ca0-30d53e6a42ac"],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_order = response.parse()
        assert_matches_type(ProductOrderSetResponse, product_order, path=["response"])

    @parametrize
    def test_streaming_response_set(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.product_orders.with_streaming_response.set(
            product_order=["13117714-3f05-48e5-a6e9-a66093f13b4d", "b086f2f4-9851-4466-9ca0-30d53e6a42ac"],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_order = response.parse()
            assert_matches_type(ProductOrderSetResponse, product_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProductOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncMetronome) -> None:
        product_order = await async_client.v1.contracts.rate_cards.product_orders.update(
            product_moves=[
                {
                    "position": 0,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                },
                {
                    "position": 1,
                    "product_id": "b086f2f4-9851-4466-9ca0-30d53e6a42ac",
                },
            ],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(ProductOrderUpdateResponse, product_order, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.product_orders.with_raw_response.update(
            product_moves=[
                {
                    "position": 0,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                },
                {
                    "position": 1,
                    "product_id": "b086f2f4-9851-4466-9ca0-30d53e6a42ac",
                },
            ],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_order = await response.parse()
        assert_matches_type(ProductOrderUpdateResponse, product_order, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.product_orders.with_streaming_response.update(
            product_moves=[
                {
                    "position": 0,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                },
                {
                    "position": 1,
                    "product_id": "b086f2f4-9851-4466-9ca0-30d53e6a42ac",
                },
            ],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_order = await response.parse()
            assert_matches_type(ProductOrderUpdateResponse, product_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set(self, async_client: AsyncMetronome) -> None:
        product_order = await async_client.v1.contracts.rate_cards.product_orders.set(
            product_order=["13117714-3f05-48e5-a6e9-a66093f13b4d", "b086f2f4-9851-4466-9ca0-30d53e6a42ac"],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(ProductOrderSetResponse, product_order, path=["response"])

    @parametrize
    async def test_raw_response_set(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.product_orders.with_raw_response.set(
            product_order=["13117714-3f05-48e5-a6e9-a66093f13b4d", "b086f2f4-9851-4466-9ca0-30d53e6a42ac"],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product_order = await response.parse()
        assert_matches_type(ProductOrderSetResponse, product_order, path=["response"])

    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.product_orders.with_streaming_response.set(
            product_order=["13117714-3f05-48e5-a6e9-a66093f13b4d", "b086f2f4-9851-4466-9ca0-30d53e6a42ac"],
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product_order = await response.parse()
            assert_matches_type(ProductOrderSetResponse, product_order, path=["response"])

        assert cast(Any, response.is_closed) is True
