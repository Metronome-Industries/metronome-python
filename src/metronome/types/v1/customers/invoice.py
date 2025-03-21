# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...shared.rate import Rate
from ...shared.credit_type_data import CreditTypeData

__all__ = [
    "Invoice",
    "LineItem",
    "LineItemAppliedCommitOrCredit",
    "LineItemPostpaidCommit",
    "LineItemSubLineItem",
    "LineItemSubLineItemTierPeriod",
    "LineItemSubLineItemTier",
    "LineItemTier",
    "CorrectionRecord",
    "CorrectionRecordCorrectedExternalInvoice",
    "ExternalInvoice",
    "InvoiceAdjustment",
    "ResellerRoyalty",
    "ResellerRoyaltyAwsOptions",
    "ResellerRoyaltyGcpOptions",
]


class LineItemAppliedCommitOrCredit(BaseModel):
    id: str

    type: Literal["PREPAID", "POSTPAID", "CREDIT"]


class LineItemPostpaidCommit(BaseModel):
    id: str


class LineItemSubLineItemTierPeriod(BaseModel):
    starting_at: datetime

    ending_before: Optional[datetime] = None


class LineItemSubLineItemTier(BaseModel):
    price: float

    quantity: float

    starting_at: float
    """at what metric amount this tier begins"""

    subtotal: float


class LineItemSubLineItem(BaseModel):
    custom_fields: Dict[str, str]

    name: str

    quantity: float

    subtotal: float

    charge_id: Optional[str] = None

    credit_grant_id: Optional[str] = None

    end_date: Optional[datetime] = None
    """The end date for the charge (for seats charges only)."""

    price: Optional[float] = None
    """
    the unit price for this charge, present only if the charge is not tiered and the
    quantity is nonzero
    """

    start_date: Optional[datetime] = None
    """The start date for the charge (for seats charges only)."""

    tier_period: Optional[LineItemSubLineItemTierPeriod] = None
    """when the current tier started and ends (for tiered charges only)"""

    tiers: Optional[List[LineItemSubLineItemTier]] = None


class LineItemTier(BaseModel):
    level: float

    starting_at: str

    size: Optional[str] = None


class LineItem(BaseModel):
    credit_type: CreditTypeData

    name: str

    total: float

    applied_commit_or_credit: Optional[LineItemAppliedCommitOrCredit] = None
    """only present for beta contract invoices"""

    commit_custom_fields: Optional[Dict[str, str]] = None
    """only present for beta contract invoices"""

    commit_id: Optional[str] = None
    """only present for beta contract invoices"""

    commit_netsuite_item_id: Optional[str] = None
    """only present for beta contract invoices.

    This field's availability is dependent on your client's configuration.
    """

    commit_netsuite_sales_order_id: Optional[str] = None
    """only present for beta contract invoices.

    This field's availability is dependent on your client's configuration.
    """

    commit_segment_id: Optional[str] = None
    """only present for beta contract invoices"""

    commit_type: Optional[str] = None
    """only present for beta contract invoices"""

    custom_fields: Optional[Dict[str, str]] = None

    ending_before: Optional[datetime] = None
    """only present for beta contract invoices"""

    group_key: Optional[str] = None

    group_value: Optional[str] = None

    is_prorated: Optional[bool] = None
    """only present for beta contract invoices"""

    list_price: Optional[Rate] = None
    """
    Only present for contract invoices and when the include_list_prices query
    parameter is set to true. This will include the list rate for the charge if
    applicable. Only present for usage and subscription line items.
    """

    metadata: Optional[str] = None

    netsuite_invoice_billing_end: Optional[datetime] = None
    """The end date for the billing period on the invoice."""

    netsuite_invoice_billing_start: Optional[datetime] = None
    """The start date for the billing period on the invoice."""

    netsuite_item_id: Optional[str] = None
    """only present for beta contract invoices.

    This field's availability is dependent on your client's configuration.
    """

    postpaid_commit: Optional[LineItemPostpaidCommit] = None
    """only present for beta contract invoices"""

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None
    """
    if presentation groups are used, this will contain the values used to break down
    the line item
    """

    pricing_group_values: Optional[Dict[str, str]] = None
    """
    if pricing groups are used, this will contain the values used to calculate the
    price
    """

    product_custom_fields: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_type: Optional[str] = None

    professional_service_custom_fields: Optional[Dict[str, str]] = None
    """only present for beta contract invoices"""

    professional_service_id: Optional[str] = None
    """only present for beta contract invoices"""

    quantity: Optional[float] = None

    reseller_type: Optional[Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]] = None

    scheduled_charge_custom_fields: Optional[Dict[str, str]] = None

    scheduled_charge_id: Optional[str] = None
    """only present for beta contract invoices"""

    starting_at: Optional[datetime] = None
    """only present for beta contract invoices"""

    sub_line_items: Optional[List[LineItemSubLineItem]] = None

    tier: Optional[LineItemTier] = None

    unit_price: Optional[float] = None
    """only present for beta contract invoices"""


