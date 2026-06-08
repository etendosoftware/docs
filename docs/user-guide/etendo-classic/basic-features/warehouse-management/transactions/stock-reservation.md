---
title: Stock Reservation
tags:
 - Stock Reservation
 - Warehouse Management
 - Inventory
 - Transactions
---

# Stock Reservation

:material-menu: `Application` > `Warehouse Management` > `Transactions` > `Stock Reservation`

## Overview

In this window, it is possible to review and manage existing Reservations.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Be_9LXecJY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Stock reservations are mainly used to ensure the stock availability when delivering a Sales Order. With this feature, it is also possible to lock stock not related to any Sales Order to avoid its consumption.

A reservation identifies certain stock in the warehouse that is reserved and cannot be consumed by anyone except the owner of the reservation. Currently, there are two possible owners, a _Sales Order line_ or the _System_. A reservation for a Sales Order line identifies stock that can only be consumed in shipments related to the Sales Order. A _System_ reservation is a special reservation type that cannot be consumed by anyone. _System_ reservations are used for _Hold_ reservations when some stock needs to be blocked in the warehouse.

!!! note
    Reservations are disabled by default. To be able to use them, please insert a new _Preference_ using property _Enable Stock Reservations_ with value _Y_. Then, end session and log in again to continue with the process.

This functionality comes with two types of reservations:

- Pre-Reservation: These are reservations that are not physically in the warehouse but ordered to a supplier and when there is a relationship between the line of the purchase order and a sales order line. Once the purchase order line is received, this pre-reservation is automatically converted to a reservation.
- Reservation: Refers to stock stored in the warehouse that is already reserved by a sales order line.

A reservation is always defined by the product that is desired to be reserved but other dimensions can be defined such as the warehouse, storage bin and attribute (i.e Colour, lots, serial number).

Another interesting thing is the possibility of allocating or not the reservation:

- _Allocated_ stock means that specific stock is reserved for a sales order, rather than it being a general reservation. That particular stock can not be reserved for any other sales order.
- A _Not Allocated_ reserved stock can be changed at any time by other existing stock but always ensuring that the Sales Order line keeps the reservation.

This functionality tries to cover several flows:

1.  Sales
2.  Procurement
3.  Purchasing plan (MRP)

## Sales Flow

A sales order can be reserved when the document is booked and pending to be delivered. The way to make the reservation is:

- Manual: No reservation is generated automatically. So when the order is booked the reservations needs to be done manually selecting the storage bin, attribute, etc.

- Automatic: The reservation is automatically created and processed, reserving the available stock.  This option reserves stock from any of the available warehouses belonging to the organization of the created sales order, not only from the warehouse defined in the order header.

