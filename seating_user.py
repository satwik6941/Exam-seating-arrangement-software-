import random
import tkinter as tk 
from tkinter import ttk

classes = 55
columns = 5
benches = 7
total_benches = columns * benches
sections = ['CSE', 'AIE', 'AID', 'ECE', 'EEE', 'MEE', 'RAE']

student_year_lists = {
    "CSE_year_1": [], "CSE_year_2": [], "CSE_year_3": [],
    "AIE_year_1": [], "AIE_year_2": [], "AIE_year_3": [],
    "AID_year_1": [], "AID_year_2": [], "AID_year_3": [],
    "ECE_year_1": [], "ECE_year_2": [], "ECE_year_3": [],
    "EEE_year_1": [], "EEE_year_2": [], "EEE_year_3": [],
    "MEE_year_1": [], "MEE_year_2": [], "MEE_year_3": [],
    "RAE_year_1": [], "RAE_year_2": [], "RAE_year_3": []
}

print("Let's BEGIN")
while True:
    print("1 - 1st year, 2 - 2nd year, 3 - 3rd year, exit - exit for the arrangement \n")
    student_year_selection = input("Enter the year of the student: ")
    
    if student_year_selection.lower() == "exit":
        break
    
    if student_year_selection == '1':
        print("CSE, AIE, AID, ECE, EEE, MEE, RAE,")
        print("exit - exit for the arrangement ")
        student_section_selection = input("Enter the section of the student: ").upper()
        
        if student_section_selection.lower() == "exit":
            break
        
        if not student_section_selection.isalpha():
            print("ERROR")
            continue
        
        if student_section_selection not in sections:
            print("Please enter one of the following: CSE, AIE, AID, ECE, EEE, MEE, RAE")
            continue
        
        print("exit - exit for the arrangement ")
        roll_numbers = input("Enter the number of students: ")
        if roll_numbers.lower() == "exit":
            break
        
        if not roll_numbers.isdigit():
            print("ERROR")
            continue
        
        if student_section_selection in sections:
            for i in range(1, int(roll_numbers) + 1):
                student_year_lists[f"{student_section_selection}_year_1"].append(f"{student_section_selection}Y1student{i}")
            print_request = input("Do you want to print the list of students? (Y/N), exit - exit for the arrangement : ")
            if print_request in ('Y', 'y'):
                print(student_year_lists[f"{student_section_selection}_year_1"])
            elif print_request in ('N', 'n'):
                print("Thank you for using the program!")
            elif print_request.lower() == "exit":
                break
            else:
                print("ERROR")
        else:
            print("ERROR")
    
    elif student_year_selection == '2':
        print("CSE, AIE, AID, ECE, EEE, MEE, RAE")
        print("exit - exit for the arrangement ")
        student_section_selection = input("Enter the section of the student: ").upper()
        
        if student_section_selection.lower() == "exit":
            break
        
        if not student_section_selection.isalpha():
            print("ERROR")
            continue
        
        if student_section_selection not in sections:
            print("Please enter one of the following: CSE, AIE, AID, ECE, EEE, MEE, RAE")
            continue
        
        print("exit - exit for the arrangement ")
        roll_numbers = input(f"Enter the number of students in {student_section_selection}: ")
        if roll_numbers.lower() == "exit":
            break
        
        if not roll_numbers.isdigit():
            print("ERROR")
            continue
        
        if student_section_selection in sections:
            for i in range(1, int(roll_numbers) + 1):
                student_year_lists[f"{student_section_selection}_year_2"].append(f"{student_section_selection}Y2student{i}")
            print_request = input("Do you want to print the list of students? (Y/N),  exit - exit for the arrangement : ")
            if print_request in ('Y', 'y'):
                print(student_year_lists[f"{student_section_selection}_year_2"])
            elif print_request in ('N', 'n'):
                print("Thank you for using the program!")
            elif print_request.lower() == "exit":
                break
            else:
                print("ERROR")
        else:
            print("ERROR")
    
    elif student_year_selection == '3':
        print("CSE, AIE, AID, ECE, EEE, MEE, RAE")
        print("exit - exit for the arrangement ")
        student_section_selection = input("Enter the section of the student: ").upper()
        
        if student_section_selection.lower() == "exit":
            break
        
        if not student_section_selection.isalpha():
            print("ERROR")
            continue
        
        if student_section_selection not in sections:
            print("Please enter one of the following: CSE, AIE, AID, ECE, EEE, MEE, RAE")
            continue
        
        print(" exit - exit for the arrangement ")
        roll_numbers = input(f"Enter the number of students in {student_section_selection}: ")
        if roll_numbers.lower() == "exit":
            break
        
        if not roll_numbers.isdigit():
            print("ERROR")
            continue
        
        if student_section_selection in sections:
            for i in range(1, int(roll_numbers) + 1):
                student_year_lists[f"{student_section_selection}_year_3"].append(f"{student_section_selection}Y3student{i}")
            print_request = input("Do you want to print the list of students? (Y/N),  exit - exit for the arrangement : ")
            if print_request in ('Y', 'y'):
                print(student_year_lists[f"{student_section_selection}_year_3"])
            elif print_request in ('N', 'n'):
                print("Thank you for using the program!")
            elif print_request.lower() == "exit":
                break
            else:
                print("ERROR")
        else:
            print("ERROR")
    
    else:
        print("ERROR")
