from env.http_config import HTTP_CONFIG, LOAD_BALANCE_ALGO
from env.proxy_config import UPSTREAM_BACKENDSERVERS


class BalancerAlgo:
    
    def __init__(self , algo_name : str = HTTP_CONFIG["load_balance_algo"]) -> None:
        
        self.algo_name = algo_name
        self.server_instance_count = len(UPSTREAM_BACKENDSERVERS)
        self.current_instance = 0


    def balance(self) -> str:
        
        if self.algo_name == LOAD_BALANCE_ALGO["ROUND_ROBIN"]:
            return self.round_robin()
        
        return UPSTREAM_BACKENDSERVERS[0]

    def round_robin(self) -> str:
        
        ip = UPSTREAM_BACKENDSERVERS[ (self.current_instance%self.server_instance_count) ]
        self.current_instance += 1
        return ip
