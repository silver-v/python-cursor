# Task 4
# Write function that return three values
# 1. Summary age of members.
# 2. The youngest member
# 3. The oldest member.
#

# Task 4
def total_value(tot: list):
    s_age = 0
    for i in tot:
        s_age += (i.get('age'))
    tot.sort(key=lambda x: x['age'])
    mi_age = tot[0].get('name')
    ma_age = tot[-1].get('name')

    return s_age, mi_age, ma_age


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
sum_age, min_age, max_age = total_value(members)
print('\nSummary age :', sum_age, ', youngest member is:', min_age, ', oldest member is:', max_age)

