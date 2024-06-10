# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertCreateParams", "CustomFieldFilter", "GroupKeyFilter"]


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
            "invoice_total_reached",
        ]
    ]
    """Type of the alert"""

    name: Required[str]
    """Name of the alert"""

    threshold: Required[float]
    """Threshold value of the alert policy"""

    billable_metric_id: str
    """
    For alerts of type `usage_threshold_reached`, specifies which billable metric to
    track the usage for.
    """

    credit_type_id: str

    custom_field_filters: Iterable[CustomFieldFilter]
    """Only present for beta contract invoices.

    This field's availability is dependent on your client's configuration. A list of
    custom field filters for alert types that support advanced filtering
    """

    customer_id: str
    """If provided, will create this alert for this specific customer.

    To create an alert for all customers, do not specify `customer_id` or `plan_id`.
    """

    evaluate_on_create: bool
    """
    If true, the alert will evaluate immediately on customers that already meet the
    alert threshold. If false, it will only evaluate on future customers that
    trigger the alert threshold. Defaults to true.
    """

    group_key_filter: GroupKeyFilter
    """
    Scopes alert evaluation to a specific presentation group key on individual line
    items. Only present for spend alerts.
    """

    invoice_types_filter: List[str]
    """Only supported for invoice_total_reached alerts.

    A list of invoice types to evaluate.
    """

    plan_id: str
    """If provided, will create this alert for this specific plan.

    To create an alert for all customers, do not specify `customer_id` or `plan_id`.
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


class GroupKeyFilter(TypedDict, total=False):
    key: Required[str]

    value: Required[str]
