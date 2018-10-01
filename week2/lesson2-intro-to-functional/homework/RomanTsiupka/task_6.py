# Advanced
# Task 6
# Write function that will convert decimal values to Roman Numerals

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