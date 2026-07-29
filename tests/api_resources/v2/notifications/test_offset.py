# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v2 import LifecycleEventOffsetNotificationConfig
from metronome.pagination import SyncBodyCursorPageCursorField, AsyncBodyCursorPageCursorField
from metronome.types.v2.notifications import (
    OffsetEditResponse,
    OffsetCreateResponse,
    OffsetArchiveResponse,
    OffsetRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOffset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )
        assert_matches_type(OffsetCreateResponse, offset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
            uniqueness_key="contract-start-notification-823j7fqzo1",
        )
        assert_matches_type(OffsetCreateResponse, offset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v2.notifications.offset.with_raw_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert_matches_type(OffsetCreateResponse, offset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v2.notifications.offset.with_streaming_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert_matches_type(OffsetCreateResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(OffsetRetrieveResponse, offset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v2.notifications.offset.with_raw_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert_matches_type(OffsetRetrieveResponse, offset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v2.notifications.offset.with_streaming_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert_matches_type(OffsetRetrieveResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.list()
        assert_matches_type(
            SyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.list(
            archive_filter="NOT_ARCHIVED",
            cursor="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=20,
        )
        assert_matches_type(
            SyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v2.notifications.offset.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert_matches_type(
            SyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v2.notifications.offset.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert_matches_type(
                SyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(OffsetArchiveResponse, offset, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v2.notifications.offset.with_raw_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert_matches_type(OffsetArchiveResponse, offset, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v2.notifications.offset.with_streaming_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert_matches_type(OffsetArchiveResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edit(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
        )
        assert_matches_type(OffsetEditResponse, offset, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Metronome) -> None:
        offset = client.v2.notifications.offset.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            is_enabled=True,
        )
        assert_matches_type(OffsetEditResponse, offset, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Metronome) -> None:
        response = client.v2.notifications.offset.with_raw_response.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = response.parse()
        assert_matches_type(OffsetEditResponse, offset, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Metronome) -> None:
        with client.v2.notifications.offset.with_streaming_response.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = response.parse()
            assert_matches_type(OffsetEditResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOffset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )
        assert_matches_type(OffsetCreateResponse, offset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
            uniqueness_key="contract-start-notification-823j7fqzo1",
        )
        assert_matches_type(OffsetCreateResponse, offset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.offset.with_raw_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert_matches_type(OffsetCreateResponse, offset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.offset.with_streaming_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert_matches_type(OffsetCreateResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(OffsetRetrieveResponse, offset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.offset.with_raw_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert_matches_type(OffsetRetrieveResponse, offset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.offset.with_streaming_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert_matches_type(OffsetRetrieveResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.list()
        assert_matches_type(
            AsyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.list(
            archive_filter="NOT_ARCHIVED",
            cursor="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=20,
        )
        assert_matches_type(
            AsyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.offset.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert_matches_type(
            AsyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.offset.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert_matches_type(
                AsyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig], offset, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(OffsetArchiveResponse, offset, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.offset.with_raw_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert_matches_type(OffsetArchiveResponse, offset, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.offset.with_streaming_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert_matches_type(OffsetArchiveResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edit(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
        )
        assert_matches_type(OffsetEditResponse, offset, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncMetronome) -> None:
        offset = await async_client.v2.notifications.offset.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            is_enabled=True,
        )
        assert_matches_type(OffsetEditResponse, offset, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.offset.with_raw_response.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offset = await response.parse()
        assert_matches_type(OffsetEditResponse, offset, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.offset.with_streaming_response.edit(
            policy={
                "offset": "P2D",
                "type": "contract.start",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offset = await response.parse()
            assert_matches_type(OffsetEditResponse, offset, path=["response"])

        assert cast(Any, response.is_closed) is True
