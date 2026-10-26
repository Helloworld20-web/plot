import matplotlib.pyplot as plt
import random as r

subjects = ["Science", "Math", "History", "Geography", "Literature"]

while True:
    intty = int(input("Enter number: "))
    scores = [r.randint(1, intty), r.randint(1, intty), r.randint(1, intty), r.randint(1, intty), r.randint(1, intty)]
    
    plt.plot(subjects, scores, color='purple', linestyle ='--', marker='d', linewidth=0.5)
    plt.title("Scores on Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Scores")
    plt.show()

    plt.bar(subjects, scores, color='purple')
    plt.title("Scores on Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Scores")
    plt.show()