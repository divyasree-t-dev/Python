
# Hospital Billing Model

## 1. Project Overview

This project implements a Hospital Billing System using Python Object-Oriented Programming concepts.

A hospital provides different types of medical visits, including Outpatient, Inpatient and Emergency visits. Each visit type follows different billing rules but uses a common invoice structure.

The system manages patients, doctors, visits, billing calculations and department-wise monthly collections.

It demonstrates abstraction, inheritance, encapsulation, polymorphism, composition, enums and nested lists.

## 2. Business Scenario

A hospital needs a billing system to:

- Manage patient and doctor information.
- Handle different types of hospital visits.
- Calculate bills based on visit type.
- Generate a common billing report.
- Associate patients and doctors with visits.
- Calculate department-wise monthly collections.
- Demonstrate correct usage of inheritance and composition.

## 3. Technologies Used

- Programming Language: Python 3.13
- Concepts: Object-Oriented Programming
- Modules: abc, enum

## 4. Project Structure

```text
Set3_Hospital_Billing_Model/
│
├── main.py
├── README.md
└── class_diagram.md
```

## 5. Tasks Implemented

### Task 1: VisitType Enum and Abstract Class

Created a VisitType enum with three predefined values:

- OUTPATIENT
- INPATIENT
- EMERGENCY

Created an abstract base class named Visit.

It contains:
- An abstract calculate_bill() method.
- Common visit information.
- A common display_bill() method.

### Task 2: Inheritance and Read-only Property

Created three subclasses:

1. OutPatientVisit
2. InPatientVisit
3. EmergencyVisit

Each subclass implements its own billing calculation.

The patient identifier is exposed through a read-only property using @property without a setter.

### Task 3: Composition

Created two separate classes:

- Patient: Stores patient ID and name.
- Doctor: Stores doctor ID, name and department.

The Visit class contains references to both Patient and Doctor objects.

This demonstrates the HAS-A relationship through composition.

### Task 4: Polymorphism and Nested Lists

Created a list containing six different visit objects.

Used a single for loop to generate the hospital billing report and calculate total revenue.

Created a two-dimensional list to maintain department-wise monthly collections.

Calculated:
- Department-wise row totals.
- Month-wise column totals.
- Overall monthly collection.

### Task 5: Inheritance vs Composition

An incorrect design would be making Patient inherit from Doctor.

This is wrong because a Patient is not a type of Doctor.

The correct design uses composition:

- Visit HAS-A Patient.
- Visit HAS-A Doctor.

Both objects are associated with a Visit instead of creating an incorrect inheritance relationship.

## 6. Billing Calculation Rules

| Visit Type | Billing Rule |
|---|---|
| Outpatient | Consultation Fee |
| Inpatient | Number of Days × Daily Charge |
| Emergency | Treatment Charge + Surcharge |

## 7. Sample Output

```text
HOSPITAL BILLING REPORT

VISIT ID   PATIENT         DEPARTMENT      VISIT TYPE   BILL AMOUNT
V001       Arun            Cardiology      Outpatient   Rs.800.00
V002       Priya           Orthopedics     Inpatient    Rs.6000.00
V003       Kumar           Neurology       Emergency    Rs.6500.00
V004       Divya           Orthopedics     Outpatient   Rs.1000.00
V005       Rahul           Cardiology      Inpatient    Rs.12500.00
V006       Sneha           Neurology       Emergency    Rs.9000.00

Total Visits : 6
Total Revenue: Rs.35800.00

DEPARTMENT-WISE MONTHLY COLLECTION

Cardiology      10000        12000        15000        37000
Orthopedics     8000         10000        9000         27000
Neurology       15000        13000        17000        45000

TOTAL           33000        35000        41000        109000
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
| Enum | VisitType |
| Abstraction | Abstract Visit class |
| Inheritance | OutPatientVisit, InPatientVisit, EmergencyVisit |
| Encapsulation | Read-only patient identifier property |
| Polymorphism | Common billing loop |
| Composition | Visit HAS-A Patient and Doctor |
| Lists | Visit objects |
| Nested Lists | Department-wise monthly totals |

## 10. Conclusion

The Hospital Billing Model demonstrates how Python OOP concepts can be applied to a real-world hospital billing scenario.

The system supports multiple visit types, individual billing rules, patient and doctor associations, common invoice reporting and department-wise monthly collection calculations.

The design uses inheritance for shared visit behaviour and composition for relationships between patients, doctors and visits.
