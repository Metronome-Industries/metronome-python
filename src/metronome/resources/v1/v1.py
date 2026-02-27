# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .plans import (
    PlansResource,
    AsyncPlansResource,
    PlansResourceWithRawResponse,
    AsyncPlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
    AsyncPlansResourceWithStreamingResponse,
)
from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .alerts import (
    AlertsResource,
    AsyncAlertsResource,
    AlertsResourceWithRawResponse,
    AsyncAlertsResourceWithRawResponse,
    AlertsResourceWithStreamingResponse,
    AsyncAlertsResourceWithStreamingResponse,
)
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from .packages import (
    PackagesResource,
    AsyncPackagesResource,
    PackagesResourceWithRawResponse,
    AsyncPackagesResourceWithRawResponse,
    PackagesResourceWithStreamingResponse,
    AsyncPackagesResourceWithStreamingResponse,
)
from .payments import (
    PaymentsResource,
    AsyncPaymentsResource,
    PaymentsResourceWithRawResponse,
    AsyncPaymentsResourceWithRawResponse,
    PaymentsResourceWithStreamingResponse,
    AsyncPaymentsResourceWithStreamingResponse,
)
from .services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .audit_logs import (
    AuditLogsResource,
    AsyncAuditLogsResource,
    AuditLogsResourceWithRawResponse,
    AsyncAuditLogsResourceWithRawResponse,
    AuditLogsResourceWithStreamingResponse,
    AsyncAuditLogsResourceWithStreamingResponse,
)
from .dashboards import (
    DashboardsResource,
    AsyncDashboardsResource,
    DashboardsResourceWithRawResponse,
    AsyncDashboardsResourceWithRawResponse,
    DashboardsResourceWithStreamingResponse,
    AsyncDashboardsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .credit_grants import (
    CreditGrantsResource,
    AsyncCreditGrantsResource,
    CreditGrantsResourceWithRawResponse,
    AsyncCreditGrantsResourceWithRawResponse,
    CreditGrantsResourceWithStreamingResponse,
    AsyncCreditGrantsResourceWithStreamingResponse,
)
from .custom_fields import (
    CustomFieldsResource,
    AsyncCustomFieldsResource,
    CustomFieldsResourceWithRawResponse,
    AsyncCustomFieldsResourceWithRawResponse,
    CustomFieldsResourceWithStreamingResponse,
    AsyncCustomFieldsResourceWithStreamingResponse,
)
from .pricing_units import (
    PricingUnitsResource,
    AsyncPricingUnitsResource,
    PricingUnitsResourceWithRawResponse,
    AsyncPricingUnitsResourceWithRawResponse,
    PricingUnitsResourceWithStreamingResponse,
    AsyncPricingUnitsResourceWithStreamingResponse,
)
from .billable_metrics import (
    BillableMetricsResource,
    AsyncBillableMetricsResource,
    BillableMetricsResourceWithRawResponse,
    AsyncBillableMetricsResourceWithRawResponse,
    BillableMetricsResourceWithStreamingResponse,
    AsyncBillableMetricsResourceWithStreamingResponse,
)
from .settings.settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .contracts.contracts import (
    ContractsResource,
    AsyncContractsResource,
    ContractsResourceWithRawResponse,
    AsyncContractsResourceWithRawResponse,
    ContractsResourceWithStreamingResponse,
    AsyncContractsResourceWithStreamingResponse,
)
from .customers.customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def alerts(self) -> AlertsResource:
        """
        [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor customer spending, balances, and other billing factors. Use these endpoints to create, retrieve, and archive customer alerts. To view sample alert payloads by alert type, navigate [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
        """
        return AlertsResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        """
        [Plans](https://docs.metronome.com/pricing-and-packaging/create-plans/) determine the base pricing for a customer. Use these endpoints to add a plan to a customer, end a customer plan, retrieve plans, and retrieve plan details. Create plans in the [Metronome app](https://app.metronome.com/plans).
        """
        return PlansResource(self._client)

    @cached_property
    def credit_grants(self) -> CreditGrantsResource:
        """
        [Credit grants](https://docs.metronome.com/invoicing/how-billing-works/manage-credits/) adjust a customer balance for prepayments, reimbursements, promotions, and so on. Use these endpoints to create, retrieve, update, and delete credit grants.
        """
        return CreditGrantsResource(self._client)

    @cached_property
    def pricing_units(self) -> PricingUnitsResource:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return PricingUnitsResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def dashboards(self) -> DashboardsResource:
        """
        [Customers](https://docs.metronome.com/provisioning/create-customers/) in Metronome represent your users for all billing and reporting. Use these endpoints to create, retrieve, update, and archive customers and their billing configuration.
        """
        return DashboardsResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        """
        [Usage events](https://docs.metronome.com/connecting-metronome/send-usage-data/) are the basis for billable metrics. Use these endpoints to send usage events to Metronome and retrieve aggregated event data.
        """
        return UsageResource(self._client)

    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AuditLogsResource(self._client)

    @cached_property
    def custom_fields(self) -> CustomFieldsResource:
        """
        [Custom fields](https://docs.metronome.com/integrations/custom-fields/) enable adding additional data to Metronome entities. Use these endpoints to create, retrieve, update, and delete custom fields.
        """
        return CustomFieldsResource(self._client)

    @cached_property
    def billable_metrics(self) -> BillableMetricsResource:
        """
        [Billable metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics) in Metronome represent the various consumption components that Metronome meters and aggregates.
        """
        return BillableMetricsResource(self._client)

    @cached_property
    def services(self) -> ServicesResource:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return ServicesResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        """
        [Invoices](https://docs.metronome.com/invoicing/) reflect how much a customer spent during a period, which is the basis for billing. Metronome automatically generates invoices based upon your pricing, packaging, and usage events. Use these endpoints to retrieve invoices.
        """
        return InvoicesResource(self._client)

    @cached_property
    def contracts(self) -> ContractsResource:
        return ContractsResource(self._client)

    @cached_property
    def packages(self) -> PackagesResource:
        return PackagesResource(self._client)

    @cached_property
    def payments(self) -> PaymentsResource:
        return PaymentsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def alerts(self) -> AsyncAlertsResource:
        """
        [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor customer spending, balances, and other billing factors. Use these endpoints to create, retrieve, and archive customer alerts. To view sample alert payloads by alert type, navigate [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
        """
        return AsyncAlertsResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        """
        [Plans](https://docs.metronome.com/pricing-and-packaging/create-plans/) determine the base pricing for a customer. Use these endpoints to add a plan to a customer, end a customer plan, retrieve plans, and retrieve plan details. Create plans in the [Metronome app](https://app.metronome.com/plans).
        """
        return AsyncPlansResource(self._client)

    @cached_property
    def credit_grants(self) -> AsyncCreditGrantsResource:
        """
        [Credit grants](https://docs.metronome.com/invoicing/how-billing-works/manage-credits/) adjust a customer balance for prepayments, reimbursements, promotions, and so on. Use these endpoints to create, retrieve, update, and delete credit grants.
        """
        return AsyncCreditGrantsResource(self._client)

    @cached_property
    def pricing_units(self) -> AsyncPricingUnitsResource:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return AsyncPricingUnitsResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def dashboards(self) -> AsyncDashboardsResource:
        """
        [Customers](https://docs.metronome.com/provisioning/create-customers/) in Metronome represent your users for all billing and reporting. Use these endpoints to create, retrieve, update, and archive customers and their billing configuration.
        """
        return AsyncDashboardsResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        """
        [Usage events](https://docs.metronome.com/connecting-metronome/send-usage-data/) are the basis for billable metrics. Use these endpoints to send usage events to Metronome and retrieve aggregated event data.
        """
        return AsyncUsageResource(self._client)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResource:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AsyncAuditLogsResource(self._client)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResource:
        """
        [Custom fields](https://docs.metronome.com/integrations/custom-fields/) enable adding additional data to Metronome entities. Use these endpoints to create, retrieve, update, and delete custom fields.
        """
        return AsyncCustomFieldsResource(self._client)

    @cached_property
    def billable_metrics(self) -> AsyncBillableMetricsResource:
        """
        [Billable metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics) in Metronome represent the various consumption components that Metronome meters and aggregates.
        """
        return AsyncBillableMetricsResource(self._client)

    @cached_property
    def services(self) -> AsyncServicesResource:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AsyncServicesResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        """
        [Invoices](https://docs.metronome.com/invoicing/) reflect how much a customer spent during a period, which is the basis for billing. Metronome automatically generates invoices based upon your pricing, packaging, and usage events. Use these endpoints to retrieve invoices.
        """
        return AsyncInvoicesResource(self._client)

    @cached_property
    def contracts(self) -> AsyncContractsResource:
        return AsyncContractsResource(self._client)

    @cached_property
    def packages(self) -> AsyncPackagesResource:
        return AsyncPackagesResource(self._client)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        return AsyncPaymentsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def alerts(self) -> AlertsResourceWithRawResponse:
        """
        [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor customer spending, balances, and other billing factors. Use these endpoints to create, retrieve, and archive customer alerts. To view sample alert payloads by alert type, navigate [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
        """
        return AlertsResourceWithRawResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        """
        [Plans](https://docs.metronome.com/pricing-and-packaging/create-plans/) determine the base pricing for a customer. Use these endpoints to add a plan to a customer, end a customer plan, retrieve plans, and retrieve plan details. Create plans in the [Metronome app](https://app.metronome.com/plans).
        """
        return PlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> CreditGrantsResourceWithRawResponse:
        """
        [Credit grants](https://docs.metronome.com/invoicing/how-billing-works/manage-credits/) adjust a customer balance for prepayments, reimbursements, promotions, and so on. Use these endpoints to create, retrieve, update, and delete credit grants.
        """
        return CreditGrantsResourceWithRawResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> PricingUnitsResourceWithRawResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return PricingUnitsResourceWithRawResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> DashboardsResourceWithRawResponse:
        """
        [Customers](https://docs.metronome.com/provisioning/create-customers/) in Metronome represent your users for all billing and reporting. Use these endpoints to create, retrieve, update, and archive customers and their billing configuration.
        """
        return DashboardsResourceWithRawResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        """
        [Usage events](https://docs.metronome.com/connecting-metronome/send-usage-data/) are the basis for billable metrics. Use these endpoints to send usage events to Metronome and retrieve aggregated event data.
        """
        return UsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithRawResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AuditLogsResourceWithRawResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithRawResponse:
        """
        [Custom fields](https://docs.metronome.com/integrations/custom-fields/) enable adding additional data to Metronome entities. Use these endpoints to create, retrieve, update, and delete custom fields.
        """
        return CustomFieldsResourceWithRawResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> BillableMetricsResourceWithRawResponse:
        """
        [Billable metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics) in Metronome represent the various consumption components that Metronome meters and aggregates.
        """
        return BillableMetricsResourceWithRawResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return ServicesResourceWithRawResponse(self._v1.services)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        """
        [Invoices](https://docs.metronome.com/invoicing/) reflect how much a customer spent during a period, which is the basis for billing. Metronome automatically generates invoices based upon your pricing, packaging, and usage events. Use these endpoints to retrieve invoices.
        """
        return InvoicesResourceWithRawResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> ContractsResourceWithRawResponse:
        return ContractsResourceWithRawResponse(self._v1.contracts)

    @cached_property
    def packages(self) -> PackagesResourceWithRawResponse:
        return PackagesResourceWithRawResponse(self._v1.packages)

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self._v1.payments)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return SettingsResourceWithRawResponse(self._v1.settings)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithRawResponse:
        """
        [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor customer spending, balances, and other billing factors. Use these endpoints to create, retrieve, and archive customer alerts. To view sample alert payloads by alert type, navigate [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
        """
        return AsyncAlertsResourceWithRawResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        """
        [Plans](https://docs.metronome.com/pricing-and-packaging/create-plans/) determine the base pricing for a customer. Use these endpoints to add a plan to a customer, end a customer plan, retrieve plans, and retrieve plan details. Create plans in the [Metronome app](https://app.metronome.com/plans).
        """
        return AsyncPlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> AsyncCreditGrantsResourceWithRawResponse:
        """
        [Credit grants](https://docs.metronome.com/invoicing/how-billing-works/manage-credits/) adjust a customer balance for prepayments, reimbursements, promotions, and so on. Use these endpoints to create, retrieve, update, and delete credit grants.
        """
        return AsyncCreditGrantsResourceWithRawResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> AsyncPricingUnitsResourceWithRawResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return AsyncPricingUnitsResourceWithRawResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> AsyncDashboardsResourceWithRawResponse:
        """
        [Customers](https://docs.metronome.com/provisioning/create-customers/) in Metronome represent your users for all billing and reporting. Use these endpoints to create, retrieve, update, and archive customers and their billing configuration.
        """
        return AsyncDashboardsResourceWithRawResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        """
        [Usage events](https://docs.metronome.com/connecting-metronome/send-usage-data/) are the basis for billable metrics. Use these endpoints to send usage events to Metronome and retrieve aggregated event data.
        """
        return AsyncUsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AsyncAuditLogsResourceWithRawResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithRawResponse:
        """
        [Custom fields](https://docs.metronome.com/integrations/custom-fields/) enable adding additional data to Metronome entities. Use these endpoints to create, retrieve, update, and delete custom fields.
        """
        return AsyncCustomFieldsResourceWithRawResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> AsyncBillableMetricsResourceWithRawResponse:
        """
        [Billable metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics) in Metronome represent the various consumption components that Metronome meters and aggregates.
        """
        return AsyncBillableMetricsResourceWithRawResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AsyncServicesResourceWithRawResponse(self._v1.services)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        [Invoices](https://docs.metronome.com/invoicing/) reflect how much a customer spent during a period, which is the basis for billing. Metronome automatically generates invoices based upon your pricing, packaging, and usage events. Use these endpoints to retrieve invoices.
        """
        return AsyncInvoicesResourceWithRawResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithRawResponse:
        return AsyncContractsResourceWithRawResponse(self._v1.contracts)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithRawResponse:
        return AsyncPackagesResourceWithRawResponse(self._v1.packages)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self._v1.payments)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return AsyncSettingsResourceWithRawResponse(self._v1.settings)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def alerts(self) -> AlertsResourceWithStreamingResponse:
        """
        [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor customer spending, balances, and other billing factors. Use these endpoints to create, retrieve, and archive customer alerts. To view sample alert payloads by alert type, navigate [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
        """
        return AlertsResourceWithStreamingResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        """
        [Plans](https://docs.metronome.com/pricing-and-packaging/create-plans/) determine the base pricing for a customer. Use these endpoints to add a plan to a customer, end a customer plan, retrieve plans, and retrieve plan details. Create plans in the [Metronome app](https://app.metronome.com/plans).
        """
        return PlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> CreditGrantsResourceWithStreamingResponse:
        """
        [Credit grants](https://docs.metronome.com/invoicing/how-billing-works/manage-credits/) adjust a customer balance for prepayments, reimbursements, promotions, and so on. Use these endpoints to create, retrieve, update, and delete credit grants.
        """
        return CreditGrantsResourceWithStreamingResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> PricingUnitsResourceWithStreamingResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return PricingUnitsResourceWithStreamingResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> DashboardsResourceWithStreamingResponse:
        """
        [Customers](https://docs.metronome.com/provisioning/create-customers/) in Metronome represent your users for all billing and reporting. Use these endpoints to create, retrieve, update, and archive customers and their billing configuration.
        """
        return DashboardsResourceWithStreamingResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        """
        [Usage events](https://docs.metronome.com/connecting-metronome/send-usage-data/) are the basis for billable metrics. Use these endpoints to send usage events to Metronome and retrieve aggregated event data.
        """
        return UsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithStreamingResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AuditLogsResourceWithStreamingResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithStreamingResponse:
        """
        [Custom fields](https://docs.metronome.com/integrations/custom-fields/) enable adding additional data to Metronome entities. Use these endpoints to create, retrieve, update, and delete custom fields.
        """
        return CustomFieldsResourceWithStreamingResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> BillableMetricsResourceWithStreamingResponse:
        """
        [Billable metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics) in Metronome represent the various consumption components that Metronome meters and aggregates.
        """
        return BillableMetricsResourceWithStreamingResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return ServicesResourceWithStreamingResponse(self._v1.services)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        """
        [Invoices](https://docs.metronome.com/invoicing/) reflect how much a customer spent during a period, which is the basis for billing. Metronome automatically generates invoices based upon your pricing, packaging, and usage events. Use these endpoints to retrieve invoices.
        """
        return InvoicesResourceWithStreamingResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> ContractsResourceWithStreamingResponse:
        return ContractsResourceWithStreamingResponse(self._v1.contracts)

    @cached_property
    def packages(self) -> PackagesResourceWithStreamingResponse:
        return PackagesResourceWithStreamingResponse(self._v1.packages)

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self._v1.payments)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return SettingsResourceWithStreamingResponse(self._v1.settings)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithStreamingResponse:
        """
        [Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor customer spending, balances, and other billing factors. Use these endpoints to create, retrieve, and archive customer alerts. To view sample alert payloads by alert type, navigate [here.](https://docs.metronome.com/manage-product-access/create-manage-alerts/#webhook-notifications)
        """
        return AsyncAlertsResourceWithStreamingResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        """
        [Plans](https://docs.metronome.com/pricing-and-packaging/create-plans/) determine the base pricing for a customer. Use these endpoints to add a plan to a customer, end a customer plan, retrieve plans, and retrieve plan details. Create plans in the [Metronome app](https://app.metronome.com/plans).
        """
        return AsyncPlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> AsyncCreditGrantsResourceWithStreamingResponse:
        """
        [Credit grants](https://docs.metronome.com/invoicing/how-billing-works/manage-credits/) adjust a customer balance for prepayments, reimbursements, promotions, and so on. Use these endpoints to create, retrieve, update, and delete credit grants.
        """
        return AsyncCreditGrantsResourceWithStreamingResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> AsyncPricingUnitsResourceWithStreamingResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return AsyncPricingUnitsResourceWithStreamingResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> AsyncDashboardsResourceWithStreamingResponse:
        """
        [Customers](https://docs.metronome.com/provisioning/create-customers/) in Metronome represent your users for all billing and reporting. Use these endpoints to create, retrieve, update, and archive customers and their billing configuration.
        """
        return AsyncDashboardsResourceWithStreamingResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        [Usage events](https://docs.metronome.com/connecting-metronome/send-usage-data/) are the basis for billable metrics. Use these endpoints to send usage events to Metronome and retrieve aggregated event data.
        """
        return AsyncUsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        """
        [Custom fields](https://docs.metronome.com/integrations/custom-fields/) enable adding additional data to Metronome entities. Use these endpoints to create, retrieve, update, and delete custom fields.
        """
        return AsyncCustomFieldsResourceWithStreamingResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> AsyncBillableMetricsResourceWithStreamingResponse:
        """
        [Billable metrics](https://docs.metronome.com/understanding-metronome/how-metronome-works#billable-metrics) in Metronome represent the various consumption components that Metronome meters and aggregates.
        """
        return AsyncBillableMetricsResourceWithStreamingResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        [Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.
        """
        return AsyncServicesResourceWithStreamingResponse(self._v1.services)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        [Invoices](https://docs.metronome.com/invoicing/) reflect how much a customer spent during a period, which is the basis for billing. Metronome automatically generates invoices based upon your pricing, packaging, and usage events. Use these endpoints to retrieve invoices.
        """
        return AsyncInvoicesResourceWithStreamingResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithStreamingResponse:
        return AsyncContractsResourceWithStreamingResponse(self._v1.contracts)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithStreamingResponse:
        return AsyncPackagesResourceWithStreamingResponse(self._v1.packages)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self._v1.payments)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
        """
        return AsyncSettingsResourceWithStreamingResponse(self._v1.settings)
