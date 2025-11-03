# Job-Scrapper-using-requests-and-beautifulsoup4
This is a Python-based job scraping tool that extracts job listings from TimesJobs using the Requests library and BeautifulSoup for HTML parsing. The script allows users to customize the search by specifying:   How recent the job posts should be,  Skills they want to exclude,  Their experience range,  Number of pages to scrape

🕵️ Job Scraper – TimesJobs

This is a Python web scraping project that extracts the newest job listings from TimesJobs.com based on filters like:

✅ Skills you want to avoid
✅ Recent posting days (e.g. “1 Day Ago”)
✅ Experience filter
✅ Number of pages to crawl
✅ Automatically saves listings into text files

🚀 Features
Feature	Description
Page Scrolling	User enters how many pages to scrape
Skill Filtering	Remove jobs containing unwanted skills
Experience Filter	Compare your experience with job requirement
Local Output	Each job saved as a separate .txt file
Clean & ETSY UI	Well formatted output in console
🧰 Requirements

Install dependencies:

pip install -r requirements.txt

▶️ Run the Script
python scraper.py


Then enter the requested information:

Enter for how recent you are looking for jobs Posted: 1
Enter skills you don't want to see jobs for: python,frontend
Enter the number of experience you have (like 1 - 3 or 3 - 4): 1 - 3
Enter the number of pages you want to scroll through: 3

📂 Output Example

Files will be auto-generated inside the Posts folder:

Posts/
│ 0.txt
│ 1.txt
│ 2.txt
...

⚠️ Important Note

This script saves scraped data into a folder named Posts.
Before running the script, please ensure that this directory exists in the same location as the Python file.

If the folder is missing, you will encounter the following error:

FileNotFoundError: [Errno 2] No such file or directory: 'Posts/1.txt'


You can manually create the Posts folder or uncomment the directory creation code provided in the script.

Each file includes:

Company Name: XYZ Corp
Required Skills: Django, APIs, SQL
Experience Required: 1-3 Years
Posted: Today
More Info: https://...

⚠️ Legal Note

This is for educational purposes only.
Respect website terms of service and avoid excessive requests.

🙌 Credits & Acknowledgment

This project was developed with guidance and reference from FreeCodeCamp.org’s Python Web Scraping Tutorial on YouTube:
https://www.youtube.com/watch?v=XVv6mJpFOb0

All credit for the learning foundation goes to the creator of that tutorial.
