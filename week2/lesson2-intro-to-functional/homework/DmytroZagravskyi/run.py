from utils.task_2 import makeUppercase
from utils.task_3 import makeLoad
from utils.task_5 import makeStats
from utils.task_6 import makeSort
from utils.task_7 import makeRoman


if __name__ == "__main__":
    members = [
        {'age': 43, 'name': 'Denis'},
        {'age': 49, 'name': 'Roman'},
        {'age': 36, 'name': 'Godzilla'},
        {'age': 47, 'name': 'Spike'},
        {'age': 31, 'name': 'SuperMan'},
        {'age': 49, 'name': 'Batman'},
        {'age': 37, 'name': 'Claus'},
        {'age': 55, 'name': 'Frank'},
        {'age': 83, 'name': 'Homer'},
        {'age': 25, 'name': 'Tom'},
        {'age': 150, 'name': 'Odin'}
    ]

    print('\ntask 1 - initial data')
    print(members)

    #task2
    print('\ntask 2 - uppercase')
    for dic in members: dic['name'] = makeUppercase(dic['name'])
    print(members)

    #task3
    print('\ntask 3 - load%')
    for dic in members: dic['load'] = makeLoad(dic['age'])
    print(members)

    #task4
    print('\ntask 4 - filter by ''o''')
    print(list(filter(lambda d: 'o' in d['name'].lower(), members)))

    #task5
    print('\ntask 5 - sum age, 1st/last members')
    print(makeStats(members))

    #task6
    print('\ntask 6 - sort data')
    print(makeSort(members))

    #task7
    print('\ntask 7 - roman num')
    print(makeRoman(6))
    print(makeRoman(13))