- Automatic - Only default warehouse: The reservation is limited only to the warehouse specified in the header of the order. This allows optimizing inventory allocation and ensuring that products are allocated according to the warehouse preferences defined in each transaction.

    !!!info
        This last option is only available if the [Automated Warehouse Reservation](../../../optional-features/bundles/warehouse-extensions/overview.md#automated-warehouse-reservation) module is installed, part of the Warehouse Extensions Bundle. To do that, follow the instructions from the marketplace: [Warehouse Extensions Bundle](https://marketplace.etendo.cloud/#/product-details?module=EFDA39668E2E4DF2824FFF0A905E6A95){target="_blank"}.

For more information, visit [Sales Order](../../../../../user-guide/etendo-classic/basic-features/sales-management/transactions.md#sales-order).

## Procurement Flow

Pre-reservations can also be made from the Purchase Order. Being in the purchase order line, there is the possibility of selecting any sales order line pending to be delivered that is waiting to receive the goods in the warehouse. Once the items are received the pre-reservation is converted to reservation and the goods are reserved for that sales order line.

For more information, visit [Purchase Order](../../../../../user-guide/etendo-classic/basic-features/procurement-management/transactions.md#purchase-order).

## Purchasing Plan (MRP)

When launching the purchasing plan there is now the possibility of making reservations for Sales Order and pre-reservations, that is, create purchase orders linked to sales orders.

## Reservation Consumption

When a Good Shipment of a reserved Sales Order is automatically created, it will consume reserved stock. The process will propose first the possible allocated stock and later any available stock based on the standard rules to retrieve stock, including reserved stock but NOT allocated (even from other reservations). If the related Sales Order does not have any reservation, only not reserved stock is proposed.

When the Goods Shipment is processed the reservation is updated to reflect the stock that has been finally delivered and update the released quantity. In this step, there are several cases:

- All the stock of the shipment matches the reserved stock. The released quantity is updated accordingly.
- A different stock is shipped.
  - The stock is not reserved by any other reservation. The reservation is updated to reserve the shipped stock and if there was other stock reserved it is deleted from the reservation so the reserved quantity remains equal.
  - The stock is reserved and not allocated in another reservation. The other reservation is updated to search for other available stock.
    - If available stock is found, the other reservation is updated to reserve the found stock and the stock is reassigned to the current reservation.
    - If no available stock is found, an error is shown as the stock is not available. The user should change the stock of the good shipment or edit the other reservation to manually search or free the conflicting stock.
  - The stock is reserved and allocated in another reservation. An error is shown as the stock is not available. The user should change the stock of the good shipment or edit the other reservation to manually search or free the conflicting stock.

## Reservation

The desired product to be reserved is defined in the main tab.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-1.png)

The reservation header defines each reservation. First, the _Organization_ where the reservation is done and the _Product_ and _Quantity_ desired to be reserved are defined. When the reservation is for a Sales Order line, these fields are inherited from the line. Later, the owner of the reservation is defined, currently it is only possible to define Sales Order lines. If this is left blank, the reservation is considered a _System_ reservation where the owner is the _Organization_. Finally, it is possible to define certain dimensions to restrict the stock that can be used to fulfill the reservation:

- _Warehouse_
- _Storage Bin_
- _Attribute Set Value_

!!! note
    It is only possible to select warehouses that are defined as _on hand_ warehouses of the organization and storage bins that belong to them.

The reservation might have different statuses:

- **Draft**: The reservation might already have some stock lines, but those are not yet considered as reserved stock and are available to everyone.
- **Completed**: The reservation has been processed. If some stock was still pending to be reserved the _Complete_ process will try to reserve the available stock. This automatically reserved stock is left as not allocated.
- **Hold**: Any reservation can be set in hold status. This means that the stock is completely blocked and it is not even possible to generate a shipment for the sales order consuming the reserved stock. In this status, the button previously named "Put on Hold" changes to "Unhold" and gives the user the possibility to undo the action.
- **Closed**: A closed Reservation can not be reactivated afterwards. Also, when a Reservation is Closed, it's Quantity is set as the same value as the Released Quantity, preventing further inconsistency problems.

A reservation has 3 main quantities:

**Quantity**

Determines the quantity that is desired to be reserved. If the reservation is related to a Sales Order line this quantity must be the same as the Ordered Quantity.

**Reserved Qty**

It is the total quantity that is really reserved. When there is not enough stock available it is possible to have a lower _Reserved Qty_ than the _Quantity_.

**Released Qty**

It is the quantity that has been delivered and released from the reservation. When a Good Shipment for a reserved Sales Order is processed the Released Qty of the reservation is increased by the delivered quantity.

## Stock

The Stock tab identifies each existing Stock or Purchase Order selected to fulfill the reservation.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-2.png)

In the _Stock_ tab, the actual reserved stock is shown. The stock should meet the dimensions defined in the header. When the stock is physically in the warehouse the reserved stock is identified by the Storage Bin and the Attribute Set Value when applied. In case of pre-reservations the stock is still not in the warehouse, so the _Storage Bin_ property is blank and the _Purchase Order line_ is set. When a pre-reservation is receipt and converted to reservation the storage bin where the stock has been stored is set keeping the purchase order line.

The reserved stock has 2 quantities:

**Quantity**

The quantity reserved.

**Released Qty**

The quantity that has been released or delivered.

## Manage Stock

When the reservation is in _Draft_ or _Completed_ status, it is possible to modify the reserved stock using a _pick and execute_ process.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-3.png)

This window shows all the already reserved stock plus other available stock and not receipt Purchase Order Lines that can be used to fulfill the reservation. The available stock is filtered by the on hand warehouses of the reservation's organization and the dimensions that might be set. The Purchase Order lines are also filtered by these dimensions. For each selected line the quantity to reserve has to be set and if the stock is allocated or not. The quantity must be lower than the available quantity considering as well the quantity that might be reserved in other reservations and the sum of all the selected lines must be lower than the quantity desired to be reserved. If the reservation already has some released quantity, the quantity of the released stock must be higher or equal than the released stock

## Goods Movement

It is allowed to move an item that is reserved from its current storage bin to another one. The button _Goods movement_ shows all the bins where the product is reserved, that is, the stock lines and it  is also possible to edit the quantity to be moved and the new storage bin.

![Stock](../../../../../assets/user-guide/etendo-classic/basic-features/warehouse-management/transactions/stock-reservation/stock-reservation-4.png)

---

This work is a derivative of [Warehouse Management](http://wiki.openbravo.com/wiki/Warehouse_Management){target="\_blank"} by [Openbravo Wiki](http://wiki.openbravo.com/wiki/Welcome_to_Openbravo){target="\_blank"}, used under [CC BY-SA 2.5 ES](https://creativecommons.org/licenses/by-sa/2.5/es/){target="\_blank"}. This work is licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/){target="\_blank"} by [Etendo](https://etendo.software){target="\_blank"}.