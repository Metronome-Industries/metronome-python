# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import DashboardGetEmbeddableURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDashboards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_embeddable_url(self, client: Metronome) -> None:
        dashboard = client.v1.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    def test_method_get_embeddable_url_with_all_params(self, client: Metronome) -> None:
        dashboard = client.v1.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
            bm_group_key_overrides=[
                {
                    "group_key_name": "tenant_id",
                    "display_name": "Org ID",
                    "value_display_names": {
                        "48ecb18f358f": "bar",
                        "e358f3ce242d": "bar",
                    },
                }
            ],
            color_overrides=[
                {
                    "name": "Gray_dark",
                    "value": "#ff0000",
                }
            ],
            dashboard_options=[
                {
                    "key": "show_zero_usage_line_items",
                    "value": "false",
                },
                {
                    "key": "hide_voided_invoices",
                    "value": "true",
                },
            ],
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    def test_raw_response_get_embeddable_url(self, client: Metronome) -> None:
        response = client.v1.dashboards.with_raw_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    def test_streaming_response_get_embeddable_url(self, client: Metronome) -> None:
        with client.v1.dashboards.with_streaming_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDashboards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_embeddable_url(self, async_client: AsyncMetronome) -> None:
        dashboard = await async_client.v1.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    async def test_method_get_embeddable_url_with_all_params(self, async_client: AsyncMetronome) -> None:
        dashboard = await async_client.v1.dashboards.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
            bm_group_key_overrides=[
                {
                    "group_key_name": "tenant_id",
                    "display_name": "Org ID",
                    "value_display_names": {
                        "48ecb18f358f": "bar",
                        "e358f3ce242d": "bar",
                    },
                }
            ],
            color_overrides=[
                {
                    "name": "Gray_dark",
                    "value": "#ff0000",
                }
            ],
            dashboard_options=[
                {
                    "key": "show_zero_usage_line_items",
                    "value": "false",
                },
                {
                    "key": "hide_voided_invoices",
                    "value": "true",
                },
            ],
        )
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    async def test_raw_response_get_embeddable_url(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.dashboards.with_raw_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

    @parametrize
    async def test_streaming_response_get_embeddable_url(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.dashboards.with_streaming_response.get_embeddable_url(
            customer_id="4db51251-61de-4bfe-b9ce-495e244f3491",
            dashboard="invoices",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardGetEmbeddableURLResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True
