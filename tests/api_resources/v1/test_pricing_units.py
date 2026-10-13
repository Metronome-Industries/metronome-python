# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import (
    PricingUnitListResponse,
    PricingUnitCreateResponse,
    PricingUnitArchiveResponse,
)
from metronome.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPricingUnits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        pricing_unit = client.v1.pricing_units.create(
            name="AI Credits",
        )
        assert_matches_type(PricingUnitCreateResponse, pricing_unit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.pricing_units.with_raw_response.create(
            name="AI Credits",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing_unit = response.parse()
        assert_matches_type(PricingUnitCreateResponse, pricing_unit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.pricing_units.with_streaming_response.create(
            name="AI Credits",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing_unit = response.parse()
            assert_matches_type(PricingUnitCreateResponse, pricing_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        pricing_unit = client.v1.pricing_units.list()
        assert_matches_type(SyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        pricing_unit = client.v1.pricing_units.list(
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(SyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.pricing_units.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing_unit = response.parse()
        assert_matches_type(SyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.pricing_units.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing_unit = response.parse()
            assert_matches_type(SyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        pricing_unit = client.v1.pricing_units.archive(
            id="fa2f1b3d-9d52-4951-a099-25991fd394d6",
        )
        assert_matches_type(PricingUnitArchiveResponse, pricing_unit, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v1.pricing_units.with_raw_response.archive(
            id="fa2f1b3d-9d52-4951-a099-25991fd394d6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing_unit = response.parse()
        assert_matches_type(PricingUnitArchiveResponse, pricing_unit, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v1.pricing_units.with_streaming_response.archive(
            id="fa2f1b3d-9d52-4951-a099-25991fd394d6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing_unit = response.parse()
            assert_matches_type(PricingUnitArchiveResponse, pricing_unit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPricingUnits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        pricing_unit = await async_client.v1.pricing_units.create(
            name="AI Credits",
        )
        assert_matches_type(PricingUnitCreateResponse, pricing_unit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.pricing_units.with_raw_response.create(
            name="AI Credits",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing_unit = await response.parse()
        assert_matches_type(PricingUnitCreateResponse, pricing_unit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.pricing_units.with_streaming_response.create(
            name="AI Credits",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing_unit = await response.parse()
            assert_matches_type(PricingUnitCreateResponse, pricing_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        pricing_unit = await async_client.v1.pricing_units.list()
        assert_matches_type(AsyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        pricing_unit = await async_client.v1.pricing_units.list(
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(AsyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.pricing_units.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing_unit = await response.parse()
        assert_matches_type(AsyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.pricing_units.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing_unit = await response.parse()
            assert_matches_type(AsyncCursorPage[PricingUnitListResponse], pricing_unit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        pricing_unit = await async_client.v1.pricing_units.archive(
            id="fa2f1b3d-9d52-4951-a099-25991fd394d6",
        )
        assert_matches_type(PricingUnitArchiveResponse, pricing_unit, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.pricing_units.with_raw_response.archive(
            id="fa2f1b3d-9d52-4951-a099-25991fd394d6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing_unit = await response.parse()
        assert_matches_type(PricingUnitArchiveResponse, pricing_unit, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.pricing_units.with_streaming_response.archive(
            id="fa2f1b3d-9d52-4951-a099-25991fd394d6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing_unit = await response.parse()
            assert_matches_type(PricingUnitArchiveResponse, pricing_unit, path=["response"])

        assert cast(Any, response.is_closed) is True
