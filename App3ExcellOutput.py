import tkinter as tk
from tkinter import messagebox
import requests
import random
import time
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook
import os

def get_job_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def search_jobs():
    min_wage = int(min_wage_entry.get())
    max_wage = int(max_wage_entry.get())
    step = 1000
    frequencies = {}

    for wage in range(min_wage, max_wage + 1, step):
        search_url = f"https://www.jobs.cz/prace/praha/?q%5B%5D=financial%20analyst&salary={wage}&locality%5Bradius%5D=0"
        page_text = get_job_count(search_url)
        index_start = page_text.find("Našli jsme ")
        if index_start != -1:
            index_end = page_text.find(" nabídek", index_start)
            if index_end != -1:
                job_count = int(page_text[index_start+len("Našli jsme "):index_end])
                frequencies[wage] = job_count
                time.sleep(random.uniform(0.5, 2))  # Add random pause to simulate human-like behavior

    # Save data to Excel file
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    save_to_excel(frequencies, desktop)

    result_label.config(text="Frequencies of job offers within the wage range:")
    frequencies_text = ""
    for wage, count in frequencies.items():
        frequencies_text += f"Wage: {wage} CZK - Frequency: {count}\n"
    frequencies_label.config(text=frequencies_text)

def save_to_excel(data, desktop_path):
    wb = Workbook()
    ws = wb.active
    ws.append(["Wage (CZK)", "Frequency"])
    for wage, frequency in data.items():
        ws.append([wage, frequency])
    file_path = os.path.join(desktop_path, "job_search_results.xlsx")
    wb.save(file_path)

def main():
    root = tk.Tk()
    root.title("Job Search")

    tk.Label(root, text="Minimum Wage (CZK):").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="Maximum Wage (CZK):").grid(row=1, column=0, sticky="w")

    global min_wage_entry, max_wage_entry, result_label, frequencies_label

    min_wage_entry = tk.Entry(root)
    max_wage_entry = tk.Entry(root)

    min_wage_entry.grid(row=0, column=1)
    max_wage_entry.grid(row=1, column=1)

    search_button = tk.Button(root, text="Search", command=search_jobs)
    search_button.grid(row=2, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=3, column=0, columnspan=2)

    frequencies_label = tk.Label(root, text="")
    frequencies_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
