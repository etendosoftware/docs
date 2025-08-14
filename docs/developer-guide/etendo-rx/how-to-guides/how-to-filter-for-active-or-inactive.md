## You can filter any request by active or all rows

The `_noActiveFilter` parameter can be used in any request method to filter active records or all records (active and inactive). This way it allows more control when obtaining the results.

---

## Example of GET request for all records

Open Postman and we will make a get request.

    Verbose: GET

    URL: http://localhost:8094/BusinessPartner?_noActiveFilter=true

    Body: empty

    Return: a json object with all businessPartners active or inactive

---

## Example of GET request only for active records

Open Postman and we will make a get request.

    Verbose: GET

    URL: http://localhost:8094/BusinessPartner?_noActiveFilter=false

    Body: empty

    Return: a json object with all active BusinessPartner rows

---

Another way to get active rows is to remove the parameter `_noActiveFilter parameter` , because by default the active row always applies the active row filter.

---

This work is a derivative of [How To Guides](https://wiki.openbravo.com/wiki/Category:HowTo){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.
