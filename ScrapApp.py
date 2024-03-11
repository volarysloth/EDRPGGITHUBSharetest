import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def get_job_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def search_jobs():
    work_title = work_title_entry.get().replace(" ", "%20")
    wage = wage_entry.get()
    city = city_entry.get().lower()
    search_url = f"https://www.jobs.cz/prace/{city}/?q%5B%5D={work_title}&salary={wage}&locality%5Bradius%5D=0"
    page_text = get_job_count(search_url)
    index_start = page_text.find("Našli jsme ")
    if index_start != -1:
        index_end = page_text.find(" nabídek", index_start)
        if index_end != -1:
            job_count = int(page_text[index_start+len("Našli jsme "):index_end])
            result_label.config(text=f"Number of job offers found: {job_count}")
            return

    result_label.config(text="No job offers found or unable to retrieve job count.")

def main():
    root = tk.Tk()
    root.title("Job Search")

    tk.Label(root, text="Work Title:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="Wage (CZK):").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="City:").grid(row=2, column=0, sticky="w")

    global work_title_entry, wage_entry, city_entry, result_label

    work_title_entry = tk.Entry(root)
    wage_entry = tk.Entry(root)
    city_entry = tk.Entry(root)

    work_title_entry.grid(row=0, column=1)
    wage_entry.grid(row=1, column=1)
    city_entry.grid(row=2, column=1)

    search_button = tk.Button(root, text="Search", command=search_jobs)
    search_button.grid(row=3, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
