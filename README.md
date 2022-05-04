⚔️ Job details : [here](https://www.upwork.com/jobs/~01be6b8b3fd3f2e740)<br>
⚔️ Fees: **$100**<br>
⚔️ Start time: **4/5/2022 17:30:00**<br>

### 📝 Work:
1. Scrape Job, Location, Remote, Function, Text from following list of websites.
2. List of websites: 
https://jobs.lever.co/Anthropic - Anthropic
https://jobs.lever.co/fiddlerlabs - Fiddler
https://jobs.lever.co/Parafin - Parafin
https://jobs.lever.co/WisprAI - Wispr AI
https://jobs.lever.co/you/ - You.com
https://jobs.lever.co/HedgeLabs	Hedge 

https://boards.greenhouse.io/mdai - MD AI
https://runwayml.com/careers/ - Runway
https://www.x2ai.com/careers - X2AI
https://www.surgehq.ai/about#careers - Surge
https://boards.greenhouse.io/spaero	Spaero Bio

https://zage.notion.site/Careers-Zage-77761fa1c3044edf87a264e965244cdd - Zage : JS Based 
https://www.onescreen.ai/careers - Onescreen : ✅
https://www.halo.science/careers - Halo Science : ✅
https://cresicor.ai/careers - Cresicor : JS based
https://careers.meetdandy.com/#Find%20your%20role - Dandy : JS Based ✅
https://facet.ai/jobs - Facet : JS based: ✅ Doubty 

3. Save the result in Knack DB.


Steps to run:
1. python -m venv .venv
2. . .venv/bin/activate
3. pip install -r requirement.txt


OneScreen:
https://boards.greenhouse.io/embed/job_board?for=onescreenaiinc&b=https%3A%2F%2Fwww.onescreen.ai%2Fcareers = Get Ids and Pass them to below url 👇
https://boards.greenhouse.io/embed/job_app?for=onescreenaiinc&token=4460840004&b=https%3A%2F%2Fwww.onescreen.ai%2Fcareers


Halo Science:
https://boards.greenhouse.io/embed/job_board?for=halodotscience&b=https%3A%2F%2Fwww.halo.science%2Fcareers = Get Ids and Pass them to below URL 👇
https://boards.greenhouse.io/embed/job_app?for=halodotscience&token=4005417005&b=https%3A%2F%2Fwww.halo.science%2Fcareers

Dandy:
https://boards-api.greenhouse.io/v1/boards/dandy/jobs?content=true
Get data from above endpoint 👆


facet.ai:
https://facet.ai/_next/data/pqDWcNvKAiD-Y7OcCIrU0/about.json : using this get the job id : Pass it to below title of job 
https://facet.ai/_next/data/pqDWcNvKAiD-Y7OcCIrU0/jobs/software-engineer-backend.json