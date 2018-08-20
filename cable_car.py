import sys

# 输入文件名，判断文件是否存在
try:
    filename = 'cable_car.txt'
    # filename = input('Please enter the name of the file you want to get data from: ')
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f'Sorry, there is no such file.')
    sys.exit()

text = ''.join(line.replace('\n', ' ') for line in lines)
print(text)

try:
    # 字符转换成整数
    list_pillars = []
    past = 0
    for i in text.split():
        now = int(i)
        if now <= past:
            raise ValueError
        past = now
        list_pillars.append(now)
    #数列大于等于2
    if len(list_pillars) < 2:
        raise ValueError
    print(list_pillars)
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()

# 最长good ride
sentry = 0
interval = 0
max_num = 1
max_num_tmp = 1
for point in range(1, len(list_pillars)):
    t_interval = list_pillars[point] - list_pillars[point - 1]
    if interval == t_interval:
        max_num_tmp += 1
    else:
        sentry = point - 1
        max_num_tmp = 1
        interval = t_interval
    if max_num_tmp > max_num:
        max_num = max_num_tmp

if (max_num + 1) == len(list_pillars):
    print('The ride is perfect!')
else:
    print('The ride could be better...')

max_length = 2
dict_series = dict()
for j in range(len(list_pillars) - 2, 0, -1):
    i, k = j - 1, j + 1
    while i >= 0 and k < len(list_pillars):
        if list_pillars[j] - list_pillars[i] < list_pillars[k] - list_pillars[j]:
            i -= 1
        elif list_pillars[j] - list_pillars[i] > list_pillars[k] - list_pillars[j]:
            k += 1
        else:
            dict_series[(i, j)] = dict_series.setdefault((j, k), 2) + 1
            if dict_series[(i, j)] > max_length:
                max_length = dict_series[(i, j)]
            i -= 1

print(f'The longest good ride has a length of: {max_num}')
print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {len(list_pillars)-max_length}')
