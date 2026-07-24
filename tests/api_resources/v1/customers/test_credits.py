# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.pagination import SyncBodyCursorPage, AsyncBodyCursorPage
from metronome.types.shared import Credit
from metronome.types.v1.customers import (
    CreditCreateResponse,
    CreditUpdateEndDateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        credit = client.v1.customers.credits.create(
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
        )
        assert_matches_type(CreditCreateResponse, credit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        credit = client.v1.customers.credits.create(
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
            applicable_contract_ids=["string"],
            applicable_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            applicable_product_tags=["string"],
            custom_fields={"foo": "string"},
            description="description",
            name="My Credit",
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
        assert_matches_type(CreditCreateResponse, credit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.customers.credits.with_raw_response.create(
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
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditCreateResponse, credit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.customers.credits.with_streaming_response.create(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditCreateResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        credit = client.v1.customers.credits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(SyncBodyCursorPage[Credit], credit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        credit = client.v1.customers.credits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_balance=True,
            include_contract_credits=True,
            include_ledgers=True,
            limit=1,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncBodyCursorPage[Credit], credit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.customers.credits.with_raw_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(SyncBodyCursorPage[Credit], credit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.customers.credits.with_streaming_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(SyncBodyCursorPage[Credit], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_end_date(self, client: Metronome) -> None:
        credit = client.v1.customers.credits.update_end_date(
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(CreditUpdateEndDateResponse, credit, path=["response"])

    @parametrize
    def test_raw_response_update_end_date(self, client: Metronome) -> None:
        response = client.v1.customers.credits.with_raw_response.update_end_date(
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditUpdateEndDateResponse, credit, path=["response"])

    @parametrize
    def test_streaming_response_update_end_date(self, client: Metronome) -> None:
        with client.v1.customers.credits.with_streaming_response.update_end_date(
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditUpdateEndDateResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        credit = await async_client.v1.customers.credits.create(
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
        )
        assert_matches_type(CreditCreateResponse, credit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        credit = await async_client.v1.customers.credits.create(
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
            applicable_contract_ids=["string"],
            applicable_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            applicable_product_tags=["string"],
            custom_fields={"foo": "string"},
            description="description",
            name="My Credit",
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
        assert_matches_type(CreditCreateResponse, credit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.credits.with_raw_response.create(
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
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditCreateResponse, credit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.credits.with_streaming_response.create(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditCreateResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        credit = await async_client.v1.customers.credits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(AsyncBodyCursorPage[Credit], credit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        credit = await async_client.v1.customers.credits.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_balance=True,
            include_contract_credits=True,
            include_ledgers=True,
            limit=1,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncBodyCursorPage[Credit], credit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.credits.with_raw_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(AsyncBodyCursorPage[Credit], credit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.credits.with_streaming_response.list(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(AsyncBodyCursorPage[Credit], credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_end_date(self, async_client: AsyncMetronome) -> None:
        credit = await async_client.v1.customers.credits.update_end_date(
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(CreditUpdateEndDateResponse, credit, path=["response"])

    @parametrize
    async def test_raw_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.credits.with_raw_response.update_end_date(
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditUpdateEndDateResponse, credit, path=["response"])

    @parametrize
    async def test_streaming_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.credits.with_streaming_response.update_end_date(
            access_ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
            credit_id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditUpdateEndDateResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True
