import numpy as np

studentsMarks = np.array([[50,56,70,87,90],
                         [40,30,60,98,12],
                         [46,67,89,39,45],
                         [56,79,38,66,56]])
StudentNames = ["Rahul","Sumit","Rohit","Mohit"]

AvgofStudents = np.mean(studentsMarks,axis=1)
AvgofSub = np.mean(studentsMarks,axis=0)
print("Average marks of each subject:", AvgofSub)
print("Average marks of each student:", AvgofStudents)
print("Highest mark obtained in each subject:",np.max(studentsMarks,axis=0))
"np.argmax() is used to find the index (position) of the largest value in an array."
print("Student with the highest overall average",StudentNames[np.argmax(AvgofStudents)],"with an average of", np.max(AvgofStudents))
