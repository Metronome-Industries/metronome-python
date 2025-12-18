# Shared Types

```python
from metronome.types import (
    BaseThresholdCommit,
    BaseUsageFilter,
    Commit,
    CommitHierarchyConfiguration,
    CommitRate,
    CommitSpecifier,
    CommitSpecifierInput,
    Contract,
    ContractV2,
    ContractWithoutAmendments,
    Credit,
    CreditTypeData,
    Discount,
    EventTypeFilter,
    HierarchyConfiguration,
    ID,
    Override,
    OverrideTier,
    OverwriteRate,
    PaymentGateConfig,
    PaymentGateConfigV2,
    PrepaidBalanceThresholdConfiguration,
    PrepaidBalanceThresholdConfigurationV2,
    PropertyFilter,
    ProService,
    Rate,
    RecurringCommitSubscriptionConfig,
    ScheduledCharge,
    ScheduleDuration,
    SchedulePointInTime,
    SpendThresholdConfiguration,
    SpendThresholdConfigurationV2,
    Subscription,
    Tier,
    UpdateBaseThresholdCommit,
)
```

# V2

## Contracts

Types:

```python
from metronome.types.v2 import (
    ContractRetrieveResponse,
    ContractListResponse,
    ContractEditResponse,
    ContractEditCommitResponse,
    ContractEditCreditResponse,
    ContractGetEditHistoryResponse,
)
```

Methods:

