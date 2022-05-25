from tkinter import *
import json

####################################################################################################################
# todo SO I DID THE HORIZONTAL CALCULATION OF THE AVERAGE OF EACH SUBJECT, NOW, YOU SHOULD DO THE VERTICAL ONE, AND#
# todo [...] IN THIS STEP, YOU SHOULD TAKE IN CONSIDERATION THE COEFFICIENTS; GOOD LUCK!!!                         #
####################################################################################################################


def advanced():
    window = Tk()
    window.title("Marks Calculator")

    titles = ["Subjects", "Exam N°1", "Exam N°2", "Exam N°3", "Exam N°4", "Activities", "Average"]
    for num, i in enumerate(titles):
        Label(window, text=i).grid(row=0, column=num, pady=2)

    subjects = {
                'EPS': [],
                'HG': [],
                'INF': [],
                'EI': [],
                'ANG': [],
                'AR': [],
                'FR': [],
                'MATH': [],
                'PH': [],
                'PC': [],
                'SVT': [],
                'Average': []
                }
    for num, i in enumerate(subjects):
        Label(window, text=i).grid(row=num+1, column=0, pady=2)
        for j in range(1, 7):
            ent = Entry(window)
            subjects[i].append(ent)
            ent.grid(row=num+1, column=j, padx=2)

    coefficient_list = []
    for i in subjects:
        if i == "MATH" or i == "PC" or i == "SVT":
            coefficient_list.append(4)
        elif i == "FR" or i == "ANG":
            coefficient_list.append(3)
        elif i != "Average":
            coefficient_list.append(2)

    subject_grades = {}

    def display_average():
        def get_grades():
            for i in subjects:
                subject_grades[i] = []
                for j in subjects[i]:
                    subject_grades[i].append(j.get())
        get_grades()

        average_list = []

        # The horizontal average calculation
        for i in subject_grades:
            average = 0
            grades_list = subject_grades[i]

            # Split in exam & activity grades
            exam_grades = grades_list[:4]
            activities_grade = float(grades_list[4]) if grades_list[4] != '' else ''

            # Gets how many exams got
            length = len(exam_grades)
            for j in exam_grades:
                if j == '':
                    length -= 1

            # Sees if the activities field was filled or not
            if not isinstance(activities_grade, str):
                sum_grades = sum([float(i) for i in grades_list[:length]])
                average = (sum_grades/length)*0.75 + activities_grade*0.25
                average_list.append(average)
            else:
                sum_grades = sum([float(i) for i in grades_list[:length]])
                if length != 0:
                    average = sum_grades/length
                    average_list.append(average)

            # Put the average in its place
            subjects[i][5].delete(0, END)
            subjects[i][5].insert(INSERT, '%.2f' % average)

        # The vertical average calculation
        for i in range(5):
            # Get the grades
            new_subject_grades = [subject_grades[l] for l in subject_grades][:len(subject_grades)-1]
            grades_list = [j[i] for j in new_subject_grades]

            # Calculate their average
            sum_grades = num_grades = sum_coefficients = 0
            for num, k in enumerate(grades_list):
                coefficient = coefficient_list[num]
                if k != '':
                    sum_grades += float(k) * coefficient
                    num_grades += 1
                    sum_coefficients += coefficient
            if num_grades != 0:
                average = sum_grades/sum_coefficients
            else:
                average = 0

            # Put the average in its appropriate place
            subjects['Average'][i].delete(0, END)
            subjects['Average'][i].insert(INSERT, "%.2f" % average)
            subject_grades['Average'][i] = average

        # Calculate the final big grade
        copy_subject_grades = {i: subject_grades[i] for i in subject_grades}
        for sub in copy_subject_grades:
            lst = copy_subject_grades[sub][:-1]
            for num, grade_str in enumerate(lst):
                try:
                    lst[num] = float(copy_subject_grades[sub][num])
                except ValueError:
                    lst[num] = None
            for i in range(lst.count(None)):
                lst.pop(lst.index(None))

            copy_subject_grades[sub] = lst[:]
        
        average_lst = []
        sum_coeff = 0
        del copy_subject_grades["Average"]
        for sub in copy_subject_grades:
            for grade in copy_subject_grades[sub]:
                if sub == "MATH" or sub == "PC" or sub == "SVT":
                    coeff = 4
                elif sub == "FR" or sub == "ANG":
                    coeff = 3
                else:
                    coeff = 2
                sum_coeff += coeff
                average_lst.append(coeff * grade)
        average = sum(average_lst) / sum_coeff

        subject_grades['Average'][-1] = average
        subjects['Average'][-1].delete(0, END)
        subjects['Average'][-1].insert(INSERT, "%.2f" % average)


    def clear():
        for i in subjects:
            for entry in subjects[i]:
                entry.delete(0, END)

    def save_data():
        display_average()
        with open("subject_grades.json", 'w') as f:
            json.dump(subject_grades, f)

    def import_data():
        with open("subject_grades.json", 'r') as f:
            json_load = json.load(f)
            if json_load != {}:
                subject_grades = json_load

                for i in subjects:
                    for j in range(5):
                        ent = subjects[i][j]
                        ent.delete(0, END)
                        ent.insert(INSERT, subject_grades[i][j])
        display_average()

    # All buttons
    average_btn = Button(window, text="DISPLAY AVERAGE", command=display_average)
    clear_btn = Button(window, text="CLEAR", command=clear)
    save_btn = Button(window, text="SAVE", command=save_data)
    import_btn = Button(window, text="IMPORT", command=import_data)
    average_btn.grid(row=len(subjects)//2-1, column=7)
    clear_btn.grid(row=len(subjects)//2+1, column=7)
    save_btn.grid(row=0, column=7)
    import_btn.grid(row=1, column=7)

    window.mainloop()


# GOOD GOOD GOOD & EASY, BUSY, SQUEEZY
