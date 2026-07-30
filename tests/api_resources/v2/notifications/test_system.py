# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from metronome import Metronome, AsyncMetronome

from metronome.types.v2.notifications import SystemListResponse

from typing import cast, Any

import os
import pytest
import httpx
from typing_extensions import get_args
from respx import MockRouter
from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestSystem:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        system = client.v2.notifications.system.list()
        assert_matches_type(SystemListResponse, system, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:

        response = client.v2.notifications.system.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        system = response.parse()
        assert_matches_type(SystemListResponse, system, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v2.notifications.system.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            system = response.parse()
            assert_matches_type(SystemListResponse, system, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncSystem:
    parametrize = pytest.mark.parametrize("async_client", [False, True, {'http_client': 'aiohttp'}], indirect=True, ids=['loose', 'strict', 'aiohttp'])


    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        system = await async_client.v2.notifications.system.list()
        assert_matches_type(SystemListResponse, system, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:

        response = await async_client.v2.notifications.system.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        system = await response.parse()
        assert_matches_type(SystemListResponse, system, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.system.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            system = await response.parse()
            assert_matches_type(SystemListResponse, system, path=['response'])

        assert cast(Any, response.is_closed) is True