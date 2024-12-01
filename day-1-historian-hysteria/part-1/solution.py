import sys

left_list = []
right_list = []

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    left_num, right_num = line.split()
    left_list.append(int(left_num))
    right_list.append(int(right_num))

left_list = sorted(left_list)
right_list = sorted(right_list)

total_distance = 0
for left_num, right_num in zip(left_list, right_list):
    total_distance += abs(left_num - right_num)

print(total_distance)

