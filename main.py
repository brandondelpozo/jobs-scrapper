from knock_db import Knock_Object, Knock_Objects, insert_knock_objects
from logger import logger
from greehouse import Parse_GreenHouse_Company_Job_Data

OBJECT_ID = 'object_1'

# scrapping green house companies data
green_house_companies = ['onescreenaiinc','halodotscience','dandy','mdai','runwayml','spaero']
for company in green_house_companies:
    res_lists = Parse_GreenHouse_Company_Job_Data(company)
    insert_knock_objects(OBJECT_ID,res_lists)
