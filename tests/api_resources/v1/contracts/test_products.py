# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.pagination import SyncCursorPage, AsyncCursorPage
from metronome.types.v1.contracts import (
    ProductListResponse,
    ProductCreateResponse,
    ProductUpdateResponse,
    ProductArchiveResponse,
    ProductRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        product = client.v1.contracts.products.create(
            name="My Product",
            type="USAGE",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        product = client.v1.contracts.products.create(
            name="My Product",
            type="USAGE",
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            composite_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            composite_tags=["string"],
            custom_fields={"foo": "string"},
            exclude_free_usage=True,
            is_refundable=True,
            netsuite_internal_item_id="netsuite_internal_item_id",
            netsuite_overage_item_id="netsuite_overage_item_id",
            presentation_group_key=["string"],
            pricing_group_key=["string"],
            quantity_conversion={
                "conversion_factor": 0,
                "operation": "MULTIPLY",
                "name": "name",
            },
            quantity_rounding={
                "decimal_places": 0,
                "rounding_method": "ROUND_UP",
            },
            tags=["string"],
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.contracts.products.with_raw_response.create(
            name="My Product",
            type="USAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.contracts.products.with_streaming_response.create(
            name="My Product",
            type="USAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductCreateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        product = client.v1.contracts.products.retrieve(
            id="d84e7f4e-7a70-4fe4-be02-7a5027beffcc",
        )
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.contracts.products.with_raw_response.retrieve(
            id="d84e7f4e-7a70-4fe4-be02-7a5027beffcc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.contracts.products.with_streaming_response.retrieve(
            id="d84e7f4e-7a70-4fe4-be02-7a5027beffcc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductRetrieveResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Metronome) -> None:
        product = client.v1.contracts.products.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Metronome) -> None:
        product = client.v1.contracts.products.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billable_metric_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            composite_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            composite_tags=["string"],
            exclude_free_usage=True,
            is_refundable=True,
            name="My Updated Product",
            netsuite_internal_item_id="netsuite_internal_item_id",
            netsuite_overage_item_id="netsuite_overage_item_id",
            presentation_group_key=["string"],
            pricing_group_key=["string"],
            quantity_conversion={
                "conversion_factor": 0,
                "operation": "MULTIPLY",
                "name": "name",
            },
            quantity_rounding={
                "decimal_places": 0,
                "rounding_method": "ROUND_UP",
            },
            tags=["string"],
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Metronome) -> None:
        response = client.v1.contracts.products.with_raw_response.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Metronome) -> None:
        with client.v1.contracts.products.with_streaming_response.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductUpdateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        product = client.v1.contracts.products.list()
        assert_matches_type(SyncCursorPage[ProductListResponse], product, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        product = client.v1.contracts.products.list(
            limit=1,
            next_page="next_page",
            archive_filter="NOT_ARCHIVED",
        )
        assert_matches_type(SyncCursorPage[ProductListResponse], product, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.contracts.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncCursorPage[ProductListResponse], product, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.contracts.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncCursorPage[ProductListResponse], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        product = client.v1.contracts.products.archive(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(ProductArchiveResponse, product, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v1.contracts.products.with_raw_response.archive(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductArchiveResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v1.contracts.products.with_streaming_response.archive(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductArchiveResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.create(
            name="My Product",
            type="USAGE",
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.create(
            name="My Product",
            type="USAGE",
            billable_metric_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            composite_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            composite_tags=["string"],
            custom_fields={"foo": "string"},
            exclude_free_usage=True,
            is_refundable=True,
            netsuite_internal_item_id="netsuite_internal_item_id",
            netsuite_overage_item_id="netsuite_overage_item_id",
            presentation_group_key=["string"],
            pricing_group_key=["string"],
            quantity_conversion={
                "conversion_factor": 0,
                "operation": "MULTIPLY",
                "name": "name",
            },
            quantity_rounding={
                "decimal_places": 0,
                "rounding_method": "ROUND_UP",
            },
            tags=["string"],
        )
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.products.with_raw_response.create(
            name="My Product",
            type="USAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductCreateResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.products.with_streaming_response.create(
            name="My Product",
            type="USAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductCreateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.retrieve(
            id="d84e7f4e-7a70-4fe4-be02-7a5027beffcc",
        )
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.products.with_raw_response.retrieve(
            id="d84e7f4e-7a70-4fe4-be02-7a5027beffcc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductRetrieveResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.products.with_streaming_response.retrieve(
            id="d84e7f4e-7a70-4fe4-be02-7a5027beffcc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductRetrieveResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billable_metric_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            composite_product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            composite_tags=["string"],
            exclude_free_usage=True,
            is_refundable=True,
            name="My Updated Product",
            netsuite_internal_item_id="netsuite_internal_item_id",
            netsuite_overage_item_id="netsuite_overage_item_id",
            presentation_group_key=["string"],
            pricing_group_key=["string"],
            quantity_conversion={
                "conversion_factor": 0,
                "operation": "MULTIPLY",
                "name": "name",
            },
            quantity_rounding={
                "decimal_places": 0,
                "rounding_method": "ROUND_UP",
            },
            tags=["string"],
        )
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.products.with_raw_response.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductUpdateResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.products.with_streaming_response.update(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductUpdateResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.list()
        assert_matches_type(AsyncCursorPage[ProductListResponse], product, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.list(
            limit=1,
            next_page="next_page",
            archive_filter="NOT_ARCHIVED",
        )
        assert_matches_type(AsyncCursorPage[ProductListResponse], product, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncCursorPage[ProductListResponse], product, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncCursorPage[ProductListResponse], product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        product = await async_client.v1.contracts.products.archive(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(ProductArchiveResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.products.with_raw_response.archive(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductArchiveResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.products.with_streaming_response.archive(
            product_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductArchiveResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True
