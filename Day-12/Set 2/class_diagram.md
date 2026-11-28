
# Vehicle Rental System – Class Diagram

## UML Class Diagram

```mermaid
classDiagram

    class VehicleType {
        <<enumeration>>
        CAR
        BIKE
        VAN
    }

    class Vehicle {
        <<abstract>>
        -__registration_number: str
        -__mileage: float
        +vehicle_type: VehicleType
        +registration_number: str
        +mileage: float
        +daily_rate()* float
        +late_fee(days)* float
    }

    class Car {
        +daily_rate() float
        +late_fee(days) float
    }

    class Bike {
        +daily_rate() float
        +late_fee(days) float
    }

    class Van {
        +daily_rate() float
        +late_fee(days) float
    }

    class Customer {
        +customer_id: str
        +name: str
    }

    class Rental {
        +rental_id: str
        +vehicle: Vehicle
        +customer: Customer
        +days: int
        +late_days: int
        +calculate_amount() float
    }

    class Billing {
        +generate_bill(rental)$
    }

    class RentalManager {
        -rentals: list
        +add_rental(rental)
        +display_rentals()
    }

    Vehicle <|-- Car
    Vehicle <|-- Bike
    Vehicle <|-- Van

    Vehicle --> VehicleType : uses

    Rental *-- Vehicle : contains
    Rental *-- Customer : contains

    Billing ..> Rental : generates bill
    RentalManager o-- Rental : manages
```

## Class Descriptions

### 1. VehicleType
An enumeration that defines the available vehicle types:
- CAR
- BIKE
- VAN

### 2. Vehicle (Abstract Class)
The common parent class for all vehicles.

Responsibilities:
- Store registration number, mileage and vehicle type.
- Validate registration number and mileage.
- Define daily_rate() and late_fee() as abstract methods.

### 3. Car
Inherits from Vehicle.

- Daily rate: Rs.2,000
- Late fee: Rs.500 per day.

### 4. Bike
Inherits from Vehicle.

- Daily rate: Rs.500
- Late fee: Rs.100 per day.

### 5. Van
Inherits from Vehicle.

- Daily rate: Rs.3,000
- Late fee: Rs.800 per day.

### 6. Customer
Stores customer ID and customer name.

### 7. Rental
Represents a rental transaction.

Contains:
- One Vehicle object.
- One Customer object.
- Rental duration.
- Late days.

Calculates the total rental amount.

### 8. Billing
Generates individual rental bills.

### 9. RentalManager
Maintains the rental list, displays rental reports and calculates total revenue.

## Relationships

- Car, Bike and Van inherit from Vehicle.
- Rental contains Vehicle and Customer objects (HAS-A relationship).
- Billing uses Rental to generate bills.
- RentalManager manages multiple Rental objects.
- Vehicle uses VehicleType to identify the vehicle category.

## Design Principles

### Composition
Rental contains Vehicle and Customer objects instead of inheriting from them.

### Single Responsibility Principle
Each class handles a separate responsibility, making the system modular and maintainable.
