# Disclaimer:
# This code/script/application/program is solely for educational and learning purposes.
# All information, datasets, images, code, and materials are presented in good faith and
# intended for instructive use. However, noarche make no representation or warranty, 
# express or implied, regarding the accuracy, adequacy, validity, reliability, availability,
# or completeness of any data or associated materials.
# Under no circumstance shall noarche have any liability to you for any loss, damage, or 
# misinterpretation arising due to the use of or reliance on the provided data. Your utilization
# of the code and your interpretations thereof are undertaken at your own discretion and risk.
#
# By executing script/code/application, the user acknowledges and agrees that they have read, 
# understood, and accepted the terms and conditions (or any other relevant documentation or 
#policy) as provided by noarche.
#
#Visit https://github.com/noarche for more information. 
#
#  _.··._.·°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°°·.·°·._.··._
# ███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗██╗  ██╗███████╗
# ████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
# ██╔██╗ ██║██║   ██║███████║██████╔╝██║     ███████║█████╗  
# ██║╚██╗██║██║   ██║██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  
# ██║ ╚████║╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║███████╗
# ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
# °°°·._.··._.·°°°·.°·..·°¯°··°¯°·.·°.·°°°°·.·°·._.··._.·°°°

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import re
import os



def update_output():

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, input_text.get(1.0, tk.END))
    update_line_count()

def update_line_count():
    input_lines.set(f"Input Lines: {len(input_text.get(1.0, tk.END).splitlines())}")
    output_lines.set(f"Output Lines: {len(output_text.get(1.0, tk.END).splitlines())}")

root = tk.Tk()
root.title("ComboToolPro GUI v1.1.1 by noarch")
root.geometry("1130x480")
root.resizable(False, False)
root.configure(bg="#333")


style = ttk.Style(root)
style.configure(
    "TFrame", background="#333"
)
style.configure(
    "TLabel", background="#333", foreground="#ddd"
)
style.configure(
    "TButton", background="#555", foreground="black"
)
style.configure(
    "TText", background="#444", foreground="#ddd", insertbackground='white'
)

main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_label = ttk.Label(main_frame, text="Input:")
input_label.grid(row=0, column=0, sticky=tk.W, pady=5)

output_label = ttk.Label(main_frame, text="Output:")
output_label.grid(row=2, column=0, sticky=tk.W, pady=5)


input_text = tk.Text(main_frame, wrap=tk.WORD, height=10)
input_text.grid(row=1, column=0, pady=5, sticky=tk.EW)
input_text.bind("<KeyRelease>", lambda e: update_line_count())

output_text = tk.Text(main_frame, wrap=tk.WORD, height=10)
output_text.grid(row=3, column=0, pady=5, sticky=tk.EW)


input_lines = tk.StringVar()
input_lines_label = ttk.Label(main_frame, textvariable=input_lines)
input_lines_label.grid(row=0, column=0, sticky=tk.W, pady=5)

output_lines = tk.StringVar()
output_lines_label = ttk.Label(main_frame, textvariable=output_lines)
output_lines_label.grid(row=2, column=0, sticky=tk.W, pady=5)


def paste_to_input():
    """Paste content from clipboard to input_text widget."""
    try:
        clipboard_content = root.clipboard_get()
        input_text.delete(1.0, tk.END)
        input_text.insert(tk.END, clipboard_content)
        update_line_count()
    except tk.TclError:
        pass

def copy_from_output():
    """Copy content from output_text widget to clipboard."""
    output_content = output_text.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(output_content)
    
def remove_duplicates():
    """Remove duplicate lines from input and display in output."""
    lines = input_text.get(1.0, tk.END).splitlines()
    unique_lines = list(dict.fromkeys(lines))
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "\n".join(unique_lines))
    update_line_count()
    
def extract_by_search():
    """Function to extract lines by a search term and save to file."""
    search_term = simpledialog.askstring("Search", "Enter the term to search for:")
    
    if search_term:
        matched_lines = [line for line in input_text.get(1.0, tk.END).splitlines() if search_term.lower() in line.lower()]


        with open(f"{search_term}.txt", "a", encoding="utf-8") as file:  # "a" mode appends to the file
            for line in matched_lines:
                file.write(line + '\n')

        with open(f"{search_term}.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            cleaned_lines = list(dict.fromkeys(lines))

        with open(f"{search_term}.txt", "w", encoding="utf-8") as file:
            file.writelines(cleaned_lines)
        
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, ''.join(cleaned_lines))
        update_line_count()

        
