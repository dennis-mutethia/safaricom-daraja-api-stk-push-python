import requests, json
from mpesa.credentials import MpesaAccessToken, LipanaMpesaPassword
from config import Config

class Operations:
    def __init__(self):
        access_token = MpesaAccessToken.validated_mpesa_access_token
        self.headers = {"Authorization": f"Bearer {access_token}"}
    
    def lipa_na_mpesa_online(self, phone, amount):        
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

        response = requests.post(Config.lnm_api_url, json=request, headers=self.headers)
        #result = json.loads(json.dumps(json.loads(response)))
        return json.loads(json.dumps(json.loads(response.content))) 

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

        response = requests.post(Config.lnm_api_url, json=request, headers=self.headers)
        #result = json.loads(json.dumps(json.loads(response)))
        return json.loads(json.dumps(json.loads(response.content))) 

        '''
        {    
   "Initiator":"API_Usename",
   "SecurityCredential":"FKXl/KPzT8hFOnozI+unz7mXDgTRbrlrZ+C1Vblxpbz7jliLAFa0E/…../uO4gzUkABQuCxAeq+0Hd0A==",
   "Command ID": "BusinessBuyGoods",
   "SenderIdentifierType": "4",
   "RecieverIdentifierType":"4",
   "Amount":"239",
   "PartyA":"123456",
   "PartyB":"000000",
   "AccountReference":"353353",
   "Requester":"254700000000",
   "Remarks":"OK",
   "QueueTimeOutURL":"https://mydomain.com/b2b/businessbuygoods/queue/",
   "ResultURL":"https://mydomain.com/b2b/businessbuygoods/result/",
}
        '''