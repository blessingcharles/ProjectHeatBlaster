#config file for request and response handlers

LOAD_BALANCE_ALGO = {
    "ROUND_ROBIN" : "round_robin",
}

HTTP_CONFIG = {
    "allowed_methods":["GET","POST","PUT","DELETE"],
    "exclude_headers" : ["content-encoding", "content-length", "transfer-encoding", "connection"],
    "block_bad_useragents":True,
    "block_malicious_payloads":True,
    "load_balance_algo":LOAD_BALANCE_ALGO["ROUND_ROBIN"]
    
}