# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.pagination import SyncBodyCursorPage, AsyncBodyCursorPage
from metronome.types.shared import Commit
from metronome.types.v1.customers import (
    CommitCreateResponse,
    CommitUpdateEndDateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        commit = client.v1.customers.commits.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ]
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        commit = client.v1.customers.commits.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ],
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
            applicable_contract_ids=["string"],
            applicable_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            applicable_product_tags=["string"],
            custom_fields={"foo": "string"},
            description="description",
            invoice_contract_id="e57d6929-c2f1-4796-a9a8-63cedefe848d",
            invoice_schedule={
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "do_not_invoice": False,
                "recurring_schedule": {
                    "amount_distribution": "DIVIDED",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "frequency": "MONTHLY",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "amount": 0,
                    "quantity": 0,
                    "unit_price": 0,
                },
                "schedule_items": [
                    {
                        "timestamp": parse_datetime("2020-03-01T00:00:00.000Z"),
                        "amount": 0,
                        "quantity": 1,
                        "unit_price": 10000000,
                    }
                ],
            },
            name="My Commit",
            netsuite_sales_order_id="netsuite_sales_order_id",
            rate_type="COMMIT_RATE",
            salesforce_opportunity_id="salesforce_opportunity_id",
            specifiers=[
                {
                    "presentation_group_values": {"foo": "string"},
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "product_tags": ["string"],
                }
            ],
            uniqueness_key="x",
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.customers.commits.with_raw_response.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ]
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.customers.commits.with_streaming_response.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ]
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(CommitCreateResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        commit = client.v1.customers.commits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(SyncBodyCursorPage[Commit], commit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        commit = client.v1.customers.commits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_balance=True,
            include_contract_commits=True,
            include_ledgers=True,
            limit=1,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncBodyCursorPage[Commit], commit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.customers.commits.with_raw_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(SyncBodyCursorPage[Commit], commit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.customers.commits.with_streaming_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(SyncBodyCursorPage[Commit], commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_end_date(self, client: Metronome) -> None:
        commit = client.v1.customers.commits.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

    @parametrize
    def test_method_update_end_date_with_all_params(self, client: Metronome) -> None:
        commit = client.v1.customers.commits.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            invoices_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

    @parametrize
    def test_raw_response_update_end_date(self, client: Metronome) -> None:
        response = client.v1.customers.commits.with_raw_response.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = response.parse()
        assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

    @parametrize
    def test_streaming_response_update_end_date(self, client: Metronome) -> None:
        with client.v1.customers.commits.with_streaming_response.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = response.parse()
            assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCommits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        commit = await async_client.v1.customers.commits.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ]
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        commit = await async_client.v1.customers.commits.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ],
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
            applicable_contract_ids=["string"],
            applicable_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            applicable_product_tags=["string"],
            custom_fields={"foo": "string"},
            description="description",
            invoice_contract_id="e57d6929-c2f1-4796-a9a8-63cedefe848d",
            invoice_schedule={
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                "do_not_invoice": False,
                "recurring_schedule": {
                    "amount_distribution": "DIVIDED",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "frequency": "MONTHLY",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "amount": 0,
                    "quantity": 0,
                    "unit_price": 0,
                },
                "schedule_items": [
                    {
                        "timestamp": parse_datetime("2020-03-01T00:00:00.000Z"),
                        "amount": 0,
                        "quantity": 1,
                        "unit_price": 10000000,
                    }
                ],
            },
            name="My Commit",
            netsuite_sales_order_id="netsuite_sales_order_id",
            rate_type="COMMIT_RATE",
            salesforce_opportunity_id="salesforce_opportunity_id",
            specifiers=[
                {
                    "presentation_group_values": {"foo": "string"},
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "product_tags": ["string"],
                }
            ],
            uniqueness_key="x",
        )
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.commits.with_raw_response.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ]
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(CommitCreateResponse, commit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.commits.with_streaming_response.create(
            access_schedule={
                "schedule_items": [
                    {
                        "amount": 1000,
                        "ending_before": parse_datetime("2020-02-01T00:00:00.000Z"),
                        "starting_at": parse_datetime("2020-01-01T00:00:00.000Z"),
                    }
                ]
            },
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            priority=100,
            product_id="f14d6729-6a44-4b13-9908-9387f1918790",
            type="PREPAID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(CommitCreateResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        commit = await async_client.v1.customers.commits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(AsyncBodyCursorPage[Commit], commit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        commit = await async_client.v1.customers.commits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_balance=True,
            include_contract_commits=True,
            include_ledgers=True,
            limit=1,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncBodyCursorPage[Commit], commit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.commits.with_raw_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(AsyncBodyCursorPage[Commit], commit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.commits.with_streaming_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(AsyncBodyCursorPage[Commit], commit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_end_date(self, async_client: AsyncMetronome) -> None:
        commit = await async_client.v1.customers.commits.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

    @parametrize
    async def test_method_update_end_date_with_all_params(self, async_client: AsyncMetronome) -> None:
        commit = await async_client.v1.customers.commits.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            invoices_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

    @parametrize
    async def test_raw_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.commits.with_raw_response.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commit = await response.parse()
        assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

    @parametrize
    async def test_streaming_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.commits.with_streaming_response.update_end_date(
            commit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commit = await response.parse()
            assert_matches_type(CommitUpdateEndDateResponse, commit, path=["response"])

        assert cast(Any, response.is_closed) is True
