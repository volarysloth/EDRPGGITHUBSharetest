import tkinter as tk
import requests
import random
import time
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook
import os
import matplotlib.pyplot as plt

def get_job_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def search_jobs():
    position = position_entry.get()
    city = city_entry.get().lower()
    min_wage = int(min_wage_entry.get())
    max_wage = int(max_wage_entry.get())
    step = int(step_entry.get())
    frequencies = {}
    positions = {}

    for wage in range(min_wage, max_wage + 1, step):
        search_url = f"https://www.jobs.cz/prace/{city}/?q%5B%5D={position}&salary={wage}&locality%5Bradius%5D=0"
        page_text = get_job_count(search_url)
        index_start = page_text.find("Našli jsme ")
        if index_start != -1:
            index_end = page_text.find(" nabídek", index_start)
            if index_end != -1:
                job_count = int(page_text[index_start+len("Našli jsme "):index_end])
                frequencies[wage] = job_count
                time.sleep(random.uniform(0.5, 2))  # Add random pause to simulate human-like behavior

    # Calculate number of positions within each wage range
    prev_freq = 0
    for wage, freq in frequencies.items():
        positions[wage] = max(0, prev_freq - freq)
        prev_freq = freq

    # Save data to Excel file
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    save_to_excel(frequencies, positions, desktop)

    # Display textual results
    result_label.config(text="Frequencies of job offers within the wage range:")
    frequencies_text = ""
    for wage, freq in frequencies.items():
        frequencies_text += f"Wage: {wage} CZK - Frequency: {freq} - Positions: {positions[wage]}\n"
    frequencies_label.config(text=frequencies_text)

    # Plot histograms
    min_freq = min(frequencies.values())
    plt.figure(figsize=(8, 6))

    plt.subplot(2, 1, 1)
    plt.bar(frequencies.keys(), frequencies.values(), width=step*0.8, align='center')
    plt.xlabel('Wage (CZK)')
    plt.ylabel('Frequency')
    plt.title('Job Offers Frequency by Wage')
    plt.grid(True)
    plt.ylim(min_freq - 5, max(frequencies.values()) + 5)  # Adjust y-axis limits

    plt.subplot(2, 1, 2)
    plt.bar(positions.keys(), positions.values(), width=step*0.8, align='center')
    plt.xlabel('Wage (CZK)')
    plt.ylabel('Number of Positions')
    plt.title('Number of Positions by Wage')
    plt.grid(True)

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

def save_to_excel(data, positions, desktop_path):
    wb = Workbook()
    ws = wb.active
    ws.append(["Wage (CZK)", "Frequency", "Positions"])
    for wage, frequency in data.items():
        ws.append([wage, frequency, positions[wage]])
    file_path = os.path.join(desktop_path, "job_search_results.xlsx")
    wb.save(file_path)

def main():
    root = tk.Tk()
    root.title("Job Search")

    tk.Label(root, text="Position:").grid(row=0, column=0, sticky="w")
    tk.Label(root, text="City:").grid(row=1, column=0, sticky="w")
    tk.Label(root, text="Minimum Wage (CZK):").grid(row=2, column=0, sticky="w")
    tk.Label(root, text="Maximum Wage (CZK):").grid(row=3, column=0, sticky="w")
    tk.Label(root, text="Step (CZK):").grid(row=4, column=0, sticky="w")

    global position_entry, city_entry, min_wage_entry, max_wage_entry, step_entry, result_label, frequencies_label

    position_entry = tk.Entry(root)
    city_entry = tk.Entry(root)
    min_wage_entry = tk.Entry(root)
    max_wage_entry = tk.Entry(root)
    step_entry = tk.Entry(root)

    position_entry.grid(row=0, column=1)
    city_entry.grid(row=1, column=1)
    min_wage_entry.grid(row=2, column=1)
    max_wage_entry.grid(row=3, column=1)
    step_entry.grid(row=4, column=1)

    search_button = tk.Button(root, text="Search", command=search_jobs)
    search_button.grid(row=5, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=6, column=0, columnspan=2)

    frequencies_label = tk.Label(root, text="")
    frequencies_label.grid(row=7, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
