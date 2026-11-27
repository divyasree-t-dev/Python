
from dataclasses import dataclass

# ==========================================
# 1. APPLICANT DETAILS
# ==========================================

@dataclass
class Applicant:
    applicant_id: int
    name: str
    age: int
    income: float
    emi: float
    credit_score: int
    employment: str
    existing_loans: int

# ==========================================
# 2. STORE LOAN DECISION
# ==========================================

@dataclass
class Decision:
    applicant: Applicant
    status: str
    reason: str
    interest_rate: float
    loan_product: str
    valid: bool

# ==========================================
# 3. LOAN ELIGIBILITY FUNCTION
# ==========================================

def evaluate_applicant(applicant: Applicant) -> Decision:

    # Edge Case Validation

    if applicant.age < 0:
        return Decision(
            applicant, "INVALID", "Negative age",
            0.0, "N/A", False
        )

    if applicant.income <= 0:
        return Decision(
            applicant, "INVALID", "Zero or negative income",
            0.0, "N/A", False
        )

    if applicant.emi <= 0:
        return Decision(
            applicant, "INVALID", "Invalid EMI",
            0.0, "N/A", False
        )

    if not 300 <= applicant.credit_score <= 900:
        return Decision(
            applicant, "INVALID", "Score out of range",
            0.0, "N/A", False
        )

    if applicant.existing_loans < 0:
        return Decision(
            applicant, "INVALID", "Invalid loan count",
            0.0, "N/A", False
        )

    # ======================================
    # RULE 1: AGE ELIGIBILITY (21-60)
    # ======================================

    if applicant.age < 21:
        age_status: bool = False

    elif applicant.age <= 60:
        age_status = True

    else:
        age_status = False

    # ======================================
    # RULE 2: INCOME-TO-EMI RATIO
    # ======================================

    ratio: float = applicant.income / applicant.emi

    if ratio >= 3:
        income_status: bool = True

    else:
        income_status = False

    # ======================================
    # RULE 3: CREDIT SCORE BAND
    # ======================================

    if applicant.credit_score >= 750:
        credit_band: str = "Excellent"

    elif applicant.credit_score >= 700:
        credit_band = "Good"

    elif applicant.credit_score >= 650:
        credit_band = "Average"

    else:
        credit_band = "Low"

    # ======================================
    # MATCH/CASE: INTEREST RATE & LOAN PRODUCT
    # ======================================

    match credit_band:

        case "Excellent":
            interest_rate: float = 8.5
            loan_product: str = "Premium Loan"

        case "Good":
            interest_rate = 9.5
            loan_product = "Standard Loan"

        case "Average":
            interest_rate = 11.0
            loan_product = "Basic Loan"

        case _:
            interest_rate = 0.0
            loan_product = "Not Eligible"

    # ======================================
    # RULE 4: EMPLOYMENT TYPE
    # ======================================

    if applicant.employment.lower() == "salaried":

        employment_status: bool = True

    elif applicant.employment.lower() == "self-employed":

        if applicant.income >= 30000:
            employment_status = True

        else:
            employment_status = False

    else:
        employment_status = False

    # ======================================
    # RULE 5: EXISTING LOAN LIMIT
    # ======================================

    if applicant.existing_loans <= 2:
        loan_status: bool = True

    else:
        loan_status = False

    # ======================================
    # RULE 6: FINAL LOAN DECISION
    # ======================================

    if age_status:

        if income_status:

            if credit_band != "Low":

                if employment_status:

                    if loan_status:

                        final_status: str = "APPROVED"
                        reason: str = "All rules satisfied"

                    else:
                        final_status = "REJECTED"
                        reason = "Too many existing loans"

                else:
                    final_status = "REJECTED"
                    reason = "Employment criteria not met"

            else:
                final_status = "REJECTED"
                reason = "Low credit score"

        else:
            final_status = "REJECTED"
            reason = "Insufficient income-to-EMI ratio"

    else:
        final_status = "REJECTED"
        reason = "Age criteria not met"

    return Decision(
        applicant,
        final_status,
        reason,
        interest_rate,
        loan_product,
        True
    )

# ==========================================
# 4. PROCESS TEN APPLICANTS
# ==========================================

def process_applicants(
    applicants: list[Applicant],
    approval_limit: int = 3
) -> list[Decision]:

    results: list[Decision] = []

    approval_count: int = 0

    # Validate approval limit

    if approval_limit <= 0:
        raise ValueError(f"Approval limit must be greater than zero.")

    # Process each applicant

    for applicant in applicants:

        decision: Decision = evaluate_applicant(applicant)

        # Skip invalid applicant records

        if not decision.valid:
            results.append(decision)
            continue

        results.append(decision)

        # Count approved applications

        if decision.status == "APPROVED":

            approval_count += 1

            # Stop when daily approval limit is reached

            if approval_count >= approval_limit:

                print(f"\nDaily approval limit reached: {approval_limit}")
                break

    else:
        print(f"\nAll applicant records processed successfully.")

    return results