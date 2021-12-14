from flask import Request
import pickle , joblib
import os 

def block_baduseragents(request : Request):

    try:
        from ReverseProxy.utils.util import process_ua

        file_path = "/home/th3h04x/Documents/github/ProjectHeatBlast/blasterModels/user_agents_models/svc_cv_pipe.pkl"
        with open(file_path , "rb") as f:
            model = joblib.load(f)
        
        print(f"----------\n{request.headers['User-Agent']}\n")
        result = model.predict([request.headers["User-Agent"]])
        print(result)
        return result[0]

    except Exception as e:
        print(e)
        return 0