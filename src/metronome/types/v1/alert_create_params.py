# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertCreateParams", "CustomFieldFilter", "GroupValue"]


class AlertCreateParams(TypedDict, total=False):
    alert_type: Required[
        Literal[
            "low_credit_balance_reached",
            "spend_threshold_reached",
            "monthly_invoice_total_spend_threshold_reached",
            "low_remaining_days_in_plan_reached",
            "low_remaining_credit_percentage_reached",
            "usage_threshold_reached",
            "low_remaining_days_for_commit_segment_reached",
            "low_remaining_commit_balance_reached",
            "low_remaining_commit_percentage_reached",
            "low_remaining_days_for_contract_credit_segment_reached",
            "low_remaining_contract_credit_balance_reached",
            "low_remaining_contract_credit_percentage_reached",
            "low_remaining_contract_credit_and_commit_balance_reached",
            "invoice_total_reached",
        ]
    ]
    """Type of the alert"""

    name: Required[str]
    """Name of the alert"""

    threshold: Required[float]
    """Threshold value of the alert policy.

    Depending upon the alert type, this number may represent a financial amount, the
    days remaining, or a percentage reached.
    """

    billable_metric_id: str
    """
    For alerts of type `usage_threshold_reached`, specifies which billable metric to
    track the usage for.
    """

    credit_grant_type_filters: List[str]
    """
    An array of strings, representing a way to filter the credit grant this alert
    applies to, by looking at the credit_grant_type field on the credit grant. This
    field is only defined for CreditPercentage and CreditBalance alerts
    """

    credit_type_id: str
    """ID of the credit's currency, defaults to USD.

    If the specific alert type requires a pricing unit/currency, find the ID in the
    [Metronome app](https://app.metronome.com/offering/pricing-units).
    """

    custom_field_filters: Iterable[CustomFieldFilter]
    """A list of custom field filters for alert types that support advanced filtering.

    Only present for contract invoices.
    """

    customer_id: str
    """If provided, will create this alert for this specific customer.

    To create an alert for all customers, do not specify a `customer_id`.
    """

    evaluate_on_create: bool
    """
    If true, the alert will evaluate immediately on customers that already meet the
    alert threshold. If false, it will only evaluate on future customers that
    trigger the alert threshold. Defaults to true.
    """

    group_values: Iterable[GroupValue]
    """Only present for `spend_threshold_reached` alerts.

    Scope alert to a specific group key on individual line items.
    """

    invoice_types_filter: List[str]
    """Only supported for invoice_total_reached alerts.

    A list of invoice types to evaluate.
    """

    plan_id: str
    """If provided, will create this alert for this specific plan.

    To create an alert for all customers, do not specify a `plan_id`.
    """

    uniqueness_key: str
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class CustomFieldFilter(TypedDict, total=False):
    entity: Required[Literal["Contract", "Commit", "ContractCredit"]]

    key: Required[str]

    value: Required[str]


class GroupValue(TypedDict, total=False):
    key: Required[str]

    value: Required[str]
