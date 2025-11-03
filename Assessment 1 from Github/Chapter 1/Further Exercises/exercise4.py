staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]
countDict = {}

for name in staff:
    if name in countDict:
        countDict[name] += 1
    else:
        countDict[name] = 1

for key, value in countDict.items():
    print(f"{key}: {value}")