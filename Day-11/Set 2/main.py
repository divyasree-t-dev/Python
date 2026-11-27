
from dataclasses import dataclass


@dataclass
class Bill:
    month: str
    units: float
    category: str
    energy_charge: float
    fixed_charge: float
    surcharge: float
    rebate: float
    total: float


def calculate_energy_charge(units: float) -> float:
    """Calculate electricity charges using four progressive slabs."""

    if units < 0:
        raise ValueError("Units cannot be negative.")

    charge = 0.0

    if units <= 100:
        charge = units * 1.50

    elif units <= 200:
        charge = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 400:
        charge = (
            (100 * 1.50)
            + (100 * 2.50)
            + ((units - 200) * 4.00)
        )

    else:
        charge = (
            (100 * 1.50)
            + (100 * 2.50)
            + (200 * 4.00)
            + ((units - 400) * 6.00)
        )

    return charge


def get_fixed_charge(category: str) -> float:
    """Return fixed charge based on consumer category."""

    match category.lower():

        case "domestic":
            return 50.0

        case "commercial":
            return 150.0

        case "industrial":
            return 300.0

        case _:
            raise ValueError("Invalid consumer category.")


def calculate_bill(
    month: str,
    units: float,
    category: str
) -> Bill:

    if units < 0:
        raise ValueError("Units cannot be negative.")

    energy_charge = calculate_energy_charge(units)
    fixed_charge = get_fixed_charge(category)

    surcharge = 0.0
    rebate = 0.0

    # Surcharge and rebate conditions
    if energy_charge >= 5000:
        surcharge = energy_charge * 0.05

    elif units <= 100:
        rebate = energy_charge * 0.02

    total = (
        energy_charge
        + fixed_charge
        + surcharge
        - rebate
    )

    return Bill(
        month=month,
        units=units,
        category=category.title(),
        energy_charge=energy_charge,
        fixed_charge=fixed_charge,
        surcharge=surcharge,
        rebate=rebate,
        total=total
    )


def display_annual_report(bills: list[Bill]) -> None:
    """Display monthly bills for up to 12 months."""

    print("\n" + "=" * 105)
    print("                         ANNUAL ELECTRICITY BILL REPORT")
    print("=" * 105)

    print(
        f"{'Month':<12}"
        f"{'Units':>10}"
        f"{'Energy':>13}"
        f"{'Fixed':>12}"
        f"{'Surcharge':>13}"
        f"{'Rebate':>12}"
        f"{'Total':>13}"
    )

    print("-" * 105)

    annual_total = 0.0

    for index in range(12):

        if index < len(bills):
            bill = bills[index]

            print(
                f"{bill.month:<12}"
                f"{bill.units:>10.2f}"
                f"{bill.energy_charge:>13.2f}"
                f"{bill.fixed_charge:>12.2f}"
                f"{bill.surcharge:>13.2f}"
                f"{bill.rebate:>12.2f}"
                f"{bill.total:>13.2f}"
            )

            annual_total += bill.total

        else:
            print(f"{'Month ' + str(index + 1):<12}{'No reading':>10}")

    print("-" * 105)
    print(f"{'Annual Total Bill:':>80} Rs. {annual_total:.2f}")
    print("=" * 105)


def collect_monthly_readings() -> list[Bill]:
    """Collect meter readings until 12 months or user enters q."""

    bills = []

    print("\nUTILITY BILLING CALCULATOR")
    print("-" * 40)

    while True:
        category = input(
            "Enter consumer category (Domestic/Commercial/Industrial): "
        ).strip()

        if category.lower() in ("domestic", "commercial", "industrial"):
            break

        print("Invalid category. Please try again.")

    # Starting meter reading
    while True:
        try:
            previous_reading = float(
                input("Enter initial meter reading: ")
            )

            if previous_reading < 0:
                print("Reading cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid numeric reading.")

    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    while len(bills) < 12:

        month = month_names[len(bills)]

        user_input = input(
            f"\nEnter {month} meter reading (or q to quit): "
        ).strip()

        if user_input.lower() == "q":
            print("Reading collection stopped.")
            break

        try:
            current_reading = float(user_input)

            if current_reading < 0:
                print("Reading cannot be negative.")
                continue

            if current_reading < previous_reading:
                print("Current reading cannot be less than previous reading.")
                continue

            units = current_reading - previous_reading

            bill = calculate_bill(month, units, category)

            bills.append(bill)

            print(
                f"{month} bill calculated successfully: "
                f"Rs. {bill.total:.2f}"
            )

            previous_reading = current_reading

        except ValueError:
            print("Invalid input. Enter a numeric reading or q.")

    return bills
