# coding=utf-8
import sys

# 读取文件的
with open('monthly_csv.csv') as f:
    lines = f.readlines()[1:5]

print(lines)
lines_p = []
for i in lines:
    lines_p.append(i.replace('\n', ''))

