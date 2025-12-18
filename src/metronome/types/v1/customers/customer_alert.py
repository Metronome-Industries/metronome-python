# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...shared.credit_type_data import CreditTypeData

__all__ = [
    "CustomerAlert",
    "Alert",
    "AlertCustomFieldFilter",
    "AlertGroupKeyFilter",
    "AlertGroupValue",
    "AlertSeatFilter",
]


class AlertCustomFieldFilter(BaseModel):
    entity: Literal["Contract", "Commit", "ContractCredit"]

    key: str

    value: str


class AlertGroupKeyFilter(BaseModel):
    """
    Scopes threshold notification evaluation to a specific presentation group key on individual line items. Only present for spend notifications.
    """

    key: str

    value: str


class AlertGroupValue(BaseModel):
    key: str

    value: Optional[str] = None


class AlertSeatFilter(BaseModel):
    """Only present for low_remaining_seat_balance_reached notifications.

    The seat group key or seat group key-value pair the alert is scoped to.
    """

    seat_group_key: str
    """The seat group key (e.g., "seat_id", "user_id") that the alert is scoped to."""

    seat_group_value: Optional[str] = None
    """The seat group value that the alert is scoped to."""


class Alert(BaseModel):
    id: str
    """the Metronome ID of the threshold notification"""

    name: str
    """Name of the threshold notification"""

    status: Literal["enabled", "archived", "disabled"]
    """Status of the threshold notification"""

    threshold: float
    """Threshold value of the notification policy"""

    type: Literal[
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
        "low_remaining_seat_balance_reached",
        "invoice_total_reached",
    ]
    """Type of the threshold notification"""

    updated_at: datetime
    """Timestamp for when the threshold notification was last updated"""

    credit_grant_type_filters: Optional[List[str]] = None
    """
    An array of strings, representing a way to filter the credit grant this
    threshold notification applies to, by looking at the credit_grant_type field on
    the credit grant. This field is only defined for CreditPercentage and
    CreditBalance notifications
    """

    credit_type: Optional[CreditTypeData] = None

    custom_field_filters: Optional[List[AlertCustomFieldFilter]] = None
    """
    A list of custom field filters for notification types that support advanced
    filtering
    """

    group_key_filter: Optional[AlertGroupKeyFilter] = None
    """
    Scopes threshold notification evaluation to a specific presentation group key on
    individual line items. Only present for spend notifications.
    """

    group_values: Optional[List[AlertGroupValue]] = None
    """Only present for `spend_threshold_reached` notifications.

    Scope notification to a specific group key on individual line items.
    """

    invoice_types_filter: Optional[List[str]] = None
    """Only supported for invoice_total_reached threshold notifications.

    A list of invoice types to evaluate.
    """

    seat_filter: Optional[AlertSeatFilter] = None
    """Only present for low_remaining_seat_balance_reached notifications.

    The seat group key or seat group key-value pair the alert is scoped to.
    """

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class CustomerAlert(BaseModel):
    alert: Alert

    customer_status: Optional[Literal["ok", "in_alarm", "evaluating"]] = None
    """The status of the threshold notification.

    If the notification is archived, null will be returned.
    """

    triggered_by: Optional[str] = None
    """If present, indicates the reason the threshold notification was triggered."""
