---
title: Installation - Connecting Openbravo POS and Etendo
tags:
    - Connector
    - Openbravo
    - POS Terminal
    - Etendo Classic
    - Etendo RX 
    - Environment Synk
---


# Installation: Connecting Openbravo POS and Etendo

## Overview
This guide provides step-by-step instructions to install and configure the integration between Openbravo and Etendo environments. This setup allows you to generate documents in Openbravo POS Terminal, store them in the Openbravo environment and synchronize them with Etendo using Etendo RX as middleware.

In this guide we will start from two clean environments using test data, which facilitates the configuration and demonstrates the potential of this integration.

!!! info 
    This guide is based on Openbravo 24Q4 and Etendo 24.4.0

## Required Software and Tools
- [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community or Ultimate Edition)
- [Eclipse](https://eclipseide.org/){target="_blank"}
- [Apache Tomcat](https://tomcat.apache.org/){target="_blank"}
- [Docker Desktop](https://www.docker.com/products/docker-desktop/){target="_blank"}
- [Openbravo 24Q4](https://gitlab.com/orisha-group/bu-commerce/openbravo/product/openbravo) or later
- [Etendo Classic 24.4.0](../../../../whats-new/release-notes/etendo-classic/release-notes.md) or later
- [Platform Extensions Bundle ](../../../../whats-new/release-notes/etendo-classic/bundles/platform-extensions/release-notes.md) latest version installed in Etendo.

## Openbravo

First, follow the [Openbravo Custom Installation Guide](https://wiki.openbravo.com/wiki/Installation/Custom){target="_blank"} and install in a local environment following [How to setup Eclipse IDE](https://wiki.openbravo.com/wiki/How_to_setup_Eclipse_IDE){target="_blank"}.  

### Modules to Install on Openbravo

In the Openbravo environment we need to install the Retail POS, EDL and Business API modules.

To obtain these modules, an active Openbravo License and access to the Openbravo Forge are required. Ensure that the Openbravo environment includes the following modules in versions compatible with the corresponding Openbravo Core version. In this example, the modules will be used in version 24Q4.

- `org.openbravo.retail.sampledata`
- `org.openbravo.retail.returns`
- `org.openbravo.retail.posterminal`
- `org.openbravo.retail.poshwmanager`
- `org.openbravo.retail.pack`
- `org.openbravo.retail.discounts`
- `org.openbravo.retail.config`
- `org.openbravo.mobile.core`
- `org.openbravo.events.core`
- `org.openbravo.api`
- `org.openbravo.service.openapi`
- `org.openbravo.service.external.integration`
- `org.openbravo.externaldata.integration`

!!! warning
    Is necesary to apply a change in the `modules/org.openbravo.api/src/org/openbravo/api/util/ApiUtils.java` file  in line 38 reeplace by: 

    ```java
        Matcher m = Pattern.compile("(^|[^\\\\]{2}):{1}([a-zA-Z0-9_]+)").matcher(hqlWhereClause);
    ```

Also, you must clone the Openbravo-Etendo connector modules, to do that Partner access level is required :

```bash
git clone git@github.com:etendosoftware/com.etendoerp.integration.openbravo.git --branch 1.0.0
git clone git@github.com:etendosoftware/com.etendoerp.integration.openbravo.template.git --branch 1.0.0
```

### Set Up the Openbravo Environment
Run the following commands to set up the Openbravo environment:

```bash title="Terminal"
ant setup
ant install.sources
ant smartbuild
```

Configurar Tomcat para correr en el puerto `8081` ya que el puerto `8080` estará ocupado por Etendo, luego reiniciar Tomcat.  


### Master Data Configuration

Luego, para simplificar la configuracion haremos algunos inserts en base de datos con configuraciones en Openbravo, para ello nos podemos conectar desde PGAdmin o bien por linea de comandos. 

```bash title="Terminal"
PGPASSWORD=tad  psql -U tad  -d openbravo -h localhost -p 5432
```

```SQL title="Setup Script"

INSERT INTO public.c_external_system(c_external_system_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, description, connectivity_process, name, ad_protocol_id)
    VALUES('73159A3D97824F07ABB4176F2D514F7D','0','0','Y','2024-05-16 08:12:58.295','0','2024-05-16 08:12:58.295','0',NULL,'N','OB Connector','36ADC30F67164F119013515280D82C01');
INSERT INTO public.c_external_system_http(c_external_system_http_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, c_external_system_id, url, authorization_type, username, password, request_method, timeout, oauth2_client_identifier, oauth2_client_secret, oauth2_auth_server_url, em_etint_token)
    VALUES ('EC60C5CF35234C648D9B5B00015190E2','0','0','Y','2024-03-12 10:02:38.42','100','2024-12-18 12:03:21.298','100','73159A3D97824F07ABB4176F2D514F7D','http://localhost:8096','ETINT_X-TOKEN',NULL,NULL,'POST',10,NULL,NULL,NULL,'eyJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJzd3MiLCJyb2xlIjoiRTcxN0Y5MDJDNDRDNDU1NzkzNDYzNDUwNDk1RkYzNkIiLCJvcmdhbml6YXRpb24iOiIwIiwiaXNzIjoic3dzIiwiY2xpZW50IjoiMzkzNjNCMDkyMUJCNDI5M0I0ODM4Mzg0NDMyNUU4NEMiLCJ3YXJlaG91c2UiOiI0RDQ1RkU0QzUxNTA0MTcwOTA0N0Y1MUQxMzlBMjFBQyIsInVzZXIiOiJFOEFEOUIyNkI3RDE0Nzg2OEI2OEE5NTAwQ0M3NkRERCIsImlhdCI6MTczNzE0MzkyM30.MEYCIQDvVJXsg-6stuky6l93cdpM_jsgu5VHDRFh81iUTK0zigIhAJb6Ha2-EnGsb9RrcBsmMPzjJ2-cAYonuuYmfF3YJG3w');
INSERT INTO public.cnc_events_subs (cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('10F0532FC9074E80923C02AA50234437','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 09:00:50.672','100','2024-05-16 09:00:50.672','100','4CABD83993ED4DD185354B826CF282AB','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('19299136996A41A188FDF0EBA613439C','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 08:59:57.049','100','2024-05-16 08:59:57.049','100','EC44C2BF556F4DE5936F77032CFFEDFA','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('41E108F4B4324D93A3822452FC28EAE2','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 08:59:45.106','100','2024-05-16 08:59:45.106','100','D4220C11026E4BCEB9F5C9E6986E3027','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('74411877488542F9A29E1A62AE9A3095','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 09:00:18.521','100','2024-05-16 09:00:18.521','100','C8846AB5E6D64201AEB1D8BDDFD1FCB8','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('8D9B45DED9154D12BB59FC61881DF504','39363B0921BB4293B48383844325E84C','0','Y','2024-12-18 16:14:12.695','100','2024-12-18 16:14:12.695','100','1E9960A3751E42BE9C295F659BF31481','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('9B196742FCBF438AB0F993CCEB0FD128','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 09:01:35.509','100','2024-05-16 09:01:35.509','100','9A827B001D82408D90DA622E6860EC1C','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('B30C7FAA3FE849568C7DFD7B6463A89B','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 09:01:26.548','100','2024-05-16 09:01:26.548','100','60F1B0A744904709A5BEC2D3163CB0F5','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('D1DFB1E5ACC1482097D2BDF79810B6C5','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 09:00:32.893','100','2024-05-16 09:00:32.893','100','EE70B36B9755410289137250E4CA3F49','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.cnc_events_subs(cnc_events_subs_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, cnc_public_events_id, em_api_c_external_system_id)
    VALUES ('FADDA04F4AF54C41B16F13F111834488','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 09:00:07.792','100','2024-05-16 09:00:07.792','100','C999B37599FA4705A110BEA8F358372A','73159A3D97824F07ABB4176F2D514F7D');
INSERT INTO public.obedl_configuration(obedl_configuration_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, obedl_process_id)
    VALUES ('B1F00DAB0FEC4C549AF0068E77492638','39363B0921BB4293B48383844325E84C','0','Y','2024-12-20 11:22:20.267','100','2024-12-20 11:22:20.267','100','9B8E4B855B7E41EB87EE37D3394B7AD2');
INSERT INTO public.obedl_config_output(obedl_config_output_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, seqno, output_path, output_user, output_pass, output_filename, obedl_configuration_id, obedl_output_type_id, wsmethod, isretryenabled, maxretry, retryinterval, timeout)
    VALUES ('EE980DAA10CA40B78547056656192F76','39363B0921BB4293B48383844325E84C','0','Y','2024-12-20 11:22:38.946','100','2024-12-20 11:22:38.946','100',10,NULL,NULL,NULL,NULL,'B1F00DAB0FEC4C549AF0068E77492638','BF9649DF97A14168A4C142222E2CBF0C',NULL,'N',NULL,NULL,5);
INSERT INTO public.ad_preference(ad_preference_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, ad_window_id, ad_user_id, attribute, value, property, ispropertylist, visibleat_client_id, visibleat_org_id, visibleat_role_id, selected, ad_module_id, inherited_from)
    VALUES ('BAB39C0A1E2D49CB85C150677CBA9C3F','39363B0921BB4293B48383844325E84C','0','Y','2024-05-16 12:41:34.285','100','2024-05-16 12:41:34.285','100',NULL,'100',NULL,'Y','ETINT_DefaultSyncValue','Y',NULL,NULL,NULL,'N',NULL,NULL);
INSERT INTO public.ad_preference(ad_preference_id, ad_client_id, ad_org_id, isactive, created, createdby, updated, updatedby, ad_window_id, ad_user_id, attribute, value, property, ispropertylist, visibleat_client_id, visibleat_org_id, visibleat_role_id, selected, ad_module_id, inherited_from)
    VALUES ('36675A275AC2478C83AB05771EAA23A5','39363B0921BB4293B48383844325E84C','D270A5AC50874F8BA67A88EE977F8E3B','Y','2024-05-23 18:04:26.01','3073EDF96A3C42CC86C7069E379522D2','2024-05-27 10:48:48.382','100',null,null,null,'Y','ETINT_DefaultSyncValue','Y',null,null,null,'Y',null,null);
DELETE FROM ad_role_orgaccess WHERE ad_client_id='39363B0921BB4293B48383844325E84C';
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('00E25567B08143EEB0218D4539268FFD','4AF94371114B4125877650274C245C5D','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','N','2023-10-11 11:59:33.521','100','2023-10-11 11:59:33.521','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('05E6998CD5B44072809EC2D8DC89810C','FF808181259DADEB01259DDDA4BB01E5','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:48.42','100','2016-05-10 17:33:48.42','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('06F04F083ABA408499DA19988FBAAB8C','FF808181259DADEB01259DDDA4C201E6','67839EEFA49E44AC969BD60093FCC899','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('070EB80EFFB945998F16D69825225A54','898E1715D1DF4C15A9CBE0813F23F892','E2A8087A81F54203969C6AED1AABBC72','39363B0921BB4293B48383844325E84C','Y','2019-02-08 00:33:00.243','100','2019-02-08 00:33:00.243','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('0B8FB016F525412E8F51A3041F022DED','45A63D86E04D4052A3E8D04ABCC17E1E','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2017-01-26 13:41:31.129','100','2017-01-26 13:41:31.129','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('0C6E8B1A5F7A46639ADDEDE817E59DB6','FF8081812250326E012250353BDE0006','BF129721D9FB4EB0819509934153E972','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('0C8EB7C3DF964C91922987E6A525A855','FF808181259DADEB01259DDDA4C201E6','4399136852B145BD96CC2A6CE0800C68','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('0E212E2128B34AC18969896B1642074B','FF808181259DADEB01259DDDA4C201E6','01AD882EFC8545ACA6455E2F6FD51EE9','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('0F73E3802207447A965055B702DAF36D','D7D7D228E4594ACE8D00FD0E08B333DE','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('145D57C3347D4F32B21EE04DC3993A2B','463683CFA16C40C0A4EC8CF934114146','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('15B90797F244416AB8F4DC181DA7BC2B','463683CFA16C40C0A4EC8CF934114146','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('1A9D803990FA42058D41EE0995AD9DE3','FF8081812250326E012250353BDE0006','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('1EFCD742FDD94113A8BC9D51651ACB42','463683CFA16C40C0A4EC8CF934114146','4399136852B145BD96CC2A6CE0800C68','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('204B559EFBF94116AF0558C428FEF5C3','D7D7D228E4594ACE8D00FD0E08B333DE','01AD882EFC8545ACA6455E2F6FD51EE9','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('21C7FA46793B4C8A8120D96FF8EFF68C','463683CFA16C40C0A4EC8CF934114146','14B1927026BE471E9B85FE699BCA61C2','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('24CFC72398FC400FB70B427A4B37D275','28D1AFB16B7C4B69B4C8026C16BF88F6','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2018-07-16 09:45:00.77','100','2018-07-16 09:45:00.77','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('27FB52278FD8499E859885BBBA81469D','FF808181259DADEB01259DDDA4BB01E5','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:32:17.675','100','2016-05-10 17:32:17.675','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('310886C13CEF4618B4854F796E297CEA','D7D7D228E4594ACE8D00FD0E08B333DE','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('37CBB9594B014AF098B8CAF10316B00C','FF8081812250326E012250353BDE0006','01AD882EFC8545ACA6455E2F6FD51EE9','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('38688BD551FA4718BD865FE8D4EA3FA7','FF808181259DADEB01259DDDA4BB01E5','14B1927026BE471E9B85FE699BCA61C2','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:12.588','100','2016-05-10 17:33:12.588','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('3AA4B571EBDA4757B30E59B19A28752B','FF808181259DADEB01259DDDA4C201E7','DF86640764AA4492AB6D4CA2D432B8D4','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:05:39.566','100','2016-09-05 19:05:39.566','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('3AED4DB65F374ED09558D3B2BC2D2FAD','D7D7D228E4594ACE8D00FD0E08B333DE','14B1927026BE471E9B85FE699BCA61C2','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('3FB7C8A13A954ED9B5AF469FFAD769CD','FF808181259DADEB01259DDDA4C201E6','102D0E6D37DA46C3BABA6DFF3708F341','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('43CFCE1377B046659E5C75B3C9A67447','E0E04AEBED4F497B98821315A039FAE0','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','Y',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('454CFB3140DA4FFEA6247835FC8A8C9D','FF808181259DADEB01259DDDA4C201E7','0','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:05:21.172','100','2016-09-05 19:05:21.172','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('471CD13FA7024D2CAC8A23B7492EAB8D','FF808181259DADEB01259DDDA4C201E6','BF129721D9FB4EB0819509934153E972','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('49CA2A40287E400DA0D8CAC3B5A6C7BA','FF808181259DADEB01259DDDA4C201E7','102D0E6D37DA46C3BABA6DFF3708F341','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:05:49.47','100','2016-09-05 19:05:49.47','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('4E087E72C4BC49C3A28FE2EB88FC5560','FF808181259DADEB01259DDDA4C201E6','0','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('4E6BA6809674438DADBA699E91A2F4A1','D7D7D228E4594ACE8D00FD0E08B333DE','4399136852B145BD96CC2A6CE0800C68','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('533DACF943EA4C68939C2F00EACBBC92','F539FCE19DD744DEA5BFD9387E61EB42','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2015-10-08 12:40:03.398','100','2015-10-08 12:40:03.398','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('53979ED48C834DD69162C1B390D5C0AA','FF808181259DADEB01259DDDA4BB01E5','0','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:32:00.203','100','2016-05-10 17:32:00.203','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('539B9A17F57F4298B07EDA0DA9791CC0','FF8081812250326E012250353BDE0006','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('53A6D8FFA4C84A8C93F6CDC83B00A7B3','5FA11B3DD8F04C0986C774624809C31E','0','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('551489F6FFB841FFB6A851C9253CEB66','463683CFA16C40C0A4EC8CF934114146','67839EEFA49E44AC969BD60093FCC899','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('56402FE8BD5449EC9244A6AC08AB7F90','4AF94371114B4125877650274C245C5D','65C1C46FB1D04CBD98CBD4167CCFE600','39363B0921BB4293B48383844325E84C','Y','2019-02-07 18:01:06.808','100','2019-02-07 18:01:06.808','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('595C29533DAA4E59AB71FBEFD9D10AEA','E717F902C44C455793463450495FF36B','0','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.048','0','2013-07-04 23:01:15.048','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('5A59133E18CE476AB489FA0EC51ACBF2','FF808181259DADEB01259DDDA4C201E7','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:05:45.382','100','2016-09-05 19:05:45.382','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('5F31E242A9BB4BD18CB7E5B496A858D7','FF808181259DADEB01259DDDA4C201E6','14B1927026BE471E9B85FE699BCA61C2','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('5FF9AAB3C384462D8E812DF4C1B5E35A','D7D7D228E4594ACE8D00FD0E08B333DE','102D0E6D37DA46C3BABA6DFF3708F341','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('6899F9065C3F4A18B46FC78DAFF0442B','FF808181259DADEB01259DDDA4BB01E5','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:17.069','100','2016-05-10 17:33:17.069','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('69F88418E80D4747BE967690EA0EC454','FF808181259DADEB01259DDDA4C201E7','687AD71263F94A31B85A3CC9942FF7ED','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:05:53.711','100','2016-09-05 19:05:53.711','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('6F9D0F236DFB42E6BE596C4569DCD58B','FF808181259DADEB01259DDDA4BB01E5','67839EEFA49E44AC969BD60093FCC899','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:43.374','100','2016-05-10 17:33:43.374','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('734B0E318B7C488196F9FF57DD409D40','FF8081812250326E012250353BDE0006','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('7420FFCA3DD94FA08754F1C309164C10','FF8081812250326E012250353BDE0006','102D0E6D37DA46C3BABA6DFF3708F341','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('78D4E9A3C23B494DB2236F0667A6B567','FF808181259DADEB01259DDDA4C201E7','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:06:29.563','100','2016-09-05 19:06:29.563','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('7944BC0FC2E246EAB81DAC10BA66C3DF','FF8081812250326E012250353BDE0006','4399136852B145BD96CC2A6CE0800C68','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('832EF36B4C8B40E18E13971A3E682CC3','FF808181259DADEB01259DDDA4C201E7','14B1927026BE471E9B85FE699BCA61C2','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:05:58.908','100','2016-09-05 19:05:58.908','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('85D5D57E01F44B49A923611D23DAD691','D7D7D228E4594ACE8D00FD0E08B333DE','BF129721D9FB4EB0819509934153E972','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('88650D508D294A79B306CEA9DBF850D7','FF808181259DADEB01259DDDA4C201E6','687AD71263F94A31B85A3CC9942FF7ED','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('88C6B42E7FA7458EB20426226AC2F2BE','7499FEEA12DF46918F5448E8260B5E3E','0','39363B0921BB4293B48383844325E84C','Y','2020-05-22 08:57:23.772','100','2020-05-22 08:57:23.772','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('893248F94B7B45D4B418825A1124B7B7','463683CFA16C40C0A4EC8CF934114146','BF129721D9FB4EB0819509934153E972','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.047','0','2013-07-04 23:01:15.047','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('89F8E8215E85452D883DB5A44695F206','FF808181259DADEB01259DDDA4BB01E5','102D0E6D37DA46C3BABA6DFF3708F341','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:32:59.49','100','2016-05-10 17:32:59.49','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('8AA885C4DA0B441D81937BE1890F2031','FF808181259DADEB01259DDDA4C201E6','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('8ED25886285A405F981F251F45C0E58F','D7D7D228E4594ACE8D00FD0E08B333DE','67839EEFA49E44AC969BD60093FCC899','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('9097B346A30C41BB914C657B4049F552','D7D7D228E4594ACE8D00FD0E08B333DE','0','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('90ABBC7550EA4CC98C8869AE959A1C1B','FF8081812250326E012250353BDE0006','14B1927026BE471E9B85FE699BCA61C2','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('974063A1AD9D4501ACF9FD7072BFF94D','FF808181259DADEB01259DDDA4C201E7','BF129721D9FB4EB0819509934153E972','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:06:33.941','100','2016-09-05 19:06:33.941','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('97AC72DCF7AF40D793D6E4BE80BD65F2','FF808181259DADEB01259DDDA4C201E6','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('9A7EC9E6391944688C7DF136379E7C30','FF8081812250326E012250353BDE0006','0','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('9ACFD154DEDA4B63B67648F4FE4AF833','FF808181259DADEB01259DDDA4BB01E5','01AD882EFC8545ACA6455E2F6FD51EE9','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:38.56','100','2016-05-10 17:33:38.56','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('A30D63F28BEE4CDF99ABCE1A6C8F801D','FF808181259DADEB01259DDDA4BB01E5','BF129721D9FB4EB0819509934153E972','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:53.083','100','2016-05-10 17:33:53.083','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('A9403C5AC5E340029CCF6A319C5FC970','45A63D86E04D4052A3E8D04ABCC17E1E','102D0E6D37DA46C3BABA6DFF3708F341','39363B0921BB4293B48383844325E84C','Y','2017-01-26 13:41:18.384','100','2017-01-26 13:41:18.384','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('AE13511035D64E4A925DAF042FB5C909','FF808181259DADEB01259DDDA4C201E7','67839EEFA49E44AC969BD60093FCC899','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:06:23.97','100','2016-09-05 19:06:23.97','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('AFD3C34DD9AA4CC590E986DC7581F571','463683CFA16C40C0A4EC8CF934114146','01AD882EFC8545ACA6455E2F6FD51EE9','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.047','0','2013-07-04 23:01:15.047','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('AFEB72B0B7424EC99167DE820AD2F20D','FF808181259DADEB01259DDDA4C201E7','01AD882EFC8545ACA6455E2F6FD51EE9','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:06:12.551','100','2016-09-05 19:06:12.551','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('B259A9E578C740F483C5FA93DDE34203','41DAFA0C214D4954A6A9B383AF9A3D96','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','N','2023-10-11 11:59:08.846','100','2023-10-11 11:59:08.846','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('B4B94E5E0E61475998070EC51D81FF75','FF808181259DADEB01259DDDA4C201E7','4399136852B145BD96CC2A6CE0800C68','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:06:08.283','100','2016-09-05 19:06:08.283','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('C94DD74AAB414D4996AE4AD6D4067886','FE77051CF38044DCB7471664F9CBB44B','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2016-09-05 10:16:42.287','100','2016-09-05 10:16:42.287','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('D1621B93AA2B46A8BD2C17A461B75417','FF8081812250326E012250353BDE0006','687AD71263F94A31B85A3CC9942FF7ED','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('D22D0FB1D0F447919D0A8B8A75747DEB','FF808181259DADEB01259DDDA4BB01E5','4399136852B145BD96CC2A6CE0800C68','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:34','100','2016-05-10 17:33:34','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('D7774F5E00B743DBA062612850A343F8','D7D7D228E4594ACE8D00FD0E08B333DE','687AD71263F94A31B85A3CC9942FF7ED','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('D95911EC4DFF426785F928105499766D','FF808181259DADEB01259DDDA4C201E6','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:53:57.752511','100','2016-05-10 18:53:57.752511','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('D9B55D1899F24A549DE4F37CE2C37722','D7D7D228E4594ACE8D00FD0E08B333DE','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:04.121774','100','2016-05-10 18:55:04.121774','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('DBF5A71716C64C41BBB95516EE3BFDA5','898E1715D1DF4C15A9CBE0813F23F892','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','N','2023-10-11 11:58:48.036','100','2023-10-11 11:58:48.036','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('E1E5122BECCD402B857A7F5719E02101','463683CFA16C40C0A4EC8CF934114146','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2013-07-04 23:01:15.047','0','2013-07-04 23:01:15.047','0','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('E35081972A7C4F8F9A6E33041F67BF80','5FA11B3DD8F04C0986C774624809C31E','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','N','2023-10-11 11:57:53.708','100','2023-10-11 11:57:53.708','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('E54135DA0A6E4F449F385986A69C355F','FF808181259DADEB01259DDDA4C201E7','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2016-09-05 19:06:03.536','100','2016-09-05 19:06:03.536','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('EA1A8571906A470EA02AD544190EA841','FF8081812250326E012250353BDE0006','67839EEFA49E44AC969BD60093FCC899','39363B0921BB4293B48383844325E84C','Y','2016-05-10 18:55:21.710401','100','2016-05-10 18:55:21.710401','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('EACCEB3F06564BC98A938B3CDC905D90','FF808181259DADEB01259DDDA4BB01E5','687AD71263F94A31B85A3CC9942FF7ED','39363B0921BB4293B48383844325E84C','Y','2016-05-10 17:33:04.719','100','2016-05-10 17:33:04.719','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('26930A6961E443CDAD94248319D8BC01','E717F902C44C455793463450495FF36B','DF86640764AA4492AB6D4CA2D432B8D4','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:19.791','100','2024-12-17 14:49:19.791','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('4B63427EF7194253AE5623B1A166F6CF','E717F902C44C455793463450495FF36B','3B187EC130A549A7A9388F8060EF156D','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:22.767','100','2024-12-17 14:49:22.767','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('3E3FDCE69F6847E28BE33CFA53D41EED','E717F902C44C455793463450495FF36B','CCAAD77DA7994401A9657F04AEB6342E','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:25.427','100','2024-12-17 14:49:25.427','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('99014DA3A05247BBAE2FEFC8EB0B4547','E717F902C44C455793463450495FF36B','102D0E6D37DA46C3BABA6DFF3708F341','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:28.241','100','2024-12-17 14:49:28.241','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('DB5BB8E6E568469DBC173CFD06D21F2E','E717F902C44C455793463450495FF36B','687AD71263F94A31B85A3CC9942FF7ED','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:32.368','100','2024-12-17 14:49:32.368','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('9E3BA9AD88A7453CA81EC5CE2A36A9E5','E717F902C44C455793463450495FF36B','14B1927026BE471E9B85FE699BCA61C2','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:34.943','100','2024-12-17 14:49:34.943','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('9A8B84A3197B4044A5F4C9315942BBA2','E717F902C44C455793463450495FF36B','E2A8087A81F54203969C6AED1AABBC72','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:39.476','100','2024-12-17 14:49:39.476','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('B59E0EFB9E7D42C699C1F0A4A406C5AF','E717F902C44C455793463450495FF36B','B5DE96143D6642228E3B9DEC69886A47','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:42.525','100','2024-12-17 14:49:42.525','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('ABC7AF1DEC994A4DAEAE9BD545074686','E717F902C44C455793463450495FF36B','4399136852B145BD96CC2A6CE0800C68','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:46.204','100','2024-12-17 14:49:46.204','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('C44405A869AB4756AD723D26FB54AC54','E717F902C44C455793463450495FF36B','01AD882EFC8545ACA6455E2F6FD51EE9','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:49:57.448','100','2024-12-17 14:49:57.448','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('CDBCDE2BB7E54D248A34F6C624F222F0','E717F902C44C455793463450495FF36B','67839EEFA49E44AC969BD60093FCC899','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:50:01.988','100','2024-12-17 14:50:01.988','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('4E49A87DF3FA40FC93B1502824A9A06D','E717F902C44C455793463450495FF36B','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:50:05.95','100','2024-12-17 14:50:05.95','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('4AFE1EB76EB64AF9B378C15A200CCD46','E717F902C44C455793463450495FF36B','65C1C46FB1D04CBD98CBD4167CCFE600','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:50:09.615','100','2024-12-17 14:50:09.615','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('C860DD8876AB49C496A0229AD09A8B29','E717F902C44C455793463450495FF36B','BF129721D9FB4EB0819509934153E972','39363B0921BB4293B48383844325E84C','Y','2024-12-17 14:50:13.15','100','2024-12-17 14:50:13.15','100','N',NULL);
INSERT INTO public.ad_role_orgaccess(ad_role_orgaccess_id, ad_role_id, ad_org_id, ad_client_id, isactive, created, createdby, updated, updatedby, is_org_admin, inherited_from)
    VALUES ('73736A39CBBB4301B04A056A831A80FA','5FA11B3DD8F04C0986C774624809C31E','D270A5AC50874F8BA67A88EE977F8E3B','39363B0921BB4293B48383844325E84C','Y','2024-12-17 15:02:50.305','100','2024-12-17 15:02:50.305','100','N',NULL);
UPDATE public.ad_org SET em_obretco_dbp_orgid='D270A5AC50874F8BA67A88EE977F8E3B' WHERE ad_org_id='D270A5AC50874F8BA67A88EE977F8E3B';

```

### Openbravo Access

You can now access Openbravo with initialized sample data

!!! success
    Openbravo Back Office
    
    - [http://localhost:8081/openbravo/](http://localhost:8081/openbravo/)
    
    - User: Openbravo
    - Password: openbravo

!!! success 
    Openbravo POS
    
    - [http://localhost:8081/openbravo/web/org.openbravo.retail.posterminal/?terminal=VBS-1#login](http://localhost:8081/openbravo/web/org.openbravo.retail.posterminal/?terminal=VBS-1#login)
    - User: vallblanca
    - Password: openbravo

By following these steps the POS should be correctly configured, for more information you can visit [Retail:Configuration Guide](https://wiki.openbravo.com/wiki/Retail:Configuration_Guide){target="_blank"}


## Etendo 

### Configure Etendo Environment

Follow the steps in the Install Etendo guide, in the tab [Steps to Install Etendo with Postgres Database and Tomcat Dockerized](../../../../getting-started/installation.md#steps-to-install-etendo-with-postgres-database-and-tomcat-dockerized).

!!! info 
    At this point we assume that you already have a development environment with Etendo Base, and Tomcat and Postgres SQL dockerized.

Then, You can open the `EtendoERP` project in IntelliJ, as mentioned in the [Install Etendo - Development Environment](../../../etendo-classic/getting-started/installation/install-etendo-development-environment.md) guide, although it is not necessary to configure Tomcat, since the service is already dockeridez and preconfigured.




### Install Modules
Once we have the Etendo environment we must install the Platform Bundle and the modules specific to the Etendo-Openbravo connector.
To do this we simply add the dependencies in the build.gradle file:

```groovy title="build.gradle"
implementation ('com.etendoerp:platform.extensions:latest.release')
implementation ('com.etendoerp:.extensions:latest.release')
others
```

Also, in the gradle.properties file the following configuration variables must be added, to execute all the necessary dockerized services:

``` groovy title="gradle.properties"
context.name=etendo

bbdd.sid=etendo
bbdd.port=5434
bbdd.systemUser=postgres
bbdd.systemPassword=syspass
bbdd.user=tad
bbdd.password=tad

org.gradle.jvmargs=-Dfile.encoding=UTF-8

docker_com.etendoerp.docker_db=true
docker_com.etendoerp.tomcat=true
docker_com.etendoerp.etendorx=true
docker_com.etendoerp.etendorx_async=true
docker_com.etendoerp.etendorx_connector=true
docker_com.etendoerp.integration.to_openbravo=true

etendorx.dependencies=com.etendorx.integration.to_openbravo:mapping:1.0.0, com.etendorx.integration.to_openbravo:worker:1.0.0
etendorx.basepackage=com.etendorx.integration.to_openbravo.mapping
```

!!! warning
    Since the database service will run dockerized and Openbravo is assumed to be installed on a local Postgres service on port `5432`, we will change the Etendo database port to `ddbb.port=5434` so that when the dockerized Postgres service is raised it will do so on that port.

Now in a terminal in the Etendo project, we execute the commands:

```bash title="Terminal"
./gradlew setup 
```
To apply the changes in the `gradle.properties` file settings.

```bash title="Terminal"
./gradlew resources.up 
```
To launch all dockerized services

<figure markdown="span">
    ![dockerized-services.png](../../../../assets/developer-guide/etendo-rx/connectors/openbravo-connector/instalation/dockerized-services.png)
    <figcaption> As you can see all the services required for the Openbravo Etendo integration are running </figcaption>
</figure>


### Compile and access to Etendo Classic 

The next step is to install Etendo and apply sampledata

```bash title="Terminal"
./gradlew install
./gradlew import.sample.data -Dmodule=com.etendoerp.integration.to.openbravo.sampledata
./gradlew smartbuild
```

Once the environment has been compiled, the Tomcat service is automatically restarted, as can be seen in the last compilation steps, and you can now access 

!!! success 
    Access Etendo Classic
        - [http://localhost:8080/etendo](http://localhost:8080/etendo)
        - User: admin
        - Password: admin


###  Etendo RX Configurations







### Aplicar Configuraciones

cd modules/com.etendoerp.integration.to_openbravo/utils
make set_wal
make insert
make setupconnector


### 5. Verify Middleware Configuration
Ensure Etendo RX middleware is configured to handle synchronization between Openbravo and Etendo. Update any required endpoints and authorization tokens.

### 6. Testing the Integration
#### Generating Documents in Openbravo POS
1. Log in to the Openbravo POS terminal.
2. Perform a sales transaction or any activity that generates a document.
3. Confirm that the document is synchronized to the Etendo environment.

#### Verifying Synchronization
1. Check the Etendo environment for the synchronized document.
2. Review logs in Etendo RX middleware to ensure smooth data flow.

## Additional Notes
- Logs can be enabled in Etendo by modifying the `config/log4j2-web.xml` file:

  ```xml
  <AppenderRef ref="Console"/>
  ```

- Run the `smartbuild` task after updating configurations:

  ```bash
  ./gradlew smartbuild --info
  ```

## Troubleshooting
- Ensure all services (Openbravo, Etendo RX, and Etendo) are running correctly.
- Verify database connections and network configurations.

## Default Credentials
- **Openbravo POS**: Default credentials vary based on setup.
- **Etendo**:
  - Username: `admin`
  - Password: `admin`

## References
- Openbravo Documentation
- Etendo Installation Guide
- PostgreSQL Official Documentation






###  Openbravo Database Backup
Now we must create a dump of the Openbravo database to restore in Etendo and keep all the master data.
In a terminal in the Etendo project we execute: 

```bash title="Terminal"
pg_dump -U tad -p 5432 -F c -b -v -f ./openbravo.dump  openbravo
```
### Database Restore

Now we will restore the Openbravo database, changing the default name to etendo which is the database name we defined in the `bbdd.sid` variable, or the database name defined in the `bbdd.sid` variable. 

```bash title="Terminal"
PGPASSWORD=syspass psql -U postgres -d postgres -h localhost -p 5434
```
Once connected to the database we will create the tad role and the empty database where we will restore the information.

```sql title="PSQL Terminal"
CREATE ROLE tad LOGIN PASSWORD 'tad' SUPERUSER CREATEDB CREATEROLE VALID UNTIL 'infinity';
CREATE DATABASE etendo WITH ENCODING='UTF8' OWNER=tad;
```
Finally, we restore the database with the following command: 

```bash title="Terminal"
PGPASSWORD=tad pg_restore -v -U tad -d etendo -h localhost -p 5434 -v -O openbravo.dump
```
The last step is to delete the content of some tables, as these tables are no longer available in Etendo. 

```bash title="Terminal"
PGPASSWORD=tad psql -U tad -d etendo -h localhost -p 5434
```
Execute: 
```sql title="PSQL Terminal"

DELETE FROM M_OFFER
WHERE M_OFFER_TYPE_ID = '20E4EC27397344309A2185097392D964';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '1C36D6974F4E4C41AA92E1EEBCD577E1';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '41616748FCCD42D287CFA1C0B5116140';

DELETE FROM M_OFFER
WHERE M_OFFER_TYPE_ID = '94AEA884F5AD4EABB72322832B9C5172';

DELETE FROM M_OFFER_ORGANIZATION
WHERE M_OFFER_ID = '0C681EECD8974D56921D47DBFFF5A22C';

DELETE FROM M_OFFER
WHERE M_OFFER_TYPE_ID = '8338556C0FBF45249512DB343FEFD280';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '1C47E773ACB341C48C8C7B970955C3DE';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '21BF154DAD644B38A667A58E12A45CAB';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '6C41BA4C0AA44BC9B38A64353DEDCB21';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '74F2E10500374BD8B2EED9E7594279EE';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '84408A74ADE548358E6701E0BF85CAC9';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '95AF235142FB4656A4B7D5A08DE24927';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '9B5F1139A656454898AE5D5D8C5A77EE';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = 'A5190E45A59E4E4DBA19E06A8ED543D5';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = 'AEBCDD6E9FD647C38E521E6AEABFEBA9';

DELETE FROM M_OFFER_BPARTNER
WHERE M_OFFER_ID = 'AEBCDD6E9FD647C38E521E6AEABFEBA9';

DELETE FROM M_OFFER
WHERE M_OFFER_TYPE_ID = '312D41071ED34BA18B748607CA679F44';

DELETE FROM M_OFFER
WHERE M_OFFER_TYPE_ID = '7B49D8CC4E084A75B7CB4D85A6A3A578';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '65BD8402B1CD428A952A0AF37B325BC3';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = '86D0C2B35B454D95A0A09E245B430FED';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = 'DB155972EDA6446290DDC3FF0387E832';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = 'DBE6100C27484800A19B6D5044B12715';

DELETE FROM M_OFFER_PRODUCT
WHERE M_OFFER_ID = 'DBE6100C27484800A19B6D5044B12715';

DELETE FROM M_OFFER
WHERE M_OFFER_TYPE_ID = 'BE5D42E554644B6AA262CCB097753951';

DELETE FROM OBUIAPP_GC_FIELD
WHERE OBUIAPP_GC_TAB_ID = '1AD989605ACA4F5FB6C11B2E7AC88867';

DELETE FROM OBUIAPP_GC_TAB
WHERE AD_TAB_ID = '14BDEAB664C146DCB662B2E3EA7A495E';

``` 