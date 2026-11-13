# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CustomerRetrieveBillingConfigurationsResponse",
    "Data",
    "DataConfiguration",
    "DataUnbillableInvoicesConfiguration",
]


class DataConfiguration(BaseModel):
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider.
    """

    aws_customer_account_id: Optional[str] = None
    """AWS Marketplace only.

    The buyer's 12 digit AWS account ID. Must be sent together with
    `aws_license_arn`.
    """

    aws_license_arn: Optional[str] = None
    """AWS Marketplace only.

    The ARN of the buyer's AWS License Manager license for this purchase. Must be
    sent together with `aws_customer_account_id`.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class DataUnbillableInvoicesConfiguration(BaseModel):
    """
    An individual rule that, when evaluated to true, indicates that any invoices for this billing provider will not be sent to its associated destination for the associated contract. Rules only apply to the specified `invoice_type` (or all invoices if omitted) and `fiat_credit_type_id` (or all invoices if omitted). Rule precedence is evaluated from more specific to less specific. This method will fail with a 400 if multiple rules with the same specificity are included.
    """

    invoice_type: Literal["USAGE", "SCHEDULED"]
    """The type of invoice this rule applies to."""

    fiat_credit_type_id: Optional[str] = None
    """Restricts the rule to invoices in this fiat currency.

    Omit for a catch-all rule that applies to every currency of the `invoice_type`.
    Required when `max_amount` is set.
    """

    max_amount: Optional[float] = None
    """A positive decimal, in the units of `fiat_credit_type_id`.

    Only invoices whose total is at or below this amount are suppressed; a higher
    total is still sent to the billing provider. When omitted, every matching
    invoice is suppressed regardless of amount.
    """


class Data(BaseModel):
    id: str
    """
    ID of this configuration; can be provided as the
    billing_provider_configuration_id when creating a contract.
    """

    archived_at: Optional[datetime] = None

    billing_provider: Literal[
        "aws_marketplace",
        "stripe",
        "netsuite",
        "custom",
        "azure_marketplace",
        "quickbooks_online",
        "workday",
        "gcp_marketplace",
        "metronome",
    ]
    """The billing provider set for this configuration."""

    configuration: DataConfiguration
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider.
    """

    customer_id: str

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]
    """The method to use for delivering invoices to this customer."""

    delivery_method_configuration: Dict[str, object]
    """Configuration for the delivery method.

    The structure of this object is specific to the delivery method.
    """

    delivery_method_id: str
    """ID of the delivery method to use for this customer."""

    unbillable_invoices_configuration: Optional[List[DataUnbillableInvoicesConfiguration]] = None
    """Rules that stop matching invoices from being sent to the billing provider.

    Supported for Stripe, NetSuite, AWS Marketplace, Azure, and GCP billing provider
    configurations. When omitted, every invoice is sent to the billing provider.
    Stripe invoices can be force-sent after a rule suppresses them.
    """


class CustomerRetrieveBillingConfigurationsResponse(BaseModel):
    data: List[Data]
