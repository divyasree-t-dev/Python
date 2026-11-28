
# Vehicle Rental System

## 1. Project Overview

This project implements a Vehicle Rental System using Python Object-Oriented Programming concepts.

A car rental company provides different types of vehicles such as Cars, Bikes and Vans. Each vehicle has different daily rental rates and late fee rules.

The system manages customers, vehicles, rental records, billing and revenue calculation.

It demonstrates abstraction, inheritance, encapsulation, polymorphism, composition and the Single Responsibility Principle.

## 2. Business Scenario

A vehicle rental company needs a system to:
- Manage different types of vehicles.
- Calculate daily rental charges.
- Apply different late fee rules.
- Maintain customer and rental information.
- Generate individual rental bills.
- Calculate total revenue from all rentals.
- Separate responsibilities into different classes.

## 3. Technologies Used

- Programming Language: Python 3.13
- Concepts: Object-Oriented Programming
- Modules: abc, enum

## 4. Project Structure

```text
Set2_Vehicle_Rental_System/
│
├── main.py
├── README.md
└── class_diagram.md
```

## 5. Tasks Implemented

### Task 1: VehicleType Enum and Abstract Class

Created a VehicleType enum with three vehicle types:

- CAR
- BIKE
- VAN

Created an abstract base class named Vehicle.

It contains two abstract methods:

- daily_rate()
- late_fee(days)

Every vehicle subclass implements these methods according to its rental rules.

### Task 2: Inheritance and Encapsulation

Created three subclasses:

1. Car
2. Bike
3. Van

Each subclass inherits from Vehicle and implements its own daily rental rate and late fee calculation.

Used private attributes:

- __registration_number
- __mileage

Used properties with validation to control access to these attributes.

### Task 3: Composition

Created a Customer class to store customer information.

Created a Rental class that contains:

- A Vehicle object.
- A Customer object.

This demonstrates HAS-A relationships through composition.

The rental amount is calculated using:

Rental Amount = (Daily Rate × Rental Days) + Late Fee

### Task 4: Polymorphism and Revenue Calculation

Created a list to store current rental objects.

Used a single for loop to calculate the rental amount for different vehicle types.

The system generates a rental report and calculates total revenue.

### Task 5: God Class Refactoring

A God class performs too many responsibilities in one class.

Instead, the system is divided into separate classes:

- Vehicle: Manages vehicle information and rental rules.
- Customer: Manages customer information.
- Rental: Manages rental relationships and calculations.
- Billing: Generates individual bills.
- RentalManager: Manages rental records and revenue reports.

This follows the Single Responsibility Principle (SRP).

## 6. Vehicle Rental Rules

| Vehicle | Daily Rate | Late Fee Per Day |
|---|---:|---:|
| Car | Rs.2,000 | Rs.500 |
| Bike | Rs.500 | Rs.100 |
| Van | Rs.3,000 | Rs.800 |

## 7. Sample Output

```text
VEHICLE RENTAL REPORT

R001       Arun            Car        3          Rs.6500.00
R002       Priya           Bike       5          Rs.2700.00
R003       Kumar           Van        2          Rs.6800.00
R004       Divya           Car        4          Rs.8000.00

Total Rentals : 4
Total Revenue : Rs.24000.00

INDIVIDUAL RENTAL BILL

Rental ID      : R001
Customer       : Arun
Vehicle        : Car
Registration   : TN01AB1234
Rental Days    : 3
Daily Rate     : Rs.2000
Late Days      : 1
Total Amount   : Rs.6500

REFACTORED DESIGN

Vehicle Class  : Handles vehicle information and rental rules
Customer Class : Stores customer information
Rental Class   : Manages vehicle-customer rental relationship
Billing Class  : Generates rental bills
RentalManager  : Manages rental records and revenue
```

## 8. How to Run

1. Install Python 3.13.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute the following command:

```bash
python main.py
```

## 9. OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Enum | VehicleType |
| Abstraction | Abstract Vehicle class |
| Inheritance | Car, Bike and Van |
| Encapsulation | Private attributes |
| Properties | Getters and setters |
| Composition | Rental HAS-A Vehicle and Customer |
| Polymorphism | Common rental calculation loop |
| Lists | Current rental records |
| SRP | Separate responsibility classes |

## 10. Composition vs Inheritance

### Inheritance (IS-A)

- Car IS-A Vehicle.
- Bike IS-A Vehicle.
- Van IS-A Vehicle.

### Composition (HAS-A)

- Rental HAS-A Vehicle.
- Rental HAS-A Customer.

Inheritance is used when classes share a common parent structure. Composition is used when one object contains or works with other objects.

### Conclusion

The Vehicle Rental System demonstrates how Python OOP concepts can be applied to a real-world rental business.

The system supports multiple vehicle types, individual rental rules, customer management, billing and revenue reporting through a modular and maintainable design.
