from flask import Request

def block_badrequests(request : Request):
    print("[+]----------------------------" , request.args)
    pass