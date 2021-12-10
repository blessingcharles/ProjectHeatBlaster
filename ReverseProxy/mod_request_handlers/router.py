from flask import Flask , Blueprint ,request , Response
from ReverseProxy.load_balancer.balancer_algo import BalancerAlgo 
from ReverseProxy.mod_roaster.bad_requests import block_badrequests
from ReverseProxy.mod_roaster.bad_useragents import block_baduseragents

from env.http_config import HTTP_CONFIG
from ReverseProxy.mod_request_handlers.controller import *
from env.proxy_config import UPSTREAM_BACKENDSERVERS

request_handlers = Blueprint('request_handlers',__name__,url_prefix="")

#creating an object for load balancing
l_balancer = BalancerAlgo()

#handle all request with different path and seperate handler for each method
@request_handlers.route("/<path:path>" , methods=HTTP_CONFIG["allowed_methods"])
@request_handlers.route("/",methods=HTTP_CONFIG["allowed_methods"])
def request_handler(path : str ="/") -> Response:

    # Trained Ml models to block requests if they are malicious
    if HTTP_CONFIG["block_bad_useragents"] :
        block_baduseragents(request)   # layer1
    
    if HTTP_CONFIG["block_malicious_payloads"] :
        block_badrequests(request)     # layer2


    server_name = l_balancer.balance()
    
    real_url = f"{server_name}{path}"

    # routing to particular http method controller
    if request.method == "GET":
        print(request , "--------------------")
        return get_handler(real_url)

    elif request.method == "POST":

        return post_handler(real_url)

    elif request.method == "PUT":

        return put_handler(real_url)

    elif request.method == "DELETE":

        return delete_handler(real_url)
    
    else : 
        return default_handler(real_url)