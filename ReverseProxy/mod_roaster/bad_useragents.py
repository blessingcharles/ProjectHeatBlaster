from flask import Request
import pickle , joblib
import os

from env.ml_config import UA_FILE_PATH, UA_ML_MODELS
from env.proxy_config import ROASTING_ML_MODELS 
from ReverseProxy.utils.util import process_ua 

file_path = UA_FILE_PATH + "/" + UA_ML_MODELS[ROASTING_ML_MODELS["user-agents"]]

with open(file_path , "rb") as f:
    model = joblib.load(f)

def block_baduseragents(request : Request):
    
    try:
        
        print(f"----------\n{request.headers['User-Agent']}\n")
        result = model.predict([request.headers["User-Agent"]])
        print(result)
        
        return result[0]

    except Exception as e:
        print(e)
        return 0