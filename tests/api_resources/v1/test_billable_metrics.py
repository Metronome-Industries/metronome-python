# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import (
    BillableMetricListResponse,
    BillableMetricCreateResponse,
    BillableMetricArchiveResponse,
    BillableMetricRetrieveResponse,
)
from metronome.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillableMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        billable_metric = client.v1.billable_metrics.create(
            name="CPU Hours",
        )
        assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        billable_metric = client.v1.billable_metrics.create(
            name="CPU Hours",
            aggregation_key="cpu_hours",
            aggregation_type="SUM",
            custom_fields={"foo": "string"},
            event_type_filter={
                "in_values": ["cpu_usage"],
                "not_in_values": ["string"],
            },
            group_keys=[["region"], ["machine_type"]],
            property_filters=[
                {
                    "name": "cpu_hours",
                    "exists": True,
                    "in_values": ["string"],
                    "not_in_values": ["string"],
                },
                {
                    "name": "region",
                    "exists": True,
                    "in_values": ["EU", "NA"],
                    "not_in_values": ["string"],
                },
                {
                    "name": "machine_type",
                    "exists": True,
                    "in_values": ["slow", "fast"],
                    "not_in_values": ["string"],
                },
            ],
            sql="sql",
        )
        assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.billable_metrics.with_raw_response.create(
            name="CPU Hours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = response.parse()
        assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.billable_metrics.with_streaming_response.create(
            name="CPU Hours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = response.parse()
            assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        billable_metric = client.v1.billable_metrics.retrieve(
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(BillableMetricRetrieveResponse, billable_metric, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.billable_metrics.with_raw_response.retrieve(
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = response.parse()
        assert_matches_type(BillableMetricRetrieveResponse, billable_metric, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.billable_metrics.with_streaming_response.retrieve(
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = response.parse()
            assert_matches_type(BillableMetricRetrieveResponse, billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billable_metric_id` but received ''"):
            client.v1.billable_metrics.with_raw_response.retrieve(
                billable_metric_id="",
            )

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        billable_metric = client.v1.billable_metrics.list()
        assert_matches_type(SyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        billable_metric = client.v1.billable_metrics.list(
            include_archived=True,
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(SyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.billable_metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = response.parse()
        assert_matches_type(SyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.billable_metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = response.parse()
            assert_matches_type(SyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        billable_metric = client.v1.billable_metrics.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )
        assert_matches_type(BillableMetricArchiveResponse, billable_metric, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v1.billable_metrics.with_raw_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = response.parse()
        assert_matches_type(BillableMetricArchiveResponse, billable_metric, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v1.billable_metrics.with_streaming_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = response.parse()
            assert_matches_type(BillableMetricArchiveResponse, billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBillableMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        billable_metric = await async_client.v1.billable_metrics.create(
            name="CPU Hours",
        )
        assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        billable_metric = await async_client.v1.billable_metrics.create(
            name="CPU Hours",
            aggregation_key="cpu_hours",
            aggregation_type="SUM",
            custom_fields={"foo": "string"},
            event_type_filter={
                "in_values": ["cpu_usage"],
                "not_in_values": ["string"],
            },
            group_keys=[["region"], ["machine_type"]],
            property_filters=[
                {
                    "name": "cpu_hours",
                    "exists": True,
                    "in_values": ["string"],
                    "not_in_values": ["string"],
                },
                {
                    "name": "region",
                    "exists": True,
                    "in_values": ["EU", "NA"],
                    "not_in_values": ["string"],
                },
                {
                    "name": "machine_type",
                    "exists": True,
                    "in_values": ["slow", "fast"],
                    "not_in_values": ["string"],
                },
            ],
            sql="sql",
        )
        assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.billable_metrics.with_raw_response.create(
            name="CPU Hours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = await response.parse()
        assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.billable_metrics.with_streaming_response.create(
            name="CPU Hours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = await response.parse()
            assert_matches_type(BillableMetricCreateResponse, billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        billable_metric = await async_client.v1.billable_metrics.retrieve(
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(BillableMetricRetrieveResponse, billable_metric, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.billable_metrics.with_raw_response.retrieve(
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = await response.parse()
        assert_matches_type(BillableMetricRetrieveResponse, billable_metric, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.billable_metrics.with_streaming_response.retrieve(
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = await response.parse()
            assert_matches_type(BillableMetricRetrieveResponse, billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `billable_metric_id` but received ''"):
            await async_client.v1.billable_metrics.with_raw_response.retrieve(
                billable_metric_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        billable_metric = await async_client.v1.billable_metrics.list()
        assert_matches_type(AsyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        billable_metric = await async_client.v1.billable_metrics.list(
            include_archived=True,
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(AsyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.billable_metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = await response.parse()
        assert_matches_type(AsyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.billable_metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = await response.parse()
            assert_matches_type(AsyncCursorPage[BillableMetricListResponse], billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        billable_metric = await async_client.v1.billable_metrics.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )
        assert_matches_type(BillableMetricArchiveResponse, billable_metric, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.billable_metrics.with_raw_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billable_metric = await response.parse()
        assert_matches_type(BillableMetricArchiveResponse, billable_metric, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.billable_metrics.with_streaming_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billable_metric = await response.parse()
            assert_matches_type(BillableMetricArchiveResponse, billable_metric, path=["response"])

        assert cast(Any, response.is_closed) is True
