---
title: How to listen new tables in Etendo RX
---

## Overview

This page explain how to setup Debezium and listen a specific table and fields in Etendo Rx environment.

## How to listen new tables in Etendo RX - Debezium UI

!!! info
    To follow this guide you must have an EtendoRx environment with Debezium and Kafka servises runing. To more information read [EtendoRx](https://docs/en/technical-documentation/etendo-environment/platform/EtendoRx).  

1. **Debezium UI**: This application offers a user interface to configure all the properties that we need to listen to the tables that we need. With docker started, we access to [_http://localhost:8095/_](http://localhost:8095/).

2. To create a new connector, click on Create a connector button.

![](/docs/assets/drive/aJzitIXqJbubWW8GARdErE46voV8KjmGcf2v00hQBmGUrTbhL81J4GoeyoTFhhBZ4xiIOrQiP6Yhd99gOZbg8sga4l54BE11ssioAvRldAq-ViG43SMV2WoYEj4AZT77cZL_J2LTIoKyZYeAtg.png)

3. Select PostgreSQL and click on Next button.

![](/docs/assets/drive/AMPZS3Vby4NP9i40khwsXUzOa2jXcCJRIxBqR4B5Q39Tu4ELWRu2TJXA4Gr28nvYinpCIll-v-hcDVeJSQ2khtmOQ6kzziXKyM-yDe94UdkSQWd5KUl2T71elJDy_Tfzdfi7kDxckVezqZdeWw.png)

4. A basic configuration needs the following:

![](/docs/assets/drive/iGY8RsjNAaEK6NsWSqaAE7DtFfFO-h3HOTNi14cniswQJcB3upduzM7iHtIkhD2_Wl5J13KpiBSWXhraX_nubdQg0EsaKXpHSMlXWfVUM67eTnFBLTPrPKUccAqRoFDp0DixbD2HHHGdauQw5Q.png)

- **Connector name**: A name of connector. Whatever you want to use.
- **Namespace**: default.
- **Hostname**: postgres. Because we called it in the docker compose file.
- **Port**: 5432.
- **User**: postgres.
- **Password**: syspass.
- **Database**: etendo.

5. Once we filled all mandatory fields, we needed to validate the data, so click on the Validate button. We should see a success message like this:

![](/docs/assets/drive/43UN2abdTb_x4vkSjotWUAomawnIgtJp-V7c_Xiw9pkTk2AUvgQYuSXaV9OrWSj2Ni-HTpBhGZ8JkvWEmPkrdtrp0JyI6CED24iBl8nW1DCobBsP0ZXB-0wb8DOPOGzX1Qk1AGE6m_5sxoC6cw.png)

6. Click on the Next button and on the next screen, we need to decide which tables we want to listen to. By default, all tables will be listened to.

![](/docs/assets/drive/sNYtCQLE0xE9y3Gg-iQaNimGbG21f_EK3O-PPae8SqJ9uQ7LkeaRaaXnH1XA85grFNpSXU4YKliN9-Yv8mDjxHXjweTxaRhN10gbtd3D55-Z2ktPN8K-goEcGgncDydvFGWIX9CAKRl9GcuE2A.png)

7. If we decide to listen to only some tables, we need to lookup the table in the input Table Filter and apply the filter. For this example, I need to listen to c_bpartner_location table only

![debezium-setup.png](/docs/assets/legacy/technicaldocumentation/platform/debezium-setup.png)

8. Once we finish with this configuration, we need to validate all configurations. For it, click on the Review and Finish button.

9. If all it is fine, then we get the following screen:

![](/docs/assets/drive/KN41JFvZb7YA2Er6wHiM3rcbp1r90WRmtDkMHADxhUSEknU7TR6qVb3DP1ukTrjlPRVrqVQXJJ2nhqj9861DYMHq88FRDHGGhn1X9U0by2iaejGeRjoa6cBmvLIKChTRVaYPt8BYwQ0MfPrTzw.png)

10. Finally, we press on the Finish button in order to create the connector.

![](/docs/assets/drive/gtfy5r9_ohJjCHsISAU5p0GqItRPbG-U_7Ih1h1uIC1wUxl3rJC3ataZfQEuOvtdpAEOIkTvmLxctK6aYq8_kpWNwtHIr_HwKTV7HfMzH4xGY_ffqRcCZPrdL8ZHnnVJ5Ue-wn8JJR9oadZtIw.png)
