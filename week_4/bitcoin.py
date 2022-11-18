import json
import sys
from urllib.request import urlopen

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    if len(sys.argv) == 2:
        res = urlopen(url)
        data = json.load(res)
        data["bpi"]["USD"]["rate_float"]
        rate = float(data["bpi"]["USD"]["rate_float"]) * float(sys.argv[1])
        print(f"${rate}")
    else:
        raise ValueError
except:
    pass
