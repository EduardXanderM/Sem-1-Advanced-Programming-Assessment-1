year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

print(year[-3])
print(f"Normal Tuple: {year}")
print(f"Reversed Tuple: {tuple(reversed(year))}")
print(f"The year 2009 was mentioned {year.count(2009)} times")
print(f"The index value of 2018 is {year.index(2018)}")
print(f"The length of this tuple is {len(year)}")