courses = { 
    "CSE_year_1": student_year_lists["CSE_year_1"], "CSE_year_2": student_year_lists["CSE_year_2"], "CSE_year_3": student_year_lists["CSE_year_3"],
    "AIE_year_1": student_year_lists["AIE_year_1"], "AIE_year_2": student_year_lists["AIE_year_2"], "AIE_year_3": student_year_lists["AIE_year_3"],
    "AID_year_1": student_year_lists["AID_year_1"], "AID_year_2": student_year_lists["AID_year_2"], "AID_year_3": student_year_lists["AID_year_3"],
    "ECE_year_1": student_year_lists["ECE_year_1"], "ECE_year_2": student_year_lists["ECE_year_2"], "ECE_year_3": student_year_lists["ECE_year_3"],
    "EEE_year_1": student_year_lists["EEE_year_1"], "EEE_year_2": student_year_lists["EEE_year_2"], "EEE_year_3": student_year_lists["EEE_year_3"],
    "MEE_year_1": student_year_lists["MEE_year_1"], "MEE_year_2": student_year_lists["MEE_year_2"], "MEE_year_3": student_year_lists["MEE_year_3"],
    "RAE_year_1": student_year_lists["RAE_year_1"], "RAE_year_2": student_year_lists["RAE_year_2"], "RAE_year_3": student_year_lists["RAE_year_3"]
}

import random

def seating_arrangement(classes, columns, benches, courses):
    print("\nArrangement time for exams")
    arrangement = [[[''] * benches for _ in range(columns)] for _ in range(classes)]

    active_courses = {key: value for key, value in courses.items() if value and len(value) > 0}
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
        print(f"\nClassroom {classroom + 1} Seating Arrangement:")
        print("=" * 100)

        current_column = 0
        current_bench = 0

        while current_pair < len(pairs):
            students_list1_name, students_list2_name = pairs[current_pair]
            students_list1 = active_courses[students_list1_name]
            students_list2 = active_courses[students_list2_name]

            while current_column < columns:
                print(f"Column {current_column + 1}: ", end="")
                while current_bench < benches:
                    if bench_count % 2 == 0 and indices[students_list1_name] < len(students_list1):
                        arrangement[classroom][current_column][current_bench] = students_list1[indices[students_list1_name]]
                        indices[students_list1_name] += 1
                    elif bench_count % 2 == 1 and indices[students_list2_name] < len(students_list2):
                        arrangement[classroom][current_column][current_bench] = students_list2[indices[students_list2_name]]
                        indices[students_list2_name] += 1

                    current_bench += 1
                    bench_count += 1

                seat_strings = [
                    str(seat) if seat != '' else 'EMPTY'
                    for seat in arrangement[classroom][current_column]
                ]
                print(" | ".join(seat_strings))

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
                print(f"Column {current_column + 1}: ", end="")
                while current_bench < benches:
                    if indices[last_class] < len(students_list):
                        arrangement[classroom][current_column][current_bench] = students_list[indices[last_class]]
                        indices[last_class] += 1
                    else:
                        arrangement[classroom][current_column][current_bench] = 'EMPTY'

                    current_bench += 2
                    bench_count += 2

                seat_strings = [
                    str(seat) if seat != '' else 'EMPTY'
                    for seat in arrangement[classroom][current_column]
                ]
                print(" | ".join(seat_strings))

                current_column += 1
                current_bench = 0

                if indices[last_class] == len(students_list):
                    break

        if current_pair >= len(pairs) and not last_class:
            while current_column < columns:
                print(f"Column {current_column + 1}: ", end="")
                print("EMPTY | " * (benches - 1) + "EMPTY")
                current_column += 1

        print("-" * 100)

    return arrangement

arrangement = seating_arrangement(classes, columns, benches, courses)

def seating_gui(arrangement):
    root = tk.Tk()
    root.title("Seating Arrangement")

    root.state("zoomed")

    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    classroom_font = ("Arial", 30, "bold") 
    header_font = ("Arial", 20, "bold")   
    seat_font = ("Arial", 18)         

    classes = len(arrangement)
    columns = len(arrangement[0])
    benches = len(arrangement[0][0])

    for i in range(classes):
        frame = tk.Frame(scrollable_frame, pady=10)
        frame.grid(row=i, column=0, padx=20, pady=20, sticky="nsew")
        
        title_label = tk.Label(frame, text=f"Classroom {i + 1}", font=classroom_font, anchor="center")
        title_label.pack(pady=10)

        seating_frame = tk.Frame(frame)
        seating_frame.pack(fill="both", expand=True)

        for col in range(columns):
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

        for col in range(columns):
            seating_frame.columnconfigure(col, weight=1)
        for row in range(benches + 1): 
            seating_frame.rowconfigure(row, weight=1)

    scrollable_frame.columnconfigure(0, weight=1)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()

seating_gui(arrangement)