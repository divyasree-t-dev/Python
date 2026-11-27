
from main import process_customer_batch, display_report


def main() -> None:

    print("=" * 60)
    print("             INSURANCE PREMIUM CALCULATOR")
    print("=" * 60)

    customer_records = [

        {
            "customer_id": "101",
            "name": "Arun",
            "age": "25",
            "height": "1.75",
            "weight": "70"
        },

        {
            "customer_id": "102",
            "name": "Bala",
            "age": "30",
            "height": "1.70",
            "weight": "50"
        },

        {
            "customer_id": "103",
            "name": "Charan",
            "age": "35",
            "height": "1.65",
            "weight": "78"
        },

        {
            "customer_id": "104",
            "name": "Divya",
            "age": "40",
            "height": "1.60",
            "weight": "85"
        },

        {
            "customer_id": "105",
            "name": "Ezhil",
            "age": "16",
            "height": "1.55",
            "weight": "45"
        },

        {
            "customer_id": "106",
            "name": "Farhan",
            "age": "abc",
            "height": "1.75",
            "weight": "70"
        },

        {
            "customer_id": "107",
            "name": "Gokul",
            "age": "28",
            "height": "invalid",
            "weight": "65"
        },

        {
            "customer_id": "108",
            "name": "Hari",
            "age": "45",
            "height": "1.80",
            "weight": "95"
        }
    ]

    results = process_customer_batch(customer_records)

    display_report(results)

    print("\nInsurance premium calculation completed.")


if __name__ == "__main__":
    main()
