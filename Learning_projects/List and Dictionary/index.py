travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(new_country, new_visits, new_cities):
    new_travel = {}
    new_travel["country"] = new_country,
    new_travel["visits"] = new_visits,
    new_travel['cities'] = new_cities
    travel_log.append(new_travel)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)