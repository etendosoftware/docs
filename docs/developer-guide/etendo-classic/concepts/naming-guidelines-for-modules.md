---
title: Naming Guidelines for Modules
---
## Introduction

It is important to select an appropriate name for your module in order to make it easier for users to recognize it both in the Forge and in the Enterprise Module Management window.

In the future, Etendo may also use these naming conventions to automatically categorize modules based on tags, therefore it is important that these naming conventions are followed.

Here is a set of naming guidelines that we ask module authors to follow:

## Branding rules

- The module name should match the project name in the Forge (optional)
- Module names should not be longer than 5 or 6 words and less than 60 character long (optional)
- Module names cannot contain the word "Etendo"
    - JSON REST Web Services: :white_check_mark:
    - Etendo JSON REST Web Services: :no_entry:
- Exception to the previous rule: modules that Etendo decides to market as products rather than modules:
    - Etendo QuickStart Template: :white_check_mark:
- You do not need to specify the Etendo version in the module name:
    - Translation: Arabic Saudi Arabia (ar_SA): :white_check_mark:
    - Translation: Arabic Saudi Arabia (ar_SA) for Etendo 2.50: :no_entry:
- Module names should not contain the word "Module"
    - Copy Role: :white_check_mark:
    - Copy Role Module: :no_entry:

## Language and grammar conventions

- All module names must be in English. The module description and help can be in any other language.
- Non English proper nouns are accepted as part of a module name specified in English
    - Tax Report: Modelo 349 (Spain): :white_check_mark:
    - Tax Report: Form 349 (Spain): :no_entry: (rationale: Modelo 349 is a proper noun and should not be  translated)
    - Informe Fiscal: Modelo 349 (Spain): :no_entry:
- The module help must differ from the module description
- Grammatically, module names should be treated as proper nouns and you should capitalize the first letter of every word in the module name (with the exception of short words and acronyms)
    - Initial Data Load: :white_check_mark:
    - Initial data load: :no_entry:
    - Direct Debit Form of Payment: :white_check_mark:
    - Direct Debit Form Of Payment: :no_entry:
    - Three Digits ISO Country Codes: :white_check_mark:
    - Three Digits Iso Country Codes: :no_entry:
- You should avoid using numeric characters to express quantities (they are OK in codes and dates)
    - Three Digit ISO Country Codes: :white_check_mark:
    - 3 Digit ISO Country Codes: :no_entry:
    - Chart of Accounts - PGC 2007 General: Spain: :white_check_mark:
    - Tax Report: Modelo 349 - Spain
- Module names should not end with a full stop:
    - Initial Data Load: :white_check_mark:
    - Initial Data Load.: :no_entry:
- Module description should end with a full stop
    - Generador de declaraciones de impuestos. Traducción al español (español España) del módulo Tax Report Launcher.: :white_check_mark:
    - Generador de declaraciones de impuestos. Traducción al español (español España) del módulo Tax Report Launcher: :no_entry:

## Specific Types of Modules

- Core translations (translation of Etendo Core) should follow the convention:
    - "Translation: $LANG $COUNTRY ($CODE)"
    - Translation: Arabic Saudi Arabia (ar_SA) :white_check_mark:
- Module translations (translations of modules other than Etendo Core) should follow the convention:
    - "$MODULE NAME Translation: $LANG $COUNTRY ($CODE)"
    - Tax Report Launcher Translation: Spanish Spain (es_ES) :white_check_mark:
- The description for module translations should include an appropriate translation of the module name in the target language as well as both the name of the language and the name of the country in the target language:
    - + Name: Tax Report Launcher Translation: Spanish Spain (es_ES) + Description: Generador de declaraciones de impuestos. Traducción al español (español España) del módulo Tax Report Launcher. :white_check_mark:
- Chart of accounts modules should follow the convention:
    - "Chart of Accounts: $COUNTRY"
    - Chart of Accounts: France :white_check_mark:
- For countries with multiple charts of accounts, use the conventions
    - "Chart of Accounts: $TYPE - $COUNTRY"
    - Chart of Accounts: PGC 2007 General - Spain :white_check_mark:
    - Chart of Accounts: PGC 2007 PYMEs - Spain :white_check_mark:
