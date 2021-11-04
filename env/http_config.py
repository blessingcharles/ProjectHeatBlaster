#config file for request and response handlers

HTTP_CONFIG = {
    "allowed_methods":["GET","POST","PUT","DELETE"],
    "exclude_headers" : ["content-encoding", "content-length", "transfer-encoding", "connection"],
    "block_bad_useragents":True,
    "load_balance_algo":"round_robin"
}