import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_stat(data) :
    print("Score Statistics : ")
    print("Avg ", np.average(data['Score']))
    print("Max ", np.max(data['Score']))
    print("Min ", np.min(data['Score']))
    print("Mean ", np.mean(data['Score']))
    print("Count ", len(data))

def draw_visual(data) :
    plt.figure(figsize=(4,4))
    plt.hist(data["Score"], bins=10)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title("Score histogram")
    plt.show()

    plt.figure(figsize=(4,4))
    max_scores = data[data["Score"] >= 90]
    plt.bar(max_scores["Name"], max_scores["Score"])
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Top Performance")
    plt.show()

if __name__ == "__main__" :
    scores = pd.read_csv("scores.csv")
    calculate_stat(scores)
    draw_visual(scores)