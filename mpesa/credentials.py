import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64
from mpesa.config import Config

class MpesaAccessToken:
    r = requests.get(Config.cred_api_url, auth=HTTPBasicAuth(Config.consumer_key, Config.consumer_secret))
    print(str(r))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')    
    OffSetValue = '0'
        
    data_to_encode = Config.business_short_code + Config.passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')