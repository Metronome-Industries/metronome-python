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
        return AlertsResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def credit_grants(self) -> CreditGrantsResource:
        return CreditGrantsResource(self._client)

    @cached_property
    def pricing_units(self) -> PricingUnitsResource:
        return PricingUnitsResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def dashboards(self) -> DashboardsResource:
        return DashboardsResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        return AuditLogsResource(self._client)

    @cached_property
    def custom_fields(self) -> CustomFieldsResource:
        return CustomFieldsResource(self._client)

    @cached_property
    def billable_metrics(self) -> BillableMetricsResource:
        return BillableMetricsResource(self._client)

    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def contracts(self) -> ContractsResource:
        return ContractsResource(self._client)

    @cached_property
    def payments(self) -> PaymentsResource:
        return PaymentsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
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
        return AsyncAlertsResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def credit_grants(self) -> AsyncCreditGrantsResource:
        return AsyncCreditGrantsResource(self._client)

    @cached_property
    def pricing_units(self) -> AsyncPricingUnitsResource:
        return AsyncPricingUnitsResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def dashboards(self) -> AsyncDashboardsResource:
        return AsyncDashboardsResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResource:
        return AsyncAuditLogsResource(self._client)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResource:
        return AsyncCustomFieldsResource(self._client)

    @cached_property
    def billable_metrics(self) -> AsyncBillableMetricsResource:
        return AsyncBillableMetricsResource(self._client)

    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def contracts(self) -> AsyncContractsResource:
        return AsyncContractsResource(self._client)

    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        return AsyncPaymentsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
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
        return AlertsResourceWithRawResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> CreditGrantsResourceWithRawResponse:
        return CreditGrantsResourceWithRawResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> PricingUnitsResourceWithRawResponse:
        return PricingUnitsResourceWithRawResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> DashboardsResourceWithRawResponse:
        return DashboardsResourceWithRawResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithRawResponse:
        return AuditLogsResourceWithRawResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithRawResponse:
        return CustomFieldsResourceWithRawResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> BillableMetricsResourceWithRawResponse:
        return BillableMetricsResourceWithRawResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._v1.services)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> ContractsResourceWithRawResponse:
        return ContractsResourceWithRawResponse(self._v1.contracts)

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self._v1.payments)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._v1.settings)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithRawResponse:
        return AsyncAlertsResourceWithRawResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> AsyncCreditGrantsResourceWithRawResponse:
        return AsyncCreditGrantsResourceWithRawResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> AsyncPricingUnitsResourceWithRawResponse:
        return AsyncPricingUnitsResourceWithRawResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> AsyncDashboardsResourceWithRawResponse:
        return AsyncDashboardsResourceWithRawResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithRawResponse:
        return AsyncAuditLogsResourceWithRawResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithRawResponse:
        return AsyncCustomFieldsResourceWithRawResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> AsyncBillableMetricsResourceWithRawResponse:
        return AsyncBillableMetricsResourceWithRawResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._v1.services)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithRawResponse:
        return AsyncContractsResourceWithRawResponse(self._v1.contracts)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self._v1.payments)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._v1.settings)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def alerts(self) -> AlertsResourceWithStreamingResponse:
        return AlertsResourceWithStreamingResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> CreditGrantsResourceWithStreamingResponse:
        return CreditGrantsResourceWithStreamingResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> PricingUnitsResourceWithStreamingResponse:
        return PricingUnitsResourceWithStreamingResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> DashboardsResourceWithStreamingResponse:
        return DashboardsResourceWithStreamingResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithStreamingResponse:
        return AuditLogsResourceWithStreamingResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> CustomFieldsResourceWithStreamingResponse:
        return CustomFieldsResourceWithStreamingResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> BillableMetricsResourceWithStreamingResponse:
        return BillableMetricsResourceWithStreamingResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._v1.services)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> ContractsResourceWithStreamingResponse:
        return ContractsResourceWithStreamingResponse(self._v1.contracts)

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self._v1.payments)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._v1.settings)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithStreamingResponse:
        return AsyncAlertsResourceWithStreamingResponse(self._v1.alerts)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def credit_grants(self) -> AsyncCreditGrantsResourceWithStreamingResponse:
        return AsyncCreditGrantsResourceWithStreamingResponse(self._v1.credit_grants)

    @cached_property
    def pricing_units(self) -> AsyncPricingUnitsResourceWithStreamingResponse:
        return AsyncPricingUnitsResourceWithStreamingResponse(self._v1.pricing_units)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def dashboards(self) -> AsyncDashboardsResourceWithStreamingResponse:
        return AsyncDashboardsResourceWithStreamingResponse(self._v1.dashboards)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        return AsyncAuditLogsResourceWithStreamingResponse(self._v1.audit_logs)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        return AsyncCustomFieldsResourceWithStreamingResponse(self._v1.custom_fields)

    @cached_property
    def billable_metrics(self) -> AsyncBillableMetricsResourceWithStreamingResponse:
        return AsyncBillableMetricsResourceWithStreamingResponse(self._v1.billable_metrics)

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._v1.services)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._v1.invoices)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithStreamingResponse:
        return AsyncContractsResourceWithStreamingResponse(self._v1.contracts)

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self._v1.payments)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._v1.settings)
