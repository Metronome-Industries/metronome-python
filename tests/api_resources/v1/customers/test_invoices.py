# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from metronome.pagination import SyncCursorPage, AsyncCursorPage
from metronome.types.v1.customers import (
    Invoice,
    InvoiceRetrieveResponse,
    InvoiceAddChargeResponse,
    InvoiceListBreakdownsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        invoice = client.v1.customers.invoices.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Metronome) -> None:
        invoice = client.v1.customers.invoices.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            skip_zero_qty_line_items=True,
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.customers.invoices.with_raw_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.customers.invoices.with_streaming_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.invoices.with_raw_response.retrieve(
                customer_id="",
                invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.v1.customers.invoices.with_raw_response.retrieve(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                invoice_id="",
            )

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        invoice = client.v1.customers.invoices.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(SyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        invoice = client.v1.customers.invoices.list(
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
        response = client.v1.customers.invoices.with_raw_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.customers.invoices.with_streaming_response.list(
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
            client.v1.customers.invoices.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_add_charge(self, client: Metronome) -> None:
        invoice = client.v1.customers.invoices.add_charge(
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
        response = client.v1.customers.invoices.with_raw_response.add_charge(
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
        with client.v1.customers.invoices.with_streaming_response.add_charge(
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
            client.v1.customers.invoices.with_raw_response.add_charge(
                customer_id="",
                charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
                customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
                description="One time charge",
                invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
                price=250,
                quantity=1,
            )

    @parametrize
    def test_method_list_breakdowns(self, client: Metronome) -> None:
        invoice = client.v1.customers.invoices.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

    @parametrize
    def test_method_list_breakdowns_with_all_params(self, client: Metronome) -> None:
        invoice = client.v1.customers.invoices.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            credit_type_id="credit_type_id",
            limit=1,
            next_page="next_page",
            skip_zero_qty_line_items=True,
            sort="date_asc",
            status="status",
            window_size="HOUR",
        )
        assert_matches_type(SyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

    @parametrize
    def test_raw_response_list_breakdowns(self, client: Metronome) -> None:
        response = client.v1.customers.invoices.with_raw_response.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list_breakdowns(self, client: Metronome) -> None:
        with client.v1.customers.invoices.with_streaming_response.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_breakdowns(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.invoices.with_raw_response.list_breakdowns(
                customer_id="",
                ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_pdf(self, client: Metronome, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/customers/d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc/invoices/6a37bb88-8538-48c5-b37b-a41c836328bd/pdf"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        invoice = client.v1.customers.invoices.retrieve_pdf(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert invoice.is_closed
        assert invoice.json() == {"foo": "bar"}
        assert cast(Any, invoice.is_closed) is True
        assert isinstance(invoice, BinaryAPIResponse)

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_pdf(self, client: Metronome, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/customers/d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc/invoices/6a37bb88-8538-48c5-b37b-a41c836328bd/pdf"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        invoice = client.v1.customers.invoices.with_raw_response.retrieve_pdf(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert invoice.is_closed is True
        assert invoice.http_request.headers.get("X-Stainless-Lang") == "python"
        assert invoice.json() == {"foo": "bar"}
        assert isinstance(invoice, BinaryAPIResponse)

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_pdf(self, client: Metronome, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/customers/d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc/invoices/6a37bb88-8538-48c5-b37b-a41c836328bd/pdf"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.v1.customers.invoices.with_streaming_response.retrieve_pdf(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as invoice:
            assert not invoice.is_closed
            assert invoice.http_request.headers.get("X-Stainless-Lang") == "python"

            assert invoice.json() == {"foo": "bar"}
            assert cast(Any, invoice.is_closed) is True
            assert isinstance(invoice, StreamedBinaryAPIResponse)

        assert cast(Any, invoice.is_closed) is True

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve_pdf(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.invoices.with_raw_response.retrieve_pdf(
                customer_id="",
                invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.v1.customers.invoices.with_raw_response.retrieve_pdf(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                invoice_id="",
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.customers.invoices.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.customers.invoices.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            skip_zero_qty_line_items=True,
        )
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.invoices.with_raw_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.invoices.with_streaming_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceRetrieveResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.invoices.with_raw_response.retrieve(
                customer_id="",
                invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.v1.customers.invoices.with_raw_response.retrieve(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                invoice_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.customers.invoices.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(AsyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.customers.invoices.list(
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
        response = await async_client.v1.customers.invoices.with_raw_response.list(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(AsyncCursorPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.invoices.with_streaming_response.list(
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
            await async_client.v1.customers.invoices.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_add_charge(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.customers.invoices.add_charge(
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
        response = await async_client.v1.customers.invoices.with_raw_response.add_charge(
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
        async with async_client.v1.customers.invoices.with_streaming_response.add_charge(
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
            await async_client.v1.customers.invoices.with_raw_response.add_charge(
                customer_id="",
                charge_id="5ae4b726-1ebe-439c-9190-9831760ba195",
                customer_plan_id="a23b3cf4-47fb-4c3f-bb3d-9e64f7704015",
                description="One time charge",
                invoice_start_timestamp=parse_datetime("2024-01-01T00:00:00Z"),
                price=250,
                quantity=1,
            )

    @parametrize
    async def test_method_list_breakdowns(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.customers.invoices.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

    @parametrize
    async def test_method_list_breakdowns_with_all_params(self, async_client: AsyncMetronome) -> None:
        invoice = await async_client.v1.customers.invoices.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            credit_type_id="credit_type_id",
            limit=1,
            next_page="next_page",
            skip_zero_qty_line_items=True,
            sort="date_asc",
            status="status",
            window_size="HOUR",
        )
        assert_matches_type(AsyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

    @parametrize
    async def test_raw_response_list_breakdowns(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.invoices.with_raw_response.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(AsyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list_breakdowns(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.invoices.with_streaming_response.list_breakdowns(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncCursorPage[InvoiceListBreakdownsResponse], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_breakdowns(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.invoices.with_raw_response.list_breakdowns(
                customer_id="",
                ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_pdf(self, async_client: AsyncMetronome, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/customers/d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc/invoices/6a37bb88-8538-48c5-b37b-a41c836328bd/pdf"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        invoice = await async_client.v1.customers.invoices.retrieve_pdf(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert invoice.is_closed
        assert await invoice.json() == {"foo": "bar"}
        assert cast(Any, invoice.is_closed) is True
        assert isinstance(invoice, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_pdf(self, async_client: AsyncMetronome, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/customers/d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc/invoices/6a37bb88-8538-48c5-b37b-a41c836328bd/pdf"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        invoice = await async_client.v1.customers.invoices.with_raw_response.retrieve_pdf(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert invoice.is_closed is True
        assert invoice.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await invoice.json() == {"foo": "bar"}
        assert isinstance(invoice, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_pdf(self, async_client: AsyncMetronome, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/customers/d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc/invoices/6a37bb88-8538-48c5-b37b-a41c836328bd/pdf"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.v1.customers.invoices.with_streaming_response.retrieve_pdf(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as invoice:
            assert not invoice.is_closed
            assert invoice.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await invoice.json() == {"foo": "bar"}
            assert cast(Any, invoice.is_closed) is True
            assert isinstance(invoice, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, invoice.is_closed) is True

    @pytest.mark.skip(reason="prism mocking library in JS SDK doesnt support application/pdf")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve_pdf(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.invoices.with_raw_response.retrieve_pdf(
                customer_id="",
                invoice_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.v1.customers.invoices.with_raw_response.retrieve_pdf(
                customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                invoice_id="",
            )
