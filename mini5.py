
from bs4 import BeautifulSoup
import requests
job_count = 0
first_url = ("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35")
base_url = ("https://www.timesjobs.com/candidate/job-search.html"
            "?from=submit&luceneResultSize=25&postWeek=60&searchType=Home_Search"
            "&cboPresFuncArea=35&pDate=Y")
days = input("Enter for how recent you are looking for jobs Posted: ")
no_skills = input("Enter skills you don't want to see jobs for: ")
list_no_skills = no_skills.split(",")
req_exp = input("Enter the number of experience you have (like 1 - 3 or 3 - 4): ")
list_req_exp = req_exp.split("-")
min_exp = list_req_exp[0]
pages = int(input("Enter the number of pages you want to scroll through: "))
for page in range (1, pages+1):
    if page == 1:
        url = first_url
    else:
        url = f"{base_url}&sequence={page}&startPage={page - 1}"

    html_requests = requests.get(url).text
    soup  = BeautifulSoup(html_requests, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    print("")
    print(f"Scraping jobs from Page no. {page}")
    print("")
    for job in jobs:
        posted = job.find("span", class_="sim-posted").span.text
        experience = job.find("i", class_="srp-icons experience").parent.text.strip()
        list_experience = experience.split("-")
        min_experience = list_experience[0]

        if days in posted:
            skills = job.find("div", class_ = "more-skills-sections").text.strip().replace(" ","_").split()
#skills = [skill for skill in skills if skill != "___"]

            a = len(skills)
            i = 0
            while i < a:
                if skills[i] == "___":
                    skills.remove("___")
                    a -= 1     # update length after removal
                else:
                    i += 1
            skills = ", ".join(skills)
            skills_list = skills.split(",")
            more_info = job.header.h2.a["href"]
            company = job.find("h3", class_= "joblist-comp-name").text.strip()
            if not any(skill.strip().lower() in [s.strip().lower() for s in skills_list]
                    for skill in list_no_skills) and min_exp>= min_experience:
                with open(f"Posts/{job_count}.txt","w") as f:
                    f.write(f"Company name: {company}\nRequired Skills: {skills}\nPosted: {posted}\nFor more info: {more_info} \nExperience required: {experience}")
                    f.write("")
                    print(f"File Saved: {job_count}.txt open this file to see the listing")
                    print(f"Company name: {company}\nRequired Skills: {skills}\nPosted: {posted}\nFor more info: {more_info} \nExperience required: {experience}")
                    job_count += 1
