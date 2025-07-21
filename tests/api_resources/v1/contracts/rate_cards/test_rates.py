# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.pagination import SyncCursorPage, AsyncCursorPage
from metronome.types.v1.contracts.rate_cards import (
    RateAddResponse,
    RateListResponse,
    RateAddManyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        rate = client.v1.contracts.rate_cards.rates.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )
        assert_matches_type(SyncCursorPage[RateListResponse], rate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        rate = client.v1.contracts.rate_cards.rates.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            limit=1,
            next_page="next_page",
            selectors=[
                {
                    "billing_frequency": "MONTHLY",
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                    "product_tags": ["string"],
                }
            ],
        )
        assert_matches_type(SyncCursorPage[RateListResponse], rate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.rates.with_raw_response.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(SyncCursorPage[RateListResponse], rate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.rates.with_streaming_response.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(SyncCursorPage[RateListResponse], rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: Metronome) -> None:
        rate = client.v1.contracts.rate_cards.rates.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Metronome) -> None:
        rate = client.v1.contracts.rate_cards.rates.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billing_frequency="MONTHLY",
            commit_rate={
                "rate_type": "FLAT",
                "price": 0,
                "tiers": [
                    {
                        "price": 0,
                        "size": 0,
                    }
                ],
            },
            credit_type_id="2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            custom_rate={"foo": "bar"},
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_prorated=True,
            price=100,
            pricing_group_values={"foo": "string"},
            quantity=0,
            tiers=[
                {
                    "price": 0,
                    "size": 0,
                }
            ],
            use_list_prices=True,
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.rates.with_raw_response.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.rates.with_streaming_response.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateAddResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_many(self, client: Metronome) -> None:
        rate = client.v1.contracts.rate_cards.rates.add_many(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rates=[
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
            ],
        )
        assert_matches_type(RateAddManyResponse, rate, path=["response"])

    @parametrize
    def test_raw_response_add_many(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.rates.with_raw_response.add_many(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rates=[
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateAddManyResponse, rate, path=["response"])

    @parametrize
    def test_streaming_response_add_many(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.rates.with_streaming_response.add_many(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rates=[
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateAddManyResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        rate = await async_client.v1.contracts.rate_cards.rates.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )
        assert_matches_type(AsyncCursorPage[RateListResponse], rate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        rate = await async_client.v1.contracts.rate_cards.rates.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            limit=1,
            next_page="next_page",
            selectors=[
                {
                    "billing_frequency": "MONTHLY",
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                    "product_tags": ["string"],
                }
            ],
        )
        assert_matches_type(AsyncCursorPage[RateListResponse], rate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.rates.with_raw_response.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(AsyncCursorPage[RateListResponse], rate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.rates.with_streaming_response.list(
            at=parse_datetime("2024-01-01T00:00:00.000Z"),
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(AsyncCursorPage[RateListResponse], rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncMetronome) -> None:
        rate = await async_client.v1.contracts.rate_cards.rates.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncMetronome) -> None:
        rate = await async_client.v1.contracts.rate_cards.rates.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billing_frequency="MONTHLY",
            commit_rate={
                "rate_type": "FLAT",
                "price": 0,
                "tiers": [
                    {
                        "price": 0,
                        "size": 0,
                    }
                ],
            },
            credit_type_id="2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            custom_rate={"foo": "bar"},
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_prorated=True,
            price=100,
            pricing_group_values={"foo": "string"},
            quantity=0,
            tiers=[
                {
                    "price": 0,
                    "size": 0,
                }
            ],
            use_list_prices=True,
        )
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.rates.with_raw_response.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateAddResponse, rate, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.rates.with_streaming_response.add(
            entitled=True,
            product_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rate_type="FLAT",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateAddResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_many(self, async_client: AsyncMetronome) -> None:
        rate = await async_client.v1.contracts.rate_cards.rates.add_many(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rates=[
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
            ],
        )
        assert_matches_type(RateAddManyResponse, rate, path=["response"])

    @parametrize
    async def test_raw_response_add_many(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.rates.with_raw_response.add_many(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rates=[
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateAddManyResponse, rate, path=["response"])

    @parametrize
    async def test_streaming_response_add_many(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.rates.with_streaming_response.add_many(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            rates=[
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
                {
                    "entitled": True,
                    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "rate_type": "FLAT",
                    "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateAddManyResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True
