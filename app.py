import random
from mpesa.operations import Operations

class App:
    def generate_numbers(self):
        numbers = []
        for j in range(10000):
            prefix = 25470 + random.randint(0, 2)
            suffix = str(random.randint(0, 9999999)).zfill(7)
            numbers.append(int(str(prefix) + suffix))
        return numbers

    def __call__(self):
        generated_numbers = self.generate_numbers() #Generate the first numbers
        for phone in generated_numbers:
            amount = 100
            reponse = Operations.lipa_na_mpesa_online(phone, amount)
            print(f"{phone} - {reponse}")

App()()