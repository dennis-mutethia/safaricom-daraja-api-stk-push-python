import base64, json, requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

from mpesa.config import Config

class Credentials:
    def __init__(self):
        pass
    
    def get_access_token(self):
        try:
            r = requests.get(Config.cred_api_url, auth=HTTPBasicAuth(Config.consumer_key, Config.consumer_secret))
            mpesa_access_token = json.loads(r.text)
            return mpesa_access_token['access_token']
        except Exception as e:
            print(e)
            return None
    
    def get_password(self):
        lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
        try:                 
            data_to_encode = Config.business_short_code + Config.passkey + lipa_time
            online_password = base64.b64encode(data_to_encode.encode())
            decode_password = online_password.decode('utf-8')
            
            return lipa_time, decode_password
        except Exception as e:
            print(e)
            return lipa_time, None
        