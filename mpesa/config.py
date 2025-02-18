import os
from dotenv import load_dotenv

load_dotenv()  
        
class Config:
    business_short_code = os.getenv("BUSINESS_SHORTCODE")
    business_till = os.getenv("BUSINESS_TILL")
    passkey = os.getenv("PASSKEY")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    call_back_url = os.getenv("CALLBACK_URL")
    cred_api_url = os.getenv("CREDENTIAL_API_URL")
    lnm_api_url = os.getenv("LNM_API_URL")

