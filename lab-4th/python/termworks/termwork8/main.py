'''

Experiment– 8 (NumPy, Pandas, Matplotlib) 
Problem Statement: Exam score Analysis and Visualization
An exam has been conducted for a class of students. The exam data is stored in a CSV file,
containing the student names and their scores.
Develop a Python program to analyse the exam scores, calculate key statistics, and
visualize the data to gain insights into the students' performance.

'''

# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calculate_statistics(data):
    return np.mean(data['Score']), np.max(data['Score']), np.min(data['Score']), len(data)

def create_visualizations(data):
    # Histogram of exam scores
    plt.figure(figsize=(4, 4))
    plt.hist(data['Score'], bins=10, edgecolor='black')
    plt.xlabel('score')
    plt.ylabel('Frequency')
    plt.title('Exam score Distribution')
    plt.show()

    # Bar chart for top-performing students
    top_students = data[data['Score'] >= 90]
    plt.figure(figsize=(4, 4))
    plt.bar(top_students['Name'], top_students['Score'], color='green')
    plt.xlabel('Student Name')
    plt.ylabel('Score')
    plt.title('Top-performing Students')
    plt.xticks(rotation=45)
    plt.show()

# Main function to execute the program
def main():
    exam_data=pd.read_csv("scores.csv")
    avg_score, max_score, min_score, num_students = calculate_statistics(exam_data)
    print("Average score:", avg_score)
    print("Maximum score:", max_score)
    print("Minimum score:", min_score)
    print("Number of Students:", num_students)

    create_visualizations(exam_data)

if __name__ == "__main__":
    main()