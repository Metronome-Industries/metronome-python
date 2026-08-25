# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "Subscription",
    "BillingPeriods",
    "BillingPeriodsCurrent",
    "BillingPeriodsNext",
    "BillingPeriodsPrevious",
    "Proration",
    "ProrationRounding",
    "QuantitySchedule",
    "SubscriptionRate",
    "SubscriptionRateProduct",
    "BillingCycleConfig",
    "SeatConfig",
]


class BillingPeriodsCurrent(BaseModel):
    ending_before: datetime

    starting_at: datetime


class BillingPeriodsNext(BaseModel):
    ending_before: datetime

    starting_at: datetime


class BillingPeriodsPrevious(BaseModel):
    ending_before: datetime

    starting_at: datetime


class BillingPeriods(BaseModel):
    """Previous, current, and next billing periods for the subscription."""

    current: Optional[BillingPeriodsCurrent] = None

    next: Optional[BillingPeriodsNext] = None

    previous: Optional[BillingPeriodsPrevious] = None


class ProrationRounding(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit. For USD, this
    means rounding to the nearest dollar).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class Proration(BaseModel):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]

    is_prorated: bool

    rounding: Optional[ProrationRounding] = None


class QuantitySchedule(BaseModel):
    quantity: float

    starting_at: datetime

    ending_before: Optional[datetime] = None


class SubscriptionRateProduct(BaseModel):
    id: str

    name: str


class SubscriptionRate(BaseModel):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    product: SubscriptionRateProduct


class BillingCycleConfig(BaseModel):
    anchor_date: datetime
    """The date this subscription's billing cycle is anchored to."""

    invoice_placement: Literal["ON_SCHEDULED_INVOICE", "ON_USAGE_INVOICE"]
    """
    Controls whether this subscription consolidates onto usage invoices or gets its
    own scheduled invoice.
    """


class SeatConfig(BaseModel):
    seat_group_key: str
    """
    The property name, sent on usage events, that identifies the seat ID associated
    with the usage event. For example, the property name might be seat_id or
    user_id. The property must be set as a group key on billable metrics and a
    presentation/pricing group key on contract products. This allows linked
    recurring credits with an allocation per seat to be consumed by only one seat's
    usage.
    """


class Subscription(BaseModel):
    billing_periods: BillingPeriods
    """Previous, current, and next billing periods for the subscription."""

    collection_schedule: Literal["ADVANCE", "ARREARS"]

    proration: Proration

    quantity_management_mode: Literal["SEAT_BASED", "QUANTITY_ONLY"]
    """Determines how the subscription's quantity is controlled.

    Defaults to QUANTITY_ONLY. **QUANTITY_ONLY**: The subscription quantity is
    specified directly on the subscription. `initial_quantity` must be provided with
    this option. Compatible with recurring commits/credits that use POOLED
    allocation. **SEAT_BASED**: Use when you want to pass specific seat identifiers
    (e.g. add user_123) to increment and decrement a subscription quantity, rather
    than directly providing the quantity. You must use a **SEAT_BASED** subscription
    to use a linked recurring credit with an allocation per seat. `seat_config` must
    be provided with this option.
    """

    quantity_schedule: List[QuantitySchedule]
    """List of quantity schedule items for the subscription.

    Only includes the current quantity and future quantity changes.
    """

    starting_at: datetime

    subscription_rate: SubscriptionRate

    id: Optional[str] = None

    billing_cycle_config: Optional[BillingCycleConfig] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    ending_before: Optional[datetime] = None

    fiat_credit_type_id: Optional[str] = None

    name: Optional[str] = None

    product_custom_fields: Optional[Dict[str, str]] = None
    """
    Custom fields from the subscription product referenced by
    `subscription_rate.product`. These are distinct from the subscription instance's
    `custom_fields`.
    """

    seat_config: Optional[SeatConfig] = None