- <code title="post /v2/contracts/get">client.v2.contracts.<a href="./src/metronome/resources/v2/contracts.py">retrieve</a>(\*\*<a href="src/metronome/types/v2/contract_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v2/contract_retrieve_response.py">ContractRetrieveResponse</a></code>
- <code title="post /v2/contracts/list">client.v2.contracts.<a href="./src/metronome/resources/v2/contracts.py">list</a>(\*\*<a href="src/metronome/types/v2/contract_list_params.py">params</a>) -> <a href="./src/metronome/types/v2/contract_list_response.py">ContractListResponse</a></code>
- <code title="post /v2/contracts/edit">client.v2.contracts.<a href="./src/metronome/resources/v2/contracts.py">edit</a>(\*\*<a href="src/metronome/types/v2/contract_edit_params.py">params</a>) -> <a href="./src/metronome/types/v2/contract_edit_response.py">ContractEditResponse</a></code>
- <code title="post /v2/contracts/commits/edit">client.v2.contracts.<a href="./src/metronome/resources/v2/contracts.py">edit_commit</a>(\*\*<a href="src/metronome/types/v2/contract_edit_commit_params.py">params</a>) -> <a href="./src/metronome/types/v2/contract_edit_commit_response.py">ContractEditCommitResponse</a></code>
- <code title="post /v2/contracts/credits/edit">client.v2.contracts.<a href="./src/metronome/resources/v2/contracts.py">edit_credit</a>(\*\*<a href="src/metronome/types/v2/contract_edit_credit_params.py">params</a>) -> <a href="./src/metronome/types/v2/contract_edit_credit_response.py">ContractEditCreditResponse</a></code>
- <code title="post /v2/contracts/getEditHistory">client.v2.contracts.<a href="./src/metronome/resources/v2/contracts.py">get_edit_history</a>(\*\*<a href="src/metronome/types/v2/contract_get_edit_history_params.py">params</a>) -> <a href="./src/metronome/types/v2/contract_get_edit_history_response.py">ContractGetEditHistoryResponse</a></code>

# V1

## Alerts

Types:

```python
from metronome.types.v1 import AlertCreateResponse, AlertArchiveResponse
```

Methods:

- <code title="post /v1/alerts/create">client.v1.alerts.<a href="./src/metronome/resources/v1/alerts.py">create</a>(\*\*<a href="src/metronome/types/v1/alert_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/alert_create_response.py">AlertCreateResponse</a></code>
- <code title="post /v1/alerts/archive">client.v1.alerts.<a href="./src/metronome/resources/v1/alerts.py">archive</a>(\*\*<a href="src/metronome/types/v1/alert_archive_params.py">params</a>) -> <a href="./src/metronome/types/v1/alert_archive_response.py">AlertArchiveResponse</a></code>

## Plans

Types:

```python
from metronome.types.v1 import (
    PlanDetail,
    PlanListResponse,
    PlanGetDetailsResponse,
    PlanListChargesResponse,
    PlanListCustomersResponse,
)
```

Methods:

- <code title="get /v1/plans">client.v1.plans.<a href="./src/metronome/resources/v1/plans.py">list</a>(\*\*<a href="src/metronome/types/v1/plan_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/plan_list_response.py">SyncCursorPage[PlanListResponse]</a></code>
- <code title="get /v1/planDetails/{plan_id}">client.v1.plans.<a href="./src/metronome/resources/v1/plans.py">get_details</a>(\*, plan_id) -> <a href="./src/metronome/types/v1/plan_get_details_response.py">PlanGetDetailsResponse</a></code>
- <code title="get /v1/planDetails/{plan_id}/charges">client.v1.plans.<a href="./src/metronome/resources/v1/plans.py">list_charges</a>(\*, plan_id, \*\*<a href="src/metronome/types/v1/plan_list_charges_params.py">params</a>) -> <a href="./src/metronome/types/v1/plan_list_charges_response.py">SyncCursorPage[PlanListChargesResponse]</a></code>
- <code title="get /v1/planDetails/{plan_id}/customers">client.v1.plans.<a href="./src/metronome/resources/v1/plans.py">list_customers</a>(\*, plan_id, \*\*<a href="src/metronome/types/v1/plan_list_customers_params.py">params</a>) -> <a href="./src/metronome/types/v1/plan_list_customers_response.py">SyncCursorPage[PlanListCustomersResponse]</a></code>

## CreditGrants

Types:

```python
from metronome.types.v1 import (
    CreditLedgerEntry,
    RolloverAmountMaxAmount,
    RolloverAmountMaxPercentage,
    CreditGrantCreateResponse,
    CreditGrantListResponse,
    CreditGrantEditResponse,
    CreditGrantListEntriesResponse,
    CreditGrantVoidResponse,
)
```

Methods:

- <code title="post /v1/credits/createGrant">client.v1.credit_grants.<a href="./src/metronome/resources/v1/credit_grants.py">create</a>(\*\*<a href="src/metronome/types/v1/credit_grant_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/credit_grant_create_response.py">CreditGrantCreateResponse</a></code>
- <code title="post /v1/credits/listGrants">client.v1.credit_grants.<a href="./src/metronome/resources/v1/credit_grants.py">list</a>(\*\*<a href="src/metronome/types/v1/credit_grant_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/credit_grant_list_response.py">SyncCursorPage[CreditGrantListResponse]</a></code>
- <code title="post /v1/credits/editGrant">client.v1.credit_grants.<a href="./src/metronome/resources/v1/credit_grants.py">edit</a>(\*\*<a href="src/metronome/types/v1/credit_grant_edit_params.py">params</a>) -> <a href="./src/metronome/types/v1/credit_grant_edit_response.py">CreditGrantEditResponse</a></code>
- <code title="post /v1/credits/listEntries">client.v1.credit_grants.<a href="./src/metronome/resources/v1/credit_grants.py">list_entries</a>(\*\*<a href="src/metronome/types/v1/credit_grant_list_entries_params.py">params</a>) -> <a href="./src/metronome/types/v1/credit_grant_list_entries_response.py">SyncCursorPageWithoutLimit[CreditGrantListEntriesResponse]</a></code>
- <code title="post /v1/credits/voidGrant">client.v1.credit_grants.<a href="./src/metronome/resources/v1/credit_grants.py">void</a>(\*\*<a href="src/metronome/types/v1/credit_grant_void_params.py">params</a>) -> <a href="./src/metronome/types/v1/credit_grant_void_response.py">CreditGrantVoidResponse</a></code>

## PricingUnits

Types:

```python
from metronome.types.v1 import PricingUnitListResponse
```

Methods:

- <code title="get /v1/credit-types/list">client.v1.pricing_units.<a href="./src/metronome/resources/v1/pricing_units.py">list</a>(\*\*<a href="src/metronome/types/v1/pricing_unit_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/pricing_unit_list_response.py">SyncCursorPage[PricingUnitListResponse]</a></code>

## Customers

Types:

```python
from metronome.types.v1 import (
    Customer,
    CustomerDetail,
    CustomerCreateResponse,
    CustomerRetrieveResponse,
    CustomerArchiveResponse,
    CustomerListBillableMetricsResponse,
    CustomerListCostsResponse,
    CustomerPreviewEventsResponse,
    CustomerRetrieveBillingConfigurationsResponse,
    CustomerSetBillingConfigurationsResponse,
    CustomerSetNameResponse,
)
```

Methods:

- <code title="post /v1/customers">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">create</a>(\*\*<a href="src/metronome/types/v1/customer_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_create_response.py">CustomerCreateResponse</a></code>
- <code title="get /v1/customers/{customer_id}">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">retrieve</a>(\*, customer_id) -> <a href="./src/metronome/types/v1/customer_retrieve_response.py">CustomerRetrieveResponse</a></code>
- <code title="get /v1/customers">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">list</a>(\*\*<a href="src/metronome/types/v1/customer_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_detail.py">SyncCursorPage[CustomerDetail]</a></code>
- <code title="post /v1/customers/archive">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">archive</a>(\*\*<a href="src/metronome/types/v1/customer_archive_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_archive_response.py">CustomerArchiveResponse</a></code>
- <code title="get /v1/customers/{customer_id}/billable-metrics">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">list_billable_metrics</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customer_list_billable_metrics_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_list_billable_metrics_response.py">SyncCursorPage[CustomerListBillableMetricsResponse]</a></code>
- <code title="get /v1/customers/{customer_id}/costs">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">list_costs</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customer_list_costs_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_list_costs_response.py">SyncCursorPage[CustomerListCostsResponse]</a></code>
- <code title="post /v1/customers/{customer_id}/previewEvents">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">preview_events</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customer_preview_events_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_preview_events_response.py">CustomerPreviewEventsResponse</a></code>
- <code title="post /v1/getCustomerBillingProviderConfigurations">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">retrieve_billing_configurations</a>(\*\*<a href="src/metronome/types/v1/customer_retrieve_billing_configurations_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_retrieve_billing_configurations_response.py">CustomerRetrieveBillingConfigurationsResponse</a></code>
- <code title="post /v1/setCustomerBillingProviderConfigurations">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">set_billing_configurations</a>(\*\*<a href="src/metronome/types/v1/customer_set_billing_configurations_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_set_billing_configurations_response.py">CustomerSetBillingConfigurationsResponse</a></code>
- <code title="post /v1/customers/{customer_id}/setIngestAliases">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">set_ingest_aliases</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customer_set_ingest_aliases_params.py">params</a>) -> None</code>
- <code title="post /v1/customers/{customer_id}/setName">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">set_name</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customer_set_name_params.py">params</a>) -> <a href="./src/metronome/types/v1/customer_set_name_response.py">CustomerSetNameResponse</a></code>
- <code title="post /v1/customers/{customer_id}/updateConfig">client.v1.customers.<a href="./src/metronome/resources/v1/customers/customers.py">update_config</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customer_update_config_params.py">params</a>) -> None</code>

### Alerts

Types:

```python
from metronome.types.v1.customers import CustomerAlert, AlertRetrieveResponse
```

Methods:

- <code title="post /v1/customer-alerts/get">client.v1.customers.alerts.<a href="./src/metronome/resources/v1/customers/alerts.py">retrieve</a>(\*\*<a href="src/metronome/types/v1/customers/alert_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/alert_retrieve_response.py">AlertRetrieveResponse</a></code>
- <code title="post /v1/customer-alerts/list">client.v1.customers.alerts.<a href="./src/metronome/resources/v1/customers/alerts.py">list</a>(\*\*<a href="src/metronome/types/v1/customers/alert_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/customer_alert.py">SyncCursorPageWithoutLimit[CustomerAlert]</a></code>
- <code title="post /v1/customer-alerts/reset">client.v1.customers.alerts.<a href="./src/metronome/resources/v1/customers/alerts.py">reset</a>(\*\*<a href="src/metronome/types/v1/customers/alert_reset_params.py">params</a>) -> None</code>

### Plans

Types:

```python
from metronome.types.v1.customers import (
    PlanListResponse,
    PlanAddResponse,
    PlanEndResponse,
    PlanListPriceAdjustmentsResponse,
)
```

Methods:

- <code title="get /v1/customers/{customer_id}/plans">client.v1.customers.plans.<a href="./src/metronome/resources/v1/customers/plans.py">list</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customers/plan_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/plan_list_response.py">SyncCursorPage[PlanListResponse]</a></code>
- <code title="post /v1/customers/{customer_id}/plans/add">client.v1.customers.plans.<a href="./src/metronome/resources/v1/customers/plans.py">add</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customers/plan_add_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/plan_add_response.py">PlanAddResponse</a></code>
- <code title="post /v1/customers/{customer_id}/plans/{customer_plan_id}/end">client.v1.customers.plans.<a href="./src/metronome/resources/v1/customers/plans.py">end</a>(\*, customer_id, customer_plan_id, \*\*<a href="src/metronome/types/v1/customers/plan_end_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/plan_end_response.py">PlanEndResponse</a></code>
- <code title="get /v1/customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments">client.v1.customers.plans.<a href="./src/metronome/resources/v1/customers/plans.py">list_price_adjustments</a>(\*, customer_id, customer_plan_id, \*\*<a href="src/metronome/types/v1/customers/plan_list_price_adjustments_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/plan_list_price_adjustments_response.py">SyncCursorPage[PlanListPriceAdjustmentsResponse]</a></code>

### Invoices

Types:

```python
from metronome.types.v1.customers import (
    Invoice,
    InvoiceRetrieveResponse,
    InvoiceAddChargeResponse,
    InvoiceListBreakdownsResponse,
)
```

Methods:

- <code title="get /v1/customers/{customer_id}/invoices/{invoice_id}">client.v1.customers.invoices.<a href="./src/metronome/resources/v1/customers/invoices.py">retrieve</a>(\*, customer_id, invoice_id, \*\*<a href="src/metronome/types/v1/customers/invoice_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="get /v1/customers/{customer_id}/invoices">client.v1.customers.invoices.<a href="./src/metronome/resources/v1/customers/invoices.py">list</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customers/invoice_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/invoice.py">SyncCursorPage[Invoice]</a></code>
- <code title="post /v1/customers/{customer_id}/addCharge">client.v1.customers.invoices.<a href="./src/metronome/resources/v1/customers/invoices.py">add_charge</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customers/invoice_add_charge_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/invoice_add_charge_response.py">InvoiceAddChargeResponse</a></code>
- <code title="get /v1/customers/{customer_id}/invoices/breakdowns">client.v1.customers.invoices.<a href="./src/metronome/resources/v1/customers/invoices.py">list_breakdowns</a>(\*, customer_id, \*\*<a href="src/metronome/types/v1/customers/invoice_list_breakdowns_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/invoice_list_breakdowns_response.py">SyncCursorPage[InvoiceListBreakdownsResponse]</a></code>
- <code title="get /v1/customers/{customer_id}/invoices/{invoice_id}/pdf">client.v1.customers.invoices.<a href="./src/metronome/resources/v1/customers/invoices.py">retrieve_pdf</a>(\*, customer_id, invoice_id) -> BinaryAPIResponse</code>

### BillingConfig

Types:

```python
from metronome.types.v1.customers import BillingConfigRetrieveResponse
```

Methods:

- <code title="post /v1/customers/{customer_id}/billing-config/{billing_provider_type}">client.v1.customers.billing_config.<a href="./src/metronome/resources/v1/customers/billing_config.py">create</a>(\*, customer_id, billing_provider_type, \*\*<a href="src/metronome/types/v1/customers/billing_config_create_params.py">params</a>) -> None</code>
- <code title="get /v1/customers/{customer_id}/billing-config/{billing_provider_type}">client.v1.customers.billing_config.<a href="./src/metronome/resources/v1/customers/billing_config.py">retrieve</a>(\*, customer_id, billing_provider_type) -> <a href="./src/metronome/types/v1/customers/billing_config_retrieve_response.py">BillingConfigRetrieveResponse</a></code>
- <code title="delete /v1/customers/{customer_id}/billing-config/{billing_provider_type}">client.v1.customers.billing_config.<a href="./src/metronome/resources/v1/customers/billing_config.py">delete</a>(\*, customer_id, billing_provider_type) -> None</code>

### Commits

Types:

```python
from metronome.types.v1.customers import CommitCreateResponse, CommitUpdateEndDateResponse
```

Methods:

- <code title="post /v1/contracts/customerCommits/create">client.v1.customers.commits.<a href="./src/metronome/resources/v1/customers/commits.py">create</a>(\*\*<a href="src/metronome/types/v1/customers/commit_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/commit_create_response.py">CommitCreateResponse</a></code>
- <code title="post /v1/contracts/customerCommits/list">client.v1.customers.commits.<a href="./src/metronome/resources/v1/customers/commits.py">list</a>(\*\*<a href="src/metronome/types/v1/customers/commit_list_params.py">params</a>) -> <a href="./src/metronome/types/shared/commit.py">SyncBodyCursorPage[Commit]</a></code>
- <code title="post /v1/contracts/customerCommits/updateEndDate">client.v1.customers.commits.<a href="./src/metronome/resources/v1/customers/commits.py">update_end_date</a>(\*\*<a href="src/metronome/types/v1/customers/commit_update_end_date_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/commit_update_end_date_response.py">CommitUpdateEndDateResponse</a></code>

### Credits

Types:

```python
from metronome.types.v1.customers import CreditCreateResponse, CreditUpdateEndDateResponse
```

Methods:

- <code title="post /v1/contracts/customerCredits/create">client.v1.customers.credits.<a href="./src/metronome/resources/v1/customers/credits.py">create</a>(\*\*<a href="src/metronome/types/v1/customers/credit_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/credit_create_response.py">CreditCreateResponse</a></code>
- <code title="post /v1/contracts/customerCredits/list">client.v1.customers.credits.<a href="./src/metronome/resources/v1/customers/credits.py">list</a>(\*\*<a href="src/metronome/types/v1/customers/credit_list_params.py">params</a>) -> <a href="./src/metronome/types/shared/credit.py">SyncBodyCursorPage[Credit]</a></code>
- <code title="post /v1/contracts/customerCredits/updateEndDate">client.v1.customers.credits.<a href="./src/metronome/resources/v1/customers/credits.py">update_end_date</a>(\*\*<a href="src/metronome/types/v1/customers/credit_update_end_date_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/credit_update_end_date_response.py">CreditUpdateEndDateResponse</a></code>

### NamedSchedules

Types:

```python
from metronome.types.v1.customers import NamedScheduleRetrieveResponse
```

Methods:

- <code title="post /v1/customers/getNamedSchedule">client.v1.customers.named_schedules.<a href="./src/metronome/resources/v1/customers/named_schedules.py">retrieve</a>(\*\*<a href="src/metronome/types/v1/customers/named_schedule_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/customers/named_schedule_retrieve_response.py">NamedScheduleRetrieveResponse</a></code>
- <code title="post /v1/customers/updateNamedSchedule">client.v1.customers.named_schedules.<a href="./src/metronome/resources/v1/customers/named_schedules.py">update</a>(\*\*<a href="src/metronome/types/v1/customers/named_schedule_update_params.py">params</a>) -> None</code>

## Dashboards

Types:

```python
from metronome.types.v1 import DashboardGetEmbeddableURLResponse
```

Methods:

- <code title="post /v1/dashboards/getEmbeddableUrl">client.v1.dashboards.<a href="./src/metronome/resources/v1/dashboards.py">get_embeddable_url</a>(\*\*<a href="src/metronome/types/v1/dashboard_get_embeddable_url_params.py">params</a>) -> <a href="./src/metronome/types/v1/dashboard_get_embeddable_url_response.py">DashboardGetEmbeddableURLResponse</a></code>

## Usage

Types:

```python
from metronome.types.v1 import UsageListResponse, UsageListWithGroupsResponse, UsageSearchResponse
```

Methods:

- <code title="post /v1/usage">client.v1.usage.<a href="./src/metronome/resources/v1/usage.py">list</a>(\*\*<a href="src/metronome/types/v1/usage_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/usage_list_response.py">SyncCursorPageWithoutLimit[UsageListResponse]</a></code>
- <code title="post /v1/ingest">client.v1.usage.<a href="./src/metronome/resources/v1/usage.py">ingest</a>(\*\*<a href="src/metronome/types/v1/usage_ingest_params.py">params</a>) -> None</code>
- <code title="post /v1/usage/groups">client.v1.usage.<a href="./src/metronome/resources/v1/usage.py">list_with_groups</a>(\*\*<a href="src/metronome/types/v1/usage_list_with_groups_params.py">params</a>) -> <a href="./src/metronome/types/v1/usage_list_with_groups_response.py">SyncCursorPage[UsageListWithGroupsResponse]</a></code>
- <code title="post /v1/events/search">client.v1.usage.<a href="./src/metronome/resources/v1/usage.py">search</a>(\*\*<a href="src/metronome/types/v1/usage_search_params.py">params</a>) -> <a href="./src/metronome/types/v1/usage_search_response.py">UsageSearchResponse</a></code>

## AuditLogs

Types:

```python
from metronome.types.v1 import AuditLogListResponse
```

Methods:

- <code title="get /v1/auditLogs">client.v1.audit_logs.<a href="./src/metronome/resources/v1/audit_logs.py">list</a>(\*\*<a href="src/metronome/types/v1/audit_log_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/audit_log_list_response.py">SyncCursorPage[AuditLogListResponse]</a></code>

## CustomFields

Types:

```python
from metronome.types.v1 import CustomFieldListKeysResponse
```

Methods:

- <code title="post /v1/customFields/addKey">client.v1.custom_fields.<a href="./src/metronome/resources/v1/custom_fields.py">add_key</a>(\*\*<a href="src/metronome/types/v1/custom_field_add_key_params.py">params</a>) -> None</code>
- <code title="post /v1/customFields/deleteValues">client.v1.custom_fields.<a href="./src/metronome/resources/v1/custom_fields.py">delete_values</a>(\*\*<a href="src/metronome/types/v1/custom_field_delete_values_params.py">params</a>) -> None</code>
- <code title="post /v1/customFields/listKeys">client.v1.custom_fields.<a href="./src/metronome/resources/v1/custom_fields.py">list_keys</a>(\*\*<a href="src/metronome/types/v1/custom_field_list_keys_params.py">params</a>) -> <a href="./src/metronome/types/v1/custom_field_list_keys_response.py">SyncCursorPageWithoutLimit[CustomFieldListKeysResponse]</a></code>
- <code title="post /v1/customFields/removeKey">client.v1.custom_fields.<a href="./src/metronome/resources/v1/custom_fields.py">remove_key</a>(\*\*<a href="src/metronome/types/v1/custom_field_remove_key_params.py">params</a>) -> None</code>
- <code title="post /v1/customFields/setValues">client.v1.custom_fields.<a href="./src/metronome/resources/v1/custom_fields.py">set_values</a>(\*\*<a href="src/metronome/types/v1/custom_field_set_values_params.py">params</a>) -> None</code>

## BillableMetrics

Types:

```python
from metronome.types.v1 import (
    BillableMetricCreateResponse,
    BillableMetricRetrieveResponse,
    BillableMetricListResponse,
    BillableMetricArchiveResponse,
)
```

Methods:

- <code title="post /v1/billable-metrics/create">client.v1.billable_metrics.<a href="./src/metronome/resources/v1/billable_metrics.py">create</a>(\*\*<a href="src/metronome/types/v1/billable_metric_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/billable_metric_create_response.py">BillableMetricCreateResponse</a></code>
- <code title="get /v1/billable-metrics/{billable_metric_id}">client.v1.billable_metrics.<a href="./src/metronome/resources/v1/billable_metrics.py">retrieve</a>(\*, billable_metric_id) -> <a href="./src/metronome/types/v1/billable_metric_retrieve_response.py">BillableMetricRetrieveResponse</a></code>
- <code title="get /v1/billable-metrics">client.v1.billable_metrics.<a href="./src/metronome/resources/v1/billable_metrics.py">list</a>(\*\*<a href="src/metronome/types/v1/billable_metric_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/billable_metric_list_response.py">SyncCursorPage[BillableMetricListResponse]</a></code>
- <code title="post /v1/billable-metrics/archive">client.v1.billable_metrics.<a href="./src/metronome/resources/v1/billable_metrics.py">archive</a>(\*\*<a href="src/metronome/types/v1/billable_metric_archive_params.py">params</a>) -> <a href="./src/metronome/types/v1/billable_metric_archive_response.py">BillableMetricArchiveResponse</a></code>

## Services

Types:

```python
from metronome.types.v1 import ServiceListResponse
```

Methods:

- <code title="get /v1/services">client.v1.services.<a href="./src/metronome/resources/v1/services.py">list</a>() -> <a href="./src/metronome/types/v1/service_list_response.py">ServiceListResponse</a></code>

## Invoices

Types:

```python
from metronome.types.v1 import InvoiceRegenerateResponse, InvoiceVoidResponse
```

Methods:

- <code title="post /v1/invoices/regenerate">client.v1.invoices.<a href="./src/metronome/resources/v1/invoices.py">regenerate</a>(\*\*<a href="src/metronome/types/v1/invoice_regenerate_params.py">params</a>) -> <a href="./src/metronome/types/v1/invoice_regenerate_response.py">InvoiceRegenerateResponse</a></code>
- <code title="post /v1/invoices/void">client.v1.invoices.<a href="./src/metronome/resources/v1/invoices.py">void</a>(\*\*<a href="src/metronome/types/v1/invoice_void_params.py">params</a>) -> <a href="./src/metronome/types/v1/invoice_void_response.py">InvoiceVoidResponse</a></code>

## Contracts

Types:

```python
from metronome.types.v1 import (
    ContractCreateResponse,
    ContractRetrieveResponse,
    ContractListResponse,
    ContractAmendResponse,
    ContractArchiveResponse,
    ContractCreateHistoricalInvoicesResponse,
    ContractListBalancesResponse,
    ContractRetrieveRateScheduleResponse,
    ContractRetrieveSubscriptionQuantityHistoryResponse,
    ContractScheduleProServicesInvoiceResponse,
    ContractUpdateEndDateResponse,
)
```

Methods:

- <code title="post /v1/contracts/create">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">create</a>(\*\*<a href="src/metronome/types/v1/contract_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_create_response.py">ContractCreateResponse</a></code>
- <code title="post /v1/contracts/get">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">retrieve</a>(\*\*<a href="src/metronome/types/v1/contract_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_retrieve_response.py">ContractRetrieveResponse</a></code>
- <code title="post /v1/contracts/list">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">list</a>(\*\*<a href="src/metronome/types/v1/contract_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_list_response.py">ContractListResponse</a></code>
- <code title="post /v1/contracts/addManualBalanceLedgerEntry">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">add_manual_balance_entry</a>(\*\*<a href="src/metronome/types/v1/contract_add_manual_balance_entry_params.py">params</a>) -> None</code>
- <code title="post /v1/contracts/amend">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">amend</a>(\*\*<a href="src/metronome/types/v1/contract_amend_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_amend_response.py">ContractAmendResponse</a></code>
- <code title="post /v1/contracts/archive">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">archive</a>(\*\*<a href="src/metronome/types/v1/contract_archive_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_archive_response.py">ContractArchiveResponse</a></code>
- <code title="post /v1/contracts/createHistoricalInvoices">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">create_historical_invoices</a>(\*\*<a href="src/metronome/types/v1/contract_create_historical_invoices_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_create_historical_invoices_response.py">ContractCreateHistoricalInvoicesResponse</a></code>
- <code title="post /v1/contracts/customerBalances/list">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">list_balances</a>(\*\*<a href="src/metronome/types/v1/contract_list_balances_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_list_balances_response.py">SyncBodyCursorPage[ContractListBalancesResponse]</a></code>
- <code title="post /v1/contracts/getContractRateSchedule">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">retrieve_rate_schedule</a>(\*\*<a href="src/metronome/types/v1/contract_retrieve_rate_schedule_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_retrieve_rate_schedule_response.py">ContractRetrieveRateScheduleResponse</a></code>
- <code title="post /v1/contracts/getSubscriptionQuantityHistory">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">retrieve_subscription_quantity_history</a>(\*\*<a href="src/metronome/types/v1/contract_retrieve_subscription_quantity_history_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_retrieve_subscription_quantity_history_response.py">ContractRetrieveSubscriptionQuantityHistoryResponse</a></code>
- <code title="post /v1/contracts/scheduleProServicesInvoice">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">schedule_pro_services_invoice</a>(\*\*<a href="src/metronome/types/v1/contract_schedule_pro_services_invoice_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_schedule_pro_services_invoice_response.py">ContractScheduleProServicesInvoiceResponse</a></code>
- <code title="post /v1/contracts/setUsageFilter">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">set_usage_filter</a>(\*\*<a href="src/metronome/types/v1/contract_set_usage_filter_params.py">params</a>) -> None</code>
- <code title="post /v1/contracts/updateEndDate">client.v1.contracts.<a href="./src/metronome/resources/v1/contracts/contracts.py">update_end_date</a>(\*\*<a href="src/metronome/types/v1/contract_update_end_date_params.py">params</a>) -> <a href="./src/metronome/types/v1/contract_update_end_date_response.py">ContractUpdateEndDateResponse</a></code>

### Products

Types:

```python
from metronome.types.v1.contracts import (
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

- <code title="post /v1/contract-pricing/products/create">client.v1.contracts.products.<a href="./src/metronome/resources/v1/contracts/products.py">create</a>(\*\*<a href="src/metronome/types/v1/contracts/product_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/product_create_response.py">ProductCreateResponse</a></code>
- <code title="post /v1/contract-pricing/products/get">client.v1.contracts.products.<a href="./src/metronome/resources/v1/contracts/products.py">retrieve</a>(\*\*<a href="src/metronome/types/v1/contracts/product_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/product_retrieve_response.py">ProductRetrieveResponse</a></code>
- <code title="post /v1/contract-pricing/products/update">client.v1.contracts.products.<a href="./src/metronome/resources/v1/contracts/products.py">update</a>(\*\*<a href="src/metronome/types/v1/contracts/product_update_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/product_update_response.py">ProductUpdateResponse</a></code>
- <code title="post /v1/contract-pricing/products/list">client.v1.contracts.products.<a href="./src/metronome/resources/v1/contracts/products.py">list</a>(\*\*<a href="src/metronome/types/v1/contracts/product_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/product_list_response.py">SyncCursorPage[ProductListResponse]</a></code>
- <code title="post /v1/contract-pricing/products/archive">client.v1.contracts.products.<a href="./src/metronome/resources/v1/contracts/products.py">archive</a>(\*\*<a href="src/metronome/types/v1/contracts/product_archive_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/product_archive_response.py">ProductArchiveResponse</a></code>

### RateCards

Types:

```python
from metronome.types.v1.contracts import (
    RateCardCreateResponse,
    RateCardRetrieveResponse,
    RateCardUpdateResponse,
    RateCardListResponse,
    RateCardArchiveResponse,
    RateCardRetrieveRateScheduleResponse,
)
```

Methods:

- <code title="post /v1/contract-pricing/rate-cards/create">client.v1.contracts.rate_cards.<a href="./src/metronome/resources/v1/contracts/rate_cards/rate_cards.py">create</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_card_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_card_create_response.py">RateCardCreateResponse</a></code>
- <code title="post /v1/contract-pricing/rate-cards/get">client.v1.contracts.rate_cards.<a href="./src/metronome/resources/v1/contracts/rate_cards/rate_cards.py">retrieve</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_card_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_card_retrieve_response.py">RateCardRetrieveResponse</a></code>
- <code title="post /v1/contract-pricing/rate-cards/update">client.v1.contracts.rate_cards.<a href="./src/metronome/resources/v1/contracts/rate_cards/rate_cards.py">update</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_card_update_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_card_update_response.py">RateCardUpdateResponse</a></code>
- <code title="post /v1/contract-pricing/rate-cards/list">client.v1.contracts.rate_cards.<a href="./src/metronome/resources/v1/contracts/rate_cards/rate_cards.py">list</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_card_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_card_list_response.py">SyncCursorPage[RateCardListResponse]</a></code>
- <code title="post /v1/contract-pricing/rate-cards/archive">client.v1.contracts.rate_cards.<a href="./src/metronome/resources/v1/contracts/rate_cards/rate_cards.py">archive</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_card_archive_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_card_archive_response.py">RateCardArchiveResponse</a></code>
- <code title="post /v1/contract-pricing/rate-cards/getRateSchedule">client.v1.contracts.rate_cards.<a href="./src/metronome/resources/v1/contracts/rate_cards/rate_cards.py">retrieve_rate_schedule</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_card_retrieve_rate_schedule_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_card_retrieve_rate_schedule_response.py">RateCardRetrieveRateScheduleResponse</a></code>

#### ProductOrders

Types:

```python
from metronome.types.v1.contracts.rate_cards import (
    ProductOrderUpdateResponse,
    ProductOrderSetResponse,
)
```

Methods:

- <code title="post /v1/contract-pricing/rate-cards/moveRateCardProducts">client.v1.contracts.rate_cards.product_orders.<a href="./src/metronome/resources/v1/contracts/rate_cards/product_orders.py">update</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_cards/product_order_update_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_cards/product_order_update_response.py">ProductOrderUpdateResponse</a></code>
- <code title="post /v1/contract-pricing/rate-cards/setRateCardProductsOrder">client.v1.contracts.rate_cards.product_orders.<a href="./src/metronome/resources/v1/contracts/rate_cards/product_orders.py">set</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_cards/product_order_set_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_cards/product_order_set_response.py">ProductOrderSetResponse</a></code>

#### Rates

Types:

```python
from metronome.types.v1.contracts.rate_cards import (
    RateListResponse,
    RateAddResponse,
    RateAddManyResponse,
)
```

Methods:

- <code title="post /v1/contract-pricing/rate-cards/getRates">client.v1.contracts.rate_cards.rates.<a href="./src/metronome/resources/v1/contracts/rate_cards/rates.py">list</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_cards/rate_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_cards/rate_list_response.py">SyncCursorPage[RateListResponse]</a></code>
- <code title="post /v1/contract-pricing/rate-cards/addRate">client.v1.contracts.rate_cards.rates.<a href="./src/metronome/resources/v1/contracts/rate_cards/rates.py">add</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_cards/rate_add_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_cards/rate_add_response.py">RateAddResponse</a></code>
- <code title="post /v1/contract-pricing/rate-cards/addRates">client.v1.contracts.rate_cards.rates.<a href="./src/metronome/resources/v1/contracts/rate_cards/rates.py">add_many</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_cards/rate_add_many_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_cards/rate_add_many_response.py">RateAddManyResponse</a></code>

#### NamedSchedules

Types:

```python
from metronome.types.v1.contracts.rate_cards import NamedScheduleRetrieveResponse
```

Methods:

- <code title="post /v1/contracts/getNamedSchedule">client.v1.contracts.rate_cards.named_schedules.<a href="./src/metronome/resources/v1/contracts/rate_cards/named_schedules.py">retrieve</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_cards/named_schedule_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/rate_cards/named_schedule_retrieve_response.py">NamedScheduleRetrieveResponse</a></code>
- <code title="post /v1/contracts/updateNamedSchedule">client.v1.contracts.rate_cards.named_schedules.<a href="./src/metronome/resources/v1/contracts/rate_cards/named_schedules.py">update</a>(\*\*<a href="src/metronome/types/v1/contracts/rate_cards/named_schedule_update_params.py">params</a>) -> None</code>

### NamedSchedules

Types:

```python
from metronome.types.v1.contracts import NamedScheduleRetrieveResponse
```

Methods:

- <code title="post /v1/contract-pricing/rate-cards/getNamedSchedule">client.v1.contracts.named_schedules.<a href="./src/metronome/resources/v1/contracts/named_schedules.py">retrieve</a>(\*\*<a href="src/metronome/types/v1/contracts/named_schedule_retrieve_params.py">params</a>) -> <a href="./src/metronome/types/v1/contracts/named_schedule_retrieve_response.py">NamedScheduleRetrieveResponse</a></code>
- <code title="post /v1/contract-pricing/rate-cards/updateNamedSchedule">client.v1.contracts.named_schedules.<a href="./src/metronome/resources/v1/contracts/named_schedules.py">update</a>(\*\*<a href="src/metronome/types/v1/contracts/named_schedule_update_params.py">params</a>) -> None</code>

## Payments

Types:

```python
from metronome.types.v1 import Payment, PaymentStatus, PaymentAttemptResponse, PaymentCancelResponse
```

Methods:

- <code title="post /v1/payments/list">client.v1.payments.<a href="./src/metronome/resources/v1/payments.py">list</a>(\*\*<a href="src/metronome/types/v1/payment_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/payment.py">SyncBodyCursorPage[Payment]</a></code>
- <code title="post /v1/payments/attempt">client.v1.payments.<a href="./src/metronome/resources/v1/payments.py">attempt</a>(\*\*<a href="src/metronome/types/v1/payment_attempt_params.py">params</a>) -> <a href="./src/metronome/types/v1/payment_attempt_response.py">PaymentAttemptResponse</a></code>
- <code title="post /v1/payments/cancel">client.v1.payments.<a href="./src/metronome/resources/v1/payments.py">cancel</a>(\*\*<a href="src/metronome/types/v1/payment_cancel_params.py">params</a>) -> <a href="./src/metronome/types/v1/payment_cancel_response.py">PaymentCancelResponse</a></code>

## Settings

Types:

```python
from metronome.types.v1 import SettingUpsertAvalaraCredentialsResponse
```

Methods:

- <code title="post /v1/upsertAvalaraCredentials">client.v1.settings.<a href="./src/metronome/resources/v1/settings/settings.py">upsert_avalara_credentials</a>(\*\*<a href="src/metronome/types/v1/setting_upsert_avalara_credentials_params.py">params</a>) -> <a href="./src/metronome/types/v1/setting_upsert_avalara_credentials_response.py">SettingUpsertAvalaraCredentialsResponse</a></code>

### BillingProviders

Types:

```python
from metronome.types.v1.settings import BillingProviderCreateResponse, BillingProviderListResponse
```

Methods:

- <code title="post /v1/setUpBillingProvider">client.v1.settings.billing_providers.<a href="./src/metronome/resources/v1/settings/billing_providers.py">create</a>(\*\*<a href="src/metronome/types/v1/settings/billing_provider_create_params.py">params</a>) -> <a href="./src/metronome/types/v1/settings/billing_provider_create_response.py">BillingProviderCreateResponse</a></code>
- <code title="post /v1/listConfiguredBillingProviders">client.v1.settings.billing_providers.<a href="./src/metronome/resources/v1/settings/billing_providers.py">list</a>(\*\*<a href="src/metronome/types/v1/settings/billing_provider_list_params.py">params</a>) -> <a href="./src/metronome/types/v1/settings/billing_provider_list_response.py">BillingProviderListResponse</a></code>
