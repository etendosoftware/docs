---
title: Setup Etendo Rx Autentication keys
---
## Overview
This page explain how to update the public and private key needed for Etendo RX to autenticate conections.

## Setup Etendo Rx autentication keys
1. Open a terminal in  `etendo_rx_compose` directory.
2. Generate the public and private keys that will be used in the Auth and Edge services:


Private key generation

```plaintext
  openssl genrsa -out main/resources/private.pem 2048
```

Public key generation

```plaintext
  openssl rsa -in main/resources/private.pem -pubout -outform PEM -out main/resources/public_key.pem
```

Private key generation with PCKS8 format

```plaintext
 openssl pkcs8 -topk8 -inform PEM -in main/resources/private.pem -out main/resources/private_key.pem -nocrypt
```

3. Update the content of `main/rxconfig/application.yaml` copyng the key content of `main/resources/public_key.pem` file.
!!! warning
   Keep the tabulation

Example file: 
````

spring:
  output:
    ansi:
      enabled: ## Shows console output with colors
        ALWAYS

public-key: >
  -----BEGIN PUBLIC KEY-----
  MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAocs6752BX8E9sUSkP0nn
  Qlp9QNtTsBHB/jFZOro2ayCf203u3DHCPrLpLDZyrqAasIRRxKAAMNfmhl7/Hgg5
  FKeLp8rKEavlDTblVfVLvBmYpoJMxE2RumW4SdyP56LNnSlY49srflyiJyd9w+m0
  vVxMpXPT1RWTv+FJibVB8asqyUWW5sJgQ8Cr3PLI8KDCcwSpjlkkack3vB2ZiFtZ
  VPntj4C6+/o5hcPgUeLVOFjH1H9zJP/ELLcueZtSbRo4J1CJsLUyY3ZCIk84wZwf
  ielygT6Yl3tNqGGnxm7moXO8+y5uJZymoMqEhV5OnlolpAb/VuGZviv932fWzEMR
  jwIDAQAB
  -----END PUBLIC KEY-----

````
4. Update the content of `main/rxconfig/auth.yaml` copyng the key content of `main/resources/private.pem` file. Keep the tabulation.

5. Create a local commit and config server will be updated wen restart Etendo Rx services.
````
cd /main/rxconfig
git add .
git commit -m "Public and private keys locally updated"
````

6. Restart Etendo RX:
````
docker-compose -p rx -f main/docker-compose.yaml restart
````

