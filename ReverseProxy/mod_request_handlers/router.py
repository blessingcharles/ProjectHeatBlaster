from logging import critical
import logging
from flask import Flask , Blueprint ,request , Response
from ReverseProxy.load_balancer.balancer_algo import BalancerAlgo 
from ReverseProxy.mod_roaster.bad_requests import block_badrequests
from ReverseProxy.mod_roaster.bad_useragents import block_baduseragents
from ReverseProxy.utils import logcritical, loginfo

from env.http_config import HTTP_CONFIG
from ReverseProxy.mod_request_handlers.controller import *
from env.proxy_config import UPSTREAM_BACKENDSERVERS
from ReverseProxy.utils import critical_logger

request_handlers = Blueprint('request_handlers',__name__,url_prefix="")

#creating an object for load balancing
l_balancer = BalancerAlgo()

#handle all request with different path and seperate handler for each method
@request_handlers.route("/<path:path>" , methods=HTTP_CONFIG["allowed_methods"])
@request_handlers.route("/",methods=HTTP_CONFIG["allowed_methods"])
def request_handler(path : str ="") -> Response:

    server_name = l_balancer.balance()
    real_url = f"{server_name}/{path}"

    # Trained Ml models to block requests if they are malicious
    if HTTP_CONFIG["block_bad_useragents"] :
        is_bad_ua = block_baduseragents(request)   # layer1

        if is_bad_ua:
            # logcritical(f"\nLayer1 Blast |URL : {real_url} |  |METHOD : {request.method} |Ip : {request.remote_addr}")
            critical_logger.logger.log(logging.CRITICAL ,"\nLayer1 Blast |URL : {real_url} |  |METHOD : {request.method} |Ip : {request.remote_addr}" )
            
            return Response("Request Blocked",403)
    
    if HTTP_CONFIG["block_malicious_payloads"] :
        is_malicious_req = block_badrequests(request)     # layer2

        if is_malicious_req:
            logcritical(f"\nLayer2 Blast |URL : {real_url} |  |METHOD : {request.method} |Ip : {request.remote_addr} ")
            return Response("Request Blocked",403)


    
    loginfo(f"\nURL : {real_url} |  |METHOD : {request.method} |Ip : {request.remote_addr}")

    print(f"[+]Requesting : {real_url}")
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