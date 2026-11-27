from main import Applicant, Decision, process_applicants


# ==========================================
# 1. CREATE TEN APPLICANT RECORDS
# ==========================================

applicants: list[Applicant] = [

    Applicant(101, "Arun", 28, 60000, 15000, 780, "salaried", 1),

    Applicant(102, "Bala", 19, 40000, 10000, 720, "salaried", 0),

    Applicant(103, "Charan", 35, 0, 10000, 750, "salaried", 1),

    Applicant(104, "Divya", 30, 80000, 20000, 730, "salaried", 2),

    Applicant(105, "Ezhil", 40, 50000, 10000, 620, "salaried", 1),

    Applicant(106, "Farhan", 45, 90000, 20000, 810, "self-employed", 1),

    Applicant(107, "Gokul", 25, 30000, 5000, 680, "salaried", 0),

    Applicant(108, "Hari", 65, 70000, 15000, 760, "salaried", 1),

    Applicant(109, "Indhu", 32, 45000, 15000, 710, "self-employed", 1),

    Applicant(110, "Jeeva", 29, 50000, 10000, 740, "salaried", 3)

]


# ==========================================
# 2. PROCESS LOAN APPLICATIONS
# ==========================================

results: list[Decision] = process_applicants(
    applicants,
    approval_limit=10
)


# ==========================================
# 3. DISPLAY DECISION TABLE
# ==========================================

print(f"\n{'=' * 100}")
print(f"{'BANK LOAN ELIGIBILITY REPORT':^100}")
print(f"{'=' * 100}")

print(
    f"{'ID':<8}"
    f"{'NAME':<12}"
    f"{'AGE':<8}"
    f"{'CREDIT':<10}"
    f"{'STATUS':<12}"
    f"{'RATE (%)':<12}"
    f"{'LOAN PRODUCT':<20}"
    f"{'REASON'}"
)

print(f"{'-' * 100}")


# ==========================================
# 4. DISPLAY EACH APPLICANT'S DECISION
# ==========================================

for result in results:

    applicant: Applicant = result.applicant

    print(
        f"{applicant.applicant_id:<8}"
        f"{applicant.name:<12}"
        f"{applicant.age:<8}"
        f"{applicant.credit_score:<10}"
        f"{result.status:<12}"
        f"{result.interest_rate:<12.2f}"
        f"{result.loan_product:<20}"
        f"{result.reason}"
    )


# ==========================================
# 5. DISPLAY SUMMARY
# ==========================================

total_processed: int = len(results)

total_approved: int = sum(
    1 for result in results
    if result.status == "APPROVED"
)

total_rejected: int = sum(
    1 for result in results
    if result.status == "REJECTED"
)

total_invalid: int = sum(
    1 for result in results
    if result.status == "INVALID"
)

print(f"\n{'=' * 100}")
print(f"{'APPLICATION SUMMARY':^100}")
print(f"{'=' * 100}")

print(f"Total applicants processed : {total_processed}")
print(f"Approved applications     : {total_approved}")
print(f"Rejected applications     : {total_rejected}")
print(f"Invalid applications      : {total_invalid}")

print(f"{'=' * 100}")
