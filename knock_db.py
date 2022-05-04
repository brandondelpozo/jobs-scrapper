import requests
import os
import json
from logger import logger


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


def insert_knock_objects(object_id: str, objs: Knock_Objects):
    for obj in objs:
        dict = {
            "field_1": obj.JobName,
            "field_2": obj.IsRemote,
            "field_3": obj.Location,
            "field_4": obj.Description,
            "field_5": obj.Text,
        }
        # code for testing please delete
        logger.info(
            f'Company: {obj.company} | Name: {obj.JobName} |  IsRemote: {obj.IsRemote} |  Location: {obj.Location} |  Description {obj.Description[0:50]}')
        # insert(object_id, dict)


def insert(object_id: str, data: dict) -> bool:

    url = f"https://api.knack.com/v1/objects/{object_id}/records"

    payload = json.dumps(data)
    headers = {
        'X-Knack-REST-API-Key': os.getenv('API_KEY'),
        'X-Knack-Application-Id': os.getenv('APPLICATION_ID'),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        logger.debug(f'inserted {data} success...')
        return True
    else:
        logger.error(
            f'error in inserting {data} to database  | error: {response.text}')
        return False
