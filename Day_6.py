# import matplotlib.pyplot as plt
# x = [10,20,30,40,50,60]
# plt.boxplot(x,notch=True,vert=False)
# plt.show()

# import matplotlib.pyplot as plt
# student = ["ali","saad","asad"]
# marks = [45,56,78]
# plt.subplot(1,2,1)
# plt.plot(student, marks, marker="o")
# plt.title("Line Plot")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# #
# plt.subplot(1,2,2)
# plt.plot(student, marks, marker="o")
# plt.title("bar Plot")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# sales = [300, 200, 400, 250]
# # First Subplot
# plt.subplot(1, 2, 1)
# plt.bar(fruits, sales)
# plt.title("Fruit Sales Bar Plot")
# # Second Subplot
# plt.subplot(1, 2, 2)
# plt.pie(sales, labels=fruits, autopct="%1.1f%%")
# plt.title("Fruit Sales Pie Chart")
# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 15, 25]

# # 1st Subplot - Line Plot
# plt.subplot(2, 2, 1)
# plt.plot(x, y, marker="o")
# plt.title("Line Plot")

# # 2nd Subplot - Bar Plot
# plt.subplot(2, 2, 2)
# plt.bar(x, y)
# plt.title("Bar Plot")

# # 3rd Subplot - Scatter Plot
# plt.subplot(2, 2, 3)
# plt.scatter(x, y)
# plt.title("Scatter Plot")

# # 4th Subplot - Pie Chart
# plt.subplot(2, 2, 4)
# plt.pie(y, labels=x, autopct="%1.1f%%")
# plt.title("Pie Chart")

# plt.tight_layout()
# plt.show()