class CorrectionRecordCorrectedExternalInvoice(BaseModel):
    billing_provider_type: Literal[
        "aws_marketplace",
        "stripe",
        "netsuite",
        "custom",
        "azure_marketplace",
        "quickbooks_online",
        "workday",
        "gcp_marketplace",
    ]

    external_status: Optional[
        Literal[
            "DRAFT",
            "FINALIZED",
            "PAID",
            "UNCOLLECTIBLE",
            "VOID",
            "DELETED",
            "PAYMENT_FAILED",
            "INVALID_REQUEST_ERROR",
            "SKIPPED",
            "SENT",
            "QUEUED",
        ]
    ] = None

    invoice_id: Optional[str] = None

    issued_at_timestamp: Optional[datetime] = None


class CorrectionRecord(BaseModel):
    corrected_invoice_id: str

    memo: str

    reason: str

    corrected_external_invoice: Optional[CorrectionRecordCorrectedExternalInvoice] = None


class ExternalInvoice(BaseModel):
    billing_provider_type: Literal[
        "aws_marketplace",
        "stripe",
        "netsuite",
        "custom",
        "azure_marketplace",
        "quickbooks_online",
        "workday",
        "gcp_marketplace",
    ]

    external_status: Optional[
        Literal[
            "DRAFT",
            "FINALIZED",
            "PAID",
            "UNCOLLECTIBLE",
            "VOID",
            "DELETED",
            "PAYMENT_FAILED",
            "INVALID_REQUEST_ERROR",
            "SKIPPED",
            "SENT",
            "QUEUED",
        ]
    ] = None

    invoice_id: Optional[str] = None

    issued_at_timestamp: Optional[datetime] = None


class InvoiceAdjustment(BaseModel):
    credit_type: CreditTypeData

    name: str

    total: float

    credit_grant_custom_fields: Optional[Dict[str, str]] = None

    credit_grant_id: Optional[str] = None


class ResellerRoyaltyAwsOptions(BaseModel):
    aws_account_number: Optional[str] = None

    aws_offer_id: Optional[str] = None

    aws_payer_reference_id: Optional[str] = None


class ResellerRoyaltyGcpOptions(BaseModel):
    gcp_account_id: Optional[str] = None

    gcp_offer_id: Optional[str] = None


class ResellerRoyalty(BaseModel):
    fraction: str

    netsuite_reseller_id: str

    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

    aws_options: Optional[ResellerRoyaltyAwsOptions] = None

    gcp_options: Optional[ResellerRoyaltyGcpOptions] = None


class Invoice(BaseModel):
    id: str

    credit_type: CreditTypeData

    customer_id: str

    line_items: List[LineItem]

    status: str

    total: float

    type: str

    amendment_id: Optional[str] = None

    billable_status: Optional[Literal["billable", "unbillable"]] = None
    """This field's availability is dependent on your client's configuration."""

    contract_custom_fields: Optional[Dict[str, str]] = None

    contract_id: Optional[str] = None

    correction_record: Optional[CorrectionRecord] = None

    created_at: Optional[datetime] = None
    """When the invoice was created (UTC).

    This field is present for correction invoices only.
    """

    custom_fields: Optional[Dict[str, object]] = None

    customer_custom_fields: Optional[Dict[str, str]] = None

    end_timestamp: Optional[datetime] = None
    """End of the usage period this invoice covers (UTC)"""

    external_invoice: Optional[ExternalInvoice] = None

    invoice_adjustments: Optional[List[InvoiceAdjustment]] = None

    issued_at: Optional[datetime] = None
    """When the invoice was issued (UTC)"""

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    plan_custom_fields: Optional[Dict[str, str]] = None

    plan_id: Optional[str] = None

    plan_name: Optional[str] = None

    reseller_royalty: Optional[ResellerRoyalty] = None
    """only present for beta contract invoices with reseller royalties"""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    start_timestamp: Optional[datetime] = None
    """Beginning of the usage period this invoice covers (UTC)"""

    subtotal: Optional[float] = None
