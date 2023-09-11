## You can filter any request by active or all rows

The \_noActiveFilter parameter can be used in any request method to filter active records or all records (active and inactive). This way it allows more control when obtaining the results.

---

## Example of GET request for all records

Open Postman and we'll make a get request.

    Verbose: GET

    URL: http://localhost:8094/BusinessPartner?_noActiveFilter=true

    Body: empty

    Return: a json object with all businessPartners active or inactive

---

## Example of GET request only for active records

Open Postman and we'll make a get request.

    Verbose: GET

    URL: http://localhost:8094/BusinessPartner?_noActiveFilter=false

    Body: empty

    Return: a json object with all active BusinessPartner rows

---

Another way to get active rows is to remove the parameter \_noActiveFilter parameter, because by default the active row always applies the active row filter.
