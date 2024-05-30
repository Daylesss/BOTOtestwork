<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">.</h1>
</p>
<p align="center">
    <em><code>► INSERT-TEXT-HERE</code></em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=default&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=default&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Redis-DC382D.svg?style=default&logo=Redis&logoColor=white" alt="Redis">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=default&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=default&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<br>
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=default&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Django-092E20.svg?style=default&logo=Django&logoColor=white" alt="Django">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=default&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=default&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=default&logo=JSON&logoColor=white" alt="JSON">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

<code>► INSERT-TEXT-HERE</code>

---

##  Features

<code>► INSERT-TEXT-HERE</code>

---

##  Repository Structure

```sh
└── ./
    ├── Makefile
    ├── README.md
    ├── bot
    │   ├── Dockerfile
    │   ├── bot.py
    │   ├── config.py
    │   ├── dialogs
    │   │   ├── balance
    │   │   │   ├── __init__.py
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   ├── card
    │   │   │   ├── __init__.py
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   ├── deposit
    │   │   │   ├── __init__.py
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   ├── errors.py
    │   │   ├── history
    │   │   │   ├── __init__.py
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   ├── main_dialog
    │   │   │   ├── __init__.py
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   ├── reports
    │   │   │   ├── __init__.py
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   ├── settings
    │   │   │   ├── __init__.py
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   ├── states.py
    │   │   ├── trader_auth
    │   │   │   ├── dialog.py
    │   │   │   ├── getters.py
    │   │   │   └── handlers.py
    │   │   └── withdraw
    │   │       ├── __init__.py
    │   │       ├── dialog.py
    │   │       ├── getters.py
    │   │       └── handlers.py
    │   ├── enums.py
    │   ├── kasha.py
    │   ├── middlewares.py
    │   ├── requirements.txt
    │   ├── utils.py
    │   └── validators.py
    ├── clickhouse
    │   └── logtable.sql
    ├── default.env
    ├── docker-compose.prod.yml
    ├── docker-compose.yml
    ├── env.example
    ├── front
    │   ├── Dockerfile
    │   ├── callbacks.py
    │   ├── clientapp.py
    │   ├── config.py
    │   ├── fapi
    │   │   ├── frontapi
    │   │   │   ├── __init__.py
    │   │   │   └── schemas.py
    │   │   └── traderapi
    │   │       ├── __init__.py
    │   │       └── schemas.py
    │   ├── kasha.py
    │   ├── main.py
    │   ├── requirements.txt
    │   ├── static
    │   │   ├── app.js
    │   │   ├── css
    │   │   │   ├── style.css
    │   │   │   └── style.min.css
    │   │   ├── fonts
    │   │   │   ├── Inter-Bold.woff
    │   │   │   ├── Inter-Bold.woff2
    │   │   │   ├── Inter-Regular.woff
    │   │   │   └── Inter-Regular.woff2
    │   │   ├── img
    │   │   │   └── icons
    │   │   │       ├── attach.svg
    │   │   │       ├── copy.svg
    │   │   │       ├── delete.svg
    │   │   │       └── rub.svg
    │   │   ├── jquery.2.3.5.min.js
    │   │   ├── js
    │   │   │   └── app.min.js
    │   │   └── loader.gif
    │   └── tools.py
    ├── manager
    │   ├── Dockerfile
    │   ├── base.py
    │   ├── chouse.py
    │   ├── common.py
    │   ├── config.py
    │   ├── deposit_matching.py
    │   ├── enums.py
    │   ├── fpg.py
    │   ├── gate_routing.py
    │   ├── kasha.py
    │   ├── manager.py
    │   ├── models.py
    │   ├── requirements.txt
    │   ├── sms.py
    │   ├── syncaccounts.py
    │   ├── utils.py
    │   └── withdraw_matching.py
    ├── nginx
    │   ├── Dockerfile
    │   └── nginx.conf
    ├── piapi
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── app.py
    │   ├── data
    │   │   └── bankbins.json
    │   └── requirements.txt
    ├── pitupi
    │   ├── Dockerfile
    │   ├── cli
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   ├── 0002_alter_clientdeposit_options_and_more.py
    │   │   │   ├── 0002_clientsetting.py
    │   │   │   ├── 0003_merge_20230901_1622.py
    │   │   │   ├── 0004_clientdepositmanager.py
    │   │   │   ├── 0005_clientclient.py
    │   │   │   ├── 0006_alter_clientclient_options.py
    │   │   │   ├── 0007_alter_clientclient_options.py
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── views.py
    │   ├── manage.py
    │   ├── money
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── config.py
    │   │   ├── fixtures
    │   │   │   ├── bank_setting.json
    │   │   │   ├── banks.json
    │   │   │   ├── currencies.json
    │   │   │   ├── mdl_currency.json
    │   │   │   ├── settings.json
    │   │   │   └── test_users.json
    │   │   ├── forms.py
    │   │   ├── helper.py
    │   │   ├── kafka.py
    │   │   ├── management
    │   │   │   ├── __init__.py
    │   │   │   └── commands
    │   │   │       ├── __init__.py
    │   │   │       ├── cleaner.py
    │   │   │       ├── kafka_consumer.py
    │   │   │       ├── kasha.py
    │   │   │       ├── proxy_loader.py
    │   │   │       ├── recognizer.py
    │   │   │       └── test_cleaner.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   ├── 0002_bank_alter_deposit_options_alter_withdraw_options_and_more.py
    │   │   │   ├── 0003_remove_deposit_error_status_deposit_error_desc_and_more.py
    │   │   │   ├── 0004_alter_visit_error_desc.py
    │   │   │   ├── 0005_alter_deposit_error_desc.py
    │   │   │   ├── 0006_deposit_pre_status_visit_callback_at_and_more.py
    │   │   │   ├── 0007_deposit_allowed_clients_visit_gate_data_and_more.py
    │   │   │   ├── 0008_deposit_error_type_withdraw_usage.py
    │   │   │   ├── 0009_visit_error_type_alter_deposit_error_type.py
    │   │   │   ├── 0010_alter_withdraw_priority.py
    │   │   │   ├── 0011_provider_supplier_rename_bank_deposit_issuer_and_more.py
    │   │   │   ├── 0012_fill_exists_cards.py
    │   │   │   ├── 0013_deposit_acquirer_visit_acquirer.py
    │   │   │   ├── 0014_card_last_deposit_at_card_last_withdraw_at_and_more.py
    │   │   │   ├── 0015_proxysupplier_gate_is_turbo_proxy_visit_proxy.py
    │   │   │   ├── 0016_deposit_user_agent_visit_browser_agent_and_more.py
    │   │   │   ├── 0017_alter_visit_deposit.py
    │   │   │   ├── 0018_account_remove_client_master_client_telegram_id_and_more.py
    │   │   │   ├── 0019_rename_flow_deposit_method_and_more.py
    │   │   │   ├── 0020_card_limit.py
    │   │   │   ├── 0021_alter_deposit_pre_status_alter_deposit_status_and_more.py
    │   │   │   ├── 0022_deposit_original_amount_deposit_updated_at_and_more.py
    │   │   │   ├── 0023_alter_card_status.py
    │   │   │   ├── 0024_alter_account_sub_id.py
    │   │   │   ├── 0025_alter_client_name_alter_client_telegram_id.py
    │   │   │   ├── 0026_alter_account_currency.py
    │   │   │   ├── 0027_account_denominator_account_is_master.py
    │   │   │   ├── 0027_setting_alter_account_created_at_and_more.py
    │   │   │   ├── 0028_merge_20230505_1427.py
    │   │   │   ├── 0029_currency_remove_account_denominator_and_more.py
    │   │   │   ├── 0030_auto_20230510_1835.py
    │   │   │   ├── 0031_auto_20230510_1836.py
    │   │   │   ├── 0032_operationlog.py
    │   │   │   ├── 0033_deposit_pin.py
    │   │   │   ├── 0034_alter_card_limit.py
    │   │   │   ├── 0035_account_address.py
    │   │   │   ├── 0036_card_currency.py
    │   │   │   ├── 0037_deposit_data_withdraw_data.py
    │   │   │   ├── 0038_receipt_withdraw_withdraw_asignee_and_more.py
    │   │   │   ├── 0039_remove_operationlog_operation_operationlog_deposit_and_more.py
    │   │   │   ├── 0040_alter_operationlog_deposit.py
    │   │   │   ├── 0041_deposit_notify_trader_at_withdraw_notify_trader_at.py
    │   │   │   ├── 0042_banksetting.py
    │   │   │   ├── 0043_remove_withdraw_asignee_withdraw_assignee.py
    │   │   │   ├── 0044_withdraw_kind_alter_withdraw_assignee_tradersettings.py
    │   │   │   ├── 0045_account_withdraw_online.py
    │   │   │   ├── 0046_clientwithdraw_deposit_external_id_and_more.py
    │   │   │   ├── 0046_rename_online_account_deposit_online.py
    │   │   │   ├── 0047_remove_tradersettings_bank_and_more.py
    │   │   │   ├── 0048_merge_20230618_0152.py
    │   │   │   ├── 0049_alter_tradersettings_trader.py
    │   │   │   ├── 0050_alter_deposit_method_alter_withdraw_method.py
    │   │   │   ├── 0051_auto_20230620_1511.py
    │   │   │   ├── 0052_clientreceipt.py
    │   │   │   ├── 0053_alter_operationlog_tag.py
    │   │   │   ├── 0054_clientgroup_account_is_verified_client_group_set.py
    │   │   │   ├── 0055_trader.py
    │   │   │   ├── 0056_receipt_withdraw_group_id_withdraw_withdraw_group_id.py
    │   │   │   ├── 0057_receiptgroup_withdrawgroup_alter_deposit_pre_status_and_more.py
    │   │   │   ├── 0058_receipt_bank_from_receipt_card_from_receipt_data_and_more.py
    │   │   │   ├── 0059_alter_deposit_pre_status_alter_deposit_status_and_more.py
    │   │   │   ├── 0059_receipt_receipt_image.py
    │   │   │   ├── 0060_account_max_order_amount_db.py
    │   │   │   ├── 0060_withdraw_assignee_trader_setting.py
    │   │   │   ├── 0061_receipt_is_recognition_attempt.py
    │   │   │   ├── 0062_merge_20230707_1116.py
    │   │   │   ├── 0063_merge_20230707_1713.py
    │   │   │   ├── 0064_notificationapp_smsapp.py
    │   │   │   ├── 0064_toptrader.py
    │   │   │   ├── 0065_merge_0064_notificationapp_smsapp_0064_toptrader.py
    │   │   │   ├── 0066_delete_notificationapp_delete_smsapp_and_more.py
    │   │   │   ├── 0067_notificationapp_smsapp_toptrader.py
    │   │   │   ├── 0068_notificationapp_amount_notificationapp_bank_and_more.py
    │   │   │   ├── 0069_deposit_assignee_alter_deposit_pre_status_and_more.py
    │   │   │   ├── 0070_alter_deposit_assignee_alter_withdraw_assignee.py
    │   │   │   ├── 0071_deposit_fail_url_deposit_success_url.py
    │   │   │   ├── 0072_alter_operationlog_tag.py
    │   │   │   ├── 0073_clientdeposit.py
    │   │   │   ├── 0074_deposit_success_trigger_withdraw_deposit_and_more.py
    │   │   │   ├── 0075_alter_deposit_success_trigger_and_more.py
    │   │   │   ├── 0076_alter_deposit_method_alter_withdraw_method.py
    │   │   │   ├── 0077_clientmanager_alter_deposit_pre_status_and_more.py
    │   │   │   ├── 0077_notificationapp_account_notificationapp_cards_and_more.py
    │   │   │   ├── 0078_merge_20230814_1918.py
    │   │   │   ├── 0079_alter_trader_options_and_more.py
    │   │   │   ├── 0080_client_merchant_brand.py
    │   │   │   ├── 0081_tradersettings_bank_settings_and_more.py
    │   │   │   ├── 0082_auto_20230822_1802.py
    │   │   │   ├── 0083_remove_tradersettings_bank_setting.py
    │   │   │   ├── 0084_remove_tradersettings_bank_settings_and_more.py
    │   │   │   ├── 0085_tradersettings_freeze_and_more.py
    │   │   │   ├── 0086_rename_tradersettings_tradersetting.py
    │   │   │   ├── 0087_alter_tradersetting_amount_done_and_more.py
    │   │   │   ├── 0088_clienttradersetting_alter_tradersetting_amount_done_and_more.py
    │   │   │   ├── 0089_alter_trader_options_and_more.py
    │   │   │   ├── 0090_clientsetting_alter_trader_options.py
    │   │   │   ├── 0090_delete_clientdeposit_delete_clientmanager_and_more.py
    │   │   │   ├── 0091_merge_20230830_1417.py
    │   │   │   ├── 0091_merge_20230831_1406.py
    │   │   │   ├── 0092_alter_withdraw_options.py
    │   │   │   ├── 0092_delete_clientsetting.py
    │   │   │   ├── 0093_alter_deposit_options_alter_withdraw_options_and_more.py
    │   │   │   ├── 0094_alter_deposit_success_trigger_and_more.py
    │   │   │   ├── 0094_merge_20230901_1622.py
    │   │   │   ├── 0095_merge_20230923_1619.py
    │   │   │   ├── 0096_bank_currency_alter_client_merchant_brand.py
    │   │   │   ├── 0097_card_device_id_card_online_at.py
    │   │   │   ├── 0098_alter_card_online_at.py
    │   │   │   ├── 0098_alter_deposit_method_alter_withdraw_method.py
    │   │   │   ├── 0099_merge_20230929_2012.py
    │   │   │   ├── 0099_merge_20231002_1842.py
    │   │   │   ├── 0100_account_need_premoderation.py
    │   │   │   ├── 0101_merge_20231002_1921.py
    │   │   │   ├── 0102_alter_account_need_premoderation.py
    │   │   │   ├── 0103_card_phone.py
    │   │   │   ├── 0104_card_card_holder.py
    │   │   │   ├── 0105_alter_c2ctradecard_options_alter_c2ctradecard_card_and_more.py
    │   │   │   ├── 0105_alter_c2ctradecard_options_client_full_name_and_more.py
    │   │   │   ├── 0106_merge_20231114_1638.py
    │   │   │   ├── 0107_alter_client_merchant_brand.py
    │   │   │   ├── 0108_account_deposit_priority.py
    │   │   │   ├── 0109_alter_client_merchant_brand.py
    │   │   │   ├── 0110_card_max_amount_limit_card_transcation_count_limit_and_more.py
    │   │   │   ├── 0111_rename_transcation_count_limit_card_transaction_count_limit_and_more.py
    │   │   │   ├── 0112_card_min_amount_limit.py
    │   │   │   ├── 0113_account_max_withdraw_order_count.py
    │   │   │   ├── 0114_alter_deposit_pre_status_alter_deposit_status_and_more.py
    │   │   │   ├── 0114_deposit_allowed_groups_withdraw_allowed_groups.py
    │   │   │   ├── 0115_client_user.py
    │   │   │   ├── 0116_alter_client_user.py
    │   │   │   ├── 0117_clientgroup_secret.py
    │   │   │   ├── 0118_merge_20231215_2102.py
    │   │   │   ├── 0119_client_withdraw_priority.py
    │   │   │   ├── 0120_alter_client_withdraw_priority.py
    │   │   │   ├── 0121_alter_client_full_name.py
    │   │   │   ├── 0122_client_kind_alter_card_status.py
    │   │   │   ├── 0123_client_deposit_percent_client_withdraw_percent.py
    │   │   │   ├── 0124_client_allow_cents_deposit_matching_amount_and_more.py
    │   │   │   ├── 0125_alter_client_merchant_brand.py
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   ├── utils.py
    │   │   └── views.py
    │   ├── pitupi
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── reports
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── views.py
    │   ├── requirements.txt
    │   ├── templates
    │   │   └── admin
    │   │       └── search_form.html
    │   ├── tests
    │   │   ├── __init__.py
    │   │   └── deposit_tests.py
    │   ├── trader
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   └── __init__.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── views.py
    │   └── turbo
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── migrations
    │       │   ├── 0001_initial.py
    │       │   ├── 0002_proxysupplier_proxy.py
    │       │   ├── 0003_alter_useragent_gibfp.py
    │       │   ├── 0004_useragent_headers_alter_useragent_gibfp.py
    │       │   ├── 0005_useragent_status.py
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── tests.py
    │       └── views.py
    └── pyproject.toml
```

