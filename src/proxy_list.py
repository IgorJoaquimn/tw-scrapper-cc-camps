import requests
import random

def get_random_proxy() -> str:
    proxy_http  = requests.get("https://sslproxies.org/").text
    proxy_list  = proxy_http.split("\n")[13:113]
    rng_proxy   = random.choice(proxy_list)
    http_server = f"http://{rng_proxy}"
    return http_server

print(get_random_proxy())
