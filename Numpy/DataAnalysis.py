import numpy as np

studentsMarks = np.array([
    [50, 56, 70, 87, 90],
    [40, 30, 60, 98, 12],
    [46, 67, 89, 39, 45],
    [56, 79, 38, 66, 56]
])

studentNames = ["Rahul", "Sumit", "Rohit", "Mohit"]

OverallAvg = np.mean(studentsMarks)
AvgofeachStudent = np.mean(studentsMarks, axis=1)

"Find which students have an average greater than the overall average."

Answer = np.where(AvgofeachStudent > OverallAvg)
print("Overall average of all students:", OverallAvg)
print("Average marks of each student:", AvgofeachStudent)
print("Students with average greater than overall average:", studentNames[Answer[0][0]],"with avg",AvgofeachStudent[Answer[0][0]] ,studentNames[Answer[0][1]],"with avg",AvgofeachStudent[Answer[0][1]] )