- Tax configuration modules should follow the convention:
    - "Tax Configuration: $COUNTRY"
    - Tax Configuration: France :white_check_mark:
- Tax report modules should follow the convention:
    - "Tax Report: $FORM_NAME - $COUNTRY"
    - Tax Report: Modelo 347 - Spain :white_check_mark:
- Region modules should follow the convention:
    - "Regions: $COUNTRY"
    - "Regions: Brazil" :white_check_mark:
    !!! note
        Whenever the regions of a country are called something other than regions, you can use the :white_check_mark: term in the module description. Example: + Name: Regions: United States of America + Description: US states.
- Report modules (other than tax reports) should follow the convention:
    - "Report: $REPORT_NAME"
    - Report: Shipments Awaiting Invoice :white_check_mark:
- Skin modules should follow the convention:
    - "Skin: $SKIN_NAME"
    - Skin: Blue Sea :white_check_mark:
- Tutorial modules (provided as examples to illustrate how to develop modules) should follow the convention:
    - "Tutorial: $TUTORIAL NAME"
    - Tutorial: Solitaire :white_check_mark:

## Bundles

- Do not use "module" in bundles, everything is a module (including core) so this would be redundant.
- In general modules should not use subpackages of other modules since it might create a conflict. In particular do not use subpackages for modules included in a pack (eg. several modules in the spanish localization pack use as a package that is a subpackage of the spanish localization pack package). That inclusion is declared in the pack itself and using subpackaging would create a kind of redundancy (the module could be taken out from the pack later) or modules originally not designed for the pack could be included later.
- The only case where a subpackage makes sense are translations since that relationship can not be changed.
For translations, do not use the word "translation" but directly the language code: translatedmodulepackage.languageCode (eg. org.openbravo.document.massinvoicing.es_ES).
- For translations of core, it does not work (org.openbravo.es_ES) because the core package is not clear enough. In that case, use org.openbravo.coretranslation.es_ES or just org.openbravo.core.es_ES)
- Do not use the "type of artifacts" included in the module for packaging (eg. org.openbravo.report.xxx or org.openbravo.callout.xxx are wrong). The content of a module should not be defined by the "technical components" used to implement them but by the functional objective of the module. It might happen that the functional objective can be reached in a different manner and it should not force repackaging.
- In some cases, functional and technical categories are the same (eg. report) - in this case, put the word "report" in the name of the module but not as a package (eg. org.openbravo.financial.taxreportXX instead of org.openbravo.financial.report.taxXX)
- A package for a module developed by Etendo and staff should be:
org.openbravo.functionalcategory.modulename

    - In some cases, it makes sense to use an additional level:
        org.openbravo.functionalcategory.functionalsubcategory.modulename

    - Use a common set of functional categories and subcategories (when needed). Each scrum team defines their own list of categories and subcategories. This is a starting point (split by teams):

        - applicationdictionary (platform)
        - kernel (platform)
        - utility (platform)
        - setup (erp engineering)
        - common (erp engineering)
        - document (erp engineering)
        - warehouse (erp engineering)
        - project (erp engineering)
        - production (erp engineering)
        - mrp (erp engineering)
        - financial (erp engineering)
        - erputil (erp engineering)
        - localization (localization) ->  subcategories for each country (eg. localization.spain)
        - localizationutil (localization)
        - quickstart (industry templates / verticals are a category by itself)
        - quickstartspain (industry templates / verticals are a category by itself)

## Choosing a db_prefix

### Modules created by Partners
- Use a db_prefix that do not begin with the letters ET
- EM is a reserved word not allowed as a db_prefix

### Modules created by Etendo and staff
- Use a db_prefix ETX where X: from one to 5 characters for the module itself

### Customization modules
- Use a db_prefix beginning with CUST

Usually customization modules are not intended to be published in Central Repository. In this case, DBPrefix should start with CUST. Modules with these kind of DBPrefixes cannot be registered in Central Repository but are collision safe because no other module in Central Repository can use this DBPrefix. This is an important decision to be taken before starting the module development: in case there is any chance of publishing the module at some moment, it should follow the standard rule, if it is absolutely sure that it will not be published you can use CUST and do not register it.

