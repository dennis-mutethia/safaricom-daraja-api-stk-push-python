import requests
import random, json
from credentials import MpesaAccessToken, LipanaMpesaPassword
from config import Config

def lipa_na_mpesa_online(phone, amount):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    headers = {"Authorization": f"Bearer {access_token}"}
    request = {
        "BusinessShortCode": Config.business_short_code,
        "Password": LipanaMpesaPassword.decode_password,
        "Timestamp": LipanaMpesaPassword.lipa_time,
        "TransactionType": "CustomerBuyGoodsOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": Config.business_till,
        "PhoneNumber": phone,
        "CallBackURL": Config.call_back_url,
        "AccountReference": "BetKing",
        "TransactionDesc": "Payment of Football Betting Tips"
    }

    response = requests.post(Config.lnm_api_url, json=request, headers=headers)
    #result = json.loads(json.dumps(json.loads(response)))
    print(response)

def generate_numbers():
    numbers = []
    for j in range(1000):
        prefix = 25470 + random.randint(0, 2)
        suffix = str(random.randint(0, 9999999)).zfill(7)
        numbers.append(int(str(prefix) + suffix))
    return numbers

generated_numbers = generate_numbers() #Generate the first numbers
for phone in generated_numbers:
    print(phone)
    amount = 100
    lipa_na_mpesa_online(phone, amount)
