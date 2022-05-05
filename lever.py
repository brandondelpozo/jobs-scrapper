import requests
import html2text
from bs4 import BeautifulSoup
from knock_db import Knock_Objects, Knock_Object
from concurrent.futures import ThreadPoolExecutor, as_completed


def Parse_Lever_Companies_Jobs_Data(company):
    res_lists = Parse_Lever_Company_Jobs_Data(
        company['id'], company['name'])
    return res_lists


def Parse_Lever_Company_Jobs_Data(company_id: str, company_name: str) -> Knock_Objects:

    k_objects = Knock_Objects()
    url = f'https://jobs.lever.co/{company_id}'
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    groups = soup.select(".postings-group")
    for group in groups:
        category_selector = group.select_one(".posting-category-title")
        category = category_selector.text

        postings_selector = group.select(".posting")

        futures = []
        for posting in postings_selector:

            link = posting.a['href']

            with ThreadPoolExecutor() as exe:
                futures.append(exe.submit(Parse_Lever_Company_Job_Data, link))

        for future in as_completed(futures):
            k_object = future.result()
            k_object.company = company_name
            k_object.Text = category
            k_objects.push(k_object)

    return k_objects


def Parse_Lever_Company_Job_Data(url: str) -> Knock_Object:
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    headline_selector = soup.select_one(".posting-headline")
    job_title = headline_selector.h2.text

    location = headline_selector.select_one('.sort-by-time').text.rstrip('/')

    remote = "No"
    if 'remote' in location.lower():
        remote = "Yes"

    jd_selector = soup.select(".content-wrapper .content .section-wrapper")[-1]
    jd_selector_eles = jd_selector.select('.section')
    jd_selector_eles.pop()

    jd = ""
    for jd_s in jd_selector_eles:
        jd += html2text.html2text(jd_s.prettify())

    knock_obj = Knock_Object(
        "", job_title, remote, location, jd, "")
    return knock_obj