def extract_32_chars_after_colon():
    """Extract lines where the content after the colon is exactly 32 characters and save to file."""
    pattern = re.compile(r":.{32}$")
    matched_lines = [line for line in input_text.get(1.0, tk.END).splitlines() if pattern.search(line)]


    with open("_Extracted_MD5_.txt", "a", encoding="utf-8") as file:  # "a" mode appends to the file
        for line in matched_lines:
            file.write(line + '\n')

    with open("_Extracted_MD5_.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        cleaned_lines = list(dict.fromkeys(lines))

    with open("_Extracted_MD5_.txt", "w", encoding="utf-8") as file:
        file.writelines(cleaned_lines)
        
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ''.join(cleaned_lines))
    update_line_count()

    
def show_domain_statistics():
    """Display domain statistics in the output_text widget in descending order."""
    lines = input_text.get(1.0, tk.END).splitlines()
    domains = [re.search(r"@(.+?)\.", line, re.IGNORECASE) for line in lines]
    domain_list = [match.group(1).lower() for match in domains if match]  # Convert to lowercase

    domain_stats = {}
    total = len(domain_list)
    for domain in domain_list:
        if domain not in domain_stats:
            domain_stats[domain] = 0
        domain_stats[domain] += 1

    sorted_stats = sorted(domain_stats.items(), key=lambda x: x[1], reverse=True)
    
    stats_output = []
    for domain, count in sorted_stats:
        percentage = (count / total) * 100
        stats_output.append(f"{count} {domain} Lines ({percentage:.2f}%)")

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, '\n'.join(stats_output))
    update_line_count()


def filter_colon_lines():
    """Keep only lines containing a colon and with 5 to 28 characters after the colon."""
    lines = input_text.get(1.0, tk.END).splitlines()
    filtered_lines = []
    
    for line in lines:
        if ":" in line:
            _, _, after_colon = line.partition(":")
            after_length = len(after_colon.strip())
            if 5 <= after_length <= 28:
                filtered_lines.append(line)
    
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, '\n'.join(filtered_lines))
    update_line_count()

def remove_after_space():
    """Remove content after the first space in each line."""
    lines = input_text.get(1.0, tk.END).splitlines()
    processed_lines = [line.split(" ")[0] for line in lines]
    
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, '\n'.join(processed_lines))
    update_line_count()

import random
from tkinter import simpledialog

def organize_lines():
    """Provide multiple sorting options and sort lines based on user's choice."""
    options = ["A-Z", "Z-A", "0-9", "Shortest to longest", "Longest to shortest", "Randomize lines"]
    choice = simpledialog.askstring("Organize", "Choose an option number:\n1. A-Z\n2. Z-A\n3. 0-9\n4. Short to long\n5. Long to short\n6. Randomize Lines", initialvalue="A-Z", parent=root)

    lines = input_text.get(1.0, tk.END).splitlines()
    if choice == "1":
        sorted_lines = sorted(lines)
    elif choice == "2":
        sorted_lines = sorted(lines, reverse=True)
    elif choice == "3":
        sorted_lines = sorted(lines, key=lambda x: [int(t) if t.isdigit() else t for t in re.split('(\d+)', x)])
    elif choice == "4":
        sorted_lines = sorted(lines, key=len)
    elif choice == "5":
        sorted_lines = sorted(lines, key=len, reverse=True)
    elif choice == "6":
        random.shuffle(lines)
        sorted_lines = lines
    else:
        return

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, '\n'.join(sorted_lines))
    update_line_count()

