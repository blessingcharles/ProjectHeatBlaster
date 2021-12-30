from flask import Request
import pickle , joblib
import os


from env.ml_config import PAYLOADS_FILE_PATH , PAYLOADS_ML_MODEL
from env.proxy_config import ROASTING_ML_MODELS 

from ReverseProxy.utils.util import process_ua 
from heatblaster.utils import extract_feature

file_path1 = PAYLOADS_FILE_PATH + "/" + PAYLOADS_ML_MODEL[ROASTING_ML_MODELS["payloads"]]
file_path2 = PAYLOADS_FILE_PATH + "/" + "rf_feature_model.pkl"

with open(file_path1 , "rb") as f:
    model = joblib.load(f)

with open(file_path2 , "rb") as f:
    custom_feature_model = joblib.load(f)


def block_badrequests(request : Request):
    
    try:
        """
            generate a string by combinig the query payloads given by the user
        """

        args_str = ""
        if request.method == "GET":
            for _ , v  in request.args.items():
                args_str += v + " "

        else:
            for _ , v in request.json.items():
                args_str += v + " "

        if not args_str:
            return 0

        print("[+]----------------------------" , args_str)

        d = extract_feature(args_str)
        result = [0]

        print(d.values)
        result = custom_feature_model.predict(d.drop(["payloads"],axis=1).values)

        print("[+]payload is malicious : " , result)
        return result[0]

    except Exception as e:
        print(e)
        return 0