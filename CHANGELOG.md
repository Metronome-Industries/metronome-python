# Changelog

## 3.2.0 (2025-12-18)

Full Changelog: [v3.1.0...v3.2.0](https://github.com/Metronome-Industries/metronome-python/compare/v3.1.0...v3.2.0)

### Features

* [ORCH-605] uses x-mint groups to enable conditional rendering of gated revenue system config apis ([0a160fd](https://github.com/Metronome-Industries/metronome-python/commit/0a160fd9339d99dd03b25e7ad1346d3644f873a5))
* [ORCH-752] Update contract creation endpoints to allow setting revenue system configuration ([29726f1](https://github.com/Metronome-Industries/metronome-python/commit/29726f1244f3bd558999989c058e7801a1eaacb5))
* [ORCH-757] Add route for get revenue system config resolver ([471ddfa](https://github.com/Metronome-Industries/metronome-python/commit/471ddfa40d4a2575e31f3faaaee64a929b335bfa))
* Add `commit_transactions` to the body of `/upsertAvalaraCredentials` endpoint ([2fd481c](https://github.com/Metronome-Industries/metronome-python/commit/2fd481ce87b8d0095b2a0be3594e60b01538c7e9))
* Add `seat_filter` field to creation request and response parameters of the alert object ([d70fc72](https://github.com/Metronome-Industries/metronome-python/commit/d70fc72c306c60c96561fedc6419ad358e06f66b))
* add quantity to plan pricing adjustment response ([4eb5277](https://github.com/Metronome-Industries/metronome-python/commit/4eb5277b78a7670da7215b4bc2a4808860176222))
* adds external_payment_id to ExternalInvoice ([35e26be](https://github.com/Metronome-Industries/metronome-python/commit/35e26be2ede51e494fd0f96ef6dda5754e9141eb))
* everything ([82c61e6](https://github.com/Metronome-Industries/metronome-python/commit/82c61e68a13f41209335e783d365a59ab951b981))
* GET-6845 get openapi specs ready for GA ([b5fb320](https://github.com/Metronome-Industries/metronome-python/commit/b5fb320ba619c3de5428f9c2e08b922766d0ffac))
* include aggregation BM info from searchEvents ([8fa8457](https://github.com/Metronome-Industries/metronome-python/commit/8fa84575cb6b097acc3ca1b5048ea9df5f66af53))
* ORCH-833/948/946/947 - updated the API to accept aws_customer_account_id all gated behind a feature flag ([31af8fd](https://github.com/Metronome-Industries/metronome-python/commit/31af8fdb88445e31c8bfc047d5aebe8ac28a784f))
* remove beta language, FF, stainless skip ([cc5e7ed](https://github.com/Metronome-Industries/metronome-python/commit/cc5e7ed287fc356246f15cc2ff590a5b57fcfe6d))
* Return values for set customer billing configuration endpoint ([b546ff5](https://github.com/Metronome-Industries/metronome-python/commit/b546ff55b1a81cff28f3e5e18a780dfc935c2fc1))
* update create alert api to allow LowRemainingSeatBalanceReached alert ([28bbf3e](https://github.com/Metronome-Industries/metronome-python/commit/28bbf3ec4e2299d5cb8e1e8faba92399b8b27a06))


### Bug Fixes

* compat with Python 3.14 ([d033920](https://github.com/Metronome-Industries/metronome-python/commit/d033920ce482641ec7c705a592e20629c18c720f))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([8748946](https://github.com/Metronome-Industries/metronome-python/commit/8748946083d6f8582dc5d91446952f2987fca3f4))
* ensure streams are always closed ([25c3ae8](https://github.com/Metronome-Industries/metronome-python/commit/25c3ae8b2e0b26e0c720736b0c5831f8d892ea84))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([9231074](https://github.com/Metronome-Industries/metronome-python/commit/9231074106d4f8009dbfd7a0cc4cf76648a58f7d))
* use async_to_httpx_files in patch method ([d1b1be0](https://github.com/Metronome-Industries/metronome-python/commit/d1b1be0961af3e6d13c604f3ebca1573cd293a97))


### Chores

* add missing docstrings ([355fe47](https://github.com/Metronome-Industries/metronome-python/commit/355fe4740a7fc3ec4e608a1d2da0e7c8588b73ba))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([041a7d2](https://github.com/Metronome-Industries/metronome-python/commit/041a7d232490a1a9e9512f8ba43883f12f32eb19))
* **docs:** use environment variables for authentication in code snippets ([d7f37cd](https://github.com/Metronome-Industries/metronome-python/commit/d7f37cd1e1d26f3a1fff5cb39da8beb0b3f81df1))
* **internal:** add `--fix` argument to lint script ([39602a0](https://github.com/Metronome-Industries/metronome-python/commit/39602a0cd5cd28ca2784da697423fbda99a4bd41))
* **internal:** add missing files argument to base client ([0dd45c5](https://github.com/Metronome-Industries/metronome-python/commit/0dd45c5a13060fde96ffb7a2272001bcb6578736))
* **internal:** codegen related update ([00a67e8](https://github.com/Metronome-Industries/metronome-python/commit/00a67e8a38c5e470dec2221cc598eb677b2ae4ef))
* **internal:** codegen related update ([9014e90](https://github.com/Metronome-Industries/metronome-python/commit/9014e904870a05da89e2ef210117f70db746e864))
* **internal:** grammar fix (it's -&gt; its) ([e844546](https://github.com/Metronome-Industries/metronome-python/commit/e8445469bd3c10da8a3c6d99b1e441866d3e1277))
* **package:** drop Python 3.8 support ([caf05b2](https://github.com/Metronome-Industries/metronome-python/commit/caf05b2f01f75a1364b9a4d00b7eff8d79e8b1f3))
* update lockfile ([27cc4f3](https://github.com/Metronome-Industries/metronome-python/commit/27cc4f3f43f10c15209cb69c547eabd46c9f1b16))


### Documentation

* document missing fields for schemas related to recurring credits and commits ([3ecb1d7](https://github.com/Metronome-Industries/metronome-python/commit/3ecb1d7544db26e955f1b08e3cb1675c0613108a))

## 3.1.0 (2025-10-31)

Full Changelog: [v3.0.0...v3.1.0](https://github.com/Metronome-Industries/metronome-python/compare/v3.0.0...v3.1.0)

### Features

* [ORCH-282] plumb `payment_method_id` to the payment gateway object ([a8c98bb](https://github.com/Metronome-Industries/metronome-python/commit/a8c98bb612d3eab8318ff405ebe44a2e7a06bce3))
* [ORCH-797] add billing_provider_error to invoice.external_invoice ([25d584b](https://github.com/Metronome-Industries/metronome-python/commit/25d584b771a073e0ff1dfabfc0ed9fa9419ecfe1))
* Add avalara creds + billing provider APIs to SDK. Add avalara creds API to docs. ([f88624e](https://github.com/Metronome-Industries/metronome-python/commit/f88624ea8665948cc0f0430a4a6af2811ed1b1ee))
* add beta tag to stripe auto charge items ([f7eaf72](https://github.com/Metronome-Industries/metronome-python/commit/f7eaf72534bcdcebe1cfc22f74693a7f9de62257))
* add exclude_zero_balances field behind a FF for anthropic ([36af1bf](https://github.com/Metronome-Industries/metronome-python/commit/36af1bfcd66da1feb70165e378ba959d3cbee998))
* add METRONOME to BillingProvider type ([b64d7f6](https://github.com/Metronome-Industries/metronome-python/commit/b64d7f63fb5433927eb1c05deeaaa0f5d817f410))
* docs(api) Documentation for seat-based subscription linked recurring commits beta release ([0d2c224](https://github.com/Metronome-Industries/metronome-python/commit/0d2c2242ca6907b7447e962756ec1907f0cf5bf0))
* ignore_duplicates ([4025e58](https://github.com/Metronome-Industries/metronome-python/commit/4025e5896f98e0189aa5fbdd01ec7c0505e4332f))
* internal: moving plans docs to deprecated section of new docs site ([2db9469](https://github.com/Metronome-Industries/metronome-python/commit/2db9469e4eccd1d147579d09bf35ff7a1f2ca738))
* not ready for review ([ca07022](https://github.com/Metronome-Industries/metronome-python/commit/ca07022666e58b2a319d81c6e1a0fdcfe3a3b1b7))
* not ready for review ([0d0d478](https://github.com/Metronome-Industries/metronome-python/commit/0d0d478ec50247380402630c76176af5a5755800))
* Relax requirement on customer level commits for invoice_contract_id if do_not_invoice is set to true ([f74df85](https://github.com/Metronome-Industries/metronome-python/commit/f74df850bdb8085f27866f36234a8612488cf65f))
* update get customer alerts api to include low seat balance type ([4bdaa73](https://github.com/Metronome-Industries/metronome-python/commit/4bdaa732cce863d5ec97aa3bee6d2a17d58a3839))


### Bug Fixes

* **api:** Make id field required in /v2/notifications/edit ([ac261c2](https://github.com/Metronome-Industries/metronome-python/commit/ac261c2589c05db34216d2bf84141bab854a592a))
* **client:** close streams without requiring full consumption ([ed2abf0](https://github.com/Metronome-Industries/metronome-python/commit/ed2abf0e91e189da7a059f8b8db33b49de9a273a))


### Chores

* **api:** Note SQL BM is not supported in previewCustomerEvents description ([a75c6fd](https://github.com/Metronome-Industries/metronome-python/commit/a75c6fd81edcad1e4b1848c9a11599c2245b58f1))
* bump `httpx-aiohttp` version to 0.1.9 ([6fc03bc](https://github.com/Metronome-Industries/metronome-python/commit/6fc03bcde0da509f5bc4e6a8e32c769d4d5d24a4))
* **internal/tests:** avoid race condition with implicit client cleanup ([53f9064](https://github.com/Metronome-Industries/metronome-python/commit/53f90642543d6ea42dcde84344b3edaf0c0cfdfb))


### Documentation

* add migrate amendments to edits page ([d1f8d43](https://github.com/Metronome-Industries/metronome-python/commit/d1f8d43d5b2c3a3b3ae26b1d21c33dd0d381229b))

## 3.0.0 (2025-10-16)

Full Changelog: [v2.0.0...v3.0.0](https://github.com/Metronome-Industries/metronome-python/compare/v2.0.0...v3.0.0)

### ⚠ BREAKING CHANGES

* **api:** Remove customer_id from preview events payload

### Features

* **api:** Remove customer_id from preview events payload ([eba7907](https://github.com/Metronome-Industries/metronome-python/commit/eba7907bb25b48e74d2a396de89b03799e421091))
* internal: Skip retrieve_pdf API SDK tests ([a13288f](https://github.com/Metronome-Industries/metronome-python/commit/a13288f79cdf3d08a2d982cd2d343a348082f707))
* update api docs ([0458f1a](https://github.com/Metronome-Industries/metronome-python/commit/0458f1ab8d5a4eddca9850f977746020a80cefb6))

## 2.0.0 (2025-10-10)

Full Changelog: [v1.0.0...v2.0.0](https://github.com/Metronome-Industries/metronome-python/compare/v1.0.0...v2.0.0)

### ⚠ BREAKING CHANGES

* **api:** in getEditHistory endpoint, commit invoice schedule amount, unit price, and quantity are now optional values
* **api:** Added optional archive_filter param to /notifications/offset/list endpoint

### Features

* Add empty handler for cancelPayment ([777d872](https://github.com/Metronome-Industries/metronome-python/commit/777d872b5549d733053cde3c11289b2be70e951e))
* Add payment + billing invoice APIs to the API reference docs ([4de924a](https://github.com/Metronome-Industries/metronome-python/commit/4de924a5b8add780cf4381071794c5f275c38891))
* Add payment APIs to the SDK ([cece47e](https://github.com/Metronome-Industries/metronome-python/commit/cece47edb190d39233627b2353501b095f904b75))
* **api:** add billing_periods to Subscription ([cc6d4ab](https://github.com/Metronome-Industries/metronome-python/commit/cc6d4ab0b5bf00aa94751da93256ca72aaa67c71))
* **api:** add new payments/attempt v1 api endpoint ([cbc0ac2](https://github.com/Metronome-Industries/metronome-python/commit/cbc0ac2b8a72cb5744e0e4a955d26b040660333a))
* **api:** Added optional archive_filter param to /notifications/offset/list endpoint ([5f9d325](https://github.com/Metronome-Industries/metronome-python/commit/5f9d32558444a88dd3d734371c5ce98874a6b411))
* Bump graphql version and fix type errors ([5b17ec5](https://github.com/Metronome-Industries/metronome-python/commit/5b17ec58e14c2fa7be7ad65a8dd958af58644380))
* elia/orch 128 add external apis for payments ([cd501d0](https://github.com/Metronome-Industries/metronome-python/commit/cd501d0c2a6d55af24644ba7bbfef14079e7b7da))
* feat(api):Allow clients retrieve archived config via `/notifications/get` ([2ec6978](https://github.com/Metronome-Industries/metronome-python/commit/2ec6978638a39021730ba22005b237d19d56910e))
* internal: releasing x-mint ([8c6b031](https://github.com/Metronome-Industries/metronome-python/commit/8c6b031c7d5c725d94f99090100d07fa26e7f72c))
* internal(docs): adding confluent endpoints ([abc0b8a](https://github.com/Metronome-Industries/metronome-python/commit/abc0b8abb4b13b6d176dd4e390b576f2e21dbf17))
* LAUNCH-516 add getSubscriptionSeatsScheduleHistory api ([3ca576c](https://github.com/Metronome-Industries/metronome-python/commit/3ca576c1bf9ae91f17d33cfb82b0f6df9e89b67d))
* rename getSubscriptionSeatsScheduleHistory to getSubscriptionSeatsHistory ([7a864da](https://github.com/Metronome-Industries/metronome-python/commit/7a864da4de117c9ac41be1118e1cc62e561a395b))
* Return array of invoices instead of single invoice and handle multipl… ([be3eb83](https://github.com/Metronome-Industries/metronome-python/commit/be3eb83e8f745cd14d4d227fcfb5b29226820d7c))
* Set up contract get and create with new AH info ([08124e6](https://github.com/Metronome-Industries/metronome-python/commit/08124e6e71fefb61646fb7bbaebcb183f1571c99))


### Bug Fixes

* **api:** in getEditHistory endpoint, commit invoice schedule amount, unit price, and quantity are now optional values ([fa178d7](https://github.com/Metronome-Industries/metronome-python/commit/fa178d7663db6c22cbd12698bc307d7b37458ab0))
* LAUNCH-1130 remove min and max in api spec for better valiation error message ([5987fcd](https://github.com/Metronome-Industries/metronome-python/commit/5987fcd4e741c5ed58a4dd84e7544ccb115051d7))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([3bc0f53](https://github.com/Metronome-Industries/metronome-python/commit/3bc0f532cdcfd1954dcd63996ae8705696f45919))
* **internal:** detect missing future annotations with ruff ([4e3eb7d](https://github.com/Metronome-Industries/metronome-python/commit/4e3eb7dc22aa9600e4a159c181a7ab50e1a71dbb))
* **internal:** update pydantic dependency ([41ac59b](https://github.com/Metronome-Industries/metronome-python/commit/41ac59bd882237b2a21f01ab4e1d4597ae827e73))
* **types:** change optional parameter type from NotGiven to Omit ([28b9d7e](https://github.com/Metronome-Industries/metronome-python/commit/28b9d7ef99043bbe59857431404ff4b27a7dc27e))

## 1.0.0 (2025-09-15)

Full Changelog: [v0.3.0...v1.0.0](https://github.com/Metronome-Industries/metronome-python/compare/v0.3.0...v1.0.0)

### ⚠ BREAKING CHANGES

* **api:** add pagination support to multiple endpoints - Added pagination to CustomerList, AlertList, InvoiceList, CommitList, CreditList, CreditGrantList, CustomerAlerts, UsageList, CustomFields list, and ContractListBalances endpoints.
* **api:** enhance subscriptions and commits/credits - Added Individual enum to SubscriptionConfig and rate_type enums to UpdateCredit/UpdateCommit.
* **api:** add comprehensive shared types to SDK - Added 34 new shared types including BaseThresholdCommit, BaseUsageFilter, Commit, CommitHierarchyConfiguration, CommitRate, CommitSpecifier, CommitSpecifierInput, Contract, ContractV2, ContractWithoutAmendments, Credit, CreditTypeData, Discount, EventTypeFilter, HierarchyConfiguration, ID, Override, OverrideTier, OverwriteRate, PaymentGateConfig, PaymentGateConfigV2, PrepaidBalanceThresholdConfiguration, PrepaidBalanceThresholdConfigurationV2, PropertyFilter, ProService, Rate, RecurringCommitSubscriptionConfig, ScheduledCharge, ScheduleDuration, SchedulePointInTime, SpendThresholdConfiguration, SpendThresholdConfigurationV2, Subscription, Tier, and UpdateBaseThresholdCommit.

### Features

* **api:** add archived_at field to CustomerBillingConfiguration ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))
* **api:** add comprehensive shared types to SDK - Added 34 new shared types including BaseThresholdCommit, BaseUsageFilter, Commit, CommitHierarchyConfiguration, CommitRate, CommitSpecifier, CommitSpecifierInput, Contract, ContractV2, ContractWithoutAmendments, Credit, CreditTypeData, Discount, EventTypeFilter, HierarchyConfiguration, ID, Override, OverrideTier, OverwriteRate, PaymentGateConfig, PaymentGateConfigV2, PrepaidBalanceThresholdConfiguration, PrepaidBalanceThresholdConfigurationV2, PropertyFilter, ProService, Rate, RecurringCommitSubscriptionConfig, ScheduledCharge, ScheduleDuration, SchedulePointInTime, SpendThresholdConfiguration, SpendThresholdConfigurationV2, Subscription, Tier, and UpdateBaseThresholdCommit. ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))
* **api:** add created_at field to Commit ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))
* **api:** add customer billing configuration endpoints - Added set and retrieve endpoints for customer billing configurations. ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))
* **api:** add pagination support to multiple endpoints - Added pagination to CustomerList, AlertList, InvoiceList, CommitList, CreditList, CreditGrantList, CustomerAlerts, UsageList, CustomFields list, and ContractListBalances endpoints. ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))
* **api:** Add support for granular spend threshold alerts with group key filters. ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))
* **api:** enhance subscriptions and commits/credits - Added Individual enum to SubscriptionConfig and rate_type enums to UpdateCredit/UpdateCommit. ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))


### Bug Fixes

* avoid newer type syntax ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))


### Chores

* revert changelog changes ([fb55732](https://github.com/Metronome-Industries/metronome-python/commit/fb55732fdf57c9cf900100a8457d4edb0f2661da))
* revert version bump ([89ff28c](https://github.com/Metronome-Industries/metronome-python/commit/89ff28cc4e5ef3f5daa29ef3a92aeca7f2f5d9f9))


### Documentation

* enhance API documentation - Added more detailed descriptions and styling improvements, and enhanced usage filter documentation with additional context. ([7f5fbab](https://github.com/Metronome-Industries/metronome-python/commit/7f5fbab6c8e949c7904ae27665a8e6c35153016b))

## 0.3.0 (2025-08-15)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/Metronome-Industries/metronome-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([000db75](https://github.com/Metronome-Industries/metronome-python/commit/000db75b4cbe7b76821fd298464de9ce31428d19))
* **api:** api update ([d3928f1](https://github.com/Metronome-Industries/metronome-python/commit/d3928f186cf1ea71c2db49fa4bc2c6ed21983518))
* **api:** api update ([adeb2a3](https://github.com/Metronome-Industries/metronome-python/commit/adeb2a33754c069bfac5a290fba749cb1f4220d1))
* **api:** api update ([3882ef7](https://github.com/Metronome-Industries/metronome-python/commit/3882ef73128f7a7cef3cfe53e27387340eecb11f))
* **api:** api update ([9f2846a](https://github.com/Metronome-Industries/metronome-python/commit/9f2846aff07a11ebb35418a0334256be839c3c2d))
* **api:** api update ([059bfe4](https://github.com/Metronome-Industries/metronome-python/commit/059bfe43d5308a2542d07e3d699ea2c1897d634b))
* **api:** api update ([7abb045](https://github.com/Metronome-Industries/metronome-python/commit/7abb0457942e3cd7a50f78109a7ef56be51938c3))
* **api:** api update ([9cb1463](https://github.com/Metronome-Industries/metronome-python/commit/9cb1463be13df569e5139e1a5fb4f7156805c47b))
* **api:** api update ([97c20fc](https://github.com/Metronome-Industries/metronome-python/commit/97c20fc49e86d7b17a8fe382923f4c0f7b17af29))
* **api:** api update ([48549d0](https://github.com/Metronome-Industries/metronome-python/commit/48549d0c3f8a9609a9245862f9a42e9556a11a7c))
* **api:** api update ([df90b39](https://github.com/Metronome-Industries/metronome-python/commit/df90b392fa589f812083f531048ce356dd53a9ee))


### Chores

* **internal:** fix ruff target version ([bd52fdd](https://github.com/Metronome-Industries/metronome-python/commit/bd52fddb684a7b10aff1d8b6c70ec12aa9ecebe2))
* **internal:** update comment in script ([585d1a1](https://github.com/Metronome-Industries/metronome-python/commit/585d1a10491743753124ff7810a183128063b3d8))
* update @stainless-api/prism-cli to v5.15.0 ([1d7e80f](https://github.com/Metronome-Industries/metronome-python/commit/1d7e80f4d3818a8a5e973a2a1847bd98257d98e4))

## 0.2.0 (2025-07-30)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0...v0.2.0)

### Features
* **api:** Add support for spend threshold alerts for specific group keys. See [updated alert documentation](https://docs.metronome.com/manage-product-access/create-manage-alerts/#spend-alerts).
* **api:** Add support for recurring commits linked to subscriptions. See documentation for [hybrid billing models](https://docs.metronome.com/launch-guides/hybrid-business/#implement-a-hybrid-model-for-a-customer).
* **api:** Add support for new styles in embeddable dashboards.
* **api:** Add reference to contract on commit objects.

### Chores

* **docs:** Improved documentation.

## 0.1.0 (2025-07-24)

Full Changelog: [v0.1.0-beta.10...v0.1.0](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.10...v0.1.0)

### Features

* **api:** Allow for Pagination past empty pages ([6125dac](https://github.com/Metronome-Industries/metronome-python/commit/6125dac096d7047556558ef1c0679ddf5325c71a))
* **api:** api update ([8c6ee39](https://github.com/Metronome-Industries/metronome-python/commit/8c6ee3958588bff07360058c37cae3cc0cd4061e))
* **api:** api update ([ba09495](https://github.com/Metronome-Industries/metronome-python/commit/ba09495d05aa90e64844a52fc7ed7c790033df54))
* **api:** api update ([9fba59d](https://github.com/Metronome-Industries/metronome-python/commit/9fba59d5d9e1195198efb1016bfafccfda155bfc))
* **api:** api update ([547e91e](https://github.com/Metronome-Industries/metronome-python/commit/547e91e47b4116f9015df00ba2d708faf5c7278f))


### Bug Fixes

* **parsing:** parse extra field types ([6f30f29](https://github.com/Metronome-Industries/metronome-python/commit/6f30f296f158d68530a0ed0bbdbf52a3cdae9159))


### Chores

* **project:** add settings file for vscode ([41f1b0a](https://github.com/Metronome-Industries/metronome-python/commit/41f1b0ae3457b89f6dfeb2a471698324e65ffc35))

## 0.1.0-beta.10 (2025-07-21)

Full Changelog: [v0.1.0-beta.9...v0.1.0-beta.10](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.9...v0.1.0-beta.10)

### Features

* **api:** Add Event Search API for finding events to match to customers and billable metrics ([9b27405](https://github.com/Metronome-Industries/metronome-python/commit/9b27405b9fb62810baefb241cccc4a7ed9315116))
* **api:** add previewEvents API for generating draft invoices with provided events ([c055fa9](https://github.com/Metronome-Industries/metronome-python/commit/c055fa990129a42da17d3e38ad7811b524c8e87a))
* **api:** add support for Anrok and Precalculated tax types in payment gateway configuration ([c85c47d](https://github.com/Metronome-Industries/metronome-python/commit/c85c47d909a47309d431dd25bdf1e2e5ba93049b))
* **api:** add custom credit type support to prepaid balance thresholds ([e5be3f5](https://github.com/Metronome-Industries/metronome-python/commit/e5be3f565a51232aacc572e82cb13fbbaf36117b))
* **api:** add contract priority field ([19bdcb7](https://github.com/Metronome-Industries/metronome-python/commit/19bdcb72cf94b067b04d09df946d6786357380a7))
* **api:** remove previewEvents API ([5a8950b](https://github.com/Metronome-Industries/metronome-python/commit/5a8950b9128a9b0123d371ce41965815d0217638))
* **api:** add contract name update functionality to v2 contracts ([a2d49b4](https://github.com/Metronome-Industries/metronome-python/commit/a2d49b44541f6ffe1287b337a1e15d610fda44c0))
* **api:** add hierarchy configuration to v1 contracts ([8ef7f4f](https://github.com/Metronome-Industries/metronome-python/commit/8ef7f4f614e1fa9fd9335a94b27314028a6d48ac))
* **api:** add hierarchy configuration to v2 contracts ([d155aad](https://github.com/Metronome-Industries/metronome-python/commit/d155aad46141751d70bf4c5f956327419f0bc7dd))
* **api:** add contract hierarchy configuration to shared types ([2579d74](https://github.com/Metronome-Industries/metronome-python/commit/2579d74bae1f0cd4cee6ec2335b9c5a71fdbab4e))
* **api:** add sort parameter to credit grant list entries API ([3564f52](https://github.com/Metronome-Industries/metronome-python/commit/3564f526944329716f1503f26b7be6e665ab2917))
* **api:** api update ([eaca7c5](https://github.com/Metronome-Industries/metronome-python/commit/eaca7c57b0d332fd54dfa12189ae43be6612fa4d))
* **api:** api update ([2163f6a](https://github.com/Metronome-Industries/metronome-python/commit/2163f6afbc57f6f9ab4a255190f9ae978ceb63ef))
* **api:** api update ([c6e1932](https://github.com/Metronome-Industries/metronome-python/commit/c6e1932f3d4d04c0eefb3d759da5031303319a34))
* **api:** api update ([285bb4b](https://github.com/Metronome-Industries/metronome-python/commit/285bb4b2ea59ad4c5f31edad295605e725490ab1))
* **api:** api update ([908cddd](https://github.com/Metronome-Industries/metronome-python/commit/908cddd68c0e5397061948cfa09a8d9b6b6ca62c))

### Bug Fixes

* **ci:** correct conditional ([6aa265b](https://github.com/Metronome-Industries/metronome-python/commit/6aa265bd6b91d2184c256d5099263e1d8e8f9011))
* **ci:** release-doctor — report correct token name ([c513faf](https://github.com/Metronome-Industries/metronome-python/commit/c513faf443bf500285e4e763c84f74f9225d1da7))
* **client:** correctly parse binary response | stream ([30fb991](https://github.com/Metronome-Industries/metronome-python/commit/30fb991418019272b5719e68bc94fe10e241a411))
* **client:** don't send Content-Type header on GET requests ([b9837d7](https://github.com/Metronome-Industries/metronome-python/commit/b9837d71f5c500b3f2e43da07ee4bbc0e4ae644b))
* **parsing:** correctly handle nested discriminated unions ([b4c9cd4](https://github.com/Metronome-Industries/metronome-python/commit/b4c9cd425e4b3490efd4edbe94ebad66bdf0a08b))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([9d3de0c](https://github.com/Metronome-Industries/metronome-python/commit/9d3de0c0da730adf9085f91425a341717efc7c6d))


### Chores

* **ci:** change upload type ([63fd7db](https://github.com/Metronome-Industries/metronome-python/commit/63fd7dbce912e2b37ef6f498cbd16ed333db8a83))
* **ci:** enable for pull requests ([b1b5781](https://github.com/Metronome-Industries/metronome-python/commit/b1b5781cff9902ee5aa0ee54b70163403fc98e7e))
* **ci:** only run for pushes and fork pull requests ([9a18b0f](https://github.com/Metronome-Industries/metronome-python/commit/9a18b0f504e8b393c73e5959edfd1d80f2b86d12))
* **docs:** remove reference to rye shell ([ad4d425](https://github.com/Metronome-Industries/metronome-python/commit/ad4d425fdb206451bdebfba56f14f06db010f9f0))
* **docs:** remove unnecessary param examples ([52c671a](https://github.com/Metronome-Industries/metronome-python/commit/52c671a3b8859d512358f12cf9427a86d3024425))
* **internal:** bump pinned h11 dep ([9d639c5](https://github.com/Metronome-Industries/metronome-python/commit/9d639c5aac9d7795fd4e76a1be1c4dd57af547df))
* **internal:** update conftest.py ([8f6de39](https://github.com/Metronome-Industries/metronome-python/commit/8f6de39968c5df64728156726bc43906cb01753c))
* **package:** mark python 3.13 as supported ([fcb8743](https://github.com/Metronome-Industries/metronome-python/commit/fcb87431b4f00c1af8394265dbc0926ec1ee6406))
* **readme:** fix version rendering on pypi ([272e07c](https://github.com/Metronome-Industries/metronome-python/commit/272e07cbbf215ffea5e88ee31522e8550861285b))
* **readme:** update badges ([9082dfa](https://github.com/Metronome-Industries/metronome-python/commit/9082dfa601fa5cdfa7c9b2503329edbca6450b52))
* **tests:** add tests for httpx client instantiation & proxies ([d45d617](https://github.com/Metronome-Industries/metronome-python/commit/d45d617056a6cf140c61b942639e4eb50ddcaa24))
* **tests:** run tests in parallel ([1133ea9](https://github.com/Metronome-Industries/metronome-python/commit/1133ea98e20bbcc06e6aed2aa74d4692388e825c))
* **tests:** skip some failing tests on the latest python versions ([78320cd](https://github.com/Metronome-Industries/metronome-python/commit/78320cddaf394b52b8e0caca78319eb3e27d38ae))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([d9bf14d](https://github.com/Metronome-Industries/metronome-python/commit/d9bf14d25a6e69e3ce3e063d157152f1cc7f8d0d))

## 0.1.0-beta.9 (2025-05-30)

Full Changelog: [v0.1.0-beta.8...v0.1.0-beta.9](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.8...v0.1.0-beta.9)

### Features

* **api:** add subscription quantity history endpoint ([0aff6fb](https://github.com/Metronome-Industries/metronome-python/commit/0aff6fb4b54c349e03e5cd9e92ceab5320339895))
* **api:** api update ([fd41393](https://github.com/Metronome-Industries/metronome-python/commit/fd413935dcb6ecd175605982f2fec3e27479b157))
* **api:** api update ([3046ce2](https://github.com/Metronome-Industries/metronome-python/commit/3046ce2fed13706294644dfb624a14002e6e7eed))
* **api:** api update ([8bfddc5](https://github.com/Metronome-Industries/metronome-python/commit/8bfddc52087bdb17f31299e072f96b9ff28a0bc0))
* **api:** api update ([9be044e](https://github.com/Metronome-Industries/metronome-python/commit/9be044e897b5d84a76965891d0e462abc995728e))
* **api:** api update ([402f778](https://github.com/Metronome-Industries/metronome-python/commit/402f77874c0e41a8807bc332516407531f4bcf3d))
* **api:** api update ([3a93a05](https://github.com/Metronome-Industries/metronome-python/commit/3a93a057c20bf5fed2cf1ce7c7ecf661a691a4ae))
* **api:** api update ([41b3e5c](https://github.com/Metronome-Industries/metronome-python/commit/41b3e5c6649d4165a3a0af933b42d7949bc28822))
* **api:** api update ([e10e81c](https://github.com/Metronome-Industries/metronome-python/commit/e10e81cc9840904c608128473a6ae8ff36c3103e))
* **api:** api update ([8ca1842](https://github.com/Metronome-Industries/metronome-python/commit/8ca18428d24888a81d0c0454cbaf971c46b17ae9))
* **api:** api update ([38b3ea8](https://github.com/Metronome-Industries/metronome-python/commit/38b3ea828e3d2f7e63075a3151903e6550f36c90))
* **api:** api update ([a30e1ef](https://github.com/Metronome-Industries/metronome-python/commit/a30e1eff6ccbc13f31baa56d9e5ac2e4ad63a1f2))
* **api:** rename get subscription quantity history to retrieve ([48abe1b](https://github.com/Metronome-Industries/metronome-python/commit/48abe1b9a5fcbc0dd93743059a1fa892b2c1dd03))


### Chores

* **ci:** fix installation instructions ([2632526](https://github.com/Metronome-Industries/metronome-python/commit/263252635cac2eee3d250bba87bc1c4455e15b03))
* **ci:** upload sdks to package manager ([bfcf037](https://github.com/Metronome-Industries/metronome-python/commit/bfcf0377811a96a7d2f8ca74f743a0fb75909a3f))
* **ci:** use --pre flag for prerelease installation instructions ([f043a72](https://github.com/Metronome-Industries/metronome-python/commit/f043a72250275647b0522767dcbdf38d62057211))
* **ci:** use --pre flag for prerelease installation instructions ([1a8388a](https://github.com/Metronome-Industries/metronome-python/commit/1a8388ae25570bcec94274e5867867d611a136b3))
* configure new SDK language ([5809492](https://github.com/Metronome-Industries/metronome-python/commit/5809492e9786e5e0d7f1d51f262e76fce97404b4))
* **docs:** grammar improvements ([d7c697d](https://github.com/Metronome-Industries/metronome-python/commit/d7c697d72fc08f18f401b7f49362588f556148bf))

## 0.1.0-beta.8 (2025-05-14)

Full Changelog: [v0.1.0-beta.7...v0.1.0-beta.8](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.7...v0.1.0-beta.8)

### Features

* **api:** api update ([610ee19](https://github.com/Metronome-Industries/metronome-python/commit/610ee195e7a8a9fd185667678096ab69350cc1b4))
* **api:** api update ([d3d975d](https://github.com/Metronome-Industries/metronome-python/commit/d3d975d4ebde46a697bf2512124ad9ced661de03))
* **api:** api update ([8d7f6cb](https://github.com/Metronome-Industries/metronome-python/commit/8d7f6cb0859c159c2e56aad4e806af95e49449fb))
* **api:** api update ([116329e](https://github.com/Metronome-Industries/metronome-python/commit/116329e9a1e036a694af3f03323a347819342e6c))
* **api:** api update ([b6cf2e5](https://github.com/Metronome-Industries/metronome-python/commit/b6cf2e5f85629033600116a6010634f9b7a6bb04))
* **api:** api update ([0860297](https://github.com/Metronome-Industries/metronome-python/commit/0860297a36f2c1813914668a475e9dfd6b6befdf))
* **api:** api update ([86a7b4e](https://github.com/Metronome-Industries/metronome-python/commit/86a7b4ea16d41e6b43692d305d6f9c3e7690b3d5))
* **api:** api update ([2326250](https://github.com/Metronome-Industries/metronome-python/commit/2326250c05bda7cc253c71360ff1b04a7e28c97f))
* **api:** api update ([0528c47](https://github.com/Metronome-Industries/metronome-python/commit/0528c474a2dba9ed62cc7267c4c9f954ed2746a4))
* **api:** api update ([50e56b8](https://github.com/Metronome-Industries/metronome-python/commit/50e56b81200bb115bd47cece25d148c40edc5e90))
* **api:** api update ([a48822a](https://github.com/Metronome-Industries/metronome-python/commit/a48822ab2841bf1ae31a861fc732eb6a4530354a))
* **api:** api update ([79e49fd](https://github.com/Metronome-Industries/metronome-python/commit/79e49fd2281b48ae4ef4a577fb58a53d0d76d7f7))
* **api:** api update ([fe12dfc](https://github.com/Metronome-Industries/metronome-python/commit/fe12dfc4934e22032cd02117a4e043bd0468d66c))
* **api:** api update ([c49c5de](https://github.com/Metronome-Industries/metronome-python/commit/c49c5de45dd29691d81865f7776c569d7f744197))
* **api:** api update ([2f3bd5b](https://github.com/Metronome-Industries/metronome-python/commit/2f3bd5bafd8b852899883c6c3d202e64b2be3af4))
* **api:** api update ([cd7f6ab](https://github.com/Metronome-Industries/metronome-python/commit/cd7f6abc3f27d826116d3c8fd81b5038b3c0faa1))
* **api:** api update ([cffc65a](https://github.com/Metronome-Industries/metronome-python/commit/cffc65a2bc884bf4f86c694e4d846626ee1a6cb3))
* **api:** api update ([7302e94](https://github.com/Metronome-Industries/metronome-python/commit/7302e945a0ed66548f5f50be1cf01535cdd1a51e))
* **api:** api update ([990908b](https://github.com/Metronome-Industries/metronome-python/commit/990908b363d612244d5d26d1482514476844ecad))
* **api:** api update ([1ce021f](https://github.com/Metronome-Industries/metronome-python/commit/1ce021f4b720b57bab2bcd769e2576712cf28487))
* **api:** api update ([40c54a1](https://github.com/Metronome-Industries/metronome-python/commit/40c54a1cc596017735beacaabb487b5bf29efe4b))
* **api:** api update ([2f1b17e](https://github.com/Metronome-Industries/metronome-python/commit/2f1b17e7380747f7460eab1f0e888d7eb71198c3))
* **api:** api update ([7ce64ef](https://github.com/Metronome-Industries/metronome-python/commit/7ce64efa5ebefb6da3344284fe5d657b8c4b943c))
* **api:** api update ([edeb0ac](https://github.com/Metronome-Industries/metronome-python/commit/edeb0acccf41b276b8fccc705e823be28a210ffe))
* **api:** api update ([9b2bf32](https://github.com/Metronome-Industries/metronome-python/commit/9b2bf3257fadde9abb40a1bc4b97f0bd20572b1b))
* **api:** api update ([9ed8dbd](https://github.com/Metronome-Industries/metronome-python/commit/9ed8dbda090cfe775f4fe1cc67b9833fe05d30e3))
* **api:** api update ([3a1453b](https://github.com/Metronome-Industries/metronome-python/commit/3a1453bc06224c8aca93128118d4faed1fbccf03))
* **api:** api update ([385ce51](https://github.com/Metronome-Industries/metronome-python/commit/385ce51e272c8677376f51ca4d907c2f8b4b5a3c))
* **api:** api update ([#228](https://github.com/Metronome-Industries/metronome-python/issues/228)) ([d801c0a](https://github.com/Metronome-Industries/metronome-python/commit/d801c0aec2faa8121dbde95976fa62c4219313cb))
* **api:** api update ([#229](https://github.com/Metronome-Industries/metronome-python/issues/229)) ([4798ffc](https://github.com/Metronome-Industries/metronome-python/commit/4798ffcb8249b59d55f88e838ce302a4368b6672))
* **api:** api update ([#230](https://github.com/Metronome-Industries/metronome-python/issues/230)) ([df64884](https://github.com/Metronome-Industries/metronome-python/commit/df648845ce28065b3bb5bcb95a2e79dcaa9b7f52))
* **api:** api update ([#231](https://github.com/Metronome-Industries/metronome-python/issues/231)) ([a805f0f](https://github.com/Metronome-Industries/metronome-python/commit/a805f0f8f995b64dade952b45a60de611145d182))
* **api:** api update ([#232](https://github.com/Metronome-Industries/metronome-python/issues/232)) ([6bed0ca](https://github.com/Metronome-Industries/metronome-python/commit/6bed0cafe4e1b3509d0e8aac0d750a75b5bdc379))
* **api:** api update ([#234](https://github.com/Metronome-Industries/metronome-python/issues/234)) ([df25d2b](https://github.com/Metronome-Industries/metronome-python/commit/df25d2b01f4ac71c9e0f4f1ce76ca23425847f1d))
* **api:** api update ([#235](https://github.com/Metronome-Industries/metronome-python/issues/235)) ([645f9ce](https://github.com/Metronome-Industries/metronome-python/commit/645f9cec4cda934bb1625c3a91b5497dbf0a2ae2))
* **api:** api update ([#237](https://github.com/Metronome-Industries/metronome-python/issues/237)) ([188234f](https://github.com/Metronome-Industries/metronome-python/commit/188234f4f255d9ed1515671f78d175d3524ebc2f))


### Bug Fixes

* **package:** support direct resource imports ([0c48f7f](https://github.com/Metronome-Industries/metronome-python/commit/0c48f7fd8a24c226aef50a30103f74adc33f5b37))
* **perf:** optimize some hot paths ([a7bdeb7](https://github.com/Metronome-Industries/metronome-python/commit/a7bdeb7f6912dd65fb563f46e030a33bbb87181b))
* **perf:** skip traversing types for NotGiven values ([38728e0](https://github.com/Metronome-Industries/metronome-python/commit/38728e04a8823902142e87ca129899947fe8e33d))
* **pydantic v1:** more robust ModelField.annotation check ([97cb73b](https://github.com/Metronome-Industries/metronome-python/commit/97cb73ba56f871ee0e5b48b30599633fc2a77145))


### Chores

* add hash of OpenAPI spec/config inputs to .stats.yml ([6fd85a0](https://github.com/Metronome-Industries/metronome-python/commit/6fd85a030be63ea99a2d305670f2ad79b812dff2))
* broadly detect json family of content-type headers ([b187f49](https://github.com/Metronome-Industries/metronome-python/commit/b187f49d525e318d656fd8bc393f22d77a41575c))
* **ci:** add timeout thresholds for CI jobs ([5432c51](https://github.com/Metronome-Industries/metronome-python/commit/5432c511c33a90b6087c365f5b5cffe83a4f2f23))
* **ci:** only use depot for staging repos ([e5e0db2](https://github.com/Metronome-Industries/metronome-python/commit/e5e0db2577b5b35b9f0ff55484dd7e1b549f68a2))
* **ci:** run on more branches and use depot runners ([2e125c3](https://github.com/Metronome-Industries/metronome-python/commit/2e125c340c58c1d7e00d92677b3744ae14edb738))
* **client:** minor internal fixes ([7faf5a3](https://github.com/Metronome-Industries/metronome-python/commit/7faf5a30a955fecbbc5ab97b8088b4809414b437))
* fix typos ([#226](https://github.com/Metronome-Industries/metronome-python/issues/226)) ([4b2e083](https://github.com/Metronome-Industries/metronome-python/commit/4b2e083adc82e1777419ad0837d34fe74ba70f44))
* **internal:** avoid errors for isinstance checks on proxies ([72b6ede](https://github.com/Metronome-Industries/metronome-python/commit/72b6edef57883cc7b29e0ce521a991003c432cb0))
* **internal:** base client updates ([04d03fa](https://github.com/Metronome-Industries/metronome-python/commit/04d03fa0fcd33e3d802081527b9ca6db84d43e77))
* **internal:** bump pyright version ([98a0503](https://github.com/Metronome-Industries/metronome-python/commit/98a05035941c4daf560609560bf76a945aa87707))
* **internal:** codegen related update ([15ca42f](https://github.com/Metronome-Industries/metronome-python/commit/15ca42f1ad1a331e41b342bd63ade6573558e921))
* **internal:** expand CI branch coverage ([#240](https://github.com/Metronome-Industries/metronome-python/issues/240)) ([c87b106](https://github.com/Metronome-Industries/metronome-python/commit/c87b106d1265fc3e54595c09b324630bb5b41a02))
* **internal:** fix list file params ([b4a5f21](https://github.com/Metronome-Industries/metronome-python/commit/b4a5f21ed1cde315a7332d34eacfe39088ddc861))
* **internal:** import reformatting ([122579a](https://github.com/Metronome-Industries/metronome-python/commit/122579a5d902d0d8e4f555f56dbbf2b2d5cdcb85))
* **internal:** minor formatting changes ([50bfdb1](https://github.com/Metronome-Industries/metronome-python/commit/50bfdb173d1702c3208fabd78654b70e80d32fa2))
* **internal:** reduce CI branch coverage ([2fe4d4d](https://github.com/Metronome-Industries/metronome-python/commit/2fe4d4de4b503a9071b691d646511c6485aac0ca))
* **internal:** refactor retries to not use recursion ([694527a](https://github.com/Metronome-Industries/metronome-python/commit/694527ad898ac8ff37784ac58c00ad6157d53230))
* **internal:** remove trailing character ([#233](https://github.com/Metronome-Industries/metronome-python/issues/233)) ([6a92eca](https://github.com/Metronome-Industries/metronome-python/commit/6a92ecaa7e684b8f13df4b4dfd50be670a44128f))
* **internal:** slight transform perf improvement ([#238](https://github.com/Metronome-Industries/metronome-python/issues/238)) ([ae468b0](https://github.com/Metronome-Industries/metronome-python/commit/ae468b00b306a32ac8bd9b33c9031188c5e44816))
* **internal:** update models test ([e3654f0](https://github.com/Metronome-Industries/metronome-python/commit/e3654f02d5fd68425fcfd013368d5019c77c867b))
* **internal:** update pyright settings ([54bc1f6](https://github.com/Metronome-Industries/metronome-python/commit/54bc1f6a2ead9b6abc02c8239e8a32d3282d38de))
* **tests:** improve enum examples ([#239](https://github.com/Metronome-Industries/metronome-python/issues/239)) ([8e18bf5](https://github.com/Metronome-Industries/metronome-python/commit/8e18bf5dc1c18654702669d8e858f7a1ded4fd59))


### Documentation

* remove private imports from datetime snippets ([59a71b3](https://github.com/Metronome-Industries/metronome-python/commit/59a71b36222422de381d96a312917504d88987e1))
* swap examples used in readme ([#236](https://github.com/Metronome-Industries/metronome-python/issues/236)) ([dfbdd9a](https://github.com/Metronome-Industries/metronome-python/commit/dfbdd9ad2d4493b4e229aa3203012e9f129150ea))

## 0.1.0-beta.7 (2025-03-25)

Full Changelog: [v0.1.0-beta.6...v0.1.0-beta.7](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.6...v0.1.0-beta.7)

### Features

* **api:** api update ([#188](https://github.com/Metronome-Industries/metronome-python/issues/188)) ([9bc534d](https://github.com/Metronome-Industries/metronome-python/commit/9bc534d337ac28774730efc42b2b2dc775c7d49c))
* **api:** api update ([#192](https://github.com/Metronome-Industries/metronome-python/issues/192)) ([d1ca147](https://github.com/Metronome-Industries/metronome-python/commit/d1ca147f6ce0d8333b0af9ae5cfff70f1cbd4971))
* **api:** api update ([#196](https://github.com/Metronome-Industries/metronome-python/issues/196)) ([9f22bd8](https://github.com/Metronome-Industries/metronome-python/commit/9f22bd8214945d1b67f44a7a3e87bad04ce724f1))
* **api:** api update ([#201](https://github.com/Metronome-Industries/metronome-python/issues/201)) ([e4d2ae1](https://github.com/Metronome-Industries/metronome-python/commit/e4d2ae18a08d77b86d48351a5dca4a71c7f1e6a8))
* **api:** api update ([#202](https://github.com/Metronome-Industries/metronome-python/issues/202)) ([e5f384e](https://github.com/Metronome-Industries/metronome-python/commit/e5f384e8e1680db9f2cf56896583254f7d85b3ff))
* **api:** api update ([#204](https://github.com/Metronome-Industries/metronome-python/issues/204)) ([9d2a0a6](https://github.com/Metronome-Industries/metronome-python/commit/9d2a0a6ddd7c18441e77a26c830ed0d798202995))
* **api:** api update ([#205](https://github.com/Metronome-Industries/metronome-python/issues/205)) ([820d02b](https://github.com/Metronome-Industries/metronome-python/commit/820d02bd4380615e27ef1880c2de0c110c8da4d0))
* **api:** api update ([#206](https://github.com/Metronome-Industries/metronome-python/issues/206)) ([6e707b6](https://github.com/Metronome-Industries/metronome-python/commit/6e707b690f806645aee4e7fc147b8ed590c2d0ba))
* **api:** api update ([#208](https://github.com/Metronome-Industries/metronome-python/issues/208)) ([2bb47cc](https://github.com/Metronome-Industries/metronome-python/commit/2bb47ccd231cccce18c5d9797ca3904b3e0f5bea))
* **api:** api update ([#210](https://github.com/Metronome-Industries/metronome-python/issues/210)) ([65f8161](https://github.com/Metronome-Industries/metronome-python/commit/65f81618115c0116334e2ccc15ad57e99b8529e4))
* **api:** api update ([#212](https://github.com/Metronome-Industries/metronome-python/issues/212)) ([a40e188](https://github.com/Metronome-Industries/metronome-python/commit/a40e18825ba44ee640db3c3b51ecaea124b667ca))
* **api:** api update ([#219](https://github.com/Metronome-Industries/metronome-python/issues/219)) ([9ae1df0](https://github.com/Metronome-Industries/metronome-python/commit/9ae1df0ef90eb31db7562639ed24143e9a785e69))
* **api:** api update ([#220](https://github.com/Metronome-Industries/metronome-python/issues/220)) ([3f60c24](https://github.com/Metronome-Industries/metronome-python/commit/3f60c2498d5f7edac41b852a9d67fcc5325ee99e))
* **api:** api update ([#221](https://github.com/Metronome-Industries/metronome-python/issues/221)) ([1eb013b](https://github.com/Metronome-Industries/metronome-python/commit/1eb013b7b6f59e49ec0b9b19e065ccc11d083184))
* **api:** api update ([#222](https://github.com/Metronome-Industries/metronome-python/issues/222)) ([32d7839](https://github.com/Metronome-Industries/metronome-python/commit/32d7839c6c5048f43dda400ad7589e9e314871f7))
* **api:** api update ([#223](https://github.com/Metronome-Industries/metronome-python/issues/223)) ([1b885e7](https://github.com/Metronome-Industries/metronome-python/commit/1b885e7877ad002ce53a239d8702d23d234a817d))
* **api:** manual updates ([#224](https://github.com/Metronome-Industries/metronome-python/issues/224)) ([3e5d2c7](https://github.com/Metronome-Industries/metronome-python/commit/3e5d2c763187d52c44a36fe78b8fbea571e43a57))
* **client:** allow passing `NotGiven` for body ([#194](https://github.com/Metronome-Industries/metronome-python/issues/194)) ([1ca4894](https://github.com/Metronome-Industries/metronome-python/commit/1ca489460616d62a669c754b3b5e432f976c2b47))


### Bug Fixes

* **ci:** ensure pip is always available ([#217](https://github.com/Metronome-Industries/metronome-python/issues/217)) ([2efccbf](https://github.com/Metronome-Industries/metronome-python/commit/2efccbf0fe1010643602732120d7e7d716adb506))
* **ci:** remove publishing patch ([#218](https://github.com/Metronome-Industries/metronome-python/issues/218)) ([5d82f90](https://github.com/Metronome-Industries/metronome-python/commit/5d82f9095091e037a9c1754175ce4c2f0d6334ab))
* **client:** mark some request bodies as optional ([1ca4894](https://github.com/Metronome-Industries/metronome-python/commit/1ca489460616d62a669c754b3b5e432f976c2b47))
* **types:** handle more discriminated union shapes ([#215](https://github.com/Metronome-Industries/metronome-python/issues/215)) ([4318222](https://github.com/Metronome-Industries/metronome-python/commit/4318222346e01af31238aabc790d9afa145e95b8))


### Chores

* **docs:** update client docstring ([#200](https://github.com/Metronome-Industries/metronome-python/issues/200)) ([7e2b853](https://github.com/Metronome-Industries/metronome-python/commit/7e2b8535ec8cf4a9aaf9e0fe93bb45a0cca372f5))
* **internal:** bump rye to 0.44.0 ([#213](https://github.com/Metronome-Industries/metronome-python/issues/213)) ([124c23b](https://github.com/Metronome-Industries/metronome-python/commit/124c23bbe2de26aa5dd794960d699c47bdd73837))
* **internal:** codegen related update ([2f2f974](https://github.com/Metronome-Industries/metronome-python/commit/2f2f9741680166c9d30912d8cbb24fdf3a3c3e41))
* **internal:** codegen related update ([562a480](https://github.com/Metronome-Industries/metronome-python/commit/562a48067994292885c5b036614b25caee574a47))
* **internal:** codegen related update ([#193](https://github.com/Metronome-Industries/metronome-python/issues/193)) ([47e7055](https://github.com/Metronome-Industries/metronome-python/commit/47e7055335b3171770fe1e7d0c0174162d32c462))
* **internal:** codegen related update ([#211](https://github.com/Metronome-Industries/metronome-python/issues/211)) ([f918315](https://github.com/Metronome-Industries/metronome-python/commit/f91831596e75c1b67a290bc45ece3d0f45a379a0))
* **internal:** codegen related update ([#214](https://github.com/Metronome-Industries/metronome-python/issues/214)) ([9045612](https://github.com/Metronome-Industries/metronome-python/commit/90456127530934fbe8edad40ba165cfaef374065))
* **internal:** codegen related update ([#216](https://github.com/Metronome-Industries/metronome-python/issues/216)) ([a734f09](https://github.com/Metronome-Industries/metronome-python/commit/a734f09a3cf81099b6573b172d85378c7945925f))
* **internal:** fix devcontainers setup ([#195](https://github.com/Metronome-Industries/metronome-python/issues/195)) ([f93005f](https://github.com/Metronome-Industries/metronome-python/commit/f93005fadf353d61aca9628cea89c8b17f42acc7))
* **internal:** properly set __pydantic_private__ ([#197](https://github.com/Metronome-Industries/metronome-python/issues/197)) ([681d4e4](https://github.com/Metronome-Industries/metronome-python/commit/681d4e49f62b39092918b448117ba85c764e963c))
* **internal:** remove extra empty newlines ([704f7f6](https://github.com/Metronome-Industries/metronome-python/commit/704f7f6f9e180486803214084173ec750e986eb8))
* **internal:** remove unused http client options forwarding ([#203](https://github.com/Metronome-Industries/metronome-python/issues/203)) ([49209b5](https://github.com/Metronome-Industries/metronome-python/commit/49209b59c21b81aeca1e6bce90aacbe89ed1c514))
* **internal:** update client tests ([#190](https://github.com/Metronome-Industries/metronome-python/issues/190)) ([8c5600a](https://github.com/Metronome-Industries/metronome-python/commit/8c5600a4d9847d19629aa02ec61ccddfc7ce6664))
* **tests:** add back parse_datetime calls to client tests ([ba6daec](https://github.com/Metronome-Industries/metronome-python/commit/ba6daecf18369ed5ee2ca8b01007d2d96cc0c772))


### Documentation

* revise readme docs about nested params ([#207](https://github.com/Metronome-Industries/metronome-python/issues/207)) ([1bd3187](https://github.com/Metronome-Industries/metronome-python/commit/1bd31875ee8be937d6e530a6e5b28118e2f1a2f9))
* update URLs from stainlessapi.com to stainless.com ([#198](https://github.com/Metronome-Industries/metronome-python/issues/198)) ([4dfe6e4](https://github.com/Metronome-Industries/metronome-python/commit/4dfe6e4da086c9fc7c90c9891c71460578ca015c))

## 0.1.0-beta.6 (2025-02-07)

Full Changelog: [v0.1.0-beta.5...v0.1.0-beta.6](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.5...v0.1.0-beta.6)

### Features

* **api:** api update ([#177](https://github.com/Metronome-Industries/metronome-python/issues/177)) ([c7434cc](https://github.com/Metronome-Industries/metronome-python/commit/c7434cc4c7ca1a9c209db010334bfae82bb9244b))
* **api:** api update ([#179](https://github.com/Metronome-Industries/metronome-python/issues/179)) ([ab2478d](https://github.com/Metronome-Industries/metronome-python/commit/ab2478d57cc45d70cf421b2242704a41da43e2e7))
* **api:** api update ([#182](https://github.com/Metronome-Industries/metronome-python/issues/182)) ([8b1e503](https://github.com/Metronome-Industries/metronome-python/commit/8b1e503a920271847a4c95e19e429ba5c8f56d37))
* **api:** api update ([#183](https://github.com/Metronome-Industries/metronome-python/issues/183)) ([e50b864](https://github.com/Metronome-Industries/metronome-python/commit/e50b864c29f5f3ad6e43736d9758ba7622daf32b))
* **api:** api update ([#184](https://github.com/Metronome-Industries/metronome-python/issues/184)) ([266e972](https://github.com/Metronome-Industries/metronome-python/commit/266e97238a4615749b1772fa87e48d1fab5672b3))
* **api:** api update ([#186](https://github.com/Metronome-Industries/metronome-python/issues/186)) ([8c6b475](https://github.com/Metronome-Industries/metronome-python/commit/8c6b475d6de889109ecedb9aa7c27fa37be1d3a0))


### Chores

* **internal:** bummp ruff dependency ([#181](https://github.com/Metronome-Industries/metronome-python/issues/181)) ([5267fcb](https://github.com/Metronome-Industries/metronome-python/commit/5267fcbebb782c069f835b7452e9e7a43152dfb1))
* **internal:** change default timeout to an int ([#180](https://github.com/Metronome-Industries/metronome-python/issues/180)) ([d9343b4](https://github.com/Metronome-Industries/metronome-python/commit/d9343b4b576fd0523eefe5671c3c3770a16fe614))
* **internal:** codegen related update ([#185](https://github.com/Metronome-Industries/metronome-python/issues/185)) ([c8027ab](https://github.com/Metronome-Industries/metronome-python/commit/c8027ab74e6a3c3b0518515046003d42f3e5cbd2))

## 0.1.0-beta.5 (2025-01-27)

Full Changelog: [v0.1.0-beta.4...v0.1.0-beta.5](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.4...v0.1.0-beta.5)

### Features

* **api:** api update ([#174](https://github.com/Metronome-Industries/metronome-python/issues/174)) ([6d2c460](https://github.com/Metronome-Industries/metronome-python/commit/6d2c460a815433f9b0a3b1fe5b0501e2dba1ee31))

## 0.1.0-beta.4 (2025-01-23)

Full Changelog: [v0.1.0-beta.3...v0.1.0-beta.4](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.3...v0.1.0-beta.4)

### Features

* **api:** api update ([#108](https://github.com/Metronome-Industries/metronome-python/issues/108)) ([a58c149](https://github.com/Metronome-Industries/metronome-python/commit/a58c14902c38e392eb61d690ab247edf42937f6e))
* **api:** api update ([#109](https://github.com/Metronome-Industries/metronome-python/issues/109)) ([9e781b0](https://github.com/Metronome-Industries/metronome-python/commit/9e781b0f90d0466f3c8a9d782cbfee5e3362b3aa))
* **api:** api update ([#111](https://github.com/Metronome-Industries/metronome-python/issues/111)) ([008bd54](https://github.com/Metronome-Industries/metronome-python/commit/008bd54b4708f25b2f8480bd7c2130cc51ee8668))
* **api:** api update ([#113](https://github.com/Metronome-Industries/metronome-python/issues/113)) ([0973898](https://github.com/Metronome-Industries/metronome-python/commit/0973898da971367fca4be616e04aaff423ea7539))
* **api:** api update ([#117](https://github.com/Metronome-Industries/metronome-python/issues/117)) ([28ed14a](https://github.com/Metronome-Industries/metronome-python/commit/28ed14ae3ab7d7454875a063af124631f7131119))
* **api:** api update ([#118](https://github.com/Metronome-Industries/metronome-python/issues/118)) ([35b2858](https://github.com/Metronome-Industries/metronome-python/commit/35b2858964a4f700e20d0043925397f3757fa5a7))
* **api:** api update ([#119](https://github.com/Metronome-Industries/metronome-python/issues/119)) ([2977ea1](https://github.com/Metronome-Industries/metronome-python/commit/2977ea1e20336adb46fa87601d7cd83d50ed43ff))
* **api:** api update ([#120](https://github.com/Metronome-Industries/metronome-python/issues/120)) ([6d70b65](https://github.com/Metronome-Industries/metronome-python/commit/6d70b6560c1c2b2e31adf7687feaf9cab7083cbc))
* **api:** api update ([#123](https://github.com/Metronome-Industries/metronome-python/issues/123)) ([6e879af](https://github.com/Metronome-Industries/metronome-python/commit/6e879af850dfbdc43fb59ff1d9aa3ff5fedaeee1))
* **api:** api update ([#124](https://github.com/Metronome-Industries/metronome-python/issues/124)) ([6b92d9c](https://github.com/Metronome-Industries/metronome-python/commit/6b92d9c56d728320405d6eea3890f93f72448d3a))
* **api:** api update ([#128](https://github.com/Metronome-Industries/metronome-python/issues/128)) ([c6a4123](https://github.com/Metronome-Industries/metronome-python/commit/c6a4123c5128c903849eeea47fe3719e9b42beda))
* **api:** api update ([#131](https://github.com/Metronome-Industries/metronome-python/issues/131)) ([bf0c16e](https://github.com/Metronome-Industries/metronome-python/commit/bf0c16e40b390f6ec12df70cc67113096afd3111))
* **api:** api update ([#136](https://github.com/Metronome-Industries/metronome-python/issues/136)) ([30f51ae](https://github.com/Metronome-Industries/metronome-python/commit/30f51ae371ea7d7c77cd2942683daa784f9e5ae5))
* **api:** api update ([#139](https://github.com/Metronome-Industries/metronome-python/issues/139)) ([6fcda79](https://github.com/Metronome-Industries/metronome-python/commit/6fcda792f14ef951f36f2c7009bbcfc8d3857406))
* **api:** api update ([#144](https://github.com/Metronome-Industries/metronome-python/issues/144)) ([63abf5d](https://github.com/Metronome-Industries/metronome-python/commit/63abf5d0af295024acbd0f31ac9fb1436927aefe))
* **api:** api update ([#147](https://github.com/Metronome-Industries/metronome-python/issues/147)) ([3690360](https://github.com/Metronome-Industries/metronome-python/commit/3690360f8f0201ada6eb14f055803bc9062b14d4))
* **api:** api update ([#148](https://github.com/Metronome-Industries/metronome-python/issues/148)) ([0e22565](https://github.com/Metronome-Industries/metronome-python/commit/0e22565a5ec0a1a08363806d88c684fe2ea50b64))
* **api:** api update ([#150](https://github.com/Metronome-Industries/metronome-python/issues/150)) ([d027800](https://github.com/Metronome-Industries/metronome-python/commit/d027800ccad33753d1d3fd1656580b461374318e))
* **api:** api update ([#156](https://github.com/Metronome-Industries/metronome-python/issues/156)) ([06e842b](https://github.com/Metronome-Industries/metronome-python/commit/06e842bd6424d166793697a18a0add5fbe4e7ee1))
* **api:** api update ([#157](https://github.com/Metronome-Industries/metronome-python/issues/157)) ([c185997](https://github.com/Metronome-Industries/metronome-python/commit/c1859971c8caf7626b511568349b836b617ec669))
* **api:** api update ([#158](https://github.com/Metronome-Industries/metronome-python/issues/158)) ([45e89f1](https://github.com/Metronome-Industries/metronome-python/commit/45e89f153886c808e7a39898eeb857e0f05bf287))
* **api:** api update ([#160](https://github.com/Metronome-Industries/metronome-python/issues/160)) ([368fd85](https://github.com/Metronome-Industries/metronome-python/commit/368fd855524a98debfd5098c818b0cc942b02749))
* **api:** api update ([#161](https://github.com/Metronome-Industries/metronome-python/issues/161)) ([109129d](https://github.com/Metronome-Industries/metronome-python/commit/109129d67fe3209dac24fcc4e8e15f17e6aca99e))
* **api:** api update ([#163](https://github.com/Metronome-Industries/metronome-python/issues/163)) ([f8eb0ab](https://github.com/Metronome-Industries/metronome-python/commit/f8eb0ab0944e08dbed06f18b12dd7c0bbdbbe9cb))
* **api:** api update ([#165](https://github.com/Metronome-Industries/metronome-python/issues/165)) ([3a868c4](https://github.com/Metronome-Industries/metronome-python/commit/3a868c4d502351e68a4da74286d8b3580a3ea86f))
* **api:** api update ([#166](https://github.com/Metronome-Industries/metronome-python/issues/166)) ([e7ca427](https://github.com/Metronome-Industries/metronome-python/commit/e7ca427b85a09c4ed735464bdfd2ae5f486c96f0))
* **api:** api update ([#171](https://github.com/Metronome-Industries/metronome-python/issues/171)) ([4389567](https://github.com/Metronome-Industries/metronome-python/commit/438956757ed829b38a44a6005b35772e0e695c42))
* **api:** OpenAPI spec update via Stainless API ([#100](https://github.com/Metronome-Industries/metronome-python/issues/100)) ([23e4233](https://github.com/Metronome-Industries/metronome-python/commit/23e4233bc784c861d75d774b0ad9b9093f604d18))
* **api:** OpenAPI spec update via Stainless API ([#105](https://github.com/Metronome-Industries/metronome-python/issues/105)) ([d53b0c0](https://github.com/Metronome-Industries/metronome-python/commit/d53b0c047bba46b022b98ab8617cb39d9aa8d4e5))
* **api:** OpenAPI spec update via Stainless API ([#97](https://github.com/Metronome-Industries/metronome-python/issues/97)) ([1b9edd9](https://github.com/Metronome-Industries/metronome-python/commit/1b9edd91340ad039cc9e0d20b0912bd25594b0e2))


### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#106](https://github.com/Metronome-Industries/metronome-python/issues/106)) ([465d868](https://github.com/Metronome-Industries/metronome-python/commit/465d86895931b326f9fec627df94e82b1b6800b4))
* **client:** compat with new httpx 0.28.0 release ([#133](https://github.com/Metronome-Industries/metronome-python/issues/133)) ([5d8b9cc](https://github.com/Metronome-Industries/metronome-python/commit/5d8b9cc2cb99a4c3245203183cbe486cd4ed447c))
* **client:** only call .close() when needed ([#153](https://github.com/Metronome-Industries/metronome-python/issues/153)) ([f8f67e6](https://github.com/Metronome-Industries/metronome-python/commit/f8f67e63c45836086260ff14d78e5547ce999f78))
* correctly handle deserialising `cls` fields ([#159](https://github.com/Metronome-Industries/metronome-python/issues/159)) ([b26b63b](https://github.com/Metronome-Industries/metronome-python/commit/b26b63bb4b49ea7da790bd8da800ca1be0c8cbf6))
* **tests:** make test_get_platform less flaky ([#168](https://github.com/Metronome-Industries/metronome-python/issues/168)) ([db126f2](https://github.com/Metronome-Industries/metronome-python/commit/db126f21197ee1e42462b86aa0a3a19f274b2564))


### Chores

* add missing isclass check ([#151](https://github.com/Metronome-Industries/metronome-python/issues/151)) ([e5fde7c](https://github.com/Metronome-Industries/metronome-python/commit/e5fde7c49a6da112c6a1b43b381bdbdf8b1b688c))
* add repr to PageInfo class ([#107](https://github.com/Metronome-Industries/metronome-python/issues/107)) ([8306ee7](https://github.com/Metronome-Industries/metronome-python/commit/8306ee749c394960eb57be7c6f41bf808f1612f7))
* **internal:** add support for parsing bool response content ([#104](https://github.com/Metronome-Industries/metronome-python/issues/104)) ([2253e61](https://github.com/Metronome-Industries/metronome-python/commit/2253e6118160b5a96f6fecb01afef46167524a07))
* **internal:** add support for TypeAliasType ([#141](https://github.com/Metronome-Industries/metronome-python/issues/141)) ([17c7ae6](https://github.com/Metronome-Industries/metronome-python/commit/17c7ae6e8af47a6e716e50f5c94b24ab4a890a7b))
* **internal:** avoid pytest-asyncio deprecation warning ([#169](https://github.com/Metronome-Industries/metronome-python/issues/169)) ([3136426](https://github.com/Metronome-Industries/metronome-python/commit/31364265a98eaa8eff463b6b533db3e2f57a13c5))
* **internal:** bump httpx dependency ([#152](https://github.com/Metronome-Industries/metronome-python/issues/152)) ([337146f](https://github.com/Metronome-Industries/metronome-python/commit/337146f18a3fb67099a876e39fc22704bd923665))
* **internal:** bump pydantic dependency ([#137](https://github.com/Metronome-Industries/metronome-python/issues/137)) ([a3d6204](https://github.com/Metronome-Industries/metronome-python/commit/a3d62042555f62a2fcdaca8bd9ab099649f24949))
* **internal:** bump pyright ([#134](https://github.com/Metronome-Industries/metronome-python/issues/134)) ([e313f0a](https://github.com/Metronome-Industries/metronome-python/commit/e313f0a5e6619457c0111c07a08fd57179ce0854))
* **internal:** bump pyright ([#140](https://github.com/Metronome-Industries/metronome-python/issues/140)) ([24f5bf0](https://github.com/Metronome-Industries/metronome-python/commit/24f5bf0075265818594feb0aa4f19f035e412e99))
* **internal:** bump pyright dependency ([#164](https://github.com/Metronome-Industries/metronome-python/issues/164)) ([6a2460f](https://github.com/Metronome-Industries/metronome-python/commit/6a2460f8097738059c33fde596d879566298e163))
* **internal:** codegen related update ([#101](https://github.com/Metronome-Industries/metronome-python/issues/101)) ([b946911](https://github.com/Metronome-Industries/metronome-python/commit/b946911194053715b04abf7e7b430c95e46a460c))
* **internal:** codegen related update ([#102](https://github.com/Metronome-Industries/metronome-python/issues/102)) ([9cbc145](https://github.com/Metronome-Industries/metronome-python/commit/9cbc145ec42ebefdfbca884ee98494ea70b8265b))
* **internal:** codegen related update ([#103](https://github.com/Metronome-Industries/metronome-python/issues/103)) ([2ed9f53](https://github.com/Metronome-Industries/metronome-python/commit/2ed9f539743b94821193900687ac15d85d9c5346))
* **internal:** codegen related update ([#149](https://github.com/Metronome-Industries/metronome-python/issues/149)) ([c30e9bf](https://github.com/Metronome-Industries/metronome-python/commit/c30e9bfb788a839943d3bc55dba69b139734bc98))
* **internal:** codegen related update ([#155](https://github.com/Metronome-Industries/metronome-python/issues/155)) ([bdfb2d0](https://github.com/Metronome-Industries/metronome-python/commit/bdfb2d005968b4890e1b31dd8e7666b95f907eee))
* **internal:** codegen related update ([#98](https://github.com/Metronome-Industries/metronome-python/issues/98)) ([b4b48c0](https://github.com/Metronome-Industries/metronome-python/commit/b4b48c0421234322967999892118c145c31900df))
* **internal:** exclude mypy from running on tests ([#132](https://github.com/Metronome-Industries/metronome-python/issues/132)) ([2917f6e](https://github.com/Metronome-Industries/metronome-python/commit/2917f6ee6b61ec96afc5942cc15f5b02b61d3ad6))
* **internal:** fix compat model_dump method when warnings are passed ([#127](https://github.com/Metronome-Industries/metronome-python/issues/127)) ([288a77f](https://github.com/Metronome-Industries/metronome-python/commit/288a77fb418850fd1564c1ca18bcc49a6e0751c8))
* **internal:** fix some typos ([#146](https://github.com/Metronome-Industries/metronome-python/issues/146)) ([7a35c26](https://github.com/Metronome-Industries/metronome-python/commit/7a35c2649bb9871c6bc2db71eb1dd8635490b075))
* **internal:** minor formatting changes ([#172](https://github.com/Metronome-Industries/metronome-python/issues/172)) ([986fa49](https://github.com/Metronome-Industries/metronome-python/commit/986fa496184c7f4b480ac5833e358e57f60a6f4c))
* **internal:** minor style changes ([#170](https://github.com/Metronome-Industries/metronome-python/issues/170)) ([20e89dc](https://github.com/Metronome-Industries/metronome-python/commit/20e89dcb8393c4b4e55fc61bed1bfe88beb9314d))
* **internal:** remove some duplicated imports ([#142](https://github.com/Metronome-Industries/metronome-python/issues/142)) ([3cf4086](https://github.com/Metronome-Industries/metronome-python/commit/3cf4086d362bab08fe31783a037dcf8f8d6a2608))
* **internal:** update deps ([#162](https://github.com/Metronome-Industries/metronome-python/issues/162)) ([db5dc45](https://github.com/Metronome-Industries/metronome-python/commit/db5dc45b2f2f9e4b71e00de08997fe6e09eda9e1))
* **internal:** updated imports ([#143](https://github.com/Metronome-Industries/metronome-python/issues/143)) ([29abf00](https://github.com/Metronome-Industries/metronome-python/commit/29abf005793a3702d235ec0aeeaeaf59dc1f7033))
* make the `Omit` type public ([#135](https://github.com/Metronome-Industries/metronome-python/issues/135)) ([85f1025](https://github.com/Metronome-Industries/metronome-python/commit/85f1025c763cb62930e618379f9b24e798200a7b))
* rebuild project due to codegen change ([#110](https://github.com/Metronome-Industries/metronome-python/issues/110)) ([5cb0771](https://github.com/Metronome-Industries/metronome-python/commit/5cb0771a536431651843c40e88b069e87b6408b2))
* rebuild project due to codegen change ([#112](https://github.com/Metronome-Industries/metronome-python/issues/112)) ([086bed0](https://github.com/Metronome-Industries/metronome-python/commit/086bed0b5ddc8e23b614be02abe0f9d73babbfda))
* rebuild project due to codegen change ([#114](https://github.com/Metronome-Industries/metronome-python/issues/114)) ([d142e14](https://github.com/Metronome-Industries/metronome-python/commit/d142e14313cefcd6e12a6a382e690eda42973629))
* rebuild project due to codegen change ([#115](https://github.com/Metronome-Industries/metronome-python/issues/115)) ([7b5ba26](https://github.com/Metronome-Industries/metronome-python/commit/7b5ba2664bab16fcd6ba7b82f67083d7bb8f7cd0))
* rebuild project due to codegen change ([#116](https://github.com/Metronome-Industries/metronome-python/issues/116)) ([c01f739](https://github.com/Metronome-Industries/metronome-python/commit/c01f739eb6730598b6386d424de1cdfb03f0d188))
* rebuild project due to codegen change ([#121](https://github.com/Metronome-Industries/metronome-python/issues/121)) ([f5da454](https://github.com/Metronome-Industries/metronome-python/commit/f5da4547cf574b22dfbfcf53edcde80a65c09e10))
* rebuild project due to codegen change ([#122](https://github.com/Metronome-Industries/metronome-python/issues/122)) ([1e76c7d](https://github.com/Metronome-Industries/metronome-python/commit/1e76c7db771e85d6b752f6b39de6e548c93fbf2b))
* rebuild project due to codegen change ([#125](https://github.com/Metronome-Industries/metronome-python/issues/125)) ([8ad959f](https://github.com/Metronome-Industries/metronome-python/commit/8ad959f010f90a4fc862fd1d8d4bc0d2e76454ae))
* rebuild project due to codegen change ([#126](https://github.com/Metronome-Industries/metronome-python/issues/126)) ([a864791](https://github.com/Metronome-Industries/metronome-python/commit/a8647918c7477a85016ae666e54c9790d3d99bbd))
* remove now unused `cached-property` dep ([#130](https://github.com/Metronome-Industries/metronome-python/issues/130)) ([9a3f84b](https://github.com/Metronome-Industries/metronome-python/commit/9a3f84bb7b53cc2e3c93787d49742d78ec5b3922))


### Documentation

* add info log level to readme ([#129](https://github.com/Metronome-Industries/metronome-python/issues/129)) ([670d5ab](https://github.com/Metronome-Industries/metronome-python/commit/670d5ab4aa1d5f77e085c7670acbeeac35a62a79))
* fix typos ([#154](https://github.com/Metronome-Industries/metronome-python/issues/154)) ([2fd0635](https://github.com/Metronome-Industries/metronome-python/commit/2fd06359cefeab3cf17dee380bdf06d6525fed12))
* **raw responses:** fix duplicate `the` ([#167](https://github.com/Metronome-Industries/metronome-python/issues/167)) ([5afb7a8](https://github.com/Metronome-Industries/metronome-python/commit/5afb7a86af029e074032962e57e187856c0f43b5))
* **readme:** example snippet for client context manager ([#145](https://github.com/Metronome-Industries/metronome-python/issues/145)) ([373b0bc](https://github.com/Metronome-Industries/metronome-python/commit/373b0bc94476027eca1c608ba655bd9728657556))
* **readme:** fix http client proxies example ([#138](https://github.com/Metronome-Industries/metronome-python/issues/138)) ([f9c9290](https://github.com/Metronome-Industries/metronome-python/commit/f9c9290fcfd0abfac1b5203cee6f7635ae184f6f))

## 0.1.0-beta.3 (2024-09-20)

Full Changelog: [v0.1.0-beta.2...v0.1.0-beta.3](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.2...v0.1.0-beta.3)

### Features

* **api:** OpenAPI spec update via Stainless API ([#84](https://github.com/Metronome-Industries/metronome-python/issues/84)) ([a8d1dfe](https://github.com/Metronome-Industries/metronome-python/commit/a8d1dfebe20be9ee5fb7d4f2b013fd87807a2737))
* **api:** OpenAPI spec update via Stainless API ([#90](https://github.com/Metronome-Industries/metronome-python/issues/90)) ([46cb936](https://github.com/Metronome-Industries/metronome-python/commit/46cb9365458494fb67d08b3c3262c3efda914120))
* **api:** OpenAPI spec update via Stainless API ([#94](https://github.com/Metronome-Industries/metronome-python/issues/94)) ([4277afd](https://github.com/Metronome-Industries/metronome-python/commit/4277afde9a016bdbc8aba455aa39f31f5b1a92aa))
* **client:** send retry count header ([#95](https://github.com/Metronome-Industries/metronome-python/issues/95)) ([4043bb1](https://github.com/Metronome-Industries/metronome-python/commit/4043bb1f46908f5f61185e14151b5e1f2eb9ee4e))


### Bug Fixes

* **client:** handle domains with underscores ([#93](https://github.com/Metronome-Industries/metronome-python/issues/93)) ([f732e98](https://github.com/Metronome-Industries/metronome-python/commit/f732e98ad0e808f38e748772794eb43f2dc14f29))


### Chores

* add docstrings to raw response properties ([#86](https://github.com/Metronome-Industries/metronome-python/issues/86)) ([2bcfcbb](https://github.com/Metronome-Industries/metronome-python/commit/2bcfcbb32dd99a56484629cc5f889370d89ba258))
* **internal:** bump pyright / mypy version ([#92](https://github.com/Metronome-Industries/metronome-python/issues/92)) ([991a602](https://github.com/Metronome-Industries/metronome-python/commit/991a602820f77257d384737e84601825ec45b853))
* **internal:** bump ruff ([#91](https://github.com/Metronome-Industries/metronome-python/issues/91)) ([51f756c](https://github.com/Metronome-Industries/metronome-python/commit/51f756c23dba7c3da03f7b4df730eeaa3b620da4))
* **internal:** codegen related update ([#88](https://github.com/Metronome-Industries/metronome-python/issues/88)) ([dad3013](https://github.com/Metronome-Industries/metronome-python/commit/dad301385a0ec75088a441351e1f6fa060f413bf))


### Documentation

* **readme:** add section on determining installed version ([#87](https://github.com/Metronome-Industries/metronome-python/issues/87)) ([c92078a](https://github.com/Metronome-Industries/metronome-python/commit/c92078afc49bbbda28c9a290956c4bcb58c487f3))
* update CONTRIBUTING.md ([#89](https://github.com/Metronome-Industries/metronome-python/issues/89)) ([9704fb9](https://github.com/Metronome-Industries/metronome-python/commit/9704fb9a6940ee716bb048f9aa6ff47615d71e49))

## 0.1.0-beta.2 (2024-09-05)

Full Changelog: [v0.1.0-beta.1...v0.1.0-beta.2](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.1...v0.1.0-beta.2)

### Features

* **api:** OpenAPI spec update via Stainless API ([#78](https://github.com/Metronome-Industries/metronome-python/issues/78)) ([23fc2d3](https://github.com/Metronome-Industries/metronome-python/commit/23fc2d3a093031a9e137d6877b462a4a7d9ea889))
* **api:** OpenAPI spec update via Stainless API ([#80](https://github.com/Metronome-Industries/metronome-python/issues/80)) ([41bd61f](https://github.com/Metronome-Industries/metronome-python/commit/41bd61ff8f70d7b59ff0c4000058caf593586fcf))
* **api:** OpenAPI spec update via Stainless API ([#82](https://github.com/Metronome-Industries/metronome-python/issues/82)) ([365cae9](https://github.com/Metronome-Industries/metronome-python/commit/365cae9dcb25d2081c83f4556e4921e13dd5b0b1))


### Chores

* pyproject.toml formatting changes ([#81](https://github.com/Metronome-Industries/metronome-python/issues/81)) ([f432b4f](https://github.com/Metronome-Industries/metronome-python/commit/f432b4f5f39e42eb888e725313ee87b84adb18ae))

## 0.1.0-beta.1 (2024-08-23)

Full Changelog: [v0.1.0-beta.0...v0.1.0-beta.1](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-beta.0...v0.1.0-beta.1)

### Features

* **api:** OpenAPI spec update via Stainless API ([#75](https://github.com/Metronome-Industries/metronome-python/issues/75)) ([4e3437e](https://github.com/Metronome-Industries/metronome-python/commit/4e3437e6bedcf2996594507ec4f7352e49a1e392))

## 0.1.0-beta.0 (2024-08-22)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-beta.0](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-alpha.4...v0.1.0-beta.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#46](https://github.com/Metronome-Industries/metronome-python/issues/46)) ([40b3e77](https://github.com/Metronome-Industries/metronome-python/commit/40b3e77f0beadf35974462d3f899caf1c98bdb09))
* **api:** OpenAPI spec update via Stainless API ([#47](https://github.com/Metronome-Industries/metronome-python/issues/47)) ([dc0a486](https://github.com/Metronome-Industries/metronome-python/commit/dc0a486b80eae244d6a0d8ee28eb720330bf45ce))
* **api:** OpenAPI spec update via Stainless API ([#51](https://github.com/Metronome-Industries/metronome-python/issues/51)) ([32b51b7](https://github.com/Metronome-Industries/metronome-python/commit/32b51b7355f3e043ee55620dba227b65ec21dc01))
* **api:** OpenAPI spec update via Stainless API ([#52](https://github.com/Metronome-Industries/metronome-python/issues/52)) ([19e0b68](https://github.com/Metronome-Industries/metronome-python/commit/19e0b68dbb8fd8709a19c983fd70bcc290259306))
* **api:** OpenAPI spec update via Stainless API ([#54](https://github.com/Metronome-Industries/metronome-python/issues/54)) ([f82e637](https://github.com/Metronome-Industries/metronome-python/commit/f82e6376a839f3d7e469f49e7d3a5f8914d1f940))
* **api:** OpenAPI spec update via Stainless API ([#57](https://github.com/Metronome-Industries/metronome-python/issues/57)) ([768bb4c](https://github.com/Metronome-Industries/metronome-python/commit/768bb4cdf7d6160b8658aea7a0ae09383c85cc96))
* **api:** OpenAPI spec update via Stainless API ([#59](https://github.com/Metronome-Industries/metronome-python/issues/59)) ([99508ad](https://github.com/Metronome-Industries/metronome-python/commit/99508adaf24ca2c3701119536e2bfb5eb0d170c4))
* **api:** OpenAPI spec update via Stainless API ([#60](https://github.com/Metronome-Industries/metronome-python/issues/60)) ([1bdc085](https://github.com/Metronome-Industries/metronome-python/commit/1bdc085afe19ed8ce2749f097f44962539cf15c9))
* **api:** OpenAPI spec update via Stainless API ([#61](https://github.com/Metronome-Industries/metronome-python/issues/61)) ([8a58b5c](https://github.com/Metronome-Industries/metronome-python/commit/8a58b5c27f2e7a8b3cf7948b2f5f008ae12fecf4))
* **api:** OpenAPI spec update via Stainless API ([#62](https://github.com/Metronome-Industries/metronome-python/issues/62)) ([6fd1a9f](https://github.com/Metronome-Industries/metronome-python/commit/6fd1a9f64baf1e8b26593265f67b0e53bc95b39b))
* **api:** OpenAPI spec update via Stainless API ([#63](https://github.com/Metronome-Industries/metronome-python/issues/63)) ([289a809](https://github.com/Metronome-Industries/metronome-python/commit/289a809b37fefe0739554154b8c63841b778ce4e))
* **api:** OpenAPI spec update via Stainless API ([#70](https://github.com/Metronome-Industries/metronome-python/issues/70)) ([b4ff212](https://github.com/Metronome-Industries/metronome-python/commit/b4ff212e9afc96cebecde3a1633b46b1f29ad834))
* **api:** OpenAPI spec update via Stainless API ([#71](https://github.com/Metronome-Industries/metronome-python/issues/71)) ([8ed8ccb](https://github.com/Metronome-Industries/metronome-python/commit/8ed8ccbca9e3909953e53580180fd3716093f61b))
* **api:** OpenAPI spec update via Stainless API ([#72](https://github.com/Metronome-Industries/metronome-python/issues/72)) ([b5e6b00](https://github.com/Metronome-Industries/metronome-python/commit/b5e6b006ae618267e682b3b4ef7be0c573bd7e37))
* **api:** OpenAPI spec update via Stainless API ([#73](https://github.com/Metronome-Industries/metronome-python/issues/73)) ([92000b7](https://github.com/Metronome-Industries/metronome-python/commit/92000b7395e73424e95cc5dbbc3662a2cd98fe07))
* **client:** add `retry_count` to raw response class ([#44](https://github.com/Metronome-Industries/metronome-python/issues/44)) ([aa7658d](https://github.com/Metronome-Industries/metronome-python/commit/aa7658d30aa75c374a16451607ebfe403a8bbd96))


### Bug Fixes

* **client:** correctly serialise array body params ([#50](https://github.com/Metronome-Industries/metronome-python/issues/50)) ([88156f9](https://github.com/Metronome-Industries/metronome-python/commit/88156f93aaf54cd5936f8a2229e03ebf1c55fd45))


### Chores

* **ci:** also run pydantic v1 tests ([#69](https://github.com/Metronome-Industries/metronome-python/issues/69)) ([84f5669](https://github.com/Metronome-Industries/metronome-python/commit/84f566900dce00002c8d737ee2c759f0ffe54c9d))
* **ci:** bump prism mock server version ([#55](https://github.com/Metronome-Industries/metronome-python/issues/55)) ([1bd186d](https://github.com/Metronome-Industries/metronome-python/commit/1bd186d700e211d9ad9c866b2d03b29034dd57e6))
* **client:** fix parsing union responses when non-json is returned ([#66](https://github.com/Metronome-Industries/metronome-python/issues/66)) ([51d2a84](https://github.com/Metronome-Industries/metronome-python/commit/51d2a841772bc332199bb9153836248f0e01744e))
* **examples:** minor formatting changes ([#58](https://github.com/Metronome-Industries/metronome-python/issues/58)) ([a518d00](https://github.com/Metronome-Industries/metronome-python/commit/a518d00c9a090dd582be30b3e1fe7ddc9e1bbd8c))
* **internal:** bump pyright ([#43](https://github.com/Metronome-Industries/metronome-python/issues/43)) ([19e30f3](https://github.com/Metronome-Industries/metronome-python/commit/19e30f3be4baf1018bf549f3ec232b3fb1b4a890))
* **internal:** bump ruff version ([#48](https://github.com/Metronome-Industries/metronome-python/issues/48)) ([b91ea15](https://github.com/Metronome-Industries/metronome-python/commit/b91ea1500f3e6d22762d7aaa674aea5ab3ecc52a))
* **internal:** ensure package is importable in lint cmd ([#56](https://github.com/Metronome-Industries/metronome-python/issues/56)) ([1a99c7e](https://github.com/Metronome-Industries/metronome-python/commit/1a99c7ef8f534cfdbe80bdf21f600cf322bd4a38))
* **internal:** remove deprecated ruff config ([#53](https://github.com/Metronome-Industries/metronome-python/issues/53)) ([36a843f](https://github.com/Metronome-Industries/metronome-python/commit/36a843f1be4ec852c6a5eaf9017bfe98e65fd4ab))
* **internal:** test updates ([#45](https://github.com/Metronome-Industries/metronome-python/issues/45)) ([d0c9e05](https://github.com/Metronome-Industries/metronome-python/commit/d0c9e051545b7da62a87877e1a46fd182afd52cc))
* **internal:** update pydantic compat helper function ([#49](https://github.com/Metronome-Industries/metronome-python/issues/49)) ([c057767](https://github.com/Metronome-Industries/metronome-python/commit/c057767494cd610adf91243c208720c37acb145d))
* **internal:** use `TypeAlias` marker for type assignments ([#41](https://github.com/Metronome-Industries/metronome-python/issues/41)) ([46f909b](https://github.com/Metronome-Industries/metronome-python/commit/46f909b46a53da1565274c81e8ab0e8bbfc7e8df))
* **internal:** use different 32bit detection method ([#64](https://github.com/Metronome-Industries/metronome-python/issues/64)) ([bec41c2](https://github.com/Metronome-Industries/metronome-python/commit/bec41c2ec4e038e0ecefd84ba655d6595118937e))
* update SDK settings ([#65](https://github.com/Metronome-Industries/metronome-python/issues/65)) ([4ac3a29](https://github.com/Metronome-Industries/metronome-python/commit/4ac3a29beb076bd1dca61b8ab882058620af4357))

## 0.1.0-alpha.4 (2024-08-01)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** OpenAPI spec update via Stainless API ([#13](https://github.com/Metronome-Industries/metronome-python/issues/13)) ([c85f8b8](https://github.com/Metronome-Industries/metronome-python/commit/c85f8b80868980ac3491764132aa22806b222499))
* **api:** OpenAPI spec update via Stainless API ([#15](https://github.com/Metronome-Industries/metronome-python/issues/15)) ([53fd756](https://github.com/Metronome-Industries/metronome-python/commit/53fd7561c04f29c34585c5aec62d91e4fe07e67f))
* **api:** OpenAPI spec update via Stainless API ([#16](https://github.com/Metronome-Industries/metronome-python/issues/16)) ([4dbb5d4](https://github.com/Metronome-Industries/metronome-python/commit/4dbb5d4de891dc5340ab1772bafc295648a72785))
* **api:** OpenAPI spec update via Stainless API ([#17](https://github.com/Metronome-Industries/metronome-python/issues/17)) ([dd62776](https://github.com/Metronome-Industries/metronome-python/commit/dd627760fc841858a6c6e0f273a09d0222a0dbdf))
* **api:** OpenAPI spec update via Stainless API ([#18](https://github.com/Metronome-Industries/metronome-python/issues/18)) ([625cc0b](https://github.com/Metronome-Industries/metronome-python/commit/625cc0b8a444149cebd38a73bdfcf1b0061aeddd))
* **api:** OpenAPI spec update via Stainless API ([#19](https://github.com/Metronome-Industries/metronome-python/issues/19)) ([4a7b4df](https://github.com/Metronome-Industries/metronome-python/commit/4a7b4df8b14883ce539d4a04704bc45bf7fbcb44))
* **api:** OpenAPI spec update via Stainless API ([#20](https://github.com/Metronome-Industries/metronome-python/issues/20)) ([e5817e2](https://github.com/Metronome-Industries/metronome-python/commit/e5817e2829c77a7bf8783fc63fba23e507028480))
* **api:** OpenAPI spec update via Stainless API ([#27](https://github.com/Metronome-Industries/metronome-python/issues/27)) ([1cc2506](https://github.com/Metronome-Industries/metronome-python/commit/1cc2506d5ff027611cfea94862290a7f82ddfcfd))
* **api:** OpenAPI spec update via Stainless API ([#35](https://github.com/Metronome-Industries/metronome-python/issues/35)) ([4f09f9a](https://github.com/Metronome-Industries/metronome-python/commit/4f09f9add276fd9775c7a77e0b25cb9c6c48c2f7))
* **api:** OpenAPI spec update via Stainless API ([#36](https://github.com/Metronome-Industries/metronome-python/issues/36)) ([8b525de](https://github.com/Metronome-Industries/metronome-python/commit/8b525de8736e9e85c1a1d431ba4c792e045222db))
* **api:** OpenAPI spec update via Stainless API ([#38](https://github.com/Metronome-Industries/metronome-python/issues/38)) ([70a5c0d](https://github.com/Metronome-Industries/metronome-python/commit/70a5c0d8cd448c351be1ce6bc08e28fd6dc3a95a))
* **api:** OpenAPI spec update via Stainless API ([#39](https://github.com/Metronome-Industries/metronome-python/issues/39)) ([406457a](https://github.com/Metronome-Industries/metronome-python/commit/406457aded2d8f2f992ee835b57bc0ba57e5a1e7))


### Chores

* **ci:** limit release doctor target branches ([#24](https://github.com/Metronome-Industries/metronome-python/issues/24)) ([acf1488](https://github.com/Metronome-Industries/metronome-python/commit/acf1488047b8f2c7bfdc56fcc1043a596aeff321))
* **ci:** limit release doctor target branches ([#31](https://github.com/Metronome-Industries/metronome-python/issues/31)) ([c156bed](https://github.com/Metronome-Industries/metronome-python/commit/c156bed56b023194020d91cee89b0de52cd4e118))
* **docs:** document how to do per-request http client customization ([#23](https://github.com/Metronome-Industries/metronome-python/issues/23)) ([08f43b4](https://github.com/Metronome-Industries/metronome-python/commit/08f43b48d9ba935fe2025b1051c7da66e98f4784))
* **docs:** document how to do per-request http client customization ([#30](https://github.com/Metronome-Industries/metronome-python/issues/30)) ([724b8a7](https://github.com/Metronome-Industries/metronome-python/commit/724b8a7dbb7b1878881f528639fc29bc33e43fae))
* fix error message import example ([#34](https://github.com/Metronome-Industries/metronome-python/issues/34)) ([8c636d4](https://github.com/Metronome-Industries/metronome-python/commit/8c636d40ae3212cceb510e35706c3753a4392669))
* **internal:** add type construction helper ([#37](https://github.com/Metronome-Industries/metronome-python/issues/37)) ([63ad7b4](https://github.com/Metronome-Industries/metronome-python/commit/63ad7b4bcf0da0ffed5c7fb11f974e9d537191ca))
* **internal:** codegen related update ([#21](https://github.com/Metronome-Industries/metronome-python/issues/21)) ([cfebac0](https://github.com/Metronome-Industries/metronome-python/commit/cfebac08c9e1fc1f429119d889848fa3c6fdf641))
* **internal:** codegen related update ([#28](https://github.com/Metronome-Industries/metronome-python/issues/28)) ([6d7401c](https://github.com/Metronome-Industries/metronome-python/commit/6d7401c68ae289876488b21b19a6107f5f4ad656))
* **internal:** refactor release doctor script ([#25](https://github.com/Metronome-Industries/metronome-python/issues/25)) ([b6f38e2](https://github.com/Metronome-Industries/metronome-python/commit/b6f38e204bffa12dd1617983674fa22533c6450f))
* **internal:** refactor release doctor script ([#32](https://github.com/Metronome-Industries/metronome-python/issues/32)) ([2698b6e](https://github.com/Metronome-Industries/metronome-python/commit/2698b6e9ffc07142e413521d2ce36f0fe9ccdce0))
* **internal:** update formatting ([#22](https://github.com/Metronome-Industries/metronome-python/issues/22)) ([1e03d52](https://github.com/Metronome-Industries/metronome-python/commit/1e03d529fda20eaa625ff8a9b80702e194fbcbc9))
* **internal:** update formatting ([#29](https://github.com/Metronome-Industries/metronome-python/issues/29)) ([f24d16c](https://github.com/Metronome-Industries/metronome-python/commit/f24d16c585f0c5688f1cbbffeee544777a52b0ab))
* **tests:** update prism version ([#26](https://github.com/Metronome-Industries/metronome-python/issues/26)) ([63a2391](https://github.com/Metronome-Industries/metronome-python/commit/63a239182cc21efc5e95beb45d1f606788e8f218))
* **tests:** update prism version ([#33](https://github.com/Metronome-Industries/metronome-python/issues/33)) ([b70a438](https://github.com/Metronome-Industries/metronome-python/commit/b70a4382fe8a94282cdc803b2462b8c2f39e046a))

## 0.1.0-alpha.3 (2024-06-14)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** OpenAPI spec update via Stainless API ([#10](https://github.com/Metronome-Industries/metronome-python/issues/10)) ([942ef29](https://github.com/Metronome-Industries/metronome-python/commit/942ef29a578bace159757b2056e417433a0d946e))
* **api:** OpenAPI spec update via Stainless API ([#7](https://github.com/Metronome-Industries/metronome-python/issues/7)) ([761be66](https://github.com/Metronome-Industries/metronome-python/commit/761be66a36024d246ec223ac99b265826d70e02d))
* **api:** OpenAPI spec update via Stainless API ([#9](https://github.com/Metronome-Industries/metronome-python/issues/9)) ([d070213](https://github.com/Metronome-Industries/metronome-python/commit/d070213b9dbbf4f5ca87915bab04924aa2c9235f))
* Update README.md with warning and remove Stainless branding ([#11](https://github.com/Metronome-Industries/metronome-python/issues/11)) ([8cb0d8b](https://github.com/Metronome-Industries/metronome-python/commit/8cb0d8b6ce2a50a2deca85ad1d185b7fb7587ccc))

## 0.1.0-alpha.2 (2024-06-10)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/Metronome-Industries/metronome-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#4](https://github.com/Metronome-Industries/metronome-python/issues/4)) ([17b7ce5](https://github.com/Metronome-Industries/metronome-python/commit/17b7ce57f0c3eb6310ccce51501c84b3e117c4c4))

## 0.1.0-alpha.1 (2024-06-10)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/Metronome-Industries/metronome-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#1](https://github.com/Metronome-Industries/metronome-python/issues/1)) ([7d15b94](https://github.com/Metronome-Industries/metronome-python/commit/7d15b941bb5ebe39b5285d651871a8da9228d2de))
