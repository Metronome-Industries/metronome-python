# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types import AuditLogListResponse
from metronome._utils import parse_datetime
from metronome.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        audit_log = client.audit_logs.list()
        assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        audit_log = client.audit_logs.list(
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            next_page="next_page",
            resource_id="resource_id",
            resource_type="resource_type",
            sort="date_asc",
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(SyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        audit_log = await async_client.audit_logs.list()
        assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        audit_log = await async_client.audit_logs.list(
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            next_page="next_page",
            resource_id="resource_id",
            resource_type="resource_type",
            sort="date_asc",
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.audit_logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.audit_logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AsyncCursorPage[AuditLogListResponse], audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True
