from knock_db import insert_knock_object
from logger import logger
from greehouse import Parse_GreenHouse_Company_Job_Data
from concurrent.futures import ThreadPoolExecutor


# scrapping green house companies data
green_house_companies = [
    {"id": 'onescreenaiinc', "name": "Onescreen"},
    {"id": 'halodotscience', "name": "Onescreen"},
    {"id": 'dandy', "name": "Onescreen"},
    {"id": 'mdai', "name": "Onescreen"},
    {"id": 'runwayml', "name": "Onescreen"},
    {"id": 'spaero', "name": "Onescreen"}
]
for company in green_house_companies:
    res_lists = Parse_GreenHouse_Company_Job_Data(
        company['id'], company['name'])

    with ThreadPoolExecutor(3) as exe:
        exe.map(insert_knock_object, res_lists)
