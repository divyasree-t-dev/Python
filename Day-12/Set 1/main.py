from abc import ABC, abstractmethod
from enum import Enum


# 1. Policy Status Enum
class PolicyStatus(Enum):
    DRAFT = "Draft"
    ACTIVE = "Active"
    LAPSED = "Lapsed"
    CANCELLED = "Cancelled"


# 2. Abstract Base Class
class Policy(ABC):

    def __init__(self, policy_number, holder_name, status):
        self.policy_number = policy_number
        self.holder_name = holder_name
        self.status = status

    @property
    def policy_number(self):
        return self.__policy_number

    @policy_number.setter
    def policy_number(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Policy number cannot be empty")
        self.__policy_number = value

    @abstractmethod
    def calculate_premium(self):
        pass

    def display_details(self):
        print(
            f"{self.policy_number:<12} "
            f"{self.holder_name:<15} "
            f"{self.status.value:<12} "
            f"Rs.{self.calculate_premium():.2f}"
        )


# 3. Motor Policy
class MotorPolicy(Policy):

    def __init__(self, policy_number, holder_name, status,
                 vehicle_value, rate):
        super().__init__(policy_number, holder_name, status)
        self.vehicle_value = vehicle_value
        self.rate = rate

    def calculate_premium(self):
        return self.vehicle_value * self.rate / 100


# 4. Health Policy
class HealthPolicy(Policy):

    def __init__(self, policy_number, holder_name, status,
                 age, coverage):
        super().__init__(policy_number, holder_name, status)
        self.age = age
        self.coverage = coverage

    def calculate_premium(self):
        premium = self.coverage * 0.02

        if self.age > 50:
            premium += premium * 0.25

        return premium


# 5. Travel Policy
class TravelPolicy(Policy):

    def __init__(self, policy_number, holder_name, status,
                 travel_days, daily_rate):
        super().__init__(policy_number, holder_name, status)
        self.travel_days = travel_days
        self.daily_rate = daily_rate

    def calculate_premium(self):
        return self.travel_days * self.daily_rate


# 6. Create 8 Policies in a List
policies = [

    MotorPolicy("M001", "Arun", PolicyStatus.ACTIVE, 500000, 2),

    HealthPolicy("H001", "Priya", PolicyStatus.ACTIVE, 45, 500000),

    TravelPolicy("T001", "Kumar", PolicyStatus.ACTIVE, 10, 150),

    MotorPolicy("M002", "Divya", PolicyStatus.DRAFT, 800000, 1.5),

    HealthPolicy("H002", "Rahul", PolicyStatus.ACTIVE, 55, 600000),

    TravelPolicy("T002", "Sneha", PolicyStatus.LAPSED, 15, 200),

    MotorPolicy("M003", "Vijay", PolicyStatus.ACTIVE, 1000000, 2.5),

    HealthPolicy("H003", "Meena", PolicyStatus.CANCELLED, 35, 400000)
]


# 7. Polymorphism - Single Report Loop
print("\n" + "=" * 65)
print("                 INSURANCE POLICY REPORT")
print("=" * 65)

print(f"{'POLICY NO':<12} {'HOLDER':<15} {'STATUS':<12} {'PREMIUM'}")
print("-" * 65)

total_premium = 0

for policy in policies:
    policy.display_details()
    total_premium += policy.calculate_premium()

print("-" * 65)
print(f"Total Policies  : {len(policies)}")
print(f"Total Premium   : Rs.{total_premium:.2f}")


# 8. Nested List - Monthly Collection by Region
monthly_collections = [

    [10000, 12000, 15000],  # North Region
    [20000, 18000, 22000],  # South Region
    [15000, 17000, 19000],  # East Region
    [25000, 23000, 21000]   # West Region
]

regions = ["North", "South", "East", "West"]

print("\n" + "=" * 65)
print("             MONTHLY PREMIUM COLLECTION")
print("=" * 65)

print(f"{'REGION':<12} {'MONTH 1':<12} {'MONTH 2':<12} "
      f"{'MONTH 3':<12} {'TOTAL'}")

print("-" * 65)

# Row totals
for i in range(len(monthly_collections)):
    row_total = sum(monthly_collections[i])

    print(
        f"{regions[i]:<12} "
        f"{monthly_collections[i][0]:<12} "
        f"{monthly_collections[i][1]:<12} "
        f"{monthly_collections[i][2]:<12} "
        f"{row_total}"
    )

# Column totals
column_totals = [
    sum(row[col] for row in monthly_collections)
    for col in range(3)
]

print("-" * 65)
print(f"{'TOTAL':<12} {column_totals[0]:<12} "
      f"{column_totals[1]:<12} {column_totals[2]:<12} "
      f"{sum(column_totals)}")


# 9. Open/Closed Principle - Add Home Policy
class HomePolicy(Policy):

    def __init__(self, policy_number, holder_name, status,
                 property_value, rate):
        super().__init__(policy_number, holder_name, status)
        self.property_value = property_value
        self.rate = rate

    def calculate_premium(self):
        return self.property_value * self.rate / 100


home_policy = HomePolicy(
    "HM001",
    "Divya",
    PolicyStatus.ACTIVE,
    5000000,
    0.5
)

print("\n" + "=" * 65)
print("              NEW HOME POLICY")
print("=" * 65)

home_policy.display_details()

print("\nHome Policy Premium: Rs.",
      f"{home_policy.calculate_premium():.2f}")

# Add Home Policy to existing list
policies.append(home_policy)

print("\nUpdated Policy Count:", len(policies))
