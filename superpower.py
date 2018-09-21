import sys
try:
    list_hero_power_input = input('Please input the heroes\' powers: ').split()
    list_hero_power = []
    for i in list_hero_power_input:
        list_hero_power.append(int(i))
except ValueError:
    print('Sorry, these are not valid power values.')
    exit()

try:
    flip = input('Please input the number of power flips:')
    nb_of_switches = int(flip)
    if nb_of_switches > len(list_hero_power):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    exit()

sum_list = sum(list_hero_power)
list_hero_power_sorted = sorted(list_hero_power)
# 第一问
n = nb_of_switches
sum_q1 = 0
past = 0
if len(list_hero_power_sorted) == 1:
    if n%2 == 0:
        sum_q1 = list_hero_power_sorted[0]
    else:
        sum_q1 = -1 * list_hero_power_sorted[0]
else:
    for i in list_hero_power_sorted:
        if n > 0:
            if i < 0:
                sum_q1 = sum_q1 + i*-1
                n -= 1
            elif i == 0:
                n = 0
            elif n % 2 == 0:
                sum_q1 = sum_q1 + i
                n = 0
            elif past*-1 > i:
                sum_q1 = sum_q1 - i
                n = 0
            else:
                sum_q1 = sum_q1 + i + 2*past
                n = 0
        else:
            sum_q1 = sum_q1 + i
        past = i

# 第二问
sum_q2 = 0
n = nb_of_switches
for i in list_hero_power_sorted:
    if n == 0:
        break
    sum_q2 = sum_q2 + i
    n -= 1
sum_q2 = sum_list - 2*sum_q2
# 第三问
min_sum_of_hero_q3 = sum_of_hero = sum(list_hero_power[0:nb_of_switches])
for i in range(nb_of_switches, len(list_hero_power)):
    sum_of_hero = list_hero_power[i] + sum_of_hero - list_hero_power[i-nb_of_switches]
    if sum_of_hero < min_sum_of_hero_q3:
        min_sum_of_hero_q3 = sum_of_hero
sum_q3 = sum_list - 2 * min_sum_of_hero_q3

# 第四问
min_sum_of_hero_q4 = 0
i = 0
while i < len(list_hero_power):
    s = 0
    if list_hero_power[i] >= 0:
        i += 1
        continue
    for j in range(i, len(list_hero_power)):
        s = s + list_hero_power[j]
        if s >= 0:
            i = j
            break
        if s < min_sum_of_hero_q4:
            min_sum_of_hero_q4 = s
    i += 1
sum_q4 = sum_list - 2*min_sum_of_hero_q4
print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {sum_q1}.')
print(f'Flipping the power of the same hero at most once, the greatest achievable power is {sum_q2}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum_q3}.')
print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {sum_q4}.')