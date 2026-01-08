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
    "LineItemOrigin",
    "LineItemPostpaidCommit",
    "LineItemSubLineItem",
    "LineItemSubLineItemTierPeriod",
    "LineItemSubLineItemTier",
    "LineItemTier",
    "ConstituentInvoice",
    "CorrectionRecord",
    "CorrectionRecordCorrectedExternalInvoice",
    "CorrectionRecordCorrectedExternalInvoiceTax",
    "ExternalInvoice",
    "ExternalInvoiceTax",
    "InvoiceAdjustment",
    "Payer",
    "ResellerRoyalty",
    "ResellerRoyaltyAwsOptions",
    "ResellerRoyaltyGcpOptions",
]


class LineItemAppliedCommitOrCredit(BaseModel):
    """Details about the credit or commit that was applied to this line item.

    Only present on line items with product of `USAGE`, `SUBSCRIPTION` or `COMPOSITE` types.
    """

    id: str

    type: Literal["PREPAID", "POSTPAID", "CREDIT"]


class LineItemOrigin(BaseModel):
    """
    Account hierarchy M3 - Present on line items from invoices with type USAGE_CONSOLIDATED. Indicates the original customer, contract, invoice and line item from which this line item was copied.
    """

    contract_id: str

    customer_id: str

    invoice_id: str

    line_item_id: str


class LineItemPostpaidCommit(BaseModel):
    """Only present for line items paying for a postpaid commit true-up."""

    id: str


class LineItemSubLineItemTierPeriod(BaseModel):
    """when the current tier started and ends (for tiered charges only)"""

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
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

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
    """Populated if the line item has a tiered price."""

    level: float

    starting_at: str

    size: Optional[str] = None


