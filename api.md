# Shared Types

```python
from metronome.types import (
    BaseUsageFilter,
    Commit,
    ContractWithoutAmendments,
    Credit,
    CreditType,
    Discount,
    EventTypeFilter,
    ID,
    Override,
    PropertyFilter,
    ProService,
    Rate,
    ScheduledCharge,
    ScheduleDuration,
    SchedulePointInTime,
    Tier,
)
```

# Alerts

Types:

```python
from metronome.types import AlertCreateResponse, AlertArchiveResponse
```

Methods:

- <code title="post /alerts/create">client.alerts.<a href="./src/metronome/resources/alerts.py">create</a>(\*\*<a href="src/metronome/types/alert_create_params.py">params</a>) -> <a href="./src/metronome/types/alert_create_response.py">AlertCreateResponse</a></code>
- <code title="post /alerts/archive">client.alerts.<a href="./src/metronome/resources/alerts.py">archive</a>(\*\*<a href="src/metronome/types/alert_archive_params.py">params</a>) -> <a href="./src/metronome/types/alert_archive_response.py">AlertArchiveResponse</a></code>

# Plans

Types:

```python
from metronome.types import (
    PlanDetail,
    PlanListResponse,
    PlanGetDetailsResponse,
    PlanListChargesResponse,
    PlanListCustomersResponse,
)
```

Methods:

- <code title="get /plans">client.plans.<a href="./src/metronome/resources/plans.py">list</a>(\*\*<a href="src/metronome/types/plan_list_params.py">params</a>) -> <a href="./src/metronome/types/plan_list_response.py">SyncCursorPage[PlanListResponse]</a></code>
- <code title="get /planDetails/{plan_id}">client.plans.<a href="./src/metronome/resources/plans.py">get_details</a>(plan_id) -> <a href="./src/metronome/types/plan_get_details_response.py">PlanGetDetailsResponse</a></code>
- <code title="get /planDetails/{plan_id}/charges">client.plans.<a href="./src/metronome/resources/plans.py">list_charges</a>(plan_id, \*\*<a href="src/metronome/types/plan_list_charges_params.py">params</a>) -> <a href="./src/metronome/types/plan_list_charges_response.py">SyncCursorPage[PlanListChargesResponse]</a></code>
- <code title="get /planDetails/{plan_id}/customers">client.plans.<a href="./src/metronome/resources/plans.py">list_customers</a>(plan_id, \*\*<a href="src/metronome/types/plan_list_customers_params.py">params</a>) -> <a href="./src/metronome/types/plan_list_customers_response.py">SyncCursorPage[PlanListCustomersResponse]</a></code>

# CreditGrants

Types:

```python
from metronome.types import (
    CreditLedgerEntry,
    RolloverAmountMaxAmount,
    RolloverAmountMaxPercentage,
    CreditGrantCreateResponse,
    CreditGrantListResponse,
    CreditGrantEditResponse,
    CreditGrantListCreditTypesResponse,
    CreditGrantListEntriesResponse,
    CreditGrantVoidResponse,
)
```

Methods:

- <code title="post /credits/createGrant">client.credit_grants.<a href="./src/metronome/resources/credit_grants.py">create</a>(\*\*<a href="src/metronome/types/credit_grant_create_params.py">params</a>) -> <a href="./src/metronome/types/credit_grant_create_response.py">CreditGrantCreateResponse</a></code>
- <code title="post /credits/listGrants">client.credit_grants.<a href="./src/metronome/resources/credit_grants.py">list</a>(\*\*<a href="src/metronome/types/credit_grant_list_params.py">params</a>) -> <a href="./src/metronome/types/credit_grant_list_response.py">SyncCursorPage[CreditGrantListResponse]</a></code>
- <code title="post /credits/editGrant">client.credit_grants.<a href="./src/metronome/resources/credit_grants.py">edit</a>(\*\*<a href="src/metronome/types/credit_grant_edit_params.py">params</a>) -> <a href="./src/metronome/types/credit_grant_edit_response.py">CreditGrantEditResponse</a></code>
- <code title="get /credit-types/list">client.credit_grants.<a href="./src/metronome/resources/credit_grants.py">list_credit_types</a>(\*\*<a href="src/metronome/types/credit_grant_list_credit_types_params.py">params</a>) -> <a href="./src/metronome/types/credit_grant_list_credit_types_response.py">SyncCursorPage[CreditGrantListCreditTypesResponse]</a></code>
- <code title="post /credits/listEntries">client.credit_grants.<a href="./src/metronome/resources/credit_grants.py">list_entries</a>(\*\*<a href="src/metronome/types/credit_grant_list_entries_params.py">params</a>) -> <a href="./src/metronome/types/credit_grant_list_entries_response.py">CreditGrantListEntriesResponse</a></code>
- <code title="post /credits/voidGrant">client.credit_grants.<a href="./src/metronome/resources/credit_grants.py">void</a>(\*\*<a href="src/metronome/types/credit_grant_void_params.py">params</a>) -> <a href="./src/metronome/types/credit_grant_void_response.py">CreditGrantVoidResponse</a></code>

