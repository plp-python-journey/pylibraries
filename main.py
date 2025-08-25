#practice exercises
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#pandas
data = {
    'name': ['charles','james','fuhad'],
    'age' : [16,17,18],
    'grade' :[34,70,93]
}

df = pd.DataFrame(data)
print(df)
df['passed']= df['grade']>50
print(df)
passed=df[df['passed']]
print(passed)
plt.plot(df['age'], df['grade'], marker='x')
plt.title("User Growth Over Time")
plt.xlabel("age")
plt.ylabel("grade")
plt.grid(True)
plt.show()

#numpy
my_array = np.arange(10,50)
print(my_array)

print("Max Value:", np.max(my_array))
print("Min Value:", np.min(my_array))

print("My Array * 3:", my_array*3)