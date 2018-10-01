
# Task 2
# For each member make his name uppercase
# Each member will be exclude of group after reaching the age of 200 years.
# Add field "load" for each member, which shows percentage of progress
# members = [
#    {'age': 43, 'name': 'Denis'},
#    {'age': 49, 'name': 'Roman'},
#    {'age': 36, 'name': 'Godzilla'},
#    {'age': 47, 'name': 'Spike'},
#    {'age': 31, 'name': 'SuperMan'},
#    {'age': 49, 'name': 'Batman'},
#    {'age': 37, 'name': 'Claus'},
#    {'age': 55, 'name': 'Frank'},
#    {'age': 83, 'name': 'Homer'}
#     ]
# Task 2
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
print('orig     ', members)

for i in members[:]:
    i['name'] = i['name'].upper()
    i['load'] = int(i['age'] / 200 * 100)
    if i['age'] >= 200: members.remove(i)
print('uppercase', members)
