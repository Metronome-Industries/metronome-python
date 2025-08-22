# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import (
    CustomFieldListKeysResponse,
)
from metronome.pagination import SyncCursorPageWithoutLimit, AsyncCursorPageWithoutLimit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_key(self, client: Metronome) -> None:
        custom_field = client.v1.custom_fields.add_key(
            enforce_uniqueness=True,
            entity="customer",
            key="x_account_id",
        )
        assert custom_field is None

    @parametrize
    def test_raw_response_add_key(self, client: Metronome) -> None:
        response = client.v1.custom_fields.with_raw_response.add_key(
            enforce_uniqueness=True,
            entity="customer",
            key="x_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert custom_field is None

    @parametrize
    def test_streaming_response_add_key(self, client: Metronome) -> None:
        with client.v1.custom_fields.with_streaming_response.add_key(
            enforce_uniqueness=True,
            entity="customer",
            key="x_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_values(self, client: Metronome) -> None:
        custom_field = client.v1.custom_fields.delete_values(
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
            keys=["x_account_id"],
        )
        assert custom_field is None

    @parametrize
    def test_raw_response_delete_values(self, client: Metronome) -> None:
        response = client.v1.custom_fields.with_raw_response.delete_values(
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
            keys=["x_account_id"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert custom_field is None

    @parametrize
    def test_streaming_response_delete_values(self, client: Metronome) -> None:
        with client.v1.custom_fields.with_streaming_response.delete_values(
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
            keys=["x_account_id"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_keys(self, client: Metronome) -> None:
        custom_field = client.v1.custom_fields.list_keys()
        assert_matches_type(SyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"])

    @parametrize
    def test_method_list_keys_with_all_params(self, client: Metronome) -> None:
        custom_field = client.v1.custom_fields.list_keys(
            next_page="next_page",
            entities=["customer"],
        )
        assert_matches_type(SyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"])

    @parametrize
    def test_raw_response_list_keys(self, client: Metronome) -> None:
        response = client.v1.custom_fields.with_raw_response.list_keys()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert_matches_type(SyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"])

    @parametrize
    def test_streaming_response_list_keys(self, client: Metronome) -> None:
        with client.v1.custom_fields.with_streaming_response.list_keys() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert_matches_type(
                SyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_key(self, client: Metronome) -> None:
        custom_field = client.v1.custom_fields.remove_key(
            entity="customer",
            key="x_account_id",
        )
        assert custom_field is None

    @parametrize
    def test_raw_response_remove_key(self, client: Metronome) -> None:
        response = client.v1.custom_fields.with_raw_response.remove_key(
            entity="customer",
            key="x_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert custom_field is None

    @parametrize
    def test_streaming_response_remove_key(self, client: Metronome) -> None:
        with client.v1.custom_fields.with_streaming_response.remove_key(
            entity="customer",
            key="x_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_values(self, client: Metronome) -> None:
        custom_field = client.v1.custom_fields.set_values(
            custom_fields={"x_account_id": "KyVnHhSBWl7eY2bl"},
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
        )
        assert custom_field is None

    @parametrize
    def test_raw_response_set_values(self, client: Metronome) -> None:
        response = client.v1.custom_fields.with_raw_response.set_values(
            custom_fields={"x_account_id": "KyVnHhSBWl7eY2bl"},
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert custom_field is None

    @parametrize
    def test_streaming_response_set_values(self, client: Metronome) -> None:
        with client.v1.custom_fields.with_streaming_response.set_values(
            custom_fields={"x_account_id": "KyVnHhSBWl7eY2bl"},
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomFields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_key(self, async_client: AsyncMetronome) -> None:
        custom_field = await async_client.v1.custom_fields.add_key(
            enforce_uniqueness=True,
            entity="customer",
            key="x_account_id",
        )
        assert custom_field is None

    @parametrize
    async def test_raw_response_add_key(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.custom_fields.with_raw_response.add_key(
            enforce_uniqueness=True,
            entity="customer",
            key="x_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert custom_field is None

    @parametrize
    async def test_streaming_response_add_key(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.custom_fields.with_streaming_response.add_key(
            enforce_uniqueness=True,
            entity="customer",
            key="x_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_values(self, async_client: AsyncMetronome) -> None:
        custom_field = await async_client.v1.custom_fields.delete_values(
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
            keys=["x_account_id"],
        )
        assert custom_field is None

    @parametrize
    async def test_raw_response_delete_values(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.custom_fields.with_raw_response.delete_values(
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
            keys=["x_account_id"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert custom_field is None

    @parametrize
    async def test_streaming_response_delete_values(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.custom_fields.with_streaming_response.delete_values(
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
            keys=["x_account_id"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_keys(self, async_client: AsyncMetronome) -> None:
        custom_field = await async_client.v1.custom_fields.list_keys()
        assert_matches_type(AsyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"])

    @parametrize
    async def test_method_list_keys_with_all_params(self, async_client: AsyncMetronome) -> None:
        custom_field = await async_client.v1.custom_fields.list_keys(
            next_page="next_page",
            entities=["customer"],
        )
        assert_matches_type(AsyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"])

    @parametrize
    async def test_raw_response_list_keys(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.custom_fields.with_raw_response.list_keys()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert_matches_type(AsyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"])

    @parametrize
    async def test_streaming_response_list_keys(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.custom_fields.with_streaming_response.list_keys() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert_matches_type(
                AsyncCursorPageWithoutLimit[CustomFieldListKeysResponse], custom_field, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_key(self, async_client: AsyncMetronome) -> None:
        custom_field = await async_client.v1.custom_fields.remove_key(
            entity="customer",
            key="x_account_id",
        )
        assert custom_field is None

    @parametrize
    async def test_raw_response_remove_key(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.custom_fields.with_raw_response.remove_key(
            entity="customer",
            key="x_account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert custom_field is None

    @parametrize
    async def test_streaming_response_remove_key(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.custom_fields.with_streaming_response.remove_key(
            entity="customer",
            key="x_account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_values(self, async_client: AsyncMetronome) -> None:
        custom_field = await async_client.v1.custom_fields.set_values(
            custom_fields={"x_account_id": "KyVnHhSBWl7eY2bl"},
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
        )
        assert custom_field is None

    @parametrize
    async def test_raw_response_set_values(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.custom_fields.with_raw_response.set_values(
            custom_fields={"x_account_id": "KyVnHhSBWl7eY2bl"},
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert custom_field is None

    @parametrize
    async def test_streaming_response_set_values(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.custom_fields.with_streaming_response.set_values(
            custom_fields={"x_account_id": "KyVnHhSBWl7eY2bl"},
            entity="customer",
            entity_id="99594816-e8a5-4bca-be21-8d1de0f45120",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert custom_field is None

        assert cast(Any, response.is_closed) is True
