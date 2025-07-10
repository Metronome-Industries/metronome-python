# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.pagination import SyncCursorPage, AsyncCursorPage
from metronome.types.v1.contracts import (
    RateCardListResponse,
    RateCardCreateResponse,
    RateCardUpdateResponse,
    RateCardArchiveResponse,
    RateCardRetrieveResponse,
    RateCardRetrieveRateScheduleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRateCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.create(
            name="My Rate Card",
        )
        assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.create(
            name="My Rate Card",
            aliases=[
                {
                    "name": "my-rate-card",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            credit_type_conversions=[
                {
                    "custom_credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "fiat_per_custom_credit": 2,
                }
            ],
            custom_fields={"foo": "string"},
            description="My Rate Card Description",
            fiat_credit_type_id="2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        )
        assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.with_raw_response.create(
            name="My Rate Card",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = response.parse()
        assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.with_streaming_response.create(
            name="My Rate Card",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = response.parse()
            assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.retrieve(
            id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )
        assert_matches_type(RateCardRetrieveResponse, rate_card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.with_raw_response.retrieve(
            id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = response.parse()
        assert_matches_type(RateCardRetrieveResponse, rate_card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.with_streaming_response.retrieve(
            id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = response.parse()
            assert_matches_type(RateCardRetrieveResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            aliases=[
                {
                    "name": "name",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            description="My Updated Rate Card Description",
            name="My Updated Rate Card",
        )
        assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.with_raw_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = response.parse()
        assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.with_streaming_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = response.parse()
            assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.list()
        assert_matches_type(SyncCursorPage[RateCardListResponse], rate_card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.list(
            limit=1,
            next_page="next_page",
            body={},
        )
        assert_matches_type(SyncCursorPage[RateCardListResponse], rate_card, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = response.parse()
        assert_matches_type(SyncCursorPage[RateCardListResponse], rate_card, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = response.parse()
            assert_matches_type(SyncCursorPage[RateCardListResponse], rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.archive(
            id="12b21470-4570-40df-8998-449d0b0bc52f",
        )
        assert_matches_type(RateCardArchiveResponse, rate_card, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.with_raw_response.archive(
            id="12b21470-4570-40df-8998-449d0b0bc52f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = response.parse()
        assert_matches_type(RateCardArchiveResponse, rate_card, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.with_streaming_response.archive(
            id="12b21470-4570-40df-8998-449d0b0bc52f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = response.parse()
            assert_matches_type(RateCardArchiveResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rate_schedule(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
        )
        assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

    @parametrize
    def test_method_retrieve_rate_schedule_with_all_params(self, client: Metronome) -> None:
        rate_card = client.v1.contracts.rate_cards.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
            limit=1,
            next_page="next_page",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            selectors=[
                {
                    "billing_frequency": "MONTHLY",
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                }
            ],
        )
        assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

    @parametrize
    def test_raw_response_retrieve_rate_schedule(self, client: Metronome) -> None:
        response = client.v1.contracts.rate_cards.with_raw_response.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = response.parse()
        assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_rate_schedule(self, client: Metronome) -> None:
        with client.v1.contracts.rate_cards.with_streaming_response.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = response.parse()
            assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRateCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.create(
            name="My Rate Card",
        )
        assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.create(
            name="My Rate Card",
            aliases=[
                {
                    "name": "my-rate-card",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            credit_type_conversions=[
                {
                    "custom_credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "fiat_per_custom_credit": 2,
                }
            ],
            custom_fields={"foo": "string"},
            description="My Rate Card Description",
            fiat_credit_type_id="2714e483-4ff1-48e4-9e25-ac732e8f24f2",
        )
        assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.with_raw_response.create(
            name="My Rate Card",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = await response.parse()
        assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.with_streaming_response.create(
            name="My Rate Card",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = await response.parse()
            assert_matches_type(RateCardCreateResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.retrieve(
            id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )
        assert_matches_type(RateCardRetrieveResponse, rate_card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.with_raw_response.retrieve(
            id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = await response.parse()
        assert_matches_type(RateCardRetrieveResponse, rate_card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.with_streaming_response.retrieve(
            id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = await response.parse()
            assert_matches_type(RateCardRetrieveResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            aliases=[
                {
                    "name": "name",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            description="My Updated Rate Card Description",
            name="My Updated Rate Card",
        )
        assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.with_raw_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = await response.parse()
        assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.with_streaming_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = await response.parse()
            assert_matches_type(RateCardUpdateResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.list()
        assert_matches_type(AsyncCursorPage[RateCardListResponse], rate_card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.list(
            limit=1,
            next_page="next_page",
            body={},
        )
        assert_matches_type(AsyncCursorPage[RateCardListResponse], rate_card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = await response.parse()
        assert_matches_type(AsyncCursorPage[RateCardListResponse], rate_card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = await response.parse()
            assert_matches_type(AsyncCursorPage[RateCardListResponse], rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.archive(
            id="12b21470-4570-40df-8998-449d0b0bc52f",
        )
        assert_matches_type(RateCardArchiveResponse, rate_card, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.with_raw_response.archive(
            id="12b21470-4570-40df-8998-449d0b0bc52f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = await response.parse()
        assert_matches_type(RateCardArchiveResponse, rate_card, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.with_streaming_response.archive(
            id="12b21470-4570-40df-8998-449d0b0bc52f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = await response.parse()
            assert_matches_type(RateCardArchiveResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
        )
        assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

    @parametrize
    async def test_method_retrieve_rate_schedule_with_all_params(self, async_client: AsyncMetronome) -> None:
        rate_card = await async_client.v1.contracts.rate_cards.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
            limit=1,
            next_page="next_page",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            selectors=[
                {
                    "billing_frequency": "MONTHLY",
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                }
            ],
        )
        assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.rate_cards.with_raw_response.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_card = await response.parse()
        assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.rate_cards.with_streaming_response.retrieve_rate_schedule(
            rate_card_id="f3d51ae8-f283-44e1-9933-a3cf9ad7a6fe",
            starting_at=parse_datetime("2024-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_card = await response.parse()
            assert_matches_type(RateCardRetrieveRateScheduleResponse, rate_card, path=["response"])

        assert cast(Any, response.is_closed) is True
