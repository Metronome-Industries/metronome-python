# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types import AlertCreateResponse, AlertArchiveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        alert = client.alerts.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
        )
        assert_matches_type(AlertCreateResponse, alert, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        alert = client.alerts.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
            billable_metric_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_grant_type_filters=["enterprise"],
            credit_type_id="2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            custom_field_filters=[
                {
                    "entity": "Contract",
                    "key": "key",
                    "value": "value",
                },
                {
                    "entity": "Contract",
                    "key": "key",
                    "value": "value",
                },
                {
                    "entity": "Contract",
                    "key": "key",
                    "value": "value",
                },
            ],
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            evaluate_on_create=True,
            group_key_filter={
                "key": "key",
                "value": "value",
            },
            invoice_types_filter=[
                "PLAN_ARREARS, SCHEDULED, USAGE, CORRECTION, CREDIT_PURCHASE, or SEAT_PURCHASE",
                "PLAN_ARREARS, SCHEDULED, USAGE, CORRECTION, CREDIT_PURCHASE, or SEAT_PURCHASE",
                "PLAN_ARREARS, SCHEDULED, USAGE, CORRECTION, CREDIT_PURCHASE, or SEAT_PURCHASE",
            ],
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            uniqueness_key="x",
        )
        assert_matches_type(AlertCreateResponse, alert, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.alerts.with_raw_response.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(AlertCreateResponse, alert, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.alerts.with_streaming_response.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(AlertCreateResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        alert = client.alerts.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )
        assert_matches_type(AlertArchiveResponse, alert, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.alerts.with_raw_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(AlertArchiveResponse, alert, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.alerts.with_streaming_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(AlertArchiveResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAlerts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.alerts.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
        )
        assert_matches_type(AlertCreateResponse, alert, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.alerts.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
            billable_metric_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_grant_type_filters=["enterprise"],
            credit_type_id="2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            custom_field_filters=[
                {
                    "entity": "Contract",
                    "key": "key",
                    "value": "value",
                },
                {
                    "entity": "Contract",
                    "key": "key",
                    "value": "value",
                },
                {
                    "entity": "Contract",
                    "key": "key",
                    "value": "value",
                },
            ],
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            evaluate_on_create=True,
            group_key_filter={
                "key": "key",
                "value": "value",
            },
            invoice_types_filter=[
                "PLAN_ARREARS, SCHEDULED, USAGE, CORRECTION, CREDIT_PURCHASE, or SEAT_PURCHASE",
                "PLAN_ARREARS, SCHEDULED, USAGE, CORRECTION, CREDIT_PURCHASE, or SEAT_PURCHASE",
                "PLAN_ARREARS, SCHEDULED, USAGE, CORRECTION, CREDIT_PURCHASE, or SEAT_PURCHASE",
            ],
            plan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            uniqueness_key="x",
        )
        assert_matches_type(AlertCreateResponse, alert, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.alerts.with_raw_response.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert_matches_type(AlertCreateResponse, alert, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.alerts.with_streaming_response.create(
            alert_type="low_credit_balance_reached",
            name="$100 spend threshold reached",
            threshold=10000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AlertCreateResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.alerts.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )
        assert_matches_type(AlertArchiveResponse, alert, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.alerts.with_raw_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert_matches_type(AlertArchiveResponse, alert, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.alerts.with_streaming_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AlertArchiveResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True
