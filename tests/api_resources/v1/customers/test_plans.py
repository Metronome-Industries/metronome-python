# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.pagination import SyncCursorPage, AsyncCursorPage
from metronome.types.v1.customers import (
    PlanAddResponse,
    PlanEndResponse,
    PlanListResponse,
    PlanListPriceAdjustmentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.customers.plans.with_raw_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.customers.plans.with_streaming_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.plans.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_add(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
        )
        assert_matches_type(PlanAddResponse, plan, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
            ending_before=parse_datetime("2022-02-01T00:00:00Z"),
            net_payment_terms_days=0,
            overage_rate_adjustments=[
                {
                    "custom_credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "fiat_currency_credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "to_fiat_conversion_factor": 0,
                }
            ],
            price_adjustments=[
                {
                    "adjustment_type": "percentage",
                    "charge_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "start_period": 0,
                    "quantity": 0,
                    "tier": 0,
                    "value": 0,
                }
            ],
            trial_spec={
                "length_in_days": 0,
                "spending_cap": {
                    "amount": 0,
                    "credit_type_id": "credit_type_id",
                },
            },
        )
        assert_matches_type(PlanAddResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Metronome) -> None:
        response = client.v1.customers.plans.with_raw_response.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanAddResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Metronome) -> None:
        with client.v1.customers.plans.with_streaming_response.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanAddResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.plans.with_raw_response.add(
                customer_id="",
                plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
                starting_on=parse_datetime("2021-02-01T00:00:00Z"),
            )

    @parametrize
    def test_method_end(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )
        assert_matches_type(PlanEndResponse, plan, path=["response"])

    @parametrize
    def test_method_end_with_all_params(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            ending_before=parse_datetime("2021-02-01T00:00:00Z"),
            void_invoices=True,
            void_stripe_invoices=True,
        )
        assert_matches_type(PlanEndResponse, plan, path=["response"])

    @parametrize
    def test_raw_response_end(self, client: Metronome) -> None:
        response = client.v1.customers.plans.with_raw_response.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanEndResponse, plan, path=["response"])

    @parametrize
    def test_streaming_response_end(self, client: Metronome) -> None:
        with client.v1.customers.plans.with_streaming_response.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanEndResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_end(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.plans.with_raw_response.end(
                customer_id="",
                customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_plan_id` but received ''"):
            client.v1.customers.plans.with_raw_response.end(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                customer_plan_id="",
            )

    @parametrize
    def test_method_list_price_adjustments(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )
        assert_matches_type(SyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

    @parametrize
    def test_method_list_price_adjustments_with_all_params(self, client: Metronome) -> None:
        plan = client.v1.customers.plans.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(SyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

    @parametrize
    def test_raw_response_list_price_adjustments(self, client: Metronome) -> None:
        response = client.v1.customers.plans.with_raw_response.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

    @parametrize
    def test_streaming_response_list_price_adjustments(self, client: Metronome) -> None:
        with client.v1.customers.plans.with_streaming_response.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_price_adjustments(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.plans.with_raw_response.list_price_adjustments(
                customer_id="",
                customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_plan_id` but received ''"):
            client.v1.customers.plans.with_raw_response.list_price_adjustments(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                customer_plan_id="",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.plans.with_raw_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.plans.with_streaming_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.plans.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
        )
        assert_matches_type(PlanAddResponse, plan, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
            ending_before=parse_datetime("2022-02-01T00:00:00Z"),
            net_payment_terms_days=0,
            overage_rate_adjustments=[
                {
                    "custom_credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "fiat_currency_credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "to_fiat_conversion_factor": 0,
                }
            ],
            price_adjustments=[
                {
                    "adjustment_type": "percentage",
                    "charge_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "start_period": 0,
                    "quantity": 0,
                    "tier": 0,
                    "value": 0,
                }
            ],
            trial_spec={
                "length_in_days": 0,
                "spending_cap": {
                    "amount": 0,
                    "credit_type_id": "credit_type_id",
                },
            },
        )
        assert_matches_type(PlanAddResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.plans.with_raw_response.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanAddResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.plans.with_streaming_response.add(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
            starting_on=parse_datetime("2021-02-01T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanAddResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.plans.with_raw_response.add(
                customer_id="",
                plan_id="d2c06dae-9549-4d7d-bc04-b78dd3d241b8",
                starting_on=parse_datetime("2021-02-01T00:00:00Z"),
            )

    @parametrize
    async def test_method_end(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )
        assert_matches_type(PlanEndResponse, plan, path=["response"])

    @parametrize
    async def test_method_end_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            ending_before=parse_datetime("2021-02-01T00:00:00Z"),
            void_invoices=True,
            void_stripe_invoices=True,
        )
        assert_matches_type(PlanEndResponse, plan, path=["response"])

    @parametrize
    async def test_raw_response_end(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.plans.with_raw_response.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanEndResponse, plan, path=["response"])

    @parametrize
    async def test_streaming_response_end(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.plans.with_streaming_response.end(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanEndResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_end(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.plans.with_raw_response.end(
                customer_id="",
                customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_plan_id` but received ''"):
            await async_client.v1.customers.plans.with_raw_response.end(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                customer_plan_id="",
            )

    @parametrize
    async def test_method_list_price_adjustments(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )
        assert_matches_type(AsyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

    @parametrize
    async def test_method_list_price_adjustments_with_all_params(self, async_client: AsyncMetronome) -> None:
        plan = await async_client.v1.customers.plans.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(AsyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

    @parametrize
    async def test_raw_response_list_price_adjustments(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.plans.with_raw_response.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list_price_adjustments(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.plans.with_streaming_response.list_price_adjustments(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursorPage[PlanListPriceAdjustmentsResponse], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_price_adjustments(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.plans.with_raw_response.list_price_adjustments(
                customer_id="",
                customer_plan_id="7aa11640-0703-4600-8eb9-293f535a6b74",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_plan_id` but received ''"):
            await async_client.v1.customers.plans.with_raw_response.list_price_adjustments(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                customer_plan_id="",
            )
