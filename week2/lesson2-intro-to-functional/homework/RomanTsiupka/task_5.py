# Task 5
# Sort members by length of their names. If length of names is equal than sort by age.

# Task 5
members = [
    {'age': 43, 'name': 'Denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'Spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'Claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'Homer'}
]
members = sorted(members, key = lambda i: (len(i['name']), i['age']))
print('\nsort by len(name)', members)
print ('\n')

