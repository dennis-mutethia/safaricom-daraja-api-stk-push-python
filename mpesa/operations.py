import json, requests

from mpesa.config import Config
from mpesa.credentials import Credentials

class Operations:
    def __init__(self):
        self.credentials = Credentials()
        self.headers = {"Authorization": f"Bearer {self.credentials.get_access_token}"}
    
    def lipa_na_mpesa_online(self, phone, amount):   
        transaction_type = "CustomerBuyGoodsOnline"
        lipa_time, password = self.credentials.get_password() 
        request = {
            "BusinessShortCode": Config.business_short_code,
            "Password": password,
            "Timestamp": lipa_time,
            "TransactionType": transaction_type,
            "Amount": amount,
            "PartyA": phone,
            "PartyB": Config.business_till,
            "PhoneNumber": phone,
            "CallBackURL": Config.call_back_url,
            "AccountReference": "BetKing",
            "TransactionDesc": "Payment of Football Betting Tips"
        }

        try:
            response = requests.post(Config.lnm_api_url, json=request, headers=self.headers)
            result =  json.loads(json.dumps(json.loads(response.content))) 
            return result
        except Exception as e:
            print(e)
            raise e