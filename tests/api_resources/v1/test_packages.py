# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.types.v1 import (
    PackageListResponse,
    PackageCreateResponse,
    PackageArchiveResponse,
    PackageRetrieveResponse,
    PackageListContractsOnPackageResponse,
)
from metronome.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPackages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Metronome) -> None:
        package = client.v1.packages.create(
            name="My package",
        )
        assert_matches_type(PackageCreateResponse, package, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Metronome) -> None:
        package = client.v1.packages.create(
            name="My package",
            aliases=[
                {
                    "name": "name",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            billing_anchor_date="contract_start_date",
            billing_provider="stripe",
            commits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "duration": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "starting_at_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "schedule_items": [
                            {
                                "date_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                    },
                    "name": "x",
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
            contract_name="contract_name",
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "duration": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "starting_at_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
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
            delivery_method="direct_to_billing_provider",
            duration={
                "unit": "DAYS",
                "value": 0,
            },
            multiplier_override_prioritization="LOWEST_MULTIPLIER",
            net_payment_terms_days=0,
            overrides=[
                {
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
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "entitled": True,
                    "is_commit_specific": True,
                    "multiplier": 0,
                    "overwrite_rate": {
                        "rate_type": "FLAT",
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "custom_rate": {"foo": "bar"},
                        "is_prorated": True,
                        "minimum_config": {"minimum": 0},
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
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "invoice_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "quantity": 0,
                        "unit_price": 0,
                    },
                    "name": "x",
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
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "name": "x",
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
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "schedule_items": [
                            {
                                "date_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
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
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "initial_quantity": 0,
                    "name": "name",
                    "quantity_management_mode": "SEAT_BASED",
                    "seat_config": {
                        "seat_group_key": "seat_group_key",
                        "initial_unassigned_seats": 0,
                    },
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "temporary_id": "temporary_id",
                }
            ],
            uniqueness_key="x",
            usage_statement_schedule={
                "frequency": "MONTHLY",
                "day": "FIRST_OF_MONTH",
                "invoice_generation_starting_at_offset": {
                    "unit": "DAYS",
                    "value": 0,
                },
            },
        )
        assert_matches_type(PackageCreateResponse, package, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Metronome) -> None:
        response = client.v1.packages.with_raw_response.create(
            name="My package",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(PackageCreateResponse, package, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Metronome) -> None:
        with client.v1.packages.with_streaming_response.create(
            name="My package",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(PackageCreateResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        package = client.v1.packages.retrieve(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(PackageRetrieveResponse, package, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.packages.with_raw_response.retrieve(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(PackageRetrieveResponse, package, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.packages.with_streaming_response.retrieve(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(PackageRetrieveResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Metronome) -> None:
        package = client.v1.packages.list()
        assert_matches_type(SyncCursorPage[PackageListResponse], package, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Metronome) -> None:
        package = client.v1.packages.list(
            limit=1,
            next_page="next_page",
            archive_filter="ARCHIVED",
        )
        assert_matches_type(SyncCursorPage[PackageListResponse], package, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Metronome) -> None:
        response = client.v1.packages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(SyncCursorPage[PackageListResponse], package, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Metronome) -> None:
        with client.v1.packages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(SyncCursorPage[PackageListResponse], package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Metronome) -> None:
        package = client.v1.packages.archive(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(PackageArchiveResponse, package, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Metronome) -> None:
        response = client.v1.packages.with_raw_response.archive(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(PackageArchiveResponse, package, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Metronome) -> None:
        with client.v1.packages.with_streaming_response.archive(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(PackageArchiveResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_contracts_on_package(self, client: Metronome) -> None:
        package = client.v1.packages.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(SyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

    @parametrize
    def test_method_list_contracts_on_package_with_all_params(self, client: Metronome) -> None:
        package = client.v1.packages.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            limit=1,
            next_page="next_page",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

    @parametrize
    def test_raw_response_list_contracts_on_package(self, client: Metronome) -> None:
        response = client.v1.packages.with_raw_response.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = response.parse()
        assert_matches_type(SyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

    @parametrize
    def test_streaming_response_list_contracts_on_package(self, client: Metronome) -> None:
        with client.v1.packages.with_streaming_response.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = response.parse()
            assert_matches_type(SyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPackages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.create(
            name="My package",
        )
        assert_matches_type(PackageCreateResponse, package, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.create(
            name="My package",
            aliases=[
                {
                    "name": "name",
                    "ending_before": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "starting_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            billing_anchor_date="contract_start_date",
            billing_provider="stripe",
            commits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "duration": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "starting_at_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "type": "PREPAID",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "invoice_schedule": {
                        "schedule_items": [
                            {
                                "date_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "do_not_invoice": True,
                    },
                    "name": "x",
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
            contract_name="contract_name",
            credits=[
                {
                    "access_schedule": {
                        "schedule_items": [
                            {
                                "amount": 0,
                                "duration": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "starting_at_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "custom_fields": {"foo": "string"},
                    "description": "description",
                    "name": "x",
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
            delivery_method="direct_to_billing_provider",
            duration={
                "unit": "DAYS",
                "value": 0,
            },
            multiplier_override_prioritization="LOWEST_MULTIPLIER",
            net_payment_terms_days=0,
            overrides=[
                {
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
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "entitled": True,
                    "is_commit_specific": True,
                    "multiplier": 0,
                    "overwrite_rate": {
                        "rate_type": "FLAT",
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "custom_rate": {"foo": "bar"},
                        "is_prorated": True,
                        "minimum_config": {"minimum": 0},
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
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "invoice_amount": {
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "quantity": 0,
                        "unit_price": 0,
                    },
                    "name": "x",
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
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "applicable_product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                    "applicable_product_tags": ["string"],
                    "description": "description",
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "name": "x",
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
            scheduled_charges=[
                {
                    "product_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "schedule": {
                        "schedule_items": [
                            {
                                "date_offset": {
                                    "unit": "DAYS",
                                    "value": 0,
                                },
                                "quantity": 0,
                                "unit_price": 0,
                            }
                        ],
                        "credit_type_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "custom_fields": {"foo": "string"},
                    "name": "x",
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
                    "duration": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "initial_quantity": 0,
                    "name": "name",
                    "quantity_management_mode": "SEAT_BASED",
                    "seat_config": {
                        "seat_group_key": "seat_group_key",
                        "initial_unassigned_seats": 0,
                    },
                    "starting_at_offset": {
                        "unit": "DAYS",
                        "value": 0,
                    },
                    "temporary_id": "temporary_id",
                }
            ],
            uniqueness_key="x",
            usage_statement_schedule={
                "frequency": "MONTHLY",
                "day": "FIRST_OF_MONTH",
                "invoice_generation_starting_at_offset": {
                    "unit": "DAYS",
                    "value": 0,
                },
            },
        )
        assert_matches_type(PackageCreateResponse, package, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.packages.with_raw_response.create(
            name="My package",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(PackageCreateResponse, package, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.packages.with_streaming_response.create(
            name="My package",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(PackageCreateResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.retrieve(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(PackageRetrieveResponse, package, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.packages.with_raw_response.retrieve(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(PackageRetrieveResponse, package, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.packages.with_streaming_response.retrieve(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(PackageRetrieveResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.list()
        assert_matches_type(AsyncCursorPage[PackageListResponse], package, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.list(
            limit=1,
            next_page="next_page",
            archive_filter="ARCHIVED",
        )
        assert_matches_type(AsyncCursorPage[PackageListResponse], package, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.packages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(AsyncCursorPage[PackageListResponse], package, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.packages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(AsyncCursorPage[PackageListResponse], package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.archive(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )
        assert_matches_type(PackageArchiveResponse, package, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.packages.with_raw_response.archive(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(PackageArchiveResponse, package, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.packages.with_streaming_response.archive(
            package_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(PackageArchiveResponse, package, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_contracts_on_package(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )
        assert_matches_type(AsyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

    @parametrize
    async def test_method_list_contracts_on_package_with_all_params(self, async_client: AsyncMetronome) -> None:
        package = await async_client.v1.packages.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            limit=1,
            next_page="next_page",
            covering_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_archived=True,
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

    @parametrize
    async def test_raw_response_list_contracts_on_package(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.packages.with_raw_response.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        package = await response.parse()
        assert_matches_type(AsyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

    @parametrize
    async def test_streaming_response_list_contracts_on_package(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.packages.with_streaming_response.list_contracts_on_package(
            package_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            package = await response.parse()
            assert_matches_type(AsyncCursorPage[PackageListContractsOnPackageResponse], package, path=["response"])

        assert cast(Any, response.is_closed) is True
