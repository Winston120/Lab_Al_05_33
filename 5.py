import csv
import numpy
import statistics
import copy


# Преобразование стоки в число
def str_to_int(str1):
    try:
        return int(str1)
    except:
        if ',' in str1:
            str1 = str1.replace(',', '.')
            return float(str1)
        else:
            return False

        # Замена ошибок


def correction(numbers, eror, replacement):
    beautiful_arr = list(numbers)
    for i in range(len(eror)):
        p = eror[i] - 1
        beautiful_arr.insert(p, replacement)
    return beautiful_arr


# Нормализация
def normalization(min_value, max_value, column_average):
    normal_arr = list(column_average)
    difference = max_value - min_value
    for i in range(len(normal_arr)):
        normal_arr[i] = round(((normal_arr[i] - min_value) / difference), 3)
    return normal_arr


# Запись нового файла
def notation(table, name):
    f = open(name, 'w')
    k = 0
    f.write(str + '\n')
    for j in range(30):
        f.write(name_line[j] + '\t')
        while k < 5:
            tmp = '{}'.format(table[k][j])
            tmp = tmp.replace('.', ',')
            f.write(tmp + '\t')
            k = k + 1
        k = 0
        f.write('\n')
    f.close()


# Запись файла метрики
def notation_one(table, name):
    f = open(name, 'w')
    k = 0
    f.write(str + '\n')
    for j in range(30):
        f.write(name_line[j] + '\t')
        while k < 5:
            tmp = '{}'.format(table[j][k])
            tmp = tmp.replace('.', ',')
            f.write(tmp + '\t')
            k = k + 1
        k = 0
        f.write('\n')
    f.close()


# Метрика
def manhattan_distance(eror_value, number_line):
    tmp_line_eror = list(horizontal_arr[number_line])
    distance = 0
    min_distance = 100000
    for index_line in range(len(horizontal_arr)):
        if index_line != number_line:
            tmp_line = list(horizontal_arr[index_line])
            if 'N/A' not in tmp_line:
                value_tmp = 0
                for value_tmp in range(len(tmp_line)):
                    if value_tmp not in eror_value:
                        distance = distance + abs(tmp_line_eror[value_tmp] - tmp_line[value_tmp])
                if distance < min_distance:
                    min_distance = copy.copy(distance)
                    for eror in eror_value:
                        horizontal_arr[number_line][eror] = tmp_line[eror]
        distance = 0


numbers = []
eror = []
name_lines = []
table_average = []
table_moda = []
table_mediana = []
table_normal = []
eror_value = []

with open("Base.txt") as f:
    data = [row for row in csv.reader(f, delimiter='\t')]
name = data[0]
name_line = []
str = '\t'.join(name)

name_file_average = 'TabSA.txt'
name_file_moda = 'TabMODA.txt'
name_file_mediana = 'TabMD.txt'
name_file_normal = 'TabNorm.txt'
name_file_manhattan = 'Tabmetrics.txt'

for i in range(len(data[0])):
    for j in range(len(data)):
        if i == 0 and j != 0:
            number = data[j][i]
            name_line.append(number)

horizontal_arr = list(data[1:])
for i in range(len(horizontal_arr)):
    horizontal_arr[i] = horizontal_arr[i][1:]
    for j in range(len(horizontal_arr[i])):
        tmp = str_to_int(horizontal_arr[i][j])
        if tmp != False:
            horizontal_arr[i][j] = tmp
number_line = 0
for i in range(len(horizontal_arr)):
    tmp = horizontal_arr[i]
    for j in range(len(tmp)):
        if 'N/A' == tmp[j]:
            number_line = i
            eror_value.append(j)
    if len(eror_value) > 0:
        manhattan_distance(eror_value, number_line)
    eror_value = []
notation_one(horizontal_arr, name_file_manhattan)

for i in range(len(data[0])):
    for j in range(len(data)):
        number = data[j][i]
        tmp = str_to_int(number)
        if tmp != False:
            numbers.append(tmp)
        else:
            if j != 0:
                eror.append(j)
    l = len(numbers)
    if l > 0:
        average = round(numpy.mean(numbers), 1)
        column_average = correction(numbers, eror, average)
        min_value = min(column_average)
        max_value = max(column_average)
        table_normal.append(normalization(min_value, max_value, column_average))
        table_average.append(column_average)
        mode = (statistics.mode(numbers))
        middle = statistics.median(numbers)
        table_moda.append(correction(numbers, eror, mode))
        table_mediana.append(correction(numbers, eror, middle))
    eror = []
    numbers = []

notation(table_average, name_file_average)
notation(table_moda, name_file_moda)
notation(table_mediana, name_file_mediana)
notation(table_normal, name_file_normal)
