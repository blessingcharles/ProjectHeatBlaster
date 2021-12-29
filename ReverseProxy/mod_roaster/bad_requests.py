from flask import Request
import pickle , joblib
import os


from env.ml_config import PAYLOADS_FILE_PATH , PAYLOADS_ML_MODEL
from env.proxy_config import ROASTING_ML_MODELS 


def block_badrequests(request : Request):
    print("[+]----------------------------" , request.args)
    

    try:
        from ReverseProxy.utils.util import process_ua 

        file_path = PAYLOADS_FILE_PATH + "/" + PAYLOADS_ML_MODEL[ROASTING_ML_MODELS["payloads"]]

        with open(file_path , "rb") as f:
            model = joblib.load(f)
        
        result = model.predict([request.headers["User-Agent"]])
  
        print("[+]----------------------------" , request.args)

        return result[0]

    except Exception as e:
        print(e)
        return 0

