# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types import DashboardGetEmbeddableURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDashboards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_embeddable_url(self, client: Metronome) -> None:
        dashboard = client.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    def test_method_get_embeddable_url_with_all_params(self, client: Metronome) -> None:
        dashboard = client.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
            color_overrides=[
                {
                    "name": "Gray_dark",
                    "value": "#ff0000",
                }
            ],
            dashboard_options=[
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
            ],
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_get_embeddable_url(self, client: Metronome) -> None:
        response = client.dashboards.with_raw_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_get_embeddable_url(self, client: Metronome) -> None:
        with client.dashboards.with_streaming_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDashboards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_embeddable_url(self, async_client: AsyncMetronome) -> None:
        dashboard = await async_client.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_get_embeddable_url_with_all_params(self, async_client: AsyncMetronome) -> None:
        dashboard = await async_client.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
            color_overrides=[
                {
                    "name": "Gray_dark",
                    "value": "#ff0000",
                }
            ],
            dashboard_options=[
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
                {
                    "key": "key",
                    "value": "value",
                },
            ],
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_get_embeddable_url(self, async_client: AsyncMetronome) -> None:
        response = await async_client.dashboards.with_raw_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_get_embeddable_url(self, async_client: AsyncMetronome) -> None:
        async with async_client.dashboards.with_streaming_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True