class LineItem(BaseModel):
    credit_type: CreditTypeData

    name: str

    total: float

    type: str
    """The type of line item.

    - `scheduled`: Line item is associated with a scheduled charge. View the
      scheduled_charge_id on the line item.
    - `commit_purchase`: Line item is associated with a payment for a prepaid
      commit. View the commit_id on the line item.
    - `usage`: Line item is associated with a usage product or composite product.
      View the product_id on the line item to determine which product.
    - `subscription`: Line item is associated with a subscription. e.g. monthly
      recurring payment for an in-advance subscription.
    - `applied_commit_or_credit`: On metronome invoices, applied commits and credits
      are associated with their own line items. These line items have negative
      totals. Use the applied_commit_or_credit object on the line item to understand
      the id of the applied commit or credit, and its type. Note that the
      application of a postpaid commit is associated with a line item, but the total
      on the line item is not included in the invoice's total as postpaid commits
      are paid in-arrears.
    - `cpu_conversion`: Line item converting between a custom pricing unit and fiat
      currency, using the conversion rate set on the rate card. This line item will
      appear when there are products priced in custom pricing units, and there is
      insufficient prepaid commit/credit in that custom pricing unit to fully cover
      the spend. Then, the outstanding spend in custom pricing units will be
      converted to fiat currency using a cpu_conversion line item.
    """

    applied_commit_or_credit: Optional[LineItemAppliedCommitOrCredit] = None
    """Details about the credit or commit that was applied to this line item.

    Only present on line items with product of `USAGE`, `SUBSCRIPTION` or
    `COMPOSITE` types.
    """

    commit_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    commit_id: Optional[str] = None
    """
    For line items with product of `USAGE`, `SUBSCRIPTION`, or `COMPOSITE` types,
    the ID of the credit or commit that was applied to this line item. For line
    items with product type of `FIXED`, the ID of the prepaid or postpaid commit
    that is being paid for.
    """

    commit_netsuite_item_id: Optional[str] = None

    commit_netsuite_sales_order_id: Optional[str] = None

    commit_segment_id: Optional[str] = None

    commit_type: Optional[str] = None
    """
    `PrepaidCommit` (for commit types `PREPAID` and `CREDIT`) or `PostpaidCommit`
    (for commit type `POSTPAID`).
    """

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    discount_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    discount_id: Optional[str] = None
    """ID of the discount applied to this line item."""

    ending_before: Optional[datetime] = None
    """The line item's end date (exclusive)."""

    group_key: Optional[str] = None

    group_value: Optional[str] = None

    is_prorated: Optional[bool] = None
    """Indicates whether the line item is prorated for `SUBSCRIPTION` type product."""

    list_price: Optional[Rate] = None
    """
    Only present for contract invoices and when the `include_list_prices` query
    parameter is set to true. This will include the list rate for the charge if
    applicable. Only present for usage and subscription line items.
    """

    metadata: Optional[str] = None

    netsuite_invoice_billing_end: Optional[datetime] = None
    """The end date for the billing period on the invoice."""

    netsuite_invoice_billing_start: Optional[datetime] = None
    """The start date for the billing period on the invoice."""

    netsuite_item_id: Optional[str] = None

    origin: Optional[LineItemOrigin] = None
    """
    Account hierarchy M3 - Present on line items from invoices with type
    USAGE_CONSOLIDATED. Indicates the original customer, contract, invoice and line
    item from which this line item was copied.
    """

    postpaid_commit: Optional[LineItemPostpaidCommit] = None
    """Only present for line items paying for a postpaid commit true-up."""

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None
    """
    Includes the presentation group values associated with this line item if
    presentation group keys are used.
    """

    pricing_group_values: Optional[Dict[str, str]] = None
    """
    Includes the pricing group values associated with this line item if dimensional
    pricing is used.
    """

    product_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    product_id: Optional[str] = None
    """ID of the product associated with the line item."""

    product_tags: Optional[List[str]] = None
    """The current product tags associated with the line item's `product_id`."""

    product_type: Optional[str] = None
    """The type of the line item's product.

    Possible values are `FixedProductListItem` (for `FIXED` type products),
    `UsageProductListItem` (for `USAGE` type products),
    `SubscriptionProductListItem` (for `SUBSCRIPTION` type products) or
    `CompositeProductListItem` (for `COMPOSITE` type products). For scheduled
    charges, commit and credit payments, the value is `FixedProductListItem`.
    """

    professional_service_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    professional_service_id: Optional[str] = None

    quantity: Optional[float] = None
    """The quantity associated with the line item."""

    reseller_type: Optional[Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]] = None

    scheduled_charge_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    scheduled_charge_id: Optional[str] = None
    """ID of scheduled charge."""

    starting_at: Optional[datetime] = None
    """The line item's start date (inclusive)."""

    sub_line_items: Optional[List[LineItemSubLineItem]] = None

    subscription_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    tier: Optional[LineItemTier] = None
    """Populated if the line item has a tiered price."""

    unit_price: Optional[float] = None
    """The unit price associated with the line item."""


class ConstituentInvoice(BaseModel):
    contract_id: str

    customer_id: str

    invoice_id: str


