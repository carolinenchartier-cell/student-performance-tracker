import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("grades.csv")

# Show the data
print("Student Data:")
print(df)

# Calculate average per student
df["average"] = df[["math", "english", "science"]].mean(axis=1)

# Show updated data
print("\nWith averages:")
print(df)

# Class statistics
class_avg = df["average"].mean()
top_student = df.loc[df["average"].idxmax()]

print("\nClass average:", round(class_avg, 2))
print("Top student:", top_student["name"], "-", round(top_student["average"], 2))

# Create a bar chart
plt.bar(df["name"], df["average"])
plt.title("Student Average Grades")
plt.xlabel("Students")
plt.ylabel("Average Grade")
plt.show()

# Save results to a new CSV
df.to_csv("results.csv", index=False)

df = df.sort_values(by="average", ascending=False)
print("\nSorted by performance:")
print(df)