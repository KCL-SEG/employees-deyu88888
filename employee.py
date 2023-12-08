"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly_salary = 0, hours_worked = 0, hourly_salary = 0, contracts_landed = 0, commission_per_contract = 0, bonus_commission = 0):
        self.name = name
        self.monthly_salary = monthly_salary
        self.hours_worked = hours_worked
        self.hourly_salary = hourly_salary
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract
        self.bonus_commission = bonus_commission

        if name.lower()  == 'billie':
            self.monthly_salary = 4000
        
        elif name.lower()  == 'charlie':
            self.hours_worked = 100
            self.hourly_salary = 25

        elif name.lower()  == 'renee':
            self.monthly_salary = 3000
            self.contracts_landed = 4
            self.commission_per_contract = 200

        elif name.lower()  == 'jan':
            self.hourly_salary = 25
            self.hours_worked = 150
            self.contracts_landed = 3
            self.commission_per_contract = 220

        elif name.lower()  == 'robbie':
            self.monthly_salary = 2000
            self.bonus_commission = 1500


        elif name.lower()  == 'ariel':
            self.hours_worked = 120
            self.hourly_salary = 30
            self.bonus_commission = 600

    def get_pay(self):
        return self.monthly_salary + self.hours_worked * self.hourly_salary + self.contracts_landed * self.commission_per_contract + self.bonus_commission

    def __str__(self):
         if self.name.lower() == 'billie':
            return f"Billie works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."
         
         elif self.name.lower() == 'charlie':
            return f"Charlie works on a contract of {self.hours_worked} hours at {self.hourly_salary}/hour. Their total pay is {self.get_pay()}."
         
         elif self.name.lower() == 'renee':
            return f"Renee works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."
         
         elif self.name.lower() == 'jan':
            return f"Jan works on a contract of {self.hours_worked} hours at {self.hourly_salary}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."
         
         elif self.name.lower() == 'robbie':
            return f"Robbie works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."
         
         elif self.name.lower() == 'ariel':
            return f"Ariel works on a contract of {self.hours_worked} hours at {self.hourly_salary}/hour and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."
         

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
