
from dataclasses import dataclass


BASE_PREMIUM = 5000.0


@dataclass
class Customer:
    customer_id: int
    name: str
    age: int
    height: float
    weight: float


@dataclass
class PremiumResult:
    customer: Customer
    bmi: float
    category: str
    loading_rate: float
    loading_amount: float
    final_premium: float
    status: str
    reason: str


def calculate_bmi(height: float, weight: float) -> float:
    """Calculate BMI using height in metres and weight in kg."""

    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive.")

    bmi = weight / (height ** 2)

    return round(bmi, 2)


def get_bmi_category(bmi: float) -> tuple[str, float]:
    """Classify BMI and return its premium loading percentage."""

    match bmi:

        case value if value < 18.5:
            return "Underweight", 5.0

        case value if 18.5 <= value < 25:
            return "Normal", 0.0

        case value if 25 <= value < 30:
            return "Overweight", 10.0

        case value if value >= 30:
            return "Obese", 20.0

        case _:
            raise ValueError("Invalid BMI value.")


def calculate_premium(customer: Customer) -> PremiumResult:

    # Validate customer details
    if customer.age <= 0:
        raise ValueError("Age must be greater than zero.")

    if customer.age < 18 or customer.age > 60:
        return PremiumResult(
            customer, 0.0, "N/A", 0.0, 0.0, 0.0,
            "REJECTED", "Age must be between 18 and 60."
        )

    if customer.height <= 0:
        raise ValueError("Height must be greater than zero.")

    if customer.weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    bmi = calculate_bmi(customer.height, customer.weight)

    category, loading_rate = get_bmi_category(bmi)

    # Premium = Base premium + loading amount
    # Equivalent formula: Base premium * (1 + loading rate / 100)
    loading_amount = BASE_PREMIUM * (loading_rate / 100)

    final_premium = BASE_PREMIUM * (1 + loading_rate / 100)

    return PremiumResult(
        customer=customer,
        bmi=bmi,
        category=category,
        loading_rate=loading_rate,
        loading_amount=loading_amount,
        final_premium=round(final_premium, 2),
        status="APPROVED",
        reason="Premium calculated successfully."
    )


def create_customer(data: dict) -> Customer:
    """Convert raw batch data into a validated customer object."""

    try:
        customer = Customer(
            customer_id=int(data["customer_id"]),
            name=str(data["name"]).strip(),
            age=int(data["age"]),
            height=float(data["height"]),
            weight=float(data["weight"])
        )

    except (ValueError, TypeError, KeyError) as error:
        raise ValueError(f"Invalid customer data: {error}")

    if not customer.name:
        raise ValueError("Customer name cannot be empty.")

    return customer


def process_customer_batch(records: list[dict]) -> list[PremiumResult]:

    results = []

    print("\nProcessing customer records...\n")

    for record in records:

        try:
            customer = create_customer(record)

            result = calculate_premium(customer)

            results.append(result)

        except ValueError as error:
            print(
                f"Customer ID: {record.get('customer_id', 'Unknown')} "
                f"| INVALID | {error}"
            )

    return results


def display_report(results: list[PremiumResult]) -> None:

    print("\n" + "=" * 105)
    print("                         INSURANCE PREMIUM REPORT")
    print("=" * 105)

    print(
        f"{'ID':<8}"
        f"{'Name':<15}"
        f"{'Age':>6}"
        f"{'BMI':>9}"
        f"{'Category':<15}"
        f"{'Loading':>10}"
        f"{'Premium':>14}"
        f"{'Status':>13}"
    )

    print("-" * 105)

    approved = 0
    rejected = 0
    total_premium = 0.0

    for result in results:

        customer = result.customer

        print(
            f"{customer.customer_id:<8}"
            f"{customer.name:<15}"
            f"{customer.age:>6}"
            f"{result.bmi:>9.2f}"
            f"{result.category:<15}"
            f"{result.loading_rate:>9.1f}%"
            f"{result.final_premium:>14.2f}"
            f"{result.status:>13}"
        )

        if result.status == "APPROVED":
            approved += 1
            total_premium += result.final_premium

        else:
            rejected += 1

    print("-" * 105)

    print(f"Approved Customers : {approved}")
    print(f"Rejected Customers : {rejected}")
    print(f"Total Premium      : Rs. {total_premium:.2f}")

    print("=" * 105)