class CorrectionRecordCorrectedExternalInvoiceTax(BaseModel):
    """Tax details for the invoice, if available from the billing provider."""

    total_tax_amount: Optional[float] = None
    """The total tax amount applied to the invoice."""

    total_taxable_amount: Optional[float] = None
    """The total taxable amount of the invoice."""

    transaction_id: Optional[str] = None
    """The transaction ID associated with the tax calculation."""


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
        "metronome",
    ]

    billing_provider_error: Optional[str] = None
    """Error message from the billing provider, if available."""

    external_payment_id: Optional[str] = None
    """The ID of the payment in the external system, if available."""

    external_status: Optional[
        Literal[
            "DRAFT",
            "FINALIZED",
            "PAID",
            "PARTIALLY_PAID",
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

    invoiced_sub_total: Optional[float] = None
    """The subtotal amount invoiced, if available from the billing provider."""

    invoiced_total: Optional[float] = None
    """The total amount invoiced, if available from the billing provider."""

    issued_at_timestamp: Optional[datetime] = None

    pdf_url: Optional[str] = None
    """A URL to the PDF of the invoice, if available from the billing provider."""

    tax: Optional[CorrectionRecordCorrectedExternalInvoiceTax] = None
    """Tax details for the invoice, if available from the billing provider."""


class CorrectionRecord(BaseModel):
    corrected_invoice_id: str

    memo: str

    reason: str

    corrected_external_invoice: Optional[CorrectionRecordCorrectedExternalInvoice] = None


class ExternalInvoiceTax(BaseModel):
    """Tax details for the invoice, if available from the billing provider."""

    total_tax_amount: Optional[float] = None
    """The total tax amount applied to the invoice."""

    total_taxable_amount: Optional[float] = None
    """The total taxable amount of the invoice."""

    transaction_id: Optional[str] = None
    """The transaction ID associated with the tax calculation."""


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
        "metronome",
    ]

    billing_provider_error: Optional[str] = None
    """Error message from the billing provider, if available."""

    external_payment_id: Optional[str] = None
    """The ID of the payment in the external system, if available."""

    external_status: Optional[
        Literal[
            "DRAFT",
            "FINALIZED",
            "PAID",
            "PARTIALLY_PAID",
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

    invoiced_sub_total: Optional[float] = None
    """The subtotal amount invoiced, if available from the billing provider."""

    invoiced_total: Optional[float] = None
    """The total amount invoiced, if available from the billing provider."""

    issued_at_timestamp: Optional[datetime] = None

    pdf_url: Optional[str] = None
    """A URL to the PDF of the invoice, if available from the billing provider."""

    tax: Optional[ExternalInvoiceTax] = None
    """Tax details for the invoice, if available from the billing provider."""


class InvoiceAdjustment(BaseModel):
    credit_type: CreditTypeData

    name: str

    total: float

    credit_grant_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    credit_grant_id: Optional[str] = None


class Payer(BaseModel):
    """Account hierarchy M3 - Required for account hierarchy usage invoices.

    An object containing the contract and customer UUIDs that pay for this invoice.
    """

    contract_id: str

    customer_id: str


class ResellerRoyaltyAwsOptions(BaseModel):
    aws_account_number: Optional[str] = None

    aws_offer_id: Optional[str] = None

    aws_payer_reference_id: Optional[str] = None


class ResellerRoyaltyGcpOptions(BaseModel):
    gcp_account_id: Optional[str] = None

    gcp_offer_id: Optional[str] = None


class ResellerRoyalty(BaseModel):
    """Only present for contract invoices with reseller royalties."""

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

    billable_status: Optional[object] = None
    """This field's availability is dependent on your client's configuration."""

    constituent_invoices: Optional[List[ConstituentInvoice]] = None
    """Account hierarchy M3 - Required on invoices with type USAGE_CONSOLIDATED.

    List of constituent invoices that were consolidated to create this invoice.
    """

    contract_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    contract_id: Optional[str] = None

    correction_record: Optional[CorrectionRecord] = None

    created_at: Optional[datetime] = None
    """When the invoice was created (UTC).

    This field is present for correction invoices only.
    """

    custom_fields: Optional[Dict[str, object]] = None

    customer_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    end_timestamp: Optional[datetime] = None
    """End of the usage period this invoice covers (UTC)"""

    external_invoice: Optional[ExternalInvoice] = None

    invoice_adjustments: Optional[List[InvoiceAdjustment]] = None

    issued_at: Optional[datetime] = None
    """When the invoice was issued (UTC)"""

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    payer: Optional[Payer] = None
    """Account hierarchy M3 - Required for account hierarchy usage invoices.

    An object containing the contract and customer UUIDs that pay for this invoice.
    """

    plan_custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    plan_id: Optional[str] = None

    plan_name: Optional[str] = None

    reseller_royalty: Optional[ResellerRoyalty] = None
    """Only present for contract invoices with reseller royalties."""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    start_timestamp: Optional[datetime] = None
    """Beginning of the usage period this invoice covers (UTC)"""

    subtotal: Optional[float] = None
