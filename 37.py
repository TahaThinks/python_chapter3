people = ["Taha younger self", "Hassouna", "Hussein", "Turkei", "Najla", "Ahmed Abdelazim", "Hussam", "Fatin"]

print("Bad News Everyone, one '2 person' can attend")

person = people.pop()
print(f"Sorry {person}, we can't have you")
person = people.pop()
print(f"Sorry {person}, we can't have you")
person = people.pop()
print(f"Sorry {person}, we can't have you")
person = people.pop()
print(f"Sorry {person}, we can't have you")
person = people.pop()
print(f"Sorry {person}, we can't have you")
person = people.pop()
print(f"Sorry {person}, we can't have you")

print(people)
print(f"Now {people[0]} is invited")
print(f"Now {people[1]} is invited")
del people[1]
del people[0]

print(people)