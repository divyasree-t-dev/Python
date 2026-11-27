
from main import collect_monthly_readings, display_annual_report


def main() -> None:

    print("=" * 50)
    print("         ELECTRICITY BILLING SYSTEM")
    print("=" * 50)

    bills = collect_monthly_readings()

    if bills:
        display_annual_report(bills)

    else:
        print("\nNo monthly readings were entered.")

    print("\nBilling process completed.")


if __name__ == "__main__":
    main()
