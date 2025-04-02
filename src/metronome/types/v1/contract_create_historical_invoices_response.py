# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ContractCreateHistoricalInvoicesResponse",
    "Data",
    "DataCreditType",
    "DataLineItem",
    "DataLineItemCreditType",
    "DataLineItemAppliedCommitOrCredit",
    "DataLineItemListPrice",
    "DataLineItemListPriceCreditType",
    "DataLineItemListPriceTier",
    "DataLineItemPostpaidCommit",
    "DataLineItemSubLineItem",
    "DataLineItemSubLineItemTierPeriod",
    "DataLineItemSubLineItemTier",
    "DataLineItemTier",
    "DataCorrectionRecord",
    "DataCorrectionRecordCorrectedExternalInvoice",
    "DataExternalInvoice",
    "DataInvoiceAdjustment",
    "DataInvoiceAdjustmentCreditType",
    "DataResellerRoyalty",
    "DataResellerRoyaltyAwsOptions",
    "DataResellerRoyaltyGcpOptions",
]


class DataCreditType(BaseModel):
    id: str

    name: str


class DataLineItemCreditType(BaseModel):
    id: str

    name: str


class DataLineItemAppliedCommitOrCredit(BaseModel):
    id: str

    type: Literal["PREPAID", "POSTPAID", "CREDIT"]


class DataLineItemListPriceCreditType(BaseModel):
    id: str

    name: str


class DataLineItemListPriceTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataLineItemListPrice(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]

    credit_type: Optional[DataLineItemListPriceCreditType] = None

    custom_rate: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    pricing_group_values: Optional[Dict[str, str]] = None
    """
    if pricing groups are used, this will contain the values used to calculate the
    price
    """

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Optional[List[DataLineItemListPriceTier]] = None
    """Only set for TIERED rate_type."""

    use_list_prices: Optional[bool] = None
    """Only set for PERCENTAGE rate_type.

    Defaults to false. If true, rate is computed using list prices rather than the
    standard rates for this product on the contract.
    """


class DataLineItemPostpaidCommit(BaseModel):
    id: str


class DataLineItemSubLineItemTierPeriod(BaseModel):
    starting_at: datetime

    ending_before: Optional[datetime] = None


class DataLineItemSubLineItemTier(BaseModel):
    price: float

    quantity: float

    starting_at: float
    """at what metric amount this tier begins"""

    subtotal: float


class DataLineItemSubLineItem(BaseModel):
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

    tier_period: Optional[DataLineItemSubLineItemTierPeriod] = None
    """when the current tier started and ends (for tiered charges only)"""

    tiers: Optional[List[DataLineItemSubLineItemTier]] = None


class DataLineItemTier(BaseModel):
    level: float

    starting_at: str

    size: Optional[str] = None


class DataLineItem(BaseModel):
    credit_type: DataLineItemCreditType

    name: str

    total: float

    applied_commit_or_credit: Optional[DataLineItemAppliedCommitOrCredit] = None
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

    list_price: Optional[DataLineItemListPrice] = None
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

    postpaid_commit: Optional[DataLineItemPostpaidCommit] = None
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

    sub_line_items: Optional[List[DataLineItemSubLineItem]] = None

    tier: Optional[DataLineItemTier] = None

    unit_price: Optional[float] = None
    """only present for beta contract invoices"""


class DataCorrectionRecordCorrectedExternalInvoice(BaseModel):
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


class DataCorrectionRecord(BaseModel):
    corrected_invoice_id: str

    memo: str

    reason: str

    corrected_external_invoice: Optional[DataCorrectionRecordCorrectedExternalInvoice] = None


class DataExternalInvoice(BaseModel):
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


class DataInvoiceAdjustmentCreditType(BaseModel):
    id: str

    name: str


class DataInvoiceAdjustment(BaseModel):
    credit_type: DataInvoiceAdjustmentCreditType

    name: str

    total: float

    credit_grant_custom_fields: Optional[Dict[str, str]] = None

    credit_grant_id: Optional[str] = None


class DataResellerRoyaltyAwsOptions(BaseModel):
    aws_account_number: Optional[str] = None

    aws_offer_id: Optional[str] = None

    aws_payer_reference_id: Optional[str] = None


class DataResellerRoyaltyGcpOptions(BaseModel):
    gcp_account_id: Optional[str] = None

    gcp_offer_id: Optional[str] = None


class DataResellerRoyalty(BaseModel):
    fraction: str

    netsuite_reseller_id: str

    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

    aws_options: Optional[DataResellerRoyaltyAwsOptions] = None

    gcp_options: Optional[DataResellerRoyaltyGcpOptions] = None


class Data(BaseModel):
    id: str

    credit_type: DataCreditType

    customer_id: str

    line_items: List[DataLineItem]

    status: str

    total: float

    type: str

    amendment_id: Optional[str] = None

    billable_status: Optional[Literal["billable", "unbillable"]] = None
    """This field's availability is dependent on your client's configuration."""

    contract_custom_fields: Optional[Dict[str, str]] = None

    contract_id: Optional[str] = None

    correction_record: Optional[DataCorrectionRecord] = None

    created_at: Optional[datetime] = None
    """When the invoice was created (UTC).

    This field is present for correction invoices only.
    """

    custom_fields: Optional[Dict[str, object]] = None

    customer_custom_fields: Optional[Dict[str, str]] = None

    end_timestamp: Optional[datetime] = None
    """End of the usage period this invoice covers (UTC)"""

    external_invoice: Optional[DataExternalInvoice] = None

    invoice_adjustments: Optional[List[DataInvoiceAdjustment]] = None

    issued_at: Optional[datetime] = None
    """When the invoice was issued (UTC)"""

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    plan_custom_fields: Optional[Dict[str, str]] = None

    plan_id: Optional[str] = None

    plan_name: Optional[str] = None

    reseller_royalty: Optional[DataResellerRoyalty] = None
    """only present for beta contract invoices with reseller royalties"""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    start_timestamp: Optional[datetime] = None
    """Beginning of the usage period this invoice covers (UTC)"""

    subtotal: Optional[float] = None


class ContractCreateHistoricalInvoicesResponse(BaseModel):
    data: List[Data]
