
from abc import ABC, abstractmethod
from enum import Enum


# 1. Vehicle Type Enum
class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    VAN = "Van"


# 2. Abstract Vehicle Class
class Vehicle(ABC):

    def __init__(self, registration_number, mileage, vehicle_type):
        self.registration_number = registration_number
        self.mileage = mileage
        self.vehicle_type = vehicle_type

    @property
    def registration_number(self):
        return self.__registration_number

    @registration_number.setter
    def registration_number(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Invalid registration number")
        self.__registration_number = value

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Mileage cannot be negative")
        self.__mileage = value

    @abstractmethod
    def daily_rate(self):
        pass

    @abstractmethod
    def late_fee(self, days):
        pass


# 3. Car Class
class Car(Vehicle):

    def __init__(self, registration_number, mileage):
        super().__init__(
            registration_number, mileage, VehicleType.CAR
        )

    def daily_rate(self):
        return 2000

    def late_fee(self, days):
        return days * 500


# 4. Bike Class
class Bike(Vehicle):

    def __init__(self, registration_number, mileage):
        super().__init__(
            registration_number, mileage, VehicleType.BIKE
        )

    def daily_rate(self):
        return 500

    def late_fee(self, days):
        return days * 100


# 5. Van Class
class Van(Vehicle):

    def __init__(self, registration_number, mileage):
        super().__init__(
            registration_number, mileage, VehicleType.VAN
        )

    def daily_rate(self):
        return 3000

    def late_fee(self, days):
        return days * 800


# 6. Customer Class
class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


# 7. Rental Class - Composition
class Rental:

    def __init__(self, rental_id, vehicle, customer, days, late_days=0):
        self.rental_id = rental_id
        self.vehicle = vehicle
        self.customer = customer
        self.days = days
        self.late_days = late_days

    def calculate_amount(self):
        rental_cost = self.vehicle.daily_rate() * self.days
        late_charge = self.vehicle.late_fee(self.late_days)

        return rental_cost + late_charge


# 8. Billing Class
class Billing:

    @staticmethod
    def generate_bill(rental):
        print(f"Rental ID      : {rental.rental_id}")
        print(f"Customer       : {rental.customer.name}")
        print(f"Vehicle        : {rental.vehicle.vehicle_type.value}")
        print(f"Registration   : {rental.vehicle.registration_number}")
        print(f"Rental Days    : {rental.days}")
        print(f"Daily Rate     : Rs.{rental.vehicle.daily_rate()}")
        print(f"Late Days      : {rental.late_days}")
        print(f"Total Amount   : Rs.{rental.calculate_amount()}")


# 9. Rental Manager Class
class RentalManager:

    def __init__(self):
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def display_rentals(self):
        print("\n" + "=" * 75)
        print("                     VEHICLE RENTAL REPORT")
        print("=" * 75)

        total_revenue = 0

        for rental in self.rentals:
            print(
                f"{rental.rental_id:<10} "
                f"{rental.customer.name:<15} "
                f"{rental.vehicle.vehicle_type.value:<10} "
                f"{rental.days:<10} "
                f"Rs.{rental.calculate_amount():.2f}"
            )

            total_revenue += rental.calculate_amount()

        print("-" * 75)
        print("Total Rentals :", len(self.rentals))
        print(f"Total Revenue : Rs.{total_revenue:.2f}")


# 10. Create Customers
customer1 = Customer("C001", "Arun")
customer2 = Customer("C002", "Priya")
customer3 = Customer("C003", "Kumar")
customer4 = Customer("C004", "Divya")


# 11. Create Vehicles
car1 = Car("TN01AB1234", 15000)
bike1 = Bike("TN02CD5678", 8000)
van1 = Van("TN03EF9012", 25000)
car2 = Car("TN04GH3456", 12000)


# 12. Create Rentals
rental1 = Rental("R001", car1, customer1, 3, 1)
rental2 = Rental("R002", bike1, customer2, 5, 2)
rental3 = Rental("R003", van1, customer3, 2, 1)
rental4 = Rental("R004", car2, customer4, 4, 0)


# 13. Manage Rentals
manager = RentalManager()

manager.add_rental(rental1)
manager.add_rental(rental2)
manager.add_rental(rental3)
manager.add_rental(rental4)


# 14. Display Rental Report
manager.display_rentals()


# 15. Generate Individual Bill
print("\n" + "=" * 75)
print("                     INDIVIDUAL RENTAL BILL")
print("=" * 75)

Billing.generate_bill(rental1)


# 16. Refactored Design Explanation
print("\n" + "=" * 75)
print("                 REFACTORED DESIGN")
print("=" * 75)

print("Vehicle Class  : Handles vehicle information and rental rules")
print("Customer Class : Stores customer information")
print("Rental Class   : Manages vehicle-customer rental relationship")
print("Billing Class  : Generates rental bills")
print("RentalManager  : Manages rental records and revenue")
