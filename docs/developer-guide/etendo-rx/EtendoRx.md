---
title: EtendoRx
---

## Overview

## 1. Introduction

### 1.1 Purpose

This document aims to define and explain a bird sight of the full picture of this new infraestructure. The main objective of this new product is to complement the existing ERP: “Etendo Classic”, making usage of new technologies and applying proved patterns and good practices while maintaining the best features it has.

### 1.2 Scope

This documents have a wider view of the software, each aspect which needs a more detailed explanation will have a specific document to more details.

### 1.3 Definitions, Acronyms and Abbreviations

### 1.4 References

### 1.5 New technologies

It’s desirable to make usage of spring boot as code base, to take advantange of all available libraries and starters.

### Classic characteristics to keep

Low code: as much we can help and guide developers to develop a strong solution in a short period of time

Data dictionary: we must maintain Etendo Classic as a tool to develop new solutions or extend existing one

### Architecture definition

Based on the Spring cloud stream framework and Kafka as message bus.

#### **Spring cloud stream**

![](https://spring.io/images/favicon-9d25009f65637a49ac8d91eb1cf7b75e.ico)

[Spring Cloud Stream](https://spring.io/projects/spring-cloud-stream)

> Spring Cloud Stream is a framework for building highly scalable event-driven microservices connected with shared messaging systems.
!!! info
    The framework provides a flexible programming model built on already established and familiar Spring idioms and best practices, including support for persistent pub/sub semantics, consumer groups, and stateful partitions.

#### **Kafka**

!!! info
    Apache Kafka is an open-source distributed event streaming platform used by thousands of >companies for high-performance data pipelines, streaming analytics, data integration, and mission->critical applications.

## 2. Architectural Representation

![6274e20b-056b-4448-a7d0-6569f3960567.png](/assets/legacy/technicaldocumentation/platform/6274e20b-056b-4448-a7d0-6569f3960567.png)
![05538c4b-7666-428e-8c8e-7c42b1e436fa.png](/assets/legacy/technicaldocumentation/platform/05538c4b-7666-428e-8c8e-7c42b1e436fa.png)

This framework will bring the base code to develop in a reactive and scalable way, following well known patterns and good practices.

EtendoRX can be runned, without change code changes, in two modes:

Monolitic

Microservices

#### **1. Full**

Simply running the root project all contained functionality will be runned in multi thread mode

#### **2. Microservices**

Complementing the previous method, each one of the components can be excluded of the full way and can be runned in a standalone way, this enable to give scalability to an specific component.

### Communication

#### Internal communication

All of the components use Kafka as a communication bus. This behaviour is near transparent because is Spring cloud stream framework

#### Public access

Any module of the framework having accesible endpoints has a different port, so, is needed an Edge server to centralize all request on a single url. Also, it is in many cases desirable to expose some of the services to the outside of the system landscape and hide the remaining microservices from external access. The exposed microservices must be protected against requests from malicious clients.

To simplify implementation, this will be achived with:

![](https://spring.io/images/favicon-9d25009f65637a49ac8d91eb1cf7b75e.ico)

[Spring Cloud Gateway](https://spring.io/projects/spring-cloud-gateway)

#### Configuration

To keep simply to configure each one of the aspects of the full stack service, is useful to apply a common partner which spring resolved and apply on the library

![](https://spring.io/images/favicon-9d25009f65637a49ac8d91eb1cf7b75e.ico)

[Spring Cloud Config](https://spring.io/projects/spring-cloud-config)

## 3. Architectural Goals and Constraints

There are some key requirements and system constraints that have a significant bearing on the architecture. They are:

a. The software must make use of Etendo Classic as a development tool, making use of the application dictionary and compilation tools.

b. It must be flexible enough to run in monolithic mode as well as microservices, both using the same code base and client-specific customizations.

## 4. Architectural drivers

### 4.1. Quality Attributes (non-functional requirements)

Performance

Scalability

Availability

Security

Privacy

Disaster Recovery

Accessibility

Monitoring

Management

Audit

Flexibility

Extensibility

Maintainability

Legal, Regulatory and Compliance

Internationalisation (i18n)

Localisation (L10n)

### 4.2 Constraints

Time and budget constraints

Technology constraints

## 5. Use-Case View

### 5.1 Architecturally-Significant Use Cases

#### **a. Security: security access on services**

[https://incidencias.atlassian.net/browse/EPL-142 - Can't find link](https://incidencias.atlassian.net/browse/EPL-142)

**Issue Description**

Is needed to add an extra layer which adds to each endpoint a method to allow / forbid access based on user credentials

**Solution design**

Develop a new library defining all methods and functionality needed to give the needed functionality to any service.

This library will be added to any EtendoRX project , then, all access points in this service will require an Authorization header.

The token will be signed with a value stored as a global configuration.

![ece5ac3f-f64f-4f08-a26e-6bc79ee9c676.png](/assets/legacy/technicaldocumentation/platform/ece5ac3f-f64f-4f08-a26e-6bc79ee9c676.png)

#### **b. Debezium: Improve configuration and funcionality (TBD)**

[https://incidencias.atlassian.net/browse/EPL-127 - Can't find link](https://incidencias.atlassian.net/browse/EPL-127)

Issue Description

Having and existing module with a basic debezium functionality is needed to have a more advanced configuration.

Solution Design

#### **c. Security: Basic server**

[https://incidencias.atlassian.net/browse/EPL-125 - Can't find link](https://incidencias.atlassian.net/browse/EPL-125)

Issue Description

As a user is needed to access to etendorx services with Etendo classic user and password

Solution design

Making usage of spring security we need to have an extra layer to connect and implement Etendo Security. Is needed to develop a Servlet which receiving an username and password, returns a valid JWT response.

#### **d. low code model layer declare jpa subdomain**

![](https://incidencias.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10815?size=medium)

[EPL-138: (P2) low code model layer declare jpa subdomain**OPEN**](https://incidencias.atlassian.net/browse/EPL-138)

Issue Description

Solution design

#### **e. security: Integration with auth servers**

![](https://incidencias.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10815?size=medium)

[EPL-132: Security: Integration with auth servers**DONE**](https://incidencias.atlassian.net/browse/EPL-132)

Issue Description

Solution design

#### **f. Improve code generation tools**

![](https://incidencias.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10815?size=medium)

[EPL-131: (P2) Improve code generation tools**OPEN**](https://incidencias.atlassian.net/browse/EPL-131)

Issue Description

Solution design

#### **g. Edge server: Add reverse proxy functionality**

![](https://incidencias.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10815?size=medium)

[EPL-130: (P2) Edge server: Add reverse proxy functionality**OPEN**](https://incidencias.atlassian.net/browse/EPL-130)

Issue Description

Solution design

#### **h. Config server**

![](https://incidencias.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10815?size=medium)

[EPL-130: (P2) Edge server: Add reverse proxy functionality**OPEN**](https://incidencias.atlassian.net/browse/EPL-130)

Issue Description

Solution design
