# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.notifications import OffsetListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOffset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        offset = client.notifications.offset.list()
        assert_matches_type(OffsetListResponse, offset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        offset = client.notifications.offset.list(
            cursor="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=20,
        )
        assert_matches_type(OffsetListResponse, offset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.notifications.offset.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert_matches_type(OffsetListResponse, offset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.notifications.offset.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert_matches_type(OffsetListResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOffset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.notifications.offset.list()
        assert_matches_type(OffsetListResponse, offset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.notifications.offset.list(
            cursor="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=20,
        )
        assert_matches_type(OffsetListResponse, offset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.notifications.offset.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert_matches_type(OffsetListResponse, offset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.notifications.offset.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert_matches_type(OffsetListResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True
