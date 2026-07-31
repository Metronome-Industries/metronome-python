# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1.settings import (
    BillingProviderListResponse,
    BillingProviderCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillingProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        billing_provider = client.v1.settings.billing_providers.create(
            billing_provider="aws_marketplace",
            configuration={
                "aws_external_id": "bar",
                "aws_iam_role_arn": "bar",
            },
            delivery_method="direct_to_billing_provider",
        )
        assert_matches_type(BillingProviderCreateResponse, billing_provider, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.settings.billing_providers.with_raw_response.create(
            billing_provider="aws_marketplace",
            configuration={
                "aws_external_id": "bar",
                "aws_iam_role_arn": "bar",
            },
            delivery_method="direct_to_billing_provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_provider = response.parse()
        assert_matches_type(BillingProviderCreateResponse, billing_provider, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.settings.billing_providers.with_streaming_response.create(
            billing_provider="aws_marketplace",
            configuration={
                "aws_external_id": "bar",
                "aws_iam_role_arn": "bar",
            },
            delivery_method="direct_to_billing_provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_provider = response.parse()
            assert_matches_type(BillingProviderCreateResponse, billing_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        billing_provider = client.v1.settings.billing_providers.list()
        assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        billing_provider = client.v1.settings.billing_providers.list(
            next_page="af26878a-de62-4a0d-9b77-3936f7c2b6d6",
        )
        assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.settings.billing_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_provider = response.parse()
        assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.settings.billing_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_provider = response.parse()
            assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBillingProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        billing_provider = await async_client.v1.settings.billing_providers.create(
            billing_provider="aws_marketplace",
            configuration={
                "aws_external_id": "bar",
                "aws_iam_role_arn": "bar",
            },
            delivery_method="direct_to_billing_provider",
        )
        assert_matches_type(BillingProviderCreateResponse, billing_provider, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.settings.billing_providers.with_raw_response.create(
            billing_provider="aws_marketplace",
            configuration={
                "aws_external_id": "bar",
                "aws_iam_role_arn": "bar",
            },
            delivery_method="direct_to_billing_provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_provider = await response.parse()
        assert_matches_type(BillingProviderCreateResponse, billing_provider, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.settings.billing_providers.with_streaming_response.create(
            billing_provider="aws_marketplace",
            configuration={
                "aws_external_id": "bar",
                "aws_iam_role_arn": "bar",
            },
            delivery_method="direct_to_billing_provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_provider = await response.parse()
            assert_matches_type(BillingProviderCreateResponse, billing_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        billing_provider = await async_client.v1.settings.billing_providers.list()
        assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        billing_provider = await async_client.v1.settings.billing_providers.list(
            next_page="af26878a-de62-4a0d-9b77-3936f7c2b6d6",
        )
        assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.settings.billing_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_provider = await response.parse()
        assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.settings.billing_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_provider = await response.parse()
            assert_matches_type(BillingProviderListResponse, billing_provider, path=["response"])

        assert cast(Any, response.is_closed) is True
