# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.types.v1 import (
    ContractListResponse,
    ContractAmendResponse,
    ContractCreateResponse,
    ContractArchiveResponse,
    ContractRetrieveResponse,
    ContractListBalancesResponse,
    ContractUpdateEndDateResponse,
    ContractRetrieveRateScheduleResponse,
    ContractCreateHistoricalInvoicesResponse,
    ContractScheduleProServicesInvoiceResponse,
    ContractRetrieveSubscriptionQuantityHistoryResponse,
)
from metronome.pagination import SyncBodyCursorPage, AsyncBodyCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        contract = client.v1.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billing_provider_configuration={
                "billing_provider": "stripe",
                "billing_provider_configuration_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "delivery_method": "direct_to_billing_provider",
            },
            commits=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "payment_gate_config": {
                        "payment_gate_type": "NONE",
                        "precalculated_tax_config": {
                            "tax_amount": 0,
                            "tax_name": "tax_name",
                        },
                        "stripe_config": {
                            "payment_type": "INVOICE",
                            "invoice_metadata": {"foo": "string"},
                            "on_session_payment": True,
                        },
                        "tax_type": "NONE",
                    },
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "temporary_id": "temporary_id",
                }
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                }
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            hierarchy_configuration={
                "parent": {
                    "contract_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "parent_behavior": {"invoice_consolidation_type": "CONCATENATE"},
                "payer": "SELF",
                "usage_statement_behavior": "CONSOLIDATE",
            },
            multiplier_override_prioritization="LOWEST_MULTIPLIER",
            name="name",
            net_payment_terms_days=0,
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "is_commit_specific": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "billing_frequency": "MONTHLY",
                            "commit_ids": ["string"],
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                            "recurring_commit_ids": ["string"],
                            "recurring_credit_ids": ["string"],
                        }
                    ],
                    "overwrite_rate": {
                        "rate_type": "FLAT",
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "custom_rate": {"foo": "bar"},
                        "is_prorated": True,
                        "price": 0,
                        "quantity": 0,
                        "tiers": [
                            {
                                "price": 0,
                                "size": 0,
                            }
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "target": "COMMIT_RATE",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        }
                    ],
                    "type": "OVERWRITE",
                }
            ],
            prepaid_balance_threshold_configuration={
                "commit": {
                    "product_id": "product_id",
                    "description": "description",
                    "name": "name",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                },
                "is_enabled": True,
                "payment_gate_config": {
                    "payment_gate_type": "NONE",
                    "precalculated_tax_config": {
                        "tax_amount": 0,
                        "tax_name": "tax_name",
                    },
                    "stripe_config": {
                        "payment_type": "INVOICE",
                        "invoice_metadata": {"foo": "string"},
                    },
                    "tax_type": "NONE",
                },
                "recharge_to_amount": 0,
                "threshold_amount": 0,
                "custom_credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            priority=0,
            professional_services=[
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            rate_card_alias="rate_card_alias",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            recurring_commits=[
                {
                    "access_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "unit_price": 0,
                        "quantity": 0,
                    },
                    "commit_duration": {
                        "value": 0,
                        "unit": "PERIODS",
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "invoice_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "quantity": 0,
                        "unit_price": 0,
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "proration": "NONE",
                    "rate_type": "COMMIT_RATE",
                    "recurrence_frequency": "MONTHLY",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "subscription_config": {
                        "apply_seat_increase_config": {"is_prorated": True},
                        "subscription_id": "subscription_id",
                        "allocation": "INDIVIDUAL",
                    },
                    "temporary_id": "temporary_id",
                }
            ],
            recurring_credits=[
                {
                    "access_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "unit_price": 0,
                        "quantity": 0,
                    },
                    "commit_duration": {
                        "value": 0,
                        "unit": "PERIODS",
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "proration": "NONE",
                    "rate_type": "COMMIT_RATE",
                    "recurrence_frequency": "MONTHLY",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "subscription_config": {
                        "apply_seat_increase_config": {"is_prorated": True},
                        "subscription_id": "subscription_id",
                        "allocation": "INDIVIDUAL",
                    },
                    "temporary_id": "temporary_id",
                }
            ],
            reseller_royalties=[
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "aws_options": {
                        "aws_account_number": "aws_account_number",
                        "aws_offer_id": "aws_offer_id",
                        "aws_payer_reference_id": "aws_payer_reference_id",
                    },
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gcp_options": {
                        "gcp_account_id": "gcp_account_id",
                        "gcp_offer_id": "gcp_offer_id",
                    },
                    "reseller_contract_value": 0,
                }
            ],
            revenue_system_configuration={
                "delivery_method": "direct_to_billing_provider",
                "provider": "netsuite",
                "revenue_system_configuration_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            scheduled_charges_on_usage_invoices="ALL",
            spend_threshold_configuration={
                "commit": {
                    "product_id": "product_id",
                    "description": "description",
                    "name": "name",
                },
                "is_enabled": True,
                "payment_gate_config": {
                    "payment_gate_type": "NONE",
                    "precalculated_tax_config": {
                        "tax_amount": 0,
                        "tax_name": "tax_name",
                    },
                    "stripe_config": {
                        "payment_type": "INVOICE",
                        "invoice_metadata": {"foo": "string"},
                    },
                    "tax_type": "NONE",
                },
                "threshold_amount": 0,
            },
            subscriptions=[
                {
                    "collection_schedule": "ADVANCE",
                    "proration": {
                        "invoice_behavior": "BILL_IMMEDIATELY",
                        "is_prorated": True,
                    },
                    "subscription_rate": {
                        "billing_frequency": "MONTHLY",
                        "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "initial_quantity": 0,
                    "name": "name",
                    "quantity_management_mode": "SEAT_BASED",
                    "seat_config": {
                        "initial_seat_ids": ["string"],
                        "seat_group_key": "seat_group_key",
                        "initial_unassigned_seats": 0,
                    },
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "temporary_id": "temporary_id",
                }
            ],
            total_contract_value=0,
            transition={
                "from_contract_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "type": "SUPERSEDE",
                "future_invoice_behavior": {"trueup": "REMOVE"},
            },
            uniqueness_key="x",
            usage_filter={
                "group_key": "group_key",
                "group_values": ["string"],
                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            usage_statement_schedule={
                "frequency": "MONTHLY",
                "billing_anchor_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "day": "FIRST_OF_MONTH",
                "invoice_generation_starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractCreateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        contract = client.v1.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            include_balance=True,
            include_ledgers=True,
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        contract = client.v1.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_balance=True,
            include_ledgers=True,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractListResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_manual_balance_entry(self, client: Metronome) -> None:
        contract = client.v1.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        )
        assert contract is None

    @parametrize
    def test_method_add_manual_balance_entry_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            per_group_amounts={"foo": 0},
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert contract is None

    @parametrize
    def test_raw_response_add_manual_balance_entry(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert contract is None

    @parametrize
    def test_streaming_response_add_manual_balance_entry(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_amend(self, client: Metronome) -> None:
        contract = client.v1.contracts.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    def test_method_amend_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            commits=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "payment_gate_config": {
                        "payment_gate_type": "NONE",
                        "precalculated_tax_config": {
                            "tax_amount": 0,
                            "tax_name": "tax_name",
                        },
                        "stripe_config": {
                            "payment_type": "INVOICE",
                            "invoice_metadata": {"foo": "string"},
                            "on_session_payment": True,
                        },
                        "tax_type": "NONE",
                    },
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "temporary_id": "temporary_id",
                }
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                }
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "is_commit_specific": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "billing_frequency": "MONTHLY",
                            "commit_ids": ["string"],
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                            "recurring_commit_ids": ["string"],
                            "recurring_credit_ids": ["string"],
                        }
                    ],
                    "overwrite_rate": {
                        "rate_type": "FLAT",
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "custom_rate": {"foo": "bar"},
                        "is_prorated": True,
                        "price": 0,
                        "quantity": 0,
                        "tiers": [
                            {
                                "price": 0,
                                "size": 0,
                            }
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "target": "COMMIT_RATE",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        }
                    ],
                    "type": "OVERWRITE",
                }
            ],
            professional_services=[
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            reseller_royalties=[
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "aws_options": {
                        "aws_account_number": "aws_account_number",
                        "aws_offer_id": "aws_offer_id",
                        "aws_payer_reference_id": "aws_payer_reference_id",
                    },
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fraction": 0,
                    "gcp_options": {
                        "gcp_account_id": "gcp_account_id",
                        "gcp_offer_id": "gcp_offer_id",
                    },
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_contract_value": 0,
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            total_contract_value=0,
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_amend(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_amend(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractAmendResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        contract = client.v1.contracts.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        )
        assert_matches_type(ContractArchiveResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractArchiveResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractArchiveResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_historical_invoices(self, client: Metronome) -> None:
        contract = client.v1.contracts.create_historical_invoices(
            invoices=[
                {
                    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                    "issue_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "usage_line_items": [
                        {
                            "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                            "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                            "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
                        }
                    ],
                }
            ],
            preview=False,
        )
        assert_matches_type(ContractCreateHistoricalInvoicesResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_create_historical_invoices(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.create_historical_invoices(
            invoices=[
                {
                    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                    "issue_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "usage_line_items": [
                        {
                            "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                            "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                            "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
                        }
                    ],
                }
            ],
            preview=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractCreateHistoricalInvoicesResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_create_historical_invoices(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.create_historical_invoices(
            invoices=[
                {
                    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                    "issue_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "usage_line_items": [
                        {
                            "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                            "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                            "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
                        }
                    ],
                }
            ],
            preview=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractCreateHistoricalInvoicesResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_balances(self, client: Metronome) -> None:
        contract = client.v1.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(SyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

    @parametrize
    def test_method_list_balances_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            exclude_zero_balances=True,
            include_archived=True,
            include_balance=True,
            include_contract_balances=True,
            include_ledgers=True,
            limit=1,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

    @parametrize
    def test_raw_response_list_balances(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(SyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

    @parametrize
    def test_streaming_response_list_balances(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(SyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rate_schedule(self, client: Metronome) -> None:
        contract = client.v1.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    def test_method_retrieve_rate_schedule_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            limit=1,
            next_page="next_page",
            at=parse_datetime("2020-01-01T00:00:00.000Z"),
            selectors=[
                {
                    "billing_frequency": "MONTHLY",
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                    "product_tags": ["string"],
                }
            ],
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_retrieve_rate_schedule(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_rate_schedule(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_subscription_quantity_history(self, client: Metronome) -> None:
        contract = client.v1.contracts.retrieve_subscription_quantity_history(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            subscription_id="1a824d53-bde6-4d82-96d7-6347ff227d5c",
        )
        assert_matches_type(ContractRetrieveSubscriptionQuantityHistoryResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_retrieve_subscription_quantity_history(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.retrieve_subscription_quantity_history(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            subscription_id="1a824d53-bde6-4d82-96d7-6347ff227d5c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveSubscriptionQuantityHistoryResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_subscription_quantity_history(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.retrieve_subscription_quantity_history(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            subscription_id="1a824d53-bde6-4d82-96d7-6347ff227d5c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveSubscriptionQuantityHistoryResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_schedule_pro_services_invoice(self, client: Metronome) -> None:
        contract = client.v1.contracts.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[{"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    def test_method_schedule_pro_services_invoice_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amendment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amount": 0,
                    "metadata": "metadata",
                    "netsuite_invoice_billing_end": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "netsuite_invoice_billing_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "quantity": 0,
                    "unit_price": 0,
                }
            ],
            netsuite_invoice_header_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            netsuite_invoice_header_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_schedule_pro_services_invoice(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[{"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_schedule_pro_services_invoice(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[{"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_usage_filter(self, client: Metronome) -> None:
        contract = client.v1.contracts.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert contract is None

    @parametrize
    def test_raw_response_set_usage_filter(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert contract is None

    @parametrize
    def test_streaming_response_set_usage_filter(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_end_date(self, client: Metronome) -> None:
        contract = client.v1.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    def test_method_update_end_date_with_all_params(self, client: Metronome) -> None:
        contract = client.v1.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            allow_ending_before_finalized_invoice=True,
            ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_update_end_date(self, client: Metronome) -> None:
        response = client.v1.contracts.with_raw_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_update_end_date(self, client: Metronome) -> None:
        with client.v1.contracts.with_streaming_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billing_provider_configuration={
                "billing_provider": "stripe",
                "billing_provider_configuration_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "delivery_method": "direct_to_billing_provider",
            },
            commits=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "payment_gate_config": {
                        "payment_gate_type": "NONE",
                        "precalculated_tax_config": {
                            "tax_amount": 0,
                            "tax_name": "tax_name",
                        },
                        "stripe_config": {
                            "payment_type": "INVOICE",
                            "invoice_metadata": {"foo": "string"},
                            "on_session_payment": True,
                        },
                        "tax_type": "NONE",
                    },
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "temporary_id": "temporary_id",
                }
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                }
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            hierarchy_configuration={
                "parent": {
                    "contract_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "customer_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                "parent_behavior": {"invoice_consolidation_type": "CONCATENATE"},
                "payer": "SELF",
                "usage_statement_behavior": "CONSOLIDATE",
            },
            multiplier_override_prioritization="LOWEST_MULTIPLIER",
            name="name",
            net_payment_terms_days=0,
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "is_commit_specific": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "billing_frequency": "MONTHLY",
                            "commit_ids": ["string"],
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                            "recurring_commit_ids": ["string"],
                            "recurring_credit_ids": ["string"],
                        }
                    ],
                    "overwrite_rate": {
                        "rate_type": "FLAT",
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "custom_rate": {"foo": "bar"},
                        "is_prorated": True,
                        "price": 0,
                        "quantity": 0,
                        "tiers": [
                            {
                                "price": 0,
                                "size": 0,
                            }
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "target": "COMMIT_RATE",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        }
                    ],
                    "type": "OVERWRITE",
                }
            ],
            prepaid_balance_threshold_configuration={
                "commit": {
                    "product_id": "product_id",
                    "description": "description",
                    "name": "name",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                },
                "is_enabled": True,
                "payment_gate_config": {
                    "payment_gate_type": "NONE",
                    "precalculated_tax_config": {
                        "tax_amount": 0,
                        "tax_name": "tax_name",
                    },
                    "stripe_config": {
                        "payment_type": "INVOICE",
                        "invoice_metadata": {"foo": "string"},
                    },
                    "tax_type": "NONE",
                },
                "recharge_to_amount": 0,
                "threshold_amount": 0,
                "custom_credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            priority=0,
            professional_services=[
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            rate_card_alias="rate_card_alias",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            recurring_commits=[
                {
                    "access_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "unit_price": 0,
                        "quantity": 0,
                    },
                    "commit_duration": {
                        "value": 0,
                        "unit": "PERIODS",
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "invoice_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "quantity": 0,
                        "unit_price": 0,
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "proration": "NONE",
                    "rate_type": "COMMIT_RATE",
                    "recurrence_frequency": "MONTHLY",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "subscription_config": {
                        "apply_seat_increase_config": {"is_prorated": True},
                        "subscription_id": "subscription_id",
                        "allocation": "INDIVIDUAL",
                    },
                    "temporary_id": "temporary_id",
                }
            ],
            recurring_credits=[
                {
                    "access_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "unit_price": 0,
                        "quantity": 0,
                    },
                    "commit_duration": {
                        "value": 0,
                        "unit": "PERIODS",
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "proration": "NONE",
                    "rate_type": "COMMIT_RATE",
                    "recurrence_frequency": "MONTHLY",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "subscription_config": {
                        "apply_seat_increase_config": {"is_prorated": True},
                        "subscription_id": "subscription_id",
                        "allocation": "INDIVIDUAL",
                    },
                    "temporary_id": "temporary_id",
                }
            ],
            reseller_royalties=[
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "aws_options": {
                        "aws_account_number": "aws_account_number",
                        "aws_offer_id": "aws_offer_id",
                        "aws_payer_reference_id": "aws_payer_reference_id",
                    },
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "gcp_options": {
                        "gcp_account_id": "gcp_account_id",
                        "gcp_offer_id": "gcp_offer_id",
                    },
                    "reseller_contract_value": 0,
                }
            ],
            revenue_system_configuration={
                "delivery_method": "direct_to_billing_provider",
                "provider": "netsuite",
                "revenue_system_configuration_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            scheduled_charges_on_usage_invoices="ALL",
            spend_threshold_configuration={
                "commit": {
                    "product_id": "product_id",
                    "description": "description",
                    "name": "name",
                },
                "is_enabled": True,
                "payment_gate_config": {
                    "payment_gate_type": "NONE",
                    "precalculated_tax_config": {
                        "tax_amount": 0,
                        "tax_name": "tax_name",
                    },
                    "stripe_config": {
                        "payment_type": "INVOICE",
                        "invoice_metadata": {"foo": "string"},
                    },
                    "tax_type": "NONE",
                },
                "threshold_amount": 0,
            },
            subscriptions=[
                {
                    "collection_schedule": "ADVANCE",
                    "proration": {
                        "invoice_behavior": "BILL_IMMEDIATELY",
                        "is_prorated": True,
                    },
                    "subscription_rate": {
                        "billing_frequency": "MONTHLY",
                        "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "initial_quantity": 0,
                    "name": "name",
                    "quantity_management_mode": "SEAT_BASED",
                    "seat_config": {
                        "initial_seat_ids": ["string"],
                        "seat_group_key": "seat_group_key",
                        "initial_unassigned_seats": 0,
                    },
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "temporary_id": "temporary_id",
                }
            ],
            total_contract_value=0,
            transition={
                "from_contract_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "type": "SUPERSEDE",
                "future_invoice_behavior": {"trueup": "REMOVE"},
            },
            uniqueness_key="x",
            usage_filter={
                "group_key": "group_key",
                "group_values": ["string"],
                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            usage_statement_schedule={
                "frequency": "MONTHLY",
                "billing_anchor_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                "day": "FIRST_OF_MONTH",
                "invoice_generation_starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractCreateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            include_balance=True,
            include_ledgers=True,
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_balance=True,
            include_ledgers=True,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractListResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_manual_balance_entry(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        )
        assert contract is None

    @parametrize
    async def test_method_add_manual_balance_entry_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            per_group_amounts={"foo": 0},
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert contract is None

    @parametrize
    async def test_raw_response_add_manual_balance_entry(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert contract is None

    @parametrize
    async def test_streaming_response_add_manual_balance_entry(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_amend(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    async def test_method_amend_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            commits=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "payment_gate_config": {
                        "payment_gate_type": "NONE",
                        "precalculated_tax_config": {
                            "tax_amount": 0,
                            "tax_name": "tax_name",
                        },
                        "stripe_config": {
                            "payment_type": "INVOICE",
                            "invoice_metadata": {"foo": "string"},
                            "on_session_payment": True,
                        },
                        "tax_type": "NONE",
                    },
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "rollover_fraction": 0,
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                    "temporary_id": "temporary_id",
                }
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "hierarchy_configuration": {"child_access": {"type": "ALL"}},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rate_type": "COMMIT_RATE",
                    "specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                        }
                    ],
                }
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "is_commit_specific": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "billing_frequency": "MONTHLY",
                            "commit_ids": ["string"],
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string"],
                            "recurring_commit_ids": ["string"],
                            "recurring_credit_ids": ["string"],
                        }
                    ],
                    "overwrite_rate": {
                        "rate_type": "FLAT",
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "custom_rate": {"foo": "bar"},
                        "is_prorated": True,
                        "price": 0,
                        "quantity": 0,
                        "tiers": [
                            {
                                "price": 0,
                                "size": 0,
                            }
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "target": "COMMIT_RATE",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        }
                    ],
                    "type": "OVERWRITE",
                }
            ],
            professional_services=[
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            reseller_royalties=[
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "aws_options": {
                        "aws_account_number": "aws_account_number",
                        "aws_offer_id": "aws_offer_id",
                        "aws_payer_reference_id": "aws_payer_reference_id",
                    },
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "fraction": 0,
                    "gcp_options": {
                        "gcp_account_id": "gcp_account_id",
                        "gcp_offer_id": "gcp_offer_id",
                    },
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_contract_value": 0,
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                        "recurring_schedule": {
                            "amount_distribution": "DIVIDED",
                            "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "frequency": "MONTHLY",
                            "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "amount": 0,
                            "quantity": 0,
                            "unit_price": 0,
                        },
                        "schedule_items": [
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                }
            ],
            total_contract_value=0,
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_amend(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_amend(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractAmendResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        )
        assert_matches_type(ContractArchiveResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractArchiveResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractArchiveResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_historical_invoices(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.create_historical_invoices(
            invoices=[
                {
                    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                    "issue_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "usage_line_items": [
                        {
                            "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                            "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                            "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
                        }
                    ],
                }
            ],
            preview=False,
        )
        assert_matches_type(ContractCreateHistoricalInvoicesResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_create_historical_invoices(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.create_historical_invoices(
            invoices=[
                {
                    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                    "issue_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "usage_line_items": [
                        {
                            "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                            "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                            "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
                        }
                    ],
                }
            ],
            preview=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractCreateHistoricalInvoicesResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_create_historical_invoices(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.create_historical_invoices(
            invoices=[
                {
                    "contract_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
                    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
                    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
                    "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                    "issue_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                    "usage_line_items": [
                        {
                            "exclusive_end_date": parse_datetime("2020-02-01T00:00:00.000Z"),
                            "inclusive_start_date": parse_datetime("2020-01-01T00:00:00.000Z"),
                            "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",
                        }
                    ],
                }
            ],
            preview=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractCreateHistoricalInvoicesResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_balances(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(AsyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

    @parametrize
    async def test_method_list_balances_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            exclude_zero_balances=True,
            include_archived=True,
            include_balance=True,
            include_contract_balances=True,
            include_ledgers=True,
            limit=1,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

    @parametrize
    async def test_raw_response_list_balances(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(AsyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

    @parametrize
    async def test_streaming_response_list_balances(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(AsyncBodyCursorPage[ContractListBalancesResponse], contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    async def test_method_retrieve_rate_schedule_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            limit=1,
            next_page="next_page",
            at=parse_datetime("2020-01-01T00:00:00.000Z"),
            selectors=[
                {
                    "billing_frequency": "MONTHLY",
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                    "product_tags": ["string"],
                }
            ],
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_subscription_quantity_history(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.retrieve_subscription_quantity_history(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            subscription_id="1a824d53-bde6-4d82-96d7-6347ff227d5c",
        )
        assert_matches_type(ContractRetrieveSubscriptionQuantityHistoryResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_subscription_quantity_history(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.retrieve_subscription_quantity_history(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            subscription_id="1a824d53-bde6-4d82-96d7-6347ff227d5c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveSubscriptionQuantityHistoryResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_subscription_quantity_history(
        self, async_client: AsyncMetronome
    ) -> None:
        async with async_client.v1.contracts.with_streaming_response.retrieve_subscription_quantity_history(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            subscription_id="1a824d53-bde6-4d82-96d7-6347ff227d5c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveSubscriptionQuantityHistoryResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_schedule_pro_services_invoice(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[{"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    async def test_method_schedule_pro_services_invoice_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {
                    "professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amendment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amount": 0,
                    "metadata": "metadata",
                    "netsuite_invoice_billing_end": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "netsuite_invoice_billing_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "quantity": 0,
                    "unit_price": 0,
                }
            ],
            netsuite_invoice_header_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            netsuite_invoice_header_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_schedule_pro_services_invoice(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[{"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_schedule_pro_services_invoice(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[{"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_usage_filter(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert contract is None

    @parametrize
    async def test_raw_response_set_usage_filter(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert contract is None

    @parametrize
    async def test_streaming_response_set_usage_filter(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_end_date(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    async def test_method_update_end_date_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.v1.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            allow_ending_before_finalized_invoice=True,
            ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.with_raw_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.with_streaming_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True
