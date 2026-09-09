# import matplotlib.pyplot as plt
# a = [1,2,3,4]
# b= [5,6,7,8]
# c =["r","g","y","b"]
# plt.bar(a,b,color=c)
# plt.show()


# Bar Plot In Matplotlib .........

# import matplotlib.pyplot as plt
# fruit = ["Apples","Banana","Cherry","Mango","Guava"]
# sales = [450,200,350,300,500]
# c =["r","g","y","b","m"]
# plt.bar(fruit,sales, color=c,width=0.4)
# plt.title("Weekly Fruit Sales",fontsize=17)
# plt.xlabel("Fruits",fontsize=17)
# plt.ylabel("Sales",fontsize=17)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# students = ["Ali", "Ahmed", "Sara", "Ayesha"]

# math = [80, 75, 90, 85]
# english = [70, 85, 88, 80]

# x = np.arange(len(students))

# plt.bar(x - 0.2, math, width=0.4, label="Math")
# plt.bar(x + 0.2, english, width=0.4, label="English")

# plt.xticks(x, students)

# plt.title("Student Marks Comparison")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.legend()

# plt.show()

# Create a bar chart showing the marks of 5 students. Add a title and labels for both axes.
# import matplotlib.pyplot as plt
# student = ["ali","asad","saad","hassan","ukasha"]
# marks = [45,67,88,90,56]
# colors = ["red", "yellow", "orange", "blue", "green"]
# plt.barh(student,marks,color= colors)
# plt.title("Student Record")
# plt.xlabel("Student")
# plt.ylabel("Marks")
# plt.show()
