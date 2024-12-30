import tkinter as tk
from tkinter import ttk

classes = 10
columns = 6
benches = 6
total_benches = columns * benches
sections = ['CSE', 'AIE', 'ECE', 'EEE', 'MEE', 'RAE']
CSE_strength = 60
AIE_strength = 70
ECE_strength = 60
EEE_strength = 30
MEE_strength = 30
RAE_strength = 70

course_strengths = {
    'CSE': CSE_strength,
    'AIE': AIE_strength,
    'ECE': ECE_strength,
    'EEE': EEE_strength,
    'MEE': MEE_strength,
    'RAE': RAE_strength
}

students_CSE = []
students_AIE = []
students_ECE = []
students_EEE = []
students_MEE = []
students_RAE = []

for section in sections: 
    if section == 'CSE':
        for i in range(1, course_strengths['CSE'] + 1):
            students_CSE.append(section + 'student' + str(i))
    elif section == 'AIE':
        for i in range(1, course_strengths['AIE'] + 1):
            students_AIE.append(section + 'student' + str(i))
    elif section == 'ECE':
        for i in range(1, course_strengths['ECE'] + 1):
            students_ECE.append(section + 'student' + str(i))
    elif section == 'EEE':
        for i in range(1, course_strengths['EEE'] + 1):
            students_EEE.append(section + 'student' + str(i))
    elif section == 'MEE':
        for i in range(1, course_strengths['MEE'] + 1):
            students_MEE.append(section + 'student' + str(i))
    else:
        for i in range(1, course_strengths['RAE'] + 1):
            students_RAE.append(section + 'student' + str(i))

def seating_arrangement(students_CSE, students_AIE, students_ECE, students_EEE, students_MEE, students_RAE, columns, benches, total_benches, course_list):
    print("\nArrangement time for exams")
    arrangement = [[[''] * benches for _ in range(columns)] for _ in range(classes)]

    pairs = [
        [students_CSE, students_ECE, 'CSE-ECE'],
        [students_AIE, students_RAE, 'AIE-RAE'],
        [students_MEE, students_EEE, 'MEE-EEE']
    ]

    indices = {
        'CSE': 0, 'AIE': 0,
        'ECE': 0, 'EEE': 0,
        'MEE': 0, 'RAE': 0
    }

    current_pair = 0  

    for classroom in range(classes):
        print(f"\nClassroom {classroom + 1} Seating Arrangement:")
        print("=" * 100)

        for col in range(columns):
            students_list1, students_list2, pair_name = pairs[current_pair]

            for i in range(0, benches, 2):
                if indices[pair_name.split('-')[0]] < len(students_list1):
                    arrangement[classroom][col][i] = students_list1[indices[pair_name.split('-')[0]]]
                    indices[pair_name.split('-')[0]] += 1

                if i + 1 < benches and indices[pair_name.split('-')[1]] < len(students_list2):
                    arrangement[classroom][col][i + 1] = students_list2[indices[pair_name.split('-')[1]]]
                    indices[pair_name.split('-')[1]] += 1

            if indices[pair_name.split('-')[0]] == len(students_list1) and indices[pair_name.split('-')[1]] < len(students_list2):
                for j in range(i + 1, benches):
                    arrangement[classroom][col][j] = students_list2[indices[pair_name.split('-')[1]]]
                    indices[pair_name.split('-')[1]] += 1

            elif indices[pair_name.split('-')[1]] == len(students_list2) and indices[pair_name.split('-')[0]] < len(students_list1):
                for j in range(i, benches, 2):
                    arrangement[classroom][col][j] = students_list1[indices[pair_name.split('-')[0]]]
                    indices[pair_name.split('-')[0]] += 1

            if indices[pair_name.split('-')[0]] == len(students_list1) and indices[pair_name.split('-')[1]] == len(students_list2):
                current_pair = (current_pair + 1) % len(pairs)

            seat_strings = []
            for seat in arrangement[classroom][col]:
                if seat != '':
                    seat_strings.append(str(seat))
                else:
                    seat_strings.append('EMPTY')
            row_str = " | ".join(seat_strings)
            print(row_str)


        print("-" * 100)

    return arrangement


def student_counts(students_CSE, students_AIE, students_ECE, students_EEE, students_MEE, students_RAE):
    print("\nStudent Counts:")
    pairs = [
        ['CSE-ECE', len(students_CSE), len(students_ECE)],
        ['AIE-RAE', len(students_AIE), len(students_RAE)],
        ['MEE-EEE', len(students_MEE), len(students_EEE)]
    ]

    total = 0
    for pair_name, count1, count2 in pairs:
        course1, course2 = pair_name.split('-')
        print(f"{course1} Students: {count1}, {course2} Students: {count2}")
        total += count1 + count2
    print(f"Total Students: {total}")

def seating_gui(arrangement):
    root = tk.Tk()
    root.title("Seating Arrangement")

    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for i in range(0, classes, 2):  # Iterate in pairs of classrooms
        frame_row = ttk.Frame(scrollable_frame)
        frame_row.grid(row=i // 2, column=0, padx=10, pady=10, sticky="nsew")

        for j in range(2):  # Create two classrooms in a row
            classroom_index = i + j
            if classroom_index < classes:
                frame = ttk.LabelFrame(frame_row, text=f"Classroom {classroom_index + 1}")
                frame.grid(row=0, column=j, padx=10, pady=10, sticky="nsew")

                for col in range(columns):
                    col_label = ttk.Label(frame, text=f"Column {col + 1}")
                    col_label.grid(row=0, column=col, padx=5, pady=5)

                    for row in range(benches):
                        seat = arrangement[classroom_index][col][row]
                        seat_label = ttk.Label(frame, text=seat if seat else "EMPTY", borderwidth=1, relief="solid")
                        seat_label.grid(row=row + 1, column=col, padx=5, pady=5)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()

student_counts(students_CSE, students_AIE, students_ECE, students_EEE, students_MEE, students_RAE)

arrangement = seating_arrangement(students_CSE, students_AIE, students_ECE, students_EEE, students_MEE, students_RAE, columns, benches, total_benches, sections)

seating_gui(arrangement)