---

##  Modules

<details closed><summary>.</summary>

| File                                               | Summary                         |
| ---                                                | ---                             |
| [env.example](env.example)                         | <code>► INSERT-TEXT-HERE</code> |
| [Makefile](Makefile)                               | <code>► INSERT-TEXT-HERE</code> |
| [docker-compose.yml](docker-compose.yml)           | <code>► INSERT-TEXT-HERE</code> |
| [pyproject.toml](pyproject.toml)                   | <code>► INSERT-TEXT-HERE</code> |
| [docker-compose.prod.yml](docker-compose.prod.yml) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>nginx</summary>

| File                           | Summary                         |
| ---                            | ---                             |
| [Dockerfile](nginx/Dockerfile) | <code>► INSERT-TEXT-HERE</code> |
| [nginx.conf](nginx/nginx.conf) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot</summary>

| File                                     | Summary                         |
| ---                                      | ---                             |
| [config.py](bot/config.py)               | <code>► INSERT-TEXT-HERE</code> |
| [bot.py](bot/bot.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [Dockerfile](bot/Dockerfile)             | <code>► INSERT-TEXT-HERE</code> |
| [middlewares.py](bot/middlewares.py)     | <code>► INSERT-TEXT-HERE</code> |
| [validators.py](bot/validators.py)       | <code>► INSERT-TEXT-HERE</code> |
| [kasha.py](bot/kasha.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [requirements.txt](bot/requirements.txt) | <code>► INSERT-TEXT-HERE</code> |
| [utils.py](bot/utils.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [enums.py](bot/enums.py)                 | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs</summary>

| File                               | Summary                         |
| ---                                | ---                             |
| [errors.py](bot/dialogs/errors.py) | <code>► INSERT-TEXT-HERE</code> |
| [states.py](bot/dialogs/states.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.history</summary>

| File                                           | Summary                         |
| ---                                            | ---                             |
| [handlers.py](bot/dialogs/history/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/history/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/history/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.reports</summary>

| File                                           | Summary                         |
| ---                                            | ---                             |
| [handlers.py](bot/dialogs/reports/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/reports/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/reports/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.card</summary>

| File                                        | Summary                         |
| ---                                         | ---                             |
| [handlers.py](bot/dialogs/card/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/card/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/card/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.deposit</summary>

| File                                           | Summary                         |
| ---                                            | ---                             |
| [handlers.py](bot/dialogs/deposit/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/deposit/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/deposit/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.settings</summary>

| File                                            | Summary                         |
| ---                                             | ---                             |
| [handlers.py](bot/dialogs/settings/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/settings/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/settings/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.withdraw</summary>

| File                                            | Summary                         |
| ---                                             | ---                             |
| [handlers.py](bot/dialogs/withdraw/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/withdraw/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/withdraw/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.trader_auth</summary>

| File                                               | Summary                         |
| ---                                                | ---                             |
| [handlers.py](bot/dialogs/trader_auth/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/trader_auth/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/trader_auth/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.balance</summary>

| File                                           | Summary                         |
| ---                                            | ---                             |
| [handlers.py](bot/dialogs/balance/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/balance/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/balance/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>bot.dialogs.main_dialog</summary>

| File                                               | Summary                         |
| ---                                                | ---                             |
| [handlers.py](bot/dialogs/main_dialog/handlers.py) | <code>► INSERT-TEXT-HERE</code> |
| [getters.py](bot/dialogs/main_dialog/getters.py)   | <code>► INSERT-TEXT-HERE</code> |
| [dialog.py](bot/dialogs/main_dialog/dialog.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>front</summary>

| File                                       | Summary                         |
| ---                                        | ---                             |
| [config.py](front/config.py)               | <code>► INSERT-TEXT-HERE</code> |
| [Dockerfile](front/Dockerfile)             | <code>► INSERT-TEXT-HERE</code> |
| [clientapp.py](front/clientapp.py)         | <code>► INSERT-TEXT-HERE</code> |
| [kasha.py](front/kasha.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [callbacks.py](front/callbacks.py)         | <code>► INSERT-TEXT-HERE</code> |
| [requirements.txt](front/requirements.txt) | <code>► INSERT-TEXT-HERE</code> |
| [tools.py](front/tools.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [main.py](front/main.py)                   | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>front.fapi.frontapi</summary>

| File                                         | Summary                         |
| ---                                          | ---                             |
| [schemas.py](front/fapi/frontapi/schemas.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>front.fapi.traderapi</summary>

| File                                          | Summary                         |
| ---                                           | ---                             |
| [schemas.py](front/fapi/traderapi/schemas.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi</summary>

| File                                        | Summary                         |
| ---                                         | ---                             |
| [Dockerfile](pitupi/Dockerfile)             | <code>► INSERT-TEXT-HERE</code> |
| [requirements.txt](pitupi/requirements.txt) | <code>► INSERT-TEXT-HERE</code> |
| [manage.py](pitupi/manage.py)               | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.trader</summary>

| File                                 | Summary                         |
| ---                                  | ---                             |
| [views.py](pitupi/trader/views.py)   | <code>► INSERT-TEXT-HERE</code> |
| [apps.py](pitupi/trader/apps.py)     | <code>► INSERT-TEXT-HERE</code> |
| [tests.py](pitupi/trader/tests.py)   | <code>► INSERT-TEXT-HERE</code> |
| [admin.py](pitupi/trader/admin.py)   | <code>► INSERT-TEXT-HERE</code> |
| [models.py](pitupi/trader/models.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.trader.migrations</summary>

| File                                                        | Summary                         |
| ---                                                         | ---                             |
| [0001_initial.py](pitupi/trader/migrations/0001_initial.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.reports</summary>

| File                                  | Summary                         |
| ---                                   | ---                             |
| [views.py](pitupi/reports/views.py)   | <code>► INSERT-TEXT-HERE</code> |
| [apps.py](pitupi/reports/apps.py)     | <code>► INSERT-TEXT-HERE</code> |
| [tests.py](pitupi/reports/tests.py)   | <code>► INSERT-TEXT-HERE</code> |
| [admin.py](pitupi/reports/admin.py)   | <code>► INSERT-TEXT-HERE</code> |
| [models.py](pitupi/reports/models.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.reports.migrations</summary>

| File                                                         | Summary                         |
| ---                                                          | ---                             |
| [0001_initial.py](pitupi/reports/migrations/0001_initial.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.money</summary>

| File                                | Summary                         |
| ---                                 | ---                             |
| [config.py](pitupi/money/config.py) | <code>► INSERT-TEXT-HERE</code> |
| [views.py](pitupi/money/views.py)   | <code>► INSERT-TEXT-HERE</code> |
| [kafka.py](pitupi/money/kafka.py)   | <code>► INSERT-TEXT-HERE</code> |
| [apps.py](pitupi/money/apps.py)     | <code>► INSERT-TEXT-HERE</code> |
| [helper.py](pitupi/money/helper.py) | <code>► INSERT-TEXT-HERE</code> |
| [tests.py](pitupi/money/tests.py)   | <code>► INSERT-TEXT-HERE</code> |
| [admin.py](pitupi/money/admin.py)   | <code>► INSERT-TEXT-HERE</code> |
| [utils.py](pitupi/money/utils.py)   | <code>► INSERT-TEXT-HERE</code> |
| [models.py](pitupi/money/models.py) | <code>► INSERT-TEXT-HERE</code> |
| [forms.py](pitupi/money/forms.py)   | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.money.management.commands</summary>

| File                                                                    | Summary                         |
| ---                                                                     | ---                             |
| [kasha.py](pitupi/money/management/commands/kasha.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [kafka_consumer.py](pitupi/money/management/commands/kafka_consumer.py) | <code>► INSERT-TEXT-HERE</code> |
| [proxy_loader.py](pitupi/money/management/commands/proxy_loader.py)     | <code>► INSERT-TEXT-HERE</code> |
| [recognizer.py](pitupi/money/management/commands/recognizer.py)         | <code>► INSERT-TEXT-HERE</code> |
| [cleaner.py](pitupi/money/management/commands/cleaner.py)               | <code>► INSERT-TEXT-HERE</code> |
| [test_cleaner.py](pitupi/money/management/commands/test_cleaner.py)     | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.money.migrations</summary>

| File                                                                                                                                                                                 | Summary                         |
| ---                                                                                                                                                                                  | ---                             |
| [0060_withdraw_assignee_trader_setting.py](pitupi/money/migrations/0060_withdraw_assignee_trader_setting.py)                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0090_clientsetting_alter_trader_options.py](pitupi/money/migrations/0090_clientsetting_alter_trader_options.py)                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0022_deposit_original_amount_deposit_updated_at_and_more.py](pitupi/money/migrations/0022_deposit_original_amount_deposit_updated_at_and_more.py)                                   | <code>► INSERT-TEXT-HERE</code> |
| [0094_alter_deposit_success_trigger_and_more.py](pitupi/money/migrations/0094_alter_deposit_success_trigger_and_more.py)                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0063_merge_20230707_1713.py](pitupi/money/migrations/0063_merge_20230707_1713.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0092_alter_withdraw_options.py](pitupi/money/migrations/0092_alter_withdraw_options.py)                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0005_alter_deposit_error_desc.py](pitupi/money/migrations/0005_alter_deposit_error_desc.py)                                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0034_alter_card_limit.py](pitupi/money/migrations/0034_alter_card_limit.py)                                                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0077_notificationapp_account_notificationapp_cards_and_more.py](pitupi/money/migrations/0077_notificationapp_account_notificationapp_cards_and_more.py)                             | <code>► INSERT-TEXT-HERE</code> |
| [0053_alter_operationlog_tag.py](pitupi/money/migrations/0053_alter_operationlog_tag.py)                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0048_merge_20230618_0152.py](pitupi/money/migrations/0048_merge_20230618_0152.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0045_account_withdraw_online.py](pitupi/money/migrations/0045_account_withdraw_online.py)                                                                                           | <code>► INSERT-TEXT-HERE</code> |
| [0021_alter_deposit_pre_status_alter_deposit_status_and_more.py](pitupi/money/migrations/0021_alter_deposit_pre_status_alter_deposit_status_and_more.py)                             | <code>► INSERT-TEXT-HERE</code> |
| [0002_bank_alter_deposit_options_alter_withdraw_options_and_more.py](pitupi/money/migrations/0002_bank_alter_deposit_options_alter_withdraw_options_and_more.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [0124_client_allow_cents_deposit_matching_amount_and_more.py](pitupi/money/migrations/0124_client_allow_cents_deposit_matching_amount_and_more.py)                                   | <code>► INSERT-TEXT-HERE</code> |
| [0013_deposit_acquirer_visit_acquirer.py](pitupi/money/migrations/0013_deposit_acquirer_visit_acquirer.py)                                                                           | <code>► INSERT-TEXT-HERE</code> |
| [0114_alter_deposit_pre_status_alter_deposit_status_and_more.py](pitupi/money/migrations/0114_alter_deposit_pre_status_alter_deposit_status_and_more.py)                             | <code>► INSERT-TEXT-HERE</code> |
| [0118_merge_20231215_2102.py](pitupi/money/migrations/0118_merge_20231215_2102.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0007_deposit_allowed_clients_visit_gate_data_and_more.py](pitupi/money/migrations/0007_deposit_allowed_clients_visit_gate_data_and_more.py)                                         | <code>► INSERT-TEXT-HERE</code> |
| [0033_deposit_pin.py](pitupi/money/migrations/0033_deposit_pin.py)                                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0099_merge_20231002_1842.py](pitupi/money/migrations/0099_merge_20231002_1842.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0027_account_denominator_account_is_master.py](pitupi/money/migrations/0027_account_denominator_account_is_master.py)                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0072_alter_operationlog_tag.py](pitupi/money/migrations/0072_alter_operationlog_tag.py)                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0059_alter_deposit_pre_status_alter_deposit_status_and_more.py](pitupi/money/migrations/0059_alter_deposit_pre_status_alter_deposit_status_and_more.py)                             | <code>► INSERT-TEXT-HERE</code> |
| [0064_toptrader.py](pitupi/money/migrations/0064_toptrader.py)                                                                                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0114_deposit_allowed_groups_withdraw_allowed_groups.py](pitupi/money/migrations/0114_deposit_allowed_groups_withdraw_allowed_groups.py)                                             | <code>► INSERT-TEXT-HERE</code> |
| [0091_merge_20230831_1406.py](pitupi/money/migrations/0091_merge_20230831_1406.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0064_notificationapp_smsapp.py](pitupi/money/migrations/0064_notificationapp_smsapp.py)                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0088_clienttradersetting_alter_tradersetting_amount_done_and_more.py](pitupi/money/migrations/0088_clienttradersetting_alter_tradersetting_amount_done_and_more.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [0039_remove_operationlog_operation_operationlog_deposit_and_more.py](pitupi/money/migrations/0039_remove_operationlog_operation_operationlog_deposit_and_more.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [0108_account_deposit_priority.py](pitupi/money/migrations/0108_account_deposit_priority.py)                                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0085_tradersettings_freeze_and_more.py](pitupi/money/migrations/0085_tradersettings_freeze_and_more.py)                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0041_deposit_notify_trader_at_withdraw_notify_trader_at.py](pitupi/money/migrations/0041_deposit_notify_trader_at_withdraw_notify_trader_at.py)                                     | <code>► INSERT-TEXT-HERE</code> |
| [0009_visit_error_type_alter_deposit_error_type.py](pitupi/money/migrations/0009_visit_error_type_alter_deposit_error_type.py)                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0008_deposit_error_type_withdraw_usage.py](pitupi/money/migrations/0008_deposit_error_type_withdraw_usage.py)                                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0109_alter_client_merchant_brand.py](pitupi/money/migrations/0109_alter_client_merchant_brand.py)                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0102_alter_account_need_premoderation.py](pitupi/money/migrations/0102_alter_account_need_premoderation.py)                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0020_card_limit.py](pitupi/money/migrations/0020_card_limit.py)                                                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0081_tradersettings_bank_settings_and_more.py](pitupi/money/migrations/0081_tradersettings_bank_settings_and_more.py)                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0098_alter_deposit_method_alter_withdraw_method.py](pitupi/money/migrations/0098_alter_deposit_method_alter_withdraw_method.py)                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0099_merge_20230929_2012.py](pitupi/money/migrations/0099_merge_20230929_2012.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0103_card_phone.py](pitupi/money/migrations/0103_card_phone.py)                                                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0049_alter_tradersettings_trader.py](pitupi/money/migrations/0049_alter_tradersettings_trader.py)                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0107_alter_client_merchant_brand.py](pitupi/money/migrations/0107_alter_client_merchant_brand.py)                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0117_clientgroup_secret.py](pitupi/money/migrations/0117_clientgroup_secret.py)                                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0077_clientmanager_alter_deposit_pre_status_and_more.py](pitupi/money/migrations/0077_clientmanager_alter_deposit_pre_status_and_more.py)                                           | <code>► INSERT-TEXT-HERE</code> |
| [0003_remove_deposit_error_status_deposit_error_desc_and_more.py](pitupi/money/migrations/0003_remove_deposit_error_status_deposit_error_desc_and_more.py)                           | <code>► INSERT-TEXT-HERE</code> |
| [0104_card_card_holder.py](pitupi/money/migrations/0104_card_card_holder.py)                                                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0123_client_deposit_percent_client_withdraw_percent.py](pitupi/money/migrations/0123_client_deposit_percent_client_withdraw_percent.py)                                             | <code>► INSERT-TEXT-HERE</code> |
| [0057_receiptgroup_withdrawgroup_alter_deposit_pre_status_and_more.py](pitupi/money/migrations/0057_receiptgroup_withdrawgroup_alter_deposit_pre_status_and_more.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [0001_initial.py](pitupi/money/migrations/0001_initial.py)                                                                                                                           | <code>► INSERT-TEXT-HERE</code> |
| [0012_fill_exists_cards.py](pitupi/money/migrations/0012_fill_exists_cards.py)                                                                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0105_alter_c2ctradecard_options_client_full_name_and_more.py](pitupi/money/migrations/0105_alter_c2ctradecard_options_client_full_name_and_more.py)                                 | <code>► INSERT-TEXT-HERE</code> |
| [0092_delete_clientsetting.py](pitupi/money/migrations/0092_delete_clientsetting.py)                                                                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0100_account_need_premoderation.py](pitupi/money/migrations/0100_account_need_premoderation.py)                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0059_receipt_receipt_image.py](pitupi/money/migrations/0059_receipt_receipt_image.py)                                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0010_alter_withdraw_priority.py](pitupi/money/migrations/0010_alter_withdraw_priority.py)                                                                                           | <code>► INSERT-TEXT-HERE</code> |
| [0116_alter_client_user.py](pitupi/money/migrations/0116_alter_client_user.py)                                                                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0125_alter_client_merchant_brand.py](pitupi/money/migrations/0125_alter_client_merchant_brand.py)                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0122_client_kind_alter_card_status.py](pitupi/money/migrations/0122_client_kind_alter_card_status.py)                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0061_receipt_is_recognition_attempt.py](pitupi/money/migrations/0061_receipt_is_recognition_attempt.py)                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0042_banksetting.py](pitupi/money/migrations/0042_banksetting.py)                                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0062_merge_20230707_1116.py](pitupi/money/migrations/0062_merge_20230707_1116.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0079_alter_trader_options_and_more.py](pitupi/money/migrations/0079_alter_trader_options_and_more.py)                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0080_client_merchant_brand.py](pitupi/money/migrations/0080_client_merchant_brand.py)                                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0052_clientreceipt.py](pitupi/money/migrations/0052_clientreceipt.py)                                                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0071_deposit_fail_url_deposit_success_url.py](pitupi/money/migrations/0071_deposit_fail_url_deposit_success_url.py)                                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0096_bank_currency_alter_client_merchant_brand.py](pitupi/money/migrations/0096_bank_currency_alter_client_merchant_brand.py)                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0112_card_min_amount_limit.py](pitupi/money/migrations/0112_card_min_amount_limit.py)                                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0060_account_max_order_amount_db.py](pitupi/money/migrations/0060_account_max_order_amount_db.py)                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0089_alter_trader_options_and_more.py](pitupi/money/migrations/0089_alter_trader_options_and_more.py)                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0091_merge_20230830_1417.py](pitupi/money/migrations/0091_merge_20230830_1417.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0035_account_address.py](pitupi/money/migrations/0035_account_address.py)                                                                                                           | <code>► INSERT-TEXT-HERE</code> |
| [0014_card_last_deposit_at_card_last_withdraw_at_and_more.py](pitupi/money/migrations/0014_card_last_deposit_at_card_last_withdraw_at_and_more.py)                                   | <code>► INSERT-TEXT-HERE</code> |
| [0047_remove_tradersettings_bank_and_more.py](pitupi/money/migrations/0047_remove_tradersettings_bank_and_more.py)                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0011_provider_supplier_rename_bank_deposit_issuer_and_more.py](pitupi/money/migrations/0011_provider_supplier_rename_bank_deposit_issuer_and_more.py)                               | <code>► INSERT-TEXT-HERE</code> |
| [0054_clientgroup_account_is_verified_client_group_set.py](pitupi/money/migrations/0054_clientgroup_account_is_verified_client_group_set.py)                                         | <code>► INSERT-TEXT-HERE</code> |
| [0018_account_remove_client_master_client_telegram_id_and_more.py](pitupi/money/migrations/0018_account_remove_client_master_client_telegram_id_and_more.py)                         | <code>► INSERT-TEXT-HERE</code> |
| [0055_trader.py](pitupi/money/migrations/0055_trader.py)                                                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0078_merge_20230814_1918.py](pitupi/money/migrations/0078_merge_20230814_1918.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0093_alter_deposit_options_alter_withdraw_options_and_more.py](pitupi/money/migrations/0093_alter_deposit_options_alter_withdraw_options_and_more.py)                               | <code>► INSERT-TEXT-HERE</code> |
| [0023_alter_card_status.py](pitupi/money/migrations/0023_alter_card_status.py)                                                                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0087_alter_tradersetting_amount_done_and_more.py](pitupi/money/migrations/0087_alter_tradersetting_amount_done_and_more.py)                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0031_auto_20230510_1836.py](pitupi/money/migrations/0031_auto_20230510_1836.py)                                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0082_auto_20230822_1802.py](pitupi/money/migrations/0082_auto_20230822_1802.py)                                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0015_proxysupplier_gate_is_turbo_proxy_visit_proxy.py](pitupi/money/migrations/0015_proxysupplier_gate_is_turbo_proxy_visit_proxy.py)                                               | <code>► INSERT-TEXT-HERE</code> |
| [0097_card_device_id_card_online_at.py](pitupi/money/migrations/0097_card_device_id_card_online_at.py)                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0111_rename_transcation_count_limit_card_transaction_count_limit_and_more.py](pitupi/money/migrations/0111_rename_transcation_count_limit_card_transaction_count_limit_and_more.py) | <code>► INSERT-TEXT-HERE</code> |
| [0030_auto_20230510_1835.py](pitupi/money/migrations/0030_auto_20230510_1835.py)                                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0121_alter_client_full_name.py](pitupi/money/migrations/0121_alter_client_full_name.py)                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0115_client_user.py](pitupi/money/migrations/0115_client_user.py)                                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0019_rename_flow_deposit_method_and_more.py](pitupi/money/migrations/0019_rename_flow_deposit_method_and_more.py)                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0076_alter_deposit_method_alter_withdraw_method.py](pitupi/money/migrations/0076_alter_deposit_method_alter_withdraw_method.py)                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0006_deposit_pre_status_visit_callback_at_and_more.py](pitupi/money/migrations/0006_deposit_pre_status_visit_callback_at_and_more.py)                                               | <code>► INSERT-TEXT-HERE</code> |
| [0120_alter_client_withdraw_priority.py](pitupi/money/migrations/0120_alter_client_withdraw_priority.py)                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0101_merge_20231002_1921.py](pitupi/money/migrations/0101_merge_20231002_1921.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0094_merge_20230901_1622.py](pitupi/money/migrations/0094_merge_20230901_1622.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0038_receipt_withdraw_withdraw_asignee_and_more.py](pitupi/money/migrations/0038_receipt_withdraw_withdraw_asignee_and_more.py)                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0083_remove_tradersettings_bank_setting.py](pitupi/money/migrations/0083_remove_tradersettings_bank_setting.py)                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0036_card_currency.py](pitupi/money/migrations/0036_card_currency.py)                                                                                                               | <code>► INSERT-TEXT-HERE</code> |
| [0028_merge_20230505_1427.py](pitupi/money/migrations/0028_merge_20230505_1427.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0070_alter_deposit_assignee_alter_withdraw_assignee.py](pitupi/money/migrations/0070_alter_deposit_assignee_alter_withdraw_assignee.py)                                             | <code>► INSERT-TEXT-HERE</code> |
| [0016_deposit_user_agent_visit_browser_agent_and_more.py](pitupi/money/migrations/0016_deposit_user_agent_visit_browser_agent_and_more.py)                                           | <code>► INSERT-TEXT-HERE</code> |
| [0090_delete_clientdeposit_delete_clientmanager_and_more.py](pitupi/money/migrations/0090_delete_clientdeposit_delete_clientmanager_and_more.py)                                     | <code>► INSERT-TEXT-HERE</code> |
| [0084_remove_tradersettings_bank_settings_and_more.py](pitupi/money/migrations/0084_remove_tradersettings_bank_settings_and_more.py)                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0075_alter_deposit_success_trigger_and_more.py](pitupi/money/migrations/0075_alter_deposit_success_trigger_and_more.py)                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0110_card_max_amount_limit_card_transcation_count_limit_and_more.py](pitupi/money/migrations/0110_card_max_amount_limit_card_transcation_count_limit_and_more.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [0106_merge_20231114_1638.py](pitupi/money/migrations/0106_merge_20231114_1638.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0095_merge_20230923_1619.py](pitupi/money/migrations/0095_merge_20230923_1619.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0024_alter_account_sub_id.py](pitupi/money/migrations/0024_alter_account_sub_id.py)                                                                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0025_alter_client_name_alter_client_telegram_id.py](pitupi/money/migrations/0025_alter_client_name_alter_client_telegram_id.py)                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0098_alter_card_online_at.py](pitupi/money/migrations/0098_alter_card_online_at.py)                                                                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0017_alter_visit_deposit.py](pitupi/money/migrations/0017_alter_visit_deposit.py)                                                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0086_rename_tradersettings_tradersetting.py](pitupi/money/migrations/0086_rename_tradersettings_tradersetting.py)                                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0046_rename_online_account_deposit_online.py](pitupi/money/migrations/0046_rename_online_account_deposit_online.py)                                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0040_alter_operationlog_deposit.py](pitupi/money/migrations/0040_alter_operationlog_deposit.py)                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0046_clientwithdraw_deposit_external_id_and_more.py](pitupi/money/migrations/0046_clientwithdraw_deposit_external_id_and_more.py)                                                   | <code>► INSERT-TEXT-HERE</code> |
| [0058_receipt_bank_from_receipt_card_from_receipt_data_and_more.py](pitupi/money/migrations/0058_receipt_bank_from_receipt_card_from_receipt_data_and_more.py)                       | <code>► INSERT-TEXT-HERE</code> |
| [0050_alter_deposit_method_alter_withdraw_method.py](pitupi/money/migrations/0050_alter_deposit_method_alter_withdraw_method.py)                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0043_remove_withdraw_asignee_withdraw_assignee.py](pitupi/money/migrations/0043_remove_withdraw_asignee_withdraw_assignee.py)                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0051_auto_20230620_1511.py](pitupi/money/migrations/0051_auto_20230620_1511.py)                                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0026_alter_account_currency.py](pitupi/money/migrations/0026_alter_account_currency.py)                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0065_merge_0064_notificationapp_smsapp_0064_toptrader.py](pitupi/money/migrations/0065_merge_0064_notificationapp_smsapp_0064_toptrader.py)                                         | <code>► INSERT-TEXT-HERE</code> |
| [0119_client_withdraw_priority.py](pitupi/money/migrations/0119_client_withdraw_priority.py)                                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0056_receipt_withdraw_group_id_withdraw_withdraw_group_id.py](pitupi/money/migrations/0056_receipt_withdraw_group_id_withdraw_withdraw_group_id.py)                                 | <code>► INSERT-TEXT-HERE</code> |
| [0066_delete_notificationapp_delete_smsapp_and_more.py](pitupi/money/migrations/0066_delete_notificationapp_delete_smsapp_and_more.py)                                               | <code>► INSERT-TEXT-HERE</code> |
| [0032_operationlog.py](pitupi/money/migrations/0032_operationlog.py)                                                                                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0044_withdraw_kind_alter_withdraw_assignee_tradersettings.py](pitupi/money/migrations/0044_withdraw_kind_alter_withdraw_assignee_tradersettings.py)                                 | <code>► INSERT-TEXT-HERE</code> |
| [0027_setting_alter_account_created_at_and_more.py](pitupi/money/migrations/0027_setting_alter_account_created_at_and_more.py)                                                       | <code>► INSERT-TEXT-HERE</code> |
| [0069_deposit_assignee_alter_deposit_pre_status_and_more.py](pitupi/money/migrations/0069_deposit_assignee_alter_deposit_pre_status_and_more.py)                                     | <code>► INSERT-TEXT-HERE</code> |
| [0067_notificationapp_smsapp_toptrader.py](pitupi/money/migrations/0067_notificationapp_smsapp_toptrader.py)                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0004_alter_visit_error_desc.py](pitupi/money/migrations/0004_alter_visit_error_desc.py)                                                                                             | <code>► INSERT-TEXT-HERE</code> |
| [0113_account_max_withdraw_order_count.py](pitupi/money/migrations/0113_account_max_withdraw_order_count.py)                                                                         | <code>► INSERT-TEXT-HERE</code> |
| [0029_currency_remove_account_denominator_and_more.py](pitupi/money/migrations/0029_currency_remove_account_denominator_and_more.py)                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0105_alter_c2ctradecard_options_alter_c2ctradecard_card_and_more.py](pitupi/money/migrations/0105_alter_c2ctradecard_options_alter_c2ctradecard_card_and_more.py)                   | <code>► INSERT-TEXT-HERE</code> |
| [0068_notificationapp_amount_notificationapp_bank_and_more.py](pitupi/money/migrations/0068_notificationapp_amount_notificationapp_bank_and_more.py)                                 | <code>► INSERT-TEXT-HERE</code> |
| [0037_deposit_data_withdraw_data.py](pitupi/money/migrations/0037_deposit_data_withdraw_data.py)                                                                                     | <code>► INSERT-TEXT-HERE</code> |
| [0074_deposit_success_trigger_withdraw_deposit_and_more.py](pitupi/money/migrations/0074_deposit_success_trigger_withdraw_deposit_and_more.py)                                       | <code>► INSERT-TEXT-HERE</code> |
| [0073_clientdeposit.py](pitupi/money/migrations/0073_clientdeposit.py)                                                                                                               | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.money.fixtures</summary>

