from flask import Request
import pickle , joblib
import os
from ReverseProxy.utils import logerror

from env.ml_config import PAYLOADS_FILE_PATH , PAYLOADS_ML_MODEL
from env.proxy_config import ROASTING_ML_MODELS 

from ReverseProxy.utils.util import process_ua 
from heatblaster.utils import extract_feature

file_path = PAYLOADS_FILE_PATH + "/" + PAYLOADS_ML_MODEL[ROASTING_ML_MODELS["payloads"]]

with open(file_path , "rb") as f:
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
            if request.headers["Content-Type"].lower() == "application/json": 
                for _ , v in request.json.items():
                    args_str += v + " "

            elif request.headers["Content-Type"].lower() == "multipart/form-data" or request.headers["Content-Type"].lower() == "application/x-www-form-urlencoded": 
                for _ , v in request.form.items():
                    args_str += v + " "
            else:
                for _ , v  in request.args.items():
                    args_str += v + " "

        if not args_str:
            return 0

        d = extract_feature(args_str)
        result = custom_feature_model.predict(d.drop(["payloads"],axis=1).values)

        return result[0]

    except Exception as e:
        logerror(e)
        print(e)
        return 0