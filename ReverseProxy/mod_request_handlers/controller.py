from flask import  request , Response
import requests

from ReverseProxy.mod_request_handlers.utils import exclude_headers


def get_handler(url : str) -> Response:
    try:
        response = requests.get(url , cookies=request.cookies)
        headers = exclude_headers(response)
        f_response = Response(response.content , response.status_code , headers)
        return f_response
    except Exception as e:
        # current redirected server failed 
        print(e)
        return Response("Internal Server Error" , 500)

def post_handler(url : str) -> Response:

    try:
        response = requests.post(url , json=request.get_json() , cookies=request.cookies)
        headers = exclude_headers(response)

        f_response = Response(response.content , response.status_code , headers)
        return f_response
    except:
        # current redirected server failed 
        return Response("Internal Server Error" , 500)
        
def put_handler(url : str) -> Response:
    try:
        response = requests.put(url , json=request.get_json(),cookies=request.cookies)
        headers = exclude_headers(response)
        f_response = Response(response.content , response.status_code , headers)
        return f_response

    except:
        # current redirected server failed 
        return Response("Internal Server Error" , 500)
       
def delete_handler(url : str) -> Response:

    try:
        response = requests.delete(url , json=request.get_json() , request=request.cookies)
        headers = exclude_headers(response)
        f_response = Response(response.content , response.status_code , headers)
        return f_response
    except:
        return Response("Internal Server Error" , 500)

def default_handler(url : str) -> Response :
    return Response("Method Not Supported" , 400)
