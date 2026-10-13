print("PROGRAM STARTED")

import pandas as pd
import matplotlib.pyplot as plt 

print("PANDAS IMPORTED")

data = {
    "Student": ["Ali", "Sara", "Ahmed", "Zoya", "Rehan"],
    "Study_Hours": [2, 5, 7, 4, 6],
    "Attendance": [65, 80, 90, 75, 85],
    "Marks": [45, 72, 88, 65, 80]
}

df = pd.DataFrame(data)
print(df)

#average marks 
print("Average Marks:",df["Marks"].mean())

#Bar chart
plt.bar(df["Student"],df["Marks"])

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student_marks.png")
plt.savefig("/home/syedmuzzammil2006/student_marks.png")
plt.close()

print("Graph saved!")

#scatter Plot
plt.scatter(df["Study_Hours"],df["Marks"])

plt.xlabel("Study_Hours")
plt.ylabel("Marks")
plt.title("Study Hours vd Marks")
plt.grid()

plt.savefig("/home/syedmuzzammil2006/study_vsmarks.png")
plt.close()

print("Scatter plot saved successfully!")