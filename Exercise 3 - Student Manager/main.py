import tkinter as tk
from tkinter import ttk, messagebox
import os

def load_data(filename): # Load student data from file
    students = []
    try:
        base_path = os.path.dirname(os.path.abspath(__file__)) # Used this method to get correct path as previously had issues
        file_path = os.path.join(base_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()[1:]  # Skips first line
            for line in lines:
                parts = [p.strip() for p in line.split(',')]
                if len(parts) == 6:
                    code, name = parts[0], parts[1]
                    c1, c2, c3, exam = map(int, parts[2:])
                    coursework_total = c1 + c2 + c3
                    total = coursework_total + exam
                    percent = (total / 160) * 100
                    grade = (
                        'A' if percent >= 70 else
                        'B' if percent >= 60 else
                        'C' if percent >= 50 else
                        'D' if percent >= 40 else
                        'F'
                    )
                    students.append({
                        'code': code, 'name': name,
                        'coursework': coursework_total,
                        'exam': exam,
                        'percent': percent,
                        'grade': grade
                    })
    except FileNotFoundError:
        messagebox.showerror("Error", f"Could not find {filename} in program folder.") # In case file is missing
    return students

def format_student(student): # Format student data for display
    return (f"Name: {student['name']}\n"
            f"ID: {student['code']}\n"
            f"Coursework Total: {student['coursework']}\n"
            f"Exam Mark: {student['exam']}\n"
            f"Overall %: {student['percent']:.2f}\n"
            f"Grade: {student['grade']}\n"
            "----------------------\n")

def view_all(): # Function to view all students
    output_box.delete(1.0, tk.END)
    if not students:
        output_box.insert(tk.END, "No student data loaded.\n")
        return
    total = 0
    for s in students:
        output_box.insert(tk.END, format_student(s))
        total += s['percent']
    avg = total / len(students)
    output_box.insert(tk.END, f"\nTotal Students: {len(students)}")
    output_box.insert(tk.END, f"\nAverage Percentage: {avg:.2f}%\n")

def view_individual(): # Function to view individual student
    selected = student_var.get()
    output_box.delete(1.0, tk.END)
    if not selected:
        output_box.insert(tk.END, "Please select a student.")
        return
    for s in students:
        if s['name'] == selected:
            output_box.insert(tk.END, format_student(s))
            return
    output_box.insert(tk.END, "Student not found.")

def view_highest(): # Function to view highest scoring student
    output_box.delete(1.0, tk.END)
    if not students:
        output_box.insert(tk.END, "No data available.\n")
        return
    top = max(students, key=lambda s: s['percent'])
    output_box.insert(tk.END, "Highest Scoring Student:\n")
    output_box.insert(tk.END, format_student(top))

def view_lowest(): # Function to view lowest scoring student
    output_box.delete(1.0, tk.END)
    if not students:
        output_box.insert(tk.END, "No data available.\n")
        return
    low = min(students, key=lambda s: s['percent'])
    output_box.insert(tk.END, "Lowest Scoring Student:\n")
    output_box.insert(tk.END, format_student(low))

# Main GUI Setup

root = tk.Tk()
root.title("Student Manager Program")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#113823")
style = ttk.Style()
style.configure(".", font=("Calibri", 12))

# Load student data

students = load_data("studentMarks.txt")

# Dropdown for student selection

student_var = tk.StringVar()
student_names = [s['name'] for s in students]

ttk.Label(root, text="Select a Student:", background="#113823", foreground="white", font=("Calibri", 24, "bold")).pack(pady=15)
dropdown = ttk.OptionMenu(root, student_var, *student_names)
dropdown.pack()

# Buttons and Button Frame

btn_frame = tk.Frame(root, background="#113823")
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="View All", command=view_all).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="View Individual", command=view_individual).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Highest", command=view_highest).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="Lowest", command=view_lowest).grid(row=0, column=3, padx=5)

# Scrollable output box

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_box = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, height=15, width=70)
output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=output_box.yview)

root.mainloop()