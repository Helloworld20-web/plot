import matplotlib.pyplot as plt

subjects = ["Science", "Math", "History", "Geography", "Literature", "Mi", "Uhhh", "aRgdgdhhd"]
scores = [93, 98, 74, 89, 97, 5010000000, 60000, 6738224]

plt.plot(subjects, scores, color='purple', linestyle ='dashed', marker='d', linewidth=0.5)
plt.title("Scores on Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.ylim(0, 100)
plt.show()

plt.bar(subjects, scores, color='purple')
plt.title("Scores on Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.ylim(0, 100)
plt.show()