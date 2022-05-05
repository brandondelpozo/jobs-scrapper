import requests
import json
from logger import logger
from config import DEBUG, COMPANY_MAPPINGS, OBJECT_ID,APPLICATION_ID,API_KEY


class Knock_Object:
    def __init__(self, company, jobName, isRemote, location, description, text):
        self.company = company
        self.JobName = jobName
        self.IsRemote = isRemote
        self.Location = location
        self.Description = description
        self.Text = text


class Knock_Objects:
    list = []

    def __init__(self):
        return

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.list):
            ele = self.list[self.i]
            self.i += 1
            return ele
        else:
            raise StopIteration

    def push(self, obj: Knock_Object):
        self.list.append(obj)


def insert_knock_objects(objs: Knock_Objects):
    for obj in objs:
        insert_knock_object(obj)


def insert_knock_object(obj):
    dict = {
        "field_7" if DEBUG else "field_164": obj.JobName,
        "field_14" if DEBUG else "field_165": [f'{COMPANY_MAPPINGS[obj.company]}'],
        "field_9" if DEBUG else "field_166": obj.Location,
        "field_10" if DEBUG else "field_167": obj.Description,
        "field_11" if DEBUG else "field_168": obj.IsRemote,
        "field_12" if DEBUG else "field_169": obj.Text,
    }

    # code for testing please delete
    logger.info(
        f'Company: {obj.company} | Name: {obj.JobName}  |  IsRemote: {obj.IsRemote} |  Location: {obj.Location} | Function: {obj.Text} |  Description {obj.Description[0:50]}')
    # insert(OBJECT_ID, dict)


def insert(object_id: str, data: dict) -> bool:

    url = f"https://api.knack.com/v1/objects/{object_id}/records"

    payload = json.dumps(data)
    headers = {
        'X-Knack-REST-API-Key': API_KEY,
        'X-Knack-Application-Id': APPLICATION_ID,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        logger.debug(f'inserted {data} success...')
        return True
    else:
        logger.error(
            f'error in inserting {payload[0:35]} to database  | error: {response.text}')
        return False
