import sys

left_frequencies = {}
right_frequencies = {}

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    left_num, right_num = [int(num) for num in line.split()]
    left_frequencies[left_num] = left_frequencies.get(left_num, 0) + 1
    right_frequencies[right_num] = right_frequencies.get(right_num, 0) + 1

similarity_score = 0
for left_num, frequency in left_frequencies.items():
    similarity_score += left_num * right_frequencies.get(left_num, 0) * frequency

print(similarity_score)

