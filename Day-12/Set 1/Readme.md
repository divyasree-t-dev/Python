
# Insurance Policy Hierarchy

## 1. Project Overview

This project implements an Insurance Policy Management System using Python Object-Oriented Programming concepts.

An insurance company offers different types of policies such as Motor, Health, Travel and Home insurance. Each policy has its own premium calculation formula, but all policies follow a common structure and reporting interface.

The system demonstrates inheritance, encapsulation, abstraction, polymorphism, enums, lists and nested lists.

## 2. Business Scenario

An insurer manages multiple insurance policies with different premium calculation rules.

The system should:
- Maintain policy details and status.
- Calculate premiums based on policy type.
- Generate a common policy report.
- Calculate monthly premium collections by region.
- Support adding new policy types without modifying existing classes.

## 3. Technologies Used

- Programming Language: Python 3.13
- Concepts: Object-Oriented Programming
- Modules: abc, enum

## 4. Project Structure

```text
Set1_Insurance_Policy_Hierarchy/
│
├── main.py
├── README.md
└── class_diagram.md
```

## 5. Tasks Implemented

### Task 1: PolicyStatus Enum

Created a PolicyStatus enum with four predefined values:

- DRAFT
- ACTIVE
- LAPSED
- CANCELLED

This ensures that only valid policy statuses are used.

### Task 2: Abstract Base Class and Inheritance

Created an abstract base class named Policy.

Features:
- Implemented calculate_premium() as an abstract method.
- Used @property to access the policy number.
- Used a setter to validate the policy number.
- Protected the policy number using a private attribute (__policy_number).

Created four subclasses:

1. MotorPolicy
2. HealthPolicy
3. TravelPolicy
4. HomePolicy

Each subclass implements its own premium calculation formula.

### Task 3: Polymorphism

Created a list containing eight policy objects.

Used a single for loop to generate the policy report and calculate premiums.

Each policy object executes its own calculate_premium() method based on its class.

This demonstrates runtime polymorphism.

### Task 4: Nested Lists

Created a two-dimensional list to store monthly premium collections across four regions:

- North
- South
- East
- West

Calculated:
- Total monthly collection for each region (row total).
- Total collection for each month (column total).
- Overall premium collection.

### Task 5: Open/Closed Principle

Added a new HomePolicy subclass without modifying the existing policy classes.

The new class extends the abstract Policy class and implements its own premium calculation method.

This follows the Open/Closed Principle:

Software entities should be open for extension but closed for modification.

## 6. Premium Calculation Rules

| Policy Type | Premium Calculation |
|---|---|
| Motor | Vehicle Value × Rate / 100 |
| Health | Coverage × 2% |
| Health (Age > 50) | Base Premium + 25% |
| Travel | Travel Days × Daily Rate |
| Home | Property Value × Rate / 100 |

## 7. Sample Output

```text
INSURANCE POLICY REPORT

POLICY NO    HOLDER          STATUS       PREMIUM
M001         Arun            Active       Rs.10000.00
H001         Priya           Active       Rs.10000.00
T001         Kumar           Active       Rs.1500.00
M002         Divya           Draft        Rs.12000.00
H002         Rahul           Active       Rs.15000.00
T002         Sneha           Lapsed       Rs.3000.00
M003         Vijay           Active       Rs.25000.00
H003         Meena           Cancelled    Rs.8000.00

Total Policies  : 8
Total Premium   : Rs.84500.00

MONTHLY PREMIUM COLLECTION

REGION       MONTH 1      MONTH 2      MONTH 3      TOTAL
North        10000        12000        15000        37000
South        20000        18000        22000        60000
East         15000        17000        19000        51000
West         25000        23000        21000        69000

TOTAL        70000        70000        77000        217000

NEW HOME POLICY

HM001        Divya           Active       Rs.25000.00

Updated Policy Count: 9
```

## 8. How to Run

1. Install Python 3.13.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

```bash
python main.py
```

## 9. OOP Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Enum | PolicyStatus |
| Abstraction | Abstract Policy class |
| Encapsulation | Private policy number |
| Property | Getter and setter |
| Inheritance | Policy subclasses |
| Polymorphism | Common reporting loop |
| Lists | Eight policy objects |
| Nested Lists | Monthly regional collections |
| Open/Closed Principle | Adding HomePolicy |

## 10. Conclusion

The Insurance Policy Hierarchy project demonstrates how Python OOP concepts can be applied to a real-world insurance management scenario.

The design supports different policy types, individual premium calculations and a common reporting interface. It also allows new policy types to be added without modifying existing implementations.
