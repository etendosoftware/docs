---
title: Route Optimization - Status Codes
---
## Status code

### 200
**Successful Operation**

The route was generated correctly without errors


### 400
**Validator Error**

The route was generated, although with validation exceptions

Possible validator errors thrown:
- The delivery <delivery_id> needs all demand values equal 0: only checked for depot.
- The delivery <delivery_id> needs at least one demand value > 0: only checked for deliveries.
- The demand type/s <demand_types> are not covered by any vehicle: all types of delivery demands must be able to be covered by at least one vehicle.
- The vehicle <vehicle_id> had a minimum capacity greater or equal than its maximum: if this does happen the minimum is set to zero.
- The time window of delivery <delivery_id> is not in any of the vehicles: no vehicle can arrive in the delivery time window.
- The delivery <delivery_id> can not pick up : the depot cannot have setting pick up in true.
- The delivery <delivery_id> needs a valid reference_id: if a delivery pick up is set to true it must have a valid reference_id.
- The delivery <delivery_id> no need reference_id or must be pick up: you cannot have a reference to delivery if pick up is set to false.
- The vehicle <vehicle_id> has no time work: the vehicle does not have working start and end times so it cannot find a route. 


### 500
**Fatal or Internal Server Error**

The route could not be generated due to a fatal error or something has gone wrong while communicating with the web server 

Possible fatal errors thrown:
- OSRM not found: the OSRM server was not found 
- OSRM maximum number of nodes: <MAX_NODES>
- The VRPRA constraint must necessarily be combined with some other restriction
- No vehicle's finishing time can surpass the depot's closing time 
- The demand type/s of a location is not covered by any vehicle 
- The VRPTWP constraint must necessarily be combined with VRPTW
- The delivery location need at least one demand value > 0
- The delivery <delivery_id> need at least one demand value > 0
- Missing coordinate data in delivery <delivery_id>
- The delivery <delivery_id> need time windows
- No valid constraints: no constraint was added in the input or the constraints that were added are not valid.
- No solution found for the given parameters: max_time_route_vehicle: <time_route>, max_time_allow_vehicle: <time_allow>, vehicle_max_distance: <max_distance>, solution_limit: <solution_limit>
