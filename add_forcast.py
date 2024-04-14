from db_class import Forcast, Create_tab
from db_session import Session
from get_data_metrologiskInstitut_api import getWeatherData

session = Session()
Create_tab()

def add_forcast(name="Korshamn",lat=58.0236,lon=7.0045):
    data = getWeatherData(lat=lat,lon=lon)
    forcast_add = []
    if data:
        forcast = data["properties"]["timeseries"][0]
        
        weather = forcast["data"]["next_6_hours"]["summary"]["symbol_code"]
        precipitation = forcast["data"]["next_6_hours"]["details"]["precipitation_amount"]
        air_temperature = forcast["data"]["instant"]["details"]["air_temperature"]
        wind_from_direction = forcast["data"]["instant"]["details"]["wind_from_direction"]
        wind_speed = forcast["data"]["instant"]["details"]["wind_speed"]

        forcast_add.append(Forcast(
            name=name
            ,lat=lat
            ,long=lon
            ,weather=weather
            ,precipitation=precipitation
            ,air_temperature = air_temperature
            ,wind_from_direction=wind_from_direction
            ,wind_speed=wind_speed))
        session.add_all(forcast_add)
        session.commit()

if __name__ == "__main__":
    add_forcast(name="Korshamn",lat=58.0236,lon=7.0045)
    add_forcast(name="Lier",lat=59.75676,lon=10.29210)