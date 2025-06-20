# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import ServiceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        service = client.v1.services.list()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.services.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.services.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        service = await async_client.v1.services.list()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.services.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.services.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True
