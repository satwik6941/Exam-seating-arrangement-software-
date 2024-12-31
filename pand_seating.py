import pandas as pd
import random
import tkinter as tk 
from tkinter import ttk

classes = 35
columns = 5
benches = 7
total_benches = columns * benches
sections = ['CSE', 'AIE', 'AID', 'ECE', 'EEE', 'MEE', 'RAE']

df = pd.read_csv("seatingarrangement_data.csv")

first_year_students = []
second_year_students = []
third_year_students = []

student_year_lists = {
    "CSE_year_1": [], "CSE_year_2": [], "CSE_year_3": [],
    "AIE_year_1": [], "AIE_year_2": [], "AIE_year_3": [],
    "AID_year_1": [], "AID_year_2": [], "AID_year_3": [],
    "ECE_year_1": [], "ECE_year_2": [], "ECE_year_3": [],
    "EEE_year_1": [], "EEE_year_2": [], "EEE_year_3": [],
    "MEE_year_1": [], "MEE_year_2": [], "MEE_year_3": [],
    "RAE_year_1": [], "RAE_year_2": [], "RAE_year_3": []
}

for reg_no in df["Registration No's"]:
    if reg_no[11:13] == '24':
        first_year_students.append(reg_no)
    elif reg_no[11:13] == '23':
        second_year_students.append(reg_no)
    elif reg_no[11:13] == '22':
        third_year_students.append(reg_no)
    else:
        print("Error")

def student_classification(first_year_students, second_year_students, third_year_students, student_year_lists):
    for student_roll_no1 in first_year_students:
        if student_roll_no1[8:11] == 'CSE':
            student_year_lists["CSE_year_1"].append(student_roll_no1)
        elif student_roll_no1[8:11] == 'AIE':
            student_year_lists["AIE_year_1"].append(student_roll_no1)
        elif student_roll_no1[8:11] == 'AID':
            student_year_lists["AID_year_1"].append(student_roll_no1)
        elif student_roll_no1[8:11] == 'ECE':
            student_year_lists["ECE_year_1"].append(student_roll_no1)
        elif student_roll_no1[8:11] == 'EEE':
            student_year_lists["EEE_year_1"].append(student_roll_no1)
        elif student_roll_no1[8:11] == 'MEE':
            student_year_lists["MEE_year_1"].append(student_roll_no1)
        elif student_roll_no1[8:11] == 'RAE':
            student_year_lists["RAE_year_1"].append(student_roll_no1)
        else:
            print("Error")

    for student_roll_no2 in second_year_students:
        if student_roll_no2[8:11] == 'CSE':
            student_year_lists["CSE_year_2"].append(student_roll_no2)
        elif student_roll_no2[8:11] == 'AIE':
            student_year_lists["AIE_year_2"].append(student_roll_no2)
        elif student_roll_no2[8:11] == 'AID':
            student_year_lists["AID_year_2"].append(student_roll_no2)
        elif student_roll_no2[8:11] == 'ECE':
            student_year_lists["ECE_year_2"].append(student_roll_no2)
        elif student_roll_no2[8:11] == 'EEE':
            student_year_lists["EEE_year_2"].append(student_roll_no2)
        elif student_roll_no2[8:11] == 'MEE':
            student_year_lists["MEE_year_2"].append(student_roll_no2)
        elif student_roll_no2[8:11] == 'RAE':
            student_year_lists["RAE_year_2"].append(student_roll_no2)
        else:
            print("Error")

    for student_roll_no3 in third_year_students:
        if student_roll_no3[8:11] == 'CSE':
            student_year_lists["CSE_year_3"].append(student_roll_no3)
        elif student_roll_no3[8:11] == 'AIE':
            student_year_lists["AIE_year_3"].append(student_roll_no3)
        elif student_roll_no3[8:11] == 'AID':
            student_year_lists["AID_year_3"].append(student_roll_no3)
        elif student_roll_no3[8:11] == 'ECE':
            student_year_lists["ECE_year_3"].append(student_roll_no3)
        elif student_roll_no3[8:11] == 'EEE':
            student_year_lists["EEE_year_3"].append(student_roll_no3)
        elif student_roll_no3[8:11] == 'MEE':
            student_year_lists["MEE_year_3"].append(student_roll_no3)
        elif student_roll_no3[8:11] == 'RAE':
            student_year_lists["RAE_year_3"].append(student_roll_no3)
        else:
            print("Error")

    return student_year_lists

students_data = student_classification(first_year_students, second_year_students, third_year_students, student_year_lists)

