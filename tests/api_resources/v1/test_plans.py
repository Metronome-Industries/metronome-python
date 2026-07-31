# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import (
    PlanListResponse,
    PlanGetDetailsResponse,
    PlanListChargesResponse,
    PlanListCustomersResponse,
)
from metronome.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        plan = client.v1.plans.list()
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        plan = client.v1.plans.list(
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_details(self, client: Metronome) -> None:
        plan = client.v1.plans.get_details(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_get_details(self, client: Metronome) -> None:
        response = client.v1.plans.with_raw_response.get_details(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_get_details(self, client: Metronome) -> None:
        with client.v1.plans.with_streaming_response.get_details(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_details(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.v1.plans.with_raw_response.get_details(
                plan_id="",
            )

    @parametrize
    def test_method_list_charges(self, client: Metronome) -> None:
        plan = client.v1.plans.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(SyncCursorPage[PlanListChargesResponse], plan, path=["response"])

    @parametrize
    def test_method_list_charges_with_all_params(self, client: Metronome) -> None:
        plan = client.v1.plans.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(SyncCursorPage[PlanListChargesResponse], plan, path=["response"])

    @parametrize
    def test_raw_response_list_charges(self, client: Metronome) -> None:
        response = client.v1.plans.with_raw_response.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListChargesResponse], plan, path=["response"])

    @parametrize
    def test_streaming_response_list_charges(self, client: Metronome) -> None:
        with client.v1.plans.with_streaming_response.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListChargesResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_charges(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.v1.plans.with_raw_response.list_charges(
                plan_id="",
            )

    @parametrize
    def test_method_list_customers(self, client: Metronome) -> None:
        plan = client.v1.plans.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(SyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

    @parametrize
    def test_method_list_customers_with_all_params(self, client: Metronome) -> None:
        plan = client.v1.plans.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=1,
            next_page="next_page",
            status="all",
        )
        assert_matches_type(SyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

    @parametrize
    def test_raw_response_list_customers(self, client: Metronome) -> None:
        response = client.v1.plans.with_raw_response.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

    @parametrize
    def test_streaming_response_list_customers(self, client: Metronome) -> None:
        with client.v1.plans.with_streaming_response.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_customers(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.v1.plans.with_raw_response.list_customers(
                plan_id="",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.plans.list()
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.plans.list(
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_details(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.plans.get_details(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_get_details(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.plans.with_raw_response.get_details(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_get_details(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.plans.with_streaming_response.get_details(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_details(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.v1.plans.with_raw_response.get_details(
                plan_id="",
            )

    @parametrize
    async def test_method_list_charges(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.plans.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(AsyncCursorPage[PlanListChargesResponse], plan, path=["response"])

    @parametrize
    async def test_method_list_charges_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.plans.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(AsyncCursorPage[PlanListChargesResponse], plan, path=["response"])

    @parametrize
    async def test_raw_response_list_charges(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.plans.with_raw_response.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListChargesResponse], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list_charges(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.plans.with_streaming_response.list_charges(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListChargesResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_charges(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.v1.plans.with_raw_response.list_charges(
                plan_id="",
            )

    @parametrize
    async def test_method_list_customers(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.plans.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(AsyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

    @parametrize
    async def test_method_list_customers_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.plans.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=1,
            next_page="next_page",
            status="all",
        )
        assert_matches_type(AsyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

    @parametrize
    async def test_raw_response_list_customers(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.plans.with_raw_response.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list_customers(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.plans.with_streaming_response.list_customers(
            plan_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListCustomersResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_customers(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.v1.plans.with_raw_response.list_customers(
                plan_id="",
            )