| File                                                         | Summary                         |
| ---                                                          | ---                             |
| [mdl_currency.json](pitupi/money/fixtures/mdl_currency.json) | <code>► INSERT-TEXT-HERE</code> |
| [banks.json](pitupi/money/fixtures/banks.json)               | <code>► INSERT-TEXT-HERE</code> |
| [bank_setting.json](pitupi/money/fixtures/bank_setting.json) | <code>► INSERT-TEXT-HERE</code> |
| [currencies.json](pitupi/money/fixtures/currencies.json)     | <code>► INSERT-TEXT-HERE</code> |
| [test_users.json](pitupi/money/fixtures/test_users.json)     | <code>► INSERT-TEXT-HERE</code> |
| [settings.json](pitupi/money/fixtures/settings.json)         | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.templates.admin</summary>

| File                                                        | Summary                         |
| ---                                                         | ---                             |
| [search_form.html](pitupi/templates/admin/search_form.html) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.pitupi</summary>

| File                                     | Summary                         |
| ---                                      | ---                             |
| [asgi.py](pitupi/pitupi/asgi.py)         | <code>► INSERT-TEXT-HERE</code> |
| [wsgi.py](pitupi/pitupi/wsgi.py)         | <code>► INSERT-TEXT-HERE</code> |
| [settings.py](pitupi/pitupi/settings.py) | <code>► INSERT-TEXT-HERE</code> |
| [urls.py](pitupi/pitupi/urls.py)         | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.turbo</summary>

