# API Change Documentation  



## March 2025

**Etendo Classic** 
[Release 25.1.0]()

### Overview
Provide a brief overview of the purpose of this release, including high-level objectives, key improvements, and the rationale behind major changes.

> **Example**:  
> Version 25.1.0 of our ERP system introduces performance enhancements, new inventory management features, security improvements, and a major update of several third-party libraries used within the platform. Additionally, several high-priority bugs from the previous version have been fixed to ensure increased stability and reliability.


### API Changes

#### Added Endpoints
List and describe any new API endpoints introduced in this version.

!!! quote
    - **Endpoint**: `/api/newEndpointExample`  
    - **Method**: `GET | POST | PUT | DELETE`  
    - **Description**: Briefly explain the purpose, required/optional parameters, and expected functionality.  
    - **Parameters**:  
        - `param1`: Data type, short description  
        - `param2`: Data type, short description  
    - **Response Codes**:  
        - `200`: Successful response example  
        - `400`: Client error example  
    - **Sample Request**:  
        ```bash
        curl -X GET "https://yourserver.com/api/newEndpointExample" \
        -H "Authorization: Bearer <TOKEN>"
        ```
    - **Sample Response**:  
        ```json
        {
        "status": "success",
        "data": []
        }
        ```

#### Modified Endpoints
List the endpoints that have been updated, indicating the nature of the modifications (e.g., new parameters, updated response structures, stricter authentication, etc.).

1. **Endpoint**: `/api/existingEndpoint`  
   - **Change**: Added a new optional parameter `documentType`.  
   - **Updated Response Example**:  
     ```json
     {
       "id": 101,
       "documentType": "Invoice",
       "date": "2025-03-01"
     }
     ```
   - **Notes**: While older clients remain compatible, it is recommended to account for the new parameter in any client implementation.

2. **Endpoint**: `/api/anotherEndpoint`
   - **Change**: Requires an additional **header** (`x-api-key`) for authentication.  
   - **Impact**: Requests missing this header will return `401 - Unauthorized`.

#### Deprecated Endpoints
Endpoints marked as deprecated and scheduled for removal in a future release.

- **Endpoint**: `/api/deprecatedEndpoint`  
  - **Reason**: Superseded by `/api/newEndpoint` which offers better security and performance.  
  - **Removal Date**: Planned for version 26.0.0.  
  - **Recommendation**: Switch to `/api/newEndpoint` as soon as possible.

---

### Data Structure Changes
Highlight changes in any data models, database tables, or JSON objects used by the API.

!!! quote
    **Example**:
        - **Table/Model**: `Orders`  
        - **Removed Field**: `additionalDiscount`  
        - **New Field**: `promoCode` (String, max length of 20)  
        - **Reason for Change**: Consolidating discounts and promotional offers under a single field.  
        - **Impact**: Client applications must update their logic to use `promoCode`.

---

### Breaking Changes
Explicitly list changes that break backward compatibility. Provide guidance on how to address them.

1. **Breaking**: Fields `x` and `y` in `/api/invoices` have been removed.  
   - **Solution**: Use `promoCode` and `specialDiscount` instead.  

2. **Breaking**: Authentication now requires OAuth2 instead of Basic Auth.  
   - **Solution**: Update client code to request OAuth2 tokens instead of using username/password in the header.



### Third-Party Library Updates
List and describe the key external libraries that have been upgraded in this release, along with the versions and any relevant breaking changes in those libraries.

- **Library Name**: `[Library ABC]`  
  - **Old Version**: 4.0.0  
  - **New Version**: 5.2.1  
  - **Notable Changes**:  
    - Updated security patches  
    - Changes in method signatures for encryption functions

- **Library Name**: `[Library XYZ]`  
  - **Old Version**: 2.1.5  
  - **New Version**: 3.0.0  
  - **Notable Changes**:  
    - Removal of deprecated methods used in our reporting module  
    - Requires additional configuration for localization support

> **Note**: Refer to each library’s release notes for more detailed information on changes and how they might affect your system.


### Additional Notes
Include any remaining points relevant to this release, such as known limitations, performance tips, or future roadmap items.


    **Example**:  
        - Enabling **query caching** is recommended to enhance API response times.  
        - We plan to introduce GraphQL support in a subsequent release.

---

###  Migration Guide
Give clear, step-by-step instructions on how to migrate existing integrations to the new version, minimizing disruptions.

1. **Dependency Update**:  
   - Indicate any third-party library or component version requirements.  
2. **Endpoint Refactoring**:  
   - Show which deprecated endpoints have replacements.  
3. **Added Parameters**:  
   - Explain mandatory vs. optional parameters that developers need to include.  
4. **Integration Testing**:  
   - Recommend testing in a staging environment before deploying to production.

---