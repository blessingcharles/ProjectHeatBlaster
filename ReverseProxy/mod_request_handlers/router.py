from flask import Flask , Blueprint, json , request , Response
import requests
from ReverseProxy.mod_roaster.bad_useragents import block_baduseragents

from env.http_config import HTTP_CONFIG
from ReverseProxy.mod_request_handlers.controller import *

request_handlers = Blueprint('request_handlers',__name__,url_prefix="")

server_name = "http://localhost:5000"

#handle all request with different path and seperate handler for each method
@request_handlers.route("/<path:path>" , methods=HTTP_CONFIG["allowed_methods"])
@request_handlers.route("/",methods=HTTP_CONFIG["allowed_methods"])
def request_handler(path : str ="/") -> Response:

    if HTTP_CONFIG["block_bad_useragents"] :
        block_baduseragents("dummy")
    

    real_url = f"{server_name}/{path}"
    # routing to particular http method controller
    if request.method == "GET":
        
        return get_handler(real_url)

    elif request.method == "POST":

        return post_handler(real_url)

    elif request.method == "PUT":

        return put_handler(real_url)

    elif request.method == "DELETE":

        return delete_handler(real_url)
    
    else : 
        return default_handler(real_url)