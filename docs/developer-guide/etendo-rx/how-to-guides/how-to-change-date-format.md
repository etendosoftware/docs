# Changing Date Format and Time Zone in a Request

## Overview

This document outlines the steps for developers to change the date format and time zone when making an HTTP request to the application. These features are useful for ensuring that date and time values are interpreted correctly based on the user's locale or specific requirements.

## Prerequisites

- Familiarity with HTTP requests and RESTful APIs.
- Access to the application's API documentation for endpoint details.

## Adding Date Format and Time Zone Parameters

### Date Format

To specify a custom date format, add a `_dateFormat` parameter to your HTTP request. The value should be a string that represents the desired date format, following the Java `SimpleDateFormat` conventions.

**Example:**

```http
GET /OBMAPBusinessPartner/2C4C71BC828B47A0AF2A79855FD3BA7A?_dateFormat=yyyy-MM-dd
```

In this example, the date format is set to `"yyyy-MM-dd"`, which will format dates as `"2023-08-29"`.

### Time Zone

To specify a custom time zone, add a `_timeZone` parameter to your HTTP request. The value should be a string that represents the desired time zone, following the Java `TimeZone` conventions. This parameter, requires to have a `_dateFormat`, cannot be used as single parameter.

**Example:**

```http
GET /OBMAPBusinessPartner/2C4C71BC828B47A0AF2A79855FD3BA7A?_dateFormat=yyyy-MM-dd&_timeZone=America/New_York
```

In this example, the date format is set to `"yyyy-MM-dd"` and the time zone is set to `"America/New_York"`.
