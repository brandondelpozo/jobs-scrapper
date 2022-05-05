from knock_db import insert_knock_object
from lever import Parse_Lever_Companies_Jobs_Data
from logger import logger
from greehouse import Parse_GreenHouse_Company_Job_Data
from concurrent.futures import ThreadPoolExecutor
import getopt
import sys


argument_list = sys.argv[1:]
options = "s:"
long_options = ["Scrap"]

try:
    args, val = getopt.getopt(argument_list, options, long_options)
    if len(args) == 0:
        print("Please provide -s or --Scrap process to scrap")

    for cArg, cVal in args:
        if cArg in ("-s", "--Scrap"):
            print(f'value to scrap is {cVal}')
        else:
            print('Please provide -s or --Scrap process to scrap')
except:
    print(sys.exc_info()[0])


def scrap_green_house_companies():
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


def scrap_lever_companies():
    lever_companies = [
        {"id": 'Anthropic', "name": "Anthropic"},
        {"id": 'fiddlerlabs', "name": "Fiddler"},
        # {"id": 'Parafin', "name": "Parafin"},
        # {"id": 'WisprAI', "name": "Wispr AI"},
        # {"id": 'you', "name": "You.com"},
        # {"id": 'HedgeLabs', "name": "Hedge"}
    ]

    lever_results = []
    with ThreadPoolExecutor() as exe:
        lever_results = exe.map(
            Parse_Lever_Companies_Jobs_Data, lever_companies)

    with ThreadPoolExecutor(3) as exe:
        for r in lever_results:
            exe.map(insert_knock_object, r)