def split_by_lines():
    """Split content based on user-defined number of lines and save to a specified directory."""
    num_lines = simpledialog.askinteger("Split", "How many lines for each split?", parent=root)
    if not num_lines:
        return
    
    split_name = simpledialog.askstring("Name", "What to name the split?", parent=root)
    if not split_name:
        return

    directory = os.path.join("split", split_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    lines = input_text.get(1.0, tk.END).splitlines()
    for index, start_line in enumerate(range(0, len(lines), num_lines), 1):
        file_path = os.path.join(directory, f"{split_name}_{index}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write('\n'.join(lines[start_line:start_line + num_lines]))

def combine_files():
    """Combine all text files from 'toCombine' directory, save to '_combined_.txt' and remove duplicates."""
    combined_content = []
    dir_path = "toCombine"

    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            with open(os.path.join(dir_path, filename), "r", encoding="utf-8") as file:
                combined_content.extend(file.readlines())

    with open("_combined_.txt", "w", encoding="utf-8") as file:
        file.writelines(combined_content)

    with open("_combined_.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        unique_lines = list(dict.fromkeys(lines))

    with open("_combined_.txt", "w", encoding="utf-8") as file:
        file.writelines(unique_lines)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ''.join(unique_lines))
    update_line_count()
    
def save_output():
    """Save the content of output_text to a file named after user's input."""
    filename = simpledialog.askstring("Save As", "Enter the name for the file:", parent=root)
    
    if not filename:
        return

    if not filename.endswith(".txt"):
        filename += ".txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_text.get(1.0, tk.END))




button_frame = ttk.Frame(main_frame)
button_frame.grid(row=5, column=0, pady=10, columnspan=2)

paste_btn = ttk.Button(button_frame, text="Paste Input", command=paste_to_input)
paste_btn.pack(side=tk.LEFT, padx=5)

copy_btn = ttk.Button(button_frame, text="Copy Output", command=copy_from_output)
copy_btn.pack(side=tk.LEFT, padx=5)

remove_dup_btn = ttk.Button(button_frame, text="Remove Duplicates", command=remove_duplicates)
remove_dup_btn.pack(side=tk.LEFT, padx=5)

extract_search_btn = ttk.Button(button_frame, text="Extract Domain", command=extract_by_search)
extract_search_btn.pack(side=tk.LEFT, padx=5)

extract_32chars_btn = ttk.Button(button_frame, text="Extract MD5", command=extract_32_chars_after_colon)
extract_32chars_btn.pack(side=tk.LEFT, padx=5)

domain_stats_btn = ttk.Button(button_frame, text="Statistics", command=show_domain_statistics)
domain_stats_btn.pack(side=tk.LEFT, padx=5)

filter_colon_btn = ttk.Button(button_frame, text="Cleanup", command=filter_colon_lines)
filter_colon_btn.pack(side=tk.LEFT, padx=5)

remove_capture_btn = ttk.Button(button_frame, text="Remove capture", command=remove_after_space)
remove_capture_btn.pack(side=tk.LEFT, padx=5)

organize_btn = ttk.Button(button_frame, text="Organize", command=organize_lines)
organize_btn.pack(side=tk.LEFT, padx=5)

split_btn = ttk.Button(button_frame, text="Split", command=split_by_lines)
split_btn.pack(side=tk.LEFT, padx=5)

combine_btn = ttk.Button(button_frame, text="Combine", command=combine_files)

save_output_btn = ttk.Button(button_frame, text="Save Output", command=save_output)
save_output_btn.pack(side=tk.LEFT, padx=5)

combine_btn.pack(side=tk.LEFT, padx=5)

update_line_count()

root.mainloop()


# Disclaimer:
# This code/script/application/program is solely for educational and learning purposes.
# All information, datasets, images, code, and materials are presented in good faith and
# intended for instructive use. However, noarche make no representation or warranty, 
# express or implied, regarding the accuracy, adequacy, validity, reliability, availability,
# or completeness of any data or associated materials.
# Under no circumstance shall noarche have any liability to you for any loss, damage, or 
# misinterpretation arising due to the use of or reliance on the provided data. Your utilization
# of the code and your interpretations thereof are undertaken at your own discretion and risk.
#
# By executing script/code/application, the user acknowledges and agrees that they have read, 
# understood, and accepted the terms and conditions (or any other relevant documentation or 
#policy) as provided by noarche.
#
#Visit https://github.com/noarche for more information. 
#
#  _.··._.·°°°·.°·..·°¯°·._.··._.·°¯°·.·° .·°°°°·.·°·._.··._
# ███╗   ██╗ ██████╗  █████╗ ██████╗  ██████╗██╗  ██╗███████╗
# ████╗  ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
# ██╔██╗ ██║██║   ██║███████║██████╔╝██║     ███████║█████╗  
# ██║╚██╗██║██║   ██║██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  
# ██║ ╚████║╚██████╔╝██║  ██║██║  ██║╚██████╗██║  ██║███████╗
# ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
# °°°·._.··._.·°°°·.°·..·°¯°··°¯°·.·°.·°°°°·.·°·._.··._.·°°°