| File                                | Summary                         |
| ---                                 | ---                             |
| [views.py](pitupi/turbo/views.py)   | <code>► INSERT-TEXT-HERE</code> |
| [apps.py](pitupi/turbo/apps.py)     | <code>► INSERT-TEXT-HERE</code> |
| [tests.py](pitupi/turbo/tests.py)   | <code>► INSERT-TEXT-HERE</code> |
| [admin.py](pitupi/turbo/admin.py)   | <code>► INSERT-TEXT-HERE</code> |
| [models.py](pitupi/turbo/models.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.turbo.migrations</summary>

| File                                                                                                                       | Summary                         |
| ---                                                                                                                        | ---                             |
| [0004_useragent_headers_alter_useragent_gibfp.py](pitupi/turbo/migrations/0004_useragent_headers_alter_useragent_gibfp.py) | <code>► INSERT-TEXT-HERE</code> |
| [0001_initial.py](pitupi/turbo/migrations/0001_initial.py)                                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0003_alter_useragent_gibfp.py](pitupi/turbo/migrations/0003_alter_useragent_gibfp.py)                                     | <code>► INSERT-TEXT-HERE</code> |
| [0002_proxysupplier_proxy.py](pitupi/turbo/migrations/0002_proxysupplier_proxy.py)                                         | <code>► INSERT-TEXT-HERE</code> |
| [0005_useragent_status.py](pitupi/turbo/migrations/0005_useragent_status.py)                                               | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.cli</summary>