# Customers

Types:

```python
from metronome.types import (
    Customer,
    CustomerDetail,
    CustomerCreateResponse,
    CustomerRetrieveResponse,
    CustomerArchiveResponse,
    CustomerListBillableMetricsResponse,
    CustomerListCostsResponse,
    CustomerSetNameResponse,
)
```

Methods:

- <code title="post /customers">client.customers.<a href="./src/metronome/resources/customers/customers.py">create</a>(\*\*<a href="src/metronome/types/customer_create_params.py">params</a>) -> <a href="./src/metronome/types/customer_create_response.py">CustomerCreateResponse</a></code>
- <code title="get /customers/{customer_id}">client.customers.<a href="./src/metronome/resources/customers/customers.py">retrieve</a>(customer_id) -> <a href="./src/metronome/types/customer_retrieve_response.py">CustomerRetrieveResponse</a></code>
- <code title="get /customers">client.customers.<a href="./src/metronome/resources/customers/customers.py">list</a>(\*\*<a href="src/metronome/types/customer_list_params.py">params</a>) -> <a href="./src/metronome/types/customer_detail.py">SyncCursorPage[CustomerDetail]</a></code>
- <code title="post /customers/archive">client.customers.<a href="./src/metronome/resources/customers/customers.py">archive</a>(\*\*<a href="src/metronome/types/customer_archive_params.py">params</a>) -> <a href="./src/metronome/types/customer_archive_response.py">CustomerArchiveResponse</a></code>
- <code title="get /customers/{customer_id}/billable-metrics">client.customers.<a href="./src/metronome/resources/customers/customers.py">list_billable_metrics</a>(customer_id, \*\*<a href="src/metronome/types/customer_list_billable_metrics_params.py">params</a>) -> <a href="./src/metronome/types/customer_list_billable_metrics_response.py">SyncCursorPage[CustomerListBillableMetricsResponse]</a></code>
- <code title="get /customers/{customer_id}/costs">client.customers.<a href="./src/metronome/resources/customers/customers.py">list_costs</a>(customer_id, \*\*<a href="src/metronome/types/customer_list_costs_params.py">params</a>) -> <a href="./src/metronome/types/customer_list_costs_response.py">SyncCursorPage[CustomerListCostsResponse]</a></code>
- <code title="post /customers/{customer_id}/setIngestAliases">client.customers.<a href="./src/metronome/resources/customers/customers.py">set_ingest_aliases</a>(customer_id, \*\*<a href="src/metronome/types/customer_set_ingest_aliases_params.py">params</a>) -> None</code>
- <code title="post /customers/{customer_id}/setName">client.customers.<a href="./src/metronome/resources/customers/customers.py">set_name</a>(customer_id, \*\*<a href="src/metronome/types/customer_set_name_params.py">params</a>) -> <a href="./src/metronome/types/customer_set_name_response.py">CustomerSetNameResponse</a></code>
- <code title="post /customers/{customer_id}/updateConfig">client.customers.<a href="./src/metronome/resources/customers/customers.py">update_config</a>(customer_id, \*\*<a href="src/metronome/types/customer_update_config_params.py">params</a>) -> None</code>

## Alerts

Types:

```python
from metronome.types.customers import CustomerAlert, AlertRetrieveResponse, AlertListResponse
```

