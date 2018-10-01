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
#
# Task 3
# Left only those members who have letter 'o' in names.
#
# Task 4
# Write function that return three values
# 1. Summary age of members.
# 2. The youngest member
# 3. The oldest member.
#
# Task 5
# Sort members by length of their names. If length of names is equal than sort by age.
#
# Advanced
# Task 6
# Write function that will convert decimal values to Roman Numerals


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

# Task 3
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
for i in members[:]:
    if not ('o' in i['name']):
        members.remove(i)
print('\nleft members with "o"', members)


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


# Task 6
rome_dig_dic = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}


def conv_to_rome (rom_dig: dict, ar_dig: int):

    assert ar_dig != 0 and ar_dig < 3999
    rom_dig = ''

    if ar_dig / 1000>=1:
        rom_dig += rome_dig_dic[1000] * (ar_dig // 1000)
        ar_dig = ar_dig % 1000

    if ar_dig / 500 >= 1:
        if ar_dig / 900 >= 1:
            rom_dig += rome_dig_dic[100] + rome_dig_dic[1000]
            ar_dig = ar_dig % 900
        else:
            rom_dig += rome_dig_dic[500] * (ar_dig // 500)
            ar_dig = ar_dig % 500

    if ar_dig / 100 >= 1:
        if ar_dig / 400 >= 1:
            rom_dig += rome_dig_dic[100] + rome_dig_dic[500]
            ar_dig = ar_dig % 400
        else:
            rom_dig += rome_dig_dic[100] * (ar_dig // 100)
            ar_dig = ar_dig % 100

    if ar_dig / 50 >= 1:
        if ar_dig / 90 >= 1 :
            rom_dig += rome_dig_dic[10] + rome_dig_dic[100]
            ar_dig = ar_dig % 90
        else:
            rom_dig += rome_dig_dic[50] * (ar_dig // 50)
            ar_dig = ar_dig % 50

    if ar_dig / 10 >= 1:
        if 5 > ar_dig / 10 >= 4:
            rom_dig += rome_dig_dic[10] + rome_dig_dic[50]
            ar_dig = ar_dig % 40
        else:
            rom_dig += rome_dig_dic[10] * (ar_dig // 10)
            ar_dig = ar_dig % 10

    if ar_dig / 5 >= 1:
        if ar_dig % 5 == 0:
            rom_dig += rome_dig_dic[5]
        if ar_dig % 5 == 4:
            rom_dig += rome_dig_dic[1] + rome_dig_dic[10]
        if 0 < ar_dig % 5 < 4:
            rom_dig += rome_dig_dic[5] + rome_dig_dic[1] * (ar_dig % 5)
    if ar_dig / 5 < 1:
        if ar_dig % 5 == 4:
            rom_dig += rome_dig_dic[1] + rome_dig_dic[5]
        else:
            rom_dig += rome_dig_dic[1] * (ar_dig % 5)






    return rom_dig


for i in range (1,101,10):
    print('dec', i, 'rome' ,conv_to_rome(rome_dig_dic, i))