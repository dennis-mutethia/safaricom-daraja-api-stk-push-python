import requests, json
from mpesa.credentials import MpesaAccessToken, LipanaMpesaPassword
from config import Config

class Operations:
    
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
        return json.loads(json.dumps(json.loads(response.content))) 
