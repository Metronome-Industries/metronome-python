# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.customers import BillingConfigRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillingConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        billing_config = client.customers.billing_config.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
        )
        assert billing_config is None

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        billing_config = client.customers.billing_config.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
            aws_product_code="aws_product_code",
            aws_region="af-south-1",
            stripe_collection_method="charge_automatically",
        )
        assert billing_config is None

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.customers.billing_config.with_raw_response.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_config = response.parse()
        assert billing_config is None

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.customers.billing_config.with_streaming_response.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_config = response.parse()
            assert billing_config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.billing_config.with_raw_response.create(
                billing_provider_type="aws_marketplace",
                customer_id="",
                billing_provider_customer_id="cus_AJ6y20bjkOOayM",
            )

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        billing_config = client.customers.billing_config.retrieve(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(BillingConfigRetrieveResponse, billing_config, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.customers.billing_config.with_raw_response.retrieve(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_config = response.parse()
        assert_matches_type(BillingConfigRetrieveResponse, billing_config, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.customers.billing_config.with_streaming_response.retrieve(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_config = response.parse()
            assert_matches_type(BillingConfigRetrieveResponse, billing_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.billing_config.with_raw_response.retrieve(
                billing_provider_type="aws_marketplace",
                customer_id="",
            )

    @parametrize
    def test_method_delete(self, client: Metronome) -> None:
        billing_config = client.customers.billing_config.delete(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert billing_config is None

    @parametrize
    def test_raw_response_delete(self, client: Metronome) -> None:
        response = client.customers.billing_config.with_raw_response.delete(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_config = response.parse()
        assert billing_config is None

    @parametrize
    def test_streaming_response_delete(self, client: Metronome) -> None:
        with client.customers.billing_config.with_streaming_response.delete(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_config = response.parse()
            assert billing_config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.billing_config.with_raw_response.delete(
                billing_provider_type="aws_marketplace",
                customer_id="",
            )


class TestAsyncBillingConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        billing_config = await async_client.customers.billing_config.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
        )
        assert billing_config is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        billing_config = await async_client.customers.billing_config.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
            aws_product_code="aws_product_code",
            aws_region="af-south-1",
            stripe_collection_method="charge_automatically",
        )
        assert billing_config is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.customers.billing_config.with_raw_response.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_config = await response.parse()
        assert billing_config is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.customers.billing_config.with_streaming_response.create(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            billing_provider_customer_id="cus_AJ6y20bjkOOayM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_config = await response.parse()
            assert billing_config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.billing_config.with_raw_response.create(
                billing_provider_type="aws_marketplace",
                customer_id="",
                billing_provider_customer_id="cus_AJ6y20bjkOOayM",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        billing_config = await async_client.customers.billing_config.retrieve(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(BillingConfigRetrieveResponse, billing_config, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.customers.billing_config.with_raw_response.retrieve(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_config = await response.parse()
        assert_matches_type(BillingConfigRetrieveResponse, billing_config, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.customers.billing_config.with_streaming_response.retrieve(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_config = await response.parse()
            assert_matches_type(BillingConfigRetrieveResponse, billing_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.billing_config.with_raw_response.retrieve(
                billing_provider_type="aws_marketplace",
                customer_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMetronome) -> None:
        billing_config = await async_client.customers.billing_config.delete(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert billing_config is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMetronome) -> None:
        response = await async_client.customers.billing_config.with_raw_response.delete(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing_config = await response.parse()
        assert billing_config is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMetronome) -> None:
        async with async_client.customers.billing_config.with_streaming_response.delete(
            billing_provider_type="aws_marketplace",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing_config = await response.parse()
            assert billing_config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.billing_config.with_raw_response.delete(
                billing_provider_type="aws_marketplace",
                customer_id="",
            )
