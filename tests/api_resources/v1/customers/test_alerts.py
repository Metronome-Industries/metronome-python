# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.pagination import SyncCursorPageWithoutLimit, AsyncCursorPageWithoutLimit
from metronome.types.v1.customers import (
    CustomerAlert,
    AlertRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        alert = client.v1.customers.alerts.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Metronome) -> None:
        alert = client.v1.customers.alerts.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            group_values=[
                {
                    "key": "key",
                    "value": "value",
                }
            ],
            plans_or_contracts="PLANS",
            seat_filter={
                "seat_group_key": "seat_group_key",
                "seat_group_value": "seat_group_value",
            },
        )
        assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.customers.alerts.with_raw_response.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.customers.alerts.with_streaming_response.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        alert = client.v1.customers.alerts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(SyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        alert = client.v1.customers.alerts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            next_page="next_page",
            alert_statuses=["ENABLED"],
        )
        assert_matches_type(SyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.customers.alerts.with_raw_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert_matches_type(SyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.customers.alerts.with_streaming_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert_matches_type(SyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reset(self, client: Metronome) -> None:
        alert = client.v1.customers.alerts.reset(
            alert_id="5e8691bf-b22a-4672-922d-f80eee940f01",
            customer_id="4c83caf3-8af4-44e2-9aeb-e290531726d9",
        )
        assert alert is None

    @parametrize
    def test_raw_response_reset(self, client: Metronome) -> None:
        response = client.v1.customers.alerts.with_raw_response.reset(
            alert_id="5e8691bf-b22a-4672-922d-f80eee940f01",
            customer_id="4c83caf3-8af4-44e2-9aeb-e290531726d9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert alert is None

    @parametrize
    def test_streaming_response_reset(self, client: Metronome) -> None:
        with client.v1.customers.alerts.with_streaming_response.reset(
            alert_id="5e8691bf-b22a-4672-922d-f80eee940f01",
            customer_id="4c83caf3-8af4-44e2-9aeb-e290531726d9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert alert is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAlerts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.v1.customers.alerts.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.v1.customers.alerts.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            group_values=[
                {
                    "key": "key",
                    "value": "value",
                }
            ],
            plans_or_contracts="PLANS",
            seat_filter={
                "seat_group_key": "seat_group_key",
                "seat_group_value": "seat_group_value",
            },
        )
        assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.alerts.with_raw_response.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.alerts.with_streaming_response.retrieve(
            alert_id="8deed800-1b7a-495d-a207-6c52bac54dc9",
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AlertRetrieveResponse, alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.v1.customers.alerts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(AsyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.v1.customers.alerts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            next_page="next_page",
            alert_statuses=["ENABLED"],
        )
        assert_matches_type(AsyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.alerts.with_raw_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert_matches_type(AsyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.alerts.with_streaming_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert_matches_type(AsyncCursorPageWithoutLimit[CustomerAlert], alert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reset(self, async_client: AsyncMetronome) -> None:
        alert = await async_client.v1.customers.alerts.reset(
            alert_id="5e8691bf-b22a-4672-922d-f80eee940f01",
            customer_id="4c83caf3-8af4-44e2-9aeb-e290531726d9",
        )
        assert alert is None

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.alerts.with_raw_response.reset(
            alert_id="5e8691bf-b22a-4672-922d-f80eee940f01",
            customer_id="4c83caf3-8af4-44e2-9aeb-e290531726d9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert alert is None

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.alerts.with_streaming_response.reset(
            alert_id="5e8691bf-b22a-4672-922d-f80eee940f01",
            customer_id="4c83caf3-8af4-44e2-9aeb-e290531726d9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert alert is None

        assert cast(Any, response.is_closed) is True
