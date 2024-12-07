import sys

def is_valid(current, test_value, nums):
    if len(nums) == 0:
        return current == test_value

    added = current + nums[0]
    multiplied = current * nums[0]
    return is_valid(added, test_value, nums[1:]) or is_valid(multiplied, test_value, nums[1:])

total = 0

for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    test_value, nums = line.split(": ")
    test_value = int(test_value)
    nums = [int(i) for i in nums.split(" ")]
    if is_valid(nums[0], test_value, nums[1:]):
        total += test_value

print(total)

