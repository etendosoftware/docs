---
tags:
    - Copilot
    - Tool
    - SQL
    - CSV
    - Database
    - Etendo
---

# Etendo SQL to CSV Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The **Etendo SQL to CSV Tool** is a specialized tool for executing SQL queries in Etendo's database and converting the results to CSV format. It connects to Etendo through the DBQueryExec webhook, executes SELECT queries securely, and exports the JSON results as CSV files for easy data analysis and reporting.

!!!info
    To be able to include this functionality, the Copilot Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about the available versions, core compatibility and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool is essential for data extraction, reporting, and analysis tasks within Etendo. It provides a secure and standardized way to query the database and export results. The tool handles:

- **Database Integration**: Connects to Etendo's database through the secure DBQueryExec webhook
- **Query Execution**: Executes SELECT statements with automatic security validation
- **Data Export**: Converts JSON results to CSV format for easy data manipulation
- **Security Enforcement**: Only allows SELECT queries and validates table aliases for security
- **Authentication Management**: Automatically handles authentication and host configuration

Using this tool consists of the following actions:

- **Processing Parameters**

    It takes the following input parameters:

    - `sql_query`: The SELECT query to execute (required, must include table aliases)
    - `output_file`: Path where to save the CSV file (optional, creates temporary file if not specified)
    - `include_headers`: Whether to include column headers in the CSV output (optional, default: true)

- **Query Validation**

    The tool validates the SQL query for security:
    - Only SELECT statements are allowed
    - Dangerous keywords (DROP, DELETE, UPDATE, etc.) are blocked
    - Must follow Etendo's requirement that all tables have aliases

- **Database Execution**

    Connects to Etendo using the DBQueryExec webhook:
    - Automatically retrieves authentication token and host configuration
    - Executes the query with Etendo's built-in security filters
    - Returns structured JSON data with columns and rows

- **CSV Conversion**

    Converts the JSON response to CSV format:
    - Extracts column names and data rows from the webhook response
    - Handles optional header inclusion
    - Writes the CSV file with proper encoding (UTF-8)

- **Result Reporting**
    Returns detailed information about the operation:
    ```
    ✅ SQL query executed successfully!
    📊 Result: 150 rows exported
    📁 CSV file saved at: /tmp/etendo_query_result_12345.csv
    📏 File size: 0.25 MB
    🔗 Webhook: DBQueryExec
    🔍 Query: SELECT u.name, u.email FROM ad_user u WHERE...
    ```

## Security Features

The Etendo SQL to CSV Tool implements multiple security layers:

- **Query Restriction**: Only SELECT statements are permitted, preventing data modification
- **Keyword Filtering**: Blocks dangerous SQL keywords and operations
- **Alias Requirement**: Enforces Etendo's security requirement for table aliases
- **Automatic Authentication**: Uses secure token-based authentication through copilot context
- **Server-side Security**: Leverages Etendo's built-in access controls and data filters

## SQL Query Requirements

All SQL queries must follow Etendo's security standards:

### Required Format
- **SELECT Only**: Only SELECT statements are allowed
- **Table Aliases**: All tables must have aliases (e.g., `FROM ad_user u`, not `FROM ad_user`)
- **Accessible Tables**: Only tables accessible to the current user can be queried
- **Security Filters**: Etendo automatically applies organization and client security filters

### Examples of Valid Queries
```sql
-- Query active users
SELECT u.name, u.email, u.created 
FROM ad_user u 
WHERE u.isactive = 'Y'

-- Query business partners with contact information
SELECT bp.name as business_partner, bp.taxid, l.phone, l.email
FROM c_bpartner bp
LEFT JOIN c_bpartner_location bpl ON bp.c_bpartner_id = bpl.c_bpartner_id
LEFT JOIN c_location l ON bpl.c_location_id = l.c_location_id
WHERE bp.iscustomer = 'Y'

-- Query sales orders with details
SELECT so.documentno, so.dateordered, so.grandtotal, bp.name as customer
FROM c_order so
JOIN c_bpartner bp ON so.c_bpartner_id = bp.c_bpartner_id
WHERE so.issotrx = 'Y' 
  AND so.docstatus = 'CO'
```

### Examples of Invalid Queries
```sql
-- Missing table alias
SELECT name FROM ad_user WHERE isactive = 'Y'

-- Non-SELECT operation
UPDATE ad_user SET isactive = 'N' WHERE ad_user_id = '123'

-- Dangerous keywords
DROP TABLE temp_table
```

## Usage Example

Imagine we want to export active users with their roles to a CSV file for analysis. Our parameters would be:

- **sql_query**: `SELECT u.name, u.email, r.name as role FROM ad_user u JOIN ad_user_roles ur ON u.ad_user_id = ur.ad_user_id JOIN ad_role r ON ur.ad_role_id = r.ad_role_id WHERE u.isactive = 'Y'`
- **output_file**: `/tmp/active_users_with_roles.csv`
- **include_headers**: true

The Etendo SQL to CSV Tool will:
1. Validate the query meets security requirements
2. Execute the query through the DBQueryExec webhook
3. Convert the JSON results to CSV format
4. Save the file with headers included
5. Return a success message with operation details

## Error Handling

The tool provides comprehensive error handling for common scenarios:

- **Invalid SQL**: Returns detailed error messages for syntax or security violations
- **Connection Issues**: Reports authentication or network problems with the webhook
- **Permission Errors**: Indicates when tables or data are not accessible to the user
- **File System Issues**: Reports problems with CSV file creation or writing
- **Empty Results**: Handles queries that return no data gracefully

## Integration with Etendo

This tool leverages Etendo's built-in security and data access features:

- **Multi-tenant Security**: Automatically respects client and organization boundaries
- **Role-based Access**: Only returns data accessible to the current user's role
- **Data Filters**: Applies Etendo's standard security filters automatically
- **Audit Trail**: Query execution is logged through Etendo's standard audit mechanisms

## Best Practices

### Query Optimization
- Use appropriate WHERE clauses to limit result sets
- Include only necessary columns in SELECT statements
- Consider using LIMIT clauses for large datasets
- Test queries in Etendo's SQL console first for validation

### File Management
- Specify output file paths in appropriate directories
- Consider file naming conventions for organized data exports
- Monitor file sizes for large result sets
- Clean up temporary files after use

### Security Considerations
- Never hardcode sensitive data in queries
- Use parameterized approaches when possible
- Validate query results before sharing or processing
- Follow your organization's data export policies
