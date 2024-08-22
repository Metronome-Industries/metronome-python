# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types import (
    ContractListResponse,
    ContractAmendResponse,
    ContractCreateResponse,
    ContractArchiveResponse,
    ContractRetrieveResponse,
    ContractListBalancesResponse,
    ContractUpdateEndDateResponse,
    ContractRetrieveRateScheduleResponse,
    ContractScheduleProServicesInvoiceResponse,
)
from metronome._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        contract = client.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billing_provider_configuration={
                "billing_provider": "aws_marketplace",
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
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            multiplier_override_prioritization="LOWEST_MULTIPLIER",
            name="name",
            net_payment_terms_days=0,
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
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
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            rate_card_alias="rate_card_alias",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            reseller_royalties=[
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
            ],
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
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
                "group_values": ["string", "string", "string"],
                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            usage_statement_schedule={
                "frequency": "MONTHLY",
                "day": "FIRST_OF_MONTH",
                "invoice_generation_starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.contracts.with_streaming_response.create(
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
        contract = client.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            include_ledgers=True,
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.contracts.with_streaming_response.retrieve(
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
        contract = client.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_ledgers=True,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.contracts.with_streaming_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractListResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_manual_balance_entry(self, client: Metronome) -> None:
        contract = client.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        )
        assert contract is None

    @parametrize
    def test_method_add_manual_balance_entry_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert contract is None

    @parametrize
    def test_raw_response_add_manual_balance_entry(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.add_manual_balance_entry(
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
        with client.contracts.with_streaming_response.add_manual_balance_entry(
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
        contract = client.contracts.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    def test_method_amend_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.amend(
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
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
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
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            reseller_royalties=[
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
            ],
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            total_contract_value=0,
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_amend(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.amend(
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
        with client.contracts.with_streaming_response.amend(
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
        contract = client.contracts.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        )
        assert_matches_type(ContractArchiveResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.archive(
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
        with client.contracts.with_streaming_response.archive(
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
    def test_method_list_balances(self, client: Metronome) -> None:
        contract = client.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

    @parametrize
    def test_method_list_balances_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_contract_balances=True,
            include_ledgers=True,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_list_balances(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_list_balances(self, client: Metronome) -> None:
        with client.contracts.with_streaming_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rate_schedule(self, client: Metronome) -> None:
        contract = client.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    def test_method_retrieve_rate_schedule_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            limit=1,
            next_page="next_page",
            at=parse_datetime("2020-01-01T00:00:00.000Z"),
            selectors=[
                {
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                    "product_tags": ["string", "string", "string"],
                }
            ],
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_retrieve_rate_schedule(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_rate_schedule(self, client: Metronome) -> None:
        with client.contracts.with_streaming_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_schedule_pro_services_invoice(self, client: Metronome) -> None:
        contract = client.contracts.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    def test_method_schedule_pro_services_invoice_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.schedule_pro_services_invoice(
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
                },
                {
                    "professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amendment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amount": 0,
                    "metadata": "metadata",
                    "netsuite_invoice_billing_end": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "netsuite_invoice_billing_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "quantity": 0,
                    "unit_price": 0,
                },
                {
                    "professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amendment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amount": 0,
                    "metadata": "metadata",
                    "netsuite_invoice_billing_end": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "netsuite_invoice_billing_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "quantity": 0,
                    "unit_price": 0,
                },
            ],
            netsuite_invoice_header_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            netsuite_invoice_header_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_schedule_pro_services_invoice(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_schedule_pro_services_invoice(self, client: Metronome) -> None:
        with client.contracts.with_streaming_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_usage_filter(self, client: Metronome) -> None:
        contract = client.contracts.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert contract is None

    @parametrize
    def test_raw_response_set_usage_filter(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.set_usage_filter(
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
        with client.contracts.with_streaming_response.set_usage_filter(
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
        contract = client.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    def test_method_update_end_date_with_all_params(self, client: Metronome) -> None:
        contract = client.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_update_end_date(self, client: Metronome) -> None:
        response = client.contracts.with_raw_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_update_end_date(self, client: Metronome) -> None:
        with client.contracts.with_streaming_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            billing_provider_configuration={
                "billing_provider": "aws_marketplace",
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
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            ending_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            multiplier_override_prioritization="LOWEST_MULTIPLIER",
            name="name",
            net_payment_terms_days=0,
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
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
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            rate_card_alias="rate_card_alias",
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            reseller_royalties=[
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "fraction": 0,
                    "netsuite_reseller_id": "netsuite_reseller_id",
                    "reseller_type": "AWS",
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
            ],
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
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
                "group_values": ["string", "string", "string"],
                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            usage_statement_schedule={
                "frequency": "MONTHLY",
                "day": "FIRST_OF_MONTH",
                "invoice_generation_starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractCreateResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.contracts.with_streaming_response.create(
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
        contract = await async_client.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            include_ledgers=True,
        )
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.retrieve(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.contracts.with_streaming_response.retrieve(
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
        contract = await async_client.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_ledgers=True,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractListResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.contracts.with_streaming_response.list(
            customer_id="9b85c1c1-5238-4f2a-a409-61412905e1e1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractListResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_manual_balance_entry(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
        )
        assert contract is None

    @parametrize
    async def test_method_add_manual_balance_entry_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.add_manual_balance_entry(
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            amount=-1000,
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            reason="Reason for entry",
            segment_id="66368e29-3f97-4d15-a6e9-120897f0070a",
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert contract is None

    @parametrize
    async def test_raw_response_add_manual_balance_entry(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.add_manual_balance_entry(
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
        async with async_client.contracts.with_streaming_response.add_manual_balance_entry(
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
        contract = await async_client.contracts.amend(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    async def test_method_amend_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.amend(
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
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "amount": 0,
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                    "rollover_fraction": 0,
                },
            ],
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                            {
                                "amount": 0,
                                "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            },
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                    "priority": 0,
                },
            ],
            custom_fields={"foo": "string"},
            discounts=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            netsuite_sales_order_id="netsuite_sales_order_id",
            overrides=[
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
                {
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "applicable_product_tags": ["string", "string", "string"],
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "entitled": True,
                    "multiplier": 0,
                    "override_specifiers": [
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
                        {
                            "presentation_group_values": {"foo": "string"},
                            "pricing_group_values": {"foo": "string"},
                            "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "product_tags": ["string", "string", "string"],
                        },
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
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                            {
                                "price": 0,
                                "size": 0,
                            },
                        ],
                    },
                    "priority": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tiers": [
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                        {
                            "multiplier": 0,
                            "size": 0,
                        },
                    ],
                    "type": "OVERWRITE",
                },
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
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "max_amount": 0,
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "quantity": 0,
                    "unit_price": 0,
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            reseller_royalties=[
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
                {
                    "reseller_type": "AWS",
                    "applicable_product_ids": [
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    ],
                    "applicable_product_tags": ["string", "string", "string"],
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
                },
            ],
            salesforce_opportunity_id="salesforce_opportunity_id",
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                            {
                                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "amount": 0,
                                "quantity": 0,
                                "unit_price": 0,
                            },
                        ],
                    },
                    "name": "x",
                    "netsuite_sales_order_id": "netsuite_sales_order_id",
                },
            ],
            total_contract_value=0,
        )
        assert_matches_type(ContractAmendResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_amend(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.amend(
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
        async with async_client.contracts.with_streaming_response.amend(
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
        contract = await async_client.contracts.archive(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            void_invoices=True,
        )
        assert_matches_type(ContractArchiveResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.archive(
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
        async with async_client.contracts.with_streaming_response.archive(
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
    async def test_method_list_balances(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

    @parametrize
    async def test_method_list_balances_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            id="6162d87b-e5db-4a33-b7f2-76ce6ead4e85",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            effective_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            include_contract_balances=True,
            include_ledgers=True,
            next_page="next_page",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_list_balances(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_list_balances(self, async_client: AsyncMetronome) -> None:
        async with async_client.contracts.with_streaming_response.list_balances(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractListBalancesResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    async def test_method_retrieve_rate_schedule_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            limit=1,
            next_page="next_page",
            at=parse_datetime("2020-01-01T00:00:00.000Z"),
            selectors=[
                {
                    "partial_pricing_group_values": {
                        "region": "us-west-2",
                        "cloud": "aws",
                    },
                    "pricing_group_values": {"foo": "string"},
                    "product_id": "d6300dbb-882e-4d2d-8dec-5125d16b65d0",
                    "product_tags": ["string", "string", "string"],
                }
            ],
        )
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_rate_schedule(self, async_client: AsyncMetronome) -> None:
        async with async_client.contracts.with_streaming_response.retrieve_rate_schedule(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractRetrieveRateScheduleResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_schedule_pro_services_invoice(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    async def test_method_schedule_pro_services_invoice_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.schedule_pro_services_invoice(
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
                },
                {
                    "professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amendment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amount": 0,
                    "metadata": "metadata",
                    "netsuite_invoice_billing_end": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "netsuite_invoice_billing_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "quantity": 0,
                    "unit_price": 0,
                },
                {
                    "professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amendment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "amount": 0,
                    "metadata": "metadata",
                    "netsuite_invoice_billing_end": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "netsuite_invoice_billing_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "quantity": 0,
                    "unit_price": 0,
                },
            ],
            netsuite_invoice_header_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            netsuite_invoice_header_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_schedule_pro_services_invoice(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_schedule_pro_services_invoice(self, async_client: AsyncMetronome) -> None:
        async with async_client.contracts.with_streaming_response.schedule_pro_services_invoice(
            contract_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            issued_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            line_items=[
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"professional_service_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractScheduleProServicesInvoiceResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_usage_filter(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.set_usage_filter(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            group_key="business_subscription_id",
            group_values=["ID-1", "ID-2"],
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert contract is None

    @parametrize
    async def test_raw_response_set_usage_filter(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.set_usage_filter(
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
        async with async_client.contracts.with_streaming_response.set_usage_filter(
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
        contract = await async_client.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    async def test_method_update_end_date_with_all_params(self, async_client: AsyncMetronome) -> None:
        contract = await async_client.contracts.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            ending_before=parse_datetime("2020-01-01T00:00:00.000Z"),
        )
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        response = await async_client.contracts.with_raw_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_update_end_date(self, async_client: AsyncMetronome) -> None:
        async with async_client.contracts.with_streaming_response.update_end_date(
            contract_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractUpdateEndDateResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True
