from typing import List, Tuple
from requests.api import head
from env.http_config import HTTP_CONFIG

def exclude_headers(response) -> List[Tuple[str,str]]:
    
    headers = [(key,response.headers[key]) for key in response.headers 
                                        if key.lower() not in HTTP_CONFIG["exclude_headers"]]

    return headers