def seating_arrangement(classes, columns, benches, students_data):
    print("\nArrangement time for exams")
    arrangement = [[[''] * benches for _ in range(columns)] for _ in range(classes)]

    active_courses = {key: value for key, value in students_data.items() if value and len(value) > 0}
    active_course_names = list(active_courses.keys())

    random.shuffle(active_course_names)
    pairs = []
    for i in range(0, len(active_course_names) - 1, 2):
        pair = [active_course_names[i], active_course_names[i + 1]]
        pairs.append(pair)

    last_class = None
    if len(active_course_names) % 2 != 0:
        last_class = active_course_names[-1]

    pair_print = input("Do you want to print the pairs formed (Y/N): ")
    if pair_print.lower() == 'y':
        for pair in pairs:
            print(pair)
        if last_class:
            print([last_class])
    elif pair_print.lower() == 'n':
        print("Thank you for using the program!")
    else:
        print("ERROR: Invalid input for pair print option.")

    print("\nThe classes being arranged are:")
    for pair in pairs:
        students_list1_name, students_list2_name = pair
        print(f"{students_list1_name} = {len(active_courses[students_list1_name])}, {students_list2_name} = {len(active_courses[students_list2_name])}")

    if last_class:
        print(f"{last_class} = {len(active_courses[last_class])}")

    indices = {key: 0 for key in active_course_names}

    current_pair = 0
    bench_count = 0 

    for classroom in range(classes):
        current_column = 0
        current_bench = 0

        while current_pair < len(pairs):
            students_list1_name, students_list2_name = pairs[current_pair]
            students_list1 = active_courses[students_list1_name]
            students_list2 = active_courses[students_list2_name]

            while current_column < columns:
                while current_bench < benches:
                    if bench_count % 2 == 0 and indices[students_list1_name] < len(students_list1):
                        arrangement[classroom][current_column][current_bench] = students_list1[indices[students_list1_name]]
                        indices[students_list1_name] += 1
                    elif bench_count % 2 == 1 and indices[students_list2_name] < len(students_list2):
                        arrangement[classroom][current_column][current_bench] = students_list2[indices[students_list2_name]]
                        indices[students_list2_name] += 1

                    current_bench += 1
                    bench_count += 1

                current_column += 1
                current_bench = 0

                if indices[students_list1_name] == len(students_list1) and indices[students_list2_name] == len(students_list2):
                    break

            if indices[students_list1_name] == len(students_list1) and indices[students_list2_name] == len(students_list2):
                current_pair += 1

            if current_column == columns:
                break

        if current_pair >= len(pairs) and last_class:
            students_list = active_courses[last_class]
            while current_column < columns:
                while current_bench < benches:
                    if indices[last_class] < len(students_list):
                        arrangement[classroom][current_column][current_bench] = students_list[indices[last_class]]
                        indices[last_class] += 1
                    else:
                        arrangement[classroom][current_column][current_bench] = 'EMPTY'

                    current_bench += 2
                    bench_count += 2  

                current_column += 1
                current_bench = 0  

                if indices[last_class] == len(students_list):
                    break

    return arrangement

def seating_gui(arrangement):
    root = tk.Tk()
    root.title("Seating Arrangement")

    # Maximize the window without full-screen mode
    root.state("zoomed")

    # Main container
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Define fonts for labels
    classroom_font = ("Arial", 30, "bold")  # Larger font size for classroom titles
    header_font = ("Arial", 20, "bold")    # Font size for column headers
    seat_font = ("Arial", 18)             # Font size for seat labels

    # Iterate classrooms, each on a separate row
    classes = len(arrangement)
    columns = len(arrangement[0])
    benches = len(arrangement[0][0])

    for i in range(classes):
        # Create a frame for the classroom
        frame = tk.Frame(scrollable_frame, pady=10)
        frame.grid(row=i, column=0, padx=20, pady=20, sticky="nsew")
        
        # Center and increase the size of the classroom title
        title_label = tk.Label(frame, text=f"Classroom {i + 1}", font=classroom_font, anchor="center")
        title_label.pack(pady=10)

        # Create a grid for seating arrangement
        seating_frame = tk.Frame(frame)
        seating_frame.pack(fill="both", expand=True)

        for col in range(columns):
            # Column header
            col_label = tk.Label(seating_frame, text=f"Column {col + 1}", font=header_font)
            col_label.grid(row=0, column=col, padx=10, pady=10, sticky="nsew")

            for row in range(benches):
                seat = arrangement[i][col][row]
                seat_label = tk.Label(
                    seating_frame,
                    text=seat if seat else "EMPTY",
                    font=seat_font,
                    borderwidth=1,
                    relief="solid"
                )
                seat_label.grid(row=row + 1, column=col, padx=10, pady=10, sticky="nsew")

        # Configure grid weights for proportional resizing
        for col in range(columns):
            seating_frame.columnconfigure(col, weight=1)
        for row in range(benches + 1):  # Include column header row
            seating_frame.rowconfigure(row, weight=1)

    # Configure main scrollable frame to expand
    scrollable_frame.columnconfigure(0, weight=1)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()

# Capture the seating arrangement returned by the function
arrangement = seating_arrangement(classes, columns, benches, students_data)

# Pass the arrangement to the GUI function
seating_gui(arrangement)
