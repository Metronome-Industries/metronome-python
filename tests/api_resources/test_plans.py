# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types import (
    PlanListResponse,
    PlanGetDetailsResponse,
    PlanListChargesResponse,
    PlanListCustomersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        plan = client.plans.list()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        plan = client.plans.list(
            limit=1,
            next_page="string",
        )
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanListResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_details(self, client: Metronome) -> None:
        plan = client.plans.get_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_get_details(self, client: Metronome) -> None:
        response = client.plans.with_raw_response.get_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_get_details(self, client: Metronome) -> None:
        with client.plans.with_streaming_response.get_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_details(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.with_raw_response.get_details(
                "",
            )

    @parametrize
    def test_method_list_charges(self, client: Metronome) -> None:
        plan = client.plans.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanListChargesResponse, plan, path=["response"])

    @parametrize
    def test_method_list_charges_with_all_params(self, client: Metronome) -> None:
        plan = client.plans.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            next_page="string",
        )
        assert_matches_type(PlanListChargesResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_list_charges(self, client: Metronome) -> None:
        response = client.plans.with_raw_response.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanListChargesResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_list_charges(self, client: Metronome) -> None:
        with client.plans.with_streaming_response.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanListChargesResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_charges(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.with_raw_response.list_charges(
                "",
            )

    @parametrize
    def test_method_list_customers(self, client: Metronome) -> None:
        plan = client.plans.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

    @parametrize
    def test_method_list_customers_with_all_params(self, client: Metronome) -> None:
        plan = client.plans.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            next_page="string",
            status="all",
        )
        assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_list_customers(self, client: Metronome) -> None:
        response = client.plans.with_raw_response.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_list_customers(self, client: Metronome) -> None:
        with client.plans.with_streaming_response.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_customers(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            client.plans.with_raw_response.list_customers(
                "",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.plans.list()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.plans.list(
            limit=1,
            next_page="string",
        )
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanListResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_details(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.plans.get_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_get_details(self, async_client: AsyncMetronome) -> None:
        response = await async_client.plans.with_raw_response.get_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_get_details(self, async_client: AsyncMetronome) -> None:
        async with async_client.plans.with_streaming_response.get_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanGetDetailsResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_details(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.with_raw_response.get_details(
                "",
            )

    @parametrize
    async def test_method_list_charges(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.plans.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanListChargesResponse, plan, path=["response"])

    @parametrize
    async def test_method_list_charges_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.plans.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            next_page="string",
        )
        assert_matches_type(PlanListChargesResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_list_charges(self, async_client: AsyncMetronome) -> None:
        response = await async_client.plans.with_raw_response.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanListChargesResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_list_charges(self, async_client: AsyncMetronome) -> None:
        async with async_client.plans.with_streaming_response.list_charges(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanListChargesResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_charges(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.with_raw_response.list_charges(
                "",
            )

    @parametrize
    async def test_method_list_customers(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.plans.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

    @parametrize
    async def test_method_list_customers_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.plans.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            next_page="string",
            status="all",
        )
        assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_list_customers(self, async_client: AsyncMetronome) -> None:
        response = await async_client.plans.with_raw_response.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_list_customers(self, async_client: AsyncMetronome) -> None:
        async with async_client.plans.with_streaming_response.list_customers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanListCustomersResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_customers(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_id` but received ''"):
            await async_client.plans.with_raw_response.list_customers(
                "",
            )
