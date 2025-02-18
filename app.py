
from mpesa.operations import Operations

class App:
    def __init__(self):        
        self.operations = Operations()
        
    def send_stk_push(self, phone, amount):
        response = self.operations.lipa_na_mpesa_online(phone, amount)
        if 'ResponseDescription' in response:
            response_description = response['ResponseDescription']
            print(response_description)
        elif 'errorMessage' in response:
            errorMessage = response['errorMessage']
            print(errorMessage)

    def __call__(self):
        phone = '254723111920'
        amount = 10

        self.send_stk_push(phone, amount)

if __name__ == '__main__':
    App()()