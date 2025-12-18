# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.types.v1 import (
    CustomerDetail,
    CustomerCreateResponse,
    CustomerArchiveResponse,
    CustomerSetNameResponse,
    CustomerRetrieveResponse,
    CustomerListCostsResponse,
    CustomerPreviewEventsResponse,
    CustomerListBillableMetricsResponse,
    CustomerSetBillingConfigurationsResponse,
    CustomerRetrieveBillingConfigurationsResponse,
)
from metronome.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        customer = client.v1.customers.create(
            name="Example, Inc.",
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        customer = client.v1.customers.create(
            name="Example, Inc.",
            billing_config={
                "billing_provider_customer_id": "billing_provider_customer_id",
                "billing_provider_type": "aws_marketplace",
                "aws_customer_account_id": "aws_customer_account_id",
                "aws_customer_id": "aws_customer_id",
                "aws_is_subscription_product": True,
                "aws_product_code": "aws_product_code",
                "aws_region": "af-south-1",
                "stripe_collection_method": "charge_automatically",
            },
            custom_fields={"foo": "string"},
            customer_billing_provider_configurations=[
                {
                    "billing_provider": "stripe",
                    "configuration": {
                        "stripe_customer_id": "bar",
                        "stripe_collection_method": "bar",
                    },
                    "delivery_method": "direct_to_billing_provider",
                    "delivery_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tax_provider": "anrok",
                }
            ],
            customer_revenue_system_configurations=[
                {
                    "provider": "netsuite",
                    "configuration": {"foo": "bar"},
                    "delivery_method": "direct_to_billing_provider",
                    "delivery_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            external_id="x",
            ingest_aliases=["team@example.com"],
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.create(
            name="Example, Inc.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.create(
            name="Example, Inc.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerCreateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        customer = client.v1.customers.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.with_raw_response.retrieve(
                customer_id="",
            )

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        customer = client.v1.customers.list()
        assert_matches_type(SyncCursorPage[CustomerDetail], customer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        customer = client.v1.customers.list(
            customer_ids=["string"],
            ingest_alias="ingest_alias",
            limit=1,
            next_page="next_page",
            only_archived=True,
            salesforce_account_ids=["string"],
        )
        assert_matches_type(SyncCursorPage[CustomerDetail], customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncCursorPage[CustomerDetail], customer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncCursorPage[CustomerDetail], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        customer = client.v1.customers.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )
        assert_matches_type(CustomerArchiveResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerArchiveResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerArchiveResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_billable_metrics(self, client: Metronome) -> None:
        customer = client.v1.customers.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(SyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

    @parametrize
    def test_method_list_billable_metrics_with_all_params(self, client: Metronome) -> None:
        customer = client.v1.customers.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            include_archived=True,
            limit=1,
            next_page="next_page",
            on_current_plan=True,
        )
        assert_matches_type(SyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

    @parametrize
    def test_raw_response_list_billable_metrics(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

    @parametrize
    def test_streaming_response_list_billable_metrics(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_billable_metrics(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.with_raw_response.list_billable_metrics(
                customer_id="",
            )

    @parametrize
    def test_method_list_costs(self, client: Metronome) -> None:
        customer = client.v1.customers.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

    @parametrize
    def test_method_list_costs_with_all_params(self, client: Metronome) -> None:
        customer = client.v1.customers.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(SyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

    @parametrize
    def test_raw_response_list_costs(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

    @parametrize
    def test_streaming_response_list_costs(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_costs(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.with_raw_response.list_costs(
                customer_id="",
                ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    def test_method_preview_events(self, client: Metronome) -> None:
        customer = client.v1.customers.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[{"event_type": "heartbeat"}],
        )
        assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

    @parametrize
    def test_method_preview_events_with_all_params(self, client: Metronome) -> None:
        customer = client.v1.customers.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[
                {
                    "event_type": "heartbeat",
                    "properties": {
                        "cpu_hours": "bar",
                        "memory_gb_hours": "bar",
                    },
                    "timestamp": "2021-01-01T00:00:00Z",
                    "transaction_id": "x",
                }
            ],
            mode="replace",
            skip_zero_qty_line_items=True,
        )
        assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_preview_events(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[{"event_type": "heartbeat"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_preview_events(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[{"event_type": "heartbeat"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_preview_events(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.with_raw_response.preview_events(
                customer_id="",
                events=[{"event_type": "heartbeat"}],
            )

    @parametrize
    def test_method_retrieve_billing_configurations(self, client: Metronome) -> None:
        customer = client.v1.customers.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    def test_method_retrieve_billing_configurations_with_all_params(self, client: Metronome) -> None:
        customer = client.v1.customers.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            include_archived=True,
        )
        assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_retrieve_billing_configurations(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_billing_configurations(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_billing_configurations(self, client: Metronome) -> None:
        customer = client.v1.customers.set_billing_configurations(
            data=[
                {
                    "billing_provider": "stripe",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "azure_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "gcp_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
            ],
        )
        assert_matches_type(CustomerSetBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_set_billing_configurations(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.set_billing_configurations(
            data=[
                {
                    "billing_provider": "stripe",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "azure_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "gcp_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerSetBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_set_billing_configurations(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.set_billing_configurations(
            data=[
                {
                    "billing_provider": "stripe",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "azure_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "gcp_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerSetBillingConfigurationsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_ingest_aliases(self, client: Metronome) -> None:
        customer = client.v1.customers.set_ingest_aliases(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ingest_aliases=["team@example.com"],
        )
        assert customer is None

    @parametrize
    def test_raw_response_set_ingest_aliases(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.set_ingest_aliases(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ingest_aliases=["team@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_streaming_response_set_ingest_aliases(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.set_ingest_aliases(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ingest_aliases=["team@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_ingest_aliases(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.with_raw_response.set_ingest_aliases(
                customer_id="",
                ingest_aliases=["team@example.com"],
            )

    @parametrize
    def test_method_set_name(self, client: Metronome) -> None:
        customer = client.v1.customers.set_name(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            name="Example, Inc.",
        )
        assert_matches_type(CustomerSetNameResponse, customer, path=["response"])

    @parametrize
    def test_raw_response_set_name(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.set_name(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            name="Example, Inc.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerSetNameResponse, customer, path=["response"])

    @parametrize
    def test_streaming_response_set_name(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.set_name(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            name="Example, Inc.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerSetNameResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_set_name(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.with_raw_response.set_name(
                customer_id="",
                name="Example, Inc.",
            )

    @parametrize
    def test_method_update_config(self, client: Metronome) -> None:
        customer = client.v1.customers.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert customer is None

    @parametrize
    def test_method_update_config_with_all_params(self, client: Metronome) -> None:
        customer = client.v1.customers.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            leave_stripe_invoices_in_draft=True,
            salesforce_account_id="0015500001WO1ZiABL",
        )
        assert customer is None

    @parametrize
    def test_raw_response_update_config(self, client: Metronome) -> None:
        response = client.v1.customers.with_raw_response.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @parametrize
    def test_streaming_response_update_config(self, client: Metronome) -> None:
        with client.v1.customers.with_streaming_response.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_config(self, client: Metronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v1.customers.with_raw_response.update_config(
                customer_id="",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.create(
            name="Example, Inc.",
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.create(
            name="Example, Inc.",
            billing_config={
                "billing_provider_customer_id": "billing_provider_customer_id",
                "billing_provider_type": "aws_marketplace",
                "aws_customer_account_id": "aws_customer_account_id",
                "aws_customer_id": "aws_customer_id",
                "aws_is_subscription_product": True,
                "aws_product_code": "aws_product_code",
                "aws_region": "af-south-1",
                "stripe_collection_method": "charge_automatically",
            },
            custom_fields={"foo": "string"},
            customer_billing_provider_configurations=[
                {
                    "billing_provider": "stripe",
                    "configuration": {
                        "stripe_customer_id": "bar",
                        "stripe_collection_method": "bar",
                    },
                    "delivery_method": "direct_to_billing_provider",
                    "delivery_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tax_provider": "anrok",
                }
            ],
            customer_revenue_system_configurations=[
                {
                    "provider": "netsuite",
                    "configuration": {"foo": "bar"},
                    "delivery_method": "direct_to_billing_provider",
                    "delivery_method_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            external_id="x",
            ingest_aliases=["team@example.com"],
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.create(
            name="Example, Inc.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.create(
            name="Example, Inc.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerCreateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.retrieve(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerRetrieveResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.with_raw_response.retrieve(
                customer_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.list()
        assert_matches_type(AsyncCursorPage[CustomerDetail], customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.list(
            customer_ids=["string"],
            ingest_alias="ingest_alias",
            limit=1,
            next_page="next_page",
            only_archived=True,
            salesforce_account_ids=["string"],
        )
        assert_matches_type(AsyncCursorPage[CustomerDetail], customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(AsyncCursorPage[CustomerDetail], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncCursorPage[CustomerDetail], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )
        assert_matches_type(CustomerArchiveResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerArchiveResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.archive(
            id="8deed800-1b7a-495d-a207-6c52bac54dc9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerArchiveResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_billable_metrics(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(AsyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

    @parametrize
    async def test_method_list_billable_metrics_with_all_params(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            include_archived=True,
            limit=1,
            next_page="next_page",
            on_current_plan=True,
        )
        assert_matches_type(AsyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

    @parametrize
    async def test_raw_response_list_billable_metrics(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(AsyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list_billable_metrics(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.list_billable_metrics(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncCursorPage[CustomerListBillableMetricsResponse], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_billable_metrics(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.with_raw_response.list_billable_metrics(
                customer_id="",
            )

    @parametrize
    async def test_method_list_costs(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

    @parametrize
    async def test_method_list_costs_with_all_params(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            next_page="next_page",
        )
        assert_matches_type(AsyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

    @parametrize
    async def test_raw_response_list_costs(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(AsyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list_costs(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.list_costs(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncCursorPage[CustomerListCostsResponse], customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_costs(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.with_raw_response.list_costs(
                customer_id="",
                ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
                starting_on=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    async def test_method_preview_events(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[{"event_type": "heartbeat"}],
        )
        assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

    @parametrize
    async def test_method_preview_events_with_all_params(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[
                {
                    "event_type": "heartbeat",
                    "properties": {
                        "cpu_hours": "bar",
                        "memory_gb_hours": "bar",
                    },
                    "timestamp": "2021-01-01T00:00:00Z",
                    "transaction_id": "x",
                }
            ],
            mode="replace",
            skip_zero_qty_line_items=True,
        )
        assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_preview_events(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[{"event_type": "heartbeat"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_preview_events(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.preview_events(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            events=[{"event_type": "heartbeat"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerPreviewEventsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_preview_events(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.with_raw_response.preview_events(
                customer_id="",
                events=[{"event_type": "heartbeat"}],
            )

    @parametrize
    async def test_method_retrieve_billing_configurations(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )
        assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    async def test_method_retrieve_billing_configurations_with_all_params(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
            include_archived=True,
        )
        assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_billing_configurations(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_billing_configurations(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.retrieve_billing_configurations(
            customer_id="6a37bb88-8538-48c5-b37b-a41c836328bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerRetrieveBillingConfigurationsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_billing_configurations(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.set_billing_configurations(
            data=[
                {
                    "billing_provider": "stripe",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "azure_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "gcp_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
            ],
        )
        assert_matches_type(CustomerSetBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_set_billing_configurations(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.set_billing_configurations(
            data=[
                {
                    "billing_provider": "stripe",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "azure_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "gcp_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerSetBillingConfigurationsResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_set_billing_configurations(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.set_billing_configurations(
            data=[
                {
                    "billing_provider": "stripe",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "azure_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "aws_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
                {
                    "billing_provider": "gcp_marketplace",
                    "customer_id": "4db51251-61de-4bfe-b9ce-495e244f3491",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerSetBillingConfigurationsResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_ingest_aliases(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.set_ingest_aliases(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ingest_aliases=["team@example.com"],
        )
        assert customer is None

    @parametrize
    async def test_raw_response_set_ingest_aliases(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.set_ingest_aliases(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ingest_aliases=["team@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert customer is None

    @parametrize
    async def test_streaming_response_set_ingest_aliases(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.set_ingest_aliases(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            ingest_aliases=["team@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_ingest_aliases(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.with_raw_response.set_ingest_aliases(
                customer_id="",
                ingest_aliases=["team@example.com"],
            )

    @parametrize
    async def test_method_set_name(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.set_name(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            name="Example, Inc.",
        )
        assert_matches_type(CustomerSetNameResponse, customer, path=["response"])

    @parametrize
    async def test_raw_response_set_name(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.set_name(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            name="Example, Inc.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerSetNameResponse, customer, path=["response"])

    @parametrize
    async def test_streaming_response_set_name(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.set_name(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            name="Example, Inc.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerSetNameResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_set_name(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.with_raw_response.set_name(
                customer_id="",
                name="Example, Inc.",
            )

    @parametrize
    async def test_method_update_config(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert customer is None

    @parametrize
    async def test_method_update_config_with_all_params(self, async_client: AsyncMetronome) -> None:
        customer = await async_client.v1.customers.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            leave_stripe_invoices_in_draft=True,
            salesforce_account_id="0015500001WO1ZiABL",
        )
        assert customer is None

    @parametrize
    async def test_raw_response_update_config(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.customers.with_raw_response.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert customer is None

    @parametrize
    async def test_streaming_response_update_config(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.customers.with_streaming_response.update_config(
            customer_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_config(self, async_client: AsyncMetronome) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v1.customers.with_raw_response.update_config(
                customer_id="",
            )
