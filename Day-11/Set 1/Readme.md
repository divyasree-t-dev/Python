# Loan Eligibility Engine

## Overview
A Python-based Loan Eligibility Engine that evaluates loan applications based on applicant details and predefined banking rules. It validates applicant information, checks eligibility criteria, and generates a loan decision report.

## Features
- Validates applicant details such as age, income, EMI, and credit score.
- Checks age eligibility (21–60 years).
- Evaluates the income-to-EMI ratio.
- Classifies credit scores into different categories.
- Supports salaried and self-employed applicants.
- Checks the number of existing loans.
- Uses `match-case` for credit score-based loan classification.
- Uses loops to process multiple applicants.
- Generates a formatted loan eligibility report.
- Supports an approval limit.

## Technologies Used
- Python 3.13
- Dataclasses
- Type Hints
- Match-Case
- Loops and Conditional Statements
- F-Strings

## Project Structure
```text
Set 1/
│
├── main.py
├── driver.py
└── README.md
```

## How to Run

1. Open the project folder in the terminal.
2. Activate the virtual environment.
3. Run the following command:

```bash
python driver.py
```

## Eligibility Criteria

| Criteria | Rule |
|---|---|
| Age | 21–60 years |
| Income-to-EMI Ratio | Minimum 3 |
| Credit Score | Minimum 650 |
| Existing Loans | Maximum 2 |
| Employment | Salaried / Self-employed |

## Output
The program generates a loan eligibility report containing:
- Applicant ID and Name
- Eligibility Status
- Interest Rate
- Loan Product
- Decision Reason

## Learning Outcomes
- Applying Python control statements in real-world scenarios.
- Implementing input validation and business rules.
- Working with dataclasses and type hints.
- Processing multiple records using loops.
- Generating structured reports using formatted strings.

---
**Assignment:** Day 11 – Set 1  
**Topic:** Loan Eligibility Engine  
**Language:** Python 3.13
