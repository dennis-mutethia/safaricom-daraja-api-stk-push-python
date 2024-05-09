import sys, random, csv, concurrent.futures
from mpesa.operations import Operations

class App:  
    def __init__(self):        
        self.max_numbers = 10000
        self.amount = 99
        self.phone_numbers_csv = 'phone_numbers.csv'
        self.existing_numbers = []
        self.operations = Operations()
    
    def read_existing_numbers(self):
        existing_numbers = []
        try:
            with open(self.phone_numbers_csv, mode='r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    phone = (row['phone'])
                    existing_numbers.append(phone)
                    
        except Exception as e:
            print(f"An error occurred in reading existing numbers: {e}")

        return existing_numbers
    
    def append_to_csv(self, phone, response):
        try:
            with open(self.phone_numbers_csv, mode='a', newline='') as csv_file:
                fieldnames = ['phone', 'response']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                # Check if the file is empty, if so write the header
                if csv_file.tell() == 0:
                    writer.writeheader()

                writer.writerow({
                    'phone': phone,
                    'response': response
                })

        except Exception as e:
            print(f"An error occurred in append_to_csv: {e}")

    def generate_numbers(self, max_numbers):
        numbers = []
        for j in range(max_numbers):
            prefix = 25470 + random.randint(0, 2)
            suffix = str(random.randint(0, 9999999)).zfill(7)
            numbers.append(int(str(prefix) + suffix))
        return numbers

    def send_stk_push(self, phone, amount):
        existing_numbers = self.read_existing_numbers()
        if phone not in existing_numbers:
            response = self.operations.lipa_na_mpesa_online(phone, amount)            
            response_description = response["ResponseDescription"]
            if 'Success.' not in response_description:
                raise SystemExit
            
            status = 'STK sent'
            self.append_to_csv(phone, status)           
            print(f"{phone} - {status}")
    
    def __call__(self):
        generated_numbers = self.generate_numbers(self.max_numbers)
        distinct_numbers = list(set(generated_numbers))
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = [executor.submit(self.send_stk_push, phone, self.amount) for phone in distinct_numbers]

            # Wait for all threads to complete
            concurrent.futures.wait(threads) 

App()()