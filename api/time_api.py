#pip install requests
import requests
from datetime import datetime

def obtener_fecha_api():
    url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Santiago"
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        return data["date"]   # yyyy-mm-dd
    else:
        return None

def obtener_fecha_actual():
    return datetime.now().strftime("%Y-%m-%d")
"""this piece of shit it is freaking bullshit it gives me a literaly joker ass state of emocion bc it is absolutly trash lptm
"""