import sys
import time
time1 = time.time()
def lines_handler(lines):
    t_lines = []
    # 将每行的数字转换成int
    for line in lines:
        line = line.replace('\n', '').split()
        t_line = []
        for i in line:
            t_line.append(int(i))
        t_lines.append(t_line)
        length_first_line = len(t_lines[0])
        # 如果当前行数的个数和第一行不相同，抛出异常
        if len(t_line) != length_first_line:
            raise ValueError
    if len(t_lines[0]) == 0:
        raise ValueError
    return t_lines


# 输入文件名，判断文件是否存在
try:
    filename = 'land.txt'
    # filename = input('Which data file do you want to use? ')
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f'There is no file named {filename}.')
    sys.exit()

# 判断文件内数据是否符合要求
try:
    lines = lines_handler(lines)
except ValueError:
    print('Content of file is not correct')
    sys.exit()

# 输入雨量，判断是否符合要求
try:
    rain = 80
    # rain = int(input('How many decilitres of water do you want to pour down? '))
    if rain<0:
        raise ValueError
except ValueError:
    print('Please input a nonnegative integer.')
    sys.exit()

#雨量
water = 100 * rain
# 底面积
num_bottom = 0
dict_block = dict()

# 遍历lines，求各高度的块的个数
for line in lines:
    for i in line:
        dict_block[i] = dict_block.setdefault(i, 0) + 1
        num_bottom += 1

dict_block_sorted = sorted(dict_block.items())
print(dict_block_sorted)
last = (0, 0, 0)
height = 0
area = last[1]

if water == 0:
    height = dict_block_sorted[0][0]
else:
    for i in dict_block_sorted:
        v = (i[0]-last[0])*area*100
        if water <= v:
            height = height + water/(area*100)
            water = 0
            break
        water = water - v
        height = height + i[0]-last[0]
        area = area + i[1]
        now = (i[0], area, v)
        last = now
    if water != 0:
        height = height + water/(num_bottom*100)

print(f'The water rises to {height:.2f} centimetres.')
time2 = time.time()
print(time2-time1)