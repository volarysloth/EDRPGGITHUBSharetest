import requests
from bs4 import BeautifulSoup

def get_job_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def search_jobs(work_title, wage):
    search_url = f"https://www.jobs.cz/prace/?q%5B%5D={work_title}&salary={wage}"
    page_text = get_job_count(search_url)
    index_start = page_text.find("Našli jsme ")
    if index_start != -1:
        index_end = page_text.find(" nabídek", index_start)
        if index_end != -1:
            job_count = int(page_text[index_start+len("Našli jsme "):index_end])
            print(f"Number of job offers found for '{work_title}' with wage at least {wage} CZK:", job_count)
            return

    print(f"Text 'Našli jsme X nabídek' not found for '{work_title}' with wage at least {wage} CZK.")

def main():
    work_title = "Financial%20analyst"  # You can insert your work title here
    wage = 85000  # You can insert your desired wage here
    search_jobs(work_title, wage)

if __name__ == "__main__":
    main()
