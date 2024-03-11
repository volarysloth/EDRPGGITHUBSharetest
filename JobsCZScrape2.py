import requests
from bs4 import BeautifulSoup

def get_job_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def search_jobs(work_title, wage, city):
    search_url = f"https://www.jobs.cz/prace/{city}/?q%5B%5D={work_title}&salary={wage}&locality%5Bradius%5D=0"
    page_text = get_job_count(search_url)
    index_start = page_text.find("Našli jsme ")
    if index_start != -1:
        index_end = page_text.find(" nabídek", index_start)
        if index_end != -1:
            job_count = int(page_text[index_start+len("Našli jsme "):index_end])
            print(f"Number of job offers found for '{work_title}' in {city} with wage at least {wage} CZK:", job_count)
            return

    print(f"Text 'Našli jsme X nabídek' not found for '{work_title}' in {city} with wage at least {wage} CZK.")

def main():
    work_title = "financial%20controller"  # You can insert your work title here
    wage = 150000  # You can insert your desired wage here
    city = "praha"  # You can insert your desired city here
    search_jobs(work_title, wage, city)

if __name__ == "__main__":
    main()
