import sys
import time
from collections import defaultdict
time1 = time.time()
# 输入文件名，判断文件是否存在
try:
    filename = 'test_3_2.txt'
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
interval = 0
max_num = 1
max_num_tmp = 1

# begin-for test
# max_num_list = []
# max_num_list_tmp = []
# end-fof_test

for point in range(1, len(list_pillars)):
    t_interval = list_pillars[point] - list_pillars[point - 1]
    if interval == t_interval:
        max_num_tmp += 1
        # begin-for test
        # max_num_list_tmp.append(list_pillars[point])
        # end-fof_test
    else:
        max_num_tmp = 1
        interval = t_interval
        # begin-for test
        # max_num_list_tmp = [list_pillars[point - 1], list_pillars[point]]
        # end-fof_test
    if max_num_tmp > max_num:
        max_num = max_num_tmp
        # begin-for test
        # max_num_list = max_num_list_tmp
        # end-fof_test

if (max_num + 1) == len(list_pillars):
    print('The ride is perfect!')
else:
    print('The ride could be better...')


max_length = 2

# begin-for test
# dif = list_pillars[1] - list_pillars[0]
# last = 1
# end-fof_test

dict_series = defaultdict(lambda: 2)
for j in range(0, len(list_pillars), 1):
    i, k = j - 1, j + 1
    while i >= 0 and k <= len(list_pillars)-1:
        if list_pillars[j] - list_pillars[i] < list_pillars[k] - list_pillars[j]:
            i -= 1
        elif list_pillars[j] - list_pillars[i] > list_pillars[k] - list_pillars[j]:
            k += 1
        else:
            dict_series[(j, k)] = dict_series[(i, j)] + 1
            if dict_series[(j, k)] > max_length:
                # begin-for test
                # last = k
                # dif = list_pillars[k] - list_pillars[j]
                # end-fof_test
                max_length = dict_series[(j, k)]
            k += 1
# begin-for test
# l_dif = []
# last = list_pillars[last]
# for i in range(max_length):
#     l_dif.append(last)
#     last = last - dif
# print(f'\n总长度：{len(list_pillars)}\n')
# print(f'连续数列（{len(max_num_list)}）：\n{max_num_list}\n')
# print(f'最长数列（{len(l_dif)}）：\n{l_dif[::-1]}\n')
# end-fof_test
print(f'The longest good ride has a length of: {max_num}')
print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {len(list_pillars)-max_length}')
time2 = time.time()
print(time2-time1)