# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.types.v1 import (
    UsageListResponse,
    UsageSearchResponse,
    UsageListWithGroupsResponse,
)
from metronome.pagination import (
    SyncCursorPage,
    AsyncCursorPage,
    SyncCursorPageWithoutLimit,
    AsyncCursorPageWithoutLimit,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        usage = client.v1.usage.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
        )
        assert_matches_type(SyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        usage = client.v1.usage.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
            next_page="next_page",
            billable_metrics=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "group_by": {
                        "key": "key",
                        "values": ["x"],
                    },
                }
            ],
            customer_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.usage.with_raw_response.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(SyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.usage.with_streaming_response.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(SyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ingest(self, client: Metronome) -> None:
        usage = client.v1.usage.ingest()
        assert usage is None

    @parametrize
    def test_method_ingest_with_all_params(self, client: Metronome) -> None:
        usage = client.v1.usage.ingest(
            usage=[
                {
                    "customer_id": "team@example.com",
                    "event_type": "heartbeat",
                    "timestamp": "2021-01-01T00:00:00Z",
                    "transaction_id": "2021-01-01T00:00:00Z_cluster42",
                    "properties": {
                        "cluster_id": "bar",
                        "cpu_seconds": "bar",
                        "region": "bar",
                    },
                }
            ],
        )
        assert usage is None

    @parametrize
    def test_raw_response_ingest(self, client: Metronome) -> None:
        response = client.v1.usage.with_raw_response.ingest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert usage is None

    @parametrize
    def test_streaming_response_ingest(self, client: Metronome) -> None:
        with client.v1.usage.with_streaming_response.ingest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_with_groups(self, client: Metronome) -> None:
        usage = client.v1.usage.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
        )
        assert_matches_type(SyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

    @parametrize
    def test_method_list_with_groups_with_all_params(self, client: Metronome) -> None:
        usage = client.v1.usage.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
            limit=1,
            next_page="next_page",
            current_period=True,
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            group_by={
                "key": "region",
                "values": ["US-East", "US-West", "EU-Central"],
            },
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
        )
        assert_matches_type(SyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

    @parametrize
    def test_raw_response_list_with_groups(self, client: Metronome) -> None:
        response = client.v1.usage.with_raw_response.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(SyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

    @parametrize
    def test_streaming_response_list_with_groups(self, client: Metronome) -> None:
        with client.v1.usage.with_streaming_response.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(SyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Metronome) -> None:
        usage = client.v1.usage.search(
            transaction_ids=["2021-01-01T00:00:00Z_cluster42"],
        )
        assert_matches_type(UsageSearchResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Metronome) -> None:
        response = client.v1.usage.with_raw_response.search(
            transaction_ids=["2021-01-01T00:00:00Z_cluster42"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageSearchResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Metronome) -> None:
        with client.v1.usage.with_streaming_response.search(
            transaction_ids=["2021-01-01T00:00:00Z_cluster42"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageSearchResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        usage = await async_client.v1.usage.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
        )
        assert_matches_type(AsyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        usage = await async_client.v1.usage.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
            next_page="next_page",
            billable_metrics=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "group_by": {
                        "key": "key",
                        "values": ["x"],
                    },
                }
            ],
            customer_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AsyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.usage.with_raw_response.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(AsyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.usage.with_streaming_response.list(
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
            window_size="HOUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(AsyncCursorPageWithoutLimit[UsageListResponse], usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ingest(self, async_client: AsyncMetronome) -> None:
        usage = await async_client.v1.usage.ingest()
        assert usage is None

    @parametrize
    async def test_method_ingest_with_all_params(self, async_client: AsyncMetronome) -> None:
        usage = await async_client.v1.usage.ingest(
            usage=[
                {
                    "customer_id": "team@example.com",
                    "event_type": "heartbeat",
                    "timestamp": "2021-01-01T00:00:00Z",
                    "transaction_id": "2021-01-01T00:00:00Z_cluster42",
                    "properties": {
                        "cluster_id": "bar",
                        "cpu_seconds": "bar",
                        "region": "bar",
                    },
                }
            ],
        )
        assert usage is None

    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.usage.with_raw_response.ingest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert usage is None

    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.usage.with_streaming_response.ingest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert usage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_with_groups(self, async_client: AsyncMetronome) -> None:
        usage = await async_client.v1.usage.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
        )
        assert_matches_type(AsyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

    @parametrize
    async def test_method_list_with_groups_with_all_params(self, async_client: AsyncMetronome) -> None:
        usage = await async_client.v1.usage.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
            limit=1,
            next_page="next_page",
            current_period=True,
            ending_before=parse_datetime("2021-01-03T00:00:00Z"),
            group_by={
                "key": "region",
                "values": ["US-East", "US-West", "EU-Central"],
            },
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
        )
        assert_matches_type(AsyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

    @parametrize
    async def test_raw_response_list_with_groups(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.usage.with_raw_response.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(AsyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

    @parametrize
    async def test_streaming_response_list_with_groups(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.usage.with_streaming_response.list_with_groups(
            billable_metric_id="222796fd-d29c-429e-89b2-549fabda4ed6",
            customer_id="04ca7e72-4229-4a6e-ab11-9f7376fccbcb",
            window_size="HOUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(AsyncCursorPage[UsageListWithGroupsResponse], usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncMetronome) -> None:
        usage = await async_client.v1.usage.search(
            transaction_ids=["2021-01-01T00:00:00Z_cluster42"],
        )
        assert_matches_type(UsageSearchResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.usage.with_raw_response.search(
            transaction_ids=["2021-01-01T00:00:00Z_cluster42"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageSearchResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.usage.with_streaming_response.search(
            transaction_ids=["2021-01-01T00:00:00Z_cluster42"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageSearchResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
