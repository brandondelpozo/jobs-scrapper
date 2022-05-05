# https://boards-api.greenhouse.io/v1/boards/dandy/jobs?content=true
import requests
import html
from logger import logger
from knock_db import Knock_Object, Knock_Objects


def Parse_GreenHouse_Company_Job_Data(company_id: str, company_name: str) -> Knock_Objects:
    url = f'https://boards-api.greenhouse.io/v1/boards/{company_id}/jobs?content=true'
    resp = requests.get(url)
    if resp.status_code == 200:
        obj = resp.json()
        knock_lst = Knock_Objects()

        assert 'jobs' in obj, 'Jobs array not exists in object'
        i = 1
        for job in obj['jobs']:
            logger.debug(f'{company_id} company {i} job is: {job}')
            i += 1

            location = job['location']['name']
            remote = "No"
            if 'remote' in location.lower():
                remote = "Yes"
            name = job['title']
            description = html.unescape(job['content'])
            text = ""  # aka function
            if len(job['departments']) > 0:
                for dep in job['departments']:
                    text += dep['name']

            knock_obj = Knock_Object(
                company_name, name, remote, location, description, text)
            knock_lst.push(knock_obj)
        return knock_lst
    else:
        logger.error(
            f'error in scraping {company_id} data, error is: {resp.text}')
        raise f'failed to scrape {company_id}, status code: {resp.status_code}'