| File                              | Summary                         |
| ---                               | ---                             |
| [views.py](pitupi/cli/views.py)   | <code>► INSERT-TEXT-HERE</code> |
| [apps.py](pitupi/cli/apps.py)     | <code>► INSERT-TEXT-HERE</code> |
| [tests.py](pitupi/cli/tests.py)   | <code>► INSERT-TEXT-HERE</code> |
| [admin.py](pitupi/cli/admin.py)   | <code>► INSERT-TEXT-HERE</code> |
| [models.py](pitupi/cli/models.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pitupi.cli.migrations</summary>

| File                                                                                                               | Summary                         |
| ---                                                                                                                | ---                             |
| [0005_clientclient.py](pitupi/cli/migrations/0005_clientclient.py)                                                 | <code>► INSERT-TEXT-HERE</code> |
| [0004_clientdepositmanager.py](pitupi/cli/migrations/0004_clientdepositmanager.py)                                 | <code>► INSERT-TEXT-HERE</code> |
| [0007_alter_clientclient_options.py](pitupi/cli/migrations/0007_alter_clientclient_options.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [0001_initial.py](pitupi/cli/migrations/0001_initial.py)                                                           | <code>► INSERT-TEXT-HERE</code> |
| [0002_clientsetting.py](pitupi/cli/migrations/0002_clientsetting.py)                                               | <code>► INSERT-TEXT-HERE</code> |
| [0003_merge_20230901_1622.py](pitupi/cli/migrations/0003_merge_20230901_1622.py)                                   | <code>► INSERT-TEXT-HERE</code> |
| [0006_alter_clientclient_options.py](pitupi/cli/migrations/0006_alter_clientclient_options.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [0002_alter_clientdeposit_options_and_more.py](pitupi/cli/migrations/0002_alter_clientdeposit_options_and_more.py) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>piapi</summary>

| File                                       | Summary                         |
| ---                                        | ---                             |
| [app.py](piapi/app.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [Dockerfile](piapi/Dockerfile)             | <code>► INSERT-TEXT-HERE</code> |
| [requirements.txt](piapi/requirements.txt) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>clickhouse</summary>

| File                                    | Summary                         |
| ---                                     | ---                             |
| [logtable.sql](clickhouse/logtable.sql) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>manager</summary>

| File                                                 | Summary                         |
| ---                                                  | ---                             |
| [config.py](manager/config.py)                       | <code>► INSERT-TEXT-HERE</code> |
| [common.py](manager/common.py)                       | <code>► INSERT-TEXT-HERE</code> |
| [Dockerfile](manager/Dockerfile)                     | <code>► INSERT-TEXT-HERE</code> |
| [fpg.py](manager/fpg.py)                             | <code>► INSERT-TEXT-HERE</code> |
| [base.py](manager/base.py)                           | <code>► INSERT-TEXT-HERE</code> |
| [manager.py](manager/manager.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [kasha.py](manager/kasha.py)                         | <code>► INSERT-TEXT-HERE</code> |
| [syncaccounts.py](manager/syncaccounts.py)           | <code>► INSERT-TEXT-HERE</code> |
| [requirements.txt](manager/requirements.txt)         | <code>► INSERT-TEXT-HERE</code> |
| [withdraw_matching.py](manager/withdraw_matching.py) | <code>► INSERT-TEXT-HERE</code> |
| [utils.py](manager/utils.py)                         | <code>► INSERT-TEXT-HERE</code> |
| [models.py](manager/models.py)                       | <code>► INSERT-TEXT-HERE</code> |
| [deposit_matching.py](manager/deposit_matching.py)   | <code>► INSERT-TEXT-HERE</code> |
| [gate_routing.py](manager/gate_routing.py)           | <code>► INSERT-TEXT-HERE</code> |
| [sms.py](manager/sms.py)                             | <code>► INSERT-TEXT-HERE</code> |
| [enums.py](manager/enums.py)                         | <code>► INSERT-TEXT-HERE</code> |
| [chouse.py](manager/chouse.py)                       | <code>► INSERT-TEXT-HERE</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the . repository:
>
> ```console
> $ git clone ../.
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd .
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run . using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://local//issues)**: Submit bugs found or log feature requests for the `.` project.
- **[Submit Pull Requests](https://local//blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://local//discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone ../.
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://local{//}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
