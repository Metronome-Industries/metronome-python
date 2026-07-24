# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.types.v1 import (
    CreditGrantEditResponse,
    CreditGrantListResponse,
    CreditGrantVoidResponse,
    CreditGrantCreateResponse,
    CreditGrantListEntriesResponse,
)
from metronome.pagination import (
    SyncCursorPage,
    AsyncCursorPage,
    SyncCursorPageWithoutLimit,
    AsyncCursorPageWithoutLimit,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditGrants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
        )
        assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
            credit_grant_type="trial",
            custom_fields={"foo": "string"},
            effective_at=parse_datetime("2022-02-01T00:00:00Z"),
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            reason="Incentivize new customer",
            rollover_settings={
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "priority": 0,
                "rollover_amount": {
                    "type": "MAX_PERCENTAGE",
                    "value": 0,
                },
            },
            uniqueness_key="x",
        )
        assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.credit_grants.with_raw_response.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = response.parse()
        assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.credit_grants.with_streaming_response.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = response.parse()
            assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.list()
        assert_matches_type(SyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.list(
            limit=1,
            next_page="next_page",
            credit_grant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            credit_type_ids=["2714e483-4ff1-48e4-9e25-ac732e8f24f2"],
            customer_ids=["d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc", "0e5b8609-d901-4992-b394-c3c2e3f37b1c"],
            effective_before=parse_datetime("2022-02-01T00:00:00Z"),
            not_expiring_before=parse_datetime("2022-02-01T00:00:00Z"),
        )
        assert_matches_type(SyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.credit_grants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = response.parse()
        assert_matches_type(SyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.credit_grants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = response.parse()
            assert_matches_type(SyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edit(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            credit_grant_type="credit_grant_type",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            name="Acme Corp Promotional Credit Grant",
        )
        assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Metronome) -> None:
        response = client.v1.credit_grants.with_raw_response.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = response.parse()
        assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Metronome) -> None:
        with client.v1.credit_grants.with_streaming_response.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = response.parse()
            assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_entries(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.list_entries()
        assert_matches_type(SyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"])

    @parametrize
    def test_method_list_entries_with_all_params(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.list_entries(
            next_page="next_page",
            sort="asc",
            credit_type_ids=["2714e483-4ff1-48e4-9e25-ac732e8f24f2"],
            customer_ids=["6a37bb88-8538-48c5-b37b-a41c836328bd"],
            ending_before=parse_datetime("2021-02-01T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
        )
        assert_matches_type(SyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"])

    @parametrize
    def test_raw_response_list_entries(self, client: Metronome) -> None:
        response = client.v1.credit_grants.with_raw_response.list_entries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = response.parse()
        assert_matches_type(SyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"])

    @parametrize
    def test_streaming_response_list_entries(self, client: Metronome) -> None:
        with client.v1.credit_grants.with_streaming_response.list_entries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = response.parse()
            assert_matches_type(
                SyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_void(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

    @parametrize
    def test_method_void_with_all_params(self, client: Metronome) -> None:
        credit_grant = client.v1.credit_grants.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            release_uniqueness_key=True,
            void_credit_purchase_invoice=True,
        )
        assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: Metronome) -> None:
        response = client.v1.credit_grants.with_raw_response.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = response.parse()
        assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: Metronome) -> None:
        with client.v1.credit_grants.with_streaming_response.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = response.parse()
            assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreditGrants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
        )
        assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
            credit_grant_type="trial",
            custom_fields={"foo": "string"},
            effective_at=parse_datetime("2022-02-01T00:00:00Z"),
            invoice_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            product_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            reason="Incentivize new customer",
            rollover_settings={
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "priority": 0,
                "rollover_amount": {
                    "type": "MAX_PERCENTAGE",
                    "value": 0,
                },
            },
            uniqueness_key="x",
        )
        assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.credit_grants.with_raw_response.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = await response.parse()
        assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.credit_grants.with_streaming_response.create(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            grant_amount={
                "amount": 1000,
                "credit_type_id": "5ae401dc-a648-4b49-9ac3-391bb5bc4d7b",
            },
            name="Acme Corp Promotional Credit Grant",
            paid_amount={
                "amount": 5000,
                "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
            },
            priority=0.5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = await response.parse()
            assert_matches_type(CreditGrantCreateResponse, credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.list()
        assert_matches_type(AsyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.list(
            limit=1,
            next_page="next_page",
            credit_grant_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            credit_type_ids=["2714e483-4ff1-48e4-9e25-ac732e8f24f2"],
            customer_ids=["d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc", "0e5b8609-d901-4992-b394-c3c2e3f37b1c"],
            effective_before=parse_datetime("2022-02-01T00:00:00Z"),
            not_expiring_before=parse_datetime("2022-02-01T00:00:00Z"),
        )
        assert_matches_type(AsyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.credit_grants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = await response.parse()
        assert_matches_type(AsyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.credit_grants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = await response.parse()
            assert_matches_type(AsyncCursorPage[CreditGrantListResponse], credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edit(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            credit_grant_type="credit_grant_type",
            expires_at=parse_datetime("2022-04-01T00:00:00Z"),
            name="Acme Corp Promotional Credit Grant",
        )
        assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.credit_grants.with_raw_response.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = await response.parse()
        assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.credit_grants.with_streaming_response.edit(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = await response.parse()
            assert_matches_type(CreditGrantEditResponse, credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_entries(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.list_entries()
        assert_matches_type(
            AsyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"]
        )

    @parametrize
    async def test_method_list_entries_with_all_params(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.list_entries(
            next_page="next_page",
            sort="asc",
            credit_type_ids=["2714e483-4ff1-48e4-9e25-ac732e8f24f2"],
            customer_ids=["6a37bb88-8538-48c5-b37b-a41c836328bd"],
            ending_before=parse_datetime("2021-02-01T00:00:00Z"),
            starting_on=parse_datetime("2021-01-01T00:00:00Z"),
        )
        assert_matches_type(
            AsyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"]
        )

    @parametrize
    async def test_raw_response_list_entries(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.credit_grants.with_raw_response.list_entries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = await response.parse()
        assert_matches_type(
            AsyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list_entries(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.credit_grants.with_streaming_response.list_entries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = await response.parse()
            assert_matches_type(
                AsyncCursorPageWithoutLimit[CreditGrantListEntriesResponse], credit_grant, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_void(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

    @parametrize
    async def test_method_void_with_all_params(self, async_client: AsyncMetronome) -> None:
        credit_grant = await async_client.v1.credit_grants.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            release_uniqueness_key=True,
            void_credit_purchase_invoice=True,
        )
        assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.credit_grants.with_raw_response.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_grant = await response.parse()
        assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.credit_grants.with_streaming_response.void(
            id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_grant = await response.parse()
            assert_matches_type(CreditGrantVoidResponse, credit_grant, path=["response"])

        assert cast(Any, response.is_closed) is True