Methods:

- <code title="post /customer-alerts/get">client.customers.alerts.<a href="./src/metronome/resources/customers/alerts.py">retrieve</a>(\*\*<a href="src/metronome/types/customers/alert_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/customers/alert_retrieve_response.py">AlertRetrieveResponse</a></code>
- <code title="post /customer-alerts/list">client.customers.alerts.<a href="./src/metronome/resources/customers/alerts.py">list</a>(\*\*<a href="src/metronome/types/customers/alert_list_params.py">params</a>) -> <a href="./src/metronome/types/customers/alert_list_response.py">AlertListResponse</a></code>
- <code title="post /customer-alerts/reset">client.customers.alerts.<a href="./src/metronome/resources/customers/alerts.py">reset</a>(\*\*<a href="src/metronome/types/customers/alert_reset_params.py">params</a>) -> None</code>

## Plans

Types:

```python
from metronome.types.customers import (
    PlanListResponse,
    PlanAddResponse,
    PlanEndResponse,
    PlanListPriceAdjustmentsResponse,
)
```

Methods:

- <code title="get /customers/{customer_id}/plans">client.customers.plans.<a href="./src/metronome/resources/customers/plans.py">list</a>(customer_id, \*\*<a href="src/metronome/types/customers/plan_list_params.py">params</a>) -> <a href="./src/metronome/types/customers/plan_list_response.py">SyncCursorPage[PlanListResponse]</a></code>
- <code title="post /customers/{customer_id}/plans/add">client.customers.plans.<a href="./src/metronome/resources/customers/plans.py">add</a>(customer_id, \*\*<a href="src/metronome/types/customers/plan_add_params.py">params</a>) -> <a href="./src/metronome/types/customers/plan_add_response.py">PlanAddResponse</a></code>
- <code title="post /customers/{customer_id}/plans/{customer_plan_id}/end">client.customers.plans.<a href="./src/metronome/resources/customers/plans.py">end</a>(customer_plan_id, \*, customer_id, \*\*<a href="src/metronome/types/customers/plan_end_params.py">params</a>) -> <a href="./src/metronome/types/customers/plan_end_response.py">PlanEndResponse</a></code>
- <code title="get /customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments">client.customers.plans.<a href="./src/metronome/resources/customers/plans.py">list_price_adjustments</a>(customer_plan_id, \*, customer_id, \*\*<a href="src/metronome/types/customers/plan_list_price_adjustments_params.py">params</a>) -> <a href="./src/metronome/types/customers/plan_list_price_adjustments_response.py">SyncCursorPage[PlanListPriceAdjustmentsResponse]</a></code>

## Invoices

Types:

```python
from metronome.types.customers import Invoice, InvoiceRetrieveResponse, InvoiceAddChargeResponse
```

Methods:

- <code title="get /customers/{customer_id}/invoices/{invoice_id}">client.customers.invoices.<a href="./src/metronome/resources/customers/invoices.py">retrieve</a>(invoice_id, \*, customer_id, \*\*<a href="src/metronome/types/customers/invoice_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/customers/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="get /customers/{customer_id}/invoices">client.customers.invoices.<a href="./src/metronome/resources/customers/invoices.py">list</a>(customer_id, \*\*<a href="src/metronome/types/customers/invoice_list_params.py">params</a>) -> <a href="./src/metronome/types/customers/invoice.py">SyncCursorPage[Invoice]</a></code>
- <code title="post /customers/{customer_id}/addCharge">client.customers.invoices.<a href="./src/metronome/resources/customers/invoices.py">add_charge</a>(customer_id, \*\*<a href="src/metronome/types/customers/invoice_add_charge_params.py">params</a>) -> <a href="./src/metronome/types/customers/invoice_add_charge_response.py">InvoiceAddChargeResponse</a></code>

## BillingConfig

Types:

```python
from metronome.types.customers import BillingConfigRetrieveResponse
```

Methods:

- <code title="post /customers/{customer_id}/billing-config/{billing_provider_type}">client.customers.billing_config.<a href="./src/metronome/resources/customers/billing_config.py">create</a>(billing_provider_type, \*, customer_id, \*\*<a href="src/metronome/types/customers/billing_config_create_params.py">params</a>) -> None</code>
- <code title="get /customers/{customer_id}/billing-config/{billing_provider_type}">client.customers.billing_config.<a href="./src/metronome/resources/customers/billing_config.py">retrieve</a>(billing_provider_type, \*, customer_id) -> <a href="./src/metronome/types/customers/billing_config_retrieve_response.py">BillingConfigRetrieveResponse</a></code>
- <code title="delete /customers/{customer_id}/billing-config/{billing_provider_type}">client.customers.billing_config.<a href="./src/metronome/resources/customers/billing_config.py">delete</a>(billing_provider_type, \*, customer_id) -> None</code>

## Commits

Types:

```python
from metronome.types.customers import (
    CommitCreateResponse,
    CommitListResponse,
    CommitUpdateEndDateResponse,
)
```

Methods:

- <code title="post /contracts/customerCommits/create">client.customers.commits.<a href="./src/metronome/resources/customers/commits.py">create</a>(\*\*<a href="src/metronome/types/customers/commit_create_params.py">params</a>) -> <a href="./src/metronome/types/customers/commit_create_response.py">CommitCreateResponse</a></code>
- <code title="post /contracts/customerCommits/list">client.customers.commits.<a href="./src/metronome/resources/customers/commits.py">list</a>(\*\*<a href="src/metronome/types/customers/commit_list_params.py">params</a>) -> <a href="./src/metronome/types/customers/commit_list_response.py">CommitListResponse</a></code>
- <code title="post /contracts/customerCommits/updateEndDate">client.customers.commits.<a href="./src/metronome/resources/customers/commits.py">update_end_date</a>(\*\*<a href="src/metronome/types/customers/commit_update_end_date_params.py">params</a>) -> <a href="./src/metronome/types/customers/commit_update_end_date_response.py">CommitUpdateEndDateResponse</a></code>

## Credits

Types:

```python
from metronome.types.customers import (
    CreditCreateResponse,
    CreditListResponse,
    CreditUpdateEndDateResponse,
)
```

Methods:

- <code title="post /contracts/customerCredits/create">client.customers.credits.<a href="./src/metronome/resources/customers/credits.py">create</a>(\*\*<a href="src/metronome/types/customers/credit_create_params.py">params</a>) -> <a href="./src/metronome/types/customers/credit_create_response.py">CreditCreateResponse</a></code>
- <code title="post /contracts/customerCredits/list">client.customers.credits.<a href="./src/metronome/resources/customers/credits.py">list</a>(\*\*<a href="src/metronome/types/customers/credit_list_params.py">params</a>) -> <a href="./src/metronome/types/customers/credit_list_response.py">CreditListResponse</a></code>
- <code title="post /contracts/customerCredits/updateEndDate">client.customers.credits.<a href="./src/metronome/resources/customers/credits.py">update_end_date</a>(\*\*<a href="src/metronome/types/customers/credit_update_end_date_params.py">params</a>) -> <a href="./src/metronome/types/customers/credit_update_end_date_response.py">CreditUpdateEndDateResponse</a></code>

## NamedSchedules

Types:

```python
from metronome.types.customers import NamedScheduleRetrieveResponse
```

Methods:

- <code title="post /customers/getNamedSchedule">client.customers.named_schedules.<a href="./src/metronome/resources/customers/named_schedules.py">retrieve</a>(\*\*<a href="src/metronome/types/customers/named_schedule_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/customers/named_schedule_retrieve_response.py">NamedScheduleRetrieveResponse</a></code>
- <code title="post /customers/updateNamedSchedule">client.customers.named_schedules.<a href="./src/metronome/resources/customers/named_schedules.py">update</a>(\*\*<a href="src/metronome/types/customers/named_schedule_update_params.py">params</a>) -> None</code>

# Dashboards

Types:

```python
from metronome.types import DashboardGetEmbeddableURLResponse
```

Methods:

- <code title="post /dashboards/getEmbeddableUrl">client.dashboards.<a href="./src/metronome/resources/dashboards.py">get_embeddable_url</a>(\*\*<a href="src/metronome/types/dashboard_get_embeddable_url_params.py">params</a>) -> <a href="./src/metronome/types/dashboard_get_embeddable_url_response.py">DashboardGetEmbeddableURLResponse</a></code>

# Usage

Types:

```python
from metronome.types import UsageListResponse, UsageListWithGroupsResponse
```

Methods:

- <code title="post /usage">client.usage.<a href="./src/metronome/resources/usage.py">list</a>(\*\*<a href="src/metronome/types/usage_list_params.py">params</a>) -> <a href="./src/metronome/types/usage_list_response.py">UsageListResponse</a></code>
- <code title="post /ingest">client.usage.<a href="./src/metronome/resources/usage.py">ingest</a>(\*\*<a href="src/metronome/types/usage_ingest_params.py">params</a>) -> None</code>
- <code title="post /usage/groups">client.usage.<a href="./src/metronome/resources/usage.py">list_with_groups</a>(\*\*<a href="src/metronome/types/usage_list_with_groups_params.py">params</a>) -> <a href="./src/metronome/types/usage_list_with_groups_response.py">SyncCursorPage[UsageListWithGroupsResponse]</a></code>

# AuditLogs

Types:

```python
from metronome.types import AuditLogListResponse
```

Methods:

- <code title="get /auditLogs">client.audit_logs.<a href="./src/metronome/resources/audit_logs.py">list</a>(\*\*<a href="src/metronome/types/audit_log_list_params.py">params</a>) -> <a href="./src/metronome/types/audit_log_list_response.py">SyncCursorPage[AuditLogListResponse]</a></code>

# CustomFields

Types:

```python
from metronome.types import CustomFieldListKeysResponse
```

Methods:

- <code title="post /customFields/addKey">client.custom_fields.<a href="./src/metronome/resources/custom_fields.py">add_key</a>(\*\*<a href="src/metronome/types/custom_field_add_key_params.py">params</a>) -> None</code>
- <code title="post /customFields/deleteValues">client.custom_fields.<a href="./src/metronome/resources/custom_fields.py">delete_values</a>(\*\*<a href="src/metronome/types/custom_field_delete_values_params.py">params</a>) -> None</code>
- <code title="post /customFields/listKeys">client.custom_fields.<a href="./src/metronome/resources/custom_fields.py">list_keys</a>(\*\*<a href="src/metronome/types/custom_field_list_keys_params.py">params</a>) -> <a href="./src/metronome/types/custom_field_list_keys_response.py">CustomFieldListKeysResponse</a></code>
- <code title="post /customFields/removeKey">client.custom_fields.<a href="./src/metronome/resources/custom_fields.py">remove_key</a>(\*\*<a href="src/metronome/types/custom_field_remove_key_params.py">params</a>) -> None</code>
- <code title="post /customFields/setValues">client.custom_fields.<a href="./src/metronome/resources/custom_fields.py">set_values</a>(\*\*<a href="src/metronome/types/custom_field_set_values_params.py">params</a>) -> None</code>

# BillableMetrics

Types:

```python
from metronome.types import (
    BillableMetricCreateResponse,
    BillableMetricRetrieveResponse,
    BillableMetricListResponse,
    BillableMetricArchiveResponse,
)
```

Methods:

- <code title="post /billable-metrics/create">client.billable_metrics.<a href="./src/metronome/resources/billable_metrics.py">create</a>(\*\*<a href="src/metronome/types/billable_metric_create_params.py">params</a>) -> <a href="./src/metronome/types/billable_metric_create_response.py">BillableMetricCreateResponse</a></code>
- <code title="get /billable-metrics/{billable_metric_id}">client.billable_metrics.<a href="./src/metronome/resources/billable_metrics.py">retrieve</a>(billable_metric_id) -> <a href="./src/metronome/types/billable_metric_retrieve_response.py">BillableMetricRetrieveResponse</a></code>
- <code title="get /billable-metrics">client.billable_metrics.<a href="./src/metronome/resources/billable_metrics.py">list</a>(\*\*<a href="src/metronome/types/billable_metric_list_params.py">params</a>) -> <a href="./src/metronome/types/billable_metric_list_response.py">SyncCursorPage[BillableMetricListResponse]</a></code>
- <code title="post /billable-metrics/archive">client.billable_metrics.<a href="./src/metronome/resources/billable_metrics.py">archive</a>(\*\*<a href="src/metronome/types/billable_metric_archive_params.py">params</a>) -> <a href="./src/metronome/types/billable_metric_archive_response.py">BillableMetricArchiveResponse</a></code>

# Services

Types:

```python
from metronome.types import ServiceListResponse
```

Methods:

- <code title="get /services">client.services.<a href="./src/metronome/resources/services.py">list</a>() -> <a href="./src/metronome/types/service_list_response.py">ServiceListResponse</a></code>

# Invoices

Types:

```python
from metronome.types import InvoiceRegenerateResponse, InvoiceVoidResponse
```

Methods:

- <code title="post /invoices/regenerate">client.invoices.<a href="./src/metronome/resources/invoices.py">regenerate</a>(\*\*<a href="src/metronome/types/invoice_regenerate_params.py">params</a>) -> <a href="./src/metronome/types/invoice_regenerate_response.py">InvoiceRegenerateResponse</a></code>
- <code title="post /invoices/void">client.invoices.<a href="./src/metronome/resources/invoices.py">void</a>(\*\*<a href="src/metronome/types/invoice_void_params.py">params</a>) -> <a href="./src/metronome/types/invoice_void_response.py">InvoiceVoidResponse</a></code>

# Contracts

Types:

```python
from metronome.types import (
    ContractCreateResponse,
    ContractRetrieveResponse,
    ContractListResponse,
    ContractAmendResponse,
    ContractArchiveResponse,
    ContractCreateHistoricalInvoicesResponse,
    ContractListBalancesResponse,
    ContractRetrieveRateScheduleResponse,
    ContractScheduleProServicesInvoiceResponse,
    ContractUpdateEndDateResponse,
)
```

Methods:

- <code title="post /contracts/create">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">create</a>(\*\*<a href="src/metronome/types/contract_create_params.py">params</a>) -> <a href="./src/metronome/types/contract_create_response.py">ContractCreateResponse</a></code>
- <code title="post /contracts/get">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">retrieve</a>(\*\*<a href="src/metronome/types/contract_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/contract_retrieve_response.py">ContractRetrieveResponse</a></code>
- <code title="post /contracts/list">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">list</a>(\*\*<a href="src/metronome/types/contract_list_params.py">params</a>) -> <a href="./src/metronome/types/contract_list_response.py">ContractListResponse</a></code>
- <code title="post /contracts/addManualBalanceLedgerEntry">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">add_manual_balance_entry</a>(\*\*<a href="src/metronome/types/contract_add_manual_balance_entry_params.py">params</a>) -> None</code>
- <code title="post /contracts/amend">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">amend</a>(\*\*<a href="src/metronome/types/contract_amend_params.py">params</a>) -> <a href="./src/metronome/types/contract_amend_response.py">ContractAmendResponse</a></code>
- <code title="post /contracts/archive">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">archive</a>(\*\*<a href="src/metronome/types/contract_archive_params.py">params</a>) -> <a href="./src/metronome/types/contract_archive_response.py">ContractArchiveResponse</a></code>
- <code title="post /contracts/createHistoricalInvoices">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">create_historical_invoices</a>(\*\*<a href="src/metronome/types/contract_create_historical_invoices_params.py">params</a>) -> <a href="./src/metronome/types/contract_create_historical_invoices_response.py">ContractCreateHistoricalInvoicesResponse</a></code>
- <code title="post /contracts/customerBalances/list">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">list_balances</a>(\*\*<a href="src/metronome/types/contract_list_balances_params.py">params</a>) -> <a href="./src/metronome/types/contract_list_balances_response.py">ContractListBalancesResponse</a></code>
- <code title="post /contracts/getContractRateSchedule">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">retrieve_rate_schedule</a>(\*\*<a href="src/metronome/types/contract_retrieve_rate_schedule_params.py">params</a>) -> <a href="./src/metronome/types/contract_retrieve_rate_schedule_response.py">ContractRetrieveRateScheduleResponse</a></code>
- <code title="post /contracts/scheduleProServicesInvoice">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">schedule_pro_services_invoice</a>(\*\*<a href="src/metronome/types/contract_schedule_pro_services_invoice_params.py">params</a>) -> <a href="./src/metronome/types/contract_schedule_pro_services_invoice_response.py">ContractScheduleProServicesInvoiceResponse</a></code>
- <code title="post /contracts/setUsageFilter">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">set_usage_filter</a>(\*\*<a href="src/metronome/types/contract_set_usage_filter_params.py">params</a>) -> None</code>
- <code title="post /contracts/updateEndDate">client.contracts.<a href="./src/metronome/resources/contracts/contracts.py">update_end_date</a>(\*\*<a href="src/metronome/types/contract_update_end_date_params.py">params</a>) -> <a href="./src/metronome/types/contract_update_end_date_response.py">ContractUpdateEndDateResponse</a></code>

## Products

Types:

```python
from metronome.types.contracts import (
    ProductListItemState,
    QuantityConversion,
    QuantityRounding,
    ProductCreateResponse,
    ProductRetrieveResponse,
    ProductUpdateResponse,
    ProductListResponse,
    ProductArchiveResponse,
)
```

Methods:

- <code title="post /contract-pricing/products/create">client.contracts.products.<a href="./src/metronome/resources/contracts/products.py">create</a>(\*\*<a href="src/metronome/types/contracts/product_create_params.py">params</a>) -> <a href="./src/metronome/types/contracts/product_create_response.py">ProductCreateResponse</a></code>
- <code title="post /contract-pricing/products/get">client.contracts.products.<a href="./src/metronome/resources/contracts/products.py">retrieve</a>(\*\*<a href="src/metronome/types/contracts/product_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/contracts/product_retrieve_response.py">ProductRetrieveResponse</a></code>
- <code title="post /contract-pricing/products/update">client.contracts.products.<a href="./src/metronome/resources/contracts/products.py">update</a>(\*\*<a href="src/metronome/types/contracts/product_update_params.py">params</a>) -> <a href="./src/metronome/types/contracts/product_update_response.py">ProductUpdateResponse</a></code>
- <code title="post /contract-pricing/products/list">client.contracts.products.<a href="./src/metronome/resources/contracts/products.py">list</a>(\*\*<a href="src/metronome/types/contracts/product_list_params.py">params</a>) -> <a href="./src/metronome/types/contracts/product_list_response.py">SyncCursorPage[ProductListResponse]</a></code>
- <code title="post /contract-pricing/products/archive">client.contracts.products.<a href="./src/metronome/resources/contracts/products.py">archive</a>(\*\*<a href="src/metronome/types/contracts/product_archive_params.py">params</a>) -> <a href="./src/metronome/types/contracts/product_archive_response.py">ProductArchiveResponse</a></code>

## RateCards

Types:

```python
from metronome.types.contracts import (
    RateCardCreateResponse,
    RateCardRetrieveResponse,
    RateCardUpdateResponse,
    RateCardListResponse,
    RateCardRetrieveRateScheduleResponse,
)
```

Methods:

- <code title="post /contract-pricing/rate-cards/create">client.contracts.rate_cards.<a href="./src/metronome/resources/contracts/rate_cards/rate_cards.py">create</a>(\*\*<a href="src/metronome/types/contracts/rate_card_create_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_card_create_response.py">RateCardCreateResponse</a></code>
- <code title="post /contract-pricing/rate-cards/get">client.contracts.rate_cards.<a href="./src/metronome/resources/contracts/rate_cards/rate_cards.py">retrieve</a>(\*\*<a href="src/metronome/types/contracts/rate_card_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_card_retrieve_response.py">RateCardRetrieveResponse</a></code>
- <code title="post /contract-pricing/rate-cards/update">client.contracts.rate_cards.<a href="./src/metronome/resources/contracts/rate_cards/rate_cards.py">update</a>(\*\*<a href="src/metronome/types/contracts/rate_card_update_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_card_update_response.py">RateCardUpdateResponse</a></code>
- <code title="post /contract-pricing/rate-cards/list">client.contracts.rate_cards.<a href="./src/metronome/resources/contracts/rate_cards/rate_cards.py">list</a>(\*\*<a href="src/metronome/types/contracts/rate_card_list_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_card_list_response.py">SyncCursorPage[RateCardListResponse]</a></code>
- <code title="post /contract-pricing/rate-cards/getRateSchedule">client.contracts.rate_cards.<a href="./src/metronome/resources/contracts/rate_cards/rate_cards.py">retrieve_rate_schedule</a>(\*\*<a href="src/metronome/types/contracts/rate_card_retrieve_rate_schedule_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_card_retrieve_rate_schedule_response.py">RateCardRetrieveRateScheduleResponse</a></code>

### ProductOrders

Types:

```python
from metronome.types.contracts.rate_cards import ProductOrderUpdateResponse, ProductOrderSetResponse
```

Methods:

- <code title="post /contract-pricing/rate-cards/moveRateCardProducts">client.contracts.rate_cards.product_orders.<a href="./src/metronome/resources/contracts/rate_cards/product_orders.py">update</a>(\*\*<a href="src/metronome/types/contracts/rate_cards/product_order_update_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_cards/product_order_update_response.py">ProductOrderUpdateResponse</a></code>
- <code title="post /contract-pricing/rate-cards/setRateCardProductsOrder">client.contracts.rate_cards.product_orders.<a href="./src/metronome/resources/contracts/rate_cards/product_orders.py">set</a>(\*\*<a href="src/metronome/types/contracts/rate_cards/product_order_set_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_cards/product_order_set_response.py">ProductOrderSetResponse</a></code>

### Rates

Types:

```python
from metronome.types.contracts.rate_cards import (
    RateListResponse,
    RateAddResponse,
    RateAddManyResponse,
)
```

Methods:

- <code title="post /contract-pricing/rate-cards/getRates">client.contracts.rate_cards.rates.<a href="./src/metronome/resources/contracts/rate_cards/rates.py">list</a>(\*\*<a href="src/metronome/types/contracts/rate_cards/rate_list_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_cards/rate_list_response.py">SyncCursorPage[RateListResponse]</a></code>
- <code title="post /contract-pricing/rate-cards/addRate">client.contracts.rate_cards.rates.<a href="./src/metronome/resources/contracts/rate_cards/rates.py">add</a>(\*\*<a href="src/metronome/types/contracts/rate_cards/rate_add_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_cards/rate_add_response.py">RateAddResponse</a></code>
- <code title="post /contract-pricing/rate-cards/addRates">client.contracts.rate_cards.rates.<a href="./src/metronome/resources/contracts/rate_cards/rates.py">add_many</a>(\*\*<a href="src/metronome/types/contracts/rate_cards/rate_add_many_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_cards/rate_add_many_response.py">RateAddManyResponse</a></code>

### NamedSchedules

Types:

```python
from metronome.types.contracts.rate_cards import NamedScheduleRetrieveResponse
```

Methods:

- <code title="post /contracts/getNamedSchedule">client.contracts.rate_cards.named_schedules.<a href="./src/metronome/resources/contracts/rate_cards/named_schedules.py">retrieve</a>(\*\*<a href="src/metronome/types/contracts/rate_cards/named_schedule_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/contracts/rate_cards/named_schedule_retrieve_response.py">NamedScheduleRetrieveResponse</a></code>
- <code title="post /contracts/updateNamedSchedule">client.contracts.rate_cards.named_schedules.<a href="./src/metronome/resources/contracts/rate_cards/named_schedules.py">update</a>(\*\*<a href="src/metronome/types/contracts/rate_cards/named_schedule_update_params.py">params</a>) -> None</code>

## NamedSchedules

Types:

```python
from metronome.types.contracts import NamedScheduleRetrieveResponse
```

Methods:

- <code title="post /contract-pricing/rate-cards/getNamedSchedule">client.contracts.named_schedules.<a href="./src/metronome/resources/contracts/named_schedules.py">retrieve</a>(\*\*<a href="src/metronome/types/contracts/named_schedule_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/contracts/named_schedule_retrieve_response.py">NamedScheduleRetrieveResponse</a></code>
- <code title="post /contract-pricing/rate-cards/updateNamedSchedule">client.contracts.named_schedules.<a href="./src/metronome/resources/contracts/named_schedules.py">update</a>(\*\*<a href="src/metronome/types/contracts/named_schedule_update_params.py">params</a>) -> None</code>
