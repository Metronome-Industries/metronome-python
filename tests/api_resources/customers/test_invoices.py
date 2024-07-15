# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.pagination import SyncCursorPage, AsyncCursorPage
from metronome.types.customers import (
    Invoice,
    InvoiceRetrieveResponse,
    InvoiceAddChargeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        invoice = client.customers.invoices.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Metronome) -> None:
        invoice = client.customers.invoices.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            skip_zero_qty_line_items=True,
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.customers.invoices.with_raw_response.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.customers.invoices.with_streaming_response.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.invoices.with_raw_response.retrieve(
                invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.customers.invoices.with_raw_response.retrieve(
                invoice_id="",
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            )

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        invoice = client.customers.invoices.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(SyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        invoice = client.customers.invoices.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            credit_type_id="credit_type_id",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            next_page="next_page",
            skip_zero_qty_line_items=True,
            sort="date_asc",
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
        )
        assert_matches_type(SyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.customers.invoices.with_raw_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.customers.invoices.with_streaming_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncCursorPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.invoices.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_add_charge(self, client: Metronome) -> None:
        invoice = client.customers.invoices.add_charge(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
            customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
            description="One time charge",
            invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
            price=250,
            quantity=1,
        )
        assert_matches_type(InvoiceAddChargeResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_add_charge(self, client: Metronome) -> None:
        response = client.customers.invoices.with_raw_response.add_charge(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
            customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
            description="One time charge",
            invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
            price=250,
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceAddChargeResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_add_charge(self, client: Metronome) -> None:
        with client.customers.invoices.with_streaming_response.add_charge(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
            customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
            description="One time charge",
            invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
            price=250,
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceAddChargeResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_charge(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.invoices.with_raw_response.add_charge(
                customer_id="",
                charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
                customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
                description="One time charge",
                invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
                price=250,
                quantity=1,
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.customers.invoices.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.customers.invoices.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            skip_zero_qty_line_items=True,
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.customers.invoices.with_raw_response.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.customers.invoices.with_streaming_response.retrieve(
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.invoices.with_raw_response.retrieve(
                invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.customers.invoices.with_raw_response.retrieve(
                invoice_id="",
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.customers.invoices.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(AsyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.customers.invoices.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            credit_type_id="credit_type_id",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            next_page="next_page",
            skip_zero_qty_line_items=True,
            sort="date_asc",
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="status",
        )
        assert_matches_type(AsyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.customers.invoices.with_raw_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(AsyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.customers.invoices.with_streaming_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncCursorPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.invoices.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_add_charge(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.customers.invoices.add_charge(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
            customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
            description="One time charge",
            invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
            price=250,
            quantity=1,
        )
        assert_matches_type(InvoiceAddChargeResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_add_charge(self, async_client: AsyncMetronome) -> None:
        response = await async_client.customers.invoices.with_raw_response.add_charge(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
            customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
            description="One time charge",
            invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
            price=250,
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceAddChargeResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_add_charge(self, async_client: AsyncMetronome) -> None:
        async with async_client.customers.invoices.with_streaming_response.add_charge(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
            customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
            description="One time charge",
            invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
            price=250,
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceAddChargeResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_charge(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.invoices.with_raw_response.add_charge(
                customer_id="",
                charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
                customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
                description="One time charge",
                invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
                price=250,
                quantity=1,
            )
