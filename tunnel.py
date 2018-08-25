import sys
from collections import deque
try:
    filename = 'test_4.txt'
    # filename = input('Please enter the name of the file you want to get data from: ')
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f'Sorry, there is no such file.')
    sys.exit()

list_blocks = []
try:
    for line in lines:
        line = line.replace('\n', '')
        if len(line) != 0:
            int_list = []
            for i in line.split():
                int_list.append(int(i))
            list_blocks.append(int_list)
    # 每行的情况
    # print(list_blocks)
    # 严格两行
    if len(list_blocks) == 2:
        # 每行个数相等，且大于等于二
        if len(list_blocks[0]) == len(list_blocks[1]) >= 2:
            high = list_blocks[0]
            low = list_blocks[1]
        else:
            # print('每行个数不相等或个数小于2')
            raise ValueError
    else:
        # print('行数不为2')
        raise ValueError
except ValueError:
    print('Sorry, input file does not store valid data.')
    exit()

max_num = 0
source = -1
source_state = 0
deque_celling = deque([(high[0], 0)])
deque_floor = deque([(low[0], 0)])

try:
    for point in range(0, len(low)):
        # 上一列严格大于下一列
        if high[point] <= low[point]:
            raise ValueError

        block_celling = deque_celling.pop()
        block_floor = deque_floor.pop()

        # 上方 去除大于等于当前块的块
        if block_celling[0] >= high[point]:
            for _ in range(0, len(deque_celling)):
                t = deque_celling.pop()
                if t[0] < high[point]:
                    deque_celling.append(t)
                    break
        else:
            deque_celling.append(block_celling)
        deque_celling.append((high[point], point))

        # 下方 去除小于等于当前块的块
        if block_floor[0] <= low[point]:
            for _ in range(0, len(deque_floor)):
                t = deque_floor.pop()
                if t[0] > low[point]:
                    deque_floor.append(t)
                    break
        else:
            deque_floor.append(block_floor)
        deque_floor.append((low[point], point))

        for floor in reversed(deque_floor):
            #保证source所取的是最靠右的数
            if floor[0] >= high[point] and floor[1] > source:
                source = floor[1]
                break

        for celling in reversed(deque_celling):
            if celling[0] <= low[point] and celling[1] > source:
                source = celling[1]
                break
        t_max_num = deque_celling[-1][1] - source
        if max_num < t_max_num:
            if source == -1:
                first_max_num = t_max_num
            max_num = t_max_num
except ValueError:
    print('Sorry, input file does not store valid data.')
    exit()
print(f'From the west, one can see into the tunnel over a distance of {first_max_num}.')
print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {max_num}.')