people = [
    {"name": "Thiago", "hobbie": "Games"},
    {"name": "João", "hobbie": "Basketball"},
    {"name": "Mark", "hobbie": "Facebook"}
]

people.sort(key=lambda person: person["name"])
# lambda is putting the function in a single line

print(people)