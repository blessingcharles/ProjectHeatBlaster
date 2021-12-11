from flask import Request
from joblib import load

def block_baduseragents(request : Request):
    file_path = "blasterModels/user_agents_models/knc.joblib"
    model = load(file_path)

    result = model.predict()

