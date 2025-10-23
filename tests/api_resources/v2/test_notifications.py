# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v2 import (
    NotificationEditResponse,
    NotificationCreateResponse,
    NotificationArchiveResponse,
    NotificationRetrieveResponse,
    NotificationListOffsetResponse,
    NotificationListSystemResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        notification = client.v2.notifications.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        notification = client.v2.notifications.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
            uniqueness_key="contract-start-notification-823j7fqzo1",
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v2.notifications.with_raw_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v2.notifications.with_streaming_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationCreateResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        notification = client.v2.notifications.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(NotificationRetrieveResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v2.notifications.with_raw_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationRetrieveResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v2.notifications.with_streaming_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationRetrieveResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        notification = client.v2.notifications.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(NotificationArchiveResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v2.notifications.with_raw_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationArchiveResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v2.notifications.with_streaming_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationArchiveResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edit_overload_1(self, client: Metronome) -> None:
        notification = client.v2.notifications.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_1(self, client: Metronome) -> None:
        notification = client.v2.notifications.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
            is_enabled=True,
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_1(self, client: Metronome) -> None:
        response = client.v2.notifications.with_raw_response.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_1(self, client: Metronome) -> None:
        with client.v2.notifications.with_streaming_response.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationEditResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edit_overload_2(self, client: Metronome) -> None:
        notification = client.v2.notifications.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    def test_method_edit_with_all_params_overload_2(self, client: Metronome) -> None:
        notification = client.v2.notifications.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
            is_enabled=True,
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_edit_overload_2(self, client: Metronome) -> None:
        response = client.v2.notifications.with_raw_response.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_edit_overload_2(self, client: Metronome) -> None:
        with client.v2.notifications.with_streaming_response.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationEditResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_offset(self, client: Metronome) -> None:
        notification = client.v2.notifications.list_offset()
        assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

    @parametrize
    def test_method_list_offset_with_all_params(self, client: Metronome) -> None:
        notification = client.v2.notifications.list_offset(
            archive_filter="NOT_ARCHIVED",
            cursor="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=20,
        )
        assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_list_offset(self, client: Metronome) -> None:
        response = client.v2.notifications.with_raw_response.list_offset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_list_offset(self, client: Metronome) -> None:
        with client.v2.notifications.with_streaming_response.list_offset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_system(self, client: Metronome) -> None:
        notification = client.v2.notifications.list_system()
        assert_matches_type(NotificationListSystemResponse, notification, path=["response"])

    @parametrize
    def test_raw_response_list_system(self, client: Metronome) -> None:
        response = client.v2.notifications.with_raw_response.list_system()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationListSystemResponse, notification, path=["response"])

    @parametrize
    def test_streaming_response_list_system(self, client: Metronome) -> None:
        with client.v2.notifications.with_streaming_response.list_system() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationListSystemResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
            uniqueness_key="contract-start-notification-823j7fqzo1",
        )
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.with_raw_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationCreateResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.with_streaming_response.create(
            name="+1 day after contract starts",
            policy={
                "offset": "P1D",
                "type": "contract.start",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationCreateResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(NotificationRetrieveResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.with_raw_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationRetrieveResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.with_streaming_response.retrieve(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationRetrieveResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(NotificationArchiveResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.with_raw_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationArchiveResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.with_streaming_response.archive(
            id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationArchiveResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edit_overload_1(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_1(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
            is_enabled=True,
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_1(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.with_raw_response.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_1(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.with_streaming_response.edit(
            policy={"type": "type"},
            type="SYSTEM_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationEditResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edit_overload_2(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params_overload_2(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
            is_enabled=True,
        )
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_edit_overload_2(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.with_raw_response.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationEditResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_edit_overload_2(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.with_streaming_response.edit(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            policy={
                "offset": "P1D",
                "type": "type",
            },
            type="OFFSET_LIFECYCLE_EVENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationEditResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_offset(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.list_offset()
        assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

    @parametrize
    async def test_method_list_offset_with_all_params(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.list_offset(
            archive_filter="NOT_ARCHIVED",
            cursor="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=20,
        )
        assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_list_offset(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.with_raw_response.list_offset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_list_offset(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.with_streaming_response.list_offset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationListOffsetResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_system(self, async_client: AsyncMetronome) -> None:
        notification = await async_client.v2.notifications.list_system()
        assert_matches_type(NotificationListSystemResponse, notification, path=["response"])

    @parametrize
    async def test_raw_response_list_system(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v2.notifications.with_raw_response.list_system()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationListSystemResponse, notification, path=["response"])

    @parametrize
    async def test_streaming_response_list_system(self, async_client: AsyncMetronome) -> None:
        async with async_client.v2.notifications.with_streaming_response.list_system() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationListSystemResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True
