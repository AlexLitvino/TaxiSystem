# TaxiSystem

## Overview
This is example for system consisting of several interacting classes.  
Also provided UML class diagram to understand dependencies between classes.  

There are two roles: Client and Driver.  
Client could make order for a taxi ride specifying location and car class.  
The nearest available driver should be assigned for a ride.  


## Description
Classes Client and Driver are inherited from User class.  
Driver could add Car object to itself.  
System is based on [Mediator](https://refactoring.guru/design-patterns/mediator) design pattern.  
Class Manager contains all clients and drivers and connects them.  
Client makes order and then manager looks for the nearest available driver.    

Class Navigator encapsulates map of the city.  
Currently, map is one-dimensional (address has one coordinate).  
It is preferably to add Location class, so main logic will not be changed when moving to 2D-map.  
Navigator provides methods to get/add/update/delete location, calculate distance between locations, download map from file.  
Map is kept in json file (dictionary location: coordinate).  

Several random maps provided in [maps](maps) directory.
A random map could be generated using [map generator](maps/map_generator.py) 


## Workflow
Create Navigator object for specific city. Map file should be located at `maps` directory and named `<city>.json`:
```python
navigator = Navigator("kharkiv")
```
Create Manager object with created navigator:
```python
manager = Manager(navigator)
```
Create drivers, add car for them and set to state looking for orders:
```python
driver1 = Driver(manager, name='John', date_of_birth=1974, licence_number='QQ324232')
driver1.add_car(plate_number='QW464', car_class=CarClass.Economy, model='Lanos', color=Color.BLUE)
driver1.look_for_order()
```
Create clients:
```python
client1 = Client(manager, 'Olga', 1995)
```

## TODOs
- [ ] Add possibility to have several cars for driver
- [ ] What if several drivers will be found?
- [ ] Add more sophisticated flow (driver takes order, removed from active users (can't be assigned to new ride till he is done with previous ride))
- [ ] Add possibility add/update/remove location (Client could suggest adding, Admin should confirm added, add/update/remove, need a new role for Admin) 
- [ ] Add 2D map
- [ ] Add tests
- [ ] Add account for clients and drivers, payment logic
- [ ] Add bonus system for Clients based on rode distance
- [ ] Add rates for Drivers
