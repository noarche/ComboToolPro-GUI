import tkinter as tk
from tkinter import filedialog

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            if '@' in line and ':' in line:
                start_index = line.index('@')
                end_index = line.index(':')
                line = line[:start_index] + line[end_index:]
            f.write(line)

def select_file():
    file_path = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def select_output_location():
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file_path)

def process():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    if input_file and output_file:
        process_file(input_file, output_file)
        status_label.config(text="File processed successfully.")
    else:
        status_label.config(text="Please select input and output files.")

# Create GUI
root = tk.Tk()
root.title("Text File Processor")

# Input file selection
input_file_label = tk.Label(root, text="Select Input File:")
input_file_label.grid(row=0, column=0, padx=5, pady=5)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)
input_file_button = tk.Button(root, text="Browse", command=select_file)
input_file_button.grid(row=0, column=2, padx=5, pady=5)

# Output file selection
output_file_label = tk.Label(root, text="Select Output File:")
output_file_label.grid(row=1, column=0, padx=5, pady=5)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)
output_file_button = tk.Button(root, text="Browse", command=select_output_location)
output_file_button.grid(row=1, column=2, padx=5, pady=5)

# Process button
process_button = tk.Button(root, text="Process", command=process)
process_button.grid(row=2, column=1, padx=5, pady=5)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
