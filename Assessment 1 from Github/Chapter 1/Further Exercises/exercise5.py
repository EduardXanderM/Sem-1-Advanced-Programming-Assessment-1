marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]

ascending = sorted(marks, key=lambda x: x[1])
descending = sorted(marks, key=lambda x: x[1], reverse=True)

print("\nAscending Order: \n")
for subject, score in ascending:
    print(f"{subject} - {score}")

print("\nDescending Order: \n")
for subject, score in descending:
    print(f"{subject} - {score}")