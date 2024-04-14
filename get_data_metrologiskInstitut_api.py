import requests

def getWeatherData(lat=58.02359,lon=7.00446):
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    try:
        data = requests.get(url=url,headers=headers)
        if data.status_code == 200:
            return data.json()
    except:
        print(f"could not get weatherforcast for lat{lat},long{lon}")
    

if __name__ == "__main__":
    import json
    with open("jsonTest.json","w") as f:
        json.dump(getWeatherData(),fp=f)